exports.id = "server";
exports.modules = {

/***/ "./src/components/Blocks/MainSlider/Edit.jsx":
false,

/***/ "./src/components/Blocks/MainSlider/Wiew.jsx":
false,

/***/ "./src/components/index.js":
false,

/***/ "./src/config.js":
/*!***********************!*\
  !*** ./src/config.js ***!
  \***********************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "default", function() { return applyConfig; });
!(function webpackMissingModule() { var e = new Error("Cannot find module '@paccomponents'"); e.code = 'MODULE_NOT_FOUND'; throw e; }());
/* harmony import */ var _plone_volto_config__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @plone/volto/config */ "./node_modules/@plone/volto/src/config/index.js");
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
  config.blocks.blocksConfig.mainslider = {
    id: 'mainslider',
    title: 'Main Slider',
    icon: sliderSVG,
    group: 'common',
    view: !(function webpackMissingModule() { var e = new Error("Cannot find module '@paccomponents'"); e.code = 'MODULE_NOT_FOUND'; throw e; }()),
    edit: !(function webpackMissingModule() { var e = new Error("Cannot find module '@paccomponents'"); e.code = 'MODULE_NOT_FOUND'; throw e; }()),
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
//# sourceMappingURL=server.ad1956b82c9dd10bcffc.hot-update.js.map