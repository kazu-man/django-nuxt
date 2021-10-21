<template>
    <chart :style="myStyles" :chartdata="chartdata" :options="options" ></chart>
</template>

<script>
import chart from '~/components/chart.vue'

  export default {
      components: {
          chart
      },
        data () {
            return {
                chartdata: {
                    datacollection: {
                        //   labels: ['January', 'February','January', 'February'], //グラフの上に表示する場合
                        targetLabels: ['January', 'February','January', 'February', 'March', 'May'],
                        datasets: [
                            {
                                label: 'Data One',
                                backgroundColor: ['#FF6384','#36A2EB','#FF6384','#36A2EB','#FF6384','#36A2EB'],
                                data: [40, 20,40, 20]
                                
                            },
                        ]
                    
                    }
                },
                options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                        datalabels: {   
                            display: true,
                            anchor: 'center',
                            align: 'center',
                            formatter: function(value, context) {
                                return context.chart.data.targetLabels[context.dataIndex];
                            },
                            labels: {
                                title: {
                                    color: 'lightgray'
                                }
                            }
                        }
                    },
                    tooltips: {
                        bodyFontSize: 15,
                        callbacks: {
                            label: function(tooltipItem, data) {
                                
                                let total = 0 // 合計格納
                                let amount = data.datasets[0].data[tooltipItem.index] // マウスを当てたデータ
                                let itemName = "";
                                // 全データの合計算出
                                data.datasets[0].data.forEach(item => {
                                    total += parseInt(item)
                                });
                                //ツールチップに表示する名前取得
                                data.targetLabels.forEach((el,index) => {
                                    if(index == tooltipItem.index){
                                        itemName = el;
                                    }
                                });

                                return itemName + ":" + amount + "円 (" + Math.round(amount / total * 100) + '%)';
                            }
                        }
                    }
                }
                }
        },
        beforeMount:function(){
            this.chartdata.datacollection.targetLabels = this.targetLabels;
            this.chartdata.datacollection.datasets[0].backgroundColor = this.backgroundColor;
            this.chartdata.datacollection.datasets[0].data = this.data;
        },
        computed: {
            myStyles () {
                if(this.chartStyle != null && this.chartStyle != undefined){
                    return this.chartStyle
                }
                return {
                    height: `120px`,
                    position: 'relative'
                }
            },
        },
        watch:{
            targetLabels: function (val, oldVal) {
                this.chartdata.datacollection.targetLabels = val;
            },
            backgroundColor:function (val, oldVal) {

                this.chartdata.datacollection.datasets[0].backgroundColor = val;
            },
            data: function (val, oldVal) {

                this.chartdata.datacollection.datasets[0].data = val;
            },
        },
        props: ['targetLabels','backgroundColor','data', 'chartStyle']
    }
</script>

<style>
    .item-card {
        box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
    }
    .container {
      max-width:800px;
    }
</style>