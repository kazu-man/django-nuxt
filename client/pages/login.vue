<template>
    <cardContainer style="margin:5% 15%">
        <template v-slot:card_body>
          <div style="width:50%">
              <img src='/images/banner.jpg' class="img-fluid" style="width: 400px border-radius: 10px box-shadow: 0 1rem 1rem rgba(0,0,0,.7)">
          </div>

          <form @submit.prevent="login" style="width:50%; padding:5%;">
            <h3 style="text-align:center">Login</h3>
            <div class="form-group">
              <label for>UserName</label>
              <input v-model="loginForm.username" type="text" class="form-control">
            </div>
            <div class="form-group">
              <label for>Password</label>
              <input v-model="loginForm.password" type="password" class="form-control">
            </div>
            <v-btn type="submit" color="primary" rounded style="display:block;margin:auto;">
              登録
            </v-btn>
          </form>

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
        data () {
            return {
            loginForm: {username:"",password:""},
            auth:""
            }
        },
        methods: {
            async login () { // eslint-disable-line
            try {
                this.$store.dispatch('store/userLogin',{
                  username:this.loginForm.username,
                  password:this.loginForm.password
                })
                this.$router.push('/items')
                console.log("LOGIN DONE!!!")

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
            }
        },
    }
</script>
