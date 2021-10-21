<script>
import { Pie } from 'vue-chartjs'
import chartjsPluginDatalabels from 'chartjs-plugin-datalabels'

export default {
  extends: Pie,
  props: {
      chartdata: {
          type: Object,
      default: null
    },
    options: {
        type: Object,
      default: null
    },
  },
    mounted () {
        this.addPlugin(chartjsPluginDatalabels)
        this.renderChart(this.chartdata['datacollection'], this.options)
    
        },
}
</script>