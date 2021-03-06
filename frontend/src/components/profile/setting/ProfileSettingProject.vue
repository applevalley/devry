<template>
  <div class="col-12 q-mb-md">
    <div class=" q-mb-sm">
      <span class="text-h6 text-weight-bold">
        Project URL
      </span>

      <span class="text-subtitle2">
        최대 3개까지 입력가능
      </span>
    </div>
    <label for="project"></label>
    <div class="row full-width q-mb-sm">
      <q-input
        stack-label
        label-slot
        v-model="pjtName"
        placeholder="프로젝트 이름을 입력해주세요"
        outlined
        class="col-3 q-pr-sm"
      >
        <template v-slot:label>
          <span class="text-primary">
            Name
          </span>
          <br />
        </template>
      </q-input>
      <q-input
        stack-label
        label-slot
        outlined
        v-model="pjtUrl"
        placeholder="프로젝트 URL을 입력해주세요"
        class="col-8"
        @keypress.enter="addProject"
      >
        <template v-slot:label>
          <span class="text-primary">
            Url
          </span>
          <br />
        </template>
      </q-input>
      <div class="col-1 q-pl-sm row justify-end items-center">
        <q-btn
          class="overflow-auto"
          color="primary"
          icon="add"
          @click="addProject"
          style="height:100%"
          :disable="propsProjectData.length < 3 ? false : true"
        />
      </div>
    </div>
    <table class="full-width q-mb-xl q-pa-sm" style="height:150px">
      <tr class="row  full-width">
        <th class="col-3 q-py-sm " style="text-align:start">프로젝트명</th>
        <th class="col-8 q-py-sm " style="text-align:start">프로젝트URL</th>
        <th class="col-1 q-py-sm"></th>
      </tr>
      <tr
        v-for="(project, index) in propsProjectData"
        :key="index"
        class="full-width row"
      >
        <td class="col-3 q-py-xs text-blue-10 text-weight-bold overflow-auto">
          {{ project.project_name }}
        </td>
        <td class="col-8 q-py-xs  row justify-between overflow-auto">
          <div class="text-subtitle2 text-grey-7">
            {{ project.project_url }}
          </div>
        </td>
        <td class="col-1 q-py-xs">
          <div
            @click="removeProject(project, index)"
            class="cursor-pointer col-2 row justify-end"
          >
            <q-icon :name="$i.ionTrash" size="sm" color="grey-6"></q-icon>
          </div>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  props: ['propsProjectData'],
  data() {
    return {
      pjtName: '',
      pjtUrl: '',
    };
  },
  methods: {
    addProject: function() {
      if (this.pjtUrl !== '' && this.pjtName !== '') {
        this.$emit('addProjectItem', this.pjtName, this.pjtUrl);
        (this.pjtName = ''), (this.pjtUrl = '');
      }
    },
    removeProject: function(project, index) {
      this.$emit('removeProjectItem', project, index);
    },
  },
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
table {
  border: 1px solid #eef0f1;
  border-radius: 5px;
}
td ::-webkit-scrollbar {
  display: none;
}
</style>
