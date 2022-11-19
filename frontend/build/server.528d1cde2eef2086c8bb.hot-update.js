exports.id = "server";
exports.modules = {

/***/ "./node_modules/@plone/volto/src/components/theme/Navigation/ContextNavigation.jsx":
/*!*****************************************************************************************!*\
  !*** ./node_modules/@plone/volto/src/components/theme/Navigation/ContextNavigation.jsx ***!
  \*****************************************************************************************/
/*! exports provided: ContextNavigationComponent, default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "ContextNavigationComponent", function() { return ContextNavigationComponent; });
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! prop-types */ "prop-types");
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(prop_types__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! semantic-ui-react */ "semantic-ui-react");
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-router-dom */ "react-router-dom");
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react_router_dom__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var classnames__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! classnames */ "classnames");
/* harmony import */ var classnames__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(classnames__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var redux__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! redux */ "redux");
/* harmony import */ var redux__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(redux__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var react_router__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! react-router */ "react-router");
/* harmony import */ var react_router__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(react_router__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! react-intl */ "react-intl");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(react_intl__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var _withContentNavigation__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! ./withContentNavigation */ "./node_modules/@plone/volto/src/components/theme/Navigation/withContentNavigation.js");
/* harmony import */ var _plone_volto_icons_left_key_svg__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! @plone/volto/icons/left-key.svg */ "./node_modules/@plone/volto/src/icons/left-key.svg");
/* harmony import */ var _plone_volto_icons_left_key_svg__WEBPACK_IMPORTED_MODULE_11___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_left_key_svg__WEBPACK_IMPORTED_MODULE_11__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__);
var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/node_modules/@plone/volto/src/components/theme/Navigation/ContextNavigation.jsx";














const messages = Object(react_intl__WEBPACK_IMPORTED_MODULE_7__["defineMessages"])({
  navigation: {
    "id": "Navigation",
    "defaultMessage": "Navigation"
  }
});

function renderNode(node, parentLevel) {
  var _node$items;

  const level = parentLevel + 1;
  return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["List"].Item, {
    active: node.is_current,
    className: `level-${level}`,
    children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["List"].Content, {
      children: [node.type !== 'link' ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsxs"])(react_router_dom__WEBPACK_IMPORTED_MODULE_3__["Link"], {
        to: Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_8__["flattenToAppURL"])(node.href),
        title: node.description,
        className: classnames__WEBPACK_IMPORTED_MODULE_4___default()(`contenttype-${node.type}`, {
          in_path: node.is_in_path
        }),
        children: [node.thumb ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Image"], {
          src: Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_8__["flattenToAppURL"])(node.thumb)
        }) : '', node.title, node.is_current ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["List"].Content, {
          className: "active-indicator",
          children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_9__["Icon"], {
            name: _plone_volto_icons_left_key_svg__WEBPACK_IMPORTED_MODULE_11___default.a,
            size: "30px"
          })
        }) : '']
      }) : /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_9__["UniversalLink"], {
        href: Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_8__["flattenToAppURL"])(node.href),
        children: node.title
      }), ((_node$items = node.items) === null || _node$items === void 0 ? void 0 : _node$items.length) && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["List"].List, {
        children: node.items.map(node => renderNode(node, level))
      }) || '']
    })
  }, node['@id']);
}
/**
 * A navigation slot implementation, similar to the classic Plone navigation
 * portlet. It uses the same API, so the options are similar to
 * INavigationPortlet
 */


function ContextNavigationComponent(props) {
  const {
    navigation = {}
  } = props;
  const {
    items = []
  } = navigation;
  const intl = Object(react_intl__WEBPACK_IMPORTED_MODULE_7__["useIntl"])();
  return items.length ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsxs"])("nav", {
    className: "context-navigation",
    children: [navigation.has_custom_name ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])("div", {
      className: "context-navigation-header",
      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])(react_router_dom__WEBPACK_IMPORTED_MODULE_3__["Link"], {
        to: Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_8__["flattenToAppURL"])(navigation.url || ''),
        children: navigation.title
      })
    }) : /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])("div", {
      className: "context-navigation-header",
      children: intl.formatMessage(messages.navigation)
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["List"], {
      children: items.map(node => renderNode(node, 0))
    })]
  }) : '';
}
ContextNavigationComponent.propTypes = {
  /**
   * Navigation tree returned from @contextnavigation restapi endpoint
   */
  navigation: prop_types__WEBPACK_IMPORTED_MODULE_0___default.a.shape({
    items: prop_types__WEBPACK_IMPORTED_MODULE_0___default.a.arrayOf(prop_types__WEBPACK_IMPORTED_MODULE_0___default.a.shape({
      title: prop_types__WEBPACK_IMPORTED_MODULE_0___default.a.string,
      url: prop_types__WEBPACK_IMPORTED_MODULE_0___default.a.string
    })),
    has_custom_name: prop_types__WEBPACK_IMPORTED_MODULE_0___default.a.bool,
    title: prop_types__WEBPACK_IMPORTED_MODULE_0___default.a.string
  })
};
/* harmony default export */ __webpack_exports__["default"] = (Object(redux__WEBPACK_IMPORTED_MODULE_5__["compose"])(react_router__WEBPACK_IMPORTED_MODULE_6__["withRouter"], _withContentNavigation__WEBPACK_IMPORTED_MODULE_10__["withContentNavigation"])(ContextNavigationComponent));

