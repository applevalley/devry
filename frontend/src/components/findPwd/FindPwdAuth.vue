<template>
  <div class="row items-center" style="width:400px; height:60%">
    <q-form @submit.prevent="submitForm" class="q-my-none q-mx-auto">
      <div class="text-h5 text-weight-bold">Forgot password</div>
      <br />

      <div class="row" style="width:400px">
        <q-input
          class="input"
          v-model="email"
          type="email"
          label="email"
          label-slot
          placeholder="이메일을 입력해주세요"
          style="width:350px;"
          stack-label
          :dense="dense"
          :error="!isValidEmail"
        >
          <template v-slot:label>
            <span
              class="text-h6"
              :class="isValidEmail ? 'text-primary' : 'text-red'"
              >이메일</span
            >
            <br />
            <br />
          </template>
          <template v-slot:error>
            <div class="text-red-8">
              잘못된 이메일 양식입니다.
            </div>
          </template>
        </q-input>
        <q-input
          v-model="nickname"
          clearable
          placeholder="별명을 입력해주세요"
          :clear-icon="$i.ionCloseOutline"
          style="width:350px;"
          stack-label
          label-slot
          bottom-slots
        >
          <template v-slot:label>
            <span class="text-h6 text-primary">별명</span>
            <br />
            <br />
          </template>
        </q-input>
      </div>
      <br />
      <q-btn
        @click="moveToChangePwd"
        :disabled="!checkForm"
        color="primary"
        label="SEND"
        style="width:350px; height:50px;"
        type="submit"
      />
    </q-form>
  </div>
</template>

<script>
import { validateEmail } from '@/utils/validation';
export default {
  data() {
    return {
      email: '',
      nickname: '',
      dense: false,
      modalState: 'auth',
    };
  },
  computed: {
    isValidEmail() {
      return this.email === '' || validateEmail(this.email);
    },
    checkForm() {
      return validateEmail(this.email);
    },
  },
  methods: {
    async submitForm() {
      try {
        this.$q.loading.show();
        // 89-93번째 코드 주석을 해제하면 에러발생
        // await checkUser({
        //   email: this.email,
        //   username: this.nickname
        // });
        // alert('계정인증에 성공했습니다. 비밀번호 변경을 진행해주세요');
        this.$emit('authPwdSuccess');
      } catch (error) {
        // alert('에러가 발생했습니다. 계정을 확인해주세요!');
        this.$emit('authPwdFail');
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },
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
