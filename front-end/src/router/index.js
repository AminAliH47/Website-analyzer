import { createRouter, createWebHistory } from 'vue-router'
const IndexPage = () => import('@/views/Index.vue')
const AnalyzePage = () => import('@/views/Analyze.vue')

const routes = [
  {
    path: '/',
    name: 'IndexPage',
    component: IndexPage,
  },
  {
    path: '/analyze',
    name: 'AnalyzePage',
    component: AnalyzePage,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
