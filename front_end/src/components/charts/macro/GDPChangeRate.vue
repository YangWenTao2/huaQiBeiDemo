<template>
  <div class="main">
    <div id="3" class="main_container"></div>
  </div>
</template>

<script src="echarts.js"></script>
<script src="theme/dark-bold.js"></script>
<script>
require('echarts/theme/dark-bold')
export default {
  name: 'GDPChangeRate',
  data () {
    return {
      titleText: 'GDP变动率'
    }
  },
  mounted () {
    this.initCharts()
  },
  methods: {
    initCharts () {
      var myChart = this.$echarts.init(document.getElementById("3"), 'dark-bold')
      myChart.setOption({
        title: {
          text: this.titleText,
          padding: 20
        },
        grid: {
          left: '5%',
          right: '7%',
          bottom: '9%',
          top: '20%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          data: ['2019/2/1', '2019/3/1', '2019/4/1','2019/5/1','2019/6/1']
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            data: [-5.7, -5.7, 3.6, 3.6, 3.6, 1.3],
            type: 'line'
          }
        ]
      })
    }
  }
}
</script>

<style scoped>
.main_container {
  width: 100%;
  height: 400px;
  overflow: hidden;
  margin-bottom: 80px;
}
.main {
  margin: 30px;
}
</style>
