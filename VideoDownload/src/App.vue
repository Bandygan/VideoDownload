<template>
  <div>
    <h1>TORONTOFOKINO Production</h1>
    <nav id="nav">
      <RouterLink to="/">Home </RouterLink>
      <RouterLink to="/user">User</RouterLink>
    </nav>
    <main>
      <RouterView/>
    </main>

    <footer>Use a telegram bot to download videos to other devices</footer>
  </div>
</template>

<script>

import {RouterLink, RouterView} from 'vue-router'

export default {
  name: 'App',

};


</script>


<style scoped>
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