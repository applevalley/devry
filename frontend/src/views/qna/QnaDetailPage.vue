<template>
  <div class="row col-12">
    <div class="row col-12">
      <div class="row col-2 q-mt-lg">
        <div class="row col-9"></div>
        <div class="row col-3">
          <qna-detail-status :info="status"></qna-detail-status>
        </div>
      </div>
      <div class="row col-10 q-mt-lg ">
        <div class="row col-9">
          <div class="row col-12">
            <qna-detail-content :info="questBody"></qna-detail-content>
          </div>
        </div>
        <div class="row col-3 q-pl-sm q-pr-xl">
          <qna-short-profile :info="shortProfile"></qna-short-profile>
        </div>
      </div>
    </div>
    <div class="row col-12">
      <qna-big-comment :info="bigComments"></qna-big-comment>
    </div>
    <div class="row col-12">
      <qna-comment-create :info="createBigComments"></qna-comment-create>
    </div>
  </div>
</template>

<script>
import QnaDetailContent from '@/components/qna/QnaDetailContent';
import QnaShortProfile from '@/components/qna/QnaShortProfile';
import QnaBigComment from '@/components/qna/QnaBigComment';
import QnaDetailStatus from '@/components/qna/QnaDetailStatus';
import QnaCommentCreate from '@/components/qna/QnaCommentCreate';
import { loadQnaItem } from '@/api/qna';
export default {
  components: {
    QnaDetailContent,
    QnaShortProfile,
    QnaBigComment,
    QnaDetailStatus,
    QnaCommentCreate,
  },
  data() {
    return {
      contents: '',
      writerStatus: false,
    };
  },
  methods: {
    goToProfile() {
      this.$router.push({ name: 'Profile' });
    },
  },
  computed: {
    status() {
      return {
        like_num: this.contents.like_num,
        liked: this.contents.liked,
        bookmarked: this.contents.bookmarked,
        bookmark_num: this.contents.bookmark_num,
        viewed_num: this.contents.viewed_num,
        comment_num: this.contents.comment_num,
        post_id: this.contents.id,
      };
    },
    questBody() {
      return {
        title: this.contents.title,
        ref_tags: this.contents.ref_tags,
        contents: this.contents.content,
        comments: this.contents.qnasmall_set,
        written_time: this.contents.written_time,
        solved: this.contents.solved,
        user_id: this.contents.user.id,
        user_name: this.contents.user.username,
        post_id: this.contents.id,
      };
    },
    shortProfile() {
      return {
        profile: this.contents.profile,
        user: this.contents.user,
        post_id: this.contents.id,
        is_following: this.contents.is_following,
      };
    },
    bigComments() {
      return this.contents.ans_set;
    },
    createBigComments() {
      return {
        post_id: this.contents.id,
      };
    },
  },
  async created() {
    const index = this.$route.params.id;
    try {
      const { data } = await loadQnaItem(index);
      this.contents = data;
    } catch (error) {
      alert(error);
    }
    this.$store.commit('offLeft');
  },
};
</script>

<style scoped>
.icon-position {
  float: right;
}
</style>
