<template>
  <div class="row col-12">
    <!-- 댓글 시작 -->
    <div v-for="(data, index) in info" :key="index" class="row col-12">
      <div class="row col-12">
        <!-- <div class="row col-12" v-for="(data, index) in info" :key="index"> -->
        <div class="row col-2">
          <!-- 댓글 좋아요 수, 댓글 수, 북마크 수 -->
          <div class="row col-9"></div>
          <div class="row col-3 q-mt-lg">
            <forum-comment-status :info="data"></forum-comment-status>
          </div>
        </div>
        <div class="row col-10">
          <div class="row col-9">
            <q-card flat bordered class="my-card q-pa-lg q-mt-lg row col-12">
              <div class="row col-11 q-mt-sm">
                <div class="row col-12">
                  <div class="col-1">
                    <span class="cursor-pointer q-ml-sm">
                      <q-avatar size="lg"
                        ><img src="https://cdn.quasar.dev/img/avatar.png" />
                      </q-avatar>
                    </span>
                  </div>
                  <!-- <q-card flat bordered class="my-card col-11 q-pa-lg"> -->
                  <span class="text-body1 text-weight-bold">{{
                    data.username
                  }}</span>
                  <span class="q-ml-sm text-caption" style="color: gray">{{
                    data.written_time | moment('YYYY/MM/DD HH:mm')
                  }}</span>
                  <!-- <div class="row col-12 q-mt-md q-ml-sm">
                    {{ data.comment_content }}
                  </div> -->
                  <!-- </q-card> -->
                </div>
              </div>

              <div class="row col-1 justify-end">
                <div v-if="data.user == $store.state.id">
                  <div>
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
                            @click="deleteComment(index)"
                          >
                            <q-item-section>삭제하기</q-item-section>
                          </q-item>
                        </q-list>
                      </q-menu>
                    </q-btn>
                  </div>
                </div>
              </div>

              <div class=" q-py-xs row col-12" v-if="editables[index]">
                <q-input
                  clearable
                  clear-icon="close"
                  type="textarea"
                  v-model="data.comment_content"
                  class="full-width q-pa-none "
                  color="blue-10"
                  dense
                  autogrow
                  borderless
                  @keypress.enter="
                    updateComment($event, data.id, index, data.comment_content)
                  "
                />
              </div>
              <pre class=" q-py-xs row col-12 q-my-none" v-else>{{
                data.comment_content
              }}</pre>
              <!-- <div class="row col-12 justify-center">
                <markdown-editor
                  v-if="modes[index] == 'editable'"
                  height="500px"
                  :fetchData="data.comment_content"
                  @input="getContents(data, $event)"
                  class="q-mb-md q-px-md"
                ></markdown-editor>
                <v-md-editor
                  v-else
                  :value="liquidResolve(data.comment_content)"
                  mode="preview"
                  class="q-mb-md"
                >
                </v-md-editor>

                <q-btn
                  @click="updateComment(index)"
                  color="primary"
                  v-if="modes[index] === 'editable'"
                  >수정 완료</q-btn
                >
              </div>

              <div class="q-ml-md row col-12">
                <q-card-section class="row col-12">
                  <q-markdown :src="info.comment_content"> </q-markdown>
                </q-card-section>
              </div> -->
            </q-card>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ForumCommentStatus from '@/components/forum/ForumCommentStatus';
import {
  loadForumItem,
  updateForumComment,
  deleteForumComment,
  getForumComment,
} from '@/api/forum';
import { liquidResolver } from '@/utils/liquidTag';
// import MarkdownEditor from '@/components/common/MarkdownEditor';

export default {
  props: {
    info: Array,
  },
  components: {
    ForumCommentStatus,
    // MarkdownEditor,
  },
  data() {
    const res = [];
    for (const i in this.info) res.push('preview');
    this.modes = res;
    return {
      contents: '',
      content: '',
      modes: res,
    };
  },
  methods: {
    liquidResolve(tag) {
      return liquidResolver(tag);
    },
    getContents(fetchData, data) {
      fetchData.comment_content = data;
    },
    editerOpen(index) {
      this.modes[index] = 'editable';
      this.modes = [...this.modes];
    },
    async updateComment(e, comment_pk, index, content) {
      if (e.shiftKey) return;
      try {
        const postId = this.info[index].post;
        await updateForumComment(comment_pk, {
          // comment_content: this.info[index].comment_content,
          comment_content: content,
          post: postId,
          user: this.$store.state.id,
        });

        this.getComments();
        this.closeEditor(index);
      } catch (error) {
        console.log(error);
      }
    },

    // async updateComment(index) {
    //   if (this.info[index].comment_content === '') {
    //     alert('내용은 필수 입력항목 입니다');
    //   }
    //   console.log(this.info)
    //   try {
    //     // const comment_pk = this.info[index].id;
    //     const postId = this.info[index].post;
    //     this.modes[index] = 'preview';
    //     this.modes = [...this.modes];
    //     this.$q.loading.show();
    //     await updateForumComment(index, {
    //       comment_content: this.info[index].comment_content,
    //       post: postId,
    //       user: this.author,
    //     });
    //   } catch (error) {
    //     console.log(error);
    //   } finally {
    //     this.$q.loading.hide();
    //   }
    // },
    async deleteComment(index) {
      try {
        this.$q.loading.show();
        const comment_pk = this.info[index].id;
        await deleteForumComment(comment_pk);
        location.reload();
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },
  },
  async created() {
    // const index = this.$route.params.id;
    try {
      // const { data } = await loadForumItem(index);
      const { data } = await getForumComment();
      this.contents = data;
      console.log(this.contents)
      this.author = data.user.id;
    } catch (error) {
      console.log(error);
    }
  },
};
</script>

<style scoped>
.icon-position {
  float: right;
}
</style>
