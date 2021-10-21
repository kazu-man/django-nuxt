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
        <v-card-title>
          <span class="text-h5">Add Item</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row v-for="(item, index) in itemAddForm" :key="index">
              <v-col
                cols="12"
                sm="4"
                md="4"
              >
                <v-text-field
                  label="Item Name"
                  required
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
                  hint="example of helper text only on focus"
                  type="number"
                  v-model="item.price"
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
                ></v-select>
            <v-btn
                class="mx-2"
                icon
                dark
                small
                color="error"
                style="position:absolute;top:30px;right:-30px"
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
          <small>*indicates required field</small>
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
        <v-card-actions>
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
            @click="addItems()"
          >
            Save
          </v-btn>
        </v-card-actions>
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
      allCategories:[]
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
    methods:{
        addItemRow(){
            this.itemAddForm.push({name:"",price:0,purchase_date:this.$route.params.date == undefined ? "" : this.$route.params.date ,category_id:null,memo:""})
        },
        deleteItemRow(index){
            this.itemAddForm.splice(index,1)
        },
        dialogClose(){
            this.itemAddForm = [{name:"",price:0,purchase_date:this.$route.params.date == undefined ? "" : this.$route.params.date ,category_id:null,memo:""}]
            this.dialog = false

        },
        selectedDate(val){
            this.itemAddForm[0].purchase_date = val
        },
        async addItems(){
            const config = {
                headers: { 'content-type': 'application/json', }
            }
            try {
                const response = await this.$axios.$post('/item/', JSON.stringify(this.itemAddForm), config)
                this.$emit("updateItems")
                this.dialogClose()

            } catch (e) {
                console.log(e)
            }
        }
    },

    }
</script>