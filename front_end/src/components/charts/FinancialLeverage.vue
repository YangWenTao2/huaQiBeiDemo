<template>
  <div>
    <div id="main" class="main_container"></div>
  </div>
</template>

<script>
export default {
  name: 'FinancialLeverage'
}
</script>

<script src="echarts.js"></script>
<script src="theme/vintage.js"></script>
<script>
require("echarts/theme/vintage")
export default {
  data() {
    return {
      titleText: '财务杠杆情况'
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
            "2011-03-31",
            "2011-06-30",
            "2011-09-30",
            "2011-12-31",
            "2013-03-31"
          ]
        },
        yAxis: {},
        series: [
          {
            type: "bar",
            data: [
              1.027,
              1.1038,
              1.1918,
              1.1737,
              1.0428,
              {
                value: 0.25,
                // 设置单个柱子的样式
                itemStyle: {
                  color: "#91cc75",
                  shadowColor: "#91cc75",
                  borderType: "dashed",
                  opacity: 0.5
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
