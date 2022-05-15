<script>
    import { fly } from 'svelte/transition';
    export let label = "Assigned to";
    export let options = ['Tom Cook', 'Wade Coop', 'Cooper Kupp'];
    export let open = false;

    export let value;

    export let selectedIdx = options.indexOf(value);
    if (selectedIdx == -1) {
        selectedIdx = 0
    }

    let selectDropdown;

    // remove pointer events if phasing out
    function removePointerEvents(elem) {
        elem.style.pointerEvents = 'none';
    }

    // add pointer events if phasing in
    function addPointerEvents(elem) {
        elem.style.pointerEvents = 'all';
    }

    $: value = options[selectedIdx];
</script>

<div>
    {#if label}
        <label class="block text-sm font-medium text-gray-700 dark:text-gray-200">{label}</label>
    {/if}
    <div class="relative mt-1">
        <button
            type="button"
            on:click={() => (open = !open)}
            class="bg-inherit relative w-full border dark:border-gray-700 border-gray-300 rounded-md shadow-sm pl-3 pr-10 py-2 text-left cursor-default focus:outline-none focus:ring-1 focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            aria-haspopup="listbox"
            aria-expanded="true"
            aria-labelledby="listbox-label">
            <span class="block truncate">{value}</span>
            <span class="absolute inset-y-0 right-0 flex items-center pr-2 pointer-events-none">
                <!-- Heroicon name: solid/selector -->
                <svg class="h-5 w-5 text-gray-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                    <path
                        fill-rule="evenodd"
                        d="M10 3a1 1 0 01.707.293l3 3a1 1 0 01-1.414 1.414L10 5.414 7.707 7.707a1 1 0 01-1.414-1.414l3-3A1 1 0 0110 3zm-3.707 9.293a1 1 0 011.414 0L10 14.586l2.293-2.293a1 1 0 011.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z"
                        clip-rule="evenodd" />
                </svg>
            </span>
        </button>

        {#if open}
            <ul
                bind:this={selectDropdown}
                on:outrostart={removePointerEvents(selectDropdown)}
                on:introstart={addPointerEvents(selectDropdown)}
                in:fly|local={{x:-20, duration:500}}
                out:fly|local={{x:-20, duration:500}}
                class="absolute z-10 mt-1 w-full bg-1 shadow-lg max-h-60 rounded-md py-1 text-base ring-1 ring-black ring-opacity-5 overflow-auto focus:outline-none sm:text-sm"
                tabindex="-1"
                role="listbox"
                aria-labelledby="listbox-label"
                aria-activedescendant="listbox-option-3">

            {#each options as option, i}
                <li
                    on:click={() => {
                        selectedIdx = i;
                        open = false;
                    }}
                    class="cursor-default select-none relative py-2 pl-3 pr-9 hover:bg-primary-600 hover:text-white
                            {selectedIdx == i ? 'dark:text-primary-400 text-primary-600 hover:dark:text-white' : 'text-gray-900 dark:text-gray-50'}"
                    id="listbox-option-0"
                    role="option">

                    <span class="font-normal block truncate">{option}</span>

                    {#if selectedIdx == i}
                    <span class="text-current absolute inset-y-0 right-0 flex items-center pr-4">

                        <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                            <path
                                fill-rule="evenodd"
                                d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                                clip-rule="evenodd" />
                        </svg>
                    </span>
                    {/if}
                </li>
            {/each}
            </ul>
        {/if}
    </div>
</div>
