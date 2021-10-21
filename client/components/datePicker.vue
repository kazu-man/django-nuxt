<template>
            <v-menu
          ref="menu"
          v-model="menu"
          :close-on-content-click="false"
          transition="scale-transition"
          offset-y
          max-width="290px"
          min-width="auto"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="dateFormatted"
              label="Date"
              persistent-hint
              prepend-icon="mdi-calendar"
              v-bind="attrs"
              @blur="date = parseDate(dateFormatted)"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="date"
            no-title
            @input="menu = false"
          ></v-date-picker>
        </v-menu>
</template>


<script>
  export default {
        data: vm => ({
            date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
            dateFormatted: vm.formatDate((new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10)),
            menu: false,
        }),
    computed: {
      computedDateFormatted () {
        return this.formatDate(this.date)
      },
    },
    mounted:function(){
        this.$emit('input', this.date)
    },
    model: {
        prop: 'parentModel', //　親モデルの値を'parentModel'というkeyで受け取る
        event: 'input' // イベント種別
    },
    props: {
        parentModel: String // 親モデルの値が入ってくるので、型を指定してあげる
    },
    watch: {
      date (val) {
        this.dateFormatted = this.formatDate(this.date)
        this.$emit('input', this.date)

      },
    },


    methods: {
      formatDate (date) {
        if (!date) return null

        const [year, month, day] = date.split('-')
        return `${year}/${month}/${day}`
      },
      parseDate (date) {
        if (!date) return null

        const [year, month, day] = date.split('/')
        return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
      },
    },
  }
</script>