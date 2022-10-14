exports.id = "server";
exports.modules = {

/***/ "./src/customizations/components/theme/Header/Header.jsx":
/*!***************************************************************!*\
  !*** ./src/customizations/components/theme/Header/Header.jsx ***!
  \***************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/defineProperty */ "@babel/runtime/helpers/defineProperty");
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! semantic-ui-react */ "semantic-ui-react");
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! prop-types */ "prop-types");
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(prop_types__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react-redux */ "react-redux");
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react_redux__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var _Menudropdown__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./Menudropdown */ "./src/customizations/components/theme/Header/Menudropdown.jsx");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__);

var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/customizations/components/theme/Header/Header.jsx";

/**
 * Header component.
 * @module components/theme/Header/Header
 */






/**
 * Header component class.
 * @class Header
 * @extends Component
 */




class Header extends react__WEBPACK_IMPORTED_MODULE_1__["Component"] {
  /**
   * Property types.
   * @property {Object} propTypes Property types.
   * @static
   */

  /**
   * Default properties.
   * @property {Object} defaultProps Default properties.
   * @static
   */

  /**
   * Render method.
   * @method render
   * @returns {string} Markup for the component.
   */
  render() {
    return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Segment"], {
      basic: true,
      className: "header-wrapper",
      role: "banner",
      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Container"], {
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])("div", {
          className: "header",
          children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsxs"])("div", {
            className: "logo-nav-wrapper",
            children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])("div", {
              className: "logo",
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])("a", {
                className: "logo-written",
                id: "writtenlogo",
                href: "/",
                children: "ZEEUWS MUSEUM"
              })
            }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_5__["Navigation"], {
              pathname: this.props.pathname
            })]
          })
        })
      })
    });
  }

}

_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(Header, "propTypes", {
  token: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.string,
  pathname: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.string.isRequired
});

_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(Header, "defaultProps", {
  token: null
});

/* harmony default export */ __webpack_exports__["default"] = (Object(react_redux__WEBPACK_IMPORTED_MODULE_4__["connect"])(state => ({
  token: state.userSession.token
}))(Header));

/***/ })

};
//# sourceMappingURL=server.c3d1e98e8db1b07a3c1b.hot-update.js.map