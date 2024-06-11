<template>
  <div class="wrapper">
      <div class="wrapper_leftzone">
        <input type="text" placeholder="Get Url"> <br><br>
      </div>
      <button>Download</button>
    </div>
</template>

<script>

export default {
  name: "download",

  components: {

  },
}
</script>

<style scoped>

.wrapper {
  margin-top: 50px;
  align-content: center;
  background: #323443;
  height: 100%;
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


</style>