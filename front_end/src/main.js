// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import Vuex from 'vuex'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import * as echarts from 'echarts'
import store from './storage/index.js'

axios.defaults.baseURL = 'http://127.0.0.1:5000'

Vue.use(ElementUI)
Vue.use(Vuex)

Vue.prototype.axios = axios
Vue.prototype.$echarts = echarts
Vue.prototype.$store = store
Vue.config.productionTip = false

// 在每次路由跳转前验证用户是否处于登录状态
router.beforeEach((to, from, next) => {
  var isLogin = sessionStorage.getItem('isLogin')
  if (to.path === '/logout') {
    sessionStorage.removeItem('isLogin')
    next({path: '/'})
  } else if (to.path === '/login') {
    if (isLogin !== null) {
      next({path: '/user'})
    }
  } else if (isLogin === null) {
    if (to.path !== '/' &&
        to.path !== '/register' &&
        to.path !== '/user-notice' &&
        to.path !== '/user-agreement') {
      next({path: '/login'})
    }
  }
  if (to.path === '/search-result') {
    next({path: '/company-information'})
  }
  next()
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
