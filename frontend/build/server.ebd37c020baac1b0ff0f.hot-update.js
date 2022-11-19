exports.id = "server";
exports.modules = {

/***/ "./src/customizations/components/theme/Navigation/Navigation.jsx":
/*!***********************************************************************!*\
  !*** ./src/customizations/components/theme/Navigation/Navigation.jsx ***!
  \***********************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/defineProperty */ "@babel/runtime/helpers/defineProperty");
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var lodash_isMatch__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! lodash/isMatch */ "lodash/isMatch");
/* harmony import */ var lodash_isMatch__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(lodash_isMatch__WEBPACK_IMPORTED_MODULE_1__);
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
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! react-intl */ "react-intl");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(react_intl__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! semantic-ui-react */ "semantic-ui-react");
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(semantic_ui_react__WEBPACK_IMPORTED_MODULE_8__);
/* harmony import */ var classnames__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! classnames */ "classnames");
/* harmony import */ var classnames__WEBPACK_IMPORTED_MODULE_9___default = /*#__PURE__*/__webpack_require__.n(classnames__WEBPACK_IMPORTED_MODULE_9__);
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var _plone_volto_actions__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! @plone/volto/actions */ "./node_modules/@plone/volto/src/actions/index.js");
/* harmony import */ var _plone_volto_registry__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! @plone/volto/registry */ "./node_modules/@plone/volto/src/registry.js");
/* harmony import */ var _plone_volto_icons_clear_svg__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! @plone/volto/icons/clear.svg */ "./node_modules/@plone/volto/src/icons/clear.svg");
/* harmony import */ var _plone_volto_icons_clear_svg__WEBPACK_IMPORTED_MODULE_14___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_clear_svg__WEBPACK_IMPORTED_MODULE_14__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__);


var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/customizations/components/theme/Navigation/Navigation.jsx";

/**
 * Navigation components.
 * @module components/theme/Navigation/Navigation
 */
















const messages = Object(react_intl__WEBPACK_IMPORTED_MODULE_7__["defineMessages"])({
  closeMobileMenu: {
    "id": "Close menu",
    "defaultMessage": "Close menu"
  },
  openMobileMenu: {
    "id": "Open menu",
    "defaultMessage": "Open menu"
  }
});
/**
 * Navigation container class.
 * @class Navigation
 * @extends Component
 */

class Navigation extends react__WEBPACK_IMPORTED_MODULE_2__["Component"] {
  /**
   * Property types.
   * @property {Object} propTypes Property types.
   * @static
   */

  /**
   * Constructor
   * @method constructor
   * @param {Object} props Component properties
   * @constructs Navigation
   */
  constructor(props) {
    super(props);

    _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(this, "handleClickOutsideNav", event => {
      if (this.container.current && !this.container.current.contains(event.target)) {
        this.setState({
          isMobileMenuOpen: false
        });
      }
    });

    this.toggleMobileMenu = this.toggleMobileMenu.bind(this);
    this.closeMobileMenu = this.closeMobileMenu.bind(this);
    this.state = {
      isMobileMenuOpen: false
    };
    this.container = /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_2___default.a.createRef();
  }
  /**
   * Component will mount
   * @method componentWillMount
   * @returns {undefined}
   */


