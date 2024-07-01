import { defineStore } from 'pinia';
import axios from 'axios';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    links: []
  }),
  actions: {
    setUser(user) {
      this.user = user;
    },
    
    async logout() {
      this.user = null;
      await axios.post('logout');
      // localStorage.removeItem('csrftoken');
    },
    
    async fetchUser() {
      try {
        const response = await axios.get('/api/v1/users/me', {
        });
        this.setUser(response.data);
      } catch (error) {
        console.error(error);
      }
    },
    // User actions
    async addLink(link) {
      try {
        const token = localStorage.getItem('authToken');
        const response = await axios.post('/api/v1/links/', { url: link }, {
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
        const response = await axios.get('/api/v1/links/', );
        this.links = response.data;
      } catch (error) {
        console.error(error);
      }
    },


    async deleteLink(linkId) {
      try {
        const token = localStorage.getItem('authToken');
        await axios.delete(`/api/v1/links/${linkId}/`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        this.links = this.links.filter(link => link.id !== linkId);
      } catch (error) {
        console.error(error);
      }
    }



  }
});
