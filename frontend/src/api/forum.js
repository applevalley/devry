import { instance, instanceAuth } from '@/api';

// forum 글 등록하기
function createForumItem(postData) {
  return instanceAuth.post('forum/', postData);
}

// forum 특정 글 불러오기
function loadForumItem(forum_pk) {
  return instance.get(`forum/${forum_pk}/`);
}
// forum 글 수정하기
function updateForumItem(postId, postData) {
  return instanceAuth.put(`forum/${postId}/`, postData);
}

// forum  글 삭제하기
function deleteForumItem(postId) {
  return instance.delete(`forum/${postId}/`);
}

// forum 글 좋아요 토글하기
function toggleForumLike(forum_pk) {
  return instance.post(`forum_like/${forum_pk}/`);
}

// forum 글 Pinned 토글하기
function togglePinned(forum_pk) {
  return instanceAuth.post(`forum_pinned/${forum_pk}/`);
}

// forum 댓글 목록 불러오기
function getForumComment() {
  return instance.get('comment/');
}

// forum 댓글 등록하기
function createForumComment(postData) {
  return instance.post('comment/', postData);
}

// forum 큰 댓글 수정하기
function updateForumComment(comment_pk, putData) {
  return instance.put(`comment/${comment_pk}/`, putData);
}

// forum 큰 댓글 삭제하기
function deleteForumComment(comment_pk) {
  return instance.delete(`comment/${comment_pk}/`);
}

// forum 큰 댓글 멘션 get
function getForumMentioned(comment_pk) {
  return instance.get(`comment/${comment_pk}/mentioned/`);
}

// forum 큰 댓글 멘션 post
function postForumMentioned(comment_pk) {
  return instance.post(`comment/${comment_pk}/mentioned/`);
}

// forum 큰 댓글 좋아요 토글하기
function toggleForumCommentLike(comment_pk) {
  return instance.post(`comment_like/${comment_pk}/`);
}

// forum 게시물 북마크하기
function toggleforumBookmark(forum_pk) {
  return instance.post(`forum_bookmark/${forum_pk}/`);
}

export {
  loadForumItem,
  createForumItem,
  updateForumItem,
  deleteForumItem,
  toggleForumLike,
  getForumComment,
  createForumComment,
  updateForumComment,
  deleteForumComment,
  getForumMentioned,
  postForumMentioned,
  toggleForumCommentLike,
  toggleforumBookmark,
  togglePinned,
};
