export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  mode: 'universal',
  head: {
    title: 'client',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '~/assets/css/transitions.css' // 追加
  ],

  auth: {
    redirect: {
      login: '/login',
      logout: '/login',
      home: false
      // callback: '/items',
    },
    strategies: {
      local: {
        scheme: 'refresh',
        token: {
          property: 'access',
          maxAge: 1,
          global: true,
          type: 'Bearer'
        },
        refreshToken: {
          property: 'refresh',
          data: 'refresh',
          global: true,
          maxAge: 60 * 60 * 24 * 30
        },
        user: {
         property: false,
         autoFetch: true
        },
        endpoints: {
          login: { url: '/auth/jwt/create/', method: 'post' , propertyName: 'access'},
          refresh: { url: '/auth/jwt/refresh/', method: 'post'},
          user: { url: '/auth/users/me/', method: 'get', propertyName: false },
          logout: false
        },
        // autoLogout: false
      }
    }
  },

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    { src: '~/plugins/axios.js', ssr: true },
    { src: '~/plugins/router.js' },
    { src: '~/plugins/filter.js' },
    { src: '@/plugins/mixin-common-methods' },
    { src: '@/plugins/validationRules' },

    // { src: '~/plugins/localStorage.js', ssr: false }

  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    '@nuxtjs/vuetify',
  ],
  
  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/bootstrap
    'bootstrap-vue/nuxt',
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    // '@nuxtjs/auth',
    '@nuxtjs/auth-next'
    // '@/plugins/date_fns'
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    baseURL: "http://localhost:8000/api" // 追加
  },

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'en'
    }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {

    extend (config, ctx) {
    }
  },
}