/***/ }),

/***/ "./node_modules/@plone/volto/src/components/theme/Navigation/withContentNavigation.js":
/*!********************************************************************************************!*\
  !*** ./node_modules/@plone/volto/src/components/theme/Navigation/withContentNavigation.js ***!
  \********************************************************************************************/
/*! exports provided: withContentNavigation */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "withContentNavigation", function() { return withContentNavigation; });
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/defineProperty */ "@babel/runtime/helpers/defineProperty");
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! prop-types */ "prop-types");
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(prop_types__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-redux */ "react-redux");
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react_redux__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var use_deep_compare_effect__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! use-deep-compare-effect */ "use-deep-compare-effect");
/* harmony import */ var use_deep_compare_effect__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(use_deep_compare_effect__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var _plone_volto_actions__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @plone/volto/actions */ "./node_modules/@plone/volto/src/actions/index.js");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__);

var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/node_modules/@plone/volto/src/components/theme/Navigation/withContentNavigation.js";

function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); if (enumerableOnly) { symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; }); } keys.push.apply(keys, symbols); } return keys; }

function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i] != null ? arguments[i] : {}; if (i % 2) { ownKeys(Object(source), true).forEach(function (key) { _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(target, key, source[key]); }); } else if (Object.getOwnPropertyDescriptors) { Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)); } else { ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } } return target; }








function withContentNavigation(WrappedComponent) {
  /**
   * Options passed in params can be:
   *
   * - name - The title of the navigation tree.
   * - root_path - Root node path, can be "frontend path", derived from router
   * - includeTop - Bool, Include top nodeschema
   * - currentFolderOnly - Bool, Only show the contents of the current folder.
   * - topLevel - Int, Start level
   * - bottomLevel - Int, Navigation tree depth
   * - no_icons - Bool, Suppress Icons
   * - thumb_scale - String, Override thumb scale
   * - no_thumbs = Bool, Suppress thumbs
   *
   */
  function Wrapped(props) {
    const {
      location,
      pathname = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_5__["getBaseUrl"])(location.pathname),
      params = {}
    } = props;
    let qs = Object.keys(params).sort().map(key => `expand.contextnavigation.${key}=${params[key]}`).join('&');
    const path = `${pathname}${pathname.endsWith('/') ? '' : '/'}@contextnavigation${qs ? `?${qs}` : ''}`;
    const dispatch = Object(react_redux__WEBPACK_IMPORTED_MODULE_3__["useDispatch"])();
    const nav = Object(react_redux__WEBPACK_IMPORTED_MODULE_3__["useSelector"])(state => {
      var _state$contextNavigat, _state$contextNavigat2;

      return (_state$contextNavigat = state.contextNavigation) === null || _state$contextNavigat === void 0 ? void 0 : (_state$contextNavigat2 = _state$contextNavigat[path]) === null || _state$contextNavigat2 === void 0 ? void 0 : _state$contextNavigat2.data;
    });
    use_deep_compare_effect__WEBPACK_IMPORTED_MODULE_4___default()(() => {
      dispatch(Object(_plone_volto_actions__WEBPACK_IMPORTED_MODULE_6__["getContextNavigation"])(pathname, params));
    }, [pathname, dispatch, params]);
    return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])(WrappedComponent, _objectSpread(_objectSpread({}, props), {}, {
      navigation: nav
    }));
  }

  Wrapped.propTypes = {
    /**
     * Location, from router
     */
    location: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.shape({
      pathname: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string
    }),

    /**
     * Parameters passed to the @contextnavigation endpoint
     */
    params: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.shape({
      name: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,
      root_path: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,
      includeTop: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.bool,
      currentFolderOnly: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.bool,
      topLevel: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.number,
      bottomLevel: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.number,
      no_icons: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.bool,
      thumb_scale: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,
      no_thumbs: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.bool
    })
  };
  Wrapped.displayName = `WithContextNavigation(${getDisplayName(WrappedComponent)})`;
  return Wrapped;
}

function getDisplayName(WrappedComponent) {
  return WrappedComponent.displayName || WrappedComponent.name || 'Component';
}

/***/ }),

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
          }), console.log( /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])(_plone_volto_components_theme_Navigation_ContextNavigation__WEBPACK_IMPORTED_MODULE_0__["default"], {
            pathname: props.pathname,
            params: {
              currentFolderOnly: false
            }
          }))]
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
  items: state
}), {
  getNavigation: _plone_volto_actions__WEBPACK_IMPORTED_MODULE_3__["getNavigation"]
})(Header));
Header.propTypes = {
  getNavigation: prop_types__WEBPACK_IMPORTED_MODULE_6___default.a.func.isRequired,
  pathname: prop_types__WEBPACK_IMPORTED_MODULE_6___default.a.string.isRequired
};

/***/ })

};
//# sourceMappingURL=server.528d1cde2eef2086c8bb.hot-update.js.map