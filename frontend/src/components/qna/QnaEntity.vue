<template>
  <div class="row col-12 " style="border: 1px solid #eaebef;">
    <div class="row col-7">
      <div
        class="full-height"
        :style="{
          'background-color': entity.solved ? '#1976D2' : '#C8DAFE',
          width: '25px',
        }"
      ></div>
      <div class="row col-11 q-pl-sm q-pt-xs">
        <div class="row text-weight-bold qna-title col-12 q-mb-xs">
          <span class="text-weight-thin text-grey-8">#{{ entity.id }}</span>
          <span class="cursor-pointer" @click="goToDetail">
            {{ entity.title }}
          </span>
        </div>

        <div class="row q-mr-xs q-gutter-sm q-mb-sm col-12">
          <span
            v-for="(tag, index) in entity.ref_tags"
            :key="index"
            :style="{ 'background-color': tagColor(tag, 0.5) }"
            style="font-size:0.8em; border-radius:3pt;"
            class="q-px-xs"
            >#{{ tag.charAt(0).toUpperCase() + tag.slice(1) }}</span
          >
        </div>
      </div>
    </div>
    <div class="row col-5 q-pl-sm">
      <div class="row col-2 items-center">
        <q-icon
          :name="entity.liked ? $i.ionHeart : $i.ionHeartOutline"
          size="sm"
          :color="entity.liked ? 'red-8' : 'grey-6'"
        ></q-icon>
        <span class="q-pl-xs text-grey-8" style="font-size:1.2em;">{{
          entity.like_num
        }}</span>
      </div>
      <div class="row col-2 items-center">
        <q-icon
          :name="$i.ionChatboxEllipsesOutline"
          size="sm"
          color="grey-6"
        ></q-icon>
        <span class="q-pl-xs text-grey-8" style="font-size:1.2em;">{{
          entity.comment_num
        }}</span>
      </div>
      <div class="row col-2  items-center ">
        <q-icon :name="$i.ionEyeOutline" size="sm" color="grey-6"></q-icon>
        <span class="q-pl-xs text-grey-8" style="font-size:1.2em;">{{
          entity.viewed_num | formatNumber
        }}</span>
      </div>
      <div class="row col-6 items-center justify-center q-py-xs ">
        <div class="col-4 row justify-end">
          <q-avatar style="border: 1px solid #ECEFF1" size="2.8em">
            <q-img
              :src="
                entity.profile.profile_img
                  ? entity.profile.profile_img
                  : require('@/assets/basic_image.png')
              "
              @click="goToProfile"
              class="cursor-pointer"
              style="height:40px;"
            />
          </q-avatar>
        </div>
        <div class="q-pl-sm col-8">
          <div
            class="text-weight-regular col-12 text-primary cursor-pointer"
            @click="goToProfile"
          >
            {{ entity.user.username }}
          </div>
          <div class="text-weight-thin col-12" style="font-size:8pt">
            {{ entity.written_time | moment('YYYY/MM/DD HH:mm') }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { colorSoloMapper } from '@/utils/tagColorMapper';
export default {
  props: {
    entity: Object,
  },
  data() {
    return {
      img_url: `${this.entity.profile.profile_img}`,
    };
  },
  methods: {
    tagColor(tag, alpha) {
      return colorSoloMapper(tag, alpha);
    },
    // TODO: 추후 연결 페이지 수정 필요
    goToDetail() {
      this.$router.push(`/qna-detail/${this.entity.id}`);
    },
    goToProfile() {
      this.$router.push(`/profile/${this.entity.user.id}`);
    },
  },
};
</script>

<style scoped>
.qna-title {
  display: block;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
