import Vue from 'vue';
import VueRouter from 'vue-router';
import store from '@/store/index';
Vue.use(VueRouter);

// 로그인 모달 작동
const loginModalOn = () => {
  store.commit('setAccountModalType', 'login');
  store.commit('onAccountModal');
};

// 로그인이 안되어있으면 로그인 모달 작동
const isLogined = (to, from, next) => {
  if (!store.getters.isLogined) {
    loginModalOn();
    return;
  }
  next();
};

// 관리자가 아닐경우 포럼으로 이동
const isAdmin = (to, from, next) => {
  if (!store.getters.isLogined && Number(store.state.id) <= 5) {
    alert('관리자만 가능합니다');
    next('/forum');
    return;
  }
  next();
};

const routes = [
  {
    path: '/',
    redirect: '/forum',
  },
  // 프로필 관련
  {
    path: '/profile/:id',
    name: 'Profile',
    component: () => import('@/views/profile/ProfilePage.vue'),
  },
  {
    path: '/profile-setting',
    name: 'ProfileSetting',
    component: () => import('@/views/profile/ProfileSettingPage.vue'),
    beforeEnter: isLogined,
  },
  // 북마크
  {
    path: '/bookmark',
    name: 'Bookmark',
    component: () => import('@/views/bookmark/BookmarkPage.vue'),
  },
  // QnA 관련
  {
    path: '/qna',
    name: 'QnA',
    component: () => import('@/views/qna/QnaBoardPage.vue'),
  },
  {
    path: '/qna-detail/:id',
    name: 'QnaDetail',
    component: () => import('@/views/qna/QnaDetailPage.vue'),
  },
  {
    path: '/qna/create',
    name: 'QnACreate',
    component: () => import('@/views/qna/QnaCreatePage.vue'),
    beforeEnter: isLogined,
  },
  {
    path: '/qna/:id',
    name: 'QnAUpdate',
    component: () => import('@/views/qna/QnaUpdatePage.vue'),
    beforeEnter: isLogined,
  },
  // 포럼 관련
  {
    path: '/forum',
    name: 'Forum',
    component: () => import('@/views/forum/ForumBoardPage.vue'),
  },
  {
    path: '/forum-detail/:id',
    name: 'ForumDetail',
    component: () => import('@/views/forum/ForumDetailPage.vue'),
  },
  {
    path: '/forum/create',
    name: 'ForumCreate',
    component: () => import('@/views/forum/ForumCreatePage.vue'),
    beforeEnter: isLogined,
  },
  {
    path: '/forum/:id',
    name: 'ForumUpdate',
    component: () => import('@/views/forum/ForumUpdatePage.vue'),
    beforeEnter: isLogined,
  },
  // 이벤트 관련
  {
    path: '/event',
    name: 'Event',
    component: () => import('@/views/event/EventBoardPage.vue'),
  },
  {
    path: '/event-detail/:id',
    name: 'EventDetail',
    component: () => import('@/views/event/EventDetailPage.vue'),
  },
  {
    path: '/event/create',
    name: 'EventCreate',
    component: () => import('@/views/event/EventCreatePage.vue'),
    beforeEnter: isAdmin,
  },
  {
    path: '/event/:id',
    name: 'EventUpdate',
    component: () => import('@/views/event/EventUpdatePage.vue'),
    beforeEnter: isAdmin,
  },
  // Not Found Page
  {
    path: '*',
    component: () => import('@/views/NotFoundPage.vue'),
  },
];

const router = new VueRouter({
  routes,
});
export default router;
