exports.id = "server";
exports.modules = {

/***/ "./src/components/Blocks/MainSlider/Edit.jsx":
/*!***************************************************!*\
  !*** ./src/components/Blocks/MainSlider/Edit.jsx ***!
  \***************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1__);
var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/components/Blocks/MainSlider/Edit.jsx";



const Edit = props => {
  return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1__["jsx"])("div", {
    children: "I'm the MainSlider edit component!"
  });
};

/* harmony default export */ __webpack_exports__["default"] = (MainsliderBlockEdit);

/***/ }),

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
  config.blocks.blocksConfog.testBlock.mainslider = {
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
//# sourceMappingURL=server.9c06a07d4516d2ce0542.hot-update.js.map