  componentDidMount() {
    var _config$settings;

    this.props.getNavigation(Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_10__["getBaseUrl"])(this.props.pathname), ((_config$settings = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_13__["default"].settings) === null || _config$settings === void 0 ? void 0 : _config$settings.navDepth) || 3);
  }

  /**
   * Component will receive props
   * @method componentWillReceiveProps
   * @param {Object} nextProps Next properties
   * @returns {undefined}
   */
  componentDidUpdate(nextProps) {
    if (nextProps.pathname !== this.props.pathname || nextProps.userToken !== this.props.userToken) {
      var _config$settings2;

      this.props.getNavigation(Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_10__["getBaseUrl"])(nextProps.pathname), ((_config$settings2 = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_13__["default"].settings) === null || _config$settings2 === void 0 ? void 0 : _config$settings2.navDepth) || 3);
      this.closeMobileMenu();
    } // Hide submenu on route change


    if (document.querySelector('body')) {
      document.querySelector('body').click();
    }
  }
  /**
   * Check if menu is active
   * @method isActive
   * @param {string} url Url of the navigation item.
   * @returns {bool} Is menu active?
   */


  isActive(url) {
    return url === '' && this.props.pathname === '/' || url !== '' && lodash_isMatch__WEBPACK_IMPORTED_MODULE_1___default()(this.props.pathname.split('/'), url.split('/'));
  }
  /**
   * Toggle mobile menu's open state
   * @method toggleMobileMenu
   * @returns {undefined}
   */


  toggleMobileMenu() {
    this.setState({
      isMobileMenuOpen: !this.state.isMobileMenuOpen
    }, () => {
      if (this.state.isMobileMenuOpen) {
        document.addEventListener('mousedown', this.handleClickOutsideNav);
      }
    });
  }
  /**
   * Close mobile menu
   * @method closeMobileMenu
   * @returns {undefined}
   */


  closeMobileMenu() {
    if (!this.state.isMobileMenuOpen) {
      return;
    }

    this.setState({
      isMobileMenuOpen: false
    }, () => {
      document.removeEventListener('mousedown', this.handleClickOutsideNav);
    });
  }
  /**
   * Render method.
   * @method render
   * @returns {string} Markup for the component.
   */


  render() {
    return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsxs"])("nav", {
      className: "navigation",
      ref: this.container,
      children: [!this.state.isMobileMenuOpen && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
        className: "hamburger-wrapper mobile only",
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("button", {
          className: classnames__WEBPACK_IMPORTED_MODULE_9___default()('hamburger hamburger--collapse', {
            'is-active': this.state.isMobileMenuOpen
          }),
          "aria-label": this.state.isMobileMenuOpen ? this.props.intl.formatMessage(messages.closeMobileMenu, {
            type: this.props.type
          }) : this.props.intl.formatMessage(messages.openMobileMenu, {
            type: this.props.type
          }),
          title: this.state.isMobileMenuOpen ? this.props.intl.formatMessage(messages.closeMobileMenu, {
            type: this.props.type
          }) : this.props.intl.formatMessage(messages.openMobileMenu, {
            type: this.props.type
          }),
          type: "button",
          onClick: this.toggleMobileMenu,
          children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("span", {
            className: "hamburger-box",
            children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("span", {
              className: "hamburger-inner"
            })
          })
        })
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_8__["Menu"], {
        stackable: true,
        pointing: true,
        secondary: true,
        className: this.state.isMobileMenuOpen ? 'open' : 'tablet computer large screen widescreen only' // onClick={this.closeMobileMenu}
        // onBlur={() => this.closeMobileMenu}
        ,
        children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_8__["Button"], {
          icon: true,
          basic: true,
          title: "Close menu",
          className: "close-button",
          onClick: this.closeMobileMenu,
          children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_11__["Icon"], {
            name: _plone_volto_icons_clear_svg__WEBPACK_IMPORTED_MODULE_14___default.a,
            size: "37px"
          })
        }), this.props.items.map(item => {
          const flatUrl = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_10__["flattenToAppURL"])(item.url);
          const draftItem = item.review_state === 'draft';
          return item.items && item.items.length ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_8__["Dropdown"], {
            item: true,
            simple: true,
            className: this.isActive(flatUrl) ? 'item firstLevel menuActive' : 'item firstLevel',
            closeOnBlur: this.state.isMobileMenuOpen ? false : true,
            trigger: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(react_router_dom__WEBPACK_IMPORTED_MODULE_6__["Link"], {
              className: draftItem ? 'disabled' : '',
              to: flatUrl === '' ? '/' : flatUrl,
              onClick: e => {
                if (draftItem) e.preventDefault();
              },
              children: item.title
            }, flatUrl),
            children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_8__["Dropdown"].Menu, {
              children: item.items.map(subitem => {
                const flatSubUrl = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_10__["flattenToAppURL"])(subitem.url);
                const subDraftItem = subitem.review_state === 'draft';
                return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_8__["Dropdown"].Item, {
                  children: subitem.title.toLowerCase().includes('country profiles') ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsxs"])(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["Fragment"], {
                    children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
                      className: "secondLevel-wrapper",
                      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(react_router_dom__WEBPACK_IMPORTED_MODULE_6__["Link"], {
                        to: flatSubUrl === '' ? '/' : flatSubUrl,
                        className: classnames__WEBPACK_IMPORTED_MODULE_9___default()('item secondLevel', {
                          menuActive: this.isActive(flatSubUrl),
                          disabled: subDraftItem
                        }),
                        onClick: e => {
                          if (subDraftItem) e.preventDefault();
                        },
                        children: subitem.title
                      }, flatSubUrl)
                    }), subitem.items && subitem.items.length > 0 && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
                      className: "submenu-wrapper",
                      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
                        className: "submenu countries-submenu",
                        children: subitem.items.map(subsubitem => {
                          const flatSubSubUrl = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_10__["flattenToAppURL"])(subsubitem.url);
                          const subSubDraftItem = subsubitem.review_state === 'draft';
                          return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(react_router_dom__WEBPACK_IMPORTED_MODULE_6__["Link"], {
                            to: flatSubSubUrl === '' ? '/' : flatSubSubUrl,
                            title: subsubitem.title,
                            className: classnames__WEBPACK_IMPORTED_MODULE_9___default()('item thirdLevel', {
                              menuActive: this.isActive(flatSubUrl),
                              disabled: subSubDraftItem
                            }),
                            onClick: e => {
                              if (subSubDraftItem) e.preventDefault();
                            },
                            children: subsubitem.title
                          }, flatSubSubUrl);
                        })
                      })
                    })]
                  }) : /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsxs"])(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["Fragment"], {
                    children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
                      className: "secondLevel-wrapper",
                      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(react_router_dom__WEBPACK_IMPORTED_MODULE_6__["Link"], {
                        to: flatSubUrl === '' ? '/' : flatSubUrl,
                        className: classnames__WEBPACK_IMPORTED_MODULE_9___default()('item secondLevel', {
                          menuActive: this.isActive(flatSubUrl),
                          disabled: subDraftItem
                        }),
                        onClick: e => {
                          if (subDraftItem) e.preventDefault();
                        },
                        children: subitem.title
                      }, flatSubUrl)
                    }), subitem.items && subitem.items.length > 0 && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
                      className: "submenu-wrapper",
                      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
                        className: "submenu",
                        children: subitem.items.map(subsubitem => {
                          const flatSubSubUrl = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_10__["flattenToAppURL"])(subsubitem.url);
                          const subSubDraftItem = subsubitem.review_state === 'draft';
                          return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(react_router_dom__WEBPACK_IMPORTED_MODULE_6__["Link"], {
                            to: flatSubSubUrl === '' ? '/' : flatSubSubUrl,
                            title: subsubitem.title,
                            className: classnames__WEBPACK_IMPORTED_MODULE_9___default()('item thirdLevel', {
                              menuActive: this.isActive(flatSubUrl),
                              disabled: subSubDraftItem
                            }),
                            onClick: e => {
                              if (subSubDraftItem) e.preventDefault();
                            },
                            children: subsubitem.title
                          }, flatSubSubUrl);
                        })
                      })
                    })]
                  })
                }, flatSubUrl);
              })
            })
          }, flatUrl) : /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(react_router_dom__WEBPACK_IMPORTED_MODULE_6__["Link"], {
            to: flatUrl === '' ? '/' : flatUrl,
            className: this.isActive(flatUrl) ? 'item menuActive firstLevel' : 'item firstLevel',
            children: item.title
          }, flatUrl);
        })]
      })]
    });
  }

}

