<template>
  <div class="row justify-center q-pt-lg ">
    <div class="row col-8 justify-center q-pt-lg q-px-md">
      <div class="row q-mb-lg col-12 justify-between">
        <div class="row col-3">
          <span class="text-h5  text-weight-bold">포럼 게시판</span>
        </div>
        <span class="q-ml-lg">
          <q-btn
            color="blue-7"
            @click="goToCreate"
            class="cursor-pointer glossy font-weight-bold"
            size="12px"
          >
            <q-icon
              :name="$i.ionDocumentTextOutline"
              class="q-mr-sm"
              size="xs"
            ></q-icon>
            글쓰기
          </q-btn>
        </span>
      </div>
      <!-- 포럼 게시판 목록 -->
      <forum-board></forum-board>
    </div>
  </div>
</template>

<script>
import ForumBoard from '@/components/forum/ForumBoard';

export default {
  components: {
    ForumBoard,
  },
  data() {
    return {
      new_board: [],
      feed_board: [],
      loaded: false,
    };
  },
  async created() {
    // myTags로부터 selectedTags를 받아옴
    this.$store.commit('initSelectedTags');
  },
  methods: {
    goToCreate() {
      // 포럼 게시물 생성 페이지로 이동
      this.$router.push('/forum/create');
    },
  },
};
</script>

<style scoped></style>
