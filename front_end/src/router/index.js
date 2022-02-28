import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/views/Login'
import Home from '@/views/Home'
import Register from '@/views/Register'
import User from '@/views/User'
import temp1 from '@/components/temp1'
import temp2 from '@/components/temp2'
import UserCenter from '@/views/UserCenter'

Vue.use(Router)

// 路由管理
// 在<router-view/>处根据routes数组中每个元素的路径path加载对应的组件

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/user',
      name: 'user',
      component: User,
      children: [
        {
          path: '/temp/1/:id',
          name: 'temp1',
          component: temp1
        },
        {
          path: '/temp/2',
          name: 'temp2',
          component: temp2
        }
      ]
    },
    {
      path: '/user-center',
      name: 'user-center',
      component: UserCenter
    }
  ]
})
