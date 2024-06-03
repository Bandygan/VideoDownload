import './assets/main.css'
import {createApp} from 'vue'
import App from './App.vue'
import axios from 'axios'

axios.default.baseURL = "http://127.0.0.1:8000"

createApp(App).use(axios).mount('#app');


