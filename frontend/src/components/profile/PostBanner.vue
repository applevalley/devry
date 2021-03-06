<template>
  <div class="col-7 q-my-lg ">
    <!-- Pinned 항목 -->
    <div class="row justify-between q-mb-sm">
      <div class="q-mb-sm row items-center">
        <q-icon
          :name="$i.ionAttachOutline"
          style="color: #B54333"
          size="md"
          class="q-mr-xs"
        ></q-icon>
        <span class="text-h5 text-weight-bold">Pinned</span>
      </div>
      <div>
        <q-tabs v-model="pinned" style="color:#259EC5">
          <q-tab name="forum" label="포럼" />
          <q-tab name="qna" label="질문" />
        </q-tabs>
      </div>
    </div>
    <!-- Pinned 게시물을 보여주는 카드 슬라이더 -->
    <q-card class="q-mb-lg pinned-background">
      <q-card-section>
        <q-carousel
          v-model="slide"
          transition-prev="slide-right"
          transition-next="slide-left"
          swipeable
          animated
          infinite
          control-color="black"
          padding
          arrows
          :autoplay="autoplay"
          @mouseenter="autoplay = false"
          @mouseleave="autoplay = true"
          height="180px"
          v-if="pinned_post.length"
        >
          <q-carousel-slide
            v-for="(post, index) in pinned_post"
            :name="index + 1"
            :key="index"
            style="border-radius: 10px;"
            class="row items-center"
          >
            <forum-post-card
              :detail="post"
              :username="info.username"
              v-if="pinned == 'forum'"
            ></forum-post-card>
            <qna-post-card
              :detail="post"
              :username="info.username"
              v-else
            ></qna-post-card>
          </q-carousel-slide>
        </q-carousel>
        <div v-else class="full-width text-center text-grey-6">없음</div>
      </q-card-section>
    </q-card>
    <!-- History 항목 -->
    <div class="row justify-between q-mb-sm">
      <div class="q-mb-sm row items-center">
        <q-icon
          :name="$i.ionLayersOutline"
          style="color: #259EC5"
          size="md"
          class="q-mr-xs"
        ></q-icon>
        <span class="text-h5 text-weight-bold">History</span>
      </div>
      <div>
        <q-tabs v-model="post" style="color:#259EC5">
          <q-tab name="forum" label="포럼" />
          <q-tab name="qna" label="질문" />
          <q-tab name="comments" label="댓글" />
        </q-tabs>
      </div>
    </div>
    <!-- Histroy 게시물을 보여주는 카드 목록 -->
    <q-card class="history-background">
      <q-card-section v-if="post == 'qna'">
        <qna-post-card
          v-for="qna in info.qnas"
          :detail="qna"
          :key="qna.id"
          :username="info.username"
        ></qna-post-card>
      </q-card-section>
      <q-card-section v-else-if="post == 'forum'">
        <forum-post-card
          v-for="forum in info.forums"
          :username="info.username"
          :detail="forum"
          :key="forum.id"
        ></forum-post-card>
      </q-card-section>
      <q-card-section v-else-if="post == 'comments'">
        <comment-card
          v-for="comment in info.comments"
          :username="info.username"
          :detail="comment"
          :key="comment.id"
        ></comment-card>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
import QnaPostCard from '@/components/qna/QnaPostCard';
import ForumPostCard from '@/components/forum/ForumPostCard';
import CommentCard from '@/components/profile/CommentCard';
export default {
  props: {
    info: Object,
  },
  components: { QnaPostCard, CommentCard, ForumPostCard },
  data() {
    return {
      autoplay: true,
      slide: 1,
      post: 'forum',
      pinned: 'forum',
      pinned_post: this.info.forums_pinned,
    };
  },
  watch: {
    pinned(newValue) {
      if (newValue === 'forum') this.pinned_post = this.info.forums_pinned;
      else this.pinned_post = this.info.qnas_pinned;
    },
  },
};
</script>

<style scoped>
.pinned-background {
  width: 100%;
  border: 2px solid #fbaa9f;
  border-radius: 5px;
}
.history-background {
  width: 100%;
  border: 2px solid #2f95b4;
  border-raidus: 5px;
}
</style>
