<template>
  <div class="row col-12 justify-center">
    <div
      class="row col-12 q-mb-md text-h6 text-weight-bold"
      style="color: #545454"
    >
      QnA 북마크
    </div>
    <template v-if="QnaBookmarkList.length > 0">
      <div
        v-for="(data, index) in QnaBookmarkList"
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
                {{ data.written_time | moment('YYYY/MM/DD HH:mm') }}
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
import { getQnaBookmarkList } from '@/api/bookmark';
import { toggleQnaBookmark } from '@/api/qna';
import { colorSoloMapper } from '@/utils/tagColorMapper';

export default {
  data() {
    return {
      QnaBookmarkList: [],
    };
  },
  methods: {
    tagColor(tag, alpha) {
      return colorSoloMapper(tag, alpha);
    },
    goToDetail(index) {
      this.$router.push(`/qna-detail/${this.QnaBookmarkList[index].id}`);
    },
    goToProfile(index) {
      this.$router.push(`/profile/${this.QnaBookmarkList[index].user.id}`);
    },
    async getQnaBookmark() {
      try {
        this.$q.loading.show();
        const { data } = await getQnaBookmarkList();
        this.QnaBookmarkList = data;
      } catch (error) {
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },
    async cancelBookmark(index) {
      try {
        this.$q.loading.show();
        const qnaId = this.QnaBookmarkList[index].id;
        await toggleQnaBookmark(qnaId);
        this.getQnaBookmark();
      } catch (error) {
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },
  },
  async created() {
    try {
      this.getQnaBookmark();
    } catch (error) {
      alert(error);
    }
  },
};
</script>

<style scoped></style>
