import "./global.css";
import "./styles/colors.scss";
import "./styles/backgrounds.scss";
import HMR from "@roxi/routify/hmr";
import App from "./App.svelte";

const app = HMR(App, { target: document.body }, "routify-app");

export default app;
