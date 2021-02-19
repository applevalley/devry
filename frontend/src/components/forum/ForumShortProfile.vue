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
                  글 {{ info.post_num }} · 팔로워 {{ follower_num }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </q-card-section>
      <div class="q-px-md q-pb-md" v-if="profile">
        <div style="font-size: 13px;">
          {{ info.bio }}
        </div>
      </div>
      <div
        class="row col-12 justify-center"
        v-if="info.user != $store.state.id"
      >
        <template v-if="is_following == false">
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
    <q-card
      flat
      bordered
      class="my-card row col-12 q-px-sm q-pt-md"
      style="max-width: 250px; max-height: 280px;"
      v-if="profile"
    >
      <div class="q-px-md q-pb-sm">
        <div style="font-size: 13px;">
          <div class="q-my-sm">
            <span
              class="text-weight-bold cursor-pointer"
              style="color: #598FFC"
              >{{ info.username }}</span
            >
            <span>님의 글 더보기</span>
          </div>
          <template v-for="post in profile.pinned">
            <q-separator :key="post.title" />
            <div class="q-my-sm" :key="post.title">
              {{ post.title }}
            </div>
          </template>

          <q-separator />
        </div>
      </div>
    </q-card>
  </div>
</template>

<script>
import { followOtherUser } from '@/api/follow';
//
export default {
  props: {
    info: Object,
  },
  data() {
    return {
      img_url: `${this.info.profile_img}`,
      is_following: this.info.is_following,
      follower_num: this.info.follower_num,
    };
  },
  watch: {
    info(newValue) {
      (this.is_following = newValue.is_following),
        (this.follower_num = newValue.follower_num);
    },
  },
  methods: {
    async toggleFollow() {
      if (!this.$store.getters.isLogined) alert('로그인이 필요합니다!');
      else {
        try {
          this.$q.loading.show();
          const want_pk = this.info.user;
          await followOtherUser(want_pk);
          this.is_following = !this.is_following;
          if (this.is_following) {
            this.follower_num = this.follower_num + 1;
          } else {
            this.follower_num = this.follower_num - 1;
          }
        } catch (error) {
          console.log(error);
        } finally {
          this.$q.loading.hide();
        }
      }
    },
    goToProfile() {
      this.$router.push(`/profile/${this.info.user}`);
    },
    goToDetail() {
      this.$router.push({ name: 'ForumDetail' });
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
