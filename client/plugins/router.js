//router.js
export default(context) => {
    context.app.router.beforeEach((to, from, next)  => {
        const isLoggedIn = context.store.state.auth.loggedIn;
        if(isLoggedIn){

            console.log(`login中: ` + context.store.state.auth.user.username)
            console.log(context.store.state.auth.user)
        }
     next()
    })
  }