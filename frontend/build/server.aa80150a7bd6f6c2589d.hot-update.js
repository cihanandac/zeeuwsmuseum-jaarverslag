exports.id = "server";
exports.modules = {

/***/ "./node_modules/@plone/volto/src/icons/open.svg":
/*!******************************************************!*\
  !*** ./node_modules/@plone/volto/src/icons/open.svg ***!
  \******************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = {"attributes":{"xmlns":"http://www.w3.org/2000/svg","width":"36","height":"36","viewBox":"0 0 36 36"},"content":"<path fill-rule=\"evenodd\" d=\"M3.1161,5.0001 L4.1161,21.0001 L3.0001,21.0001 L4.3341,29.0001 L32.0281,29.0001 L33.3611,21.0001 L32.2671,21.0001 L33.2681,9.0001 L17.5941,9.0001 L13.5951,5.0001 L3.1161,5.0001 Z M5.2451,7.0001 L12.7671,7.0001 L16.7661,11.0001 L31.0931,11.0001 L30.2611,21.0001 L6.1201,21.0001 L5.2451,7.0001 Z M5.3611,23.0001 L31.0001,23.0001 L30.3341,27.0001 L6.0271,27.0001 L5.3611,23.0001 Z\"/>"}

/***/ }),

/***/ "./src/customizations/components/theme/View/AlbumView.jsx":
/*!****************************************************************!*\
  !*** ./src/customizations/components/theme/View/AlbumView.jsx ***!
  \****************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! prop-types */ "prop-types");
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(prop_types__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! semantic-ui-react */ "semantic-ui-react");
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var _plone_volto_icons_open_svg__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @plone/volto/icons/open.svg */ "./node_modules/@plone/volto/src/icons/open.svg");
/* harmony import */ var _plone_volto_icons_open_svg__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_open_svg__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _plone_volto_icons_ahead_svg__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @plone/volto/icons/ahead.svg */ "./node_modules/@plone/volto/src/icons/ahead.svg");
/* harmony import */ var _plone_volto_icons_ahead_svg__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_ahead_svg__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _plone_volto_icons_back_svg__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @plone/volto/icons/back.svg */ "./node_modules/@plone/volto/src/icons/back.svg");
/* harmony import */ var _plone_volto_icons_back_svg__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_back_svg__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_8__);
var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/customizations/components/theme/View/AlbumView.jsx";

/**
 * Album view component.
 * @module components/theme/View/AlbumView
 */









/**
 * Album view component class.
 * @function AlbumView
 * @param {Object} content Content object.
 * @returns {string} Markup of the component.
 */



class AlbumView extends react__WEBPACK_IMPORTED_MODULE_0__["Component"] {
  constructor(props) {
    super(props);
    this.state = {
      openIndex: undefined
    };
    this.closeModal = this.closeModal.bind(this);
    this.nextImage = this.nextImage.bind(this);
    this.prevImage = this.prevImage.bind(this);
  }

  closeModal() {
    this.setState({
      openIndex: -1
    });
  }

  nextImage() {
    const openIndex = (this.state.openIndex + 1) % this.props.content.items.length;
    this.setState({
      openIndex
    });
  }

  prevImage() {
    const openIndex = (this.state.openIndex - 1) % this.props.content.items.length;
    this.setState({
      openIndex
    });
  }

  render() {
    const {
      content
    } = this.props;
    return Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_7__["hasBlocksData"])(content) ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_8__["jsx"])(CustomTag, {
      children: map(content[blocksLayoutFieldname].items, block => {
        var _blocksConfig$content, _content$blocksFieldn, _content$blocksFieldn2, _location, _content$blocksFieldn3, _content$blocksFieldn4;

        const Block = (_blocksConfig$content = blocksConfig[(_content$blocksFieldn = content[blocksFieldname]) === null || _content$blocksFieldn === void 0 ? void 0 : (_content$blocksFieldn2 = _content$blocksFieldn[block]) === null || _content$blocksFieldn2 === void 0 ? void 0 : _content$blocksFieldn2['@type']]) === null || _blocksConfig$content === void 0 ? void 0 : _blocksConfig$content.view;
        const blockData = applyBlockDefaults({
          data: content[blocksFieldname][block],
          intl,
          metadata,
          properties: content
        });
        return Block ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_8__["jsx"])(Block, {
          id: block,
          metadata: metadata,
          properties: content,
          data: blockData,
          path: getBaseUrl(((_location = location) === null || _location === void 0 ? void 0 : _location.pathname) || ''),
          blocksConfig: blocksConfig
        }, block) : /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_8__["jsx"])("div", {
          children: intl.formatMessage(messages.unknownBlock, {
            block: (_content$blocksFieldn3 = content[blocksFieldname]) === null || _content$blocksFieldn3 === void 0 ? void 0 : (_content$blocksFieldn4 = _content$blocksFieldn3[block]) === null || _content$blocksFieldn4 === void 0 ? void 0 : _content$blocksFieldn4['@type']
          })
        }, block);
      })
    }) : '';
  }

}
/**
 * Property types.
 * @property {Object} propTypes Property types.
 * @static
 */


AlbumView.propTypes = {
  /**
   * Content of the object
   */
  content: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.shape({
    /**
     * Title of the object
     */
    title: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,

    /**
     * Description of the object
     */
    description: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,

    /**
     * Child items of the object
     */
    items: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.arrayOf(prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.shape({
      /**
       * Title of the item
       */
      title: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,

      /**
       * Description of the item
       */
      description: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,

      /**
       * Url of the item
       */
      url: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,

      /**
       * Image of the item
       */
      image: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.object,

      /**
       * Image caption of the item
       */
      image_caption: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,

      /**
       * Type of the item
       */
      '@type': prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string
    }))
  }).isRequired
};
/* harmony default export */ __webpack_exports__["default"] = (AlbumView);

/***/ })

};
//# sourceMappingURL=server.aa80150a7bd6f6c2589d.hot-update.js.map