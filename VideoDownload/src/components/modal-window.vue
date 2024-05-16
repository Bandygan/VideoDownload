<template>
  <button @click="setIsOpen(true)">Открыть окно</button>


  <Dialog :open="isOpen" @close="setIsOpen">
    <div class="modal-back">
      <div class="box-modal">
        <DialogPanel class="dialog-box">
          <DialogTitle>Окно регистрации</DialogTitle>
          <DialogDescription>
            Привет
          </DialogDescription>
          <p>
            Вот тут вы будете регистрироваться
          </p>

          <button @click="">Регистрация</button>
          <button @click="setIsOpen(false)">Закрыть</button>
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

</style>