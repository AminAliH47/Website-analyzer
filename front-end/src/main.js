import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import './assets/css/tailwind/index.css'
import './assets/css/style.css'

createApp(App).use(router).mount('#app')
