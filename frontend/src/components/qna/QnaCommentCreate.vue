<template>
  <div class="row col-12">
    <div class="row col-12 q-mt-xl q-pr-md">
      <div class="row col-2"></div>
      <div class="row col-8 q-pr-xl">
        <div class="text-h6 text-weight-bold q-mb-md">새 답변 작성하기</div>

        <markdown-editor
          @input="getContents"
          :height="'400px'"
        ></markdown-editor>
      </div>
      <div class="row col-2"></div>

      <!-- 제출 버튼 -->
      <div class="row col-9 q-mt-lg q-pl-xl">
        <div class="row col-3"></div>
        <div class="row col-9">
          <div class="row col-12 q-mb-xl">
            <div style="margin:0 auto;">
              <q-btn
                no-caps
                color="primary"
                id="follow-btn"
                label="답변 작성하기"
                style="width: 200px"
                class="q-mb-xl q-mt-lg"
                @click="createBigComment"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { createQnaBigComment } from '@/api/qna';
import MarkdownEditor from '@/components/common/MarkdownEditor';

export default {
  components: { MarkdownEditor },
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
    async createBigComment() {
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
        await createQnaBigComment({
          // 넘길 데이터
          user: this.$store.state.id,
          content: this.content,
          qna: this.info.post_id,
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
