
export const state = () => ({
    // loginUser:null
});

export const mutations = {
    // setLoginUser(state, user){
    //     state.loginUser = user
    // },

}

export const actions = {
    async userLogin(context, usercredentials){

        this.$auth.loginWith('local', {
            data: {
                username: usercredentials.username,
                password: usercredentials.password
            }
        })
        .then(response => {
            console.log("LOGIN SUCCESS!!")
            // $nuxt.$router.push('/items')

        })
        .catch(response => {
            console.log(response)
            console.log("LOGIN ERROR!!")

        })
    },

}


export const getters = {
    // accessToken (state) {
    //   return state.accessToken
    // }
  }