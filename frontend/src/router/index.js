import Vue from 'vue';
import VueRouter from 'vue-router';
import CreateRoom from "@/views/CreateRoom";
import SpotifyLogin from "@/views/SpotifyLogin";
import Login from "@/views/Login";

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    component: SpotifyLogin
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
  {
    path: '/spotify',
    name: 'SpotifyLogin',
    component: SpotifyLogin
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
