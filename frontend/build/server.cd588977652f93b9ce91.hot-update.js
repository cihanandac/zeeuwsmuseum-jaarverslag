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
/* harmony import */ var react_icons_bs__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! react-icons/bs */ "react-icons/bs");
/* harmony import */ var react_icons_bs__WEBPACK_IMPORTED_MODULE_11___default = /*#__PURE__*/__webpack_require__.n(react_icons_bs__WEBPACK_IMPORTED_MODULE_11__);
/* harmony import */ var _plone_volto_components_theme_Navigation_NavItems__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! @plone/volto/components/theme/Navigation/NavItems */ "./src/customizations/components/theme/Navigation/NavItems.jsx");
/* harmony import */ var react_icons_fa__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! react-icons/fa */ "react-icons/fa");
/* harmony import */ var react_icons_fa__WEBPACK_IMPORTED_MODULE_13___default = /*#__PURE__*/__webpack_require__.n(react_icons_fa__WEBPACK_IMPORTED_MODULE_13__);
/* harmony import */ var _plone_volto_icons_home_svg__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! @plone/volto/icons/home.svg */ "./node_modules/@plone/volto/src/icons/home.svg");
/* harmony import */ var _plone_volto_icons_home_svg__WEBPACK_IMPORTED_MODULE_14___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_home_svg__WEBPACK_IMPORTED_MODULE_14__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__);

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
    return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Segment"], {
      role: "navigation",
      "aria-label": this.props.intl.formatMessage(messages.breadcrumbs),
      className: "breadcrumbs",
      secondary: true,
      vertical: true,
      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Container"], {
        id: "crumbcontainer",
        children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Breadcrumb"], {
          id: "folderMap",
          children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(react_router_dom__WEBPACK_IMPORTED_MODULE_5__["Link"], {
            to: this.props.root || '/',
            className: "section",
            title: this.props.intl.formatMessage(messages.home)
          }), this.props.items.map((item, index, items) => [index != 0 ? index <= 2 ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsxs"])(react_router_dom__WEBPACK_IMPORTED_MODULE_5__["Link"], {
            to: item.url,
            className: "section",
            children: [item.title, /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("span", {
              children: "\xA0"
            })]
          }, item.url) : index > 2 ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Breadcrumb"].Section, {
            className: "crumbcontainer",
            active: true,
            children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Breadcrumb"].Divider, {
              className: "breaddivider",
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(react_icons_bs__WEBPACK_IMPORTED_MODULE_11__["BsChevronCompactRight"], {
                stroke: "white",
                fill: "currentColor",
                strokeWidth: "0.5"
              })
            }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
              className: "breadtitle",
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("span", {
                children: item.title
              })
            })]
          }, item.url) : '' : ''])]
        }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Container"], {
          id: "dropdowncontainer",
          children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
            id: "inhoud",
            children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"], {
              item: true,
              simple: true,
              text: this.props.items.length > 4 ? this.props.items[2].title : 'INHOUD',
              icon: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(react_icons_fa__WEBPACK_IMPORTED_MODULE_13__["FaChevronDown"], {
                color: "#808080"
              }),
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Menu, {
                className: "dropdownContentPage",
                children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Item, {
                  id: "InhoudDropdown",
                  children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
                    href: this.props.items[2] != null || undefined ? this.props.items[2].url : '',
                    children: "Beeldimpressie"
                  })
                }), this.props.items[2] != null || undefined ? [...this.props.menuItems].map((x, i) => x['@type'] == 'Document' ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Item, {
                  id: "InhoudDropdown",
                  children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
                    href: x['@id'],
                    children: x.title
                  })
                }) : '') : '', console.log(this.props.menuItems['@id']), console.log(this.props.menuItems[2]['title'])]
              })
            })
          })
        })]
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
//# sourceMappingURL=server.cd588977652f93b9ce91.hot-update.js.map