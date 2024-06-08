<template>
  <div class="wrapper">
      <div class="wrapper_leftzone">
        <input type="text" placeholder="Get Url"> <br><br>
        <ModalWindow class="button" :isOpen="isModalOpen" @close="closeModal"/>
        <LogIn class="button" :isOpen="isModalOpen"/>
      </div>
      <button>Download</button>
    </div>
</template>

<script>

import ModalWindow from "./modal-window.vue";
import LogIn from "./log-in.vue";

export default {
  name: "download",

  components: {
    ModalWindow,
    LogIn
  },
}
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

</style>