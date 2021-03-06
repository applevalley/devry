<template>
  <div class="full-width q-mb-xl">
    <div class="text-h6 text-weight-bold q-mb-sm">
      Related Tags
    </div>
    <div class="row full-width q-mb-sm">
      <q-input
        outlined
        stack-label
        label-slot
        v-model="tagItem"
        placeholder="태그를 입력해주세요"
        @keypress.enter="createTag"
        class="col-11"
      >
        <template v-slot:label>
          <span class="text-primary">
            관련 태그
          </span>
          <br />
        </template>
      </q-input>
      <div class="col-1 q-pl-sm row justify-end items-center">
        <q-btn
          class="overflow-auto"
          color="primary"
          icon="add"
          @click="createTag"
          style="height:100%"
        />
      </div>
    </div>
    <!-- 자동 완성 -->
    <div class="row col-12">
      <div
        class="row col-3 bg-light-blue-1"
        style="position: absolute; z-index:999; border-radius: 5px;"
      >
        <div
          v-for="tag in suggests"
          class="col-12 q-py-md q-px-md"
          :class="{ 'bg-blue-3': tags[tag] }"
          :key="tag"
          @click="checkDuplicateTag(tag)"
          @mouseover="tags[tag] = true"
          @mouseout="tags[tag] = false"
        >
          {{ tag }}
        </div>
      </div>
    </div>
    <div>
      <ul class="row q-gutter-sm">
        <li
          v-for="(tag, index) in propsTagData"
          :key="index"
          class="cursor-pointer"
        >
          <q-badge
            class="text-black q-pa-sm shadow-3"
            :style="{
              'background-color': tagColor(tag),
            }"
          >
            # {{ tag }}
            <span @click="removeTag(tag, index)" class="q-ml-sm">X</span>
          </q-badge>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { colorSoloMapper } from '@/utils/tagColorMapper';
import { filtered_tags, first_matched_tag } from '@/utils/autoComplete';
export default {
  props: ['propsTagData'],
  data() {
    return {
      tagItem: '',
      tags: { ...this.$store.state.tags_selected },
      ref_tags: [],
    };
  },
  methods: {
    createTag: function() {
      if (this.tagItem !== '') {
        const str = first_matched_tag(this.tagItem);
        this.checkDuplicateTag(str);
      }
    },
    removeTag: function(tag, index) {
      this.ref_tags.splice(index, 1);
      this.$emit('removeTagItem', tag, index);
    },
    tagColor(tag) {
      return colorSoloMapper(tag, 0.5);
    },
    // 태그 중복 확인
    checkDuplicateTag(tag) {
      if (tag && this.ref_tags.indexOf(tag) < 0) {
        this.ref_tags.push(tag);
        this.$emit('addTagItem', tag);
        this.tagItem = '';
      }
    },
  },
  computed: {
    // 일부 문자열을 받고 정규 표현식을 활용하여 비슷한 형태의 문자열 목록을 반환
    suggests() {
      return filtered_tags(this.tagItem);
    },
  },
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
</style>
