<template>

    <cardContainer>
            <template v-slot:top_area >

              <v-btn rounded small color="success" style="width:30px;margin:10px 10px 2px 10px" @click="backToMonth()">
                Back
              </v-btn>

            </template>
            <template v-slot:card_header>
                <cardTop v-bind:total="total" :itemsData="itemsData" :myTopChartStyles="myTopChartStyles">

                    <template v-slot:title>
                      {{$route.params.date}}
                      
                    </template>
                    <template v-slot:total >
                      計 {{$options.filters.addComma(total)}} 円

                      <addComponent @updateItems="updateItems" style="position:absolute;top:118px;left:-3px;"></addComponent>

                    </template>
                    <template v-slot:content>
                      
                        <chartTemp v-if="chartRerender && itemsData.length" :chartStyle="myTopChartStyles" :targetLabels="computedChartLabels" :data="computedChartData" :backgroundColor="computedChartBackGround"></chartTemp>
                        <div v-else style="width:100%"></div>
                        <v-btn rounded color="primary" @click="updateItems()" style="width:30px;margin:10px 10px 2px 10px;position:absolute;top:10px;right:10px;">
                          更新
                        </v-btn>

                    </template>

                </cardTop>
            </template>

            <template v-slot:card_body>
                        <!-- 各日 付ごとのコンポーネント -->
                <v-col v-for="item in items" :key="item.id" cols=12>
                    <date-purchase :item="item" :allCategories="allCategories" :itemUpdate="itemUpdate" @removeItem="removeItem"></date-purchase>
                </v-col>

            </template>

    </cardContainer>

</template>

<script>
const DatePurchase = () => import('~/components/DatePurchase.vue')
const cardTop = () => import('~/components/slot/CardTop.vue')
const chartTemp = () => import('~/components/ChartTemplate.vue')
const cardContainer = () => import('~/components/slot/CardContainer.vue')
const addComponent = () => import('~/components/addComponent.vue')

  export default {
      middleware: 'nuxtAuth',
      components: {
          DatePurchase,
          cardTop,
          chartTemp,
          cardContainer,
          addComponent
      },
        data () {
            return {
            items:[],
            total:0,
            itemsData:[],
            from:"",
            to:"",
            query:"",
            chartRerender:true,
            itemUpdate:false
            }
        },
        async asyncData ({ $axios, params }) {
            try {

              var dt = new Date(params.date); 

              let fromFormat = "yyyy-M-d 00:00:00"
              let toFormat = "yyyy-M-d 23:59:59"
              let targetMonth = "00" + (dt.getMonth() + 1)
              let targetDate = "00" + (dt.getDate())

              fromFormat = fromFormat.replace(/yyyy/g, dt.getFullYear());
              fromFormat = fromFormat.replace(/M/g, targetMonth.slice(-2));
              fromFormat = fromFormat.replace(/d/g, targetDate.slice(-2));

              dt.setMonth(dt.getMonth() + 1)
              dt.setDate(0)
              targetMonth = "00" + (dt.getMonth() + 1)
              toFormat = toFormat.replace(/yyyy/g, dt.getFullYear());
              toFormat  = toFormat.replace(/M/g, targetMonth.slice(-2));
              toFormat = toFormat.replace(/d/g, targetDate.slice(-2));
              const query = "?purchase_date_time_after=" + fromFormat + "&purchase_date_time_before=" + toFormat

              const items = await $axios.$get(`/item` + query)
              const total = await $axios.$get(`/total/` + params.date + '/')
              const from = fromFormat.split(" ")[0];
              const to = toFormat.split(" ")[0]
              const itemsData =  await $axios.$get(`/item_data/` + fromFormat.split(" ")[0] + '/' + toFormat.split(" ")[0] + `/`)
              const allCategories = await $axios.$get(`/category/`)
              

              return { items,total,itemsData,allCategories,from,to,query }
            } 
            catch (e) {
              console.log(e)
            return { items: [],total:100 }
            }
        },
        methods:{
          backToMonth(){
              const month = this.$route.params.date.split("-")
              this.$router.push('/items/calendar/month/' + month[0] + "-" + month[1])
          },
          async updateItems(){
            const config = {
                headers: { 'content-type': 'application/json', }
            }
            try {
                await this.$axios.$put('/itemList/', JSON.stringify(this.items), config)
                this.updateItemList();
            } catch (e) {
                console.log(e)
            }
          },
          async removeItem(id){
            this.items.forEach((item,index) => {
              
              if (item.id == id) {
                this.items.splice(index,1)
              }
            });

            this.updateItemList();
          },
          async updateItemList(){
              this.chartRerender = false
              this.itemUpdate = false

              try{
                  const itemsData = await this.$axios.$get(`/item_data/` + this.from + '/' + this.to + `/`)
                  const total = await this.$axios.$get(`/total/` + this.$route.params.date + '/')
                  const items = await this.$axios.$get(`/item` + this.query)
                  this.total = total
                  this.itemsData = itemsData
                  this.items = items
                  this.itemUpdate = true
              }catch(e){
                  console.log(e)

              }finally{
                  this.chartRerender = true
              }

          },
        },
    }
</script>
