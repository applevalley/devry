<template>
  <div style="height:50%">
    <div class="row justify-start items-end" style="height:60%">
      <p class="text-h4 text-weight-bolder">
        비밀번호 변경 실패😥
      </p>
    </div>
    <br />
    <br />
    <div class="row justify-start" style="height:55%">
      <q-btn
        color="blue-12"
        class="text-center"
        style="width:330px;height:50px;border-radius:5px;font-size:16pt"
        type="submit"
        @click="backToReset"
        >뒤로가기</q-btn
      >
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    backToReset() {
      this.$emit('resetPwd');
    },
  },
};
</script>

<style scoped></style>
