import { board } from '@/api';
function getQnaList() {
  return board.get(`qna`);
}

function getEventList() {
  return board.get(`event`);
}

function getMainEventList() {
  return board.get(`event/main`);
}

// forum board - 최신순 리스트 불러오기
function loadForumNew() {
  return board.get(`forumno/`);
}
// forum board - 피드 리스트 불러오기
function loadForumFeed() {
  return board.get(`forum/`);
}

export {
  getQnaList,
  getEventList,
  getMainEventList,
  loadForumNew,
  loadForumFeed,
};
