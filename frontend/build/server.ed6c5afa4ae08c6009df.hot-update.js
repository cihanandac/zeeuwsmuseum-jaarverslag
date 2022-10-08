exports.id = "server";
exports.modules = {

/***/ "./node_modules/@plone/volto/src/icons/slider.svg":
/*!********************************************************!*\
  !*** ./node_modules/@plone/volto/src/icons/slider.svg ***!
  \********************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = {"attributes":{"xmlns":"http://www.w3.org/2000/svg","width":"36","height":"36","viewBox":"0 0 36 36"},"content":"<g fill-rule=\"evenodd\"><path d=\"M7,28.4 L29,28.4 L29,7.6 L7,7.6 L7,28.4 Z M5,31 L31,31 L31,5 L5,5 L5,31 Z\"/><path d=\"M15.012 13.037L18.781 19.633 21.917 16.497 25.219 20.625 26.781 19.375 22.083 13.503 19.219 16.367 14.988 8.963 9.126 19.515 10.874 20.485zM19.5 25C19.5 25.828 18.828 26.5 18 26.5 17.172 26.5 16.5 25.828 16.5 25 16.5 24.172 17.172 23.5 18 23.5 18.828 23.5 19.5 24.172 19.5 25L19.5 25zM23.5 25C23.5 25.828 22.828 26.5 22 26.5 21.172 26.5 20.5 25.828 20.5 25 20.5 24.172 21.172 23.5 22 23.5 22.828 23.5 23.5 24.172 23.5 25L23.5 25zM15.5 25C15.5 25.828 14.828 26.5 14 26.5 13.172 26.5 12.5 25.828 12.5 25 12.5 24.172 13.172 23.5 14 23.5 14.828 23.5 15.5 24.172 15.5 25L15.5 25z\"/></g>"}

/***/ }),

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

/* harmony default export */ __webpack_exports__["default"] = (Edit);

/***/ }),

/***/ "./src/components/Blocks/MainSlider/Wiew.jsx":
/*!***************************************************!*\
  !*** ./src/components/Blocks/MainSlider/Wiew.jsx ***!
  \***************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1__);
var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/components/Blocks/MainSlider/Wiew.jsx";



const View = props => {
  return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1__["jsx"])("div", {
    children: "I'm the MainSlider view component!"
  });
};

/* harmony default export */ __webpack_exports__["default"] = (View);

/***/ }),

/***/ "./src/components/index.js":
/*!*********************************!*\
  !*** ./src/components/index.js ***!
  \*********************************/
/*! exports provided: MainsliderBlockEdit, MainsliderBlockView */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _Blocks_MainSlider_Wiew__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./Blocks/MainSlider/Wiew */ "./src/components/Blocks/MainSlider/Wiew.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "MainsliderBlockView", function() { return _Blocks_MainSlider_Wiew__WEBPACK_IMPORTED_MODULE_0__["default"]; });

/* harmony import */ var _Blocks_MainSlider_Edit__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./Blocks/MainSlider/Edit */ "./src/components/Blocks/MainSlider/Edit.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "MainsliderBlockEdit", function() { return _Blocks_MainSlider_Edit__WEBPACK_IMPORTED_MODULE_1__["default"]; });

/**
 * Add your components here.
 * @module components
 * @example
 * import Footer from './Footer/Footer';
 *
 * export {
 *   Footer,
 * };
 */




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
/* harmony import */ var _package_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @package/components */ "./src/components/index.js");
/* harmony import */ var _plone_volto_icons_slider_svg__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @plone/volto/icons/slider.svg */ "./node_modules/@plone/volto/src/icons/slider.svg");
/* harmony import */ var _plone_volto_icons_slider_svg__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_slider_svg__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _plone_volto_config__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @plone/volto/config */ "./node_modules/@plone/volto/src/config/index.js");
!(function webpackMissingModule() { var e = new Error("Cannot find module 'defineMessages'"); e.code = 'MODULE_NOT_FOUND'; throw e; }());
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
//# sourceMappingURL=server.ed6c5afa4ae08c6009df.hot-update.js.map