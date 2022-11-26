exports.id = "server";
exports.modules = {

/***/ "./src/customizations/components/theme/App/App.jsx":
/*!*********************************************************!*\
  !*** ./src/customizations/components/theme/App/App.jsx ***!
  \*********************************************************/
/*! exports provided: __test__, fetchContent, default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "__test__", function() { return __test__; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "fetchContent", function() { return fetchContent; });
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/defineProperty */ "@babel/runtime/helpers/defineProperty");
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var jwt_decode__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! jwt-decode */ "jwt-decode");
/* harmony import */ var jwt_decode__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(jwt_decode__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! prop-types */ "prop-types");
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(prop_types__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react-redux */ "react-redux");
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react_redux__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var redux__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! redux */ "redux");
/* harmony import */ var redux__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(redux__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! semantic-ui-react */ "semantic-ui-react");
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(semantic_ui_react__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var react_router_config__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! react-router-config */ "react-router-config");
/* harmony import */ var react_router_config__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(react_router_config__WEBPACK_IMPORTED_MODULE_8__);
/* harmony import */ var react_toastify__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! react-toastify */ "react-toastify");
/* harmony import */ var react_toastify__WEBPACK_IMPORTED_MODULE_9___default = /*#__PURE__*/__webpack_require__.n(react_toastify__WEBPACK_IMPORTED_MODULE_9__);
/* harmony import */ var lodash_split__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! lodash/split */ "lodash/split");
/* harmony import */ var lodash_split__WEBPACK_IMPORTED_MODULE_10___default = /*#__PURE__*/__webpack_require__.n(lodash_split__WEBPACK_IMPORTED_MODULE_10__);
/* harmony import */ var lodash_join__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! lodash/join */ "lodash/join");
/* harmony import */ var lodash_join__WEBPACK_IMPORTED_MODULE_11___default = /*#__PURE__*/__webpack_require__.n(lodash_join__WEBPACK_IMPORTED_MODULE_11__);
/* harmony import */ var lodash_trim__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! lodash/trim */ "lodash/trim");
/* harmony import */ var lodash_trim__WEBPACK_IMPORTED_MODULE_12___default = /*#__PURE__*/__webpack_require__.n(lodash_trim__WEBPACK_IMPORTED_MODULE_12__);
/* harmony import */ var classnames__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! classnames */ "classnames");
/* harmony import */ var classnames__WEBPACK_IMPORTED_MODULE_13___default = /*#__PURE__*/__webpack_require__.n(classnames__WEBPACK_IMPORTED_MODULE_13__);
/* harmony import */ var _plone_volto_registry__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! @plone/volto/registry */ "./node_modules/@plone/volto/src/registry.js");
/* harmony import */ var _plone_volto_components_manage_Pluggable__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! @plone/volto/components/manage/Pluggable */ "./node_modules/@plone/volto/src/components/manage/Pluggable/index.js");
/* harmony import */ var _plone_volto_helpers_Blocks_Blocks__WEBPACK_IMPORTED_MODULE_16__ = __webpack_require__(/*! @plone/volto/helpers/Blocks/Blocks */ "./node_modules/@plone/volto/src/helpers/Blocks/Blocks.js");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_17__ = __webpack_require__(/*! react-intl */ "react-intl");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_17___default = /*#__PURE__*/__webpack_require__.n(react_intl__WEBPACK_IMPORTED_MODULE_17__);
/* harmony import */ var _plone_volto_error__WEBPACK_IMPORTED_MODULE_18__ = __webpack_require__(/*! @plone/volto/error */ "./node_modules/@plone/volto/src/error.jsx");
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_19__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var _plone_volto_actions__WEBPACK_IMPORTED_MODULE_20__ = __webpack_require__(/*! @plone/volto/actions */ "./node_modules/@plone/volto/src/actions/index.js");
/* harmony import */ var _plone_volto_icons_clear_svg__WEBPACK_IMPORTED_MODULE_21__ = __webpack_require__(/*! @plone/volto/icons/clear.svg */ "./node_modules/@plone/volto/src/icons/clear.svg");
/* harmony import */ var _plone_volto_icons_clear_svg__WEBPACK_IMPORTED_MODULE_21___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_clear_svg__WEBPACK_IMPORTED_MODULE_21__);
/* harmony import */ var _plone_volto_components_theme_MultilingualRedirector_MultilingualRedirector__WEBPACK_IMPORTED_MODULE_22__ = __webpack_require__(/*! @plone/volto/components/theme/MultilingualRedirector/MultilingualRedirector */ "./node_modules/@plone/volto/src/components/theme/MultilingualRedirector/MultilingualRedirector.jsx");
/* harmony import */ var _plone_volto_components_manage_WorkingCopyToastsFactory_WorkingCopyToastsFactory__WEBPACK_IMPORTED_MODULE_23__ = __webpack_require__(/*! @plone/volto/components/manage/WorkingCopyToastsFactory/WorkingCopyToastsFactory */ "./node_modules/@plone/volto/src/components/manage/WorkingCopyToastsFactory/WorkingCopyToastsFactory.jsx");
/* harmony import */ var _plone_volto_components_manage_LockingToastsFactory_LockingToastsFactory__WEBPACK_IMPORTED_MODULE_24__ = __webpack_require__(/*! @plone/volto/components/manage/LockingToastsFactory/LockingToastsFactory */ "./node_modules/@plone/volto/src/components/manage/LockingToastsFactory/LockingToastsFactory.jsx");
/* harmony import */ var _sentry_browser__WEBPACK_IMPORTED_MODULE_25__ = __webpack_require__(/*! @sentry/browser */ "@sentry/browser");
/* harmony import */ var _sentry_browser__WEBPACK_IMPORTED_MODULE_25___default = /*#__PURE__*/__webpack_require__.n(_sentry_browser__WEBPACK_IMPORTED_MODULE_25__);
/* harmony import */ var react_icons_bs__WEBPACK_IMPORTED_MODULE_26__ = __webpack_require__(/*! react-icons/bs */ "react-icons/bs");
/* harmony import */ var react_icons_bs__WEBPACK_IMPORTED_MODULE_26___default = /*#__PURE__*/__webpack_require__.n(react_icons_bs__WEBPACK_IMPORTED_MODULE_26__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27__);

