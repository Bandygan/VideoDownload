import './assets/main.css'
import {createApp} from 'vue'
import App from './App.vue'
import axios from 'axios'
import {createPinia} from 'pinia'
import router from './router'
import { globalCookiesConfig } from "vue3-cookies";

//axios.default.headers.common = {'Authorization': `Bearer ${token}`}
//export default axios;
axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

globalCookiesConfig({
    expireTimes: "30d",
    path: "/",
    domain: "",
    secure: true,
    sameSite: "None",
});

const app = createApp(App)
const pinia = createPinia();

app.use(router)
// app.use(axios)
app.use(pinia)
app.mount('#app')





