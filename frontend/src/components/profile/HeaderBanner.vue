<template>
  <q-card class="col-7 q-mt-xl">
    <q-card-section>
      <div class="row items-center q-mt-sm">
        <div class="col-3 row justify-center">
          <div class="col-9">
            <q-img
              :src="
                info.profileImg
                  ? info.profileImg
                  : require('@/assets/basic_image.png')
              "
              alt="change-password"
              class="profile-picture "
              style="width:130px;height:130px"
            ></q-img>
          </div>
        </div>
        <div class="col-9 q-pr-xl">
          <div class="row q-mb-sm justify-between">
            <span class="text-h5 text-indigo-14 q-mt-sm">
              @{{ info.username }}</span
            >
            <template v-if="$store.state.id != info.userId">
              <template v-if="!is_following">
                <q-btn
                  no-caps
                  color="primary"
                  label="Follow"
                  @click="toggleFollow"
                  style="width: 100px"
                  class="q-mb-sm q-mt-sm row col-10"
                />
              </template>
              <template v-else>
                <q-btn
                  no-caps
                  outline
                  color="primary"
                  label="Following"
                  @click="toggleFollow"
                  style="width: 100px"
                  class="q-mb-sm q-mt-sm row col-10"
                />
              </template>
            </template>
            <template v-else>
              <div class="q-mb-lg q-mt-lg"></div>
            </template>
          </div>
          <!-- 사는 곳, 소속, 이메일 정보를 받는 행 -->
          <div class="row q-mb-sm full-width">
            <div class="q-mr-md row items-center">
              <q-icon
                :name="$i.ionLocationOutline"
                size="sm"
                class="q-mr-xs"
              ></q-icon>
              <span>{{ info.region ? info.region : '-' }}</span>
            </div>
            <div class="q-mr-md row items-center">
              <q-icon
                :name="$i.ionBriefcaseOutline"
                size="sm"
                class="q-mr-xs"
              ></q-icon>
              <span>{{ info.group ? info.group : '-' }}</span>
            </div>
            <div class="q-mr-md row items-center">
              <q-icon
                :name="$i.ionMailOutline"
                size="sm"
                class="q-mr-xs"
              ></q-icon>
              <span>{{ info.email }}</span>
            </div>
          </div>
          <!-- 등록된 웹싸이트 링크에 맞춰 로고를 보여주는 행-->
          <div class="row q-mb-md full-width">
            <q-icon
              v-for="link in info.links"
              :key="link.sns_name"
              :name="$i[`ionLogo${link.sns_name}`]"
              size="sm"
              color="grey-8"
              class="q-mr-xs cursor-pointer"
              @click="linkRedirect(link.sns_url)"
            ></q-icon>
          </div>
          <!-- 가입날짜와 팔로워/팔로우 수를 표시해주는 행 -->
          <div class="row q-mb-sm justify-between full-width">
            <div class="row items-center">
              <q-icon
                :name="$i.ionCalendarClearOutline"
                color="grey-8"
                size="xs"
                class="q-mr-xs"
              ></q-icon>
              <span>joined on {{ info.joined | moment('YYYY/MM/DD') }}</span>
            </div>
            <div>
              <span class="q-mr-md cursor-pointer" @click="onFollow('follow')"
                >팔로워: <b>{{ followerNum }}</b></span
              >
              <span class="cursor-pointer" @click="onFollow('following')"
                >팔로잉: <b>{{ info.followeeNum }}</b></span
              >
            </div>
          </div>
        </div>
      </div>
      <div class="row q-px-xl q-my-sm full-width">
        <div class="full-width" v-if="info.bio">
          <q-icon
            :name="$i.ionChatboxEllipsesOutline"
            style="color:#727272"
            size="17px"
          ></q-icon>
          {{ info.bio }}
        </div>
      </div>
    </q-card-section>
  </q-card>
</template>

<script>
import { followOtherUser } from '@/api/follow';

export default {
  props: {
    info: Object,
  },
  data() {
    return {
      followerData: [],
      is_following: this.info.is_following,
      followerNum: this.info.followerNum,
    };
  },
  watch: {
    info(newValue) {
      (this.is_following = newValue.is_following),
        (this.followerNum = newValue.followerNum);
    },
  },
  methods: {
    linkRedirect(url) {
      window.open(url);
    },
    onFollow(tab) {
      this.$store.commit('onFollowModal', [tab, this.$route.params.id]);
    },
    async toggleFollow() {
      try {
        this.$q.loading.show();
        const want_pk = this.info.userId;
        await followOtherUser(want_pk);
        this.is_following = !this.is_following;
        if (this.is_following) {
          this.followerNum = this.followerNum + 1;
        } else {
          this.followerNum = this.followerNum - 1;
        }
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
.profile-picture {
  width: 100%;
  border: 5px solid #d1d4f1;
  border-radius: 100px;
}
</style>