var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/customizations/components/theme/App/App.jsx";

function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); if (enumerableOnly) { symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; }); } keys.push.apply(keys, symbols); } return keys; }

function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i] != null ? arguments[i] : {}; if (i % 2) { ownKeys(Object(source), true).forEach(function (key) { _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(target, key, source[key]); }); } else if (Object.getOwnPropertyDescriptors) { Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)); } else { ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } } return target; }

/**
 * App container.
 * @module components/theme/App/App
 */



























/**
 * @export
 * @class App
 * @extends {Component}
 */




class App extends react__WEBPACK_IMPORTED_MODULE_1__["Component"] {
  constructor(...args) {
    super(...args);

    _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(this, "state", {
      hasError: false,
      error: null,
      errorInfo: null
    });
  }

  /**
   * @method componentWillReceiveProps
   * @param {Object} nextProps Next properties
   * @returns {undefined}
   */
  UNSAFE_componentWillReceiveProps(nextProps) {
    if (nextProps.pathname !== this.props.pathname) {
      if (this.state.hasError) {
        this.setState({
          hasError: false
        });
      }
    }
  }
  /**
   * ComponentDidCatch
   * @method ComponentDidCatch
   * @param {string} error  The error
   * @param {string} info The info
   * @returns {undefined}
   */


  componentDidCatch(error, info) {
    this.setState({
      hasError: true,
      error,
      errorInfo: info
    });

    if (false) { var _window, _window$env, _SENTRY__; }
  }
  /**
   * Render method.
   * @method render
   * @returns {string} Markup for the component.
   */


