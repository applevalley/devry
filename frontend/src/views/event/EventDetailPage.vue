<template>
  <div class="row q-pa-md justify-center q-mt-md">
    <div class="col-7 q-px-lg">
      <!-- 이벤트 메인 -->
      <div class="row full-width q-pb-sm justify-center q-px-sm">
        <!-- 이벤트 썸네일 이미지 -->
        <q-img
          :src="thumnail ? this.thumnail : require('@/assets/basic_image.png')"
          spinner-color="white"
          class="rounded-borders col-6"
        >
          <q-badge
            v-if="bookmarked === false"
            @click="checkbookmarked"
            class="q-ma-xs cursor-pointer"
          >
            <q-icon size="sm" name="turned_in_not" />
          </q-badge>
          <q-badge
            v-else
            @click="checkbookmarked"
            class="q-ma-xs cursor-pointer"
          >
            <q-icon size="sm" name="turned_in" />
          </q-badge>
        </q-img>
        <!-- 이벤트 소개 -->
        <div class=" col-6 q-px-xl q-pt-sm row justify-center">
          <div class="row full-width q-mb-sm">
            <q-badge class="q-pa-xs q-mr-sm" color="orange">
              {{ state }}
            </q-badge>
            <q-badge class="q-pa-xs" color="purple">
              {{ category }}
            </q-badge>
          </div>
          <div class="text-h4 text-weight-bold q-mb-md  full-width">
            {{ title }}
          </div>
          <div class="row q-mb-sm full-width items-center">
            <span class="text-h6 text-weight-bold q-mr-md">장소</span>
            <span>{{ place }}</span>
          </div>
          <div class="row q-mb-sm full-width items-center">
            <div class="text-h6 text-weight-bold q-mr-md">일시</div>
            <div class="row">
              <div class="row full-width">
                {{ start_date }} {{ start_time }} ~ {{ end_date }}
                {{ end_time }}
              </div>
            </div>
          </div>

          <div class="row q-mb-sm full-width items-center">
            <div class="text-h6 text-weight-bold q-mr-md">주최</div>
            <div>{{ host_name }}</div>
          </div>
          <div class="row q-mb-sm full-width items-center">
            <div class="text-h6 text-weight-bold q-mr-md">비용</div>
            <div>{{ cost }}</div>
          </div>
        </div>
      </div>
      <q-separator spaced="md" color="grey-6" />
      <!-- 이벤트 신청 -->
      <div class="row full-width q-my-lg q-px-sm">
        <div class="col-6 ">
          <p>
            <q-icon size="xs" name="bookmarks" /> {{ bookmark_num }}건의 북마크
          </p>
          <p>
            <q-icon size="xs" name="calendar_today" /> 신청기간 :
            {{ start_date }} 까지
          </p>
        </div>
        <div class="col-6 row justify-center">
          <q-btn
            @click="register"
            color="blue-12"
            class="col-8 "
            label="이벤트 페이지로 이동"
            style="max-width:300px; height:50px;"
          />
        </div>
      </div>
      <q-separator spaced="md" color="grey-6" />
      <!-- 이벤트 상세 정보 -->
      <div class="full-width q-mt-lg  q-px-sm">
        <!-- 관련 태그 -->
        <div class="q-mb-xl ">
          <div class="text-h6 text-weight-bold q-mb-md">관련 태그</div>
          <ul class="row q-gutter-sm">
            <li
              v-for="(tag, index) in ref_tags"
              :key="index"
              class="cursor-pointer"
            >
              <q-badge
                class="text-black q-pa-sm q-mr-sm shadow-3"
                :style="{
                  'background-color': tagColor(tag),
                }"
              >
                # {{ tag }}
              </q-badge>
            </li>
          </ul>
        </div>
        <!-- 참가대상 -->
        <div class="q-mt-md row full-width">
          <div class="text-h6 text-weight-bold q-mb-xs full-width">
            이벤트 참가대상
          </div>
          <div>{{ participation }}</div>
        </div>
        <!-- 소개 -->
        <div class="q-mt-lg row full-width">
          <div class="text-h6 text-weight-bold q-mb-xs full-width">
            이벤트 소개
          </div>
          <div>{{ introduction }}</div>
        </div>
        <!-- 스케쥴 -->
        <div class="q-mt-lg row full-width">
          <div class="text-h6 text-weight-bold q-mb-xs full-width">
            이벤트 상세 일정
          </div>
          <div>{{ schedule }}</div>
        </div>
        <!-- 주최자 정보 -->
        <div class="q-my-lg row full-width">
          <div class="row text-h6 text-weight-bold q-mb-xs full-width">
            주최자 정보
          </div>
          <div class="row full-width">
            <img
              :src="
                profile_img
                  ? this.profile_img
                  : require('@/assets/basic_image.png')
              "
              class="col-6 rounded-borders"
              style="width: 70px; height: 50px;"
            />
            <div class="col-6 q-pt-sm q-px-lg text-h6 text-weight-bold">
              {{ host_name }}
            </div>
          </div>
        </div>

        <!-- 수정하기 버튼 -->
        <div class="row q-mb-xl q-mt-md float-right">
          <q-btn
            outline
            color="blue-12"
            class="text-weight-bold q-px-xl q-py-sm q-mr-md"
            label="수정하기"
            size="md"
            @click="updateEvent"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getEvent, toggleEventBookmark } from '@/api/event';
