import Vue from 'vue'
import VueRouter from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import Dashboard_1 from '../views/Dashboard_1.vue'
import Event_list from '../views/Event_list.vue'
import Team from '../views/Team.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/eventlist',
    name: 'Event_list',
    component: Event_list,
  },
  {
    path: '/team',
    name: 'team',
    component: Team,
  },
  {
    path: '/D1',
    name: 'Dashboard_1',
    component: Dashboard_1,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
