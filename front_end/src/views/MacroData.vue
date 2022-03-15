<template>
  <div class="macroDataBox">
    <el-divider content-position="center">
      <p><i class="el-icon-s-data"></i> 宏观数据</p>
    </el-divider>
    <div class="chartBox">
      <exchange-settlement-change-rate/>
    </div>
    <el-divider></el-divider>
    <div class="chartBox">
      <foreign-exchange-rate-fluctuation/>
    </div>
    <el-divider></el-divider>
    <div class="chartBox">
      <g-d-p-change-rate/>
    </div>
    <el-divider></el-divider>
    <div class="chartBox">
      <import-and-export-change-rate/>
    </div>
    <el-divider></el-divider>
    <div class="chartBox">
      <total-sales-change-rate/>
    </div>
    <el-divider></el-divider>
  </div>
</template>

<script>
import GDPChangeRate from '../components/charts/macro/GDPChangeRate.vue'
import ExchangeSettlementChangeRate from '../components/charts/macro/ExchangeSettlementChangeRate.vue'
import ForeignExchangeRateFluctuation from '../components/charts/macro/ForeignExchangeRateFluctuation.vue'
import ImportAndExportChangeRate from '../components/charts/macro/ImportAndExportChangeRate.vue'
import TotalSalesChangeRate from '../components/charts/macro/TotalSalesChangeRate.vue'
export default {
  name: 'MacroData',
  components: {
    GDPChangeRate,
    ExchangeSettlementChangeRate,
    ForeignExchangeRateFluctuation,
    ImportAndExportChangeRate,
    TotalSalesChangeRate
  }
}
</script>

<style scoped>
.macroDataBox {
  margin: 0px auto;
  width: 1200px;
}
.chartBox {
  width: 1200px;
}
.el-divider {
  margin-top: 50px;
  margin-bottom: 60px;
  background-color: #969696;
}
.el-divider p {
  font-size: 25px;
}
</style>
