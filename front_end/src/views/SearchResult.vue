<template>
  <div class="searchResultBox">
    <search-result-head/>
    <el-container>
      <el-menu
        :default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
        background-color="#303133"
        text-color="#fff"
        active-text-color="#ffd04b">
        <el-menu-item index="/company-information">企业信息</el-menu-item>
        <el-menu-item index="/industry-risk">行业风险情况</el-menu-item>
        <el-submenu index="/company-risk-assessment">
          <template slot="title">企业风险评估</template>
          <el-menu-item index="/exchange-rate-risk">汇率风险</el-menu-item>
          <el-menu-item index="/stock-volatility">股票波动率</el-menu-item>
          <el-menu-item index="/financial-leverage">财务杠杆情况</el-menu-item>
        </el-submenu>
        <el-submenu index="user" style="float: right; margin-right: 10px;">
          <template slot="title">
            <i class="el-icon-s-custom" style="margin-right: 15px"></i>
            <span style="color: white;">{{ this.$store.getters.getUser.name }}</span>
          </template>
          <el-menu-item index="/user-center">
            <div style="text-align: center;">用户中心</div>
          </el-menu-item>
          <el-menu-item index="/logout">
            <div style="text-align: center;">退出登录</div>
          </el-menu-item>
        </el-submenu>
      </el-menu>
    </el-container>
    <div id="graph-box">
      <router-view/>
    </div>
    <div class="footer"></div>
  </div>
</template>

<script>
import SearchResultHead from '../components/SearchResultHead.vue'
export default {
  name: 'SearchResult',
  components: {
    SearchResultHead
  },
  data () {
    return {
      activeIndex: '/company-information'
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      switch (key) {
        case '/company-information':
        case '/industry-risk':
        case '/user-center':
        case '/logout':
          this.$router.push(key); break
        case '/exchange-rate-risk':
        case '/stock-volatility':
        case '/financial-leverage':
          if (this.$store.getters.getUser.isVIP === 'true') {
            this.$router.push(key)
          } else {
            this.$message({
              message: '您正在访问会员资源, 请前往用户中心开通会员',
              type: 'warning',
              duration: 4000,
              showClose: true
            })
          } break
        default: console.log(key, keyPath)
      }
    }
  }
}
</script>

<style>
.searchResultBox .el-container {
  border-top: 1px solid #000;
}
.searchResultBox .el-menu {
  width: 100%;
  border-bottom: 1px solid #000;
}
.searchResultBox .el-page-header {
  line-height: 60px;
  padding-left: 10px;
  background-color: #303133;
  color: #fff;
}
.searchResultBox #graph-box {
  padding: 40px 40px;
  height: 450px;
  background-color: #303030;
  border-bottom: 2px solid #000;
}
.searchResultBox .el-menu-item {
  border-radius: 50px;
  min-width: 100px;
  letter-spacing: 2px;
}
.searchResultBox .el-submenu__title {
  border-radius: 50px;
  letter-spacing: 2px;
}
.searchResultBox .footer {
  height: 90px;
  background-color: #303133;
}
</style>
