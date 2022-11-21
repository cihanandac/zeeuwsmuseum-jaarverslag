exports.id = "server";
exports.modules = {

/***/ "./node_modules/@plone/volto/src/components/theme/View/RenderBlocks.jsx":
/*!******************************************************************************!*\
  !*** ./node_modules/@plone/volto/src/components/theme/View/RenderBlocks.jsx ***!
  \******************************************************************************/
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

var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/node_modules/@plone/volto/src/components/theme/View/RenderBlocks.jsx";






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

/***/ }),

/***/ "./src/customizations/config/Views.jsx":
/*!*********************************************!*\
  !*** ./src/customizations/config/Views.jsx ***!
  \*********************************************/
/*! exports provided: layoutViews, contentTypesViews, defaultView, errorViews */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "layoutViews", function() { return layoutViews; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "contentTypesViews", function() { return contentTypesViews; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "defaultView", function() { return defaultView; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "errorViews", function() { return errorViews; });
/* harmony import */ var _loadable_component__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @loadable/component */ "@loadable/component");
/* harmony import */ var _loadable_component__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_loadable_component__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _plone_volto_components_theme_View_DefaultView__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @plone/volto/components/theme/View/DefaultView */ "./src/customizations/components/theme/View/DefaultView.jsx");
/* harmony import */ var _plone_volto_components_theme_View_FileView__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @plone/volto/components/theme/View/FileView */ "./node_modules/@plone/volto/src/components/theme/View/FileView.jsx");
/* harmony import */ var _plone_volto_components_theme_View_ImageView__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @plone/volto/components/theme/View/ImageView */ "./node_modules/@plone/volto/src/components/theme/View/ImageView.jsx");
/* harmony import */ var _plone_volto_components_theme_View_ListingView__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @plone/volto/components/theme/View/ListingView */ "./src/customizations/components/theme/View/ListingView.jsx");
/* harmony import */ var _plone_volto_components_theme_View_NewsItemView__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @plone/volto/components/theme/View/NewsItemView */ "./node_modules/@plone/volto/src/components/theme/View/NewsItemView.jsx");
/* harmony import */ var _plone_volto_components_theme_View_SummaryView__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @plone/volto/components/theme/View/SummaryView */ "./node_modules/@plone/volto/src/components/theme/View/SummaryView.jsx");
/* harmony import */ var _plone_volto_components_theme_View_TabularView__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @plone/volto/components/theme/View/TabularView */ "./node_modules/@plone/volto/src/components/theme/View/TabularView.jsx");
/* harmony import */ var _plone_volto_components_theme_View_LinkView__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @plone/volto/components/theme/View/LinkView */ "./node_modules/@plone/volto/src/components/theme/View/LinkView.jsx");
/* harmony import */ var _plone_volto_components_theme_NotFound_NotFound__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @plone/volto/components/theme/NotFound/NotFound */ "./node_modules/@plone/volto/src/components/theme/NotFound/NotFound.jsx");
/* harmony import */ var _plone_volto_components_theme_ConnectionRefused_ConnectionRefused__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @plone/volto/components/theme/ConnectionRefused/ConnectionRefused */ "./node_modules/@plone/volto/src/components/theme/ConnectionRefused/ConnectionRefused.jsx");
/* harmony import */ var _plone_volto_components_theme_CorsError_CorsError__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! @plone/volto/components/theme/CorsError/CorsError */ "./node_modules/@plone/volto/src/components/theme/CorsError/CorsError.jsx");
/* harmony import */ var _plone_volto_components_theme_RequestTimeout_RequestTimeout__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! @plone/volto/components/theme/RequestTimeout/RequestTimeout */ "./node_modules/@plone/volto/src/components/theme/RequestTimeout/RequestTimeout.jsx");
/* harmony import */ var _plone_volto_components_theme_View_AlbumView__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! @plone/volto/components/theme/View/AlbumView */ "./node_modules/@plone/volto/src/components/theme/View/AlbumView.jsx");
/* harmony import */ var _plone_volto_components_theme_Unauthorized_Unauthorized__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! @plone/volto/components/theme/Unauthorized/Unauthorized */ "./node_modules/@plone/volto/src/components/theme/Unauthorized/Unauthorized.jsx");
/* harmony import */ var _plone_volto_components_theme_Forbidden_Forbidden__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! @plone/volto/components/theme/Forbidden/Forbidden */ "./node_modules/@plone/volto/src/components/theme/Forbidden/Forbidden.jsx");
/* harmony import */ var components__WEBPACK_IMPORTED_MODULE_16__ = __webpack_require__(/*! components */ "./src/components/index.js");
/* harmony import */ var _omelette_src_components_theme_View_RenderBlocks__WEBPACK_IMPORTED_MODULE_17__ = __webpack_require__(/*! ../../../omelette/src/components/theme/View/RenderBlocks */ "./node_modules/@plone/volto/src/components/theme/View/RenderBlocks.jsx");


















