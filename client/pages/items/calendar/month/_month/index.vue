<template>
    <cardContainer>
        <template v-slot:top_area >

            <v-btn rounded small color="success" style="width:100px;margin:10px 10px 2px 10px" @click="monthBefore()">
            Last Month
            </v-btn>
            <v-btn rounded small color="success" style="width:100px;margin:10px 10px 2px 10px" @click="monthAfter()">
            Next Month
            </v-btn>

        </template>
        <template v-slot:card_header>
            <cardTop v-bind:total="total" v-bind:totalData="totalData">

                <template v-slot:title>{{$route.params.month}}</template>
                <template v-slot:total >計 {{$options.filters.addComma(total)}} 円</template>
                <template v-slot:content>
                    
                    <chartTemp v-if="chartRerender && totalData.categories" :chartStyle="myTopChartStyles" :targetLabels="extractLabels(totalData.categories)" :data="extractChartData(totalData.categories)" :backgroundColor="extractChartBackGround(totalData.categories)"></chartTemp>
                    <div v-else style="width:100%"></div>
                        
                    <addComponent @updateItems="updateItems" :datePickFlg="true" style="width:30px;margin:10px 10px 2px 10px;position:absolute;top:10px;right:10px;"></addComponent>

                </template>

            </cardTop>
        </template>

        <template v-slot:card_body>

            <v-col
            v-for="(item, i) in itemsData"
            :key="i"
            cols="12"
            >
                <cardSlot v-bind:item="item">

                    <template v-slot:date>{{item.purchase_date}}</template>
                    <template v-slot:total class="text-h5" >計 {{$options.filters.addComma(item.total)}} 円</template>
                    <template v-slot:content>
                        <div style="margin-bottom:20px">
                        <chartTemp :targetLabels="extractLabels(item.categories)" :data="extractChartData(item.categories)" :backgroundColor="extractChartBackGround(item.categories)"></chartTemp>
                        </div>
                    </template>
                    <template v-slot:right_area>
                            <div>
                                <div class="">
                                    <v-btn
                                        class="my-2"
                                        color="primary"
                                        rounded
                                        small
                                        @click="toDetail(item.purchase_date)"
                                    >
                                    Detail
                                    </v-btn>
                                </div>
                            </div>
                    </template>
                </cardSlot>        
            </v-col>
        </template>

    </cardContainer>

</template>

<script>
const DatePurchase  = () =>  import('~/components/DatePurchase.vue')
const chart  = () =>  import('~/components/chart.vue')
const chartTemp  = () =>  import('~/components/ChartTemplate.vue')
const cardTop  = () =>  import('~/components/slot/CardTop.vue')
const cardSlot  = () =>  import('~/components/slot/CardSlot.vue')
const cardContainer  = () =>  import('~/components/slot/CardContainer.vue')

  export default {
      middleware: 'nuxtAuth', 
      components: {
          DatePurchase,
          chart,
          chartTemp,
          cardTop,
          cardSlot,
          cardContainer

      },
      head () {
        return {
          title: 'Account'
        }
      },      
        data () {
            return {
                total:0,
                totalData:[],
                itemsData:[],
                to:"",
                from:"",
                chartRerender:true
            }
        },
        async asyncData ({ $axios, params }) {
            try {
                //月で表示するとき
                
              var dt = new Date(params.month); 

              let fromFormat = "yyyy-M-01"
              let toFormat = "yyyy-M-d"
              let targetMonth = "00" + (dt.getMonth() + 1)
              fromFormat = fromFormat.replace(/yyyy/g, dt.getFullYear());
              fromFormat = fromFormat.replace(/M/g, targetMonth.slice(-2));

              dt.setMonth(dt.getMonth() + 1)
              dt.setDate(0)
              targetMonth = "00" + (dt.getMonth() + 1)
              toFormat = toFormat.replace(/yyyy/g, dt.getFullYear());
              toFormat  = toFormat.replace(/M/g, targetMonth.slice(-2));
              toFormat = toFormat.replace(/d/g, (dt.getDate()));
              
              const to = toFormat
              const from = fromFormat
              const itemsData =  await $axios.$get(`/item_data/` + fromFormat + '/' + toFormat + `/`)
              const totalMonthData = await $axios.$get(`/total_month/` + fromFormat + '/' + toFormat + `/`)
              const total  = totalMonthData.total
              const totalData = totalMonthData.totalPriceDate
              return { total,itemsData,totalData, to, from}
            } 
            catch (e) {
              console.log(e)
            }
        },
        methods:{
            toDetail(date){
                this.$router.push('/items/calendar/date/' + date)
            },
            monthAfter(){
              var dt = new Date(this.$route.params.month); 
              dt.setMonth(dt.getMonth() + 1)
              const month = this.getMonthString(dt)
              
              this.$router.push("/items/calendar/month/" + month)
            },
            monthBefore(){
              var dt = new Date(this.$route.params.month); 
              dt.setMonth(dt.getMonth() - 1)
              const month = this.getMonthString(dt)
              
              this.$router.push("/items/calendar/month/" + month)

            },
            async updateItems(){
              this.chartRerender = false
              this.itemsData = []
                try{
                    const totalMonthData = await this.$axios.$get(`/total_month/` + this.from + '/' + this.to + `/`)
                    const total  = totalMonthData.total
                    const totalData = totalMonthData.totalPriceDate
                    const itemsData =  await this.$axios.$get(`/item_data/` + this.from + '/' + this.to + `/`)
      
                    this.totalMonthData = totalMonthData
                    this.total = total
                    this.totalData = totalData
                    this.itemsData = itemsData

                }catch(e){
                    console.log(e)
                }finally{
                    this.chartRerender = true
                }


            }
        },
    }
</script>
