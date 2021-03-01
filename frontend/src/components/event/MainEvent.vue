<template>
  <div style="clear: both; " class="q-mb-xl ">
    <q-carousel
      animated
      v-model="slide"
      navigation
      infinite
      :autoplay="autoplay"
      arrows
      transition-prev="slide-right"
      transition-next="slide-left"
      @mouseenter="autoplay = false"
      @mouseleave="autoplay = true"
      height="270px"
    >
      <q-carousel-slide
        :name="index"
        v-for="(event, index) in this.main_events"
        :key="event.eventId"
        style="background-color: black; border-radius: 10px;"
        class="overflow-hidden"
      >
        <main-entity :entity="event"></main-entity>
      </q-carousel-slide>
    </q-carousel>
  </div>
</template>

<script>
import MainEntity from '@/components/event/MainEntity.vue';
import { getMainEventList } from '@/api/board';

export default {
  components: {
    MainEntity,
  },
  data() {
    return {
      autoplay: true,
      slide: 1,
      main_events: [],
      num: 1,
    };
  },
  async created() {
    try {
      this.$q.loading.show();
      // 가져올 데이터 목록
      const { data } = await getMainEventList();
      this.main_events = data;
      return data;
    } catch (error) {
      console.log(error);
      // alert('에러가 발생했습니다.)
    } finally {
      this.$q.loading.hide();
    }
  },
};
</script>

<style></style>
