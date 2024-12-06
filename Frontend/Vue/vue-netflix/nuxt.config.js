// nuxt.config.js/ts
export default defineNuxtConfig({
    modules: ['@bootstrap-vue-next/nuxt'],
    bootstrapVueNext: {
      composables: true, // Will include all composables
      // composables: {useBreadcrumb: true, useColorMode: true, all: false}, // Will include only useBreadcrumb & useColorMode
      // composables: {useBreadcrumb: false, useColorMode: false, all: true} // Will include everything except useBreadcrumb & useColorMode
      directives: {all: true}, // Will include all directives
      css: true, // Will include the module's CSS. If set to false, you can add the CSS manually in the 'css' property below
    },
    css: [
      // 'bootstrap/dist/css/bootstrap.min.css' // Not necessary if `css: true`
    ],
  })