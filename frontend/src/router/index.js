import Vue from 'vue';
import VueRouter from 'vue-router';
import CreateRoom from "@/views/CreateRoom.vue";
import SpotifyLogin from "@/views/SpotifyLogin";
import Login from "@/views/Login";
import Home from "@/views/Home";
import CreateGame from "@/views/Game/CreateGame";
import ChooseRole from "@/views/Game/ChooseRole";
import Player from "@/views/Game/Player";
import Judge from "@/views/Game/Judge";
import Stub from "@/views/Stub";
import MobileLogin from "@/views/Game/MobileLogin";
import Games from "@/views/Games";
import Playlist from "@/views/Playlist";
import LeaderBoard from "@/views/Game/LeaderBoard";
import PlayMusic from "@/views/Game/PlayMusic";

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
    path: '/create/game',
    name: 'CreateGame',
    component: CreateGame
  },
  {
    path: '/play',
    component: ChooseRole,
  },
  {
    path: '/play/player',
    name: 'Player',
    component: Player
  },
  {
    path: '/play/judge',
    name: 'Judge',
    component: Judge
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
    path: '/mobileLogin/:sessionId',
    name: 'MobileLogin',
    component: MobileLogin
  },
  {
    path: '/home/:id',
    name: 'Home',
    component: Home
  },
  {
    path: '/in-progress',
    name: 'Stub',
    component: Stub
  },
  {
    path: '/games',
    name: 'Games',
    component: Games
  },
  {
    path: '/playlist/:id',
    name: 'Playlist',
    component: Playlist
  },
  {
    path: '/leaderboard',
    name: 'LeaderBoard',
    component: LeaderBoard
  },
  {
    path: '/play/music',
    name: 'PlayMusic',
    component: PlayMusic
  },
  {
    path: '*',
    redirect: '/in-progress'
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
