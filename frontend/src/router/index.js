import Vue from 'vue';
import VueRouter from 'vue-router';
import CreateParty from "@/views/CreateParty";

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    component: CreateParty
  },
  {
    path: '/create-party',
    name: "CreateParty",
    component: CreateParty
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
