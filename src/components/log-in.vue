<template>
  <button v-if="authenticated" @click="logout" id="log-m">Logout</button>
  <div  :hidden="authenticated" ref="telegramLoginWidget"></div>
</template>

<script setup>
import {computed, getCurrentInstance, onMounted, ref, watch} from 'vue';
import {useAuthStore} from '../stores/auth.js';
import {useRouter} from 'vue-router';
import {useCookies} from "vue3-cookies";

const authStore = useAuthStore();
const router = useRouter();
const { cookies } = useCookies();
const app = getCurrentInstance();

const authenticated = computed(() => authStore.user !== null);
onMounted(() => {
  addTelegramWidget();
})

function logout() {
  authStore.logout();
  router.push('/');
}



function addTelegramWidget() {
  const script = document.createElement('script');
  script.async = true;
  script.src = 'https://telegram.org/js/telegram-widget.js?22';
  script.setAttribute('data-telegram-login', 'VideoDownloadTG_bot');
  script.setAttribute('data-size', 'large');
  script.setAttribute('data-auth-url',
      'https://da3c-185-57-28-150.ngrok-free.app/auth/complete/telegram'
  );
  script.setAttribute('data-request-access', 'write');
  app.refs.telegramLoginWidget.appendChild(script);
}
</script>

<style scoped>
.dialog-box {
  padding: 10px;
  width: 100%;
  max-width: 24rem;
  border-radius: 0.5rem;
  background: #323443;
  border: solid 1px;
}

.modal-back {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.3);
}

.box-modal {
  align-items: center;
  position: fixed;
  display: flex;
  padding: 4px;
  justify-content: center;
  inset: 0;
}

#log-m {
  background: #333333;
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

button {
  background: #272727;
  font-size: 20px;
  border-radius: 50px;
}

input {
  background: #1d1c1c;
  width: 70%;
  border-radius: 10px;
  height: 50px;
  border: 0;
  font-size: 20px;
}
</style>
