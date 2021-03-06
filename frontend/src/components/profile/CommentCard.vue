<template>
  <div class="row q-mb-sm q-pl-sm card-background">
    <div class="row justify-between q-pt-xs q-mb-xs">
      <div class="row items-center">
        <div class="q-mr-sm">@{{ username }},</div>
        <div>{{ detail.written_time | moment('YYYY/MM/DD HH:mm') }}</div>
      </div>
    </div>
    <div
      class="row text-bold q-mb-sm full-width cursor-pointer"
      style="font-size:14pt;"
      @click="$router.push(`/${detail.type}-detail/${detail.post_id}`)"
    >
      <span>[{{ detail.type }}] </span>
      {{ detail.title }}
    </div>
    <div
      class="row text-weight-thin q-mb-sm text-grey-8 q-pr-lg comment-content"
    >
      댓글: {{ detail.content }}
    </div>
  </div>
</template>

<script>
export default {
  props: {
    username: String,
    detail: Object,
  },
};
</script>

<style scoped>
.comment-content {
  display: block;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.card-background {
  width: 100%;
  border: 1px solid #c1b9b9;
  border-radius: 8px;
}
</style>
