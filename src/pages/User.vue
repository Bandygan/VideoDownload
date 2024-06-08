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

      <p v-if="error" class="error">{{ error }}</p>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, onMounted, watch } from 'vue';
import { useAuthStore } from '../stores/auth.js';

export default defineComponent({
  name: 'User',
  setup() {
    const userStore = useAuthStore();
    const newLink = ref('');
    const error = ref('');

    const addNewLink = async () => {
      try {
        await userStore.addLink(newLink.value);
        newLink.value = '';
        error.value = '';
        await userStore.fetchLinks();  // Refresh the links list after adding a new link
      } catch (err) {
        console.error('Error adding link:', err);
        error.value = 'Failed to add link.';
      }
    };

    onMounted(async () => {
      try {
        await userStore.fetchUser();
        await userStore.fetchLinks();
      } catch (err) {
        console.error('Error fetching user or links:', err);
        error.value = 'Failed to load user or links.';
      }
    });

    watch(() => userStore.links, (newLinks) => {
      console.log('Links updated:', newLinks);
    });

    return {
      user: userStore.user,
      links: userStore.links,
      newLink,
      addNewLink,
      error
    };
  }
});
</script>

<style scoped>
.error {
  color: red;
}
</style>
