exports.id = "server";
exports.modules = {

/***/ "./node_modules/@plone/volto/src/components/manage/LockingToastsFactory/LockingToastsFactory.jsx":
/*!*******************************************************************************************************!*\
  !*** ./node_modules/@plone/volto/src/components/manage/LockingToastsFactory/LockingToastsFactory.jsx ***!
  \*******************************************************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_toastify__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react-toastify */ "react-toastify");
/* harmony import */ var react_toastify__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react_toastify__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react-redux */ "react-redux");
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(react_redux__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-router-dom */ "react-router-dom");
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react_router_dom__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react-intl */ "react-intl");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react_intl__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var date_fns__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! date-fns */ "date-fns");
/* harmony import */ var date_fns__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(date_fns__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var use_deep_compare_effect__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! use-deep-compare-effect */ "use-deep-compare-effect");
/* harmony import */ var use_deep_compare_effect__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(use_deep_compare_effect__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_8__);
var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/node_modules/@plone/volto/src/components/manage/LockingToastsFactory/LockingToastsFactory.jsx";
 // import { Link } from 'react-router-dom';





 // import { flattenToAppURL } from '@plone/volto/helpers';




const messages = Object(react_intl__WEBPACK_IMPORTED_MODULE_4__["defineMessages"])({
  thisItemIsLocked: {
    "id": "This item was locked by {creator} on {date}",
    "defaultMessage": "This item was locked by {creator} on {date}"
  },
  unlockItem: {
    "id": "If you are certain this user has abandoned the object, you may unlock the object. You will then be able to edit it.",
    "defaultMessage": "If you are certain this user has abandoned the object, you may unlock the object. You will then be able to edit it."
  }
});

const LockingToastsFactory = props => {
  const intl = Object(react_intl__WEBPACK_IMPORTED_MODULE_4__["useIntl"])();
  const pathname = Object(react_router_dom__WEBPACK_IMPORTED_MODULE_3__["useLocation"])().pathname;
  const lang = Object(react_redux__WEBPACK_IMPORTED_MODULE_2__["useSelector"])(state => state.intl.locale);
  const {
    content,
    user
  } = props;
  const lock = content === null || content === void 0 ? void 0 : content.lock;
  const creator = (lock === null || lock === void 0 ? void 0 : lock.creator_name) || (lock === null || lock === void 0 ? void 0 : lock.creator) || ''; // const creator_url = locking?.creator_url || '';

  const date = (lock === null || lock === void 0 ? void 0 : lock.created) || '';
  const dateOptions = {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: 'numeric',
    minute: 'numeric'
  };
  use_deep_compare_effect__WEBPACK_IMPORTED_MODULE_7___default()(() => {
    if (user && content) {
      if (lock !== null && lock !== void 0 && lock.locked && lock !== null && lock !== void 0 && lock.stealable && (lock === null || lock === void 0 ? void 0 : lock.creator) !== user) {
        if (react_toastify__WEBPACK_IMPORTED_MODULE_1__["toast"].isActive('lockinginfo')) {
          react_toastify__WEBPACK_IMPORTED_MODULE_1__["toast"].update('lockinginfo', {
            render: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_8__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_5__["Toast"], {
              info: true,
              title: intl.formatMessage(messages.thisItemIsLocked, {
                creator: creator,
                date: new Intl.DateTimeFormat(lang, dateOptions).format(Object(date_fns__WEBPACK_IMPORTED_MODULE_6__["parse"])(date))
              }),
              content: intl.formatMessage(messages.unlockItem, {})
            })
          });
        } else {
          react_toastify__WEBPACK_IMPORTED_MODULE_1__["toast"].info( /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_8__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_5__["Toast"], {
            info: true,
            title: intl.formatMessage(messages.thisItemIsLocked, {
              creator: creator,
              date: new Intl.DateTimeFormat(lang, dateOptions).format(Object(date_fns__WEBPACK_IMPORTED_MODULE_6__["parse"])(date))
            }),
            content: intl.formatMessage(messages.unlockItem, {})
          }), {
            toastId: 'lockinginfo',
            autoClose: false,
            closeButton: false,
            transition: null
          });
        }
      } else {
        if (react_toastify__WEBPACK_IMPORTED_MODULE_1__["toast"].isActive('lockinginfo')) {
          react_toastify__WEBPACK_IMPORTED_MODULE_1__["toast"].dismiss('lockinginfo');
        }
      }
    }
  }, [content, creator, date, dateOptions, intl, lang, lock, pathname, user]);
  return null;
};

