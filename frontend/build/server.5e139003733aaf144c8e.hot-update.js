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
/* harmony import */ var _plone_volto_config__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @plone/volto/config */ "./node_modules/@plone/volto/src/config/index.js");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! prop-types */ "prop-types");
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(prop_types__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react-redux */ "react-redux");
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react_redux__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var redux__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! redux */ "redux");
/* harmony import */ var redux__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(redux__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! react-router-dom */ "react-router-dom");
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(react_router_dom__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! semantic-ui-react */ "semantic-ui-react");
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(semantic_ui_react__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! react-intl */ "react-intl");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(react_intl__WEBPACK_IMPORTED_MODULE_8__);
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var _plone_volto_actions__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @plone/volto/actions */ "./node_modules/@plone/volto/src/actions/index.js");
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var react_icons_bs__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! react-icons/bs */ "react-icons/bs");
/* harmony import */ var react_icons_bs__WEBPACK_IMPORTED_MODULE_12___default = /*#__PURE__*/__webpack_require__.n(react_icons_bs__WEBPACK_IMPORTED_MODULE_12__);
/* harmony import */ var _plone_volto_components_theme_Navigation_NavItems__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! @plone/volto/components/theme/Navigation/NavItems */ "./src/customizations/components/theme/Navigation/NavItems.jsx");
/* harmony import */ var react_icons_fa__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! react-icons/fa */ "react-icons/fa");
/* harmony import */ var react_icons_fa__WEBPACK_IMPORTED_MODULE_14___default = /*#__PURE__*/__webpack_require__.n(react_icons_fa__WEBPACK_IMPORTED_MODULE_14__);
/* harmony import */ var _plone_volto_icons_home_svg__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! @plone/volto/icons/home.svg */ "./node_modules/@plone/volto/src/icons/home.svg");
/* harmony import */ var _plone_volto_icons_home_svg__WEBPACK_IMPORTED_MODULE_15___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_home_svg__WEBPACK_IMPORTED_MODULE_15__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16__);

var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/customizations/components/theme/Breadcrumbs/Breadcrumbs.jsx";

/**
 * Breadcrumbs components.
 * @module components/theme/Breadcrumbs/Breadcrumbs
 */




















const messages = Object(react_intl__WEBPACK_IMPORTED_MODULE_8__["defineMessages"])({
  home: {
    "id": "Home",
    "defaultMessage": "Home"
  },
  breadcrumbs: {
    "id": "Breadcrumbs",
    "defaultMessage": "Breadcrumbs"
  }
});
let menuArray = [];
/**
 * Breadcrumbs container class.
 */