_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(Navigation, "propTypes", {
  getNavigation: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.func.isRequired,
  pathname: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.string.isRequired,
  items: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.arrayOf(prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.shape({
    title: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.string,
    url: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.string,
    items: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.array,
    review_state: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.string
  })).isRequired
});

/* harmony default export */ __webpack_exports__["default"] = (Object(redux__WEBPACK_IMPORTED_MODULE_5__["compose"])(react_intl__WEBPACK_IMPORTED_MODULE_7__["injectIntl"], Object(react_redux__WEBPACK_IMPORTED_MODULE_4__["connect"])(state => {
  var _state$userSession;

  return {
    items: state.localnavigation.items,
    userToken: state === null || state === void 0 ? void 0 : (_state$userSession = state.userSession) === null || _state$userSession === void 0 ? void 0 : _state$userSession.token
  };
}, {
  getNavigation: _plone_volto_actions__WEBPACK_IMPORTED_MODULE_12__["getNavigation"]
}))(Navigation));

/***/ }),

/***/ "lodash/isMatch":
/*!*********************************!*\
  !*** external "lodash/isMatch" ***!
  \*********************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = require("lodash/isMatch");

/***/ })

};
//# sourceMappingURL=server.ebd37c020baac1b0ff0f.hot-update.js.map