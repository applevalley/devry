<template>
  <q-drawer
    show-if-above
    v-model="$store.state.leftDrawal"
    side="left"
    behavior="desktop"
    bordered
    overlay
    :width="240"
    persistent
  >
    <q-tabs
      v-model="tab"
      vertical
      class="text-black q-pt-xl"
      active-bg-color="blue-1"
      indicator-color="blue-4"
      inline-label
      align="left"
    >
      <q-route-tab
        name="qna"
        :icon="$i.ionSearchOutline"
        label="QnA"
        to="/qna"
      />
      <q-route-tab
        name="forum"
        :icon="$i.ionCafeOutline"
        label="포럼"
        to="/forum"
      />
      <q-route-tab name="event" icon="event" label="이벤트" to="/event" />
    </q-tabs>
    <div v-if="$store.getters.isLogined">
      <div class="row my-tags q-pt-lg">
        <div class="row col-12 q-mb-sm" style="font-size: 14pt;">#My tags</div>
        <div class="row q-mr-sm">
          <span
            v-for="tag in $store.getters.getMyTags"
            :key="tag"
            class="q-mb-sm q-mr-xs q-pa-sm my-tags-element"
            >#{{ tag }}</span
          >
        </div>
      </div>
    </div>
  </q-drawer>
</template>

<script>
export default {
  data() {
    return {
      tab: 'qna',
      tags: ['Javascript', 'vue', 'react', 'python'],
    };
  },
};
</script>

<style scoped>
.q-tab {
  justify-content: start;
}
.q-tab >>> .q-tab__content {
  padding-left: 40px;
}
.q-tab >>> .q-tab__label {
  font-weight: bold;
}
.q-tabs--vertical {
  height: auto;
}
.my-tags {
  padding-left: 48px;
}
.my-tags-element {
  font-size: 10pt;
  border-radius: 5pt;
  background-color: #dddddd;
}
</style>
