<template>
  <div class="card item-card">
    <div class="card-body row">

        <div class="card-text col-4">
            <h5 class="card-title">{{item.name}}</h5>
            <p style="margin-bottom:1px">値段: {{ item.price }} 円</p>
            <p style="margin-bottom:1px"><small>購入日: {{ item.purchase_date }}</small></p>
        </div>

        <div class="col-4 memo">
            {{item.memo}}
        </div>
        
        <div class="price col-4">
            <template v-for="category in item.categories">
                <category-card :category="category" :key="category.id"></category-card>
            </template>
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

        },
        props: ['item']
    }
</script>

<style scoped>
    .item-card {
        box-shadow: 0 0.3rem 0.5rem rgba(0,0,0,.6);
        position:relative;
        margin-bottom:5px;
    }
    .price {
        /* position:absolute;
        top:5%;
        right:5%; */
        float:right;
        height:100px;
    }

    .memo {
        border:lightgray solid 1px;
        border-radius:5px;
        background:lightcyan;
    }

</style>