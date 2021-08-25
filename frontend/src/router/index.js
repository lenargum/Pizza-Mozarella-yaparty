import Vue from 'vue';
import VueRouter from 'vue-router';
import CreateRoom from "@/views/CreateRoom.vue";
import SpotifyLogin from "@/views/SpotifyLogin";
import Login from "@/views/Login";
import Home from "@/views/Home";
import CreateGame from "@/views/CreateGame";
import ChooseRole from "@/views/ChooseRole";
import Player from "@/views/Player";
import Judge from "@/views/Judge";
import Stub from "@/views/Stub";
import MobileLogin from "@/views/MobileLogin";
import Games from "@/views/Games";
import Playlist from "@/views/Playlist";
import LeaderBoard from "@/views/LeaderBoard";
import PlayMusic from "@/views/PlayMusic";

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    component: PlayMusic
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
    path: '/spotify',
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
    path: '/home',
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
    path: '/playlist',
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
