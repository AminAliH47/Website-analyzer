import { createRouter, createWebHashHistory } from 'vue-router'
import IndexPage from '../views/Index.vue'

const routes = [
  {
    path: '/',
    name: 'IndexPage',
    component: IndexPage,
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
