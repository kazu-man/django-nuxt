
export const state = () => ({
    // isSuperUser:false
});

export const mutations = {
    // setIsSuperUser(state, flg){
    //     state.isSuperUser = flg
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
    // isSuperUser (state) {
    //   return state.isSuperUser
    // }
  }