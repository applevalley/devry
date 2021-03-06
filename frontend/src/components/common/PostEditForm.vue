<template>
  <div class="q-pa-md q-gutter-sm row justify-center">
    <div class="q-pa-sm" style="width: 85vw;">
      <div class="q-pa-md q-gutter-sm">
        <!-- 제목 입력 -->
        <q-input
          class=" q-my-md text-h4 text-weight-bolder q-mx-none"
          borderless
          v-model="title"
          placeholder="제목을 입력해주세요"
          maxlength="70"
        />
        <!-- 썸네일 -->
        <slot name="thumbnail"> </slot>
        <!-- 태그 입력 -->
        <q-input
          class="q-ma-none"
          borderless
          v-model="tagItem"
          placeholder="태그를 두개 이상 네개 이하로 입력해주세요"
          @keypress.enter="createTag"
          :disable="ref_tags.length >= 4"
        >
        </q-input>
        <!-- 자동완성 -->
        <div class="row col-12">
          <div
            class="row col-3 bg-light-blue-1"
            style="position: absolute; z-index:999; border-radius: 5px;"
          >
            <div
              v-for="tag in suggests"
              class="col-12 q-py-md q-px-md"
              :class="{ 'bg-blue-3': tags[tag] }"
              :key="tag"
              @click="checkDuplicateTag(tag)"
              @mouseover="tags[tag] = true"
              @mouseout="tags[tag] = false"
            >
              {{ tag }}
            </div>
          </div>
        </div>
        <!-- 태그 보여주기 -->
        <ul class="row relative-position q-mx-none q-my-none q-mb-lg">
          <li
            class="q-mb-xs cursor-pointer q-ml-none q-mr-sm"
            v-for="(tag, index) in ref_tags"
            :key="index"
          >
            <q-chip outline square color="primary" class="q-ma-none">
              <div @click="removeTag(tag, index)">{{ tag }}</div>
            </q-chip>
          </li>
        </ul>

        <!-- 마크다운 에디터 -->
        <markdown-editor
          :height="'800px'"
          :fetchData="content"
          @input="getContents"
        ></markdown-editor>
      </div>
      <!-- 버튼 -->
      <div class="q-mb-xl q-mt-xl" style="text-align: center;">
        <slot
          name="buttons"
          :createQna="createQna"
          :updateQna="updateQna"
          :deleteQna="deleteQna"
          :createForum="createForum"
          :updateForum="updateForum"
          :deleteForum="deleteForum"
        ></slot>
      </div>
    </div>
  </div>
</template>

