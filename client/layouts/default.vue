<template>
    <v-app>
      <Header></Header>
      <div style="margin-top:60px"></div>
      <nuxt/>
    </v-app>
</template>

<script>
import Header from '@/components/Header.vue'

export default {
  components:{
    Header
  }
}
</script>

<style>
</style>