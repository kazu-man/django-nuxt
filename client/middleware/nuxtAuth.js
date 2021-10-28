export default function (context) {
    // 認証されていないユーザーの場合、リダイレクト
    const isLoggedIn = context.store.state.auth.loggedIn;
    if (!isLoggedIn) {
      console.log("loginしてないのでダメ！")
      context.redirect('/login')
    }
  }