<template>
  <div class="full-width">
    <div class="q-mb-md">
      <div class="text-h6 text-weight-bold q-mb-sm">
        Personal details
      </div>
      <div class="row full-width">
        <div class="row col-6">
          <!-- 프로필 이미지 -->
          <q-img
            :src="
              info.profile_img
                ? info.profile_img
                : require('@/assets/basic_image.png')
            "
            spinner-color="white"
            class="rounded-borders q-mb-lg profile-image"
          />
          <div class="q-ml-sm">
            <div class="text-subtitle1">@{{ $store.state.nickname }}</div>
            <div class="text-caption text-grey">{{ profile_info.email }}</div>

            <!-- 이미지 업로드 -->
            <input
              ref="imageInput"
              type="file"
              hidden
              @change="onChangeImages"
            />
            <q-btn
              @click="onClickImageUpload"
              round
              color="primary"
              class="upload-button"
            >
              <q-icon :name="$i.ionCamera"></q-icon>
            </q-btn>
            <span @click="onClickImageUpload" class="upload-button">
              {{ profile_info.chageImg ? '이미지 업로드 성공' : '' }}
            </span>
          </div>
        </div>
        <div class="row col-6">
          <div class="full-width">
            <q-input
              stack-label
              label-slot
              outlined
              v-model="username"
              placeholder="닉네임을 입력해주세요"
            >
              <template v-slot:label>
                <span class="text-primary">이름</span>
                <br />
              </template>
            </q-input>
          </div>

          <div class="full-width">
            <q-input
              stack-label
              label-slot
              outlined
              v-model="profile_info.group"
              placeholder="현재 소속을 입력해주세요"
            >
              <template v-slot:label>
                <span class="text-primary">소속</span>
                <br />
              </template>
            </q-input>
          </div>
        </div>
      </div>

      <div class="row col-6">
        <div class="col-12 q-mb-md">
          <q-input
            stack-label
            label-slot
            outlined
            v-model="profile_info.region"
            placeholder="거주지역을 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">거주지</span>
              <br />
            </template>
          </q-input>
        </div>
      </div>
      <!-- 이름, 소속, 거주지, 자기소개 -->
      <div class="full-width q-mb-xl">
        <div class="col-12">
          <q-input
            v-model="profile_info.bio"
            stack-label
            label-slot
            outlined
            type="textarea"
            placeholder="자기 소개를 입력해주세요"
          >
            <template v-slot:label>
              <span class="text-primary">자기소개</span>
              <br />
            </template>
          </q-input>
        </div>
      </div>
    </div>
    <!-- link 연동 -->
    <div class="full-width q-mb-xl">
      <div class="text-h6 text-weight-bold q-mb-md">
        Links
      </div>
      <div class="row items-center q-mb-sm">
        <div class="col-1 row justify-center">
          <q-icon :name="$i.ionLogoGithub" size="lg" />
        </div>
        <q-input
          class="q-pl-xs col-11"
          stack-label
          clearable
          clear-icon="clear"
          label-slot
          v-model="github"
          placeholder="https://github.com/.."
        >
          <template v-slot:label>
            <span class="text-primary">
              Github URL
            </span>
            <br />
          </template>
        </q-input>
      </div>
      <!-- <div class="row items-center q-mb-sm">
        <div class="col-1 row justify-center">
          <q-icon :name="$i.ionLogoGitlab" size="lg" />
        </div>
        <q-input
          class="q-pl-xs col-11"
          stack-label
          clearable
          clear-icon="clear"
          label-slot
          v-model="gitlab"
          placeholder="https://gitlab.com/.."
        >
          <template v-slot:label>
            <span class="text-primary">
              Gitlab URL
            </span>
            <br />
          </template>
        </q-input>
      </div> -->
      <div class="row items-center q-mb-sm">
        <div class="col-1 row justify-center">
          <q-icon :name="$i.ionLogoFacebook" size="lg" />
        </div>
        <q-input
          stack-label
          label-slot
          clearable
          clear-icon="clear"
          v-model="facebook"
          placeholder="https://www.facebook.com/.."
          class="q-pl-xs col-11"
        >
          <template v-slot:label>
            <span class="text-primary">
              Facebook URL
            </span>
            <br />
          </template>
        </q-input>
      </div>
      <div class="row items-center">
        <div class="col-1 row justify-center">
          <q-icon :name="$i.ionLogoLinkedin" size="lg" />
        </div>
        <q-input
          stack-label
          label-slot
          clearable
          clear-icon="clear"
          v-model="linkedin"
          placeholder="https://www.linkedin.com/in/.."
          class="q-pl-xs col-11"
        >
          <template v-slot:label>
            <span class="text-primary">
              LinkedIn URL
            </span>
            <br />
          </template>
        </q-input>
      </div>
    </div>
    <profile-setting-tech
      @addTechStackItem="addOneSkill"
      @removeTechStackItem="removeOneSkill"
      :propsTechStackData="profile_info.tech_stack"
    ></profile-setting-tech>
    <profile-setting-project
      @addProjectItem="addOneProject"
      @removeProjectItem="removeOneProject"
      :propsProjectData="profile_info.project"
    ></profile-setting-project>
    <profile-setting-tag
      @addTagItem="addOneTag"
      @removeTagItem="removeOneTag"
      :propsTagData="profile_info.my_tags"
    ></profile-setting-tag>
    <!-- 저장 버튼 -->
    <div class="row q-mb-xl q-mt-md float-right ">
      <q-btn
        color="primary"
        label="저장"
        @click="submitForm"
        class="save-button"
      />
    </div>
  </div>
