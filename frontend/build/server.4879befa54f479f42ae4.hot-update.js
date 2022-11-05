exports.id = "server";
exports.modules = {

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
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! semantic-ui-react */ "semantic-ui-react");
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__);
var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/components/Blocks/PhotoDescription/View.jsx";






const View = ({
  data
}) => {
  const urlHandler = url => Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_1__["isInternalURL"])(url) ? `${Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_1__["flattenToAppURL"])(url)}/@@images/image` : url;

  return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsxs"])("div", {
    className: "bannerAreaRoot",
    style: {
      backgroundImage: `url("${urlHandler(backgroundImage)}")`
    },
    children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsxs"])("div", {
      className: "bannerAreaLeft",
      children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsx"])("div", {
        className: "bannerAreaTag",
        children: tag
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsxs"])("div", {
        className: "bannerAreaHeading",
        children: [headingLine1, /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsx"])("br", {}), headingLine2]
      }), showActionButton ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Button"], {
        primary: true,
        className: "bannerAreaCTA",
        content: actionButtonText,
        as: "a",
        href: actionButtonUrl
      }) : null]
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsx"])("div", {
      className: "bannerAreaRight",
      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Image"], {
        src: urlHandler(foregroundImage),
        className: "bannerAreaRightImage"
      })
    })]
  });
};

/* harmony default export */ __webpack_exports__["default"] = (View);

/***/ })

};
//# sourceMappingURL=server.4879befa54f479f42ae4.hot-update.js.map