  render() {
    var _this$props$content, _this$props$content$l;

    const {
      views
    } = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_14__["default"];
    const path = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["getBaseUrl"])(this.props.pathname);
    const action = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["getView"])(this.props.pathname);
    const isCmsUI = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["isCmsUi"])(this.props.pathname);
    const ConnectionRefusedView = views.errorViews.ECONNREFUSED;
    const menuItems = this.props.content; // const language =
    //   this.props.content?.language?.token ?? this.props.intl?.locale;

    return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27__["jsxs"])(_plone_volto_components_manage_Pluggable__WEBPACK_IMPORTED_MODULE_15__["PluggablesProvider"], {
      children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27__["jsx"])(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["BodyClass"], {
        className: `view-${action}view`
      }), this.props.content && this.props.content['@type'] && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27__["jsx"])(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["BodyClass"], {
        className: `contenttype-${this.props.content['@type'].replace(' ', '-').toLowerCase()}`
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27__["jsx"])(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["BodyClass"], {
        className: classnames__WEBPACK_IMPORTED_MODULE_13___default()({
          [lodash_trim__WEBPACK_IMPORTED_MODULE_12___default()(lodash_join__WEBPACK_IMPORTED_MODULE_11___default()(lodash_split__WEBPACK_IMPORTED_MODULE_10___default()(this.props.pathname, '/'), ' section-'))]: this.props.pathname !== '/',
          siteroot: this.props.pathname === '/',
          'is-authenticated': !!this.props.token,
          'is-anonymous': !this.props.token,
          'cms-ui': isCmsUI,
          'public-ui': !isCmsUI
        })
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27__["jsx"])(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["BodyClass"], {
        className: this.props.content != null ? this.props.content['@type'] == 'Folder' || this.props.content['@type'] == 'jaarverslag' ? this.props.content.Hide_Footer != undefined ? 'invisible' : '' : '' : ''
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_19__["SkipLinks"], {}), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_19__["Header"], {
        pathname: path,
        menuItems: menuItems
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27__["jsx"])(_plone_volto_components_theme_MultilingualRedirector_MultilingualRedirector__WEBPACK_IMPORTED_MODULE_22__["default"], {
        pathname: this.props.pathname,
        contentLanguage: (_this$props$content = this.props.content) === null || _this$props$content === void 0 ? void 0 : (_this$props$content$l = _this$props$content.language) === null || _this$props$content$l === void 0 ? void 0 : _this$props$content$l.token,
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_7__["Segment"], {
          basic: true,
          className: "content-area",
          children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27__["jsxs"])("main", {
            children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_19__["OutdatedBrowser"], {}), this.props.connectionRefused ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27__["jsx"])(ConnectionRefusedView, {}) : this.state.hasError ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27__["jsx"])(_plone_volto_error__WEBPACK_IMPORTED_MODULE_18__["default"], {
              message: this.state.error.message,
              stackTrace: this.state.errorInfo.componentStack
            }) : Object(react_router_config__WEBPACK_IMPORTED_MODULE_8__["renderRoutes"])(this.props.route.routes, {
              staticContext: this.props.staticContext
            })]
          })
        })
      }), this.props.content != undefined ? this.props.content['@type'] == 'Folder' || this.props.content['@type'] == 'jaarverslag' ? this.props.content.Hide_Footer === null || undefined ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_19__["Footer"], {}) : '' : /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_19__["Footer"], {}) : '', /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27__["jsx"])(_plone_volto_components_manage_LockingToastsFactory_LockingToastsFactory__WEBPACK_IMPORTED_MODULE_24__["default"], {
        content: this.props.content,
        user: this.props.userId
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27__["jsx"])(_plone_volto_components_manage_WorkingCopyToastsFactory_WorkingCopyToastsFactory__WEBPACK_IMPORTED_MODULE_23__["default"], {
        content: this.props.content
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27__["jsx"])(react_toastify__WEBPACK_IMPORTED_MODULE_9__["ToastContainer"], {
        position: react_toastify__WEBPACK_IMPORTED_MODULE_9__["toast"].POSITION.BOTTOM_CENTER,
        hideProgressBar: true,
        transition: react_toastify__WEBPACK_IMPORTED_MODULE_9__["Slide"],
        autoClose: 5000,
        closeButton: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_19__["Icon"], {
          className: "toast-dismiss-action",
          name: _plone_volto_icons_clear_svg__WEBPACK_IMPORTED_MODULE_21___default.a,
          size: "18px"
        })
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_27__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_19__["AppExtras"], _objectSpread({}, this.props))]
    });
  }

}

