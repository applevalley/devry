<template>
  <div class="row q-mb-sm post-card-frame">
    <div class="full-width q-pl-sm row content-between wrap">
      <div class="row justify-between q-pt-xs q-mb-sm col-12">
        <div class="row items-baseline q-mb-sm">
          <div class="q-mr-sm text-weight-regular">@{{ username }}</div>
          <div class="text-weight-thin" style="font-size:8pt">
            {{ detail.written_time | moment('YYYY/MM/DD') }}
          </div>
        </div>
        <div class="row">
          <div class="row items-center q-mr-sm">
            <template v-if="detail.liked">
              <q-icon
                :name="$i.ionHeart"
                color="red"
                size="20px"
                class="cursor-pointer"
                @click="checkLiked(index)"
              ></q-icon>
            </template>
            <template v-else>
              <q-icon
                :name="$i.ionHeartOutline"
                style="color:#727272"
                size="20px"
                class="cursor-pointer"
                @click="checkLiked(index)"
              ></q-icon>
            </template>
            <span>{{ detail.like_num }}</span>
          </div>
          <div class="row items-center q-mr-md">
            <q-icon
              :name="$i.ionChatboxEllipsesOutline"
              style="color:#617E9F"
              size="22px"
              class="q-mr-sm"
            ></q-icon>
            <span>{{ detail.comment_num }}</span>
          </div>

          <div class="row items-center q-mr-md cursor-pointer">
            <q-icon
              :name="$i.ionAttachOutline"
              :style="{ color: pinned ? '#B54333' : '#bbbbbb' }"
              size="22px"
              class="q-mr-xs"
              @click="togglePin"
            ></q-icon>
          </div>
        </div>
      </div>
      <div
        class="row text-bold col-12 q-px-md q-mb-xs cursor-pointer"
        style="font-size:14pt; height:80px"
        @click="$router.push(`/qna-detail/${detail.id}`)"
      >
        {{ detail.title }}
      </div>
      <div class="row justify-end items-end col-12">
        <span
          v-for="tag in detail.tags"
          class="q-mr-sm q-mb-sm q-px-xs tag-color"
          :style="{ 'background-color': tagColor(tag) }"
          :key="tag"
          >#{{ tag }}</span
        >
      </div>
    </div>
  </div>
</template>

<script>
import { colorSoloMapper } from '@/utils/tagColorMapper';
import { togglePinned } from '@/api/qna';
export default {
  props: {
    username: String,
    detail: Object,
  },
  data() {
    return {
      pinned: this.detail.pinned,
    };
  },
  methods: {
    tagColor(tag) {
      return colorSoloMapper(tag, 0.2);
    },
    async togglePin() {
      try {
        await togglePinned(this.detail.id);
        this.pinned = !this.pinned;
      } catch (error) {
        alert(error);
      }
    },
  },
};
</script>

<style scoped>
.post-card-frame {
  width: 100%;
  height: 110px;
  border: 1px solid #c1b9b9;
  border-radius: 8px;
}
.tag-color {
  font-size: 10pt;
  border-radius: 5pt;
}
</style>
