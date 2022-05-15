<script>
    import { fade } from "svelte/transition";
    import { createPopperActions } from "svelte-popperjs";
    const [popperRef, popperContent] = createPopperActions();

    const DEFAULTS = {
        'top': {
            placement: 'top',
            modifiers: [{ name: "offset", options: { offset: [0, 8] } }],
        },
        'left': {
            placement: 'left',
            modifiers: [{ name: "offset", options: { offset: [0, 8] } }],
        },
        'right': {
            placement: 'right',
            modifiers: [{ name: "offset", options: { offset: [0, 8] } }],
        },
    }

    export let tooltipPos = 'top';
    let popperOptions

    if (tooltipPos) {
        popperOptions = DEFAULTS[tooltipPos];
    }

    let showTooltip = false;

    export let example = false;
</script>


{#if example}
    <svelte:self tooltipPos="top">
        <button class="" slot="element">Test button</button>
        <div slot="tooltipDiv"
                in:fade|local={{duration: 400}}
                class="dark:bg-slate-800 bg-white px-4 py-2 rounded-md z-50">
            This is the tooltip text!
        </div>
    </svelte:self>

{:else}

<div style="height:fit-content; width:fit-content;" use:popperRef on:mouseenter={() => (showTooltip = true)} on:mouseleave={() => (showTooltip = false)}>
    <slot name="element" />
    {#if showTooltip}
        <div
            use:popperContent={popperOptions}>
            <slot name="tooltipDiv" />
        </div>
    {/if}
</div>

{/if}
