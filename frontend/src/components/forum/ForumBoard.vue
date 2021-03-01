<template>
  <div class="row col-12">
    <div class="row justify-between  col-12">
      <q-tabs
        dens
        v-model="sort"
        style="color:#3B77AF"
        class="row justify-start"
      >
        <q-tab name="feed" label="피드" v-if="$store.getters.isLogined" />
        <q-tab name="recomm" label="추천" v-else />
        <q-tab name="time" label="최신글" />
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
    <div class="row q-mt-md col-12" v-if="cur_board.length">
      <div
        class="row col-4 q-pa-sm"
        v-for="forum in cur_board"
        :key="forum.forumId"
      >
        <forum-entity :entity="forum"></forum-entity>
      </div>
    </div>
    <div
      class="row q-mt-md col-12  justify-center items-center"
      v-else-if="$store.getters.isLogined"
    >
      <div class="row justify-center full-width">
        <div class="text-grey-7 q-mb-md">
          아직 데이터가 없습니다. 다른 사용자들을 팔로우 해서 소식을 받아보세요.
        </div>
        <recommend-user></recommend-user>
      </div>
    </div>
  </div>
</template>

<script>
import ForumEntity from '@/components/forum/ForumEntity';
import { loadForumTime, loadForumFeed } from '@/api/board';
import RecommendUser from '@/components/forum/RecommendUser';
export default {
  components: {
    ForumEntity,
    RecommendUser,
  },
  data() {
    return {
      sort: this.$store.getters.isLogined ? 'feed' : 'recomm',
      search: '',
      time_board: [],
      feed_board: [],
      recomm_board: [],
      cur_board: [],
    };
  },
  async created() {
    // QnA 게시판의 정보를 서버로부터 받아옴
    this.loadBoard();
  },
  methods: {
    tagFilter(board) {
      // 게시물 목록으로부터 selectedTags에 매칭된 게시물만 가져온다.
      return board.filter(post => {
        for (const tag of post.ref_tags) {
          if (this.selectedTags.indexOf(tag) >= 0) return true;
        }
        return false;
      });
    },
    async loadBoard() {
      // 포럼 게시판 목록 정보를 불러온다.
      try {
        this.$q.loading.show();
        // 로그인에 상관없이 최신순으로 포럼 목록을 받아온다.
        let { data } = await loadForumTime();
        this.time_board = data;

        if (this.$store.getters.isLogined) {
          // 로그인이 되어 있으면 Feed를 가져온다.
          let { data } = await loadForumFeed();
          this.feed_board = data;
          this.cur_board = this.tagFilter(data);
        } else {
          // 로그인이 되어 있지 않으면 추천순서대로 정렬된 포럼 목록을 가져온다.
          this.recomm_board = [...this.time_board].sort(
            (item1, item2) => item2.like_num - item1.like_num,
          );
          this.cur_board = this.tagFilter(this.recomm_board);
        }
        this.loaded = true;
      } catch (error) {
        console.log(error);
      } finally {
        this.$q.loading.hide();
      }
    },

    seachPost() {
      // 검색창에 키워드를 적으면 title 또는 username에 일부 일치하는 게시물들을 필터링한다.
      const searchReg = new RegExp(this.search, 'i');
      this.board = this.origin_board.filter(item => {
        if (searchReg.test(item.title)) return true;
        if (searchReg.test(item.user.username)) return true;
        return false;
      });
    },
  },
  watch: {
    sort(newValue) {
      // sort를 감시해서 바뀌면 현재 게시판을 탭에 맞게 바꿈
      if (newValue === 'time') {
        this.cur_board = this.time_board;
      } else if (newValue === 'feed') {
        this.cur_board = this.feed_board;
      } else {
        this.cur_board = this.recomm_board;
      }

      // 태그 필터링
      this.cur_board = this.tagFilter(this.cur_board);
    },
    selectedTags() {
      // store의 selectedTags가 바뀌면 게시판 목록을 필터링함.
      this.cur_board = this.tagFilter(this.origin_board);
    },
  },

  computed: {
    // watch로 감시하기 위해서 store의 데이터를 selectedTags에 담음.
    selectedTags() {
      return this.$store.getters.getSelectedTags;
    },
    origin_board() {
      if (this.sort === 'time') return this.time_board;
      else if (this.sort === 'feed') return this.feed_board;
      else return this.recomm_board;
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
