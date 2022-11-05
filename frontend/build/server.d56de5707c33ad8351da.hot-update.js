exports.id = "server";
exports.modules = {

/***/ "./src/components/Blocks/PhotoDescription/Siderbar.jsx":
/*!*************************************************************!*\
  !*** ./src/components/Blocks/PhotoDescription/Siderbar.jsx ***!
  \*************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/defineProperty */ "@babel/runtime/helpers/defineProperty");
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var _BlockSchema__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./BlockSchema */ "./src/components/Blocks/PhotoDescription/BlockSchema.js");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__);

var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/components/Blocks/PhotoDescription/Siderbar.jsx";

function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); if (enumerableOnly) { symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; }); } keys.push.apply(keys, symbols); } return keys; }

function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i] != null ? arguments[i] : {}; if (i % 2) { ownKeys(Object(source), true).forEach(function (key) { _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(target, key, source[key]); }); } else if (Object.getOwnPropertyDescriptors) { Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)); } else { ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } } return target; }






const BannerAreaBlockSidebar = props => {
  const {
    data,
    block,
    onChangeBlock,
    selected
  } = props;
  const schema = bannerAreaBlockSchema();
  return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_2__["SidebarPortal"], {
    selected: selected,
    children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_2__["BlockDataForm"], {
      schema: schema,
      title: schema.title,
      onChangeField: (id, value) => {
        onChangeBlock(block, _objectSpread(_objectSpread({}, data), {}, {
          [id]: value
        }));
      },
      formData: data,
      fieldIndex: data.index,
      block: block
    })
  });
};

/* harmony default export */ __webpack_exports__["default"] = (Sidebar);

/***/ })

};
//# sourceMappingURL=server.d56de5707c33ad8351da.hot-update.js.map