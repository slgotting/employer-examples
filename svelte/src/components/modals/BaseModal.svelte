<!-- <script context="module">
    // export assignment only necessary for example
    let canOpen = true;

    export function openModal() {
		if (canOpen == true) {
            console.log('opening');
            open = true;
			return true
		}
	}
</script> -->


<script>
    import Portal from "../Portal.svelte";
    import { fly } from "svelte/transition";
    import DocumentBackdrop from "../backdrops/DocumentBackdrop.svelte";

    export let position = 'top-center';
    export let example = false;

    export let open = false;
    export let canOpen = true;

    export let openDelay = 0;

    let style;
    let modal;
    let transition = calculateTransition(position);

    // this delay is a hack to allow the element to be actually assigned before calculating its width
    let delay = 20;

    const POSITIONS = {
        'top-left': (translateX, translateY) => `left: 50px; top: 50px;`,
        'top-center': (translateX, translateY) =>  `left: calc(50% - ${translateX}px); top: 50px;`,
        'top-right': (translateX, translateY) => `right: 50px; top: 50px;`,
        'middle-left': (translateX, translateY) => `left: 50px; top: calc(50% - ${translateY}px - 68px);`,
        'middle-center': (translateX, translateY) => `left: calc(50% - ${translateX}px); top: calc(50% - ${translateY}px - 68px);`,
        'middle-right': (translateX, translateY) => `right: 50px; top: calc(50% - ${translateY}px - 68px);`,
        'bottom-left': (translateX, translateY) => `left: 50px; bottom: 50px;`,
        'bottom-center': (translateX, translateY) => `left: calc(50% - ${translateX}px); bottom: 50px;`,
        'bottom-right': (translateX, translateY) => `right: 50px; bottom: 50px;`,
    }

    function setPosition(pos, open, delay) {
        setTimeout(() => {
            let modalWidth;
            let modalHeight;
            let translateX;
            let translateY;
            try {
                modalWidth = modal.offsetWidth;
                modalHeight = modal.offsetHeight;
                translateX = modalWidth / 2;
                translateY = modalHeight / 2;
            } catch {
                translateX = 0;
                translateY = 0;
            }
            style = POSITIONS[pos](translateX, translateY)
        }, delay);
    }

    function handleForOffset() {
        return [0, 0]
    }

    function calculateTransition(position, delay) {
        let trans;
        if (position.split('-')[1] == 'left') {
            trans = {x: -30, duration: 500, delay:delay}
        } else if (position.split('-')[1] == 'right') {
            trans = {x: 30, duration: 500, delay:delay}
        } else if (position == 'top-center') {
            trans = {y: -30, duration: 500, delay:delay}
        } else if (position.split('-')[1] == 'center') {
            trans = {y: 30, duration: 500, delay:delay}
        }
        return trans
    }

    const handleKeydown = e => {
		if (e.key === 'Escape') {
            open = false;
			return;
		}
	};

    $: setPosition(position, open, delay);

    export function openModal() {
        if (canOpen) {
            setTimeout(() => {
                open = true
            }, openDelay);
        }
    }
</script>

<svelte:window on:keydown={handleKeydown}/>

{#if example}

    <button on:click={() => openModal()}>Open Modal</button>
    <svelte:self bind:open={open} bind:canOpen={canOpen}>
        <div class="px-4 py-2 dark:bg-slate-800 bg-white">
            This is an example modal
        </div>
    </svelte:self>

{:else}

    {#if open}
        <Portal>
            <div bind:this={modal}
                in:fly|local={transition}
                out:fly|local={transition}
                on:outrostart="{() => {
                    modal.style.pointerEvents = 'none'
                    canOpen = false
                }}"
                on:outroend="{() => {
                    modal.style.pointerEvents = 'all'
                    canOpen = true
                }}"
                class="modal fixed z-50 shadow-8"
                style="{style}">
                <slot />
            </div>
        </Portal>
    {:else}
        <div bind:this={modal} class="absolute invisible pointer-events-none"><slot /></div>
    {/if}

    <DocumentBackdrop bind:visible={open} />

{/if}

<style>


</style>