const EventView = _loadable_component__WEBPACK_IMPORTED_MODULE_0___default()({
  resolved: {},

  chunkName() {
    return "plone-volto-components-theme-View-EventView";
  },

  isReady(props) {
    const key = this.resolve(props);

    if (this.resolved[key] !== true) {
      return false;
    }

    if (true) {
      return !!__webpack_require__.m[key];
    }

    return false;
  },

  importAsync: () => __webpack_require__.e(/*! import() | plone-volto-components-theme-View-EventView */ "plone-volto-components-theme-View-EventView").then(__webpack_require__.bind(null, /*! @plone/volto/components/theme/View/EventView */ "./node_modules/@plone/volto/src/components/theme/View/EventView.jsx")),

  requireAsync(props) {
    const key = this.resolve(props);
    this.resolved[key] = false;
    return this.importAsync(props).then(resolved => {
      this.resolved[key] = true;
      return resolved;
    });
  },

  requireSync(props) {
    const id = this.resolve(props);

    if (true) {
      return __webpack_require__(id);
    }

    return eval('module.require')(id);
  },

  resolve() {
    if (true) {
      return /*require.resolve*/(/*! @plone/volto/components/theme/View/EventView */ "./node_modules/@plone/volto/src/components/theme/View/EventView.jsx");
    }

    return eval('require.resolve')("@plone/volto/components/theme/View/EventView");
  }

}); // Layout View Registry

const layoutViews = {
  document_view: _plone_volto_components_theme_View_DefaultView__WEBPACK_IMPORTED_MODULE_1__["default"],
  summary_view: _plone_volto_components_theme_View_SummaryView__WEBPACK_IMPORTED_MODULE_6__["default"],
  tabular_view: _plone_volto_components_theme_View_TabularView__WEBPACK_IMPORTED_MODULE_7__["default"],
  listing_view: _plone_volto_components_theme_View_ListingView__WEBPACK_IMPORTED_MODULE_4__["default"],
  link_redirect_view: _plone_volto_components_theme_View_LinkView__WEBPACK_IMPORTED_MODULE_8__["default"],
  album_view: _plone_volto_components_theme_View_AlbumView__WEBPACK_IMPORTED_MODULE_13__["default"],
  slider_view: components__WEBPACK_IMPORTED_MODULE_16__["SliderPage"],
  block_view: _omelette_src_components_theme_View_RenderBlocks__WEBPACK_IMPORTED_MODULE_17__["default"]
}; // Content Types View Registry

const contentTypesViews = {
  'News Item': _plone_volto_components_theme_View_NewsItemView__WEBPACK_IMPORTED_MODULE_5__["default"],
  File: _plone_volto_components_theme_View_FileView__WEBPACK_IMPORTED_MODULE_2__["default"],
  Image: _plone_volto_components_theme_View_ImageView__WEBPACK_IMPORTED_MODULE_3__["default"],
  Event: EventView
}; // Default view

const defaultView = _plone_volto_components_theme_View_DefaultView__WEBPACK_IMPORTED_MODULE_1__["default"];
const errorViews = {
  '404': _plone_volto_components_theme_NotFound_NotFound__WEBPACK_IMPORTED_MODULE_9__["default"],
  '401': _plone_volto_components_theme_Unauthorized_Unauthorized__WEBPACK_IMPORTED_MODULE_14__["default"],
  '403': _plone_volto_components_theme_Forbidden_Forbidden__WEBPACK_IMPORTED_MODULE_15__["default"],
  '408': _plone_volto_components_theme_RequestTimeout_RequestTimeout__WEBPACK_IMPORTED_MODULE_12__["default"],
  ECONNREFUSED: _plone_volto_components_theme_ConnectionRefused_ConnectionRefused__WEBPACK_IMPORTED_MODULE_10__["default"],
  corsError: _plone_volto_components_theme_CorsError_CorsError__WEBPACK_IMPORTED_MODULE_11__["default"]
};

/***/ })

};
//# sourceMappingURL=server.dfb8e930622d48517d2e.hot-update.js.map