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
/* harmony import */ var _plone_volto_components_theme_Navigation_ContextNavigation__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @plone/volto/components/theme/Navigation/ContextNavigation */ "./node_modules/@plone/volto/src/components/theme/Navigation/ContextNavigation.jsx");
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var _plone_volto_registry__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @plone/volto/registry */ "./node_modules/@plone/volto/src/registry.js");
/* harmony import */ var _plone_volto_actions__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @plone/volto/actions */ "./node_modules/@plone/volto/src/actions/index.js");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! semantic-ui-react */ "semantic-ui-react");
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(semantic_ui_react__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! prop-types */ "prop-types");
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(prop_types__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! react-redux */ "react-redux");
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(react_redux__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var redux__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! redux */ "redux");
/* harmony import */ var redux__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(redux__WEBPACK_IMPORTED_MODULE_8__);
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__);
var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/customizations/components/theme/Header/Header.jsx";

/**
 * Header component.
 * @module components/theme/Header/Header
 */













function useScrollDirection() {
  const [scrollDirection, setScrollDirection] = Object(react__WEBPACK_IMPORTED_MODULE_4__["useState"])(null);
  Object(react__WEBPACK_IMPORTED_MODULE_4__["useEffect"])(() => {
    let lastScrollY = window.pageYOffset;

    const updateScrollDirection = () => {
      const scrollY = window.pageYOffset;
      const direction = scrollY > lastScrollY ? 'down' : 'up';

      if (direction !== scrollDirection && (scrollY - lastScrollY > 30 || scrollY - lastScrollY < -10)) {
        setScrollDirection(direction);
      }

      lastScrollY = scrollY > 0 ? scrollY : 0;
    };

    window.addEventListener('scroll', updateScrollDirection); // add event listener

    return () => {
      window.removeEventListener('scroll', updateScrollDirection); // clean up
    };
  }, [scrollDirection]);
  return scrollDirection;
}
/**
 * Header component class.
 * @class Header
 * @extends Component
 */


const Header = props => {
  /**
  /**
   * Render method.
   * @method render
   * @returns {string} Markup for the component.
   */
  const scrollDirection = useScrollDirection();
  const menuItems = props.menuItems;
  const {
    settings
  } = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_2__["default"];
  return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_5__["Segment"], {
    basic: true,
    className: `header-wrapper ${scrollDirection === 'down' ? 'hide' : 'show'}`,
    id: "header-wrapper",
    role: "banner",
    children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_5__["Container"], {
      className: "header-container",
      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])("div", {
        className: "header",
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsxs"])("div", {
          className: "logo-nav-wrapper",
          children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])("div", {
            className: "logo",
            children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])("a", {
              className: "logo-written",
              id: "writtenlogo",
              href: "/",
              children: "ZEEUWS MUSEUM"
            })
          }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_9__["Navigation"], {
            pathname: props.pathname
          }), console.log(props.items)]
        })
      })
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_9__["Breadcrumbs"], {
      pathname: props.pathname,
      menuItems: props.menuItems
    })]
  });
};

/* harmony default export */ __webpack_exports__["default"] = (Object(react_redux__WEBPACK_IMPORTED_MODULE_7__["connect"])(state => ({
  token: state.userSession.token,
  items: state.navigation.items
}), {
  getNavigation: _plone_volto_actions__WEBPACK_IMPORTED_MODULE_3__["getNavigation"]
})(Header));
Header.propTypes = {
  getNavigation: prop_types__WEBPACK_IMPORTED_MODULE_6___default.a.func.isRequired,
  pathname: prop_types__WEBPACK_IMPORTED_MODULE_6___default.a.string.isRequired
};

/***/ })

};
//# sourceMappingURL=server.df710330d8dd07676a48.hot-update.js.map