class BreadcrumbsComponent extends react__WEBPACK_IMPORTED_MODULE_2__["Component"] {
  /**
   * Property types.
   * @property {Object} propTypes Property types.
   * @static
   * 
   */
  componentDidMount() {
    if (!Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_11__["hasApiExpander"])('breadcrumbs', Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_11__["getBaseUrl"])(this.props.pathname))) {
      this.props.getBreadcrumbs(Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_11__["getBaseUrl"])(this.props.pathname));
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
      if (!Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_11__["hasApiExpander"])('breadcrumbs', Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_11__["getBaseUrl"])(this.props.pathname))) {
        this.props.getBreadcrumbs(Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_11__["getBaseUrl"])(nextProps.pathname));
      }
    }
  }
  /**
   * Render method.
   * @method render
   * @returns {string} Markup for the component.
   */


  render() {
    return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_7__["Segment"], {
      role: "navigation",
      "aria-label": this.props.intl.formatMessage(messages.breadcrumbs),
      className: "breadcrumbs",
      secondary: true,
      vertical: true,
      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_7__["Container"], {
        id: "crumbcontainer",
        children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_7__["Breadcrumb"], {
          id: "folderMap",
          children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16__["jsx"])(react_router_dom__WEBPACK_IMPORTED_MODULE_6__["Link"], {
            to: this.props.root || '/',
            className: "section",
            title: this.props.intl.formatMessage(messages.home)
          }), console.log(this.props.items), "let navLength = ", ";", console.log(navLength), this.props.items.map((item, index, items) => [index != 0 ? index <= 2 ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16__["jsxs"])(react_router_dom__WEBPACK_IMPORTED_MODULE_6__["Link"], {
            to: item.url,
            className: "section",
            children: [item.title, /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16__["jsx"])("span", {
              children: "\xA0"
            })]
          }, item.url) : index > 2 ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_7__["Breadcrumb"].Section, {
            className: "crumbcontainer",
            active: true,
            children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_7__["Breadcrumb"].Divider, {
              className: "breaddivider",
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16__["jsx"])(react_icons_bs__WEBPACK_IMPORTED_MODULE_12__["BsChevronCompactRight"], {
                stroke: "white",
                fill: "currentColor",
                strokeWidth: "0.5"
              })
            }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16__["jsx"])("div", {
              className: "breadtitle",
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16__["jsx"])("span", {
                children: item.title
              })
            })]
          }, item.url) : '' : ''])]
        }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_7__["Container"], {
          id: "dropdowncontainer",
          children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16__["jsx"])("div", {
            id: "inhoud",
            children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_7__["Dropdown"], {
              item: true,
              simple: true,
              text: this.props.items.length > 4 ? this.props.items[2].title : 'INHOUD',
              icon: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16__["jsx"])(react_icons_fa__WEBPACK_IMPORTED_MODULE_14__["FaChevronDown"], {
                color: "#808080"
              }),
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_7__["Dropdown"].Menu, {
                className: "dropdownContentPage",
                children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_7__["Dropdown"].Item, {
                  id: "InhoudDropdown",
                  children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16__["jsx"])("a", {
                    href: this.props.items.length != undefined && this.props.items.length > 2 ? this.props.menuItems['@type'] == 'Document' ? this.props.items[this.props.items.length - 2].url : this.props.items[this.props.items.length - 1].url : '',
                    children: "Beeldimpressie"
                  })
                }), (() => {
                  if (this.props.menuItems['@type'] == "Document") {
                    let steps = this.props.items;
                    let nav = this.props.navItems;
                    let depth = 0;
                    let parentTitle = this.props.menuItems.parent.title;

                    for (let item1 of nav) {
                      if (item1.title == parentTitle) {
                        menuArray = item1.items;
                        break;
                      }

                      for (let item2 of item1.items) {
                        if (item2.title == parentTitle) {
                          menuArray = item2.items;
                          break;
                        }

                        for (let item3 of item2.items) {
                          if (item3.title == parentTitle) {
                            menuArray = item3.items;
                            break;
                          }

                          for (let item4 of item3.items) {
                            if (item4.title == parentTitle) {
                              menuArray = item4.items;
                              break;
                            }
                          }
                        }
                      }
                    }
                  } else {
                    menuArray = [];

                    for (let item of this.props.menuItems.items) {
                      if (menuArray.includes(item) == false) {
                        menuArray.push(item);
                        console.log(menuArray);
                      }
                    }
                  }
                })(), [...menuArray].map((x, i) => /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_7__["Dropdown"].Item, {
                  id: "InhoudDropdown",
                  children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_16__["jsx"])("a", {
                    href: x.url,
                    children: x.title
                  })
                }, i))]
              })
            })
          })
        })]
      })
    });
  }

}

_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(BreadcrumbsComponent, "propTypes", {
  getBreadcrumbs: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.func.isRequired,
  pathname: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.string.isRequired,
  root: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.string,
  items: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.arrayOf(prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.shape({
    title: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.string,
    url: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.string
  })).isRequired,
  navItems: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.arrayOf(prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.shape({
    title: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.string,
    url: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.string
  })).isRequired
});

/* harmony default export */ __webpack_exports__["default"] = (Object(redux__WEBPACK_IMPORTED_MODULE_5__["compose"])(react_intl__WEBPACK_IMPORTED_MODULE_8__["injectIntl"], Object(react_redux__WEBPACK_IMPORTED_MODULE_4__["connect"])(state => ({
  navItems: state.navigation.items,
  items: state.breadcrumbs.items,
  root: state.breadcrumbs.root
}), {
  getBreadcrumbs: _plone_volto_actions__WEBPACK_IMPORTED_MODULE_10__["getBreadcrumbs"]
}))(BreadcrumbsComponent));

/***/ })

};
//# sourceMappingURL=server.5e139003733aaf144c8e.hot-update.js.map