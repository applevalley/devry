<template>
  <q-header bordered class="bg-white" height-hint="98">
    <q-toolbar>
      <div class="row items-center">
        <q-btn
          dense
          flat
          round
          icon="menu"
          @click="toggleLeft"
          color="primary"
        />
        <router-link :to="logolink">
          <span class="text-primary logo-font">DEVRY</span>
        </router-link>
      </div>
      <q-toolbar-title>
        <div></div>
      </q-toolbar-title>
      <q-tabs align="left">
        <q-btn color="grey" round flat v-if="!$store.getters.isLogined">
          <q-avatar :icon="$i.ionPersonCircleOutline"></q-avatar>
          <q-menu>
            <q-item @click="loginModal" clickable>
              <q-item-section avatar>
                <q-icon :name="$i.ionPersonCircleOutline"></q-icon>
              </q-item-section>
              <q-item-section>
                로그인
              </q-item-section>
            </q-item>
            <q-item @click="signupModal" clickable>
              <q-item-section avatar>
                <q-icon :name="$i.ionPersonAddOutline"></q-icon>
              </q-item-section>
              <q-item-section>
                회원가입
              </q-item-section>
            </q-item>
          </q-menu>
        </q-btn>
        <!-- 로그인 이후 보여지는 버튼 구현 -->
        <q-btn color="primary" round flat v-if="$store.getters.isLogined">
          <q-avatar :icon="$i.ionPersonCircleOutline"></q-avatar>
          <q-menu style="width:30%">
            <q-item @click="moveToProfilePage" clickable>
              <q-item-section avatar>
                <q-icon :name="$i.ionHappyOutline"></q-icon>
              </q-item-section>
              <q-item-section>
                프로필
              </q-item-section>
            </q-item>
            <q-item @click="moveToProfileSettingPage" clickable>
              <q-item-section avatar>
                <q-icon :name="$i.ionColorWandOutline"></q-icon>
              </q-item-section>
              <q-item-section>
                프로필 설정
              </q-item-section>
            </q-item>
            <q-item @click="moveToBookmarkPage" clickable>
              <q-item-section avatar>
                <q-icon :name="$i.ionBookmarkOutline"></q-icon>
              </q-item-section>
              <q-item-section>
                북마크
              </q-item-section>
            </q-item>

            <q-item @click="logout" clickable>
              <q-item-section avatar>
                <q-icon :name="$i.ionLogOutOutline"></q-icon>
              </q-item-section>
              <q-item-section>
                로그아웃
              </q-item-section>
            </q-item>
          </q-menu>
        </q-btn>
      </q-tabs>
    </q-toolbar>
  </q-header>
</template>

<script>
export default {
  data() {
    return {
      search: '',
    };
  },
  computed: {
    logolink() {
      return '/main';
    },
  },

  methods: {
    loginModal() {
      this.$store.commit('setAccountModalType', 'login');
      this.$store.commit('onAccountModal');
    },
    signupModal() {
      this.$store.commit('setAccountModalType', 'signup');
      this.$store.commit('onAccountModal');
    },
    fingPwdModal() {
      this.$store.commit('setAccountModalType', 'findPwd');
      this.$store.commit('onAccountModal');
    },
    followModal() {
      this.$store.commit('onFollowModal');
    },
    moveToProfilePage() {
      this.$router.push(`/profile/${this.$store.getters.getAccountId}`);
    },
    moveToProfileSettingPage() {
      this.$router.push(`/profile-setting/`);
    },
    moveToBookmarkPage() {
      this.$router.push(`/bookmark/`);
    },
    toggleLeft() {
      this.$store.commit('toggleLeft');
    },
    async logout() {
      try {
        await this.$store.dispatch('LOGOUT');
        location.reload();
      } catch (error) {
        alert(error);
      }
    },
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Bungee+Inline&display=swap');
a {
  color: white;
}
.logo-font {
  font-size: 20pt;
  font-family: 'Bungee Inline', cursive;
}
.q-input >>> .q-field__control {
  height: 40px;
}
.q-input >>> .q-field__append {
  height: 40px;
}
</style>
