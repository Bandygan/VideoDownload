import './assets/main.css'
import {createApp} from 'vue'
import App from './App.vue'
import axios from 'axios'
import {createPinia} from 'pinia'
import router from './router'

axios.default.baseURL = "http://127.0.0.1:8000"

const app = createApp(App)
app.use(router)
app.use(axios)
app.use(createPinia)
app.mount('#app')





