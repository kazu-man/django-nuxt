<template>

    <div class="category-card badge" v-bind:style="{ background: category.color }" style="color:white;display:inline-block">
        {{ category.name }}
    </div>

</template>

<script>
    export default {
        props: ['category', 'onDelete']
    }
</script>

<style>
    .category-card {
        box-shadow: 0 0.2rem 0.3rem rgba(0,0,0,.6);
    }
</style>