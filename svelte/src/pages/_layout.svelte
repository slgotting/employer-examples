<script>
    import { page, metatags } from "@roxi/routify";
    import capitalize from "../lib/string";
    let title = $page.title.replace(/-/g, " ");
    if ($page.title == "index") {
        title = "Home";
    }
    $: metatags.title = capitalize(title) + " - Svelte Tailwind Boilerplate";
</script>


<slot />
