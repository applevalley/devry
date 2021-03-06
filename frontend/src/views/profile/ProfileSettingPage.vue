<template>
  <div class="row q-pa-md justify-center q-mt-md fu">
    <div class="row col-6">
      <!-- 타이틀 -->
      <div class="q-mb-md">
        <span class="text-h4 text-weight-bolder">Settings for </span>
        <span class="text-h4 text-weight-bolder text-primary">{{
          $store.state.nickname
        }}</span>
        <p class="text-subtitle2 q-mt-sm">
          회원정보 수정 페이지입니다 :)
        </p>
      </div>

      <!-- 입력 폼 -->
      <profile-setting-form
        v-if="loaded"
        :info="profile_info"
      ></profile-setting-form>
    </div>
  </div>
</template>

<script>
import ProfileSettingForm from '@/components/profile/setting/ProfileSettingForm';
import { loadProfile } from '@/api/profile';
export default {
  components: { ProfileSettingForm },
  data() {
    return {
      profile_info: {
        bio: '',
        email: '',
        group: '',
        link: [
          { sns_name: '', sns_url: '' },
          { sns_name: '', sns_url: '' },
          { sns_name: '', sns_url: '' },
        ],
        my_tags: [],
        profile_img: null,
        project: [],
        region: '',
        tech_stack: [],
        username: '',
      },
      loaded: false,
    };
  },
  async created() {
    try {
      this.$q.loading.show();
      const { data } = await loadProfile(this.$store.state.id);
      const username = this.$store.state.nickname;

      this.profile_info.bio = data.bio;
      this.profile_info.email = data.email;
      this.profile_info.group = data.group;
      for (const index in data.link) {
        this.profile_info.link[index]['sns_name'] =
          data.link[index]['sns_name'];
        this.profile_info.link[index]['sns_url'] = data.link[index]['sns_url'];
      }
      // my_tags와 tech_stack은 넘어오는 값이 하나일 경우에 배열이 아닌 string으로 오는 문제가 있다.
      this.profile_info.my_tags =
        typeof data.my_tags == 'string' ? [data.my_tags] : data.my_tags;
      this.profile_info.tech_stack =
        typeof data.tech_stack == 'string'
          ? [data.tech_stack]
          : data.tech_stack;
      this.profile_info.profile_img = data.profile_img;
      this.profile_info.project = data.project;
      this.profile_info.region = data.region;
      this.profile_info.username = username;
      this.loaded = true;
    } catch (error) {
      alert(error);
    } finally {
      this.$q.loading.hide();
    }
  },
};
</script>

<style scoped></style>
