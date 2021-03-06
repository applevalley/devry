<template>
  <div class="row col-12">
    <div class="row col-12">
      <div class="row col-2 q-mt-lg">
        <div class="row col-9"></div>
        <div class="row col-3">
          <forum-detail-status
            :info="status"
            v-if="loaded"
          ></forum-detail-status>
        </div>
      </div>
      <div class="row col-10 q-mt-lg">
        <div class="col-9">
          <div class="row col-12">
            <forum-detail-content
              :info="forumBody"
              v-if="loaded"
            ></forum-detail-content>
          </div>
        </div>
        <div class="col-3 q-pl-sm q-pr-xl">
          <forum-short-profile
            :info="shortProfile"
            :followingStatus="followingStatus"
            :followerNum="followerNum"
            v-if="loaded"
          ></forum-short-profile>
        </div>
      </div>
    </div>
    <div class="row col-12 q-my-lg">
      <forum-comment-create
        :info="createComments"
        v-if="loaded"
      ></forum-comment-create>
    </div>
    <div class="row col-12 q-mb-xl">
      <forum-comment :info="comments" v-if="loaded"></forum-comment>
    </div>
  </div>
</template>

<script>
import ForumComment from '@/components/forum/ForumComment';
import ForumDetailStatus from '@/components/forum/ForumDetailStatus';
import ForumDetailContent from '@/components/forum/ForumDetailContent';
import ForumCommentCreate from '@/components/forum/ForumCommentCreate';
import ForumShortProfile from '@/components/forum/ForumShortProfile';
import { loadForumItem } from '@/api/forum';

export default {
  components: {
    ForumComment,
    ForumDetailStatus,
    ForumDetailContent,
    ForumCommentCreate,
    ForumShortProfile,
  },
  data() {
    return {
      contents: '',
      status: '',
      forumBody: '',
      comments: '',
      shortProfile: '',
      followingStatus: '',
      loaded: false,
    };
  },
  computed: {
    createComments() {
      return {
        post_id: this.contents.id,
      };
    },
  },
  async created() {
    const index = this.$route.params.id;
    try {
      const { data } = await loadForumItem(index);
      this.contents = data;
      this.status = this.contents;
      this.forumBody = this.contents;
      this.shortProfile = this.contents.profile;
      this.followerNum = this.contents.user.follower_num;
      this.followingStatus = this.contents.is_following;
      this.comments = this.contents.comment_set;
      this.loaded = true;
    } catch (error) {
      alert(error);
    }
    this.$store.commit('offLeft');
  },
};
</script>

<style scoped></style>
