<template>
  <div>
    <p v-if="user">Username: {{ user.username }}</p>
    <p v-else>Loading...</p>

    <div v-if="user">
      <h2>Your Links</h2>
      <ul>
        <li v-for="link in links" :key="link.id">
          {{ link.url }}
          <button @click="removeLink(link.id)">Delete</button>
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
import {defineComponent, ref, watch} from 'vue';
import {useAuthStore} from '../stores/auth';

export default defineComponent({
  name: 'User',
  setup() {
    const links = ref([]);
    const authStore = useAuthStore();
    const newLink = ref('');

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


    authStore.fetchUser();
    authStore.fetchLinks();

    return {
      user: authStore.user,
      links,
      newLink,
      addNewLink,
      removeLink
    };
  }
});
</script>


<!--<script>-->
import { defineComponent, ref, watch } from 'vue'; // Импортируем функцию watch
import { useAuthStore } from '../stores/auth';

export default defineComponent({
name: 'User',
setup() {
const authStore = useAuthStore();
const newLink = ref('');

const addNewLink = async () => {
await authStore.addLink(newLink.value);
newLink.value = '';
};

const removeLink = async (linkId) => {
await authStore.deleteLink(linkId);
};

// Следим за изменениями в списке ссылок и обновляем его
watch(() => authStore.links, (newValue) => {
links.value = newValue;
});

authStore.fetchUser();
authStore.fetchLinks();

const user = ref(null); // Создаем реактивную переменную для пользователя
const links = ref([]); // Создаем реактивный массив для ссылок

return {
user,
links,
newLink,
addNewLink,
removeLink
};
}
});
<!--</script>-->

<style scoped>

ul button {
  width: 9vh;
  height: 4vh;
  font-size: 15px;
}


</style>
