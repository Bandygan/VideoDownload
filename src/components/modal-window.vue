<template>
  <button @click="setIsOpen(true)" id="regist-m">Registration</button>


  <Dialog :open="isOpen" @close="setIsOpen">
    <div class="modal-back">
      <div class="box-modal">
        <DialogPanel class="dialog-box">
          <DialogTitle>Registration</DialogTitle>
          <dialog-description>
            <form @submit.prevent="submitForm">
              <label>Username </label>
              <input type="text" name="username" v-model="username"><br><br>
              <label>Password </label>
              <input type="password" name="password" v-model="password"><br><br>
              <button type="submit">Registration</button>
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
  name: 'Modal-Registration',
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    submitForm(e) {
      const formData = {
        username: this.username,
        password: this.password,
      }

      axios

            .post('http://127.0.0.1:8000/api/v1/users/', formData)
            .then(response => {
              console.log(response)
              this.$router.push('/')
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

button{
  background: #272727;
  font-size: 20px;
  border-radius: 50px;
}

#regist-m{
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

input{
  background: #1D1C1C;
  width: 70%;
  border-radius: 10px;
  height: 50px;
  border: 0;
  font-size: 20px;
}
</style>