<template>
  <div class="row full-width">
    <div
      class="text-primary cursor-pointer full-width"
      @click="$store.commit('onLiquidGuideModal')"
    >
      Liquid 태그 가이드 보기
    </div>
    <div class="text-grey-4">
      Ctrl+S를 통해서 입력한 내용을 미리 보기할 수 있습니다
    </div>
    <!-- 마크다운 에디터 -->
    <div class="row full-width">
      <div class="col-6">
        <v-md-editor
          v-model="content"
          :height="height"
          left-toolbar="undo redo clear | h bold italic strikethrough quote | ul ol table hr | link image code video | save"
          right-toolbar=""
          :disabled-menus="['undo']"
          :toolbar="toolbar"
          mode="edit"
          @upload-image="handleUploadImage"
          @save="renderPreview"
          @input="getContents"
        >
        </v-md-editor>
      </div>

      <q-scroll-area
        :thumb-style="thumbStyle"
        :bar-style="barStyle"
        class="col-6  preview-shadow q-py-lg"
        :style="{ height: height }"
      >
        <v-md-editor
          v-model="translation"
          mode="preview"
          class="col-6"
        ></v-md-editor>
      </q-scroll-area>
    </div>
  </div>
</template>

<script>
import { filtered_tags, first_matched_tag } from '@/utils/autoComplete';
import { liquidResolver } from '@/utils/liquidTag';
import { saveQnaImage } from '@/api/qna';
export default {
  props: {
    height: String,
    fetchData: String,
    mode: String,
  },
  data() {
    return {
      thumbStyle: {
        right: '4px',
        borderRadius: '5px',
        backgroundColor: '#dddddd',
        width: '6px',
        opacity: 0.75,
      },

      barStyle: {
        right: '2px',
        borderRadius: '9px',
        backgroundColor: '#dddddd',
        width: '7px',
        opacity: 0.2,
      },
      user: '',
      profile: '',
      title: '',
      tagItem: '',
      content: this.fetchData ? this.fetchData : '',
      translation: '',
      ref_tags: [],
      img: '',
      imgUrl: 'https//',
      tags: { ...this.$store.state.tags_selected },
      toolbar: {
        video: {
          title: '비디오',
          icon: 'v-md-icon-toc',

          action(editor) {
            editor.insert(function() {
              const imagetxt = 'Image text';
              const image = 'Screenshot image URL';
              const youtube = 'Youtube Link';

              return {
                text: `[![${imagetxt}](${image})](${youtube})`,
                selected: imagetxt,
              };
            });
          },
        },
      },
    };
  },
  watch: {
    fetchData(newValue) {
      this.content = newValue;
    },
  },
  methods: {
    getContents() {
      this.$emit('input', this.content);
    },
    renderPreview(text) {
      this.translation = liquidResolver(text);
    },
    createTag() {
      if (this.tagItem !== '') {
        const str = first_matched_tag(this.tagItem);
        if (str && this.ref_tags.indexOf(str) < 0) {
          this.ref_tags.push(str);
          this.tagItem = '';
        }
      }
    },
    autoCreateTag(tag) {
      if (tag && this.ref_tags.indexOf(tag) < 0) {
        this.ref_tags.push(tag);
        this.tagItem = '';
      }
    },
    removeTag(tag, index) {
      this.ref_tags.splice(index, 1);
    },
    async handleUploadImage(event, insertImage) {
      const frm = new FormData();
      frm.append('image', event.target.files[0]);
      try {
        // 이미지 url 받아오기
        const { data } = await saveQnaImage(frm);
        this.imgUrl = data.image;
      } catch (error) {
        alert(error);
      }
      // Here is just an example
      insertImage({
        url: this.imgUrl,
        desc: 'file_name',
        // responseType: 'blob',
      });
    },
  },
  computed: {
    isValid() {
      return this.tagItem === '' || this.ref_tags.length > 0;
    },
    suggests() {
      return filtered_tags(this.tagItem);
    },
  },
};
</script>
<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
.preview-shadow {
  box-shadow: 0 2px 12px 0 rgb(0 0 0 / 10%);
}
</style>
