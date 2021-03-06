import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import VueMoment from 'vue-moment';
import './quasar';
// Resources for the basic markdown editor
import VMdEditor from '@kangc/v-md-editor/lib/codemirror-editor';
import VMdPreview from '@kangc/v-md-editor/lib/preview';
import '@kangc/v-md-editor/lib/style/preview.css';
import createCopyCodePlugin from '@kangc/v-md-editor/lib/plugins/copy-code/index';
import '@kangc/v-md-editor/lib/style/codemirror-editor.css';
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js';
import '@kangc/v-md-editor/lib/theme/style/github.css';
import '@kangc/v-md-editor/lib/plugins/copy-code/copy-code.css';
import koKR from '@kangc/v-md-editor/lib/lang/ko-KR';

// Resources for the codemirror editor
import Codemirror from 'codemirror';
import 'codemirror/mode/markdown/markdown';
import 'codemirror/addon/display/placeholder';
import 'codemirror/addon/selection/active-line';
import 'codemirror/addon/scroll/simplescrollbars';
import 'codemirror/addon/scroll/simplescrollbars.css';
import 'codemirror/lib/codemirror.css';

// filter
import { formatNumber } from '@/utils/filters';

// vue-tilt
import VueTilt from 'vue-tilt.js';

// basic markdown editor
VMdEditor.lang.use('ko-KR', koKR);
VMdEditor.Codemirror = Codemirror;
VMdEditor.use(createCopyCodePlugin());
VMdEditor.use(githubTheme, {
  codeHighlightExtensionMap: {
    vue: 'html',
  },
});
VMdEditor.xss.extend({
  // extend white list
  whiteList: {
    source: [],
    iframe: ['src', 'height', 'width', 'frameborder'],
  },
});
VMdPreview.use(githubTheme);
Vue.use(VMdPreview);
Vue.use(VMdEditor);

// Vue Moment
Vue.use(VueMoment);

// Vue tilt
Vue.use(VueTilt);

Vue.config.productionTip = false;

Vue.filter('formatNumber', formatNumber);
new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
