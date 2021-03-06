<template>
  <div class="row col-12">
    <!-- 댓글 시작 -->
    <div class="row col-12" v-for="(data, index) in info" :key="index">
      <div class="row col-2">
        <!-- 댓글 좋아요 수, 댓글 수, 북마크 수 -->
        <div class="row col-9"></div>
        <div class="row col-3 q-mt-lg">
          <qna-comment-status :info="data"></qna-comment-status>
        </div>
      </div>
      <div class="row col-10">
        <div class="row col-9">
          <q-card flat bordered class="my-card q-pa-lg q-mt-lg row col-12">
            <div class="row col-10">
              <div class="q-ml-md row col-12 q-mt-sm">
                <span
                  class="text-body1 text-weight-bold cursor-pointer"
                  style="color: #585858"
                  @click="goToProfile(index)"
                >
                  @{{ data.user.username }}
                </span>
                <span
                  class="q-ml-sm text-caption"
                  style="color: gray; margin-top: 2px"
                >
                  {{ data.written_time | moment('YYYY/MM/DD HH:mm') }}
                  <!-- 답변 채택 버튼 -->

                  <span v-if="$store.state.id == author" class="q-ml-sm">
                    <template v-if="data.assisted">
                      <q-badge
                        color="blue"
                        @click="chooseComment(index)"
                        class="cursor-pointer"
                      >
                        채택 답변
                      </q-badge>
                      🥇
                    </template>
                    <template v-else>
                      <q-badge
                        color="grey-5"
                        @click="chooseComment(index)"
                        class="cursor-pointer"
                      >
                        채택 하기
                      </q-badge>
                    </template>
                  </span>
                  <span v-else-if="data.assisted" class="q-ml-sm">
                    <q-badge color="blue">
                      채택 답변
                    </q-badge>
                    🥇
                  </span>
                </span>
              </div>
            </div>

            <div class="row col-2 justify-end">
              <div v-if="data.user.id == $store.state.id">
                <q-btn flat round dense icon="more_vert">
                  <q-menu>
                    <q-list style="min-width: 100px">
                      <q-item
                        clickable
                        v-close-popup
                        @click="editerOpen(index)"
                      >
                        <q-item-section>수정하기</q-item-section>
                      </q-item>
                      <q-item
                        clickable
                        v-close-popup
                        @click="deleteQnaComment(index)"
                      >
                        <q-item-section>삭제하기</q-item-section>
                      </q-item>
                      <q-separator />
                    </q-list>
                  </q-menu>
                </q-btn>
              </div>
            </div>

            <div class="row col-12 justify-center">
              <v-md-editor
                v-if="modes[index] == 'preview'"
                :value="liquidResolve(data.content)"
                mode="preview"
                class="q-mb-md"
              >
              </v-md-editor>
              <markdown-editor
                v-else
                height="500px"
                :fetchData="data.content"
                @input="getContents(data, $event)"
                class="q-mb-md q-px-md"
              ></markdown-editor>
              <q-btn
                @click="updateQnaComment(index)"
                color="primary"
                v-if="modes[index] === 'editable'"
                >수정 완료</q-btn
              >
            </div>

            <!-- 큰 댓글의 작은 댓글 -->
            <q-card-section class="row col-12">
              <template v-if="data.anssmall_set.length">
                <div class="row full-width items-end q-mb-xs">
                  <q-icon
                    :name="$i.ionChatbubblesOutline"
                    style="color:#727272"
                    size="sm"
                  ></q-icon>
                  <span>댓글 {{ data.anssmall_set.length }}개</span>
                </div>
                <q-separator />
              </template>
              <qna-recomment
                :ans_id="data.id"
                :recomments="data.anssmall_set"
                @reloadRecomment="reloadRecomment(index)"
              ></qna-recomment>
            </q-card-section>
          </q-card>
        </div>
        <!-- 채택 댓글 프로필 -->
        <div v-if="data.assisted === true">
          <qna-comment-selected :info="data"></qna-comment-selected>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { toggleQnaCommentChoose } from '@/api/qna';
import QnaCommentSelected from '@/components/qna/QnaCommentSelected';
import QnaCommentStatus from '@/components/qna/QnaCommentStatus';
import QnaRecomment from '@/components/qna/QnaRecomment';
import { liquidResolver } from '@/utils/liquidTag';
import {
  loadQnaItem,
  updateQnaBigComment,
  deleteQnaBigComment,
  getRecomments,
} from '@/api/qna';
import MarkdownEditor from '@/components/common/MarkdownEditor';

export default {
  props: {
    info: Array,
  },
  components: {
    QnaCommentSelected,
    QnaCommentStatus,
    QnaRecomment,
    MarkdownEditor,
  },
  data() {
    const res = [];
    for (const i in this.info) res.push('preview');
    this.modes = res;
    return {
      text: '',
      follow: true,
      contents: '',
      content: '',
      qna: null,
      author: null,
      modes: res,
      ans_pk: null,
      recomments: Array,
      is_following: Boolean,
    };
  },
  methods: {
    goToProfile(index) {
      this.$router.push(`/profile/${this.info[index].user.id}`);
    },
    liquidResolve(tag) {
      return liquidResolver(tag);
    },
    getContents(fetchData, data) {
      fetchData.content = data;
    },
    editerOpen(index) {
      this.modes[index] = 'editable';
      this.modes = [...this.modes];
    },
    async updateQnaComment(index) {
      if (this.contents === '') {
        alert('내용은 필수 입력항목 입니다');
      }
      try {
        const ans_pk = this.info[index].id;
        const qnaId = this.info[index].qna;
        this.modes[index] = 'preview';
        this.modes = [...this.modes];
        this.$q.loading.show();
        await updateQnaBigComment(ans_pk, {
          content: this.info[index].content,
          qna: qnaId,
        });
      } catch (error) {
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },
    async deleteQnaComment(index) {
      try {
        this.$q.loading.show();
        const ans_pk = this.info[index].id;
        await deleteQnaBigComment(ans_pk);
        location.reload();
      } catch (error) {
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },
    async chooseComment(index) {
      try {
        for (let check of this.info) {
          if (check.assisted == true && !this.info[index].assisted) {
            check.assisted = false;
            await toggleQnaCommentChoose(check.id);
          }
        }
        const ans_pk = this.info[index].id;
        await toggleQnaCommentChoose(ans_pk);
        this.info[index].assisted = !this.info[index].assisted;
      } catch (error) {
        alert(error);
      }
    },
    async reloadRecomment(index) {
      try {
        this.recomments = await getRecomments(this.info[index].id);
      } catch (error) {
        alert(error);
      }
    },
  },
};
</script>

<style scoped></style>
