<template>
  <div class="card item-card">
    <img :src="item.picture" class="card-img-top">
    <div class="card-body">
      <h5 class="card-title">
        {{ item.name }}
      </h5>
      <p class="card-text">
        <strong>値段:</strong> {{ item.price }}
      </p>
      <div class="action-buttons">
        <nuxt-link :to="`/items/${item.id}/`" class="btn btn-sm btn-success">
          詳細
        </nuxt-link>
        <nuxt-link :to="`/items/${item.id}/edit/`" class="btn btn-sm btn-primary">
          編集
        </nuxt-link>
        <button @click="onDelete(item.id)" class="btn btn-sm btn-danger">
          削除
        </button>
      </div>
      
      <div v-for="category in item.categories" :key="category.id">
          <category-card :onDelete="deleteCategory" :category="category"></category-card>
      </div>

    </div>
  </div>
</template>

<script>
    import CategoryCard from '~/components/CategoryCard.vue'

    export default {
        components: {
            CategoryCard,
        },
        methods: {
            async deleteCategory (category_id) { // eslint-disable-line
            try {
                await this.$axios.$delete(`/category/${category_id}/`) // eslint-disable-line
                const newCategory = await this.$axios.$get('/category/')
                // this.category = newCategory
                this.item.categories = newCategory
            } catch (e) {
                console.log(e)
            }
            }
        },
        props: ['item', 'onDelete']
    }
</script>

<style>
    .item-card {
        box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
    }
</style>