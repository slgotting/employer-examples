from pydantic import ConfigError
import requests
from logger_slg import init_logger
from endpoint_parameters import ALL_FUNCTIONS
import yaml
import time
import json
import datetime


def read_config_file(filepath, logger):
    try:
        with open(filepath, 'r') as stream:
            try:
                config = yaml.safe_load(stream)
                return config
            except yaml.YAMLError as exc:
                print(exc)
                logger.error('\n\nYAML Error. Exiting...')
                exit(0)
    except FileNotFoundError:
        logger.exception('Config file not found. Proceeding with defaults')
        return {}

def read_json_file(filepath, logger):
    try:
        with open(filepath, 'r') as f:
            data = json.loads(f.readlines())
        return data
    except:
        logger.exception('Could not read json from filepath due to unknown error')

def write_json_file(data, filepath, logger):
    try:
        with open(filepath, 'w') as f:
            f.write(json.dumps(data))
    except:
        logger.exception('Could not write to filepath due to unknown error')

class AlphaVantage:
    '''
    api_call_count is how many requests each symbol generally has to run. I'm not going to get granular to the individual call level
    because that is a premature optimization that is unneeded once max_requests is uncapped
    '''

    def __init__(self, config_filepath="", state_file="", log_filepath=f'/var/log/slg/{__file__.split("/")[-1]}.log', api_call_count=74, max_requests=400):
        self.logger = init_logger(
            name=__name__,
            log_path=log_filepath
        )

        self.config = read_config_file(config_filepath, self.logger)
        self.config_filepath = config_filepath
        self.requests_per_minute = self.config.get('requests_per_minute')
        self.state_file = state_file

        # get desired functions with exception handling
        if self.config.get('include_functions') and self.config.get('exclude_functions'):
            raise ConfigError('Both include_functions and exclude_functions were specified. Only one should be.')
        if not self.config.get('include_functions') and not self.config.get('exclude_functions'):
            raise ConfigError('Specify functions to include or exclude from the endpoints')
        if self.config.get('include_functions'):
            self.functions = self.config.get('include_functions')
        else:
            self.functions = [function for function in ALL_FUNCTIONS if function not in self.config.get('exclude_functions')]

    def wait_til_rate_limit_allows(self):
        '''
        This verifies that we will not surpass the rate limit as defined by max_requests.

        self.api_call_count is how many requests each symbol generally has to run

        We're taking the overly simplified approach of current_requests + api_call_count < max_requests
        '''
        while True:
            if self.get_num_requests_on_the_day() + self.api_call_count < self.max_daily_requests:
                return True
            time.sleep(30*60)

    def get_num_requests_on_the_day(self):
        try:
            data = read_json_file(self.state_file, self.logger)
            return data.get(self.get_todays_datetime_str(), 0)
        except:
            self.logger.exception('Error in get_num_requests_on_the_day')

    def set_num_requests_on_the_day(self, request_count):
        try:
            data = read_json_file(self.state_file, self.logger)
            data[self.get_todays_datetime_str()] = request_count
            write_json_file(data, self.state_file, self.logger)
        except:
            self.logger.exception('Error in set_num_requests_on_the_day')

    def increment_todays_num_requests(self):
        curr_num = self.get_num_requests_on_the_day()
        self.set_num_requests_on_the_day(curr_num + 1)

    def get_todays_datetime_str(self):
        return datetime.datetime.utcnow().strftime('%Y-%m-%d')

    def format_datetime_key(self, datetime_str):
        # datetimes for TIME_SERIES_INTRADAY come in like this 2022-02-23 20:00:00
        # datetimes for technical indicators like SMA come in as 2022-04-14 15:00

        #TODO convert this to a datetime.datetime.strptime check to make sure we have an appropriate datetime

        # this formatter may be incomplete for other indicators or datetime keys; I will try to log instances of that
        str_length = len(datetime_str)

        if str_length != 16 and str_length != 19:
            self.logger.error(f'Datetime key "{datetime_str}" came in as unexpected length: {str_length}. Exiting...')
            raise Exception('Datetime key came in as an unexpected length. Exiting')

        return datetime_str[:16]

    def get_all_data(self, symbol):
        '''
        output of this function is an object of form:
         {
          date1: {
              techIndicator1: n,
              techIndicator2: n,
              },
          date2: {
              techIndicator1: n,
              techIndicator2: n,
              },
              etc...
          }
        '''

        output = {}
        for function in self.functions:
            try:
                data = self.get_function_data(symbol, function)
                formatted_data = self.parse_unformatted_data_object(data, function)

                # add our keys to our output; keys here are datetimes
                for datetime_str in formatted_data:
                    key = self.format_datetime_key(datetime_str)
                    if key not in output:
                        output[key] = formatted_data[datetime_str]
                    else:
                        output[key].update(formatted_data[datetime_str])

                self.logger.info(f'Successfully captured function: {function}. Sleeping for {60 / self.requests_per_minute} seconds...')
                time.sleep(60 / self.requests_per_minute)
            except:
                self.logger.exception(f'Exception raised for function {function}')
                time.sleep(60 / self.requests_per_minute)
        return output

    def get_all_data_and_write_output(self, symbol):
        json_data = self.get_all_data()

        # create a suitable filepath/name
        directory = '/'.join(self.config_filepath.split('.')[0].split('/')[:-1])
        filename = self.config_filepath.split('.')[0].split('/')[-1]
        current_dt = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        write_filepath = f'{directory}/{current_dt}-{filename}.json'

        with open(write_filepath, 'w') as f:
            try:
                f.write(json.dumps(json_data))
            except:
                self.logger.exception('Unknown error writing data to file')

    def get_function_data(self, symbol, function):
        qs = self.build_query_string(symbol, function)
        query = 'https://www.alphavantage.co/' + qs
        print(query)
        resp = requests.get(query)
        data = resp.json()
        # self.increment_todays_num_requests()
        return data

    def parse_unformatted_data_object(self, data, function):
        # output is object of form {date: {function: value}, date2: {function: value}}

        def format_data(function, data_obj):
            '''
            This takes in a data_obj that has form:
            {
                "QUADRATURE": "7.1811",
                "PHASE": "-3.0938"
            }

            and converts it to:
            {
                "HT_PHASOR-QUADRATURE": "7.1811",
                "HT_PHASOR-PHASE": "-3.0938"
            }
            if the keys don't match the function name, else the key is just the function name
            '''
            output = {}
            for key in data_obj:
                if key == function:
                    output[key] = data_obj[key]
                else:
                    output[f'{function}-{key}'] = data_obj[key]
            return output

        # Data typically has two keys, "Meta Data" and the other is the data we're looking for.
        # Its variable so we will simply grab the 2nd key in data.keys()
        data_obj_key = list(data.keys())[1]
        new_data = data[data_obj_key]

        output = {datetime_str: format_data(function, data_obj) for datetime_str, data_obj in new_data.items()}
        return output

    def build_query_string(self, symbol, function):
        output = f'query?function={function}&symbol={symbol}'

        overridden = {}
        # apply overrides before anything else
        for parameter, value in self.config.get('parameter_overrides', {}).get(function, {}).items():
            output += f'&{parameter}={value}'
            overridden[parameter] = 1

        # build defaults and append to string
        defaults = {parameter: self.config.get('default_parameter_values').get(parameter) for parameter in ALL_FUNCTIONS[function] if parameter not in overridden and (parameter != 'function' and parameter != 'symbol')}
        for parameter, value in defaults.items():
            output += f'&{parameter}={value}'

        return output
