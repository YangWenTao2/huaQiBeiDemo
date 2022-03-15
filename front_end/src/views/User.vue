<template>
  <el-container class="searchBox">
    <el-header>
      <div class="yesClientele">
        <i>Yes, clientele</i>
      </div>
      <div class="welcome canClick" @click="toLogout">退出登录</div>
      <el-divider class="welcome d1" direction="vertical"></el-divider>
      <div class="welcome canClick" @click="toUserCenter">用户中心</div>
      <el-divider class="welcome d2" direction="vertical"></el-divider>
      <div class="welcome">
        Welcome, {{ this.$store.getters.getUser.name }}
      </div>
    </el-header>
    <el-main>
      <div  style="text-align: center;">
        <img src="../assets/YesClientele.jpg" width="200px" height="130px">
      </div>
      <el-col :span="8" class="center">
        <el-input
          placeholder="请输入公司名称"
          v-model="input"
          clearable>
          <el-button
            slot="append"
            icon="el-icon-search"
            id="search"
            @click="handleSearch">
          </el-button>
        </el-input>
      </el-col>
      <el-col class="popular" style="margin-right: 50px;">
        <el-divider content-position="center">
          <p><i class="el-icon-s-data"></i> 热门搜索</p>
        </el-divider>
        <el-table class="mytable"
          ref="singleTable"
          :data="tableData"
          highlight-current-row
          style="width: 70%">
          <el-table-column
            type="index"
            width="50">
          </el-table-column>
          <el-table-column
            property="company_name"
            label="公司名称"
            width="120">
          </el-table-column>
          <el-table-column
            property="address"
            label="地址"
            width="120">
          </el-table-column>
          <el-table-column
            property="contact"
            label="联系方式"
            width="120">
          </el-table-column>
        </el-table>
      </el-col>
      <el-col class="carousel">
        <el-divider content-position="center">
          <p><i class="el-icon-s-data"></i> 宏观数据</p>
        </el-divider>
        <el-carousel :interval="4000" type="card" height="200px">
          <el-carousel-item v-for="(item, index) in carouselImages" :key="index">
            <h4 class="small">{{ item.title }}</h4>
            <img :src="item.url" width="455px" height="150px">
          </el-carousel-item>
        </el-carousel>
        <el-divider content-position="center">
          <el-button type="warning" plain @click="toMacroData">查看详情</el-button>
        </el-divider>
      </el-col>
    </el-main>
    <el-footer>
    </el-footer>
  </el-container>
</template>

<script>
export default {
  name: 'User',
  components: {
  },
  data () {
    return {
      currentRow: null,
      input: '',
      debug: 'fdsd',
      tableData: [
        {
          company_name: 'Apple Inc.',
          address: 'Califonia',
          contact: 'xxxxxxxxxx'
        },
        {
          company_name: 'Microsoft',
          address: 'Seattle',
          contact: 'xxxxxxxxxx'
        },
        {
          company_name: '腾讯',
          address: '深圳',
          contact: 'xxxxxxxxxx'
        },
        {
          company_name: '阿里巴巴',
          address: '杭州',
          contact: 'xxxxxxxxxx'
        }
      ],
      carouselImages: [
        {
          url: require('../assets/1.png'),
          title: '结售汇变动率'
        },
        {
          url: require('../assets/2.png'),
          title: '外汇汇率波动率'
        },
        {
          url: require('../assets/3.png'),
          title: 'GDP变动率'
        },
        {
          url: require('../assets/4.png'),
          title: '进出口变动率'
        },
        {
          url: require('../assets/5.png'),
          title: '社会销售品零售总额变动率'
        }
      ]
    }
  },
  methods: {
    setCurrent (row) {
      this.$refs.singleTable.setCurrentRow(row)
    },
    handleSearch () {
      // 测试与后端通讯时请将第144行注释掉
      this.$router.push('/search-result')
      // this.axios({
      //   method: 'post',
      //   url: '/search',
      //   headers: { 'content-type': 'application/x-www-form-urlencoded' },
      //   data: {
      //     searchInput: this.input
      //   }.then(response => {
      //     this.$store.dispatch(
      //       'asyncUpdateCompanyData',
      //       {
      //         name: response.data.companyName,
      //         number: response.data.companyStockNumber,
      //         beta: response.data.betaValues,
      //         leverage: response.data.financialLeverage
      //       }
      //     )
      //     this.$router.push('/search-result')
      //   }).catch(error => {
      //     this.$message({
      //       message: '连接服务器失败',
      //       type: 'error'
      //     })
      //     console.log(error)
      //   })
      // })
    },
    toMacroData () {
      this.$router.push('/macro-data')
    },
    toLogout () {
      this.$router.push('/logout')
    },
    toUserCenter () {
      this.$router.push('/user-center')
    }
  }
}
</script>

<style>
.searchBox .el-header {
  background-color: #303133;
  line-height: 60px;
}
.searchBox .el-footer {
  background-color: #303133;
  line-height: 60px;
}
.searchBox .center {
  margin-top: 15px;
  margin-left: 300px;
}
.searchBox .mytable {
  margin-top: 50px;
  margin-left: 250px;
}
.searchBox #search {
  background-color: #303133;
  border-radius: 0%;
}
.searchBox .el-main {
  margin-left: 250px;
  margin-right: 250px;
  box-shadow: 0 8px 20px #303133, 0 0 6px rgba(0, 0, 0, .14);
  overflow: hidden;
}
.searchBox .center .el-button {
  color: #ffd04b;
  background-color: #303133;
}
.searchBox .yesClientele {
  float: left;
  margin-left: 20px;
  color: #ffbb00;
  font-size: 25px;
  font-family: fantasy;
}
.searchBox .welcome {
  color: #ffd04b;
  float: right;
  height: 30px;
  margin-right: 20px;
  font-weight: 600;
  font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}
.searchBox .canClick {
  font-weight: 500;
  margin-right: 10px;
}
.searchBox .canClick:hover {
  cursor: pointer;
  color: #ffbb00;
}
.searchBox .el-divider {
  margin-top: 15px;
  background-color: #7c7c7c;
}
.searchBox .el-divider.d2 {
  width: 1.5px;
}
.searchBox .el-input__inner:focus {
  border: 2px solid #ffd04b;
}
.searchBox .carousel {
  margin-top: 50px;
  text-align: center;
}
.searchBox .carousel p {
  letter-spacing: 2px;
  font-weight: 600px;
  font-size: 20px;
}
.searchBox .el-carousel {
  margin: 40px auto;
}
.searchBox .el-carousel__item h4 {
  line-height: 5px;
  opacity: 0.75;
  color: #303133;
}
.searchBox .popular {
  margin: 40px auto;
}
.searchBox .popular p {
  letter-spacing: 2px;
  font-weight: 600px;
  font-size: 20px;
}
.searchBox .el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}
.searchBox .el-carousel__item:nth-child(2n+1) {
  background-color: #d3dce6;
}
</style>
