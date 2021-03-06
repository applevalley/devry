<template>
  <q-form @submit.prevent="submitForm">
    <div class="row">
      <div>
        <q-input
          v-model="email"
          clearable
          :clear-icon="$i.ionCloseOutline"
          stack-label
          label-slot
          placeholder="이메일 주소를 입력해주세요"
          type="email"
          label="e-mail"
          autocapitalize="none"
          :dense="dense"
          :error="!isEmailValid"
          :input-style="{ width: '400px' }"
        >
          <template v-slot:label>
            <span
              class="text-h6"
              :class="isEmailValid ? 'text-primary' : 'text-red'"
              >Email</span
            >
            <br />
            <br />
          </template>
          <template v-slot:error>
            <div class="text-red-8">잘못된 이메일 양식입니다</div>
          </template>
        </q-input>

        <br />
        <br />

        <q-input
          v-model="password"
          clearable
          :clear-icon="$i.ionCloseOutline"
          stack-label
          bottom-slots
          placeholder="6~12자 영문 대 소문자, 숫자를 사용하세요"
          type="password"
          label="password"
          :dense="dense"
          :error="!isValidPwd"
          :input-style="{ width: '400px' }"
        >
          <template v-slot:label>
            <span
              class="text-h6"
              :class="isValidPwd ? 'text-primary' : 'text-red'"
              >Password</span
            >
            <br />
            <br />
          </template>
          <template v-slot:error>
            <div class="text-red-8" v-if="password.length < 6">
              6자 이상의 비밀번호를 입력해주세요
            </div>
            <div class="text-red-8" v-else-if="password.length > 12">
              12자 이하의 비밀번호를 입력해주세요
            </div>
            <div class="text-red-8" v-else>
              특수문자를 제외하고 입력해주세요
            </div>
          </template>
        </q-input>
      </div>
    </div>
    <!-- 비밀번호 찾기 이동 -->
    <div
      class="text-right q-mb-md q-mt-md text-grey-6"
      style="width:400px;font-size:9pt"
    >
      <span @click="fingPwdModal" style="cursor:pointer"
        >비밀번호를 잊으셨나요?</span
      >
    </div>
    <br />
    <div class="row q-mb-md q-mt-md">
      <q-btn
        color="primary"
        label="LOGIN"
        style="width:400px; height:50px; border-radius:5px;"
        :disabled="!checkForm"
        type="submit"
      />
    </div>
  </q-form>
</template>

<script>
import { validateEmail, validatePwd } from '@/utils/validation';
// import axios from 'axios'

export default {
  data() {
    return {
      email: '',
      password: '',
      dense: false,
    };
  },
  methods: {
    fingPwdModal() {
      this.$store.commit('setAccountModalType', 'findPwd');
    },
    offModal() {
      this.$store.commit('offAccountModal');
    },
    async submitForm() {
      try {
        this.$q.loading.show();
        await this.$store.dispatch('LOGIN', {
          username: this.email,
          password: this.password,
        });
        this.$q.loading.hide();
        this.offModal();
        location.reload();
      } catch (error) {
        alert(error);
        this.$q.loading.hide();
        alert('이메일이나 비밀번호를 다시 확인해주세요.');
      }
    },
  },
  computed: {
    isEmailValid() {
      return this.email === '' || validateEmail(this.email);
    },
    isValidPwd() {
      return this.password === '' || validatePwd(this.password);
    },
    checkForm() {
      return validateEmail(this.email) && validatePwd(this.password);
    },
  },
};
</script>

<style scoped>
.title {
  margin-bottom: 30px;
  padding-top: 20%;
}

.close-button {
  padding-top: 30px;
}

.input {
  margin-bottom: 25px;
}

.password-info {
  margin-bottom: 40px;
}

.no-account {
  margin-top: 10px;
  margin-bottom: 20px;
}
</style>
