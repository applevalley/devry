<template>
  <q-card class="col-7">
    <div class="row full-width">
      <!-- chart.js를 이용해 태그로 보는 포스팅 횟수 출력 -->
      <div class="row col-6 ">
        <q-card-section class="row justify-center full-width">
          <div class=" text-bold q-mb-md text-center full-width">
            태그로 보는 포스팅 횟수
          </div>
          <pie-chart
            v-if="loaded && tagCounts.length"
            :data="chartData"
            :options="chartOptions"
            style="width:25vw"
          ></pie-chart>
          <span v-else class="text-grey-5 full-width text-center">
            없음
          </span>
        </q-card-section>
      </div>

      <!-- My Tags, My Skills, My Projects, My History -->
      <div class="row col-6 items-start">
        <div class="row items-start col-12">
          <div class="col-6">
            <q-card-section>
              <div class="text-bold q-mb-md  text-center">
                My Tags
              </div>
              <div class="row q-mb-xl items-center justify-center">
                <span
                  v-for="(tag, index) in info.myTags"
                  :key="tag"
                  class="q-mb-sm q-mr-xs q-pa-sm"
                  :style="{ 'background-color': tagColors[index] }"
                  style="font-size:10pt; border-radius:5pt;"
                  >#{{ tag }}</span
                >
                <span v-if="info.myTags.length == 0" class="text-grey-5">
                  없음
                </span>
              </div>
            </q-card-section>
          </div>
          <div class="col-6">
            <q-card-section>
              <div class=" text-bold q-mb-md text-center">
                My Skills/languages
              </div>
              <div class="row items-center justify-center">
                <span
                  v-for="skill in info.skills"
                  :key="skill"
                  class="q-mb-sm q-mr-xs q-pa-sm my-grey-background"
                  >{{ skill }}</span
                >
                <span v-if="info.skills.length == 0" class="text-grey-5">
                  없음
                </span>
              </div>
            </q-card-section>
          </div>
        </div>
        <div class="row items-start col-12 ">
          <div class="col-6 ">
            <q-card-section>
              <div class="text-bold text-center q-mb-md">
                My Projects
              </div>
              <div class="row full-width ">
                <q-list
                  separator
                  class="full-width items-center justify-center row"
                >
                  <q-item
                    clickable
                    v-ripple
                    class="q-mb-sm full-width my-grey-background"
                    v-for="project in info.projects"
                    :key="project.project_name"
                  >
                    <q-item-section>
                      <div
                        style="color: #08458C"
                        class="text-center  q-py-none"
                      >
                        <a :href="project.project_url" target="_blank">
                          {{ project.project_name }}
                        </a>
                      </div>
                    </q-item-section>
                  </q-item>
                  <span v-if="info.projects.length == 0" class="text-grey-5">
                    없음
                  </span>
                </q-list>
              </div>
            </q-card-section>
          </div>
          <div class="col-6">
            <q-card-section>
              <div class=" text-bold q-mb-md text-center">
                My History
              </div>
              <div class="row" style="width:100%">
                <q-list separator style="width:100%">
                  <q-item
                    clickable
                    v-ripple
                    style="background-color:#FADDDD; border-radius:6px; "
                    class="q-mb-sm q-pl-lg"
                  >
                    <q-item-section avatar>
                      <span
                        ><q-icon
                          :name="$i.ionDocumentTextOutline"
                          size="24px"
                        />
                        posts</span
                      >
                    </q-item-section>
                    <q-item-section
                      ><div class="row text-bold justify-end">
                        {{ info.postNum }}
                      </div></q-item-section
                    >
                  </q-item>
                  <q-item
                    clickable
                    v-ripple
                    style="background-color:#BAD9F6; border-radius:6px"
                    class="q-mb-sm q-pl-lg"
                  >
                    <q-item-section avatar>
                      <span
                        ><q-icon
                          :name="$i.ionChatboxEllipsesOutline"
                          size="24px"
                        />
                        comments</span
                      >
                    </q-item-section>
                    <q-item-section
                      ><div class="row text-bold justify-end">
                        {{ info.commentNum }}
                      </div></q-item-section
                    >
                  </q-item>
                  <q-item
                    clickable
                    v-ripple
                    style="background-color:#DCA4E5; border-radius:6px; "
                    class="q-pl-lg"
                  >
                    <q-item-section avatar>
                      <span
                        ><q-icon :name="$i.ionPricetagsOutline" size="24px" />
                        tags</span
                      >
                    </q-item-section>
                    <q-item-section>
                      <div class="row text-bold justify-end">
                        <span>{{ tagLength }}</span>
                      </div>
                    </q-item-section>
                  </q-item>
                </q-list>
              </div>
            </q-card-section>
          </div>
        </div>
      </div>
    </div>
  </q-card>
</template>

<script>
import PieChart from '@/utils/pieChart';
import { colorListMapper } from '@/utils/tagColorMapper';
export default {
  components: {
    PieChart,
  },
  props: {
    info: Object,
  },
  data() {
    return {
      chartOptions: {
        responsive: true,
        cutoutPercentage: 75,
        legend: {
          display: true,
          position: 'bottom',
          fullWidth: true,
          labels: {
            boxWidth: 10,
            fontSize: 14,
          },
        },
        animation: {
          animateScale: true,
        },
        hoverBorderWidth: 20,
      },
      chartData: {
        hoverBackgroundColor: 'red',
        hoverBorderWidth: 10,
        labels: '',
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '',
            data: '',
          },
        ],
      },
      tagNames: [],
      tagColors: [],
      tagBoldColors: [],
      tagLength: 0,
      tagCounts: [],
      loaded: false,
    };
  },
  created() {
    this.tagNames = Object.keys(this.info.tags);
    this.tagColors = colorListMapper(this.info.myTags, 0.5);
    this.tagBoldColors = colorListMapper(this.tagNames, 1);
    this.tagLength = this.tagNames.length;
    this.tagCounts = Object.values(this.info.tags);
    this.chartData.labels = this.tagNames;
    this.chartData.datasets[0].backgroundColor = this.tagBoldColors;
    this.chartData.datasets[0].data = this.tagCounts;
    this.loaded = true;
  },
};
</script>

<style scoped>
a:link {
  color: #08458c;
  text-decoration: none;
}
a:visited {
  color: #08458c;
  text-decoration: none;
}
a:hover {
  color: #08458c;
  text-decoration: none;
}
.my-grey-background {
  background-color: #dddddd;
  font-size: 10pt;
  border-radius: 5pt;
}
</style>
