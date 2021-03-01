<template>
  <div class="row justify-center overflow-hidden">
    <img
      :src="entity.thumnail"
      style="height:240px; width:60%;"
      class="cursor-pointer"
      @click="goToDetail"
    />
  </div>
</template>

<script>
export default {
  props: {
    entity: Object,
  },
  data() {
    return {
      num: '',
      img_url: this.entity.thumnail,
    };
  },
  methods: {
    goToDetail() {
      this.$router.push(`/event-detail/${this.entity.id}`);
    },
  },
};
</script>

<style></style>
