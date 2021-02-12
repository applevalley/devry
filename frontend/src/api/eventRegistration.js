import { instance } from '@/api';

// Event 글 불러오기
function loadEventItem(postId) {
  return instance.get(`event/${postId}/`);
}

// Event 글 등록하기
function createEventItem(postData) {
  return instance.post('event/eventwrite/', postData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
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
  loadEventItem,
  createEventItem,
  updateEventItem,
  deleteEventItem,
};