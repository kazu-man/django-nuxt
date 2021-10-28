import Vue from 'vue'

Vue.mixin({
    data () {
        return {
            validationRules: {
                required: value => !!value || '必須項目です',
                counter: value => value.length >= 8 || '8文字以上入力してください',
                email: value => {
                  const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                  return pattern.test(value) || '不正なe-mailアドレスです'
                },
                num: value => value > 0 || '0以上で入力してください',
            },
        }
      },

})