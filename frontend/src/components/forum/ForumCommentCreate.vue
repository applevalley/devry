<template>
  <div class="row col-12">
    <div class="row col-12 q-mt-md q-pr-md">
      <div class="row col-2"></div>
      <div class="row col-8 q-pr-xl">
        <div class="text-h6 text-weight-bold q-mb-sm">댓글 작성하기</div>
        <q-input
          outlined
          flat
          type="textarea"
          placeholder="댓글을 입력해주세요"
          class="full-width"
          @input="getContents"
        />
      </div>
      <div class="row col-2"></div>

      <!-- 제출 버튼 -->
      <div class="row col-2"></div>
      <div class="row col-8 justify-end ">
        <q-btn
          no-caps
          color="primary"
          label="댓글 작성하기"
          class="q-mb-md q-mt-md q-mr-xl"
          style="width: 150px;"
          @click="createComment"
        />
      </div>
      <div class="row col-1"></div>
    </div>
  </div>
</template>

<script>
import { createForumComment } from '@/api/forum';

export default {
  props: {
    info: Object,
  },
  data() {
    return {
      content: '',
    };
  },
  methods: {
    getContents(data) {
      this.content = data;
    },
    async createComment() {
      if (!this.$store.getters.isLogined) {
        alert('로그인을 해주세요');
        return;
      }
      if (this.content === '') {
        alert('댓글 내용을 작성해주세요.');
        return;
      }
      try {
        this.$q.loading.show();
        await createForumComment({
          user: this.$store.state.id,
          comment_content: this.content,
          post: this.info.post_id,
        });
        location.reload();
      } catch (error) {
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },
  },
};
</script>

<style scoped></style>
