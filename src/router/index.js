import {createRouter, createWebHistory} from 'vue-router'
import Home from '../pages/Home.vue'
import User from '../pages/User.vue'




const routes = [
  { path: '/', component: Home },
  { path: '/User', component: User },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
