import { instance, instanceAuth } from '@/api';
// 단일 사용자 프로필 정보를 불러온다.
function getProfile(userid) {
  return instance.get(`profiles/${userid}`);
}
// 여러 사용자 프로필 정보를 불러온다
function getProfiles() {
  return instance.get('profiles/');
}
// 프로필 세팅 정보를 불러온다
function loadProfile(profileId) {
  return instanceAuth.get(`profiles/setting/${profileId}/`);
}
// 프로필 정보 수정을 요청한다.
function updateProfile(profileId, profileData) {
  return instanceAuth.put(`profiles/setting/${profileId}/`, profileData);
}
// 프로필 정보 삭제를 요청한다 => 회원탈퇴를 의미
function deleteProfile() {
  return instanceAuth.delete('profiles/setting/');
}
export { getProfile, getProfiles, loadProfile, updateProfile, deleteProfile };