/* harmony default export */ __webpack_exports__["default"] = (LockingToastsFactory);

/***/ }),

/***/ "./node_modules/@plone/volto/src/components/manage/WorkingCopyToastsFactory/WorkingCopyToastsFactory.jsx":
/*!***************************************************************************************************************!*\
  !*** ./node_modules/@plone/volto/src/components/manage/WorkingCopyToastsFactory/WorkingCopyToastsFactory.jsx ***!
  \***************************************************************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react-router-dom */ "react-router-dom");
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react_router_dom__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var react_toastify__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react-toastify */ "react-toastify");
/* harmony import */ var react_toastify__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(react_toastify__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-redux */ "react-redux");
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react_redux__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react-intl */ "react-intl");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react_intl__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var date_fns__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! date-fns */ "date-fns");
/* harmony import */ var date_fns__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(date_fns__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _plone_volto_registry__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @plone/volto/registry */ "./node_modules/@plone/volto/src/registry.js");
/* harmony import */ var use_deep_compare_effect__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! use-deep-compare-effect */ "use-deep-compare-effect");
/* harmony import */ var use_deep_compare_effect__WEBPACK_IMPORTED_MODULE_9___default = /*#__PURE__*/__webpack_require__.n(use_deep_compare_effect__WEBPACK_IMPORTED_MODULE_9__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__);
var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/node_modules/@plone/volto/src/components/manage/WorkingCopyToastsFactory/WorkingCopyToastsFactory.jsx";












const messages = Object(react_intl__WEBPACK_IMPORTED_MODULE_4__["defineMessages"])({
  thisIsAWorkingCopyOf: {
    "id": "This is a working copy of {title}",
    "defaultMessage": "This is a working copy of {title}"
  },
  workingCopyIs: {
    "id": "This has an ongoing working copy in {title}",
    "defaultMessage": "This has an ongoing working copy in {title}"
  },
  workingCopyCreatedBy: {
    "id": "Created by {creator} on {date}",
    "defaultMessage": "Created by {creator} on {date}"
  }
});

const WorkingCopyToastsFactory = props => {
  const intl = Object(react_intl__WEBPACK_IMPORTED_MODULE_4__["useIntl"])();
  const pathname = Object(react_router_dom__WEBPACK_IMPORTED_MODULE_1__["useLocation"])().pathname;
  const lang = Object(react_redux__WEBPACK_IMPORTED_MODULE_3__["useSelector"])(state => state.intl.locale);
  const {
    content
  } = props;
  const title = content === null || content === void 0 ? void 0 : content.title;
  const working_copy = content === null || content === void 0 ? void 0 : content.working_copy;
  const dateOptions = {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  };
  use_deep_compare_effect__WEBPACK_IMPORTED_MODULE_9___default()(() => {
    if (content && _plone_volto_registry__WEBPACK_IMPORTED_MODULE_8__["default"].settings.hasWorkingCopySupport) {
      if (working_copy) {
        let toastMessage, toastTitle;

        if (content.working_copy_of) {
          var _content$working_copy;

          // I'm a working copy
          toastMessage = messages.thisIsAWorkingCopyOf;
          toastTitle = /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])(react_router_dom__WEBPACK_IMPORTED_MODULE_1__["Link"], {
            to: Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["flattenToAppURL"])(content.working_copy_of['@id']),
            children: (_content$working_copy = content.working_copy_of) === null || _content$working_copy === void 0 ? void 0 : _content$working_copy.title
          });
        } else {
          // I'm a baseline
          toastMessage = messages.workingCopyIs;
          toastTitle = /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])(react_router_dom__WEBPACK_IMPORTED_MODULE_1__["Link"], {
            to: Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["flattenToAppURL"])(working_copy['@id']),
            children: working_copy === null || working_copy === void 0 ? void 0 : working_copy.title
          });
        }

        if (react_toastify__WEBPACK_IMPORTED_MODULE_2__["toast"].isActive('workingcopyinfo')) {
          react_toastify__WEBPACK_IMPORTED_MODULE_2__["toast"].update('workingcopyinfo', {
            render: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_5__["Toast"], {
              info: true,
              title: intl.formatMessage(toastMessage, {
                title: toastTitle
              }),
              content: intl.formatMessage(messages.workingCopyCreatedBy, {
                creator: working_copy === null || working_copy === void 0 ? void 0 : working_copy.creator_name,
                date: new Intl.DateTimeFormat(lang, dateOptions).format(Object(date_fns__WEBPACK_IMPORTED_MODULE_7__["parse"])(working_copy === null || working_copy === void 0 ? void 0 : working_copy.created))
              })
            })
          });
        } else {
          react_toastify__WEBPACK_IMPORTED_MODULE_2__["toast"].info( /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_5__["Toast"], {
            info: true,
            title: intl.formatMessage(toastMessage, {
              title: toastTitle
            }),
            content: intl.formatMessage(messages.workingCopyCreatedBy, {
              creator: working_copy === null || working_copy === void 0 ? void 0 : working_copy.creator_name,
              date: new Intl.DateTimeFormat(lang, dateOptions).format(Object(date_fns__WEBPACK_IMPORTED_MODULE_7__["parse"])(working_copy === null || working_copy === void 0 ? void 0 : working_copy.created))
            })
          }), {
            toastId: 'workingcopyinfo',
            autoClose: false,
            closeButton: false,
            transition: null
          });
        }
      }

      if (!working_copy) {
        if (react_toastify__WEBPACK_IMPORTED_MODULE_2__["toast"].isActive('workingcopyinfo')) {
          react_toastify__WEBPACK_IMPORTED_MODULE_2__["toast"].dismiss('workingcopyinfo');
        }
      }
    }
  }, [pathname, content, title, working_copy, intl, lang, dateOptions]);
  return null;
};

