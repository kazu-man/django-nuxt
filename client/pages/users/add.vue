<template>
  <main class="container my-5">
    <div class="row">

    <cardContainer class="col-8">
            <template v-slot:top_area >

              <v-btn rounded small color="success" @click="toLogin()" style="width:30px;margin:10px 10px 2px 10px">
                Back
              </v-btn>

            </template>

            <template v-slot:card_body>

                <div class="col-md-12">
                  <v-form @submit.prevent="submitUser" ref="form" lazy-validation>
                    <div class="form-group">
                      <v-text-field
                        v-model="userInfo.username"
                        label="User Name"
                        :rules="[validationRules.required]"
                        required
                        ></v-text-field>                   
                    </div>
                    <div class="form-group">
                      <v-text-field
                        v-model="userInfo.email"
                        label="Email"
                        :rules="[validationRules.required,validationRules.email]"
                        required
                      ></v-text-field>  
                      </div>
                    <div class="form-group">
                      <v-text-field
                        v-model="userInfo.password"
                        label="Password"
                        :rules="[validationRules.required,validationRules.counter_8]"
                        :type="'password'"
                        required
                      ></v-text-field>
                    </div>
                    <div class="form-group">
                      <v-text-field
                        v-model="userInfo.confirm_password"
                        label="Password confirmation"
                        :rules="[validationRules.required,validationRules.counter_8,passwordConfirmationRule]"
                        :type="'password'"
                        required
                      ></v-text-field>                                        
                    </div>
                    <div style="text-align:center">
                      <button type="submit" class="btn btn-primary" style="color:white">
                        登録
                      </button>
                    </div>
                  </v-form>

                </div>

            </template>

    </cardContainer>
    </div>
  </main>
</template>
<script>
import CategoryCard from '~/components/CategoryCard.vue'
const cardContainer = () => import('~/components/slot/CardContainer.vue')

export default {
    components: {
        CategoryCard,
        cardContainer,
    },
  head () {
    return {
      title: 'User'
    }
  },
  data () {
    return {
      userInfo: {
          username:"",
          email:"",
          password:"",
          confirm_password:""
      },
      preview: '',
    }
  },
  methods: {
    async submitUser () {
      //formの入力値が正常な場合
      if(!this.$refs.form.validate()){
          return false;
      }
        
      const config = {
        headers: { 'content-type': 'multipart/form-data', }
      }
      const formData = new FormData()
      for (const data in this.userInfo) {
          formData.append(data, this.userInfo[data])
      }
      try {
        const response = await this.$axios.$post('/userList/', formData, config)
        
        this.$router.push('/items/')
      } catch (e) {
        //エラーがあればアラートを表示
        let message = "";
         Object.keys(e.response.data).map(value => {
            message += e.response.data[value] + "\n"
        });
        alert(message)
      }
    },
    toLogin() {
        this.$router.push("/login/")
    }
  },
    computed: {
        passwordConfirmationRule() {
            return  (this.userInfo.password === this.userInfo.confirm_password) || 'パスワードが一致していません'
        },
    }


}
</script>
<style scoped>
</style>