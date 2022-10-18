exports.id = "server";
exports.modules = {

/***/ "./src/customizations/components/theme/Breadcrumbs/Breadcrumbs.jsx":
/*!*************************************************************************!*\
  !*** ./src/customizations/components/theme/Breadcrumbs/Breadcrumbs.jsx ***!
  \*************************************************************************/
/*! exports provided: BreadcrumbsComponent, default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "BreadcrumbsComponent", function() { return BreadcrumbsComponent; });
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/defineProperty */ "@babel/runtime/helpers/defineProperty");
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! prop-types */ "prop-types");
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(prop_types__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-redux */ "react-redux");
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react_redux__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var redux__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! redux */ "redux");
/* harmony import */ var redux__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(redux__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! react-router-dom */ "react-router-dom");
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(react_router_dom__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! semantic-ui-react */ "semantic-ui-react");
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! react-intl */ "react-intl");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(react_intl__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var _plone_volto_actions__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @plone/volto/actions */ "./node_modules/@plone/volto/src/actions/index.js");
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var _plone_volto_icons_home_svg__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! @plone/volto/icons/home.svg */ "./node_modules/@plone/volto/src/icons/home.svg");
/* harmony import */ var _plone_volto_icons_home_svg__WEBPACK_IMPORTED_MODULE_11___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_home_svg__WEBPACK_IMPORTED_MODULE_11__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__);

var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/customizations/components/theme/Breadcrumbs/Breadcrumbs.jsx";

/**
 * Breadcrumbs components.
 * @module components/theme/Breadcrumbs/Breadcrumbs
 */













const messages = Object(react_intl__WEBPACK_IMPORTED_MODULE_7__["defineMessages"])({
  home: {
    "id": "Home",
    "defaultMessage": "Home"
  },
  breadcrumbs: {
    "id": "Breadcrumbs",
    "defaultMessage": "Breadcrumbs"
  }
});
/**
 * Breadcrumbs container class.
 */

class BreadcrumbsComponent extends react__WEBPACK_IMPORTED_MODULE_1__["Component"] {
  /**
   * Property types.
   * @property {Object} propTypes Property types.
   * @static
   */
  componentDidMount() {
    if (!Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_10__["hasApiExpander"])('breadcrumbs', Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_10__["getBaseUrl"])(this.props.pathname))) {
      this.props.getBreadcrumbs(Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_10__["getBaseUrl"])(this.props.pathname));
    }
  }
  /**
   * Component will receive props
   * @method componentWillReceiveProps
   * @param {Object} nextProps Next properties
   * @returns {undefined}
   */


  UNSAFE_componentWillReceiveProps(nextProps) {
    if (nextProps.pathname !== this.props.pathname) {
      if (!Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_10__["hasApiExpander"])('breadcrumbs', Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_10__["getBaseUrl"])(this.props.pathname))) {
        this.props.getBreadcrumbs(Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_10__["getBaseUrl"])(nextProps.pathname));
      }
    }
  }
  /**
   * Render method.
   * @method render
   * @returns {string} Markup for the component.
   */


  render() {
    return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Segment"], {
      role: "navigation",
      "aria-label": this.props.intl.formatMessage(messages.breadcrumbs),
      className: "breadcrumbs",
      secondary: true,
      vertical: true,
      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Container"], {
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Breadcrumb"], {
          icon: "right angle",
          children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])(react_router_dom__WEBPACK_IMPORTED_MODULE_5__["Link"], {
            to: this.props.root || '/',
            className: "section",
            title: this.props.intl.formatMessage(messages.home),
            children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Breadcrumb"], {
              icon: "right chevron"
            })
          }), this.props.items.map((item, index, items) => [
          /*#__PURE__*/
          // <Breadcrumb.Divider key={`divider-${item.url}`} />,
          Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Breadcrumb"].Divider, {
            icon: "right chevron"
          }), index < items.length - 1 ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])(react_router_dom__WEBPACK_IMPORTED_MODULE_5__["Link"], {
            to: item.url,
            className: "section",
            children: item.title
          }, item.url) : /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Breadcrumb"].Section, {
            active: true,
            children: item.title
          }, item.url)])]
        })
      })
    });
  }

}

_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(BreadcrumbsComponent, "propTypes", {
  getBreadcrumbs: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.func.isRequired,
  pathname: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string.isRequired,
  root: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string,
  items: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.arrayOf(prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.shape({
    title: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string,
    url: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string
  })).isRequired
});

/* harmony default export */ __webpack_exports__["default"] = (Object(redux__WEBPACK_IMPORTED_MODULE_4__["compose"])(react_intl__WEBPACK_IMPORTED_MODULE_7__["injectIntl"], Object(react_redux__WEBPACK_IMPORTED_MODULE_3__["connect"])(state => ({
  items: state.breadcrumbs.items,
  root: state.breadcrumbs.root
}), {
  getBreadcrumbs: _plone_volto_actions__WEBPACK_IMPORTED_MODULE_9__["getBreadcrumbs"]
}))(BreadcrumbsComponent));

/***/ })

};
//# sourceMappingURL=server.83661ed5385d34bbc911.hot-update.js.map