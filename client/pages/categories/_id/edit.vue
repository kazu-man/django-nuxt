<template>
  <main class="container my-5">
    <div class="row">

    <cardContainer class="col-8">
            <template v-slot:top_area >

              <v-btn rounded small color="success" @click="goToCategory" style="width:30px;margin:10px 10px 2px 10px">
                Back
              </v-btn>

            </template>

            <template v-slot:card_body>

                <div class="col-md-12">
                  <v-form @submit.prevent="submitCategory" ref="form" lazy-validation>
                    <div class="form-group">
                      <v-text-field
                        v-model="targetCategory.name"
                        label="カテゴリー名"
                        :rules="[validationRules.required]"
                        required
                        ></v-text-field>                   
                    </div>
                    <div class="form-group">
                      <v-text-field
                        v-model="targetCategory.color"
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
    middleware: 'nuxtAuth',
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
      targetCategory:{},
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
      for (const data in this.targetCategory) {
          formData.append(data, this.targetCategory[data])
      }
      try {
        const response = await this.$axios.$patch(`/category/${this.targetCategory.id}/`, formData, config)
        
        this.$router.push('/categories/add')
      } catch (e) {
        //エラーがあればアラートを表示
        let message = "";
         Object.keys(e.response.data).map(value => {
            message += e.response.data[value] + "\n"
        });
        alert(message)
        console.log(e.response.data)
      }
    },
  },
  async asyncData ({ $axios, params }) {    
    try {
      const targetCategory = await $axios.$get(`/category/${params.id}`)
      return { targetCategory }
    } catch (e) {
      return { targetCategory: [] }
    }
  }
}
</script>
<style scoped>
</style>