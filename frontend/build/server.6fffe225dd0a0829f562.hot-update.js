exports.id = "server";
exports.modules = {

/***/ "./node_modules/@plone/volto/src/config/Views.jsx":
/*!********************************************************!*\
  !*** ./node_modules/@plone/volto/src/config/Views.jsx ***!
  \********************************************************/
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
/* harmony import */ var _plone_volto_components_theme_View_RenderBlocks__WEBPACK_IMPORTED_MODULE_16__ = __webpack_require__(/*! @plone/volto/components/theme/View/RenderBlocks */ "./node_modules/@plone/volto/src/components/theme/View/RenderBlocks.jsx");

















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
  render_blocks: _plone_volto_components_theme_View_RenderBlocks__WEBPACK_IMPORTED_MODULE_16__["default"]
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
//# sourceMappingURL=server.6fffe225dd0a0829f562.hot-update.js.map