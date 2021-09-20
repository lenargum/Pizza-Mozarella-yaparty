import Vue from 'vue';
import VueRouter from 'vue-router';
import CreateRoom from "@/views/CreateRoom.vue";
import SpotifyLogin from "@/views/SpotifyLogin";
import Login from "@/views/Login";
import Home from "@/views/Home";
import Player from "@/views/Games/Game/Player";
import Judge from "@/views/Games/Game/Judge";
import Stub from "@/views/Stub";
import GamesWrapper from "@/views/GamesWrapper";
import GamesLibrary from "@/views/Games/GamesLibrary";
import GuessTheMelody from "@/views/Games/Game/GuessTheMelody";
import Playlist from "@/views/Playlist";
import LeaderBoard from "@/views/Games/Game/LeaderBoard";
import PlayMusic from "@/views/Games/Game/PlayMusic";


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
        name: "GuessTheMelody",
        component: GuessTheMelody
      },
      {
        path: 'guess-the-melody',
        name: "GuessTheMelody",
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
