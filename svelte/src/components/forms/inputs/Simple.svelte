<script>
    export let componentType = "standard"; // standard, helpText, cornerHint, leadingIcon, trailingIcon, prefixAddon, inlineAddon, doubleAddon, leadingDropdown, trailingDropdown
    export let label = "Email";
    export let description = "Your full email address";
    export let value = "you@example.com";
    export let hint = "Optional"

    export let addonText = "http://";

</script>

{#if componentType == "standard"}
    <div>
        <label for="email" class="block text-sm font-medium text-gray-700 dark:text-gray-200">{@html label}</label>
        <div class="mt-1">
            <input
                bind:value={value}
                type="text"
                class="bg-inherit dark:border-gray-700 shadow-sm focus:ring-primary-500 focus:border-primary-500 block w-full sm:text-sm border-gray-300 rounded-md"
                placeholder={value} />
        </div>
    </div>
{:else if componentType == "helpText"}
    <div>
        <label for="email" class="block text-sm font-medium text-gray-700 dark:text-gray-200">{label}</label>
        <div class="mt-1">
            <input
                type="text"
                class="shadow-sm focus:ring-primary-500 focus:border-primary-500 block w-full sm:text-sm border-gray-300 rounded-md"
                placeholder={value}
                aria-describedby="email-description" />
        </div>
        <p class="mt-2 text-sm text-gray-500" id="email-description">{description}</p>
    </div>
{:else if componentType == "cornerHint"}
    <div>
        <div class="flex justify-between">
            <label for="email" class="block text-sm font-medium text-gray-700 dark:text-gray-200">{label}</label>
            <span class="text-sm text-gray-500" id="email-optional">{hint}</span>
        </div>
        <div class="mt-1">
            <input
                type="text"
                name="email"
                id="email"
                class="shadow-sm focus:ring-primary-500 focus:border-primary-500 block w-full sm:text-sm border-gray-300 rounded-md"
                placeholder={value}
                aria-describedby="email-optional" />
        </div>
    </div>
{:else if componentType == "leadingIcon"}
    <div>
        <label for="email" class="block text-sm font-medium text-gray-700 dark:text-gray-200">{label}</label>
        <div class="mt-1 relative rounded-md shadow-sm">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <!-- Heroicon name: solid/mail -->
                <svg class="h-5 w-5 text-gray-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                    <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z" />
                    <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" />
                </svg>
            </div>
            <input
                type="text"
                name="email"
                id="email"
                class="focus:ring-primary-500 focus:border-primary-500 block w-full pl-10 sm:text-sm border-gray-300 rounded-md"
                placeholder={value} />
        </div>
    </div>
{:else if componentType == "trailingIcon"}
    <div>
        <label for="account-number" class="block text-sm font-medium text-gray-700 dark:text-gray-200">Account number</label>
        <div class="mt-1 relative rounded-md shadow-sm">
            <input
                type="text"
                name="account-number"
                id="account-number"
                class="focus:ring-primary-500 focus:border-primary-500 block w-full pr-10 sm:text-sm border-gray-300 rounded-md"
                placeholder="000-00-0000" />
            <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                <!-- Heroicon name: solid/question-mark-circle -->
                <svg class="h-5 w-5 text-gray-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                    <path
                        fill-rule="evenodd"
                        d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z"
                        clip-rule="evenodd" />
                </svg>
            </div>
        </div>
    </div>
{:else if componentType == "prefixAddon"}
    <div>
        <label for="company-website" class="block text-sm font-medium text-gray-700 dark:text-gray-200"> Company Website </label>
        <div class="mt-1 flex rounded-md shadow-sm">
            <span class="inline-flex items-center px-3 rounded-l-md border border-r-0 border-gray-300 bg-gray-50 text-gray-500 sm:text-sm">{addonText}</span>
            <input
                type="text"
                name="company-website"
                id="company-website"
                class="flex-1 min-w-0 block w-full px-3 py-2 rounded-none rounded-r-md focus:ring-primary-500 focus:border-primary-500 sm:text-sm border-gray-300"
                placeholder="www.example.com" />
        </div>
    </div>
{:else if componentType == "inlineAddon"}
    <div>
        <label for="company-website" class="block text-sm font-medium text-gray-700 dark:text-gray-200">Company Website</label>
        <div class="mt-1 relative rounded-md shadow-sm">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <span class="text-gray-500 sm:text-sm">{addonText}</span>
            </div>
            <input
                type="text"
                name="company-website"
                id="company-website"
                class="focus:ring-primary-500 focus:border-primary-500 block w-full pl-16 sm:pl-14 sm:text-sm border-gray-300 rounded-md"
                placeholder="www.example.com" />
        </div>
    </div>
{:else if componentType == "doubleAddon"}
    <div>
        <label for="price" class="block text-sm font-medium text-gray-700 dark:text-gray-200">Price</label>
        <div class="mt-1 relative rounded-md shadow-sm">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <span class="text-gray-500 sm:text-sm"> $ </span>
            </div>
            <input
                type="text"
                name="price"
                id="price"
                class="focus:ring-primary-500 focus:border-primary-500 block w-full pl-7 pr-12 sm:text-sm border-gray-300 rounded-md"
                placeholder="0.00"
                aria-describedby="price-currency" />
            <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                <span class="text-gray-500 sm:text-sm" id="price-currency"> USD </span>
            </div>
        </div>
    </div>
{:else if componentType == "leadingDropdown"}
    <div>
        <label for="phone-number" class="block text-sm font-medium text-gray-700 dark:text-gray-200">Phone Number</label>
        <div class="mt-1 relative rounded-md shadow-sm">
            <div class="absolute inset-y-0 left-0 flex items-center">
                <label for="country" class="sr-only">Country</label>
                <select
                    id="country"
                    name="country"
                    autocomplete="country"
                    class="focus:ring-primary-500 focus:border-primary-500 h-full py-0 pl-3 pr-7 border-transparent bg-transparent text-gray-500 sm:text-sm rounded-md">
                    <option>US</option>
                    <option>CA</option>
                    <option>EU</option>
                </select>
            </div>
            <input
                type="text"
                name="phone-number"
                id="phone-number"
                class="focus:ring-primary-500 focus:border-primary-500 block w-full pl-16 sm:text-sm border-gray-300 rounded-md"
                placeholder="+1 (555) 987-6543" />
        </div>
    </div>
{:else if componentType == "trailingDropdown"}
    <div>
        <label for="price" class="block text-sm font-medium text-gray-700 dark:text-gray-200">Price</label>
        <div class="mt-1 relative rounded-md shadow-sm">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <span class="text-gray-500 sm:text-sm"> $ </span>
            </div>
            <input
                type="text"
                name="price"
                id="price"
                class="focus:ring-primary-500 focus:border-primary-500 block w-full pl-7 pr-12 sm:text-sm border-gray-300 rounded-md"
                placeholder="0.00" />
            <div class="absolute inset-y-0 right-0 flex items-center">
                <label for="currency" class="sr-only">Currency</label>
                <select
                    id="currency"
                    name="currency"
                    class="focus:ring-primary-500 focus:border-primary-500 h-full py-0 pl-2 pr-7 border-transparent bg-transparent text-gray-500 sm:text-sm rounded-md">
                    <option>USD</option>
                    <option>CAD</option>
                    <option>EUR</option>
                </select>
            </div>
        </div>
    </div>
{/if}
