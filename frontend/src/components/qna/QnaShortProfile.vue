<template>
  <div>
    <q-card
      flat
      bordered
      class="my-card row col-12 q-pa-sm q-mb-sm"
      style="max-width: 250px; max-height: 280px;"
    >
      <q-card-section>
        <div class="row col-12">
          <div class="row col-2">
            <span class="q-mt-xs">
              <q-avatar style="border: 1px solid #ECEFF1" size="2.8em">
                <q-img
                  :src="
                    info.profile.profile_img
                      ? img_url
                      : require('@/assets/basic_image.png')
                  "
                  @click="goToProfile"
                  class="cursor-pointer"
                  style="width: 40px; height: 40px;"
                />
              </q-avatar>
            </span>
          </div>
          <div class="row col-10">
            <div class="row col-12">
              <div
                class="q-pl-lg"
                style="font-size: 15px; color: #464646"
                @click="goToProfile"
              >
                <b class="cursor-pointer">{{
                  profile ? profile.username : info.user.username
                }}</b>
                <div class="text-caption row">
                  팔로잉 {{ info.user.followee_num }} · 팔로워
                  {{ follower_num }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </q-card-section>
      <div class="q-px-md q-pb-md" v-if="profile">
        <div style="font-size: 13px;">
          {{ info.profile.bio }}
        </div>
      </div>
      <div
        class="row col-12 justify-center"
        v-if="info.profile.user != $store.state.id"
      >
        <template v-if="is_following">
          <q-btn
            no-caps
            outline
            color="primary"
            label="Following"
            @click="checkFollow"
            class="q-mb-sm row col-10"
          />
        </template>
        <template v-else>
          <q-btn
            no-caps
            color="primary"
            id="follow-btn"
            label="Follow"
            @click="checkFollow"
            class="q-mb-sm row col-10"
          />
        </template>
      </div>
    </q-card>
    <template
      v-if="
        info.profile.pinned_forums.length > 0 ||
          info.profile.pinned_qnas.length > 0
      "
    >
      <q-card
        flat
        bordered
        class="my-card row col-12 q-px-sm q-pt-md"
        style="max-width: 250px; max-height: 280px;"
      >
        <div class="q-px-md q-pb-sm row col-12">
          <div class="q-my-sm">
            <span
              class="text-weight-bold cursor-pointer"
              style="color: #598FFC"
              >{{ info.profile.username }}</span
            >
            <span>님의 글 더보기</span>
          </div>
          <template v-for="(post, index) in info.profile.pinned_forums">
            <q-separator :key="post.title" />
            <div class="q-my-sm" :key="post.title">
              <span class="cursor-pointer" @click="goToForum(index)">{{
                post.title
              }}</span>
            </div>
          </template>
          <template v-for="(qna, index) in info.profile.pinned_qnas">
            <q-separator :key="qna.title" />
            <div class="q-my-sm" :key="qna.title">
              <span class="cursor-pointer" @click="goToQna(index)">{{
                qna.title
              }}</span>
            </div>
          </template>
        </div>
      </q-card>
    </template>
  </div>
</template>

<script>
import { checkQnaFollowing } from '@/api/qna';

export default {
  props: {
    info: Object,
  },
  data() {
    return {
      is_following: this.info.is_following,
      follower_num: this.info.user.follower_num,
      img_url: `${this.info.profile.profile_img}`,
    };
  },
  methods: {
    async checkFollow() {
      if (!this.$store.getters.isLogined) {
        alert('로그인을 해주세요');
        return;
      }
      try {
        await checkQnaFollowing(this.info.post_id);
        this.is_following = !this.is_following;
        if (this.is_following) {
          this.follower_num = this.follower_num + 1;
        } else {
          this.follower_num = this.follower_num - 1;
        }
      } catch (error) {
        alert(error);
      }
    },
    goToProfile() {
      this.$router.push(`/profile/${this.info.profile.user}`);
    },
    goToForum(index) {
      this.$router.push(
        `/forum-detail/${this.info.profile.pinned_forums[index].id}`,
      );
    },
    goToQna(index) {
      this.$router.push(
        `/qna-detail/${this.info.profile.pinned_qnas[index].id}`,
      );
      location.reload();
    },
  },
  computed: {
    profile() {
      return this.info.profile;
    },
  },
};
</script>

<style scoped></style>
