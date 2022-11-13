exports.id = "server";
exports.modules = {

/***/ "./src/customizations/components/theme/View/RenderBlocks.jsx":
/*!*******************************************************************!*\
  !*** ./src/customizations/components/theme/View/RenderBlocks.jsx ***!
  \*******************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var lodash_map__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! lodash/map */ "lodash/map");
/* harmony import */ var lodash_map__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(lodash_map__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-intl */ "react-intl");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react_intl__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _plone_volto_registry__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @plone/volto/registry */ "./node_modules/@plone/volto/src/registry.js");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__);

var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/customizations/components/theme/View/RenderBlocks.jsx";






const messages = Object(react_intl__WEBPACK_IMPORTED_MODULE_3__["defineMessages"])({
  unknownBlock: {
    "id": "Unknown Block",
    "defaultMessage": "Unknown Block {block}"
  }
});

const RenderBlocks = props => {
  const {
    location,
    intl,
    content,
    metadata
  } = props;
  const blocksFieldname = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_2__["getBlocksFieldname"])(content);
  const blocksLayoutFieldname = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_2__["getBlocksLayoutFieldname"])(content);
  const blocksConfig = props.blocksConfig || _plone_volto_registry__WEBPACK_IMPORTED_MODULE_4__["default"].blocks.blocksConfig;
  const CustomTag = `${props.as || 'div'}`;
  {
    console.log('yes');
  }
  return Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_2__["hasBlocksData"])(content) ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__["jsx"])(CustomTag, {
    children: lodash_map__WEBPACK_IMPORTED_MODULE_0___default()(content[blocksLayoutFieldname].items, block => {
      var _blocksConfig$content, _content$blocksFieldn, _content$blocksFieldn2, _content$blocksFieldn3, _content$blocksFieldn4;

      const Block = (_blocksConfig$content = blocksConfig[(_content$blocksFieldn = content[blocksFieldname]) === null || _content$blocksFieldn === void 0 ? void 0 : (_content$blocksFieldn2 = _content$blocksFieldn[block]) === null || _content$blocksFieldn2 === void 0 ? void 0 : _content$blocksFieldn2['@type']]) === null || _blocksConfig$content === void 0 ? void 0 : _blocksConfig$content.view;
      const blockData = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_2__["applyBlockDefaults"])({
        data: content[blocksFieldname][block],
        intl,
        metadata,
        properties: content
      });
      return Block ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__["jsx"])(Block, {
        id: block,
        metadata: metadata,
        properties: content,
        data: blockData,
        path: Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_2__["getBaseUrl"])((location === null || location === void 0 ? void 0 : location.pathname) || ''),
        blocksConfig: blocksConfig
      }, block) : /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__["jsx"])("div", {
        children: intl.formatMessage(messages.unknownBlock, {
          block: (_content$blocksFieldn3 = content[blocksFieldname]) === null || _content$blocksFieldn3 === void 0 ? void 0 : (_content$blocksFieldn4 = _content$blocksFieldn3[block]) === null || _content$blocksFieldn4 === void 0 ? void 0 : _content$blocksFieldn4['@type']
        })
      }, block);
    })
  }) : '';
};

/* harmony default export */ __webpack_exports__["default"] = (Object(react_intl__WEBPACK_IMPORTED_MODULE_3__["injectIntl"])(RenderBlocks));

/***/ })

};
//# sourceMappingURL=server.fb952545e5a86abffad9.hot-update.js.map