<template>
  <div class="row items-center" style="width:400px; height:60%">
    <q-form @submit.prevent="submitForm" class="q-my-none q-mx-auto ">
      <div class="text-h5 text-weight-bold ">
        Create new password
      </div>
      <br />
      <q-input
        class="input"
        v-model="newPwd"
        type="password"
        label="password"
        label-slot
        placeholder="6-12자 이내의 새로운 비밀번호를 입력해주세요"
        style="width:350px;"
        stack-label
        :dense="dense"
        :error="!isValidPwd"
      >
        <template v-slot:label>
          <span
            class="text-h6"
            :class="isValidPwd ? 'text-primary' : 'text-red'"
            >새 비밀번호</span
          >
          <br />
          <br />
        </template>
        <template v-slot:error>
          <div class="text-red-8" v-if="newPwd.length < 6">
            6자 이상의 비밀번호를 입력해주세요
          </div>
          <div class="text-red-8" v-else-if="newPwd.length > 12">
            12자 이하의 비밀번호를 입력해주세요
          </div>
          <div class="text-red-8" v-else-if="newPwd === password">
            이전의 비밀번호와 다른 비밀번호를 입력해주세요
          </div>
          <div class="text-red-8" v-else>
            특수문자를 제외하고 입력해주세요
          </div>
        </template>
      </q-input>
      <q-input
        class="input"
        v-model="confirmNewPwd"
        type="password"
        label="confirm password"
        placeholder="비밀번호를 다시 한 번 입력해주세요"
        style="width:350px;"
        stack-label
        :dense="dense"
        :error="!isValidPwdConfirm"
        error-message="비밀번호를 다시 확인해주세요"
      >
        <template v-slot:label>
          <span
            class="text-h6"
            :class="isValidPwdConfirm ? 'text-primary' : 'text-red'"
            >비밀번호 확인</span
          >
          <br />
          <br />
        </template>
      </q-input>
      <q-btn
        :disabled="!checkForm"
        color="primary"
        label="SAVE"
        style="width:350px; height:50px;"
        type="submit"
      />
    </q-form>
  </div>
</template>

<script>
import { validatePwd } from '@/utils/validation';
export default {
  data() {
    return {
      password: '12345678',
      jwt: this.$route.query.jwt,
      newPwd: '',
      confirmNewPwd: '',
      dense: false,
      login: false,
    };
  },
  computed: {
    isValidPwd() {
      return (
        (this.newPwd === '' || validatePwd(this.newPwd)) &&
        this.newPwd !== this.password
      );
    },
    isValidPwdConfirm() {
      return this.confirmNewPwd === '' || this.newPwd === this.confirmNewPwd;
    },
    checkForm() {
      return (
        validatePwd(this.newPwd) &&
        this.newPwd === this.confirmNewPwd &&
        this.newPwd !== this.password
      );
    },
  },
  methods: {
    signupModal() {
      this.$store.commit('setAccountModalType', 'signup');
      this.$store.commit('onAccountModal');
    },
    fingPwdModal() {
      this.$store.commit('setAccountModalType', 'findPwd');
      this.$store.commit('onAccountModal');
    },
    setToken: function() {
      const token = localStorage.getItem('jwt');
      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        },
      };
      return config;
    },
    async submitForm() {
      // const config = this.setToken();
      try {
        this.$q.loading.show();
        // 131 - 133번째 주석을 해제하면 에러발생
        // await changePwdUser({
        //   password: this.newPwd,
        // });
        this.password = this.newPwd;
        // alert('비밀번호 변경에 성공하였습니다!');
        this.$emit('resetPwdSuccess');
      } catch (error) {
        // alert('에러가 발생했습니다. 다시 시도해주세요!')
        this.$emit('resetPwdFail');
      } finally {
        this.$q.loading.hide();
      }
    },
  },
  created() {
    // 로그인 되어있는 상태인지 확인
    const token = localStorage.getItem('jwt');
    if (token) {
      this.login = true;
    }
  },
};
</script>

<style scoped>
.title {
  margin-bottom: 30px;
  padding-top: 30%;
}

.close-button {
  padding-top: 30px;
}

.input {
  margin-bottom: 25px;
}

.save-button {
  margin-top: 50px;
}
</style>
