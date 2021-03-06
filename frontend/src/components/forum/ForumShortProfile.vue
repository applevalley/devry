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
            <span style="cursor:pointer;" class="q-mt-xs">
              <q-avatar style="border: 1px solid #ECEFF1" size="2.8em">
                <q-img
                  :src="
                    info.profile_img
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
                style="font-size: 15px; cursor:pointer; color: #464646"
                @click="goToProfile"
              >
                <b>{{ info.username }}</b>
                <div class="text-caption">
                  글 {{ info.post_num }} · 팔로워 {{ followerNum }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </q-card-section>
      <div class="q-px-md q-pb-md" v-if="info.bio">
        <div style="font-size: 13px;">
          {{ info.bio }}
        </div>
      </div>
      <div
        class="row col-12 justify-center"
        v-if="info.user != $store.state.id"
      >
        <template v-if="followingStatus == false">
          <q-btn
            no-caps
            color="primary"
            id="follow-btn"
            label="Follow"
            @click="toggleFollow"
            style="width: 200px"
            class="q-mb-sm row col-10"
          />
        </template>
        <template v-else>
          <q-btn
            no-caps
            outline
            color="primary"
            label="Following"
            @click="toggleFollow"
            style="width: 200px"
            class="q-mb-sm row col-10"
          />
        </template>
      </div>
    </q-card>
    <template
      v-if="info.pinned_forums.length > 0 || info.pinned_qnas.length > 0"
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
              >{{ info.username }}</span
            >
            <span>님의 글 더보기</span>
          </div>
          <template v-for="(post, index) in info.pinned_forums">
            <q-separator :key="post.title" />
            <div class="q-my-sm" :key="post.title">
              <span class="cursor-pointer" @click="goToForum(index)">{{
                post.title
              }}</span>
            </div>
          </template>
          <template v-for="(qna, index) in info.pinned_qnas">
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
import { followOtherUser } from '@/api/follow';
export default {
  props: {
    info: Object,
    followingStatus: Boolean,
    followerNum: Number,
  },
  data() {
    return {
      img_url: `${this.info.profile_img}`,
      follower_num: this.followerNum,
    };
  },
  methods: {
    async toggleFollow() {
      if (!this.$store.getters.isLogined) alert('로그인이 필요합니다!');
      else {
        try {
          this.$q.loading.show();
          const want_pk = this.info.user;
          await followOtherUser(want_pk);
          this.followingStatus = !this.followingStatus;
          if (this.followingStatus) {
            this.followerNum = this.followerNum + 1;
          } else {
            this.followerNum = this.followerNum - 1;
          }
        } catch (error) {
          alert(error);
        } finally {
          this.$q.loading.hide();
        }
      }
    },
    goToProfile() {
      this.$router.push(`/profile/${this.info.user}`);
    },
    goToForum(index) {
      this.$router.push(`/forum-detail/${this.info.pinned_forums[index].id}`);
      location.reload();
    },
    goToQna(index) {
      this.$router.push(`/qna-detail/${this.info.pinned_qnas[index].id}`);
    },
  },
};
</script>

<style scoped></style>
