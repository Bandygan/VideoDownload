<template>
  <div>
    <p v-if="user">Username: {{ user.username }}</p>
    <p v-else>Loading...</p>

    <div v-if="user">
      <h2>Your Links</h2>
      <ul class="dark-list">
        <li v-for="link in links" :key="link.id">
          {{ link.url }}
          <button class="delete-button" @click="removeLink(link.id)">Delete</button>
        </li>
      </ul>

      <form @submit.prevent="addNewLink">
        <label for="newLink">Add new link:</label>
        <input type="url" id="newLink" v-model="newLink" required>
        <button type="submit">Add Link</button>
      </form>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, watch } from 'vue';
import { useAuthStore } from '../stores/auth';
import { useRouter } from 'vue-router';

export default defineComponent({
  name: 'User',
  setup() {
    const links = ref([]);
    const authStore = useAuthStore();
    const newLink = ref('');
    const router = useRouter();

    const addNewLink = async () => {
      await authStore.addLink(newLink.value);
      newLink.value = '';
    };

    const removeLink = async (linkId) => {
      await authStore.deleteLink(linkId);
    };

    watch(() => authStore.links, (newValue) => {
      links.value = newValue;
    });

    const logout = () => {
      authStore.logout();
      router.push('/');
    };

    authStore.fetchUser();
    authStore.fetchLinks();

    return {
      user: authStore.user,
      links,
      newLink,
      addNewLink,
      removeLink,
      logout
    };
  }
});
</script>

<style scoped>
/* Стили для списка */
.dark-list {
  list-style: none; /* Убираем маркеры списка */
  padding: 0; /* Убираем внутренние отступы */
}

.dark-list li {
  background-color: #333; /* Цвет фона элемента списка */
  color: #fff; /* Цвет текста элемента списка */
  padding: 5px; /* Внутренние отступы */
  margin-bottom: 5px; /* Отступ между элементами списка */
  border-radius: 5px; /* Закругление углов */
  display: flex; /* Отображаем элементы списка в строку */
  align-items: center; /* Выравниваем элементы по вертикали */
}

/* Стили для кнопок в списке */
.delete-button {
  background-color: #ff0000; /* Цвет фона кнопки */
  color: #fff; /* Цвет текста кнопки */
  border: none; /* Убираем границу */
  border-radius: 5px; /* Закругление углов */
  margin-left: auto; /* Размещаем кнопку справа */
  cursor: pointer; /* Изменяем курсор при наведении */
  transition: background-color 0.3s ease; /* Анимация при наведении */
}

.delete-button:hover {
  background-color: #cc0000; /* Изменяем цвет фона кнопки при наведении */
}

button {
  background: #272727;
  width: 30vh;
  height: 7vh;
  border-radius: 50px;
}
</style>
