import { defineStore } from 'pinia';
import axios from 'axios';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('authToken') || null,
    user: null,
    links: []
  }),
  actions: {
    // Auth actions
    setToken(token) {
      this.token = token;
      localStorage.setItem('authToken', token);
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    },
    setUser(user) {
      this.user = user;
    },
    logout() {
      this.token = null;
      this.user = null;
      localStorage.removeItem('authToken');
      delete axios.defaults.headers.common['Authorization'];
    },
    async fetchUser() {
      try {
        const token = this.token;
        const response = await axios.get('http://127.0.0.1:8000/api/v1/users/me', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        this.setUser(response.data);
      } catch (error) {
        console.error(error);
      }
    },
    async login(username, password) {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/v1/jwt/create/', { username, password });
        this.setToken(response.data.access);
        await this.fetchUser();
        return response;
      } catch (error) {
        console.error('Login failed', error);
        throw error;
      }
    },
    // User actions
    async addLink(link) {
      try {
        const token = localStorage.getItem('authToken');
        const response = await axios.post('http://127.0.0.1:8000/api/v1/add_link/', { link }, {
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
        const response = await axios.get('http://127.0.0.1:8000/api/v1/links/', {
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
