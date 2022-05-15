ALL_FUNCTIONS = {
	'TIME_SERIES_INTRADAY': {'function': 'TIME_SERIES_INTRADAY', 'symbol': 'IBM', 'interval': '5min', 'outputsize': 'full', 'apikey': 'demo'},
	'TIME_SERIES_INTRADAY_EXTENDED': {'function': 'TIME_SERIES_INTRADAY_EXTENDED', 'symbol': 'IBM', 'interval': '60min', 'slice': 'year1month3', 'adjusted': 'false', 'apikey': 'demo'},
	'TIME_SERIES_DAILY': {'function': 'TIME_SERIES_DAILY', 'symbol': 'IBM', 'outputsize': 'full', 'apikey': 'demo'},
	'TIME_SERIES_DAILY_ADJUSTED': {'function': 'TIME_SERIES_DAILY_ADJUSTED', 'symbol': 'IBM', 'outputsize': 'full', 'apikey': 'demo'},
	'TIME_SERIES_WEEKLY': {'function': 'TIME_SERIES_WEEKLY', 'symbol': 'IBM', 'apikey': 'demo'},
	'TIME_SERIES_WEEKLY_ADJUSTED': {'function': 'TIME_SERIES_WEEKLY_ADJUSTED', 'symbol': 'IBM', 'apikey': 'demo'},
	'TIME_SERIES_MONTHLY': {'function': 'TIME_SERIES_MONTHLY', 'symbol': 'IBM', 'apikey': 'demo'},
	'TIME_SERIES_MONTHLY_ADJUSTED': {'function': 'TIME_SERIES_MONTHLY_ADJUSTED', 'symbol': 'IBM', 'apikey': 'demo'},
	'GLOBAL_QUOTE': {'function': 'GLOBAL_QUOTE', 'symbol': 'IBM', 'apikey': 'demo'},
	'SYMBOL_SEARCH': {'function': 'SYMBOL_SEARCH', 'keywords': 'tesco', 'apikey': 'demo'},
	'OVERVIEW': {'function': 'OVERVIEW', 'symbol': 'IBM', 'apikey': 'demo'},
	'EARNINGS': {'function': 'EARNINGS', 'symbol': 'IBM', 'apikey': 'demo'},
	'INCOME_STATEMENT': {'function': 'INCOME_STATEMENT', 'symbol': 'IBM', 'apikey': 'demo'},
	'BALANCE_SHEET': {'function': 'BALANCE_SHEET', 'symbol': 'IBM', 'apikey': 'demo'},
	'CASH_FLOW': {'function': 'CASH_FLOW', 'symbol': 'IBM', 'apikey': 'demo'},
	'LISTING_STATUS': {'function': 'LISTING_STATUS', 'date': '2014-07-10', 'state': 'delisted', 'apikey': 'demo'},
	'EARNINGS_CALENDAR': {'function': 'EARNINGS_CALENDAR', 'symbol': 'IBM', 'horizon': '12month', 'apikey': 'demo'},
	'IPO_CALENDAR': {'function': 'IPO_CALENDAR', 'apikey': 'demo'},
	'CURRENCY_EXCHANGE_RATE': {'function': 'CURRENCY_EXCHANGE_RATE', 'from_currency': 'BTC', 'to_currency': 'CNY', 'apikey': 'demo'},
	'FX_INTRADAY': {'function': 'FX_INTRADAY', 'from_symbol': 'EUR', 'to_symbol': 'USD', 'interval': '5min', 'outputsize': 'full', 'apikey': 'demo'},
	'FX_DAILY': {'function': 'FX_DAILY', 'from_symbol': 'EUR', 'to_symbol': 'USD', 'outputsize': 'full', 'apikey': 'demo'},
	'FX_WEEKLY': {'function': 'FX_WEEKLY', 'from_symbol': 'EUR', 'to_symbol': 'USD', 'apikey': 'demo'},
	'FX_MONTHLY': {'function': 'FX_MONTHLY', 'from_symbol': 'EUR', 'to_symbol': 'USD', 'apikey': 'demo'},
	'CURRENCY_EXCHANGE_RATE': {'function': 'CURRENCY_EXCHANGE_RATE', 'from_currency': 'USD', 'to_currency': 'JPY', 'apikey': 'demo'},
	'CRYPTO_RATING': {'function': 'CRYPTO_RATING', 'symbol': 'BTC', 'apikey': 'demo'},
	'CRYPTO_INTRADAY': {'function': 'CRYPTO_INTRADAY', 'symbol': 'ETH', 'market': 'USD', 'interval': '5min', 'outputsize': 'full', 'apikey': 'demo'},
	'DIGITAL_CURRENCY_DAILY': {'function': 'DIGITAL_CURRENCY_DAILY', 'symbol': 'BTC', 'market': 'CNY', 'apikey': 'demo'},
	'DIGITAL_CURRENCY_WEEKLY': {'function': 'DIGITAL_CURRENCY_WEEKLY', 'symbol': 'BTC', 'market': 'CNY', 'apikey': 'demo'},
	'DIGITAL_CURRENCY_MONTHLY': {'function': 'DIGITAL_CURRENCY_MONTHLY', 'symbol': 'BTC', 'market': 'CNY', 'apikey': 'demo'},
	'SMA': {'function': 'SMA', 'symbol': 'IBM', 'interval': 'weekly', 'time_period': '10', 'series_type': 'open', 'apikey': 'demo'},
	'EMA': {'function': 'EMA', 'symbol': 'IBM', 'interval': 'weekly', 'time_period': '10', 'series_type': 'open', 'apikey': 'demo'},
	'WMA': {'function': 'WMA', 'symbol': 'IBM', 'interval': 'weekly', 'time_period': '10', 'series_type': 'open', 'apikey': 'demo'},
	'DEMA': {'function': 'DEMA', 'symbol': 'IBM', 'interval': 'weekly', 'time_period': '10', 'series_type': 'open', 'apikey': 'demo'},
	'TEMA': {'function': 'TEMA', 'symbol': 'IBM', 'interval': 'weekly', 'time_period': '10', 'series_type': 'open', 'apikey': 'demo'},
	'TRIMA': {'function': 'TRIMA', 'symbol': 'IBM', 'interval': 'weekly', 'time_period': '10', 'series_type': 'open', 'apikey': 'demo'},
	'KAMA': {'function': 'KAMA', 'symbol': 'IBM', 'interval': 'weekly', 'time_period': '10', 'series_type': 'open', 'apikey': 'demo'},
	'MAMA': {'function': 'MAMA', 'symbol': 'IBM', 'interval': 'daily', 'series_type': 'close', 'fastlimit': '0.02', 'apikey': 'demo'},
	'VWAP': {'function': 'VWAP', 'symbol': 'IBM', 'interval': '15min', 'apikey': 'demo'},
	'T3': {'function': 'T3', 'symbol': 'IBM', 'interval': 'weekly', 'time_period': '10', 'series_type': 'open', 'apikey': 'demo'},
	'MACD': {'function': 'MACD', 'symbol': 'IBM', 'interval': 'daily', 'series_type': 'open', 'apikey': 'demo'},
	'MACDEXT': {'function': 'MACDEXT', 'symbol': 'IBM', 'interval': 'daily', 'series_type': 'open', 'apikey': 'demo'},
	'STOCH': {'function': 'STOCH', 'symbol': 'IBM', 'interval': 'daily', 'apikey': 'demo'},
	'STOCHF': {'function': 'STOCHF', 'symbol': 'IBM', 'interval': 'daily', 'apikey': 'demo'},
	'RSI': {'function': 'RSI', 'symbol': 'IBM', 'interval': 'weekly', 'time_period': '10', 'series_type': 'open', 'apikey': 'demo'},
	'STOCHRSI': {'function': 'STOCHRSI', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'series_type': 'close', 'fastkperiod': '6', 'fastdmatype': '1', 'apikey': 'demo'},
	'WILLR': {'function': 'WILLR', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'apikey': 'demo'},
	'ADX': {'function': 'ADX', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'apikey': 'demo'},
	'ADXR': {'function': 'ADXR', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'apikey': 'demo'},
	'APO': {'function': 'APO', 'symbol': 'IBM', 'interval': 'daily', 'series_type': 'close', 'fastperiod': '10', 'matype': '1', 'apikey': 'demo'},
	'PPO': {'function': 'PPO', 'symbol': 'IBM', 'interval': 'daily', 'series_type': 'close', 'fastperiod': '10', 'matype': '1', 'apikey': 'demo'},
	'MOM': {'function': 'MOM', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'series_type': 'close', 'apikey': 'demo'},
	'BOP': {'function': 'BOP', 'symbol': 'IBM', 'interval': 'daily', 'apikey': 'demo'},
	'CCI': {'function': 'CCI', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'apikey': 'demo'},
	'CMO': {'function': 'CMO', 'symbol': 'IBM', 'interval': 'weekly', 'time_period': '10', 'series_type': 'close', 'apikey': 'demo'},
	'ROC': {'function': 'ROC', 'symbol': 'IBM', 'interval': 'weekly', 'time_period': '10', 'series_type': 'close', 'apikey': 'demo'},
	'ROCR': {'function': 'ROCR', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'series_type': 'close', 'apikey': 'demo'},
	'AROON': {'function': 'AROON', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '14', 'apikey': 'demo'},
	'AROONOSC': {'function': 'AROONOSC', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'apikey': 'demo'},
	'MFI': {'function': 'MFI', 'symbol': 'IBM', 'interval': 'weekly', 'time_period': '10', 'apikey': 'demo'},
	'TRIX': {'function': 'TRIX', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'series_type': 'close', 'apikey': 'demo'},
	'ULTOSC': {'function': 'ULTOSC', 'symbol': 'IBM', 'interval': 'daily', 'timeperiod1': '8', 'apikey': 'demo'},
	'ULTOSC': {'function': 'ULTOSC', 'symbol': 'IBM', 'interval': 'weekly', 'apikey': 'demo'},
	'DX': {'function': 'DX', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'apikey': 'demo'},
	'MINUS_DI': {'function': 'MINUS_DI', 'symbol': 'IBM', 'interval': 'weekly', 'time_period': '10', 'apikey': 'demo'},
	'PLUS_DI': {'function': 'PLUS_DI', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'apikey': 'demo'},
	'MINUS_DM': {'function': 'MINUS_DM', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'apikey': 'demo'},
	'PLUS_DM': {'function': 'PLUS_DM', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'apikey': 'demo'},
	'BBANDS': {'function': 'BBANDS', 'symbol': 'IBM', 'interval': 'weekly', 'time_period': '5', 'series_type': 'close', 'nbdevup': '3', 'nbdevdn': '3', 'apikey': 'demo'},
	'MIDPOINT': {'function': 'MIDPOINT', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'series_type': 'close', 'apikey': 'demo'},
	'MIDPRICE': {'function': 'MIDPRICE', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'apikey': 'demo'},
	'SAR': {'function': 'SAR', 'symbol': 'IBM', 'interval': 'weekly', 'acceleration': '0.05', 'maximum': '0.25', 'apikey': 'demo'},
	'TRANGE': {'function': 'TRANGE', 'symbol': 'IBM', 'interval': 'daily', 'apikey': 'demo'},
	'ATR': {'function': 'ATR', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '14', 'apikey': 'demo'},
	'NATR': {'function': 'NATR', 'symbol': 'IBM', 'interval': 'weekly', 'time_period': '14', 'apikey': 'demo'},
	'AD': {'function': 'AD', 'symbol': 'IBM', 'interval': 'daily', 'apikey': 'demo'},
	'ADOSC': {'function': 'ADOSC', 'symbol': 'IBM', 'interval': 'daily', 'fastperiod': '5', 'apikey': 'demo'},
	'OBV': {'function': 'OBV', 'symbol': 'IBM', 'interval': 'weekly', 'apikey': 'demo'},
	'HT_TRENDLINE': {'function': 'HT_TRENDLINE', 'symbol': 'IBM', 'interval': 'daily', 'series_type': 'close', 'apikey': 'demo'},
	'HT_SINE': {'function': 'HT_SINE', 'symbol': 'IBM', 'interval': 'daily', 'series_type': 'close', 'apikey': 'demo'},
	'HT_TRENDMODE': {'function': 'HT_TRENDMODE', 'symbol': 'IBM', 'interval': 'weekly', 'series_type': 'close', 'apikey': 'demo'},
	'HT_DCPERIOD': {'function': 'HT_DCPERIOD', 'symbol': 'IBM', 'interval': 'daily', 'series_type': 'close', 'apikey': 'demo'},
	'HT_DCPHASE': {'function': 'HT_DCPHASE', 'symbol': 'IBM', 'interval': 'daily', 'series_type': 'close', 'apikey': 'demo'},
	'HT_PHASOR': {'function': 'HT_PHASOR', 'symbol': 'IBM', 'interval': 'weekly', 'series_type': 'close', 'apikey': 'demo'},
}

