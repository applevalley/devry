<template>
  <div class="q-pt-lg row justify-center">
    <div class="col-8 q-pl-lg">
      <!-- 타이틀 -->
      <div class="row q-mb-sm q-mb-lg col-12 text-h5 text-weight-bold">
        <div class="row col-9">Event 게시판</div>
      </div>
      <main-event></main-event>
      <recommend-events></recommend-events>
      <upcoming-events class="q-mb-lg"></upcoming-events>
      <!-- 이벤트 등록 신청 버튼 -->
      <div
        class="q-mb-xl q-mt-md float-right"
        v-if="Number($store.state.id) <= 5"
      >
        <q-btn
          color="blue-12"
          class="text-weight-bold q-px-md q-py-sm"
          label="이벤트 등록 신청"
          @click="goToEventRegister"
          size="md"
        />
      </div>
    </div>
  </div>
</template>

<script>
import MainEvent from '@/components/event/MainEvent';
import RecommendEvents from '@/components/event/RecommendEvents';
import UpcomingEvents from '@/components/event/UpcomingEvents';

export default {
  components: {
    MainEvent,
    RecommendEvents,
    UpcomingEvents,
  },
  methods: {
    goToEventRegister() {
      this.$router.push('/event/create');
    },
  },
  created() {
    // 왼쪽 사이드 바 열림
    this.$store.commit('onLeft');
  },
};
</script>

<style scoped></style>
