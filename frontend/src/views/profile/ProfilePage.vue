<template>
  <div class="row ">
    <!-- 백그라운드 파란색 헤더(장식) -->
    <div class="row  justify-center full-width"></div>
    <!-- 개인 정보가 담긴 배너 -->
    <div class="row justify-center full-width q-my-md">
      <header-banner :info="headerInfo" v-if="loaded"></header-banner>
    </div>
    <div class="row justify-center full-width q-my-md">
      <!-- 커뮤니티 활동 성향 관련 정보가 담긴 배너 -->
      <side-banner :info="sideInfo" v-if="loaded"></side-banner>
      <!-- 글과 댓글 정보가 담긴 배너 -->
      <post-banner :info="postInfo" v-if="loaded"></post-banner>
    </div>
  </div>
</template>

<script>
import HeaderBanner from '@/components/profile/HeaderBanner';
import SideBanner from '@/components/profile/SideBanner';
import PostBanner from '@/components/profile/PostBanner';
import { getProfile } from '@/api/profile.js';
// import { testCase } from '@/dummy/Profile';
export default {
  // 가짜 데이터
  data() {
    return {
      headerInfo: {},
      sideInfo: {},
      postInfo: {},
      loaded: false,
      followerData: [],
    };
  },
  computed: {},
  async created() {
    const id = this.$route.params.id;
    try {
      this.$q.loading.show();
      const { data } = await getProfile(id);
      this.headerInfo = {
        userId: data.user,
        username: data.username,
        region: data.region,
        group: data.group,
        email: data.email,
        links: data.link,
        joined: data.joined,
        followerNum: data.follower_num,
        followeeNum: data.followee_num,
        bio: data.bio,
        profileImg: data.profile_img,
        is_following: data.is_following,
      };
      this.sideInfo = {
        tags: data.tags,
        skills:
          typeof data.tech_stack == 'string'
            ? [data.tech_stack]
            : data.tech_stack,
        projects: data.project,
        postNum: data.qnas.length + data.forums.length,
        commentNum: data.qnas_comments.length + data.forums_comments.length,
        myTags: typeof data.my_tags == 'string' ? [data.my_tags] : data.my_tags,
      };
      this.postInfo = {
        qnas: data.qnas,
        comments: [...data.qnas_comments, ...data.forums_comments],
        qnas_pinned: data.pinned_qnas,
        forums_pinned: data.pinned_forums,
      };
      this.loaded = true;
    } catch (error) {
      console.log(error);
    } finally {
      this.$q.loading.hide();
    }
  },
  components: {
    HeaderBanner,
    SideBanner,
    PostBanner,
  },
};
</script>

<style scoped></style>
