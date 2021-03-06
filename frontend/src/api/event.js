import { instance } from '@/api';

// Event 내용 불러오기
function getEvent(postId) {
  return instance.get(`event/${postId}/`);
}

// Event 북마크 토글하기
function toggleEventBookmark(postId) {
  return instance.post(`event_bookmark/${postId}/`);
}
// Event 글 불러오기
function loadEventItem(postId) {
  return instance.get(`event/${postId}/`);
}

// Event 글 등록하기
function createEventItem(postData) {
  return instance.post('event/', postData);
}

// Event 글 수정하기
function updateEventItem(postId, postData) {
  return instance.put(`event/${postId}/`, postData);
}
// Event  글 삭제하기
function deleteEventItem(postId) {
  return instance.delete(`event/${postId}/`);
}
export {
  getEvent,
  toggleEventBookmark,
  loadEventItem,
  createEventItem,
  updateEventItem,
  deleteEventItem,
};
