exports.id = "server";
exports.modules = {

/***/ "./src/config.js":
/*!***********************!*\
  !*** ./src/config.js ***!
  \***********************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "default", function() { return applyConfig; });
/* harmony import */ var _plone_volto_config__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @plone/volto/config */ "./node_modules/@plone/volto/src/config/index.js");
/**
 * Add your config changes here.
 * @module config
 * @example
 * export default function applyConfig(config) {
 *   config.settings = {
 *     ...config.settings,
 *     port: 4300,
 *     listBlockTypes: {
 *       ...config.settings.listBlockTypes,
 *       'my-list-item',
 *    }
 * }
 */
// import MainsliderBlockView from '@package/components/Blocks/MainSlider/View';
// import MainsliderBlockEdit from '@package/components/Blocks/MainSlider/Edit';
// All your imports required for the config here BEFORE this line

function applyConfig(config) {
  // Add here your project's configuration here by modifying `config` accordingly
  config.blocks.blocksConfog.testBlock.mainslider = {
    id: 'mainslider',
    title: 'Main Slider',
    icon: sliderSVG,
    group: 'common',
    view: MainsliderBlockView,
    edit: MainsliderBlockEdit,
    restricted: false,
    mostUsed: true,
    security: {
      addPermission: [],
      view: []
    }
  };
  return config;
}

/***/ })

};
//# sourceMappingURL=server.0bcd980753340094d979.hot-update.js.map