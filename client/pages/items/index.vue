<template>
  <main class="container mt-5">
    <div class="row">
      <div class="col-12 text-right mb-4">
        <div class="d-flex justify-content-between">
          <h3>育てた水草一覧</h3>
          <h4>{{total}}</h4>
          <nuxt-link to="/items/add" class="btn btn-info">
            水草を追加する
          </nuxt-link>
        </div>
      </div>
      <template v-for="item in items">
        <div :key="item.id" class="col-lg-3">
          <item-card :onDelete="deleteItem" :item="item"></item-card>
        </div>
      </template>
    </div>
  </main>
</template>
<script>
import ItemCard from '~/components/ItemCard.vue'

export default {
  head () {
    return {
      title: '水草一覧'
    }
  },
  components: {
    ItemCard
  },
  data () {
    return {
      items: [],
      total: 0
    }
  },
  async asyncData ({ $axios, params }) {
    try {
      const items = await $axios.$get(`/item/`)
      // const total = await $axios.$get(`/total/hey?a=b&c=d`)
      return { items }
    } 
    catch (e) {
      return { items: [],total:0 }
    }
  },
  methods: {
    async deleteItem (item_id) { // eslint-disable-line
      try {

        //練習
        const formData = new FormData()
        formData.append("date", "2021/09/19")
        const config = {
          headers: { 'content-type': 'multipart/form-data',}
        }
        const total = await this.$axios.$post(`/total/test/`,formData,config)
        this.total = total

        await this.$axios.$delete(`/item/${item_id}/`) // eslint-disable-line
        const newItems = await this.$axios.$get('/item/')
        this.items = newItems
      } catch (e) {
        console.log(e)
      }
    }
  }
}
</script>
<style scoped>
</style>