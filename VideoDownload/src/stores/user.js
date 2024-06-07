import { defineStore } from 'pinia';
import axios from 'axios';

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null,
    links: []
  }),
  actions: {
    async fetchUser() {
      try {
        const token = localStorage.getItem('authToken');
        const response = await axios.get('http://127.0.0.1:8000/api/v1/users/me', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        this.user = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async addLink(link) {
      try {
        const token = localStorage.getItem('authToken');
        const response = await axios.post('http://127.0.0.1:8000/api/v1/users/add_link', { link }, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        this.links.push(response.data);
      } catch (error) {
        console.error(error);
      }
    },
    async fetchLinks() {
      try {
        const token = localStorage.getItem('authToken');
        const response = await axios.get('http://127.0.0.1:8000/api/v1/users/links', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        this.links = response.data;
      } catch (error) {
        console.error(error);
      }
    }
  }
});
