<template>
  <div class="row q-pa-md justify-center q-mt-md">
    <div class="row col-6">
      <!-- 타이틀 -->
      <div class="q-mb-md">
        <span class="text-h4 text-weight-bolder"
          >Event 등록 관리자 페이지
        </span>
        <p class="text-subtitle2 q-mt-sm">
          관리자 전용 Event 등록 페이지입니다 :)
        </p>
      </div>
      <!-- 이벤트 입력폼 -->
      <event-create-form></event-create-form>
    </div>
  </div>
</template>

<script>
import EventCreateForm from '@/components/event/EventCreateForm';
export default {
  components: { EventCreateForm },
};
</script>

<style scoped></style>
