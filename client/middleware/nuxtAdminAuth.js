export default function (context) {
    // 認証されていないユーザーの場合、リダイレクト
    const isLoggedIn = context.store.state.auth.loggedIn;
    const isSuperUser = context.store.state.auth.user.is_superuser;
    if (!isLoggedIn || !isSuperUser) {
      console.log("adminのみ閲覧可能")
      context.redirect('/login')
    }
  }