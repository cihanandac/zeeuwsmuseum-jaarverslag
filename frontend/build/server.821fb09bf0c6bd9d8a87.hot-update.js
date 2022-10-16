exports.id = "server";
exports.modules = {

/***/ "./src/customizations/components/theme/Header/Stickyfunction.jsx":
/*!***********************************************************************!*\
  !*** ./src/customizations/components/theme/Header/Stickyfunction.jsx ***!
  \***********************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_dom__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react-dom */ "react-dom");
/* harmony import */ var react_dom__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react_dom__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var ___WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../../../ */ "./src/index.js");




function Stickyfunction() {
  const [position, setPosition] = Object(react__WEBPACK_IMPORTED_MODULE_0__["useState"])(window.pageYOffset);
  const [visible, setVisible] = Object(react__WEBPACK_IMPORTED_MODULE_0__["useState"])(true);
  Object(react__WEBPACK_IMPORTED_MODULE_0__["useEffect"])(() => {
    const handleScroll = () => {
      let moving = window.pageYOffset;
      setVisible(position > moving);
      setPosition(moving);
    };

    window.addEventListener('scroll', handleScroll);
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  });
  const cls = visible ? 'visible' : 'hidden';
}

/* harmony default export */ __webpack_exports__["default"] = (Stickyfunction);

/***/ })

};
//# sourceMappingURL=server.821fb09bf0c6bd9d8a87.hot-update.js.map