<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      persistent
      max-width="600px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
            class="mx-2"
            fab
            dark
            small
            color="error"
            v-bind="attrs"
            v-on="on"

        >
            <v-icon dark>
            mdi-plus
            </v-icon>
        </v-btn>
      </template>
      <v-card>
        <v-form @submit.prevent="addItems" ref="form" lazy-validation>
        <v-card-title>
          <span class="text-h5">Add Item</span>
        </v-card-title>
        <v-card-text>
          <v-container v-if="dialog">
            <v-row v-for="(item, index) in itemAddForm" :key="index">
              <v-col
                cols="12"
                sm="4"
                md="4"
              >
                <v-text-field
                  label="Item Name"
                  required
                  :rules="[validationRules.required]"
                  v-model="item.name"
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="4"
                md="4"
              >
                <v-text-field
                  label="Price"
                  type="number"
                  v-model="item.price"
                  :rules="[validationRules.counter_0]"
                  required
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="4"
                md="4"
              >
                <v-select
                    label="Category"
                    :items="allCategories"
                    item-text="name"
                    item-value="id"
                    v-model="item.category_id"
                    :rules="[validationRules.required]"
                    required
                ></v-select>
            <v-btn
                v-if="lastRowFlg"
                class="mx-2"
                icon
                dark
                small
                color="error"
                style="position:absolute;top:30px;right:-25px"
                @click="deleteItemRow(index)"
            >
                <v-icon dark>
                mdi-close-thick
                </v-icon>
            </v-btn>
              </v-col>

              <v-col cols="12" v-if="datePickFlg != null">
                <v-row justify="center">
                    <date-picker v-model="item.purchase_date"></date-picker>
                </v-row>
              </v-col>

              <v-col
                cols="12"
              >
                <v-textarea
                  label="Memo"
                  outlined
                  rows="2"
                  row-height="25"
                  v-model="item.memo"
                ></v-textarea>
              </v-col>              
            </v-row>
          </v-container>
            <v-btn
                class="mx-2"
                fab
                dark
                small
                color="error"
                style="position:absolute;bottom:70px;right:-3px;"
                @click="addItemRow()"
            >
            <v-icon dark>
            mdi-plus
            </v-icon>
        </v-btn>
        </v-card-text>
        <v-card-actions style="display:block;text-align:center">
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="dialogClose()"
          >
            Close
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            type="submit"
          >
            Save
          </v-btn>
        </v-card-actions>
        </v-form>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
const datePicker = () => import('~/components/datePicker.vue')

  export default {
      components:{
          datePicker
      },
    data: () => ({
      dialog: false,
      itemAddForm:[{name:"",price:0,purchase_date:"",category_id:null,memo:""}],
      allCategories:[],


    }),
    mounted:async function(){
        if(this.$route.params.date != null){
            this.itemAddForm[0].purchase_date = this.$route.params.date
        }

        try {
            const categories = await this.$axios.$get(`/category/`)
            this.allCategories = categories
        } catch (e) {
            console.log(e)
        }
    },
    props:["datePickFlg"],
    computed:{
        lastRowFlg:function(){
            return this.itemAddForm.length >= 2 ? true : false;
        }
    },
    methods:{
        addItemRow(){
            this.itemAddForm.push({name:"",price:0,purchase_date:this.$route.params.date == undefined ? "" : this.$route.params.date ,category_id:null,memo:""})
        },
        deleteItemRow(index){
            this.itemAddForm.splice(index,1)
        },
        dialogClose(){
            this.dialog = false
            this.itemAddForm = [{name:"",price:0,purchase_date:this.$route.params.date == undefined ? "" : this.$route.params.date ,category_id:null,memo:""}]

        },
        selectedDate(val){
            this.itemAddForm[0].purchase_date = val
        },
        async addItems(){

            //formの入力値が正常な場合
            if(!this.$refs.form.validate()){
                return false;
            }
            const config = {
                headers: { 'content-type': 'application/json', }
            }
            try {
                const response = await this.$axios.$post('/item/', JSON.stringify(this.itemAddForm), config)
                this.$emit("updateItems")
                this.dialogClose()

            } catch (e) {

                //エラーがあればアラートを表示
                let message = "";
                Object.keys(e.response.data).map(value => {
                    message += e.response.data[value] + "\n"
                });
                alert(message)
                
                console.log(e.response.data)
            }
        }
    },

    }
</script>