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

      <button @click="logout">Logout</button>
    </div>
  </div>
</template>

<script>
import {defineComponent, ref, watch} from 'vue';
import {useAuthStore} from '../stores/auth';
import {useRouter} from 'vue-router'

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

ul button {
  width: 9vh;
  height: 4vh;
  font-size: 15px;
}


</style>
