<template>
  <div class="row col-12">
    <div class="row justify-between  col-12">
      <q-tabs
        dens
        v-model="sort"
        style="color:#3B77AF"
        class="row justify-start"
      >
        <q-tab name="time" label="최신순" />
        <q-tab name="comment" label="댓글순" />
        <q-tab name="like" label="추천순" />
      </q-tabs>
      <div class="row justify-end q-gutter-lg">
        <q-input
          v-model="search"
          type="search"
          class="q-mb-sm"
          outlined
          @keypress.enter="seachPost"
        >
          <template v-slot:append>
            <q-icon :name="$i.ionSearchOutline" />
          </template>
        </q-input>
        <q-btn
          class="tag-filter"
          outline
          color="primary"
          @click="$store.commit('toggleTagFilter')"
          >태그 선택</q-btn
        >
      </div>
    </div>
    <div class="row q-mt-md col-12">
      <qna-entity
        v-for="quest in board.slice((current - 1) * 10, current * 10)"
        :key="quest.questId"
        :entity="quest"
      ></qna-entity>
    </div>

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
            class="row col-12 shadow-1 overflow-hidden "
            style="border-radius:5px;"
          >
            <div class="col-2" :style="{ 'background-color': color }"></div>
            <div
              class="col-10 row justify-center items-center"
              style="font-size:0.8rem"
            >
              <div class="text-center">{{ msg }}</div>
            </div>
          </div>
        </div>
      </div>
      <!-- 페이지네이션 -->
      <div class="col-9 row justify-end">
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
</template>

<script>
import QnaEntity from '@/components/qna/QnaEntity.vue';
import { getQnaList } from '@/api/board';
export default {
  components: {
    QnaEntity,
  },
  data() {
    return {
      origin_board: [],
      sort: 'time',
      search: '',
      board: [],
      max: 1,
      current: 1,
      loaded: false,
    };
  },

  computed: {
    // watch로 감시하기 위해서 store의 데이터를 selectedTags에 담음.
    selectedTags() {
      return this.$store.getters.getSelectedTags;
    },
  },

  created() {
    // QnA 게시판의 정보를 서버로부터 받아옴
    this.loadBoard();
  },

  methods: {
    async loadBoard() {
      // 게시판의 정보를 서버로부터 받아옴
      try {
        this.$q.loading.show();
        const { data } = await getQnaList();
        this.origin_board = this.timeSort(data);
        this.board = this.origin_board;
        this.max = Math.ceil(data.length / 10);
        this.loaded = true;
      } catch (error) {
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },
    seachPost() {
      // 게시판에서 제목, 유저이름으로 검색 가능
      const searchReg = new RegExp(this.search, 'i');
      this.board = this.origin_board.filter(item => {
        if (searchReg.test(item.title)) return true;
        if (searchReg.test(item.user.username)) return true;
        return false;
      });
    },
    timeSort(board) {
      // 최신순으로 정렬
      return board.sort((item1, item2) => {
        const date1 = new Date(item2.written_time);
        const date2 = new Date(item1.written_time);
        return date1 - date2;
      });
    },
    commentSort(board) {
      // 댓글 갯수 많은 순으로 정렬
      return board.sort(
        (item1, item2) => item2.comment_num - item1.comment_num,
      );
    },
    likeSort(board) {
      // 좋아요 갯수 많은 순으로 정렬
      return board.sort((item1, item2) => item2.like_num - item1.like_num);
    },
  },

  watch: {
    sort(newValue) {
      // sort를 감시해서 바뀌면 새롭게 정렬함
      if (newValue === 'time') {
        this.timeSort(this.board);
      } else if (newValue === 'comment') {
        this.commentSort(this.board);
      } else {
        this.likeSort(this.board);
      }
    },
    selectedTags(newValue) {
      // store의 selectedTags가 바뀌면 해당 태그를 가지고 있는 게시물들만 필터링함
      this.board = this.origin_board.filter(post => {
        for (const tag of post.ref_tags) {
          if (newValue.indexOf(tag) >= 0) return true;
        }
        return false;
      });
    },
  },
};
</script>

<style scoped>
.q-input >>> .q-field__control {
  height: 40px;
}
.q-input >>> .q-field__append {
  height: 40px;
}
.tag-filter {
  height: 40px;
}
</style>
