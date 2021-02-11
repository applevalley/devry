import { instance } from '@/api';
import { setInterceptors } from '@/api/common/interceptors';

// QnA 글 불러오기
function loadQnaItem(postId) {
  return instance.get(`qna/${postId}/`);
}

// QnA 글 등록하기
function createQnaItem(postData) {
  return instance.post('qna/', postData);
}

// QnA 글 수정하기
function updateQnaItem(postId, postData) {
  return instance.put(`qna/${postId}/`, postData);
}

// QnA  글 삭제하기
function deleteQnaItem(postId) {
  return instance.delete(`qna/${postId}/`);
}

// QnA 작은 댓글 등록하기
function registerSmallComment(postData) {
  return instance.post('qna_create_small/', postData);
}

// QnA 작은 댓글들 불러오기
function getSmallComments(postId) {
  return instance.get(`qna_smallq/${postId}/`);
}
// QnA 작은 댓글 수정하기
function updateSmallComment(qnasmall_pk, putData) {
  return instance.put(`qna_small/${qnasmall_pk}/`, putData);
}
// QnA 작은 댓글 삭제하기
function deleteSmallComment(qnasmall_pk) {
  return instance.delete(`qna_small/${qnasmall_pk}/`);
}

// QnA 글 좋아요 토글하기
function toggleQnaLike(postId) {
  return instance.post(`qna_like/${postId}/`);
}

// QnA 큰 댓글 등록하기
function createQnaBigComment(postData) {
  return instance.post('ans/', postData);
}

// QnA 큰 댓글 수정하기
function updateQnaBigComment(ans_pk, putData) {
  return instance.put(`ans/${ans_pk}/`, putData);
}

// QnA 큰 댓글 삭제하기
function deleteQnaBigComment(ans_pk) {
  return instance.delete(`ans/${ans_pk}/`);
}

// QnA 큰 댓글 좋아요 토글하기
function toggleQnaCommentLike(commentId) {
  // return instance.post(`ans_like/${commentId}/`);
  return setInterceptors(instance).post(`ans_like/${commentId}/`);
}

// QnA 큰 댓글 채택 토글하기
function toggleQnaCommentChoose(ans_pk) {
  return instance.post(`qna_solved/${ans_pk}/`);
}
/////
// QnA 큰 댓글의 작은 댓글들 불러오기
function getRecomments(ans_pk) {
  return instance.get(`ans_smallq/${ans_pk}/`);
}
// QnA 큰 댓글에 작은 댓글 등록하기
function registerRecomment(postData) {
  return instance.post('ans_create_small/', postData);
}
// QnA 큰 댓글의 작은 댓글 수정하기
function updateRecomment(anssmall_pk, putData) {
  return instance.put(`ans_small/${anssmall_pk}/`, putData);
}
// QnA 큰 댓글의 작은 댓글 삭제하기
function deleteRecomment(anssmall_pk) {
  return instance.delete(`ans_small/${anssmall_pk}/`);
}

// QnA 이미지 임시저장 하기
function saveQnaImage(postData) {
  return instance.post('qna_image/', postData);
}

// QnA 이미지 임시저장한 내용 불러오기
function loadQnaImage() {
  return instance.get('qna/');
}

export {
  registerSmallComment,
  getSmallComments,
  toggleQnaLike,
  loadQnaItem,
  createQnaItem,
  updateQnaItem,
  deleteQnaItem,
  createQnaBigComment,
  updateQnaBigComment,
  deleteQnaBigComment,
  toggleQnaCommentLike,
  toggleQnaCommentChoose,
  updateSmallComment,
  deleteSmallComment,
  getRecomments,
  registerRecomment,
  updateRecomment,
  deleteRecomment,
  saveQnaImage,
  loadQnaImage,
};