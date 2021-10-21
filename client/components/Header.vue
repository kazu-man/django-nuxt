<template>
    <div>
        <v-app-bar
            dark
            color="pink"
            clipped
            style="z-index:99;height:64px"
            >
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

            <v-toolbar-title>My Sample Project</v-toolbar-title>

        </v-app-bar>
        <v-navigation-drawer app v-model="drawer" clipped style="margin-top:64px;position:absolute">

        <v-list>
            <v-list-item v-if="!isLoggedIn" @click="login()">
              <v-list-item-action>
                <v-icon>mdi-label</v-icon>
              </v-list-item-action>

              <v-list-item-content>
                <v-list-item-title>Login</v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-list-item v-else @click="logout()">
              <v-list-item-action>
                <v-icon>mdi-label</v-icon>
              </v-list-item-action>

              <v-list-item-content>
                <v-list-item-title>Logout</v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-list-item @click="goToAccount()">
              <v-list-item-action>
                <v-icon>mdi-label</v-icon>
              </v-list-item-action>

              <v-list-item-content>
                <v-list-item-title>Account</v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-list-item @click="goToCategories()">
              <v-list-item-action>
                <v-icon>mdi-label</v-icon>
              </v-list-item-action>

              <v-list-item-content>
                <v-list-item-title>Categories</v-list-item-title>
              </v-list-item-content>
            </v-list-item>

        </v-list>


        </v-navigation-drawer>
    </div>
</template>

<script>

    export default {
        data () {
            return {
            drawer:false,
            }
        },
        computed:{
            isLoggedIn(){
                return this.$store.state.auth.loggedIn;
            }
        },
        methods: {
            async login () { 
                this.$router.push('/login')
            },
            async logout () { 
              try {
                  await this.$auth.logout()
              } catch (e) {
                  console.log(e)
              }
            },
            goToAccount(){
              var dt = new Date(); 
              const month = this.getMonthString(dt)
              
              this.$router.push("/items/calendar/month/" + month)
            },
            goToCategories(){
              this.$router.push("/categories/add/")
            }
        },
    }
</script>
