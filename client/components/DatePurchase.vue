<template>
    <cardSlot v-bind:item="item" style="height: 140px;">
        <template v-slot:date style="padding:0">
                <!-- {{item.name}} -->
                <div v-if="!edit"  style="overflow:scroll;max-height:45px">
                <h6 style="margin:0;font-weight:bold">{{item.name}}</h6>
                </div>
                <v-text-field
                  v-else
                  label="Item Name"
                  required
                  outlined
                  filled
                  dense
                  v-model="item.name"
                ></v-text-field>
                <v-btn
                    class="mx-2"
                    fab
                    x-small
                    color="error"
                    style="position:absolute;left:-20px;top:35%"
                    @click="editSet()"
                >
                    <v-icon dark>
                    mdi-wrench
                    </v-icon>
                </v-btn>                      
        </template>
        <template v-slot:total style="padding:0;font-size:15px">
                
                <template v-if="!edit">
                    <div style="padding:30px 0;overflow:scroll">
                        {{$options.filters.addComma(item.price)}} 円
                    </div>
                </template>
                
                <v-text-field
                  v-else
                  label="Price"
                  type="number"
                  outlined
                  filled
                  dense
                  v-model="item.price"
                ></v-text-field>
            </template>
        <template v-slot:content>
            <div class="memo" style="color:black" v-if="!edit">
                {{item.memo}}
            </div>
            <v-textarea
                v-else
                label="Memo"
                rows="3"
                row-height="25"
                v-model="item.memo"
                outlined
                filled
                style="padding-top: 15px;"
            ></v-textarea>

        </template>
        <template v-slot:right_area>
            <template v-if="!edit">
                <category-card v-for="category in item.categories" :category="category" :key="category.id" style="font-size:15px"></category-card>
            </template>

            <v-select
                v-else
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
                style="position:absolute;top:0px;right:-10px"
                @click="deleteItemRow(item.id)"
                v-if="edit"
            >
                <v-icon dark>
                mdi-close-thick
                </v-icon>
            </v-btn>            
        </template>
    </cardSlot>  
</template>

<script>
    import CategoryCard from '~/components/CategoryCard.vue'
    import cardSlot from '~/components/slot/CardSlot.vue'

    export default {
        components: {
            CategoryCard,
            cardSlot
        },
        data: () => ({
            edit: false,
            defaultItem:{}
        }),
        mounted:function(){
            this.defaultItem = {...this.item}
        },         
        methods: {
            async deleteItemRow(id){

                const config = {
                    headers: { 'content-type': 'application/json', }
                }
                const formData = new FormData()
                formData.append("id",id)
                try {
                    const response = await this.$axios.$delete('/item/' + id,config)
                    this.$emit("removeItem",id)
                    this.edit = false
                } catch (e) {
                    console.log(e)
                }
            },
            editSet(){
                //選択から表示に切り替える際初期値に戻す
                if(this.edit){
                    this.item.name = this.defaultItem.name
                    this.item.price = this.defaultItem.price
                    this.item.memo = this.defaultItem.memo
                    delete this.item.category_id;

                //表示から選択に切り替える際初期値を設定
                }else{
                    this.item.category_id = this.item.categories[0].id;
                }
                this.edit = !this.edit
            }
        },
        watch:{
            itemUpdate:function(newVal,old){
                console.log("item update row")
                console.log(newVal)
                if(newVal){
                    this.edit = false
                }
            }
        },
        props: ['item','allCategories','itemUpdate']
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
        height:100px;
        margin-top: 15px;
    }
    .v-textarea textarea {
line-height: 70px !important;
}

</style>