<template>
  <button @click="setIsOpen(true)">logIn</button>


  <Dialog :open="isOpen" @close="setIsOpen">
    <div class="modal-back">
      <div class="box-modal">
        <DialogPanel class="dialog-box">
          <DialogTitle>Sing In</DialogTitle>
          <dialog-description>
            <form @submit.prevent="submitForm">
              <label>Username </label>
              <input type="email" name="username" v-model="username"><br><br>
              <label>Password </label>
              <input type="password" name="password" v-model="password"><br><br>
              <button type="submit">LogIn</button>
            </form>
          </dialog-description>
        </DialogPanel>
      </div>
    </div>
  </Dialog>
</template>

<script setup>
import {ref} from 'vue'
import {
  Dialog,
  DialogPanel,
  DialogTitle,
  DialogDescription,
} from '@headlessui/vue'


const isOpen = ref(false)

function setIsOpen(value) {
  isOpen.value = value
}
</script>

<script>

import axios from 'axios'

export default {
  name: 'LogIn',
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    submitForm(e) {
      axios.defaults.headers.common['Authorization'] = ''
      localStorage.removeItem("access")

      const formData = {
        username: this.username,
        password: this.password
      }

      axios
            .post('http://127.0.0.1:8000/api/v1/jwt/create/', formData)
            .then(response => {
              console.log(response)

              this.$router.push('/user')

            })
            .catch(error => {
              console.log(error)
            })

    }
  }
}


</script>

<style>

.dialog-box {
  padding: 10px 10px 10px 10px;
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

button {
  background: #272727;
  width: 30vh;
  height: 7vh;
  font-size: 25px;
  border-radius: 50px;
}

input {
  background: #1D1C1C;
  width: 70%;
  border-radius: 10px;
  height: 50px;
  border: 0;
  font-size: 20px;
}
</style>