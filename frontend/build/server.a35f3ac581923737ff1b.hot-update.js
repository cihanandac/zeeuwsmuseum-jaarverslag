exports.id = "server";
exports.modules = {

/***/ "./src/customizations/components/theme/FormattedDate/FormattedDate.jsx":
/*!*****************************************************************************!*\
  !*** ./src/customizations/components/theme/FormattedDate/FormattedDate.jsx ***!
  \*****************************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/defineProperty */ "@babel/runtime/helpers/defineProperty");
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _plone_volto_helpers_Utils_Date__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @plone/volto/helpers/Utils/Date */ "./node_modules/@plone/volto/src/helpers/Utils/Date.js");
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-redux */ "react-redux");
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react_redux__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__);

var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/customizations/components/theme/FormattedDate/FormattedDate.jsx";

function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); if (enumerableOnly) { symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; }); } keys.push.apply(keys, symbols); } return keys; }

function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i] != null ? arguments[i] : {}; if (i % 2) { ownKeys(Object(source), true).forEach(function (key) { _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(target, key, source[key]); }); } else if (Object.getOwnPropertyDescriptors) { Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)); } else { ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } } return target; }




/**
 * Friendly formatting of dates
 */



const FormattedDate = ({
  date,
  format,
  long,
  includeTime,
  relative,
  className,
  locale,
  children
}) => {
  const language = Object(react_redux__WEBPACK_IMPORTED_MODULE_3__["useSelector"])(state => locale || state.intl.locale);

  const toDate = d => typeof d === 'string' ? new Date(d) : d;

  const args = {
    date,
    long,
    includeTime,
    format,
    locale: language
  };
  return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])("time", {
    className: className,
    dateTime: date,
    title: new Intl.DateTimeFormat(language, _plone_volto_helpers_Utils_Date__WEBPACK_IMPORTED_MODULE_2__["long_date_format"]).format(new Date(toDate(date))),
    children: children ? children(Object(_plone_volto_helpers_Utils_Date__WEBPACK_IMPORTED_MODULE_2__["formatDate"])(_objectSpread(_objectSpread({}, args), {}, {
      formatToParts: true
    }))) : Object(_plone_volto_helpers_Utils_Date__WEBPACK_IMPORTED_MODULE_2__["formatDate"])(args)
  });
};

/* harmony default export */ __webpack_exports__["default"] = (FormattedDate);

/***/ })

};
//# sourceMappingURL=server.a35f3ac581923737ff1b.hot-update.js.map