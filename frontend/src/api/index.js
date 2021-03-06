import axios from 'axios';
import { setInterceptors } from '@/api/common/interceptors';
function createInstance() {
  return axios.create({
    baseURL: process.env.VUE_APP_SERVER_API_URL,
  });
}

// header의 Authorization에 토큰을 부여함
function createInstanceWithAuth(url) {
  const instance = axios.create({
    baseURL: `${process.env.VUE_APP_SERVER_API_URL}${url}`,
  });
  return setInterceptors(instance);
}

const instance = createInstance();
const instanceAuth = createInstanceWithAuth('');
export { instance, instanceAuth };
