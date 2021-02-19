<template>
  <div class="row justify-center q-pt-lg ">
    <div class="row col-8 justify-center q-pl-lg">
      <div class="row q-mb-lg col-12 justify-between">
        <div class="row col-10">
          <div class="row col-3">
            <span class="text-h5  text-weight-bold">Forum 게시판</span>
          </div>
        </div>
        <span class="q-ml-lg">
          <q-btn
            color="blue-7"
            @click="goToDetail"
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
      <!-- <forum-board></forum-board> -->
      <bulletin-board
        :origin_board="new_board"
        :feed_board="feed_board"
        v-if="loaded"
        sorting="feed"
      >
        <template slot="tab">
          <q-tab name="feed" label="피드" />
          <q-tab name="latest" label="최신글" />
        </template>
        <template slot="entities" slot-scope="scopeProps">
          <div
            class="row col-4 q-pa-sm"
            v-for="(post, index) in scopeProps.entities"
            :key="index"
          >
            <forum-entity :entity="post"></forum-entity>
          </div>
        </template>
      </bulletin-board>
    </div>
  </div>
</template>

<script>
// import ForumBoard from '@/components/forum/ForumBoard';
import BulletinBoard from '@/components/common/BulletinBoard';
import ForumEntity from '@/components/forum/ForumEntity';
import { loadForumNew, loadForumFeed } from '@/api/board';

export default {
  components: {
    BulletinBoard,
    ForumEntity,
  },
  data() {
    return {
      new_board: [],
      feed_board: [],
      loaded: false,
    };
  },
  methods: {
    goToDetail() {
      if (this.$store.getters.isLogined) this.$router.push('/forum/create');
      else {
        this.$store.commit('setAccountModalType', 'login');
        this.$store.commit('onAccountModal');
      }
    },
    // 게시판의 '최신순' 정보를 서버로부터 받아옴
    async loadBoard() {
      try {
        this.$q.loading.show();
        let { data } = await loadForumNew();
        // this.origin_board = data;
        this.new_board = data;
        if (this.$store.getters.isLogined) {
          let res = await loadForumFeed();
          this.feed_board = res.data;
        }
        this.loaded = true;
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
    this.loadBoard();
  },
};
</script>

<style scoped></style>
