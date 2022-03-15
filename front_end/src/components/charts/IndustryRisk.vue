<template>
  <div>
    <div id="main" class="main_container"></div>
  </div>
</template>

<script>
export default {
  name: 'IndustryRisk'
}
</script>

<script src="echarts.js"></script>
<script src="theme/vintage.js"></script>
<script>
require("echarts/theme/vintage")
export default {
  data() {
    return {
      titleText: '行业风险'
    }
  },
  mounted() {
    this.initCharts()
  },
  methods: {
    initCharts() {
      var myChart = this.$echarts.init(document.getElementById("main"), "vintage")
      myChart.setOption({
        title: {
          text: this.titleText,
          textStyle: {
            color: "#333"
          },
          padding: 20
        },
        grid: {
          left: "5%",
          right: "7%",
          bottom: "9%",
          top: "20%",
          containLabel: true
        },
        xAxis: {
          data: [
            "2012-01-01",
            "2012-02-01",
            "2012-03-01",
            "2012-04-01",
            "2012-05-01"
          ]
        },
        yAxis: {},
        series: [
          {
            type: "bar",
            data: [
              1.2543,
              1.1868,
              1.1598,
              1.3567,
              1.4241,
              {
                value: 0.3,
                // 设置单个柱子的样式
                itemStyle: {
                  color: "#91cc75",
                  shadowColor: "#91cc75",
                  borderType: "dashed",
                  opacity: 0.5,
                }
              },
              2
            ],
            itemStyle: {
              barBorderRadius: 5,
              borderWidth: 1,
              borderType: "solid",
              borderColor: "#73c0de",
              shadowColor: "#5470c6",
              shadowBlur: 3
            }
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
  height: 450px;
  overflow: hidden;
}
</style>
