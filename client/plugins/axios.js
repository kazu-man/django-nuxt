// import store from '~/store.js'

import { state } from "~/store/store"

export default function ({$axios, $auth, store, $router}) {
    // const {$axios} = context
    
    //request前の共通処理
    // $axios.interceptors.request.use((config) => {
    //     const token = 'Bearer ' + store.getters['store/accessToken'];
    //     console.log(token)
    //     config.headers.Authorization = token  // todo: ここでトークンを付与する
    //     return config
    //   })


    //request後の共通処理
  //   $axios.interceptors.response.use((response) => {

  //     return response

  //   }, async function (error) {

  //     return error

  // })
}