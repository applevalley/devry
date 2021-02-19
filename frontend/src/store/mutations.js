export default {
  onAccountModal(state) {
    state.accountModal = true;
  },
  offAccountModal(state) {
    state.accountModal = false;
  },
  onFollowModal(state, info) {
    state.follow.id = info[1];
    state.follow.modal = true;
    state.follow.tab = info[0];
  },
  offFollowModal(state) {
    state.follow.modal = false;
  },
  onLiquidGuideModal(state) {
    state.liquidTagGuideModal = true;
  },
  setAccountModalType(state, type) {
    state.accountModalType = type;
  },
  setUserid(state, id) {
    state.id = id;
  },
  setUsername(state, nickname) {
    state.nickname = nickname;
  },
  setToken(state, token) {
    state.token = token;
  },
  setPassword(state, password) {
    state.password = password;
  },
  clearUserInfo(state) {
    state.id = '';
    state.nickname = '';
    state.token = '';
  },
  toggleLeft(state) {
    state.leftDrawal = !state.leftDrawal;
  },
  onLeft(state) {
    state.leftDrawal = true;
  },
  offLeft(state) {
    state.leftDrawal = false;
  },
  toggleTagFilter(state) {
    state.tagFilter = !state.tagFilter;
  },
  initSelectedTags(state) {
    state.selectedTags = state.myTags;
  },
  setSelectedTags(state, tags) {
    state.selectedTags = tags;
  },
  setMyTags(state, tags) {
    state.myTags = tags;
  },
};
