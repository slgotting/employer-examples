<script>

    import { fade } from 'svelte/transition';
    import Tooltip from "./Tooltip.svelte";

    export let example = false
    export let size = "h-4 w-4";
    export let tooltipPos = 'top'


</script>


{#if example}
    <svelte:self>
        <div in:fade|local={{duration: 400}}
             class="dark:bg-slate-800 bg-white px-4 py-2
                    rounded-md max-w-xs shadow-4">
            <div class="text-sm">
                This is my lidl tooltip
            </div>
        </div>
    </svelte:self>
{:else}

<Tooltip tooltipPos="{tooltipPos}">
    <span slot="element">
        <svg xmlns="http://www.w3.org/2000/svg" class="{size}" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
    </span>

    <div slot="tooltipDiv" class="z-50">
        <slot />
    </div>
</Tooltip>

{/if}