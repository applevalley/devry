<template>
  <div class="row full-width">
    <q-card flat bordered class="my-card q-px-lg q-pt-xs row col-12">
      <div class="row col-11 q-mt-xl"></div>
      <div v-if="info.user_id == $store.state.id" class="row col-1 justify-end">
        <q-btn flat round dense icon="more_vert" class="q-mt-md">
          <q-menu>
            <q-list style="min-width: 100px">
              <q-item clickable v-close-popup @click="qnaPostEdit">
                <q-item-section>수정하기</q-item-section>
              </q-item>
              <q-item clickable v-close-popup @click="deleteQna">
                <q-item-section>삭제하기</q-item-section>
              </q-item>
              <q-separator />
            </q-list>
          </q-menu>
        </q-btn>
      </div>

      <q-card-section class="row col-12 q-py-none q-mb-sm">
        <div class="row col-12 text-h4 text-weight-bold q-mb-sm">
          <span>
            {{ info.title }}
          </span>

          <div v-if="info.solved" class="q-ml-lg">
            <q-badge color="blue" align="middle">
              답변 완료 ✔
            </q-badge>
          </div>
          <div v-else class="q-ml-lg">
            <q-badge color="primary" outline align="middle">
              답변 대기
            </q-badge>
          </div>
        </div>
        <div class="text-subtitle2 text-grey-6 q-mb-md">
          {{ info.written_time | moment('YYYY/MM/DD HH:mm') }}
        </div>
      </q-card-section>
      <q-card-section class="q-pa-none full-width q-mb-sm">
        <div class="q-ml-sm">
          <span v-for="tag in info.ref_tags" :key="tag" class="q-px-xs">
            <q-badge
              class="q-pa-sm text-black"
              :style="{ 'background-color': tagColor(tag, 0.5) }"
              style="font-size:1em; border-radius:3pt;"
            >
              # {{ tag }}
            </q-badge>
          </span>
        </div>
      </q-card-section>
      <div class="row col-12">
        <v-md-editor :value="liquidResolve(content)" mode="preview">
        </v-md-editor>
      </div>
      <q-card-section class="row col-12">
        <template v-if="info.comments.length">
          <div class="row full-width items-end q-mb-xs">
            <q-icon
              :name="$i.ionChatbubblesOutline"
              style="color:#727272"
              size="sm"
            ></q-icon>
            <span>댓글 {{ info.comments.length }}개</span>
          </div>
          <q-separator />
        </template>
        <qna-small-comment
          :comments="comments"
          :user_id="info.user_id"
          :post_id="info.post_id"
          :username="info.username"
          @reloadSmallAns="reloadSmallAns"
        ></qna-small-comment>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
import QnaSmallComment from '@/components/qna/QnaSmallComment';
import { colorSoloMapper } from '@/utils/tagColorMapper';
import { getSmallComments, deleteQnaItem } from '@/api/qna';
import { liquidResolver } from '@/utils/liquidTag';
export default {
  props: {
    info: Object,
  },
  components: {
    QnaSmallComment,
  },
  data: function() {
    return {
      content: this.info.contents,
      msg: true,
      comments: this.info.comments,
      solved: this.info.solved,
      tags: ['Vue', 'Javascript', 'Typescript'],
      writerStatus: false,
    };
  },
  methods: {
    liquidResolve(tag) {
      return liquidResolver(tag);
    },
    tagColor(tag, alpha) {
      return colorSoloMapper(tag, alpha);
    },
    qnaPostEdit() {
      this.$router.push(`/qna/${this.info.post_id}`);
    },
    async reloadSmallAns() {
      try {
        this.comments = await getSmallComments(this.info.post_id);
      } catch (error) {
        alert(error);
      }
    },
    async deleteQna() {
      try {
        const post_id = this.$route.params.id;
        this.$q.loading.show();
        await deleteQnaItem(post_id);
        // 이동 시킬 페이지 적어주기(QnA 게시판으로 이동)
        this.$router.push({ path: '/qna' });
      } catch (error) {
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },
  },
};
</script>

<style scoped>
.icon-position {
  float: right;
}
</style>
