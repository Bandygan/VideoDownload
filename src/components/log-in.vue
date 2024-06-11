<template>
  <button v-if="!isLoggedIn" @click="setIsOpen(true)" id="log-m">Login</button>


  <button v-if="isLoggedIn" @click="logout" id="log-m">Logout</button>

  <Dialog :open="isOpen" @close="setIsOpen">
    <div class="modal-back">
      <div class="box-modal">
        <DialogPanel class="dialog-box">
          <DialogTitle>Sign In</DialogTitle>
          <DialogDescription>
            <form @submit.prevent="submitForm">
              <label>Username </label>
              <input type="text" name="username" v-model="username"><br><br>
              <label>Password </label>
              <input type="password" name="password" v-model="password"><br><br>
              <button type="submit">Log In</button>
            </form>
          </DialogDescription>
        </DialogPanel>
      </div>
    </div>
  </Dialog>
</template>

<script setup>
import { ref, watch} from 'vue';
import { useAuthStore} from '../stores/auth.js';
import { useRouter } from 'vue-router';
import {
  Dialog,
  DialogPanel,
  DialogTitle,
  DialogDescription,
} from '@headlessui/vue';

const isOpen = ref(false);
const username = ref('');
const password = ref('');
const authStore = useAuthStore();
const router = useRouter();

const isLoggedIn = ref(false);

watch(() => authStore.user, (newValue) => {
  isLoggedIn.value = !!newValue;
});

function logout() {
  authStore.logout();
  router.push('/');
}

function setIsOpen(value) {
  isOpen.value = value;
}



async function submitForm() {
  try {
    await authStore.login(username.value, password.value);
    setIsOpen(false);
    router.push('/user');
  } catch (error) {
    console.error('Login failed', error);
  }
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

#log-m{
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
