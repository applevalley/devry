<template>
  <q-card
    class="row full-width"
    style="height:300px"
    v-tilt="{ speed: 300, perspective: 800 }"
  >
    <!-- 썸네일 -->
    <q-img
      :src="entity.thumbnail ? entity.thumbnail : require('@/assets/DEVRY.jpg')"
      style="height: 40%; border-bottom: 1px solid #cccccc"
      class="cursor-pointer"
      @click="goToDetail"
    />
    <!-- 타이틀 -->
    <div
      class="row full-width q-pt-sm q-px-md q-mb-xs text-weight-bold forum-title"
      style="font-size: 1.1em; height:20%"
    >
      <span class="cursor-pointer" @click="goToDetail">{{ entity.title }}</span>
    </div>
    <!-- 태그 -->
    <div class="row full-width q-px-md" style="height:18%">
      <span
        v-for="(tag, index) in entity.ref_tags"
        :key="index"
        :style="{ 'background-color': tagColor(tag, 0.3) }"
        style="font-size:0.8em; border-radius:3pt; height:20px"
        class="q-px-xs q-mr-xs row items-center  q-mb-xs"
      >
        <div># {{ tag.charAt(0).toUpperCase() + tag.slice(1) }}</div>
      </span>
    </div>
    <!-- 프로필 정보 -->
    <div class="row full-width q-px-md" style="height:22%">
      <div class="row col-8 items-center">
        <div class="row q-mr-sm">
          <q-avatar style="border: 1px solid #ECEFF1" size="2.3rem">
            <q-img
              :src="
                entity.profile.profile_img
                  ? entity.profile.profile_img
                  : require('@/assets/basic_image.png')
              "
              @click="goToProfile"
              class="cursor-pointer"
              style="height:100%"
            />
          </q-avatar>
        </div>
        <div class="row col-9">
          <div
            style="font-size: 0.9rem; color: #464646"
            @click="goToProfile"
            class="cursor-pointer text-weight-bold full-width"
          >
            {{ entity.user.username }}
          </div>
          <div style="font-size:0.7rem" class="full-width">
            {{ entity.written_time | moment('YYYY/MM/DD hh:mm') }}
          </div>
        </div>
      </div>
      <div class="row col-4">
        <div class="row col-5">
          <div class="row col-6 items-center">
            <q-icon
              :name="entity.liked ? $i.ionHeart : $i.ionHeartOutline"
              size="1.5rem"
              :color="entity.liked ? 'red-8' : 'grey-6'"
            ></q-icon>
          </div>
          <div class="row col-6 items-center justify-end">
            <div style=" font-size: 1rem;">{{ entity.like_num }}</div>
          </div>
        </div>
        <div class="col-2"></div>
        <div class="row col-5 ">
          <div class="row col-6 justify-end items-center">
            <q-icon
              :name="$i.ionChatboxEllipsesOutline"
              style="color:#727272"
              size="1.5em"
            ></q-icon>
          </div>
          <div class="row col-6 items-center justify-end">
            <div style="font-size: 1rem;">{{ entity.comment_count }}</div>
          </div>
        </div>
      </div>
    </div>
  </q-card>
</template>

<script>
// import { toggleForumLike, toggleforumBookmark } from '@/api/forum';

import { colorSoloMapper } from '@/utils/tagColorMapper';
export default {
  props: {
    entity: Object,
  },
  data() {
    return {
      img_url: `${this.entity.profile.profile_img}`,
      thumbnail_url: `${this.entity.thumbnail}`,
    };
  },
  methods: {
    tagColor(tag, alpha) {
      return colorSoloMapper(tag, alpha);
    },
    goToDetail() {
      this.$router.push(`/forum-detail/${this.entity.id}`);
    },
    goToProfile() {
      this.$router.push(`/profile/${this.entity.user.id}`);
    },
  },
};
</script>

<style scoped>
.forum-title {
  line-height: 1.5;
  max-height: 3.2em;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}
/* .q-avatar >>> .q-avatar__content {
  width: 1em;
  height: 1em;
  font-size: 1em;
} */
</style>
