<template>
  <div class="row col-12">
    <div class="row col-12 q-mb-sm">
      <div
        class="row col-12 q-py-sm"
        v-for="(data, index) in commentList"
        :key="index"
      >
        <div class="row col-12 justify-between">
          <div class="row col-10">
            <span class="q-mr-xs">{{ index + 1 }}.</span>
            <span class="q-mr-sm text-weight-bold" style="color: #585858">
              @{{ data.user.username }}
            </span>
            <span class="text-caption" style="color: gray">
              {{ data.written_time | moment('YYYY/MM/DD HH:mm') }}
            </span>
            <template v-if="data.user.id == $store.state.id">
              <span class="q-ml-sm">
                <q-icon
                  :name="$i.ionCreateOutline"
                  class="cursor-pointer"
                  size="17px"
                  style="color: #727272"
                  @click="editComment(index)"
                >
                </q-icon>
              </span>
              <span class="q-ml-sm">
                <q-icon
                  :name="$i.ionTrashOutline"
                  class="cursor-pointer"
                  size="16px"
                  style="color: #727272"
                  @click="deleteComment(data.id)"
                >
                </q-icon>
              </span>
            </template>
          </div>
        </div>
        <div class=" q-py-xs row col-12" v-if="editables[index]">
          <q-input
            clearable
            clear-icon="close"
            type="textarea"
            v-model="data.content"
            class="full-width q-pa-none "
            color="blue-10"
            dense
            autogrow
            borderless
            @keypress.enter="
              updateComment($event, data.id, index, data.content)
            "
          />
        </div>
        <pre class=" q-py-xs row col-12 q-my-none" v-else>{{
          data.content
        }}</pre>
      </div>
    </div>
    <q-separator />
    <div class="q-mt-sm row col-12">
      <div class="row col-12">
        <q-input
          borderless
          v-model="newComment"
          autogrow
          placeholder="댓글을 입력해주세요"
          class="full-width"
          @keypress.enter="registerComment"
        />
      </div>
    </div>
  </div>
</template>

<script>
import {
  registerSmallComment,
  deleteSmallComment,
  updateSmallComment,
  getSmallComments,
} from '@/api/qna';
export default {
  props: {
    comments: Array,
    user_id: Number,
    post_id: Number,
    username: String,
  },
  data: function() {
    const res = [];
    for (const i in this.comments) res.push(false);
    return {
      newComment: '',
      editables: [...res],
      updatedContent: '',
      commentList: this.comments,
    };
  },
  methods: {
    editComment(index) {
      this.editables[index] = true;
      this.editables = [...this.editables];
    },
    closeEditor(index) {
      this.editables[index] = false;
      this.editables = [...this.editables];
    },
    async registerComment(e) {
      if (e.shiftKey) return;
      if (!this.$store.getters.isLogined) {
        alert('로그인을 해주세요');
        return;
      }
      try {
        await registerSmallComment({
          qna: this.post_id,
          content: this.newComment,
          user: this.$store.state.id,
        });
        this.newComment = '';
        this.getComments();
      } catch (error) {
        alert(error);
      }
    },
    async getComments() {
      try {
        const { data } = await getSmallComments(this.post_id);
        this.commentList = data;
      } catch (error) {
        alert(error);
      }
    },
    async updateComment(e, quset_small_id, index, content) {
      if (e.shiftKey) return;
      try {
        await updateSmallComment(quset_small_id, {
          qna: this.post_id,
          content,
          user: this.$store.state.id,
        });

        this.getComments();
        this.closeEditor(index);
      } catch (error) {
        alert(error);
      }
    },
    async deleteComment(quset_small_id) {
      try {
        await deleteSmallComment(quset_small_id);
        this.getComments();
      } catch (error) {
        alert(error);
      }
    },
  },
};
</script>

<style scoped>
.q-input >>> input {
  padding: 0;
}
</style>
