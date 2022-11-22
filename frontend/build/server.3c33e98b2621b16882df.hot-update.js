exports.id = "server";
exports.modules = {

/***/ "./src/customizations/components/theme/View/DefaultView.jsx":
/*!******************************************************************!*\
  !*** ./src/customizations/components/theme/View/DefaultView.jsx ***!
  \******************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var lodash_map__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! lodash/map */ "lodash/map");
/* harmony import */ var lodash_map__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(lodash_map__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! prop-types */ "prop-types");
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(prop_types__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-intl */ "react-intl");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react_intl__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! semantic-ui-react */ "semantic-ui-react");
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(semantic_ui_react__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _plone_volto_registry__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @plone/volto/registry */ "./node_modules/@plone/volto/src/registry.js");
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var moment__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! moment */ "moment");
/* harmony import */ var moment__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(moment__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__);

var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/customizations/components/theme/View/DefaultView.jsx";

/**
 * Document view component.
 * @module components/theme/View/DefaultView
 */










const messages = Object(react_intl__WEBPACK_IMPORTED_MODULE_3__["defineMessages"])({
  unknownBlock: {
    "id": "Unknown Block",
    "defaultMessage": "Unknown Block {block}"
  }
});
/**
 * Component to display the default view.
 * @function DefaultView
 * @param {Object} content Content object.
 * @returns {string} Markup of the component.
 */

const DefaultView = ({
  content,
  intl,
  location
}) => {
  const blocksFieldname = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_8__["getBlocksFieldname"])(content);
  const blocksLayoutFieldname = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_8__["getBlocksLayoutFieldname"])(content);
  return Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_8__["hasBlocksData"])(content) ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsxs"])("div", {
    id: "page-document",
    className: "ui container",
    children: [content.review_state === 'published' && content.effective && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("p", {
      children: moment__WEBPACK_IMPORTED_MODULE_7___default()(content.effective).format('d:m:yy')
    }), lodash_map__WEBPACK_IMPORTED_MODULE_0___default()(content[blocksLayoutFieldname].items, block => {
      var _config$blocks$blocks, _content$blocksFieldn, _content$blocksFieldn2, _content$blocksFieldn3, _content$blocksFieldn4;

      const Block = ((_config$blocks$blocks = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_5__["default"].blocks.blocksConfig[(_content$blocksFieldn = content[blocksFieldname]) === null || _content$blocksFieldn === void 0 ? void 0 : (_content$blocksFieldn2 = _content$blocksFieldn[block]) === null || _content$blocksFieldn2 === void 0 ? void 0 : _content$blocksFieldn2['@type']]) === null || _config$blocks$blocks === void 0 ? void 0 : _config$blocks$blocks['view']) || null;
      return Block !== null ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])(Block, {
        id: block,
        properties: content,
        data: content[blocksFieldname][block],
        path: Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_8__["getBaseUrl"])((location === null || location === void 0 ? void 0 : location.pathname) || '')
      }, block) : /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("div", {
        children: intl.formatMessage(messages.unknownBlock, {
          block: (_content$blocksFieldn3 = content[blocksFieldname]) === null || _content$blocksFieldn3 === void 0 ? void 0 : (_content$blocksFieldn4 = _content$blocksFieldn3[block]) === null || _content$blocksFieldn4 === void 0 ? void 0 : _content$blocksFieldn4['@type']
        })
      }, block);
    })]
  }) : /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_4__["Container"], {
    id: "page-document",
    children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("h1", {
      className: "documentFirstHeading",
      children: content.title
    }), content.description && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("p", {
      className: "documentDescription",
      children: content.description
    }), content.image && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_4__["Image"], {
      className: "document-image",
      src: content.image.scales.thumb.download,
      floated: "right"
    }), content.remoteUrl && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsxs"])("span", {
      children: ["The link address is:", /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("a", {
        href: content.remoteUrl,
        children: content.remoteUrl
      })]
    }), content.text && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("div", {
      dangerouslySetInnerHTML: {
        __html: content.text.data
      }
    })]
  });
};
/**
 * Property types.
 * @property {Object} propTypes Property types.
 * @static
 */


DefaultView.propTypes = {
  /**
   * Content of the object
   */
  content: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.shape({
    /**
     * Title of the object
     */
    title: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string,

    /**
     * Description of the object
     */
    description: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string,

    /**
     * Text of the object
     */
    text: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.shape({
      /**
       * Data of the text of the object
       */
      data: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string
    })
  }).isRequired
};
/* harmony default export */ __webpack_exports__["default"] = (Object(react_intl__WEBPACK_IMPORTED_MODULE_3__["injectIntl"])(DefaultView));

/***/ })

};
//# sourceMappingURL=server.3c33e98b2621b16882df.hot-update.js.map