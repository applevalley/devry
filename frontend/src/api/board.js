import { instance, instanceAuth } from '@/api';

// QnA 게시판에 들어올 QnA 리스트 제공
function getQnaList() {
  return instance.get(`board/qna`);
}
// 이벤트 게시판에 들어올 일반 이벤트 리스트 제공
function getEventList() {
  return instance.get(`board/event`);
}
// 이벤트 게시판에 들어올 메인 이벤트 리스트 제공
function getMainEventList() {
  return instance.get(`board/event/main`);
}

// 포럼 게시판에 들어올 포럼 리스트 제공 - 최신순
function loadForumTime() {
  return instance.get(`board/forumno/`);
}
// 포럼 게시판에 들어올 포럼 리스트 제공 - 피드
function loadForumFeed() {
  return instanceAuth.get(`board/forum/`);
}

export {
  getQnaList,
  getEventList,
  getMainEventList,
  loadForumTime,
  loadForumFeed,
};
