<script setup>

</script>

<template>
  <h1>Download video</h1>
  <div class="wrapper">
     <div class="wrapper_leftzone"> <input type="text" placeholder="Get Url">
          <button>Audio</button>
          <button>Cut</button>
     </div>

    <button>Download</button>
  </div>

  <footer>Use a telegram bot to download videos to other devices </footer>

</template>

<style scoped>

.wrapper{
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

.wrapper button{
  background: #272727;
  width: 30vh;
  height: 7vh;
  font-size: 25px;
  border-radius: 50px;
  border: 0;
}

.wrapper input{
  background: #1D1C1C;
  width: 100%;
  border-radius: 10px;
  height: 50px;
  border: 0;
  font-size: 20px;

}

.wrapper_leftzone{
  text-align: left;
  margin-right: 50px;
  width: 100%;

}

.wrapper_leftzone button{
  margin-top: 10px;
  margin-right: 20px;
  width: 150px;
  height: 50px;
  font-size: 25px;
}

footer{
  margin-top: 45vh;
  color: white;
  font-size: 30px;
  border-top: white 2px solid;
}

h1{
  margin-top: 20px;
}

</style>
