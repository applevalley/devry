<template>
  <div class="row col-12 justify-center">
    <div
      class="row col-12 q-mb-md text-h6 text-weight-bold"
      style="color: #545454"
    >
      이벤트 북마크
    </div>
    <template v-if="EventBookmarkList.length > 0">
      <div
        v-for="(data, index) in EventBookmarkList"
        :key="index"
        class="row col-12 q-mb-sm"
      >
        <q-card class="row full-width q-pa-md" flat bordered>
          <div class="row col-12">
            <div class="row col-9">
              <div class="row col-12 q-mb-sm">
                <span
                  class="text-body1 cursor-pointer"
                  @click="goToDetail(index)"
                  >{{ data.title }}</span
                >
              </div>
              <div class="row col-12">
                <span
                  v-for="tag in data.ref_tags"
                  :key="tag"
                  :style="{ 'background-color': tagColor(tag, 0.5) }"
                  style="font-size:0.8em; border-radius:3pt;"
                  class="q-px-xs q-mr-sm"
                  >#{{ tag.charAt(0).toUpperCase() + tag.slice(1) }}</span
                >
              </div>
            </div>
            <div class="row col-2">
              <div
                class="row col-12 cursor-pointer text-primary"
                @click="goToProfile(index)"
              >
                @{{ data.user.username }}
              </div>
              <div class="row col-12 text-caption">
                {{ data.start | moment('YYYY/MM/DD') }}
              </div>
            </div>
            <div class="row col-1 justify-end">
              <q-icon
                :name="$i.ionBookmark"
                :style="{ color: '#598FFC' }"
                size="xs"
                class="cursor-pointer"
                @click="cancelBookmark(index)"
              ></q-icon>
            </div>
          </div>
        </q-card>
      </div>
    </template>
    <template v-else>
      아직 북마크한 내역이 없습니다.
    </template>
  </div>
</template>

<script>
import { getEventBookmarkList } from '@/api/bookmark';
import { toggleEventBookmark } from '@/api/event';
import { colorSoloMapper } from '@/utils/tagColorMapper';

export default {
  data() {
    return {
      EventBookmarkList: [],
    };
  },
  methods: {
    goToDetail(index) {
      this.$router.push(`/event-detail/${this.EventBookmarkList[index].id}`);
    },
    goToProfile(index) {
      this.$router.push(`/profile/${this.EventBookmarkList[index].user.id}`);
    },
    tagColor(tag, alpha) {
      return colorSoloMapper(tag, alpha);
    },
    async getEventBookmark() {
      try {
        this.$q.loading.show();
        const { data } = await getEventBookmarkList();
        this.EventBookmarkList = data;
      } catch (error) {
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },
    async cancelBookmark(index) {
      try {
        this.$q.loading.show();
        const eventId = this.EventBookmarkList[index].id;
        await toggleEventBookmark(eventId);
        this.getEventBookmark();
      } catch (error) {
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },
  },
  async created() {
    try {
      this.getEventBookmark();
    } catch (error) {
      alert(error);
    }
  },
};
</script>

<style scoped></style>