<script>
import { filtered_tags, first_matched_tag } from '@/utils/autoComplete';
import MarkdownEditor from '@/components/common/MarkdownEditor';
import {
  createQnaItem,
  updateQnaItem,
  deleteQnaItem,
  loadQnaItem,
} from '@/api/qna';
import {
  createForumItem,
  loadForumItem,
  updateForumItem,
  deleteForumItem,
} from '@/api/forum';
import { saveQnaImage } from '@/api/qna';
export default {
  components: {
    MarkdownEditor,
  },
  props: ['file', 'category'],
  data() {
    return {
      user: '',
      profile: '',
      title: '',
      tagItem: '',
      content: '',
      ref_tags: [],
      thumbnail: '',
      img: '',
      imgUrl: 'https//',
      tags: { ...this.$store.state.tags_selected },
      loaded: false,
    };
  },
  async created() {
    // update의 경우에만 기존의 data를 불러옴
    const post_id = this.$route.params.id;
    if (post_id) {
      if (this.category == 'qna') {
        try {
          this.$q.loading.show();
          const { data } = await loadQnaItem(post_id);
          this.user = data.user;
          this.profile = data.profile;
          this.title = data.title;
          this.content = data.content;
          this.ref_tags = data.ref_tags;
        } catch (error) {
          alert(error);
        } finally {
          this.$q.loading.hide();
        }
      } else {
        try {
          this.$q.loading.show();
          const { data } = await loadForumItem(post_id);
          const loadedData = data;
          this.title = loadedData.title;
          this.content = loadedData.content;
          this.ref_tags = loadedData.ref_tags;
          this.thumbnail = loadedData.thumbnail;
        } catch (error) {
          alert(error);
        } finally {
          this.$q.loading.hide();
        }
      }
    }
  },
  computed: {
    // 일부 문자열을 받고 정규 표현식을 활용하여 비슷한 형태의 문자열 목록을 반환
    suggests() {
      return filtered_tags(this.tagItem);
    },
  },
  methods: {
    // 마크다운 에디터에서 input 이벤트가 발생할 경우 데이터를 content에 저장한다.
    getContents(data) {
      this.content = data;
    },

    // 양식 폼이 잘 쓰였는지 확인한다.
    checkForm() {
      if (this.title === '') {
        alert('제목은 필수 입력 항목입니다');
        return true;
      }
      if (this.ref_tags.length < 2) {
        alert('태그를 둘 이상 입력해주세요');
        return true;
      }
      if (this.ref_tags.length > 4) {
        alert('태그를 넷 이하로 입력해주세요');
        return true;
      }
      if (this.content === '') {
        alert('내용은 필수 입력항목 입니다');
        return true;
      }
      return false;
    },

    // 태그 일부 입력시 정규 표현식을 통해 적합한 태그를 자동 등록해준다
    createTag() {
      if (this.tagItem !== '') {
        const str = first_matched_tag(this.tagItem);
        this.checkDuplicateTag(str);
      }
    },

    // 태그 중복을 확인한다
    checkDuplicateTag(tag) {
      if (tag && this.ref_tags.indexOf(tag) < 0) {
        this.ref_tags.push(tag);
        this.tagItem = '';
      }
    },

    // 태그 삭제
    removeTag(tag, index) {
      this.ref_tags.splice(index, 1);
    },

    // QnA 포스트를 새롭게 생성한다.
    async createQna() {
      if (this.checkForm()) return;

      try {
        this.$q.loading.show();
        await createQnaItem({
          title: this.title,
          user: this.$store.state.id,
          content: this.content,
          ref_tags: this.ref_tags,
        });
        // 이전 페이지로 이동
        this.$router.go(-1);
      } catch (error) {
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },

    // 기존의 QnA 포스트를 수정한다.
    async updateQna() {
      if (this.checkForm()) return;
      try {
        // post_id 넘겨주기
        const post_id = this.$route.params.id;
        this.$q.loading.show();
        await updateQnaItem(post_id, {
          title: this.title,
          user: this.user.id,
          content: this.content,
          ref_tags: this.ref_tags,
        });
        // 이전 페이지로 이동
        this.$router.go(-1);
      } catch (error) {
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },

    // 기존의 QnA 포스트를 삭제한다.
    async deleteQna() {
      try {
        const post_id = this.$route.params.id;
        this.$q.loading.show();
        await deleteQnaItem(post_id);
        // 이전 페이지로 이동
        this.$router.go(-1);
      } catch (error) {
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },

    // Forum post 생성
    async createForum() {
      if (this.checkForm()) return;
      try {
        this.$q.loading.show();
        // 썸네일을 우선 서버에 저장한다.
        if (this.file) {
          const frm = new FormData();
          frm.append('image', this.file);
          const { data } = await saveQnaImage(frm);
          this.thumbnail = data.image;
        }

        // 돌려받은 썸네일 url을 thumbnail 항목에 넣어서 저장한다.
        await createForumItem({
          title: this.title,
          user: this.$store.state.id,
          content: this.content,
          ref_tags: this.ref_tags,
          thumbnail: this.thumbnail,
        });

        // 이전 페이지로 이동
        this.$router.go(-1);
      } catch (error) {
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },

    // 기존의 QnA 포스트를 수정한다.
    async updateForum() {
      if (this.checkForm()) return;
      try {
        this.$q.loading.show();
        // 썸네일을 우선 서버에 저장한다.
        if (this.file) {
          const frm = new FormData();
          frm.append('image', this.file);
          const { data } = await saveQnaImage(frm);
          this.thumbnail = data.image;
        }

        // 돌려받은 썸네일 url을 thumbnail 항목에 넣어서 저장한다.
        await updateForumItem(this.$route.params.id, {
          title: this.title,
          user: this.$store.state.id,
          content: this.content,
          ref_tags: this.ref_tags,
          thumbnail: this.thumbnail,
        });

        // 이전 페이지로 이동
        this.$router.go(-1);
      } catch (error) {
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },

    // 기존의 QnA 포스트를 삭제한다.
    async deleteForum() {
      try {
        const post_id = this.$route.params.id;
        this.$q.loading.show();
        await deleteForumItem(post_id);
        // 이전 페이지로 이동
        this.$router.go(-1);
      } catch (error) {
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },
  },
};
</script>
<style scoped>
ul {
  list-style-type: none;
  padding: 0px;
}
.preview-shadow {
  box-shadow: 0 2px 12px 0 rgb(0 0 0 / 10%);
}
</style>
