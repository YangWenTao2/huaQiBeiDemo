<template>
  <div class="main">
    <div id="4" class="main_container"></div>
  </div>
</template>

<script src="echarts.js"></script>
<script src="theme/dark-bold.js"></script>
<script>
require('echarts/theme/dark-bold')
export default {
  name: 'ImportAndExportChangeRate',
  data () {
    return {
      titleText: '进出口变动率'
    }
  },
  mounted () {
    this.initCharts()
  },
  methods: {
    initCharts () {
      var myChart = this.$echarts.init(
        document.getElementById("4"),
        'dark-bold'
      )
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
          data: ['2019/2/1', '2019/3/1', '2019/4/1','2019/5/1','2019/6/1']
        },
        yAxis: {},
        series: [
          {
            data: [10, 22, 28, 43, 49],
            type: 'line',
            stack: 'x',
            areaStyle: {}
          },
          {
            data: [5, 4, 3, 5, 10],
            type: 'line',
            stack: 'x',
            areaStyle: {}
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
