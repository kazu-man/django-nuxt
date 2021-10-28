<template>
    <cardContainer style="margin:5% 15%">
        <template v-slot:card_body>
          <div style="width:50%">
              <img src='/images/banner.jpg' class="img-fluid" style="width: 400px border-radius: 10px box-shadow: 0 1rem 1rem rgba(0,0,0,.7)">
          </div>

          <v-form @submit.prevent="login" style="width:50%; padding:5%;" ref="form" lazy-validation >
            <h3 style="text-align:center">Login</h3>
            <div class="form-group">
              <v-text-field
                v-model="loginForm.username"
                label="User Name"
                :rules="[validationRules.required]"
                ></v-text-field>                
            </div>
            <div class="form-group">
              <v-text-field
                v-model="loginForm.password"
                label="Password"
                :type="'password'"
                :rules="[validationRules.required]"
              ></v-text-field>                 
            </div>
            <v-btn type="submit" color="primary" rounded style="display:block;margin:auto;">
              ログイン
            </v-btn>
            <div style="text-align:center;margin-top:15px;color:blue">
              <p @click="toSignin()" style="cursor:pointer" small>
                登録する
              </p>
            </div>
          </v-form>

          <!-- <form @submit.prevent="logout">
            <button type="submit" class="btn btn-primary">
              ログアウト
            </button>
          </form> -->
        </template>
    </cardContainer>

</template>

<script>
const cardContainer = () => import('~/components/slot/CardContainer.vue')

    export default {
      components:{
        cardContainer
      },
      head () {
        return {
          title: 'Login'
        }
      },      
        data () {
            return {
            loginForm: {username:"",password:""},
            auth:""
            }
        },
        methods: {
            async login () { // eslint-disable-line
              //formの入力値が正常な場合
              if(!this.$refs.form.validate()){
                  return false;
              }
            
            try {
                await this.$store.dispatch('store/userLogin',{
                  username:this.loginForm.username,
                  password:this.loginForm.password
                })

                if(this.$store.state.auth.loggedIn){
                  
                  this.goToAccountPage()

                }

            } catch (e) {
                console.log(e)
            }
            },
            async logout () { 
              try {
                  await this.$auth.logout()
                  .then(response => {
                    console.log("LOGOUT DONE!!!")
                  })        
              } catch (e) {
                  console.log(e)
              }
            },
            toSignin() {
              this.$router.push("/users/add/")
            }
        },
    }
</script>
