<template>
  <q-form @submit.prevent="submitForm">
    <div class="row">
      <!-- 회원가입 입력 form -->
      <div>
        <div class="row" style="width:400px">
          <div class="col-8">
            <q-input
              v-model="email"
              clearable
              :clear-icon="$i.ionCloseOutline"
              stack-label
              label-slot
              :input-style="{ width: '180px' }"
              bottom-slots
              placeholder="이메일 주소를 입력해주세요"
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
                <div class="text-red-8">잘못된 이메일 양식입니다</div>
              </template>
            </q-input>
          </div>
          <div class="col-1"></div>
          <div class="col-3">
            <q-input
              v-model="nickname"
              clearable
              :clear-icon="$i.ionCloseOutline"
              stack-label
              label-slot
              :input-style="{ width: '110px' }"
              bottom-slots
            >
              <template v-slot:label>
                <span class="text-h6 text-primary">별명</span>
                <br />
                <br />
              </template>
            </q-input>
          </div>
        </div>
        <br />
        <br />
        <q-input
          v-model="password1"
          clearable
          :clear-icon="$i.ionCloseOutline"
          stack-label
          label-slot
          placeholder="6~12자 영문 대 소문자, 숫자를 사용하세요"
          type="password"
          :error="!isValidPwd"
        >
          <template v-slot:label>
            <span
              class="text-h6"
              :class="isValidPwd ? 'text-primary' : 'text-red'"
              >비밀번호</span
            >
            <br />
            <br />
          </template>
          <template v-slot:error>
            <div class="text-red-8" v-if="password1.length < 6">
              6자 이상의 비밀번호를 입력해주세요
            </div>
            <div class="text-red-8" v-else-if="password1.length > 12">
              12자 이하의 비밀번호를 입력해주세요
            </div>
            <div class="text-red-8" v-else>
              특수문자를 제외하고 입력해주세요
            </div>
          </template>
        </q-input>
        <br />
        <br />
        <q-input
          v-model="password2"
          clearable
          :clear-icon="$i.ionCloseOutline"
          stack-label
          label-slot
          placeholder="다시 한번 비밀번호를 입력해주세요"
          type="password"
          :error="!isValidPwdConfirm"
          error-message="다시 비밀번호를 확인해주세요"
        >
          <template v-slot:label>
            <span
              class="text-h6"
              :class="isValidPwdConfirm ? 'text-primary' : 'text-red'"
            >
              비밀번호 확인
            </span>
            <br />
            <br />
          </template>
        </q-input>
      </div>
    </div>
    <!-- Signup 버튼  -->
    <div class="row q-mb-md q-mt-md">
      <q-btn
        color="blue-12"
        class="text-center"
        style="width:400px;height:50px;border-radius:5px;"
        type="submit"
        :disabled="!checkForm"
        label="SIGN UP"
      ></q-btn>
    </div>
  </q-form>
</template>

<script>
import { registerUser } from '@/api/auth';
import { validateEmail, validatePwd } from '@/utils/validation';
export default {
  data() {
    return {
      email: '',
      nickname: '',
      password1: '',
      password2: '',
    };
  },
  computed: {
    isValidEmail() {
      return this.email === '' || validateEmail(this.email);
    },
    isValidPwd() {
      return this.password1 === '' || validatePwd(this.password1);
    },
    isValidPwdConfirm() {
      return this.password2 === '' || this.password1 === this.password2;
    },
    checkForm() {
      return (
        validateEmail(this.email) &&
        validatePwd(this.password1) &&
        this.password1 === this.password2 &&
        this.nickname !== ''
      );
    },
  },
  methods: {
    async submitForm() {
      try {
        this.$q.loading.show();
        await registerUser({
          username: this.nickname,
          email: this.email,
          password: this.password1,
        });
        this.$emit('signupSuccess');
      } catch (error) {
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },
    offModal() {
      this.$store.commit('offAccountModal');
    },
  },
};
</script>

<style scoped></style>