_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(App, "propTypes", {
  pathname: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.string.isRequired
});

const __test__ = Object(react_redux__WEBPACK_IMPORTED_MODULE_4__["connect"])((state, props) => ({
  pathname: props.location.pathname,
  token: state.userSession.token,
  content: state.content.data,
  apiError: state.apierror.error,
  connectionRefused: state.apierror.connectionRefused
}), {})(App);
const fetchContent = async ({
  store,
  location
}) => {
  const content = await store.dispatch(Object(_plone_volto_actions__WEBPACK_IMPORTED_MODULE_20__["getContent"])(Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["getBaseUrl"])(location.pathname)));
  const promises = [];
  const {
    blocksConfig
  } = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_14__["default"].blocks;

  const visitor = ([id, data]) => {
    const blockType = data['@type'];
    const {
      getAsyncData
    } = blocksConfig[blockType];

    if (getAsyncData) {
      const p = getAsyncData({
        store,
        dispatch: store.dispatch,
        path: location.pathname,
        location,
        id,
        data
      });

      if (!(p !== null && p !== void 0 && p.length)) {
        throw new _plone_volto_error__WEBPACK_IMPORTED_MODULE_18__["default"]('You should return a list of promises from getAsyncData');
      }

      promises.push(...p);
    }
  };

  Object(_plone_volto_helpers_Blocks_Blocks__WEBPACK_IMPORTED_MODULE_16__["visitBlocks"])(content, visitor);
  await Promise.allSettled(promises);
  return content;
};
/* harmony default export */ __webpack_exports__["default"] = (Object(redux__WEBPACK_IMPORTED_MODULE_5__["compose"])(Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["asyncConnect"])([{
  key: 'breadcrumbs',
  promise: ({
    location,
    store: {
      dispatch
    }
  }) =>  true && dispatch(Object(_plone_volto_actions__WEBPACK_IMPORTED_MODULE_20__["getBreadcrumbs"])(Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["getBaseUrl"])(location.pathname)))
}, {
  key: 'content',
  promise: ({
    location,
    store
  }) =>  true && fetchContent({
    store,
    location
  })
}, {
  key: 'navigation',
  promise: ({
    location,
    store: {
      dispatch
    }
  }) =>  true && dispatch(Object(_plone_volto_actions__WEBPACK_IMPORTED_MODULE_20__["getNavigation"])(Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["getBaseUrl"])(location.pathname), _plone_volto_registry__WEBPACK_IMPORTED_MODULE_14__["default"].settings.navDepth))
}, {
  key: 'types',
  promise: ({
    location,
    store: {
      dispatch
    }
  }) =>  true && dispatch(Object(_plone_volto_actions__WEBPACK_IMPORTED_MODULE_20__["getTypes"])(Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["getBaseUrl"])(location.pathname)))
}, {
  key: 'workflow',
  promise: ({
    location,
    store: {
      dispatch
    }
  }) =>  true && dispatch(Object(_plone_volto_actions__WEBPACK_IMPORTED_MODULE_20__["getWorkflow"])(Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["getBaseUrl"])(location.pathname)))
}]), react_intl__WEBPACK_IMPORTED_MODULE_17__["injectIntl"], Object(react_redux__WEBPACK_IMPORTED_MODULE_4__["connect"])((state, props) => ({
  pathname: props.location.pathname,
  token: state.userSession.token,
  userId: state.userSession.token ? jwt_decode__WEBPACK_IMPORTED_MODULE_2___default()(state.userSession.token).sub : '',
  content: state.content.data,
  apiError: state.apierror.error,
  connectionRefused: state.apierror.connectionRefused
}), null))(App));

/***/ })

};
//# sourceMappingURL=server.08e4a5f46cbd34fa9b48.hot-update.js.map