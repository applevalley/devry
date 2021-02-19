<template>
  <post-edit-form :file="file" category="forum">
    <template slot="thumbnail">
      <q-file
        v-model="file"
        label="썸네일 등록"
        standout="bg-indigo-3 text-white "
        color="primary"
        style="max-width:300px"
        class="q-mt-none q-mx-none q-mb-lg"
      >
        <template v-slot:prepend>
          <q-icon name="attach_file" />
        </template>
      </q-file>
    </template>
    <template slot="buttons" slot-scope="scopeProps">
      <q-btn
        outline
        color="red-12"
        class="text-weight-bold q-px-xl q-py-sm q-mr-md"
        label="삭제하기"
        size="md"
        @click="scopeProps.deleteForum"
      />
      <q-btn
        color="blue-12"
        class="text-weight-bold q-px-xl q-py-sm"
        label="작성하기"
        size="md"
        @click="scopeProps.updateForum"
      />
    </template>
  </post-edit-form>
</template>

<script>
import PostEditForm from '@/components/common/PostEditForm';

export default {
  components: {
    PostEditForm,
  },
  data() {
    return {
      file: '',
    };
  },
  async created() {
    this.$store.commit('offLeft');
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
