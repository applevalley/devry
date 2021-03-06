<template>
  <div>
    <div class="row cal-3 q-pt-lg q-ml-sm">
      <div v-if="info.assisted == true">
        <q-card
          flat
          bordered
          class="my-card row col-12 q-pa-sm"
          style="max-width: 250px; max-height: 280px;"
        >
          <q-card-section>
            <div class="row col-12">
              <div class="row col-2">
                <span style="cursor:pointer;" class="q-mt-xs">
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
                    style="font-size: 15px; cursor:pointer; color: #464646"
                    @click="goToProfile"
                  >
                    <b>{{ info.user.username }}</b>
                    <div class="text-caption">
                      팔로잉 {{ info.user.followee_num }} · 팔로워
                      {{ follower_num }}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </q-card-section>
          <div class="q-px-md q-pb-md">
            <div style="font-size: 13px;">
              {{ info.profile.bio }}
            </div>
          </div>
          <div
            class="row col-12 justify-center"
            v-if="info.user.id != $store.state.id"
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
      </div>
    </div>
  </div>
</template>

<script>
import { checkQnaSmallFollowStatus, checkQnaSmallFollowing } from '@/api/qna';

export default {
  props: {
    info: Object,
    getFollowingStatus: Boolean,
  },
  data() {
    return {
      is_following: Boolean,
      follower_num: this.info.user.follower_num,
      img_url: `${this.info.profile.profile_img}`,
    };
  },
  watch: {
    info(newValue) {
      (this.is_following = newValue.is_following),
        (this.follower_num = newValue.follower_num);
    },
  },
  methods: {
    goToProfile() {
      this.$router.push(`/profile/${this.info.user.id}`);
    },
    async checkFollow() {
      if (!this.$store.getters.isLogined) {
        alert('로그인을 해주세요');
        return;
      }
      try {
        await checkQnaSmallFollowing(this.info.id);
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
  },
  async created() {
    const ansId = this.info.id;
    try {
      const { data } = await checkQnaSmallFollowStatus(ansId);
      this.is_following = data.is_following;
    } catch (error) {
      alert(error);
    }
    this.$store.commit('offLeft');
  },
};
</script>

<style scoped></style>
