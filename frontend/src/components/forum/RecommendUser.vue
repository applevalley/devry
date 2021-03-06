<template>
  <div
    class=" q-pa-sm row full-width q-mb-lg "
    style="border: 2px solid #ECEFF1;border-radius: 8px; "
  >
    <div
      class="col-3 q-px-sm "
      v-for="profile in filtered_profiles"
      :key="profile.user_id"
      v-tilt="{ speed: 300, perspective: 800 }"
    >
      <q-card>
        <div class="row full-width justify-center q-my-sm q-pt-sm">
          <q-avatar style="border: 1px solid #ECEFF1" size="10.0em">
            <q-img
              :src="
                profile.profile_img
                  ? profile.profile_img
                  : require('@/assets/basic_image.png')
              "
              style="height:2em"
            />
          </q-avatar>
        </div>
        <div
          class="row full-width justify-center q-mb-sm"
          style="font-size:1.3em"
        >
          @{{ profile.username }}
        </div>
        <div class="row justify-center ">
          <q-btn
            color="primary"
            label="프로필 보러 가기"
            class="col-8 q-mb-md"
            @click="goToProfile(profile.user_id)"
          />
        </div>
      </q-card>
    </div>
  </div>
</template>

<script>
import { getProfiles } from '@/api/profile';
export default {
  data() {
    return {
      profiles: [],
      unit: 10,
      cur: 1,
      max: 1,
    };
  },
  computed: {
    filtered_profiles() {
      return this.profiles
        .filter(profile => profile.user_id != this.$store.state.id)
        .slice(0, 8);
    },
  },
  created() {
    // 사용자들을 불러온다.
    this.loadProfiles();
  },
  methods: {
    async loadProfiles() {
      try {
        const { data } = await getProfiles();
        this.profiles = data;
        this.max = Math.ceil(data.length / this.unit);
      } catch (error) {
        alert(error);
      }
    },
    goToProfile(id) {
      this.$router.push(`/profile/${id}/`);
    },
  },
};
</script>

<style scoped>
.vifnslb-container >>> .vifnslb-element {
  width: auto;
}
.vifnslb-container >>> .vifnslb-bar {
  display: flex;
  justify-content: center;
}
</style>
