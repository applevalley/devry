<template>
  <q-card class="row full-width" style="min-height:300px">
    <!-- 썸네일 -->
    <q-img
      :src="
        entity.thumbnail
          ? thumbnail_url
          : require('@/assets/basic_thumbnail.png')
      "
      style="height: 50%;"
      class="cursor-pointer"
      @click="goToDetail"
    />
    <!-- 타이틀 -->
    <div
      class="row full-width q-pt-sm q-px-md q-mb-xs text-weight-bold forum-title"
      style="font-size: 1.1em; height:19%"
    >
      <span class="cursor-pointer" @click="goToDetail">{{ entity.title }}</span>
    </div>
    <!-- 태그 -->
    <div class="row full-width q-px-md ">
      <span
        v-for="(tag, index) in entity.ref_tags"
        :key="index"
        :style="{ 'background-color': tagColor(tag, 0.3) }"
        style="font-size:0.8em; border-radius:3pt; height:20px"
        class="q-px-xs q-mr-xs"
        ># {{ tag.charAt(0).toUpperCase() + tag.slice(1) }}</span
      >
    </div>
    <div class="row full-width  q-px-md q-py-sm ">
      <div class="row col-12">
        <div class="row col-8 items-center q-gutter-sm">
          <div class="row col-12">
            <div class="row col-2">
              <span class="q-mt-xs">
                <q-avatar style="border: 1px solid #ECEFF1" size="2.8em">
                  <q-img
                    :src="
                      entity.profile.profile_img
                        ? img_url
                        : require('@/assets/basic_image.png')
                    "
                    @click="goToProfile"
                    class="cursor-pointer"
                  />
                </q-avatar>
              </span>
            </div>
            <div class="row col-10">
              <div class="q-pl-lg">
                <span
                  style="font-size: 14px; color: #464646"
                  @click="goToProfile"
                  class="cursor-pointer"
                  ><b>{{ entity.user.username }}</b></span
                >
                <div class="text-caption row">
                  {{ entity.written_time | moment('YYYY/MM/DD hh:mm') }}
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-4 row items-end justify-end items-md-baseline">
          <div class="icon-position q-mb-xs row items-center">
            <div class="q-mr-xs">
              <q-icon
                :name="$i.ionHeartOutline"
                style="color:#727272"
                size="22px"
              ></q-icon>
            </div>
            <div class="q-mr-md" style=" font-size: 13pt;">
              {{ entity.like_num }}
            </div>
            <div class="q-mr-sm">
              <q-icon
                :name="$i.ionChatboxEllipsesOutline"
                style="color:#727272"
                size="22px"
              ></q-icon>
            </div>
            <span style="font-size: 13pt;">{{ entity.comment_count }}</span>
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
      if (!this.$store.getters.isLogined) {
        alert('로그인이 필요합니다!');
        return;
      }
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
</style>
