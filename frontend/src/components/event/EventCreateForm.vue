<template>
  <div class="full-width">
    <!-- 메인 이미지 설정 -->
    <q-toggle
      class="float-right"
      v-model="king"
      checked-icon="check"
      color="primary"
      label="메인 이벤트 설정"
      unchecked-icon="clear"
    />
    <!-- 기본 정보 입력 part -->
    <div class="q-mb-md">
      <div class="text-h6 text-weight-bold q-mt-xl q-mb-sm">
        Event Information
      </div>
      <div class="full-width">
        <div class="row q-mb-xl relative-position">
          <!-- 이미지 등록 -->
          <q-img
            :src="thumnail ? thumnail : require('@/assets/basic_image.png')"
            spinner-color="white"
            style="height: 215px;"
            class="rounded-borders col-8"
          />
          <div class="q-ml-lg col-3">
            <!-- 이미지 등록 버튼 -->
            <q-file
              v-model="file"
              label="대표 이미지 등록"
              standout="bg-indigo-3 text-white "
              color="blue-12"
              bg-color="blue-12"
              label-color="white"
              style="max-width: 200px; position:absolute; bottom:0px;"
            >
              <template v-slot:append>
                <q-icon name="attachment" class="text-white" />
              </template>
            </q-file>
          </div>
        </div>
        <!-- 이벤트 상태 및 카테고리 -->
        <div class="full-width row q-mb-xl">
          <q-select
            class="col-6 q-pr-sm"
            stack-label
            label-slot
            outlined
            v-model="state"
            :options="state_options"
          >
            <template v-slot:label>
              <span class="text-primary">진행 상태</span>
              <br />
            </template>
          </q-select>
          <q-select
            class="col-6"
            stack-label
            label-slot
            outlined
            v-model="category"
            :options="category_options"
          >
            <template v-slot:label>
              <span class="text-primary">카테고리</span>
              <br />
            </template>
          </q-select>
        </div>
        <!-- 이벤트 타이틀 -->
        <div class="full-width q-mb-xl">
          <q-input
            class="col-12"
            stack-label
            label-slot
            outlined
            v-model="title"
            placeholder="타이틀을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">타이틀</span>
              <br />
            </template>
          </q-input>
        </div>
        <!-- 이벤트 날짜 -->
        <div class="full-width row q-mb-xl">
          <q-input
            class="col-6 q-pr-sm"
            stack-label
            label-slot
            outlined
            v-model="start"
            placeholder="이벤트 시작일과 시간을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">시작일정</span>
              <br />
            </template>
            <template slot="append">
              <q-icon name="event" class="cursor-pointer">
                <q-popup-proxy
                  ref="qDateProxy"
                  transition-show="scale"
                  transition-hide="scale"
                >
                  <q-date v-model="start" mask="YYYY-MM-DD HH:mm">
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-date>
                </q-popup-proxy>
              </q-icon>
            </template>
            <template slot="append">
              <q-icon name="access_time" class="cursor-pointer">
                <q-popup-proxy transition-show="scale" transition-hide="scale">
                  <q-time v-model="start" mask="YYYY-MM-DD HH:mm">
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-time>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
          <q-input
            class="col-6"
            stack-label
            label-slot
            outlined
            v-model="end"
            placeholder="이벤트 종료일과 시간을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">종료일정</span>
              <br />
            </template>
            <template slot="append">
              <q-icon name="event" class="cursor-pointer">
                <q-popup-proxy
                  ref="qDateProxy"
                  transition-show="scale"
                  transition-hide="scale"
                >
                  <q-date v-model="end" mask="YYYY-MM-DD HH:mm">
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-date>
                </q-popup-proxy>
              </q-icon>
            </template>
            <template slot="append">
              <q-icon name="access_time" class="cursor-pointer">
                <q-popup-proxy transition-show="scale" transition-hide="scale">
                  <q-time v-model="end" mask="YYYY-MM-DD HH:mm">
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-time>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
        </div>
        <!-- 이벤트 장소 및 비용 -->
        <div class="full-width row q-mb-xl">
          <q-input
            class="col-6 q-pr-sm"
            stack-label
            label-slot
            outlined
            v-model="place"
            placeholder="이벤트 장소를 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">장소</span>
              <br />
            </template>
          </q-input>
          <q-input
            class="col-6"
            stack-label
            label-slot
            outlined
            v-model="cost"
            placeholder="이벤트 비용을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">비용</span>
              <br />
            </template>
          </q-input>
        </div>
      </div>
    </div>
    <!-- 이벤트 소개 part -->
    <div class="q-mb-md">
      <div class="text-h6 text-weight-bold q-mt-xl q-mb-sm">
        Event introduction
      </div>
      <div class="full-width">
        <!-- 참가대상 -->
        <div class="full-width q-mb-xl">
          <q-input
            class="col-12"
            stack-label
            label-slot
            outlined
            v-model="participation"
            placeholder="참가대상을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">참가대상</span>
              <br />
            </template>
          </q-input>
        </div>
        <!-- 이벤트 소개글 -->
        <div class="full-width q-mb-xl">
          <q-input
            class="col-12"
            stack-label
            label-slot
            outlined
            v-model="introduction"
            placeholder="이벤트를 소개해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">소개</span>
              <br />
            </template>
          </q-input>
        </div>
        <!-- 스케쥴 -->
        <div class="full-width q-mb-xl">
          <q-input
            class="col-12"
            type="textarea"
            stack-label
            label-slot
            outlined
            v-model="schedule"
            placeholder="스케쥴을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">스케쥴</span>
              <br />
            </template>
          </q-input>
        </div>
      </div>
    </div>
    <!-- 호스트 정보 입력 part -->
    <div class="q-mb-md">
      <div class="text-h6 text-weight-bold q-mt-xl q-mb-sm">
        Host Information
      </div>
      <div class="full-width">
        <div class="row q-mb-xl relative-position">
          <!-- 프로필 이미지 등록 -->
          <q-img
            :src="
              profile_img ? profile_img : require('@/assets/basic_image.png')
            "
            spinner-color="white"
            style="height: 127px; max-width: 250px; "
            class="rounded-borders col-3"
          />
          <div class="q-ml-lg col-3">
            <!-- 프로필 이미지 등록 버튼 -->
            <q-file
              v-model="second_file"
              label="프로필 이미지 등록"
              standout="bg-indigo-3 text-white "
              color="blue-12"
              bg-color="blue-12"
              label-color="white"
              style="max-width: 200px; border-radius:5px; position:absolute; bottom:0px; "
            >
              <template v-slot:append>
                <q-icon name="attachment" class="text-white" />
              </template>
            </q-file>
          </div>
        </div>
        <!-- 호스트 이름 -->
        <div class="full-width q-mb-xl">
          <q-input
            class="col-12"
            stack-label
            label-slot
            outlined
            v-model="host_name"
            placeholder="호스트 명을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">호스트 이름</span>
              <br />
            </template>
          </q-input>
        </div>
        <!-- 이벤트 등록 url -->
        <div class="full-width q-mb-xl">
          <q-input
            class="col-12"
            stack-label
            label-slot
            outlined
            v-model="register_url"
            placeholder="이벤트 등록을 위한 url을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">이벤트 등록 URL</span>
              <br />
            </template>
          </q-input>
        </div>
      </div>
    </div>
    <!-- 이벤트 관련 태그 -->
    <event-create-tag
      @addTagItem="addOneTag"
      @removeTagItem="removeOneTag"
      :propsTagData="ref_tags"
    >
    </event-create-tag>
    <!-- 버튼 -->
    <div class="row q-mb-md q-mt-xl float-right" style="margin-bottom: 150px;">
      <div v-if="this.$route.params.id !== undefined">
        <q-btn
          outline
          color="red-12"
          class="text-weight-bold q-px-xl q-py-sm q-mr-md"
          label="삭제하기"
          size="md"
          @click="deleteEvent"
        />
        <q-btn
          color="blue-12"
          label="수정하기"
          class="text-weight-bold q-px-xl q-py-sm"
          size="md"
          @click="updateEvent"
        />
      </div>
      <q-btn
        v-else
        color="blue-12"
        label="등록하기"
        class="text-weight-bold q-px-xl q-py-sm"
        size="md"
        @click="createEvent"
      />
    </div>
  </div>