</template>

<script>
import ProfileSettingTech from '@/components/profile/setting/ProfileSettingTech';
import ProfileSettingProject from '@/components/profile/setting/ProfileSettingProject';
import ProfileSettingTag from '@/components/profile/setting/ProfileSettingTag';
import { updateProfile } from '@/api/profile';
import { saveUserNicknameToCookie, deleteCookie } from '@/utils/cookies';
import { saveQnaImage } from '@/api/qna';
export default {
  components: {
    ProfileSettingTech,
    ProfileSettingProject,
    ProfileSettingTag,
  },
  props: {
    info: Object,
  },

  data() {
    return {
      email: '',
      username: this.$store.state.nickname,
      profile_info: this.info,
      chageImg: false,
      github: this.info.link[0].sns_url,
      // gitlab: '',
      facebook: this.info.link[1].sns_url,
      linkedin: this.info.link[2].sns_url,
      file: '',
    };
  },

  // TODO : 프로필 수정 중 페이지를 이동할 때 경고문구 띄우기
  beforeRouteLeave(to, from, next) {
    const answer = window.confirm('정말 페이지를 나가시겠습니까?');
    if (answer) {
      next();
    } else {
      next(false);
    }
  },
  methods: {
    onClickImageUpload() {
      this.$refs.imageInput.click();
    },
    onChangeImages(e) {
      this.file = e.target.files[0];
      this.profile_info.profile_img = URL.createObjectURL(this.file);
    },

    addOneSkill(techStack) {
      if (this.profile_info.tech_stack.indexOf(techStack) < 0)
        this.profile_info.tech_stack.push(techStack);
    },
    removeOneSkill(skill, index) {
      this.profile_info.tech_stack.splice(index, 1);
    },
    addOneProject(pjtName, pjtUrl) {
      this.profile_info.project.push({
        project_name: pjtName,
        project_url: pjtUrl,
      });
    },
    removeOneProject(project, index) {
      this.profile_info.project.splice(index, 1);
    },
    addOneTag(tagItem) {
      this.profile_info.my_tags.push(tagItem);
    },
    removeOneTag(tag, index) {
      this.profile_info.my_tags.splice(index, 1);
    },

    // 프로필 재설정 요청
    async submitForm() {
      try {
        if (this.file) {
          const frm = new FormData();
          frm.append('image', this.file);
          const { data } = await saveQnaImage(frm);
          this.profile_info.profile_img = data.image;
        }

        this.$q.loading.show();
        await updateProfile(this.$store.state.id, {
          username: this.username,
          profile_img: this.profile_info.profile_img,
          region: this.profile_info.region,
          group: this.profile_info.group,
          bio: this.profile_info.bio,
          sns_name1: 'Github',
          sns_url1: this.github,
          sns_name2: 'Facebook',
          sns_url2: this.facebook,
          sns_name3: 'Linkedin',
          sns_url3: this.linkedin,
          tech_stack: this.profile_info.tech_stack,
          project_name1: this.profile_info.project[0].project_name,
          project_url1: this.profile_info.project[0].project_url,
          project_name2: this.profile_info.project[1].project_name,
          project_url2: this.profile_info.project[1].project_url,
          project_name3: this.profile_info.project[2].project_name,
          project_url3: this.profile_info.project[2].project_url,
          my_tags: this.profile_info.my_tags,
        });
        deleteCookie('login_nickname');
        saveUserNicknameToCookie(this.username);
        this.$store.commit('setUsername', this.username);
        alert('성공적으로 프로필을 변경하였습니다!');
        // this.$router.go(-1);
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
.profile-image {
  height: 140px;
  max-width: 150px;
  position: relative;
  border: 1px solid #cccccc;
}
.upload-button {
  position: relative;
  left: -35px;
  top: 60px;
}
.save-button {
  width: 200px;
  height: 50px;
  border-radius: 5px;
}
</style>
