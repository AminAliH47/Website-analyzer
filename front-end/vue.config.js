const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  pwa: {
    name: 'Website Analyzer',
    themeColor: '#5C7F67',
    msTileColor: '#5C7F67',
    appleMobileWebAppCapable: 'yes',
    appleMobileWebAppStatusBarStyle: 'black',

    // configure the workbox plugin
    // workboxPluginMode: 'InjectManifest',
    // workboxOptions: {
    //   // swSrc is required in InjectManifest mode.
    //   swSrc: 'dev/sw.js',
    //   // ...other Workbox options...
    // },
    icons: {
      faviconSVG: './public/img/icons/logo.svg',
      favicon32: 'img/icons/logo-32.png',
      favicon16: 'img/icons/logo-16.png',
      appleTouchIcon: 'img/icons/apple-touch-152.png',
      maskIcon: 'img/icons/safari.svg',
      msTileImage: 'img/icons/msapplication-144.png'
    }
  }
})