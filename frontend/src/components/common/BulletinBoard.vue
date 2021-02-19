<template>
  <div class="row col-12">
    <div class="row justify-between  col-12">
      <!-- tab -->
      <q-tabs
        dens
        v-model="sort"
        style="color:#3B77AF"
        class="row justify-start"
      >
        <slot name="tab"></slot>
      </q-tabs>
      <!-- 검색창 및 태그 필터 선택 -->
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
    <!-- 게시물 목록 -->
    <div class="row q-mt-md col-12">
      <slot name="entities" :entities="board"></slot>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    origin_board: Array,
    feed_board: Array,
    sorting: String,
  },
  data() {
    return {
      sort: this.sorting,
      search: '',
      board: this.origin_board,
      union_board: this.feed_board
        ? [...this.feed_board, ...this.origin_board]
        : this.origin_board,
    };
  },
  watch: {
    origin_board(newValue) {
      // origin_board가 바뀔 때 다음과 같이 초기 목록을 뽑아온다.
      this.board = newValue.filter(post => {
        for (const tag of post.ref_tags) {
          if (this.selectedTags.indexOf(tag) >= 0) {
            return true;
          }
        }
        return false;
      });
      // 최신순 정렬
      this.board.reverse();
      this.prep_board = this.board;
    },
    sort(newValue) {
      // sort값이 바뀌면 board의 정렬 순서를 바꾼다.
      if (newValue === 'time') {
        this.board.sort((item1, item2) => {
          const date1 = new Date(item2.written_time);
          const date2 = new Date(item1.written_time);
          return date1 - date2;
        });
      } else if (newValue === 'comment') {
        this.board.sort(
          (item1, item2) => item2.comment_num - item1.comment_num,
        );
      } else if (newValue === 'like') {
        this.board.sort((item1, item2) => item2.like_num - item1.like_num);
      } else if (newValue === 'feed') {
        this.board = this.union_board;
      } else if (newValue === 'latest') {
        this.board = this.origin_board;
      }
    },
    selectedTags(newValue) {
      // store의 selectedTags가 바뀌면 새롭게 개시될 게시물들을 필터링한다.
      this.board = this.origin_board
        .filter(post => {
          for (const tag of post.ref_tags) {
            if (newValue.indexOf(tag) >= 0) return true;
          }
          return false;
        })
        .reverse();
      this.prep_board = this.board;
    },
  },
  computed: {
    // watch로 감시하기 위해서 store의 데이터를 selectedTags에 담음.
    selectedTags() {
      return this.$store.getters.getSelectedTags.length
        ? this.$store.getters.getSelectedTags
        : this.$store.state.all_tag_list;
    },
  },
  methods: {
    seachPost() {
      const searchReg = new RegExp(this.search, 'i');
      this.board = this.origin_board.filter(item => {
        if (searchReg.test(item.title)) return true;
        if (searchReg.test(item.user.username)) return true;
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
