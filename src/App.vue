<template>
    <menuhead/>

 <div class="container-main">
    <main>
      <RouterView/>
    </main>
</div>
    <footer>
      Use a telegram bot to download videos to other devices
    </footer>

</template>

<script>
import {defineComponent, onMounted} from 'vue';
import {useAuthStore} from './stores/auth';
import menuhead from "./components/menuhead.vue";

export default defineComponent({
  name: 'App',
  components: {
    menuhead,
  },
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
  font-size: 30px;
  border-top: white 2px solid;
  background-color: #1E1E1E; /* Цвет фона футера */
  color: #fff; /* Цвет текста */
  padding: 20px 0; /* Внутренние отступы */
}

.container-main{
  display: flex;
  justify-content: center;
  text-align: center;
}

main{
  width: 75%;
  background-color: #1E1E1E; /* Цвет фона контейнера */
  padding: 20px; /* Внутренние отступы */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); /* Тень для визуального выделения */
  border-radius: 10px; /* Скругленные углы */
  margin-top: 20px; /* Отступ сверху */
  box-sizing: border-box; /* Включаем padding в общую ширину элемента */
}


</style>