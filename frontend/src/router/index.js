import Vue from 'vue';
import VueRouter from 'vue-router';
import CreateRoom from "@/views/CreateRoom.vue";
import SpotifyLogin from "@/views/SpotifyLogin";
import Login from "@/views/Login";
import Home from "@/views/Home";
import Stub from "@/views/Stub";
import GamesWrapper from "@/views/GamesWrapper";
import GamesLibrary from "@/views/Games/GamesLibrary";
import GuessTheMelody from "@/views/Games/Game/GuessTheMelody";
import Playlist from "@/views/Playlist";


Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    component: Home
  },
  {
    path: '/create',
    redirect: '/create/room'
  },
  {
    path: '/create/room',
    name: 'CreateRoom',
    component: CreateRoom
  },
  {
    path: '/spotify/:id',
    name: 'SpotifyLogin',
    component: SpotifyLogin
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/home/:id',
    name: 'Home',
    component: Home
  },
  {
    path: '/games',
    component: GamesWrapper,
    children: [
      {
        path: 'guess-the-melody/:sessionId',
        component: GuessTheMelody
      },
      {
        path: 'guess-the-melody',
        component: GuessTheMelody
      },
      {
        path: '',
        name: "GamesLibrary",
        component: GamesLibrary
      },
    ]
  },
  {
    path: '/playlist/:id',
    name: 'Playlist',
    component: Playlist
  },
  {
    path: '/in-progress',
    name: 'Stub',
    component: Stub
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
