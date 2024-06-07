<template>
  <div>
    <p v-if="user">Username: {{ user.username }}</p>
    <p v-else>Loading...</p>

    <div v-if="user">
      <h2>Your Links</h2>
      <ul>
        <li v-for="link in links" :key="link.id">{{ link.url }}</li>
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
import { defineComponent, ref } from 'vue';
import { useUserStore } from '../stores/user';

export default defineComponent({
  name: 'User',
  setup() {
    const userStore = useUserStore();
    const newLink = ref('');

    const addNewLink = async () => {
      await userStore.addLink(newLink.value);
      newLink.value = '';
    };

    userStore.fetchUser();
    userStore.fetchLinks();

    return {
      user: userStore.user,
      links: userStore.links,
      newLink,
      addNewLink
    };
  }
});
</script>

<style scoped>


</style>
