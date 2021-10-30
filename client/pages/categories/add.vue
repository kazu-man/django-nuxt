<template>
  <main class="container my-5">
    <div class="row">

    <cardContainer class="col-8">
            <template v-slot:top_area >

              <v-btn rounded small color="success" @click="goToAccountPage" style="width:30px;margin:10px 10px 2px 10px">
                Back
              </v-btn>

            </template>
            <template v-slot:card_header :allCategories="allCategories">

                  <div style="width:100%;padding:30px">
                      <category-card :category="category" :allowToDetail="true" v-for="category in allCategories" :key="category.id" style="margin:3px"></category-card>
                  </div>

            </template>

            <template v-slot:card_body>

                <div class="col-md-12">
                  <v-form @submit.prevent="submitCategory" ref="form" lazy-validation>
                    <div class="form-group" style="height:82px">
                      <v-text-field
                       v-if="showInput"
                        v-model="category.name"
                        label="カテゴリー名"
                        :rules="[validationRules.required]"
                        required
                        ></v-text-field>                   
                    </div>
                    <div class="form-group"  style="height:82px">
                      <v-text-field
                       v-if="showInput"
                        v-model="category.color"
                        label="カラー"
                        :rules="[validationRules.required]"
                        required
                      ></v-text-field>                      
                    </div>
                    <div style="text-align:center">
                      <button type="submit" class="btn btn-primary" style="color:white">
                        登録
                      </button>
                    </div>
                  </v-form>

                </div>

            </template>

    </cardContainer>
    </div>
  </main>
</template>
<script>
import CategoryCard from '~/components/CategoryCard.vue'
const cardContainer = () => import('~/components/slot/CardContainer.vue')

export default {
    middleware: 'nuxtAdminAuth',
    components: {
        CategoryCard,
        cardContainer,
    },
  head () {
    return {
      title: 'Category'
    }
  },
  data () {
    return {
      category: {},
      allCategories:{},
      preview: '',
      showInput:true
    }
  },
  methods: {
    async submitCategory () {
      //formの入力値が正常な場合
      if(!this.$refs.form.validate()){
          return false;
      }

      const config = {
        headers: { 'content-type': 'multipart/form-data', }
      }
      const formData = new FormData()
      for (const data in this.category) {
          formData.append(data, this.category[data])
      }
      try {
        const response = await this.$axios.$post('/category/', formData, config)
        this.showInput = false
        this.category = {}
        this.allCategories = await this.$axios.$get(`/category/`)
      } catch (e) {
        //エラーがあればアラートを表示
        let message = "";
         Object.keys(e.response.data).map(value => {
           message += e.response.data[value] + "\n"
        });
        alert(message)
        console.log(e.response.data)
      } finally{
        this.showInput = true
      }
    },
  },
  async asyncData ({ $axios, params }) {    
    try {
      const allCategories = await $axios.$get(`/category/`)
      return { allCategories }
    } catch (e) {
      return { allCategories: [] }
    }
  }
}
</script>
<style scoped>
</style>