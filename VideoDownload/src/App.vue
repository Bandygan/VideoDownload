<template>
  <div>
    <h1>TORONTOFOKINO Production</h1>
    <div class="wrapper">
      <div class="wrapper_leftzone">
        <input type="text" placeholder="Get Url">
        <!-- Добавляем обработчик события клика на кнопку регистрации -->
        <button
            @click="openModal">Registration
        </button>
        <!-- Вставляем компонент модального окна -->
        <ModalWindow :isOpen="isModalOpen" @close="closeModal"/>
      </div>
      <button>Download</button>
    </div>
    <footer>Use a telegram bot to download videos to other devices</footer>
  </div>
</template>

<script>
import ModalWindow from './components/modal-window.vue';
import {ref} from 'vue';

export default {
  name: 'App',
  components: {
    ModalWindow
  },
  data() {
    return {
      isModalOpen: true
    };
  },
  methods: {
    openModal() {
      this.isModalOpen = true;
      console.log('Кнопка "Registration" была нажата!');
    },
    closeModal() {
      this.isModalOpen = false;
    }
  }
};


</script>


<style scoped>


.wrapper {
  margin-top: 50px;
  align-content: center;
  background: #323443;
  width: 120vh;
  height: 130px;
  border-radius: 50px;
  padding: 50px;
  text-align: center;
  justify-content: space-between;
  display: flex;
}

.wrapper button {
  background: #272727;
  width: 30vh;
  height: 7vh;
  font-size: 25px;
  border-radius: 50px;
}

.wrapper input {
  background: #1D1C1C;
  width: 100%;
  border-radius: 10px;
  height: 50px;
  border: 0;
  font-size: 20px;

}

.wrapper_leftzone {
  text-align: left;
  margin-right: 50px;
  width: 100%;

}

.wrapper_leftzone button {
  margin-top: 10px;
  margin-right: 20px;
  width: 150px;
  height: 50px;
  font-size: 25px;
}

footer {
  margin-top: 38vh;
  color: white;
  font-size: 30px;
  border-top: white 2px solid;
}

h1 {
  margin-top: 20px;
}

</style>