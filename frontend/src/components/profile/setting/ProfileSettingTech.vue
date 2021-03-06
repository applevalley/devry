<template>
  <div class="full-width q-mb-xl">
    <div class="text-h6 text-weight-bold q-mb-md">
      Tech Stack
    </div>
    <div class="full-width row q-mb-sm">
      <q-input
        class=" col-11"
        outlined
        stack-label
        label-slot
        v-model="techStack"
        placeholder="보유하신 기술을 입력해주세요"
        @keypress.enter.prevent="addTechStack"
      >
        <template v-slot:label>
          <span class="text-primary">
            Skills/Language
          </span>
          <br />
        </template>
      </q-input>
      <div class="col-1 q-pl-sm row justify-end items-center">
        <q-btn
          class="overflow-auto"
          color="primary"
          icon="add"
          @click="addTechStack"
          style="height:100%"
        />
      </div>
    </div>
    <div class="row col-12">
      <div class="row col-3 bg-light-blue-1 auto-tag">
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
    <ul class="row q-gutter-sm">
      <li
        v-for="(skill, index) in propsTechStackData"
        :key="index"
        class="cursor-pointer"
      >
        <q-badge color="light-blue-8" class="q-pa-sm shadow-3">
          {{ skill }}
          <span @click="removeTechStack(skill, index)" class="q-ml-sm">X</span>
        </q-badge>
      </li>
    </ul>
  </div>
</template>

<script>
import { filtered_tags, first_matched_tag } from '@/utils/autoComplete';
export default {
  props: {
    propsTechStackData: Array,
  },
  data() {
    return {
      techStack: '',
      techStacks: [],
      tags: { ...this.$store.state.tags_selected },
    };
  },
  methods: {
    addTechStack: function() {
      if (this.techStack !== '') {
        const str = first_matched_tag(this.techStack);
        this.checkDuplicateTag(str);
      }
    },
    removeTechStack: function(skill, index) {
      this.techStacks.splice(index, 1);
      this.$emit('removeTechStackItem', skill, index);
    },
    checkDuplicateTag(stack) {
      if (stack && this.techStacks.indexOf(stack) < 0) {
        this.techStacks.push(stack);
        this.$emit('addTechStackItem', stack);
        this.techStack = '';
      }
    },
  },
  watch: {
    propsTechStackData(newValue) {
      this.techStacks = newValue;
    },
  },
  computed: {
    // 일부 문자열을 받고 정규 표현식을 활용하여 비슷한 형태의 문자열 목록을 반환
    suggests() {
      return filtered_tags(this.techStack);
    },
  },
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
.auto-tag {
  position: absolute;
  z-index: 999;
  border-radius: 5px;
}
</style>
