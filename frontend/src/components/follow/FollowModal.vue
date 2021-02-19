<template>
  <q-dialog v-model="$store.state.follow.modal">
    <q-card style="min-width:650px; height:670px">
      <!-- x버튼 -->
      <div class="row justify-end" style="height:40px;">
        <q-icon
          :name="$i.ionClose"
          class="q-ma-lg"
          size="md"
          @click="offModal"
        ></q-icon>
      </div>

      <!-- 스크롤 영역 설정 -->
      <div class="q-ma-md">
        <q-scroll-area
          :thumb-style="thumbStyle"
          style="height: 585px; max-width: 650px;"
        >
          <!-- 탭 시작 -->
          <div class="q-pa-md">
            <div class="q-gutter-y-md" style="max-width: 600px">
              <center>
                <q-tabs
                  v-model="tab"
                  class="text-grey"
                  active-color="primary"
                  indicator-color="primary"
                  align="justify"
                  style="max-width: 450px;"
                >
                  <q-tab name="follow" label="팔로워" />
                  <q-tab name="following" label="팔로우" />
                </q-tabs>

                <q-separator style="width: 75%;" />
              </center>

              <q-tab-panels v-model="tab" animated>
                <q-tab-panel name="follow" style="padding-top: 0px;">
                  <FollowerList :userId="userId"></FollowerList>
                </q-tab-panel>

                <q-tab-panel name="following" style="padding-top: 0px;">
                  <FollowingList :userId="userId"></FollowingList>
                </q-tab-panel>
              </q-tab-panels>
            </div>
          </div>
        </q-scroll-area>
      </div>
    </q-card>
  </q-dialog>
</template>

<script>
import FollowerList from '@/components/follow/FollowerList';
import FollowingList from '@/components/follow/FollowingList';
export default {
  components: { FollowerList, FollowingList },
  data() {
    return {
      tab: this.$store.state.follow.tab,
      userId: this.$store.state.follow.id,
      thumbStyle: {
        right: '2px',
        borderRadius: '5px',
        backgroundColor: '#027be3',
        width: '5px',
        opacity: 0.75,
      },
    };
  },
  methods: {
    offModal() {
      this.$store.commit('offFollowModal');
    },
  },
  computed: {
    followTab() {
      return this.$store.state.follow.tab;
    },
  },
  watch: {
    followTab(newValue) {
      console.log(newValue);
      this.tab = newValue;
    },
  },
};
</script>

<style scoped>
/* .q-tab__label {
  font-size: 50px;
} */
.q-tab-only-label {
  font-size: tabs-big-font-size;
}
.q-tab >>> .q-tab__label {
  font-size: 12pt;
}
</style>
