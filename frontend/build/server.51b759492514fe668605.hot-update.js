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
/* harmony import */ var _plone_volto_icons_slider_svg__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @plone/volto/icons/slider.svg */ "./node_modules/@plone/volto/src/icons/slider.svg");
/* harmony import */ var _plone_volto_icons_slider_svg__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_slider_svg__WEBPACK_IMPORTED_MODULE_1__);
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


defineMessages({
  mainslider: {
    id: 'Main Slider',
    defaultMessage: 'Main Slider'
  }
});
function applyConfig(config) {
  // Add here your project's configuration here by modifying `config` accordingly
  config.blocks.blocksConfig.mainslider = {
    id: 'mainslider',
    title: 'Main Slider',
    icon: _plone_volto_icons_slider_svg__WEBPACK_IMPORTED_MODULE_1___default.a,
    group: 'common',
    view: _package_components__WEBPACK_IMPORTED_MODULE_0__["MainsliderBlockView"],
    edit: _package_components__WEBPACK_IMPORTED_MODULE_0__["MainsliderBlockEdit"],
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
//# sourceMappingURL=server.51b759492514fe668605.hot-update.js.map