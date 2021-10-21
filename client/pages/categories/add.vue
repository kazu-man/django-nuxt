<template>
  <main class="container my-5">
    <div class="row">

      <!-- <div class="col-md-6 mb-4">
        <img
          v-if="preview"
          :src="preview"
          class="img-fluid"
          style="width: 400px border-radius: 10px box-shadow: 0 1rem 1rem rgba(0,0,0,.7)"
          alt
        >
        <img
          v-else
          src="@/static/images/banner.jpg"
          class="img-fluid"
          style="width: 400px border-radius: 10px box-shadow: 0 1rem 1rem rgba(0,0,0,.7)"
        >
      </div> -->


    <cardContainer class="col-8">
            <template v-slot:top_area >

              <v-btn rounded small color="success" style="width:30px;margin:10px 10px 2px 10px">
                Back
              </v-btn>

            </template>
            <template v-slot:card_header :allCategories="allCategories">

                  <div style="width:100%;padding:30px">
                      <category-card :category="category" v-for="category in allCategories" :key="category.id" style="margin:3px"></category-card>
                  </div>

            </template>

            <template v-slot:card_body>

                <div class="col-md-12">
                  <form @submit.prevent="submitCategory">
                    <div class="form-group">
                      <label for>カテゴリー名</label>
                      <input v-model="category.name" type="text" class="form-control">
                    </div>
                    <div class="form-group">
                      <label for>カラー</label>
                      <input v-model="category.color" type="text" class="form-control">
                    </div>
                    <div style="text-align:center">
                      <button type="submit" class="btn btn-primary" style="color:white">
                        登録
                      </button>
                    </div>
                  </form>

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
    components: {
        CategoryCard,
        cardContainer,
    },
  head () {
    return {
      title: '水草追加'
    }
  },
  data () {
    return {
      category: {},
      allCategories:{},
      preview: ''
    }
  },
  methods: {
    async submitCategory () {
      const config = {
        headers: { 'content-type': 'multipart/form-data', }
      }
      const formData = new FormData()
      for (const data in this.category) {
          formData.append(data, this.category[data])
      }
      try {
        const response = await this.$axios.$post('/category/', formData, config)
        
        this.$router.push('/items/')
      } catch (e) {
        debugger
        console.log(e)
      }
    }
  },
  async asyncData ({ $axios, params }) {
    try {
      const allCategories = await $axios.$get(`/test/`)
      return { allCategories }
    } catch (e) {
      return { allCategories: [] }
    }
  }
}
</script>
<style scoped>
</style>