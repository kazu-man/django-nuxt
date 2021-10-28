import Vue from 'vue'

Vue.mixin({
  methods: {
    goToAccountPage(){
        var dt = new Date(); 
        const month = this.getMonthString(dt)
    
        this.$router.push("/items/calendar/month/" + month)
    },
    goToCategory(){
        this.$router.push('/categories/add')
    },    
    truncate(str, length) {
      return str.length <= length ? str: (str.substr(0, length) + "...");
    },
    extractLabels :function(categories){
        let result = [];
        
        categories.forEach(function(v,k){
            result.push(v.name);
        })
        return result;
    },
    extractChartData :function(categories){
        let result = [];
                        

        categories.forEach(function(v,k){
            result.push(v.price);
        })
        return result;
    },
    extractChartBackGround :function(categories){
        let result = [];
                        

        categories.forEach(function(v,k){
            result.push(v.color);
        })
        return result;
    },
    getMonthString(dt){
        let month = "yyyy-M"
        let targetMonth = "00" + (dt.getMonth() + 1)
        month = month.replace(/yyyy/g, dt.getFullYear());
        month = month.replace(/M/g, targetMonth.slice(-2));
        
        return month
    },


  },
  computed: {
    myStyles () {
        return {
            height: `120px`,
            position: 'relative'
        }
    },
    myTopChartStyles () {
        return {
            height: `150px`,
            position: 'relative'
        }
    },

    computedChartLabels(){
        return this.extractLabels(this.itemsData[0].categories);
    },
    computedChartData(){
        return this.extractChartData(this.itemsData[0].categories);
    },
    computedChartBackGround(){
        return this.extractChartBackGround(this.itemsData[0].categories);
    },
},

})