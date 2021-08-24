import Vue from 'vue';
import VueRouter from 'vue-router';
import CreateRoom from "@/views/CreateRoom";

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    // component: () => import("@/views/Home.vue")
    component: CreateRoom
  },
  {
    path: '/create',
    component: CreateRoom,
    children: [
      {
        path: 'room',
        name: 'CreateRoom',
        component: CreateRoom
      }
    ]
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
