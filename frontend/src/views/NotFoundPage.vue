<template>
  <q-page class="q-px-xl row flex items-center" style="height:100%;">
    <div class="col-3" style="padding-left:100px;">
      <div class="text-h6 text-primary text-weight-bold">404</div>
      <div class="error-title text-h2 text-weight-bold">
        Ooooooo<br />ooooops!
      </div>
      <div class="error-detail-message text-weight-regular">
        죄송합니다. 페이지를 찾을 수 없습니다.
      </div>
      <q-btn
        @click="goToMain"
        color="primary"
        label="Back to Home"
        style="width:200px; height:50px;"
        type="submit"
      />
    </div>
    <div class="col-9">
      <q-img
        :src="require('@/assets/panda.png')"
        alt="panda"
        style="height:1000px;"
      />
    </div>
  </q-page>
</template>

<script>
export default {
  methods: {
    goToMain() {
      this.$router.push({ path: '/main' });
    },
  },
};
</script>

<style scoped>
.error-title {
  margin: 20px 0px;
}

.error-detail-message {
  margin-bottom: 35px;
}
</style>
