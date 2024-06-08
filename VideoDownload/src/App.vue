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
import { defineComponent, onMounted } from 'vue';
import { useAuthStore } from './stores/auth';

export default defineComponent({
  name: 'App',
  setup() {
    const authStore = useAuthStore();

    onMounted(async () => {
      if (authStore.token) {
        await authStore.fetchUser();
        await userStore.fetchLinks();
      }
    });

    return {
      isAuthenticated: authStore.isAuthenticated,
    };
  },
});
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