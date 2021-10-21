<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">
          {{ item.name }}
        </h2>
      </div>
      <div class="col-md-6 mb-4">
        <img src='/images/banner.jpg' class="img-fluid" style="width: 400px border-radius: 10px box-shadow: 0 1rem 1rem rgba(0,0,0,.7)">
      </div>
      <div class="col-md-4">
        <form @submit.prevent="submititem">
          <div class="form-group">
            <label for>商品名</label>
            <input v-model="item.name" type="text" class="form-control">
          </div>
          <div class="form-group">
            <label for>値段</label>
            <input v-model="item.price" type="text" class="form-control" name="Positions">
          </div>

          <div class="form-group">
            <label for>カテゴリー</label>
            <div v-for="category in categories" :key="category.id">
                <input type="checkbox" :value="category" v-model="item.categories">{{category.name}}
            </div>
          </div>


          <button type="submit" class="btn btn-success">
            更新
          </button>
        </form>
      </div>
    </div>
  </main>
</template>
<script>
export default {
  middleware: 'nuxtAuth',
  head () {
    return {
      title: '水草編集ページ'
    }
  },
  data () {
    return {
      item: {
        name: '',
        position: '',
        picture: '',
        difficulty: '',
        addition_amount: '',
        leaf_length: '',
        water_quality: ''
      },
      preview: '',
      categories:[]
    }
  },
  async asyncData ({ $axios, params }) {
    try {
      const item = await $axios.$get(`/item/${params.id}`)
      const categories = await $axios.$get(`/category`)
      return { item, categories }
    } catch (e) {
      return { item: [], categories:[] }
    }
  },
  methods: {
    // onFileChange (e) {
    //   const files = e.target.files || e.dataTransfer.files
    //   if (!files.length) {
    //     return
    //   }
    //   this.item.picture = files[0]
    //   this.createImage(files[0])
    // },
    // createImage (file) {
    //   const reader = new FileReader()
    //   const vm = this
    //   reader.onload = (e) => {
    //     vm.preview = e.target.result
    //   }
    //   reader.readAsDataURL(file)
    // },
    async submititem () {
      const editItem = this.item
      const config = {
        headers: { 'content-type': 'multipart/form-data' }
      }
      const formData = new FormData()
      for (const data in editItem) {

          if(data === "categories"){
        //     console.log(JSON.stringify(editItem[data]))
            formData.append(data, JSON.stringify(editItem[data]))
            // formData.append("data", JSON.stringify(editItem[data]))

          }else{
            formData.append(data, editItem[data])
          }
      }
        // formData.append("category_set", editItem["categories"])
        // formData.append("test", editItem["name"])

      try {
        console.log(this.item)
        // editItem["aaa"] = "hi"
        const response = await this.$axios.$patch(`/item/${editItem.id}/`, formData, config)
        this.$router.push('/items/')
        // console.log(response)
      } catch (e) {
        console.log(e)
      }
    }
  }
}
</script>

<style>
</style>