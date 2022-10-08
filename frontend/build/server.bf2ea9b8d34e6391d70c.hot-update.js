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

/* harmony default export */ __webpack_exports__["default"] = (MainsliderBlockView);

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
/* harmony import */ var components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! components */ "./src/components/index.js");
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
  return config;
}

/***/ })

};
//# sourceMappingURL=server.bf2ea9b8d34e6391d70c.hot-update.js.map