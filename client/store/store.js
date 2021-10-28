
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

        await this.$auth.loginWith('local', {
            data: {
                username: usercredentials.username,
                password: usercredentials.password
            }
        })
        .then(response => {
            console.log("LOGIN SUCCESS!!")
            // $nuxt.$router.push('/items')

        })
        .catch(e => {
            let message = "";
            Object.keys(e.response.data).map(value => {
               message += e.response.data[value] + "\n"
           });
           alert(message)
            console.log("LOGIN ERROR!!")

        })
    },

}


export const getters = {
    // accessToken (state) {
    //   return state.accessToken
    // }
  }