import { colorSoloMapper } from '@/utils/tagColorMapper';

export default {
  data() {
    return {
      state: 'ready',
      thumnail: 'https://placeimg.com/500/300/nature',
      title: 'Vue.js 컨퍼런스',
      place: 'Online',
      category: '컨퍼런스',
      start: '',
      end: '',
      start_date: '2021/02/11',
      end_date: '2021/02/13',
      start_time: '18:00',
      end_time: '19:30',
      cost: '무료',
      participation: '개발자 혹은 개발에 관심있는 누구나',
      introduction: '프론트엔드 개발을 위한 Vue.js 컨퍼런스입니다.',
      schedule:
        '1. 주최자 소개 | 2. 컨퍼런스 소개 | 3. 프론트엔드 프레임워크 소개',
      host_name: 'Eddie',
      profile_img: 'https://cdn.quasar.dev/img/parallax1.jpg',
      register_url: 'https://google.com',
      ref_tags: ['Vue.js', 'Python3', 'JavaScript', 'React'],
      bookmarked: false,
      bookmark_num: 159,
    };
  },
  methods: {
    updateEvent() {
      const post_id = this.$route.params.id;
      // 이벤트 등록 수정하기 페이지로 이동
      this.$router.push({ path: `/event/${post_id}` });
    },
    // 북마크 토글하기
    async checkbookmarked() {
      // 로그인 확인
      if (!this.$store.getters.isLogined) {
        alert('로그인이 필요합니다');
        return;
      }
      const post_id = this.$route.params.id;
      try {
        await toggleEventBookmark(post_id);
        // 넘겨줄 데이터
        this.bookmarked = !this.bookmarked;
        if (this.bookmarked) {
          this.bookmark_num = this.bookmark_num + 1;
        } else {
          this.bookmark_num = this.bookmark_num - 1;
        }
      } catch (error) {
        alert(error);
      }
    },
    register() {
      window.open(this.register_url, '_blank');
    },
    tagColor(tag) {
      return colorSoloMapper(tag, 0.5);
    },
  },
  async created() {
    this.$store.commit('offLeft');
    // id 가져오기
    try {
      const post_id = this.$route.params.id;
      this.$q.loading.show();
      const { data } = await getEvent(post_id);
      // 가져올 데이터 목록
      this.state = data.state;
      this.thumnail = data.thumnail;
      this.title = data.title;
      this.place = data.place;
      this.category = data.category;
      this.start = data.start;
      this.end = data.end;
      this.cost = data.cost;
      this.participation = data.participation;
      this.introduction = data.introduction;
      this.schedule = data.schedule;
      this.host_name = data.host_name;
      this.profile_img = data.profile_img;
      this.register_url = data.register_url;
      this.ref_tags = data.ref_tags;
      this.bookmarked = data.bookmarked;
      this.bookmark_num = data.bookmark_num;
      // 날짜 시간 형식 변경
      const sArray = this.start.split('T');
      this.start_date = sArray[0];
      const stimes = sArray[1].split('+');
      const stime = stimes[0].split(':');
      this.start_time = stime[0] + '시 ' + stime[1] + '분';
      const eArray = this.end.split('T');
      this.end_date = eArray[0];
      const etimes = eArray[1].split('+');
      const etime = etimes[0].split(':');
      this.end_time = etime[0] + '시 ' + etime[1] + '분';
    } catch (error) {
      alert(error);
      // alert('에러가 발생했습니다.)
    } finally {
      this.$q.loading.hide();
    }
  },
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
}
</style>
