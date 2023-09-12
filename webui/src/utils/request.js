import axios from 'axios'

let request = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    timeout: 8000
});

// 请求拦截器
request.interceptors.request.use(function (config) {
    return config;
}, function (error) {
    return Promise.reject(error);
});

// 响应拦截器
request.interceptors.response.use(function (response) {
    return response;
}, function (error) {
    return Promise.reject(error);
});

export default request;