/* harmony default export */ __webpack_exports__["default"] = (WorkingCopyToastsFactory);

/***/ }),

/***/ "./node_modules/@plone/volto/src/components/theme/MultilingualRedirector/MultilingualRedirector.jsx":
/*!**********************************************************************************************************!*\
  !*** ./node_modules/@plone/volto/src/components/theme/MultilingualRedirector/MultilingualRedirector.jsx ***!
  \**********************************************************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react-router-dom */ "react-router-dom");
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react_router_dom__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react-redux */ "react-redux");
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(react_redux__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react_cookie__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-cookie */ "react-cookie");
/* harmony import */ var react_cookie__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react_cookie__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _plone_volto_registry__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @plone/volto/registry */ "./node_modules/@plone/volto/src/registry.js");
/* harmony import */ var _plone_volto_actions__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @plone/volto/actions */ "./node_modules/@plone/volto/src/actions/index.js");
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__);
var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/node_modules/@plone/volto/src/components/theme/MultilingualRedirector/MultilingualRedirector.jsx";










const MultilingualRedirector = props => {
  const {
    settings
  } = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_4__["default"];
  const {
    pathname,
    children
  } = props;
  const [cookies] = Object(react_cookie__WEBPACK_IMPORTED_MODULE_3__["useCookies"])();
  const currentLanguage = cookies['I18N_LANGUAGE'] || settings.defaultLanguage;
  const redirectToLanguage = settings.supportedLanguages.includes(currentLanguage) ? currentLanguage : settings.defaultLanguage;
  const dispatch = Object(react_redux__WEBPACK_IMPORTED_MODULE_2__["useDispatch"])();
  react__WEBPACK_IMPORTED_MODULE_0___default.a.useEffect(() => {
    // ToDo: Add means to support language negotiation (with config)
    // const detectedLang = (navigator.language || navigator.userLanguage).substring(0, 2);
    let mounted = true;

    if (settings.isMultilingual && pathname === '/') {
      const langFileName = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["normalizeLanguageName"])(redirectToLanguage);
      __webpack_require__("./locales lazy recursive ^\\.\\/.*\\.json$")("./" + langFileName + ".json").then(locale => {
        if (mounted) {
          dispatch(Object(_plone_volto_actions__WEBPACK_IMPORTED_MODULE_5__["changeLanguage"])(redirectToLanguage, locale.default));
        }
      });
    }

    return () => {
      mounted = false;
    };
  }, [pathname, dispatch, redirectToLanguage, settings.isMultilingual]);
  return pathname === '/' && settings.isMultilingual ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])(react_router_dom__WEBPACK_IMPORTED_MODULE_1__["Redirect"], {
    to: `/${redirectToLanguage}`
  }) : /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["Fragment"], {
    children: children
  });
};

/* harmony default export */ __webpack_exports__["default"] = (MultilingualRedirector);

