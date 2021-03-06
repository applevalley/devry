<template>
  <div class="q-pl-md row col-12">
    <div class="row col-12">
      <q-card flat bordered style="width: 45px; height: 65px;">
        <div style="margin:0 auto; text-align:center" class="q-pt-sm">
          <template v-if="info.liked_ans">
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

          <br />
          <span>{{ info.like_ans_num }}</span>
        </div>
      </q-card>
    </div>
  </div>
</template>

<script>
import { toggleQnaCommentLike } from '@/api/qna';

export default {
  props: {
    info: Object,
  },
  data() {
    return {
      liked_ans: this.info.liked_ans,
      like_ans_num: this.info.like_ans_num,
    };
  },
  methods: {
    async checkLiked() {
      if (!this.$store.getters.isLogined) {
        alert('로그인을 해주세요');
        return;
      }
      try {
        const commentId = this.info.id;
        await toggleQnaCommentLike(commentId);
        this.info.liked_ans = !this.info.liked_ans;
        if (this.info.liked_ans) {
          this.info.like_ans_num = this.info.like_ans_num + 1;
        } else {
          this.info.like_ans_num = this.info.like_ans_num - 1;
        }
      } catch (error) {
        alert(error);
      }
    },
  },
};
</script>

<style scoped></style>