</template>

<script>
import EventCreateTag from '@/components/event/EventCreateTag';
import {
  loadEventItem,
  createEventItem,
  updateEventItem,
  deleteEventItem,
} from '@/api/event';
import { saveQnaImage } from '@/api/qna';

export default {
  components: {
    EventCreateTag,
  },
  data() {
    return {
      state: 'Ready',
      state_options: ['Ready', 'Start', 'End'],
      thumnail: require('@/assets/basic_image.png'),
      title: '',
      category: 'Conference',
      category_options: [
        'Conference',
        'Workshop',
        'Hackathon',
        'Competition',
        'Meeting',
        'Recruting',
      ],
      place: '',
      start: '',
      end: '',
      cost: '',
      participation: '',
      introduction: '',
      schedule: '',
      host_name: '',
      profile_img: require('@/assets/basic_image.png'),
      register_url: '',
      ref_tags: [],
      king: false,
      file: '',
      second_file: '',
    };
  },
  watch: {
    file() {
      this.thumnail = URL.createObjectURL(this.file);
    },
    second_file() {
      this.profile_img = URL.createObjectURL(this.second_file);
    },
  },
  methods: {
    addOneTag(tagItem) {
      this.ref_tags.push(tagItem);
    },
    removeOneTag(tag, index) {
      this.ref_tags.splice(index, 1);
    },
    async createEvent() {
      try {
        this.$q.loading.show();
        // 메인 이미지 서버에 저장하기
        if (this.file) {
          const frm = new FormData();
          frm.append('image', this.file);
          const { data } = await saveQnaImage(frm);
          this.thumnail = data.image;
        }
        // 호스트 프로필 서버에 저장하기
        if (this.second_file) {
          const frm = new FormData();
          frm.append('image', this.second_file);
          const { data } = await saveQnaImage(frm);
          this.profile_img = data.image;
        }
        // 이벤트 새로 생성하기
        await createEventItem({
          // 넘길 데이터 적어주기
          state: this.state,
          thumnail: this.thumnail,
          title: this.title,
          category: this.category,
          place: this.place,
          start: this.start,
          end: this.end,
          cost: this.cost,
          participation: this.participation,
          introduction: this.introduction,
          schedule: this.schedule,
          host_name: this.host_name,
          profile_img: this.profile_img,
          register_url: this.register_url,
          ref_tags: this.ref_tags,
          user: this.$store.state.id,
          king: this.king,
        });
        // 이동 시킬 페이지 적어주기(이벤트 게시판)
        this.$router.push({ path: '/event' });
      } catch (error) {
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },
    // 이벤트 수정하기
    async updateEvent() {
      // id 넘겨주기
      const post_id = this.$route.params.id;
      try {
        this.$q.loading.show();
        // 메인 이미지 서버에 저장하기
        if (this.file) {
          const frm = new FormData();
          frm.append('image', this.file);
          const { data } = await saveQnaImage(frm);
          this.thumnail = data.image;
        }
        // 호스트 프로필 서버에 저장하기
        if (this.second_file) {
          const frm = new FormData();
          frm.append('image', this.second_file);
          const { data } = await saveQnaImage(frm);
          this.profile_img = data.image;
        }
        await updateEventItem(post_id, {
          // 넘길 데이터 적어주기
          state: this.state,
          thumnail: this.thumnail,
          title: this.title,
          category: this.category,
          place: this.place,
          start: this.start,
          end: this.end,
          cost: this.cost,
          participation: this.participation,
          introduction: this.introduction,
          schedule: this.schedule,
          host_name: this.host_name,
          profile_img: this.profile_img,
          register_url: this.register_url,
          ref_tags: this.ref_tags,
          user: this.$store.state.id,
          king: this.king,
        });
        // 이동 시킬 페이지 적어주기(이벤트 게시판)
        this.$router.push({ path: '/event' });
      } catch (error) {
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },
    // 이벤트 삭제하기
    async deleteEvent() {
      try {
        const post_id = this.$route.params.id;
        this.$q.loading.show();
        await deleteEventItem(post_id);
        this.$router.push({ path: '/event' });
      } catch (error) {
        alert(error);
      } finally {
        this.$q.loading.hide();
      }
    },
  },
  // Event 수정하기 (데이터 받아오기)
  async created() {
    this.$store.commit('offLeft');
    // id 가져오기
    const post_id = this.$route.params.id;
    // post_id가 존재할 경우에 기존 정보 가져오기
    if (post_id) {
      try {
        this.$q.loading.show();
        const { data } = await loadEventItem(post_id);
        // 가져올 데이터 목록
        this.state = data.state;
        this.thumnail = data.thumnail;
        this.title = data.title;
        this.category = data.category;
        this.place = data.place;
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
        this.king = data.king;
      } catch (error) {
        alert(error);
        // alert('에러가 발생했습니다.)
      } finally {
        this.$q.loading.hide();
      }
    }
  },
};
</script>

<style></style>
