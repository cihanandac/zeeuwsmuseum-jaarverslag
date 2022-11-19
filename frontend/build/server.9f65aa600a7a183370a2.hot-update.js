exports.id = "server";
exports.modules = {

/***/ "./src/customizations/components/theme/Navigation/NavItem.jsx":
/*!********************************************************************!*\
  !*** ./src/customizations/components/theme/Navigation/NavItem.jsx ***!
  \********************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react-router-dom */ "react-router-dom");
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react_router_dom__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var _plone_volto_registry__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @plone/volto/registry */ "./node_modules/@plone/volto/src/registry.js");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__);
var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/customizations/components/theme/Navigation/NavItem.jsx";







const NavItem = ({
  item,
  lang
}) => {
  const {
    settings
  } = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_3__["default"]; // The item.url in the root is ''
  // TODO: make more consistent it everywhere (eg. reducers to return '/' instead of '')

  if (Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_2__["isInternalURL"])(item.url) || item.url === '') {
    return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsxs"])(react_router_dom__WEBPACK_IMPORTED_MODULE_1__["NavLink"], {
      to: item.url === '' ? '/' : item.url,
      className: "item",
      activeClassName: "active",
      exact: settings.isMultilingual ? item.url === `/${lang}` : item.url === '',
      children: [item.title, console.log(item)]
    }, item.url);
  } else {
    return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])("a", {
      href: item.url,
      className: "item",
      rel: "noopener noreferrer",
      children: item.title
    }, item.url);
  }
};

/* harmony default export */ __webpack_exports__["default"] = (NavItem);

/***/ })

};
//# sourceMappingURL=server.9f65aa600a7a183370a2.hot-update.js.map