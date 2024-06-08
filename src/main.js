import './assets/main.css'
import {createApp} from 'vue'
import App from './App.vue'
import axios from 'axios'
import {createPinia} from 'pinia'
import router from './router'

axios.default.baseURL = "http://127.0.0.1:8000"
//axios.default.headers.common = {'Authorization': `Bearer ${token}`}
//export default axios;


const app = createApp(App)
const pinia = createPinia();

app.use(router)
app.use(axios)
app.use(pinia)
app.mount('#app')





