# huaqi-front-end

> A Vue.js project

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

### 项目结构简介

（一些配置文件简介在此省略）

1. Vue.js 框架制作的是一个单页面应用，即整个前端项目只有一个页面，通过前端路由（vue-router）映射并加载不同的视图层组件，实现页面跳转的效果

2. .vue 格式的文件代表一个 vue 组件，封装了一个 html 模板、对应的数据和方法（js部分）以及 css 样式

3. 项目唯一的页面 index.html 挂载了 src/App.vue 组件，src/main.js 声明了一个全局 Vue 对象，src/App.vue 组件中的 <router-view/> 标签表示根据不同路由加载不同的组件，对应规则由 src/router/index.js 确定
4. src/views 存放视图层组件（每一个视图层组件即一个页面），src/components 存放视图层组件中需要嵌套的组件

5. src/storage/index.js 借助 Vuex 实现前端的全局数据管理，可以将后端传送来的需要重复利用的信息保存起来，减少对后端的请求，提升应用运行效率

### 与后端对接的接口

假定后端服务器地址为 localhost:8888

```javascript
/** 
 * 注册
 * 请求类型：post
 * 请求路径：/register
 * 请求头：'application/x-www-form-urlencoded'
 * 传参方式：data（json数组）
 * @param name : 机构名称
 * @param email : 邮箱地址
 * @param pass : 密码
 * @response 接收后端返回的提示信息，类型为Number
 *           0表示注册成功，1表示邮箱已被注册过，2表示服务器异常
 * 注：注册时用户isVIP字段默认为"false"
 */
this.axios({
    method: 'post',
    url: 'localhost:8888/register',
    headers: { 'content-type': 'application/x-www-form-urlencoded' },
    data: {
		name: this.registerForm.name,
		email: this.registerForm.email,
		pass: this.registerForm.pass
	}
}).then(response => {
    // 处理服务器返回的信息
}).catch(error => {
    // 异常处理
})
```

```javascript
/** 
 * 登录
 * 请求类型：post
 * 请求路径：/login
 * 请求头：'application/x-www-form-urlencoded'
 * 传参方式：data（json数组）
 * @param email : 邮箱地址
 * @param pass : 密码
 * @response 接收后端返回的提示信息，类型为Number
 *           0表示登录成功，1表示能查询到邮箱的注册信息但密码错误，2表示查询不到邮箱的注册信息
 *           **若登陆成功，则还需要接收一个json数组，里面包含机构名称和邮箱**
 */
this.axios({
    method: 'post',
    url: 'localhost:8888/login',
    headers: { 'content-type': 'application/x-www-form-urlencoded' },
    data: {
		email: this.registerForm.email,
		pass: this.registerForm.pass
	}
}).then(response => {
    // 处理服务器返回的信息
}).catch(error => {
    // 异常处理
})
```

```javascript
/** 
 * 变更该邮箱绑定的用户的会员信息
 * 请求类型：post
 * 请求路径：/login
 * 请求头：'application/x-www-form-urlencoded'
 * 传参方式：data（json数组）
 * @param email : 邮箱地址
 * @param isVIP : 更新之后的会员信息
 * **数据库中同步修改email对应用户的会员信息即可**
 */
this.axios({
    method: 'post',
    url: 'localhost:8888/updateVIPState',
    headers: { 'content-type': 'application/x-www-form-urlencoded' },
    data: {
		email: this.$store.getters.getUser.name,
		isVIP: callback ? 'true' : 'false'
	}
}).catch(error => {
    // 异常处理
})
```

```javascript
/** 
 * s
 * 请求类型：post
 * 请求路径：/search
 * 请求头：'application/x-www-form-urlencoded'
 * 传参方式：data（json数组）
 * @param searchText : 用户在搜索框中输入的信息
 * @response 接收后端返回的提示信息，类型为json数组，若没有搜索结果则返回null
 *           返回的信息的格式为：
 *			 {
 *				name: 'xxx', // 公司名称
 *				data1: xxx,
 *    			data2: xxx,
 *				…… （待明确）
 *			 }
 */
this.axios({
    method: 'post',
    url: 'localhost:8888/search',
    headers: { 'content-type': 'application/x-www-form-urlencoded' },
    data: {
		searchText: this.searchForm.text
	}
}).catch(response => {
    // 处理服务器返回的信息
}).catch(error => {
    // 异常处理
})
```

