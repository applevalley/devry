<template>
  <div class="row justify-center q-pt-lg ">
    <div class="row col-8 justify-center q-pl-lg">
      <div class="row q-mb-lg col-12 justify-between">
        <div class="row col-10">
          <div class="row col-2">
            <span class="text-h5  text-weight-bold">QnA 게시판</span>
          </div>
        </div>
        <span class="q-ml-lg">
          <q-btn
            color="blue-7"
            @click="goToCreate"
            class="cursor-pointer glossy font-weight-bold"
            size="12px"
          >
            <q-icon :name="$i.ionHelpCircleOutline" class="q-mr-sm"></q-icon>
            질문하기
          </q-btn>
        </span>
      </div>

      <!-- 게시판 보드 -->
      <qna-board></qna-board>
    </div>
  </div>
</template>

<script>
import QnaBoard from '@/components/qna/QnaBoard';
export default {
  components: {
    QnaBoard,
  },
  async created() {
    // myTags로부터 selectedTags를 받아옴
    this.$store.commit('initSelectedTags');
  },
  methods: {
    goToCreate() {
      if (this.$store.getters.isLogined) this.$router.push('/qna/create');
      else {
        this.$store.commit('setAccountModalType', 'login');
        this.$store.commit('onAccountModal');
      }
    },
  },
};
</script>

<style scoped></style>
