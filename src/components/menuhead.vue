<template>
  <div class="container-head">

    <nav class="nav-menu">
      <router-link to="/" class="nav-button" :class="{ 'router-link-active': $route.path === '/' }">Home</router-link>
      <router-link to="/user" class="nav-button" :class="{ 'router-link-active': $route.path === '/user' }">User</router-link>
    </nav>

    <div class="container-auth">
      <div ref="telegramLoginWidget"></div>
      <ModalWindow :isOpen="isModalOpen" @close="closeModal"/>
      <LogIn :isOpen="isModalOpen"/>
    </div>
  </div>
</template>

<script>
import ModalWindow from "./modal-window.vue";
import LogIn from "./log-in.vue";
import { useRouter } from "vue-router";
import { useAuthStore } from '../stores/auth';
import { ref } from 'vue';

export default {
  name: "menuhead",

  components: {
    ModalWindow,
    LogIn
  },

  mounted() {
    this.addTelegramWidget();
  },

  methods: {
    addTelegramWidget() {
      const script = document.createElement('script');
      script.async = true;
      script.src = 'https://telegram.org/js/telegram-widget.js?22';
      script.setAttribute('data-telegram-login', 'VideoDownloadTG_bot');
      script.setAttribute('data-size', 'large');
      script.setAttribute('data-auth-url', 'https://da3c-185-57-28-150.ngrok-free.app/auth/complete/telegram');
      script.setAttribute('data-request-access', 'write');

      this.$refs.telegramLoginWidget.appendChild(script);
    }
  },

  setup() {
    const router = useRouter();
    const authStore = useAuthStore();
    const isModalOpen = ref(false);

    const logout = () => {
      authStore.logout();
      router.push('/');
    };

    const closeModal = () => {
      isModalOpen.value = false;
    };

    return {
      logout,
      isModalOpen,
      closeModal
    };
  }
}
</script>

<style scoped>
.container-head {
  width: 100%;
  background-color: #1E1E1E;
  padding: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.5);
  box-sizing: border-box;
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.nav-button {
  background-color: #333;
  border: none;
  padding: 15px 25px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 8px;
  transition-duration: 0.4s;
}

.nav-button:hover {
  background-color: #555;
  color: white;
}

.nav-button:active {
  background-color: #555;
  color: white;
}

.router-link-active {
  background-color: #555;
  color: white;
}

.container-auth {}
</style>
