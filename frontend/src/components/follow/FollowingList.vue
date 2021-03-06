<template>
  <div>
    <div v-for="(data, index) in followeeData" :key="index" class="q-pa-xs">
      <div class="q-pa-md row col-align" style="height:80px;">
        <div class="col-8 row" style="height:100%">
          <q-list style="min-width:300px; margin-left: 30px;">
            <q-item>
              <!-- <q-item-section avatar>
                <q-avatar @click="goToProfile(index)" class="cursor-pointer"
                  ><img :src="data.profile_img" />
                </q-avatar>
              </q-item-section> -->
              <q-item-section>
                <span
                  class="change-tag-color cursor-pointer"
                  @click="goToProfile(index)"
                >
                  <b style="font-size: 15px;">{{
                    data.following_user.username
                  }}</b>
                </span>
                <span
                  >팔로잉 {{ data.following_user.followee_num }} · 팔로워
                  {{ data.following_user.follower_num }}</span
                >
              </q-item-section>
            </q-item>
          </q-list>
        </div>
        <div
          v-if="data.following_user.id != $store.state.id"
          class="col-4 row justify-center items-center"
          style="height:100%"
        >
          <div v-if="data.is_following">
            <q-btn
              no-caps
              outline
              color="primary"
              label="Following"
              style="width:90px;"
              @click="toggleFollow(index)"
            />
          </div>
          <div v-else>
            <q-btn
              no-caps
              color="primary"
              id="follow-btn"
              label="Follow"
              style="width:90px;"
              @click="toggleFollow(index)"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getOtherFolloweeList, followOtherUser } from '@/api/follow';

export default {
  props: {
    userId: String,
  },
  data() {
    return {
      followeeData: [],
    };
  },
  methods: {
    goToProfile(index) {
      this.$router.push(
        `/profile/${this.followeeData[index].following_user.id}`,
      );
      location.reload();
    },
    async toggleFollow(index) {
      try {
        this.$q.loading.show();
        const want_pk = this.followeeData[index].following_user.id;
        await followOtherUser(want_pk);
        this.getFollowee();
      } catch (error) {
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },
    async getFollowee() {
      try {
        this.$q.loading.show();
        const { data } = await getOtherFolloweeList(this.userId);
        console.log(data);
        this.followeeData = data;
      } catch (error) {
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },
  },
  computed: {
    followId() {
      return this.$store.state.follow.id;
    },
  },
  watch: {
    async followId(newValue) {
      const { data } = await getOtherFolloweeList(newValue);
      this.followeeData = data;
    },
  },
  async created() {
    try {
      this.getFollowee();
    } catch (error) {
      alert(error);
    }
  },
};
</script>

<style scoped>
.col-align {
  display: flex;
  align-items: center;
}
.change-tag-color {
  text-decoration: none;
  color: #000000;
}
</style>
