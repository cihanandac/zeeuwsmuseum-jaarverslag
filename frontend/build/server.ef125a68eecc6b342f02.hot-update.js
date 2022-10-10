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
/* harmony import */ var _package_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @package/components */ "./src/components/index.js");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react-intl */ "react-intl");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react_intl__WEBPACK_IMPORTED_MODULE_1__);
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

 // defineMessages({
//   mainslider: {
//     id: 'Main Slider',
//     defaultMessage: 'Main Slider',
//   },
// });

function applyConfig(config) {
  config.blocks.blocksConfig.mainslider = {
    id: 'mainslider',
    title: 'Main Slider',
    // icon: sliderSVG,
    group: 'common',
    view: _package_components__WEBPACK_IMPORTED_MODULE_0__["MainSliderViewBlock"],
    edit: _package_components__WEBPACK_IMPORTED_MODULE_0__["MainSliderEditBlock"],
    restricted: false,
    mostUsed: true,
    security: {
      addPermission: [],
      view: []
    }
  }; // Add here your project's configuration here by modifying `config` accordingly

  return config;
}

/***/ })

};
//# sourceMappingURL=server.ef125a68eecc6b342f02.hot-update.js.map