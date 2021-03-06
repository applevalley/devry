import { instance, instanceAuth } from '@/api';
//// 팔로워
// 로그인한 유저의 팔로워 목록 불러오기 (나를 팔로우하는 사람)
function getFollowerList() {
  return instance.get('myfollower/');
}

// 로그인한 유저의 팔로이 목록 불러오기 (내가 팔로우하는 사람)
function getFolloweeList() {
  return instance.get('myfollow/');
}

// 특정 유저 팔로우하기
function followOtherUser(want_pk) {
  return instanceAuth.post(`following/${want_pk}/`);
}

// 특정 유저의 팔로워 목록 불러오기 (내가 팔로우하는 사람)
function getOtherFollowerList(want_pk) {
  return instance.get(`whofollower/${want_pk}/`);
}

// 특정 유저의 팔로이 목록 불러오기 (내가 팔로우하는 사람)
function getOtherFolloweeList(want_pk) {
  return instance.get(`whofollow/${want_pk}/`);
}

export {
  getFollowerList,
  getFolloweeList,
  followOtherUser,
  getOtherFollowerList,
  getOtherFolloweeList,
};