CURRENT_FUNCTIONS = {
	'TIME_SERIES_DAILY_ADJUSTED': {'function': 'TIME_SERIES_DAILY_ADJUSTED', 'symbol': 'IBM', 'outputsize': 'full', 'apikey': 'demo'},
	# 'OVERVIEW': {'function': 'OVERVIEW', 'symbol': 'IBM', 'apikey': 'demo'},
	# 'EARNINGS': {'function': 'EARNINGS', 'symbol': 'IBM', 'apikey': 'demo'},
	# 'INCOME_STATEMENT': {'function': 'INCOME_STATEMENT', 'symbol': 'IBM', 'apikey': 'demo'},
	# 'BALANCE_SHEET': {'function': 'BALANCE_SHEET', 'symbol': 'IBM', 'apikey': 'demo'},
	# 'CASH_FLOW': {'function': 'CASH_FLOW', 'symbol': 'IBM', 'apikey': 'demo'},
	# 'LISTING_STATUS': {'function': 'LISTING_STATUS', 'date': '2014-07-10', 'state': 'delisted', 'apikey': 'demo'},
	# 'IPO_CALENDAR': {'function': 'IPO_CALENDAR', 'apikey': 'demo'},
	# 'CURRENCY_EXCHANGE_RATE': {'function': 'CURRENCY_EXCHANGE_RATE', 'from_currency': 'BTC', 'to_currency': 'CNY', 'apikey': 'demo'},
	# 'FX_INTRADAY': {'function': 'FX_INTRADAY', 'from_symbol': 'EUR', 'to_symbol': 'USD', 'interval': '5min', 'outputsize': 'full', 'apikey': 'demo'},
	# 'FX_DAILY': {'function': 'FX_DAILY', 'from_symbol': 'EUR', 'to_symbol': 'USD', 'outputsize': 'full', 'apikey': 'demo'},
	# 'FX_WEEKLY': {'function': 'FX_WEEKLY', 'from_symbol': 'EUR', 'to_symbol': 'USD', 'apikey': 'demo'},
	# 'FX_MONTHLY': {'function': 'FX_MONTHLY', 'from_symbol': 'EUR', 'to_symbol': 'USD', 'apikey': 'demo'},
	# 'CURRENCY_EXCHANGE_RATE': {'function': 'CURRENCY_EXCHANGE_RATE', 'from_currency': 'BTC', 'to_currency': 'CNY', 'apikey': 'demo'},
	# 'CRYPTO_RATING': {'function': 'CRYPTO_RATING', 'symbol': 'BTC', 'apikey': 'demo'},
	# 'CRYPTO_INTRADAY': {'function': 'CRYPTO_INTRADAY', 'symbol': 'ETH', 'market': 'USD', 'interval': '5min', 'outputsize': 'full', 'apikey': 'demo'},
	# 'DIGITAL_CURRENCY_DAILY': {'function': 'DIGITAL_CURRENCY_DAILY', 'symbol': 'BTC', 'market': 'CNY', 'apikey': 'demo'},
	# 'DIGITAL_CURRENCY_WEEKLY': {'function': 'DIGITAL_CURRENCY_WEEKLY', 'symbol': 'BTC', 'market': 'CNY', 'apikey': 'demo'},
	# 'DIGITAL_CURRENCY_MONTHLY': {'function': 'DIGITAL_CURRENCY_MONTHLY', 'symbol': 'BTC', 'market': 'CNY', 'apikey': 'demo'},
	'SMA': {'function': 'SMA', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'series_type': 'close', 'apikey': 'demo'},
	'EMA': {'function': 'EMA', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'series_type': 'close', 'apikey': 'demo'},
	'WMA': {'function': 'WMA', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'series_type': 'close', 'apikey': 'demo'},
	'DEMA': {'function': 'DEMA', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'series_type': 'close', 'apikey': 'demo'},
	'TEMA': {'function': 'TEMA', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'series_type': 'close', 'apikey': 'demo'},
	'TRIMA': {'function': 'TRIMA', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'series_type': 'close', 'apikey': 'demo'},
	'KAMA': {'function': 'KAMA', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'series_type': 'close', 'apikey': 'demo'},
	'MAMA': {'function': 'MAMA', 'symbol': 'IBM', 'interval': 'daily', 'series_type': 'close', 'fastlimit': '0.02', 'apikey': 'demo'},
	# 'VWAP': {'function': 'VWAP', 'symbol': 'IBM', 'interval': '15min', 'apikey': 'demo'},
	'T3': {'function': 'T3', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'series_type': 'close', 'apikey': 'demo'},
	'MACD': {'function': 'MACD', 'symbol': 'IBM', 'interval': 'daily', 'series_type': 'close', 'apikey': 'demo'},
	'MACDEXT': {'function': 'MACDEXT', 'symbol': 'IBM', 'interval': 'daily', 'series_type': 'close', 'apikey': 'demo'},
	'STOCH': {'function': 'STOCH', 'symbol': 'IBM', 'interval': 'daily', 'apikey': 'demo'},
	'STOCHF': {'function': 'STOCHF', 'symbol': 'IBM', 'interval': 'daily', 'apikey': 'demo'},
	'RSI': {'function': 'RSI', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'series_type': 'close', 'apikey': 'demo'},
	'STOCHRSI': {'function': 'STOCHRSI', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'series_type': 'close', 'fastkperiod': '6', 'fastdmatype': '1', 'apikey': 'demo'},
	'WILLR': {'function': 'WILLR', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'apikey': 'demo'},
	'ADX': {'function': 'ADX', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'apikey': 'demo'},
	'ADXR': {'function': 'ADXR', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'apikey': 'demo'},
	'APO': {'function': 'APO', 'symbol': 'IBM', 'interval': 'daily', 'series_type': 'close', 'fastperiod': '10', 'matype': '1', 'apikey': 'demo'},
	'PPO': {'function': 'PPO', 'symbol': 'IBM', 'interval': 'daily', 'series_type': 'close', 'fastperiod': '10', 'matype': '1', 'apikey': 'demo'},
	'MOM': {'function': 'MOM', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'series_type': 'close', 'apikey': 'demo'},
	'BOP': {'function': 'BOP', 'symbol': 'IBM', 'interval': 'daily', 'apikey': 'demo'},
	'CCI': {'function': 'CCI', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'apikey': 'demo'},
	'CMO': {'function': 'CMO', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'series_type': 'close', 'apikey': 'demo'},
	'ROC': {'function': 'ROC', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'series_type': 'close', 'apikey': 'demo'},
	'ROCR': {'function': 'ROCR', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'series_type': 'close', 'apikey': 'demo'},
	'AROON': {'function': 'AROON', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '14', 'apikey': 'demo'},
	'AROONOSC': {'function': 'AROONOSC', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'apikey': 'demo'},
	'MFI': {'function': 'MFI', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'apikey': 'demo'},
	'TRIX': {'function': 'TRIX', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'series_type': 'close', 'apikey': 'demo'},
	'ULTOSC': {'function': 'ULTOSC', 'symbol': 'IBM', 'interval': 'daily', 'timeperiod1': '8', 'apikey': 'demo'},
	'DX': {'function': 'DX', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'apikey': 'demo'},
	'MINUS_DI': {'function': 'MINUS_DI', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'apikey': 'demo'},
	'PLUS_DI': {'function': 'PLUS_DI', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'apikey': 'demo'},
	'MINUS_DM': {'function': 'MINUS_DM', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'apikey': 'demo'},
	'PLUS_DM': {'function': 'PLUS_DM', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'apikey': 'demo'},
	'BBANDS': {'function': 'BBANDS', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '5', 'series_type': 'close', 'nbdevup': '3', 'nbdevdn': '3', 'apikey': 'demo'},
	'MIDPOINT': {'function': 'MIDPOINT', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'series_type': 'close', 'apikey': 'demo'},
	'MIDPRICE': {'function': 'MIDPRICE', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '10', 'apikey': 'demo'},
	'SAR': {'function': 'SAR', 'symbol': 'IBM', 'interval': 'daily', 'acceleration': '0.05', 'maximum': '0.25', 'apikey': 'demo'},
	'TRANGE': {'function': 'TRANGE', 'symbol': 'IBM', 'interval': 'daily', 'apikey': 'demo'},
	'ATR': {'function': 'ATR', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '14', 'apikey': 'demo'},
	'NATR': {'function': 'NATR', 'symbol': 'IBM', 'interval': 'daily', 'time_period': '14', 'apikey': 'demo'},
	'AD': {'function': 'AD', 'symbol': 'IBM', 'interval': 'daily', 'apikey': 'demo'},
	'ADOSC': {'function': 'ADOSC', 'symbol': 'IBM', 'interval': 'daily', 'fastperiod': '5', 'apikey': 'demo'},
	'OBV': {'function': 'OBV', 'symbol': 'IBM', 'interval': 'daily', 'apikey': 'demo'},
	'HT_TRENDLINE': {'function': 'HT_TRENDLINE', 'symbol': 'IBM', 'interval': 'daily', 'series_type': 'close', 'apikey': 'demo'},
	'HT_SINE': {'function': 'HT_SINE', 'symbol': 'IBM', 'interval': 'daily', 'series_type': 'close', 'apikey': 'demo'},
	'HT_TRENDMODE': {'function': 'HT_TRENDMODE', 'symbol': 'IBM', 'interval': 'daily', 'series_type': 'close', 'apikey': 'demo'},
	'HT_DCPERIOD': {'function': 'HT_DCPERIOD', 'symbol': 'IBM', 'interval': 'daily', 'series_type': 'close', 'apikey': 'demo'},
	'HT_DCPHASE': {'function': 'HT_DCPHASE', 'symbol': 'IBM', 'interval': 'daily', 'series_type': 'close', 'apikey': 'demo'},
	'HT_PHASOR': {'function': 'HT_PHASOR', 'symbol': 'IBM', 'interval': 'daily', 'series_type': 'close', 'apikey': 'demo'},
}