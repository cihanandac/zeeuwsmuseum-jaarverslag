exports.id = "server";
exports.modules = {

/***/ "./src/components/Blocks/Mainslider/Edit.jsx":
/*!***************************************************!*\
  !*** ./src/components/Blocks/Mainslider/Edit.jsx ***!
  \***************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/defineProperty */ "@babel/runtime/helpers/defineProperty");
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _View__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./View */ "./src/components/Blocks/Mainslider/View.jsx");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__);

var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/components/Blocks/Mainslider/Edit.jsx";

function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); if (enumerableOnly) { symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; }); } keys.push.apply(keys, symbols); } return keys; }

function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i] != null ? arguments[i] : {}; if (i % 2) { ownKeys(Object(source), true).forEach(function (key) { _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(target, key, source[key]); }); } else if (Object.getOwnPropertyDescriptors) { Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)); } else { ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } } return target; }





const Edit = props => {
  return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsx"])(_View__WEBPACK_IMPORTED_MODULE_2__["default"], _objectSpread({}, props));
};

/* harmony default export */ __webpack_exports__["default"] = (Edit);

/***/ }),

/***/ "./src/components/Blocks/Mainslider/View.jsx":
/*!***************************************************!*\
  !*** ./src/components/Blocks/Mainslider/View.jsx ***!
  \***************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/defineProperty */ "@babel/runtime/helpers/defineProperty");
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_slick__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react-slick */ "react-slick");
/* harmony import */ var react_slick__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react_slick__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _slide1_jpeg__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./slide1.jpeg */ "./src/components/Blocks/Mainslider/slide1.jpeg");
/* harmony import */ var _slide1_jpeg__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_slide1_jpeg__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _slide2_jpeg__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./slide2.jpeg */ "./src/components/Blocks/Mainslider/slide2.jpeg");
/* harmony import */ var _slide2_jpeg__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_slide2_jpeg__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _slide3_jpg__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./slide3.jpg */ "./src/components/Blocks/Mainslider/slide3.jpg");
/* harmony import */ var _slide3_jpg__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_slide3_jpg__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__);

var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/components/Blocks/Mainslider/View.jsx";

function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); if (enumerableOnly) { symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; }); } keys.push.apply(keys, symbols); } return keys; }

function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i] != null ? arguments[i] : {}; if (i % 2) { ownKeys(Object(source), true).forEach(function (key) { _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(target, key, source[key]); }); } else if (Object.getOwnPropertyDescriptors) { Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)); } else { ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } } return target; }








const View = props => {
  var settings = {
    outerWidth: 40,
    className: "center",
    centerMode: true,
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1
  };
  return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__["jsxs"])(react_slick__WEBPACK_IMPORTED_MODULE_1___default.a, _objectSpread(_objectSpread({}, settings), {}, {
    children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__["jsx"])("div", {
      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__["jsx"])("img", {
        src: "$(slide1)",
        alt: ""
      })
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__["jsx"])("div", {
      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__["jsx"])("img", {
        src: "$(slide2)",
        alt: ""
      })
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__["jsx"])("div", {
      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__["jsx"])("img", {
        src: "$(slide3)",
        alt: ""
      })
    })]
  }));
};

/* harmony default export */ __webpack_exports__["default"] = (View);

/***/ }),

/***/ "./src/components/Blocks/Mainslider/slide1.jpeg":
/*!******************************************************!*\
  !*** ./src/components/Blocks/Mainslider/slide1.jpeg ***!
  \******************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__.p + "static/media/slide1.316218d0.jpeg";

/***/ }),

/***/ "./src/components/Blocks/Mainslider/slide2.jpeg":
/*!******************************************************!*\
  !*** ./src/components/Blocks/Mainslider/slide2.jpeg ***!
  \******************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__.p + "static/media/slide2.3dc62288.jpeg";

/***/ }),

/***/ "./src/components/Blocks/Mainslider/slide3.jpg":
/*!*****************************************************!*\
  !*** ./src/components/Blocks/Mainslider/slide3.jpg ***!
  \*****************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__.p + "static/media/slide3.32e842af.jpg";

/***/ }),

/***/ "./src/components/index.js":
/*!*********************************!*\
  !*** ./src/components/index.js ***!
  \*********************************/
/*! exports provided: MainSliderViewBlock, MainSliderEditBlock */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _Blocks_Mainslider_View__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./Blocks/Mainslider/View */ "./src/components/Blocks/Mainslider/View.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "MainSliderViewBlock", function() { return _Blocks_Mainslider_View__WEBPACK_IMPORTED_MODULE_0__["default"]; });

/* harmony import */ var _Blocks_Mainslider_Edit__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./Blocks/Mainslider/Edit */ "./src/components/Blocks/Mainslider/Edit.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "MainSliderEditBlock", function() { return _Blocks_Mainslider_Edit__WEBPACK_IMPORTED_MODULE_1__["default"]; });

/**
 * Add your components here.
 * 
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

 // import { defineMessages } from 'react-intl';
// All your imports required for the config here BEFORE this line

 // defineMessages({
//   mainslider: {
//     id: 'Main Slider',
//     defaultMessage: 'Main Slider',
//   },
// });

function applyConfig(config) {
  // config.blocks.blocksConfig.mainslider = {
  //   id: 'mainslider',
  //   title: 'Main Slider',
  //   icon: sliderSVG,
  //   group: 'common',
  //   view: MainSliderViewBlock,
  //   edit: MainSliderEditBlock,
  //   restricted: false,
  //   mostUsed: true,
  //   security: {
  //     addPermission: [],
  //     view: [],
  //   },
  // };
  // Add here your project's configuration here by modifying `config` accordingly
  return config;
}

/***/ })

};
//# sourceMappingURL=server.d76285ddd529b37d904b.hot-update.js.map