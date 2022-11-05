exports.id = "server";
exports.modules = {

/***/ "./src/components/Blocks/PhotoDescription/Edit.jsx":
/*!*********************************************************!*\
  !*** ./src/components/Blocks/PhotoDescription/Edit.jsx ***!
  \*********************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/defineProperty */ "@babel/runtime/helpers/defineProperty");
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _View__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./View */ "./src/components/Blocks/PhotoDescription/View.jsx");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__);

var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/components/Blocks/PhotoDescription/Edit.jsx";

function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); if (enumerableOnly) { symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; }); } keys.push.apply(keys, symbols); } return keys; }

function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i] != null ? arguments[i] : {}; if (i % 2) { ownKeys(Object(source), true).forEach(function (key) { _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(target, key, source[key]); }); } else if (Object.getOwnPropertyDescriptors) { Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)); } else { ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } } return target; }





const Edit = props => {
  return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsx"])(_View__WEBPACK_IMPORTED_MODULE_2__["default"], _objectSpread({}, props));
};

/* harmony default export */ __webpack_exports__["default"] = (Edit);

/***/ }),

/***/ "./src/components/Blocks/PhotoDescription/View.jsx":
/*!*********************************************************!*\
  !*** ./src/components/Blocks/PhotoDescription/View.jsx ***!
  \*********************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1__);
var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/components/Blocks/PhotoDescription/View.jsx";




const View = () => {
  return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1__["jsxs"])("p", {
    id: "photo-credit",
    children: ["Personeelsportret Marjan Ruiter ", /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1__["jsx"])("br", {}), "Foto Viorella Luciano"]
  });
};

/* harmony default export */ __webpack_exports__["default"] = (View);

/***/ }),

/***/ "./src/components/index.js":
/*!*********************************!*\
  !*** ./src/components/index.js ***!
  \*********************************/
/*! exports provided: EmptylineViewBlock, EmptylineEditBlock, SocialTopViewBlock, SocialTopEditBlock, SocialBottomViewBlock, SocialBottomEditBlock, NutezienViewBlock, NutezienEditBlock, PhotoDescriptionViewBlock, PhotoDescriptionEditBlock */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _Blocks_Emptyline_View__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./Blocks/Emptyline/View */ "./src/components/Blocks/Emptyline/View.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "EmptylineViewBlock", function() { return _Blocks_Emptyline_View__WEBPACK_IMPORTED_MODULE_0__["default"]; });

/* harmony import */ var _Blocks_Emptyline_Edit__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./Blocks/Emptyline/Edit */ "./src/components/Blocks/Emptyline/Edit.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "EmptylineEditBlock", function() { return _Blocks_Emptyline_Edit__WEBPACK_IMPORTED_MODULE_1__["default"]; });

/* harmony import */ var _Blocks_SocialTop_View__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./Blocks/SocialTop/View */ "./src/components/Blocks/SocialTop/View.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "SocialTopViewBlock", function() { return _Blocks_SocialTop_View__WEBPACK_IMPORTED_MODULE_2__["default"]; });

/* harmony import */ var _Blocks_SocialTop_Edit__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./Blocks/SocialTop/Edit */ "./src/components/Blocks/SocialTop/Edit.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "SocialTopEditBlock", function() { return _Blocks_SocialTop_Edit__WEBPACK_IMPORTED_MODULE_3__["default"]; });

/* harmony import */ var _Blocks_SocialBottom_View__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./Blocks/SocialBottom/View */ "./src/components/Blocks/SocialBottom/View.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "SocialBottomViewBlock", function() { return _Blocks_SocialBottom_View__WEBPACK_IMPORTED_MODULE_4__["default"]; });

/* harmony import */ var _Blocks_SocialBottom_Edit__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./Blocks/SocialBottom/Edit */ "./src/components/Blocks/SocialBottom/Edit.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "SocialBottomEditBlock", function() { return _Blocks_SocialBottom_Edit__WEBPACK_IMPORTED_MODULE_5__["default"]; });

/* harmony import */ var _Blocks_Nutezien_View__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./Blocks/Nutezien/View */ "./src/components/Blocks/Nutezien/View.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "NutezienViewBlock", function() { return _Blocks_Nutezien_View__WEBPACK_IMPORTED_MODULE_6__["default"]; });

/* harmony import */ var _Blocks_Nutezien_Edit__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./Blocks/Nutezien/Edit */ "./src/components/Blocks/Nutezien/Edit.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "NutezienEditBlock", function() { return _Blocks_Nutezien_Edit__WEBPACK_IMPORTED_MODULE_7__["default"]; });

/* harmony import */ var _Blocks_PhotoDescription_View__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./Blocks/PhotoDescription/View */ "./src/components/Blocks/PhotoDescription/View.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "PhotoDescriptionViewBlock", function() { return _Blocks_PhotoDescription_View__WEBPACK_IMPORTED_MODULE_8__["default"]; });

/* harmony import */ var _Blocks_PhotoDescription_Edit__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./Blocks/PhotoDescription/Edit */ "./src/components/Blocks/PhotoDescription/Edit.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "PhotoDescriptionEditBlock", function() { return _Blocks_PhotoDescription_Edit__WEBPACK_IMPORTED_MODULE_9__["default"]; });

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












/***/ })

};
//# sourceMappingURL=server.298b19c4f3fd01ee1239.hot-update.js.map