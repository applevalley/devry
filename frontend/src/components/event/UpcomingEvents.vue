<template>
  <div class="row">
    <!-- 소제목 타이틀 -->
    <div class="row col-12 text-h6 text-weight-bold">개최 이벤트 목록</div>
    <!-- 이벤트 카테고리 -->
    <div class="row col-12 justify-end q-mb-sm">
      <q-select
        outlined
        v-model="category"
        :options="[
          'ALL',
          'Conference',
          'Workshop',
          'Hackathon',
          'Competition',
          'Meeting',
          'Recruting',
        ]"
        style="width:140px;"
      />
    </div>
    <!-- 이벤트 목록 -->
    <div class="q-ma-xs row col-12">
      <div class="row col-12">
        <q-intersection
          v-for="event in categorySortedList"
          :key="event.eventId"
          transition="scale"
          class=" col-4 q-pa-xs"
        >
          <upcoming-entity :entity="event"></upcoming-entity>
        </q-intersection>
      </div>
    </div>
  </div>
</template>

<script>
import UpcomingEntity from '@/components/event/UpcomingEntity.vue';
import { getEventList } from '@/api/board';

export default {
  components: {
    UpcomingEntity,
  },
  data() {
    return {
      category: 'ALL',
      upcoming_events: [],
    };
  },
  computed: {
    categorySortedList() {
      return this.upcoming_events.filter(article => {
        if (this.category === 'ALL') return true;
        if (article.category === this.category) return true;
        return false;
      });
    },
  },
  async created() {
    try {
      this.$q.loading.show();
      // 가져올 데이터 목록
      const { data } = await getEventList();
      this.upcoming_events = data;
      return data;
    } catch (error) {
      alert(error);
      // alert('에러가 발생했습니다.)
    } finally {
      this.$q.loading.hide();
    }
  },
};
</script>

<style scoped>
.q-select >>> .q-field--auto-height {
  min-height: 40px;
}
.q-select >>> .q-field__native {
  min-height: 40px;
  height: 40px;
}
.q-select >>> .q-field__append {
  min-height: 40px;
  height: 40px;
}
.q-select >>> .q-field__marginal {
  min-height: 40px;
}
.q-select >>> .q-field__control {
  min-height: 40px;
}
.q-select >>> .q-field__control-container {
  height: inherit;
}
.q-intersection > div {
  width: 100%;
}
</style>