/***/ }),

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
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__);

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
  } // {pagetype == "Jaarverslag Folder" ? console.log("yes"): console.log("no")};
  // This is for choosing the page type and make the footer disappear
  // {document.getElementById('field-Page_Type').childNodes[1].children[0].children[0].children[0].firstChild.wholeText === 'Jaarverslag Folder' ? "yes" : "no"}
  // document.getElementById('field-Page_Type').childNodes[1].children[0].children[0].children[0].firstChild.wholeText
  // (document.getElementById('footer').className = 'invisibleFooter') : (document.getElementById('footer').className = 'visibleFooter');

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

    const pagetype = () => {
      try {
        return document.getElementById('field-Page_Type').childNodes[1].children[0].children[0].children[0].firstChild.wholeText;
      } catch (e) {}
    };

    {
      console.log(pagetype());
    } // const language =
    //   this.props.content?.language?.token ?? this.props.intl?.locale;

    return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsxs"])(_plone_volto_components_manage_Pluggable__WEBPACK_IMPORTED_MODULE_15__["PluggablesProvider"], {
      children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["BodyClass"], {
        className: `view-${action}view`
      }), this.props.content && this.props.content['@type'] && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["BodyClass"], {
        className: `contenttype-${this.props.content['@type'].replace(' ', '-').toLowerCase()}`
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["BodyClass"], {
        className: classnames__WEBPACK_IMPORTED_MODULE_13___default()({
          [lodash_trim__WEBPACK_IMPORTED_MODULE_12___default()(lodash_join__WEBPACK_IMPORTED_MODULE_11___default()(lodash_split__WEBPACK_IMPORTED_MODULE_10___default()(this.props.pathname, '/'), ' section-'))]: this.props.pathname !== '/',
          siteroot: this.props.pathname === '/',
          'is-authenticated': !!this.props.token,
          'is-anonymous': !this.props.token,
          'cms-ui': isCmsUI,
          'public-ui': !isCmsUI
        })
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_19__["SkipLinks"], {}), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_19__["Header"], {
        pathname: path
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_components_theme_MultilingualRedirector_MultilingualRedirector__WEBPACK_IMPORTED_MODULE_22__["default"], {
        pathname: this.props.pathname,
        contentLanguage: (_this$props$content = this.props.content) === null || _this$props$content === void 0 ? void 0 : (_this$props$content$l = _this$props$content.language) === null || _this$props$content$l === void 0 ? void 0 : _this$props$content$l.token,
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_7__["Segment"], {
          basic: true,
          className: "content-area",
          children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsxs"])("main", {
            children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_19__["OutdatedBrowser"], {}), this.props.connectionRefused ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(ConnectionRefusedView, {}) : this.state.hasError ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_error__WEBPACK_IMPORTED_MODULE_18__["default"], {
              message: this.state.error.message,
              stackTrace: this.state.errorInfo.componentStack
            }) : Object(react_router_config__WEBPACK_IMPORTED_MODULE_8__["renderRoutes"])(this.props.route.routes, {
              staticContext: this.props.staticContext
            })]
          })
        })
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_19__["Footer"], {}), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_components_manage_LockingToastsFactory_LockingToastsFactory__WEBPACK_IMPORTED_MODULE_24__["default"], {
        content: this.props.content,
        user: this.props.userId
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_components_manage_WorkingCopyToastsFactory_WorkingCopyToastsFactory__WEBPACK_IMPORTED_MODULE_23__["default"], {
        content: this.props.content
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(react_toastify__WEBPACK_IMPORTED_MODULE_9__["ToastContainer"], {
        position: react_toastify__WEBPACK_IMPORTED_MODULE_9__["toast"].POSITION.BOTTOM_CENTER,
        hideProgressBar: true,
        transition: react_toastify__WEBPACK_IMPORTED_MODULE_9__["Slide"],
        autoClose: 5000,
        closeButton: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_19__["Icon"], {
          className: "toast-dismiss-action",
          name: _plone_volto_icons_clear_svg__WEBPACK_IMPORTED_MODULE_21___default.a,
          size: "18px"
        })
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_19__["AppExtras"], _objectSpread({}, this.props))]
    });
  }

}

_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(App, "propTypes", {
  pathname: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.string.isRequired,
  pagetype: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.string.isRequired
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

/***/ }),

/***/ "@sentry/browser":
/*!**********************************!*\
  !*** external "@sentry/browser" ***!
  \**********************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = require("@sentry/browser");

/***/ }),

/***/ "lodash/trim":
/*!******************************!*\
  !*** external "lodash/trim" ***!
  \******************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = require("lodash/trim");

/***/ })

};
//# sourceMappingURL=server.48ac0238050008cffa21.hot-update.js.map