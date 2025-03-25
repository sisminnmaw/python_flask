<template>
  <div class="hello">
    <h1>{{ message }}</h1>
    <button @click="fetchMessage">Get Message from API</button>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      message: 'Welcome to Vue.js'
    }
  },
  methods: {
    async fetchMessage() {
      try {
        const response = await fetch('http://localhost:5000/api/hello')
        const data = await response.json()
        this.message = data.message
      } catch (error) {
        console.error('Error fetching message:', error)
      }
    }
  }
}
</script>

<style scoped>
.hello {
  text-align: center;
  margin-top: 60px;
}
</style> 