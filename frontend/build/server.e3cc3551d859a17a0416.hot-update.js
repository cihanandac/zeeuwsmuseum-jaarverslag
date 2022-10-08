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
!(function webpackMissingModule() { var e = new Error("Cannot find module '@package/components/Blocks/MainSlider/View'"); e.code = 'MODULE_NOT_FOUND'; throw e; }());
/* harmony import */ var _package_components_Blocks_MainSlider_Edit__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @package/components/Blocks/MainSlider/Edit */ "./src/components/Blocks/MainSlider/Edit.jsx");
/* harmony import */ var _plone_volto_config__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @plone/volto/config */ "./node_modules/@plone/volto/src/config/index.js");
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

 // All your imports required for the config here BEFORE this line


function applyConfig(config) {
  // Add here your project's configuration here by modifying `config` accordingly
  config.blocks.blocksConfog.mainslider = {
    id: 'mainslider',
    title: 'Main Slider',
    icon: sliderSVG,
    group: 'common',
    view: !(function webpackMissingModule() { var e = new Error("Cannot find module '@package/components/Blocks/MainSlider/View'"); e.code = 'MODULE_NOT_FOUND'; throw e; }()),
    edit: _package_components_Blocks_MainSlider_Edit__WEBPACK_IMPORTED_MODULE_1__["default"],
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
//# sourceMappingURL=server.e3cc3551d859a17a0416.hot-update.js.map