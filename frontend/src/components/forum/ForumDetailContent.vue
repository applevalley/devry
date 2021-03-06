<template>
  <div class="row full-width">
    <template v-if="info.thumbnail">
      <q-img
        class="full-width row items-center"
        position="0 -130px"
        style="height:200px; border:1px solid #cccccc; border-bottom:none "
        :src="info.thumbnail"
      />
    </template>
    <q-card
      flat
      bordered
      class="q-px-lg row col-12 q-pt-xs my-card"
      style="min-height: 300px"
    >
      <div class="row col-12 justify-end">
        <span>
          <q-btn flat round dense icon="more_vert" class="q-mt-md">
            <q-menu>
              <q-list style="min-width: 100px">
                <q-item clickable v-close-popup @click="updateForum">
                  <q-item-section>수정하기</q-item-section>
                </q-item>
                <q-item clickable v-close-popup @click="deleteForum">
                  <q-item-section>삭제하기</q-item-section>
                </q-item>
                <q-separator />
              </q-list>
            </q-menu>
          </q-btn>
        </span>
      </div>
      <q-card-section class="row col-12 q-py-none">
        <div class="row col-12 text-weight-bold q-mb-md text-h4">
          <span>{{ info.title }}</span>
        </div>
        <div class="text-subtitle2 text-grey-6 q-mb-md">
          {{ info.written_time | moment('YYYY/MM/DD HH:mm') }}
        </div>
      </q-card-section>
      <q-card-section class="q-pa-none full-width">
        <div class="q-ml-sm">
          <span v-for="tag in info.ref_tags" :key="tag" class="q-px-xs">
            <q-badge
              class="q-pa-sm text-black"
              :style="{ 'background-color': tagColor(tag, 0.5) }"
              style="font-size:1em; border-radius:3pt;"
            >
              # {{ tag }}
            </q-badge>
          </span>
        </div>
      </q-card-section>
      <div class="row col-12">
        <v-md-editor :value="liquidResolve(content)" mode="preview">
        </v-md-editor>
      </div>
    </q-card>
  </div>
</template>

<script>
import { colorSoloMapper } from '@/utils/tagColorMapper';
import { deleteForumItem } from '@/api/forum';
import { liquidResolver } from '@/utils/liquidTag';
export default {
  props: {
    info: Object,
  },
  data() {
    return {
      content: this.info.content,
    };
  },
  methods: {
    tagColor(tag, alpha) {
      return colorSoloMapper(tag, alpha);
    },
    liquidResolve(tag) {
      return liquidResolver(tag);
    },
    updateForum() {
      this.$router.push(`/forum/${this.info.id}`);
    },
    async deleteForum() {
      try {
        const post_id = this.info.id;
        this.$q.loading.show();
        await deleteForumItem(post_id);
        this.$router.push({ path: '/forum' });
      } catch (error) {
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },
  },
};
</script>

<style scoped></style>
