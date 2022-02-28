<template>
<!-- 用户中心页面，可以查看用户信息 -->
  <div class="userCenterBox">
    <div>
      <el-avatar icon="el-icon-user-solid"></el-avatar>
      <p>用户中心</p>
    </div>
    <el-descriptions class="margin-top" :column="1" border>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-user"></i>
          <span>机构名称</span>
        </template>
        <span>{{this.$store.getters.getUser.name}}</span>
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-message"></i>
          <span>电子邮箱</span>
        </template>
        <span>{{this.$store.getters.getUser.email}}</span>
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-star-off"></i>
          <span>会员信息</span>
        </template>
        <el-switch v-model="isVIP" @change="changeVIPState"></el-switch>
        <span v-if=this.isVIP>会员用户</span>
        <span v-else>普通用户</span>
      </el-descriptions-item>
    </el-descriptions>
  </div>
</template>

<script>
export default {
  name: 'UserCenter',
  data () {
    return {
      isVIP: this.$store.getters.getUser.isVIP === 'true'
    }
  },
  methods: {
    changeVIPState (callback) {
      this.$store.dispatch('asynUpdateVIPState', callback)
      // this.axios({
      //   method: 'post',
      //   url: '服务器地址/updateVIPState',
      //   headers: { 'content-type': 'application/x-www-form-urlencoded' },
      //   data: {
      //     name: this.$store.getters.getUser.name,
      //     isVIP: callback ? 'true' : 'false'
      //   },
      //   timeout: 1000
      // })
    }
  }
}
</script>

<style scoped>
.userCenterBox {
  width: 400px;
  margin: 100px auto;
  border: 1px solid #dcdfe6;
  padding: 15px;
  border-radius: 5px;
  box-shadow: 0 0 30px #dcdfe6;
}
p {
  float: left;
  width: 120px;
  margin: 20px 10px;
}
.el-avatar {
  float: left;
  margin: 15px 20px;
}
.el-switch {
  margin-right: 10px;
}
</style>
