<template>
  <q-layout view="hHh lpR fFf" style="width:100vw" id="app">
    <main-header />
    <liquid-tag-guide-modal></liquid-tag-guide-modal>
    <account-modal></account-modal>
    <follow-modal v-if="onFollowModal"></follow-modal>
    <side-bar></side-bar>
    <tag-bar></tag-bar>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import MainHeader from '@/components/common/MainHeader';
import SideBar from '@/components/common/SideBar';
import AccountModal from '@/components/common/AccountModal';
import FollowModal from '@/components/follow/FollowModal';
import TagBar from '@/components/common/TagBar';
import LiquidTagGuideModal from '@/components/common/LiquidTagGuideModal';
export default {
  components: {
    MainHeader,
    AccountModal,
    FollowModal,
    SideBar,
    TagBar,
    LiquidTagGuideModal,
  },
  computed: {
    onFollowModal() {
      return this.$store.state.follow.modal;
    },
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap');
#app {
  font-family: 'Noto Sans KR', sans-serif;
}
a {
  text-decoration: none;
}
</style>
