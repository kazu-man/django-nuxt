<template>

    <div class="category-card badge" v-bind:class="{pointer : isDetailAllowed}" v-bind:style="{ background: category.color }" style="color:white;display:inline-block" @click="toCategoryDetail()">
        {{ category.name }}
    </div>

</template>

<script>
    export default {
        props: ['category', 'onDelete','allowToDetail'],
        methods:{
            toCategoryDetail(){
                if(this.isDetailAllowed){
                    this.$router.push("/categories/" + this.category.id + "/edit")
                }
            }
        },
        computed:{
            isDetailAllowed(){
                return this.allowToDetail != undefined && this.allowToDetail
            }
        }
    }
</script>

<style>
    .category-card {
        box-shadow: 0 0.2rem 0.3rem rgba(0,0,0,.6);
    }
    .pointer{
        cursor:pointer
    }
</style>