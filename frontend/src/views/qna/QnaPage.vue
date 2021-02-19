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
            @click="goToDetail"
            class="cursor-pointer glossy font-weight-bold"
            size="12px"
          >
            <q-icon :name="$i.ionHelpCircleOutline" class="q-mr-sm"></q-icon>
            질문하기
          </q-btn>
        </span>
      </div>

      <!-- 게시판 보드 -->
      <!-- <qna-board :current="current"></qna-board> -->
      <bulletin-board :origin_board="board" sorting="time">
        <template slot="tab">
          <q-tab name="time" label="최신순" />
          <q-tab name="comment" label="댓글순" />
          <q-tab name="like" label="추천순" />
        </template>
        <template slot="entities" slot-scope="scopeProps">
          <qna-entity
            v-for="quest in scopeProps.entities.slice(
              (current - 1) * 10,
              current * 10,
            )"
            :key="quest.questId"
            :entity="quest"
          ></qna-entity>
        </template>
      </bulletin-board>
      <div class="row q-mt-md col-12 q-mb-xl">
        <!-- 답변 완료 표기 -->
        <div class="col-3 row q-py-xs">
          <div
            class="row col-4 q-pb-xs q-mr-md"
            v-for="(color, msg) in {
              '답변 완료': '#1976D2',
              '답변 대기': '#C8DAFE',
            }"
            :key="msg"
          >
            <div
              class="row col-12 shadow-1 overflow-hidden"
              style="border-radius:5px;"
            >
              <div class="col-2" :style="{ 'background-color': color }"></div>
              <div class="col-10 text-center">{{ msg }}</div>
            </div>
          </div>
        </div>
        <!-- 페이지네이션 -->
        <div class="col-6 row justify-center">
          <q-pagination
            v-model="current"
            color="grey"
            :max="max"
            :boundary-links="true"
          >
          </q-pagination>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import BulletinBoard from '@/components/common/BulletinBoard';
import QnaEntity from '@/components/qna/QnaEntity.vue';
import { getQnaList } from '@/api/board';
// import QnaBoard from '@/components/qna/QnaBoard';
export default {
  components: {
    // QnaBoard,
    BulletinBoard,
    QnaEntity,
  },
  data() {
    return {
      current: 1,
      board: [],
      max: 1,
    };
  },
  methods: {
    goToDetail() {
      if (this.$store.getters.isLogined) this.$router.push('/qna/create');
      else {
        this.$store.commit('setAccountModalType', 'login');
        this.$store.commit('onAccountModal');
      }
    },
    async loadBoard() {
      try {
        this.$q.loading.show();
        const { data } = await getQnaList();
        this.board = data;
        this.max = Math.ceil(data.length / 10);
        return data;
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },
  },
  async created() {
    // myTags로부터 selectedTags를 받아옴
    this.$store.commit('initSelectedTags');
    // QnA 게시판의 정보를 서버로부터 받아옴
    await this.loadBoard();
  },
};
</script>

<style scoped></style>
