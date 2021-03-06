<template>
  <div class="col-1 q-pl-lg">
    <q-card class="q-ml-lg" flat style="width: 45px; height: 65px;">
      <div style="margin:0 auto; text-align:center">
        <template v-if="liked_comment">
          <q-icon
            :name="$i.ionHeart"
            color="red"
            size="17px"
            class="cursor-pointer"
            @click="checkLiked"
          ></q-icon>
        </template>
        <template v-else>
          <q-icon
            :name="$i.ionHeartOutline"
            style="color:#727272"
            size="17px"
            class="cursor-pointer"
            @click="checkLiked"
          ></q-icon>
        </template>
        <span class="q-ml-sm q-mt-md">{{ like_comment_num }}</span>
        <br />
        <br />
      </div>
    </q-card>
  </div>
</template>

<script>
import { toggleForumCommentLike } from '@/api/forum';
export default {
  props: {
    info: Object,
  },
  data() {
    return {
      liked_comment: this.info.liked_comment,
      like_comment_num: this.info.like_comment_num,
    };
  },
  watch: {
    info(newValue) {
      (this.liked_comment = newValue.liked_comment),
        (this.like_comment_num = newValue.like_comment_num);
    },
  },
  methods: {
    async checkLiked() {
      if (!this.$store.getters.isLogined) {
        alert('로그인을 해주세요');
        return;
      }
      const commentId = this.info.id;
      try {
        await toggleForumCommentLike(commentId);
        this.liked_comment = !this.liked_comment;
        if (this.liked_comment) {
          this.like_comment_num = this.like_comment_num + 1;
        } else {
          this.like_comment_num = this.like_comment_num - 1;
        }
      } catch (error) {
        alert(error);
      }
    },
  },
};
</script>

<style scoped></style>
