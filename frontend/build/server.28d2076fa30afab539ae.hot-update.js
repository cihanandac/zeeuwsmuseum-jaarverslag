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
  album_view: _plone_volto_components_theme_View_AlbumView__WEBPACK_IMPORTED_MODULE_13__["default"]
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

/***/ }),

/***/ "./node_modules/@plone/volto/src/icons/dots.svg":
/*!******************************************************!*\
  !*** ./node_modules/@plone/volto/src/icons/dots.svg ***!
  \******************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = {"attributes":{"xmlns":"http://www.w3.org/2000/svg","width":"36","height":"36","viewBox":"0 0 36 36"},"content":"<path d=\"M8 16C6.897 16 6 16.897 6 18 6 19.103 6.897 20 8 20 9.103 20 10 19.103 10 18 10 16.897 9.103 16 8 16M8 22C5.794 22 4 20.206 4 18 4 15.794 5.794 14 8 14 10.206 14 12 15.794 12 18 12 20.206 10.206 22 8 22M18 16C16.897 16 16 16.897 16 18 16 19.103 16.897 20 18 20 19.103 20 20 19.103 20 18 20 16.897 19.103 16 18 16M18 22C15.794 22 14 20.206 14 18 14 15.794 15.794 14 18 14 20.206 14 22 15.794 22 18 22 20.206 20.206 22 18 22M28 16C26.897 16 26 16.897 26 18 26 19.103 26.897 20 28 20 29.103 20 30 19.103 30 18 30 16.897 29.103 16 28 16M28 22C25.794 22 24 20.206 24 18 24 15.794 25.794 14 28 14 30.206 14 32 15.794 32 18 32 20.206 30.206 22 28 22M8 26C6.897 26 6 26.897 6 28 6 29.103 6.897 30 8 30 9.103 30 10 29.103 10 28 10 26.897 9.103 26 8 26M8 32C5.794 32 4 30.206 4 28 4 25.794 5.794 24 8 24 10.206 24 12 25.794 12 28 12 30.206 10.206 32 8 32M18 26C16.897 26 16 26.897 16 28 16 29.103 16.897 30 18 30 19.103 30 20 29.103 20 28 20 26.897 19.103 26 18 26M18 32C15.794 32 14 30.206 14 28 14 25.794 15.794 24 18 24 20.206 24 22 25.794 22 28 22 30.206 20.206 32 18 32M28 26C26.897 26 26 26.897 26 28 26 29.103 26.897 30 28 30 29.103 30 30 29.103 30 28 30 26.897 29.103 26 28 26M28 32C25.794 32 24 30.206 24 28 24 25.794 25.794 24 28 24 30.206 24 32 25.794 32 28 32 30.206 30.206 32 28 32M8 6C6.897 6 6 6.897 6 8 6 9.103 6.897 10 8 10 9.103 10 10 9.103 10 8 10 6.897 9.103 6 8 6M8 12C5.794 12 4 10.206 4 8 4 5.794 5.794 4 8 4 10.206 4 12 5.794 12 8 12 10.206 10.206 12 8 12M18 6C16.897 6 16 6.897 16 8 16 9.103 16.897 10 18 10 19.103 10 20 9.103 20 8 20 6.897 19.103 6 18 6M18 12C15.794 12 14 10.206 14 8 14 5.794 15.794 4 18 4 20.206 4 22 5.794 22 8 22 10.206 20.206 12 18 12M28 6C26.897 6 26 6.897 26 8 26 9.103 26.897 10 28 10 29.103 10 30 9.103 30 8 30 6.897 29.103 6 28 6M28 12C25.794 12 24 10.206 24 8 24 5.794 25.794 4 28 4 30.206 4 32 5.794 32 8 32 10.206 30.206 12 28 12\" fill-rule=\"evenodd\"/>"}

/***/ }),

/***/ "./node_modules/@plone/volto/src/icons/presentation.svg":
/*!**************************************************************!*\
  !*** ./node_modules/@plone/volto/src/icons/presentation.svg ***!
  \**************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = {"attributes":{"xmlns":"http://www.w3.org/2000/svg","width":"36","height":"36","viewBox":"0 0 36 36"},"content":"<path fill-rule=\"evenodd\" d=\"M5,25 L31,25 L31,11 L5,11 L5,25 Z M3,26.999 L3,8.999 L33,8.999 L33,26.999 L3,26.999 Z M17,7 L19,7 L19,9 L17,9 L17,7 Z M14.5500002,27 L21.4500008,27 L24.707,30.293 L23.293,31.707 L19,27.414 L19,32 L17,32 L17,27.414 L12.707,31.707 L11.293,30.293 L14.5500002,27 Z\"/>"}

/***/ }),

/***/ "./src/config.js":
/*!***********************!*\
  !*** ./src/config.js ***!
  \***********************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "default", function() { return applyConfig; });
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/defineProperty */ "@babel/runtime/helpers/defineProperty");
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _package_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @package/components */ "./src/components/index.js");
/* harmony import */ var _plone_volto_icons_slider_svg__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @plone/volto/icons/slider.svg */ "./node_modules/@plone/volto/src/icons/slider.svg");
/* harmony import */ var _plone_volto_icons_slider_svg__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_slider_svg__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _plone_volto_icons_dots_svg__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @plone/volto/icons/dots.svg */ "./node_modules/@plone/volto/src/icons/dots.svg");
/* harmony import */ var _plone_volto_icons_dots_svg__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_dots_svg__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _plone_volto_icons_show_svg__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @plone/volto/icons/show.svg */ "./node_modules/@plone/volto/src/icons/show.svg");
/* harmony import */ var _plone_volto_icons_show_svg__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_show_svg__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _plone_volto_icons_presentation_svg__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @plone/volto/icons/presentation.svg */ "./node_modules/@plone/volto/src/icons/presentation.svg");
/* harmony import */ var _plone_volto_icons_presentation_svg__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_presentation_svg__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _plone_volto_icons_editing_svg__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @plone/volto/icons/editing.svg */ "./node_modules/@plone/volto/src/icons/editing.svg");
/* harmony import */ var _plone_volto_icons_editing_svg__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_editing_svg__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _plone_volto_config__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @plone/volto/config */ "./node_modules/@plone/volto/src/config/index.js");
/* harmony import */ var _omelette_src_config_Views__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ../omelette/src/config/Views */ "./node_modules/@plone/volto/src/config/Views.jsx");
/* harmony import */ var customizations_components_theme_View_RenderBlocks__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! customizations/components/theme/View/RenderBlocks */ "./src/customizations/components/theme/View/RenderBlocks.jsx");
/* harmony import */ var customizations_components_theme_View_ListingView__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! customizations/components/theme/View/ListingView */ "./src/customizations/components/theme/View/ListingView.jsx");
/* harmony import */ var _omelette_src_components_theme_View_TabularView__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! ../omelette/src/components/theme/View/TabularView */ "./node_modules/@plone/volto/src/components/theme/View/TabularView.jsx");


function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); if (enumerableOnly) { symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; }); } keys.push.apply(keys, symbols); } return keys; }

function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i] != null ? arguments[i] : {}; if (i % 2) { ownKeys(Object(source), true).forEach(function (key) { _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(target, key, source[key]); }); } else if (Object.getOwnPropertyDescriptors) { Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)); } else { ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } } return target; }

/**
 * Add your config changes here.
 * @module config
 * @example
 * export default function applyConfig(config) {
 *   config.settings = {
 *     ...config.settings,
 *     port: 4300,
 *     listBlockTypes: {
 *       ...config.settings.listBlockTypes,
 *       'my-list-item',
 *    }
 * }
 */





 // import { defineMessages } from 'react-intl';
// All your imports required for the config here BEFORE this line






 // defineMessages({
//   mainslider: {
//     id: 'Main Slider',
//     defaultMessage: 'Main Slider',
//   },
// });

function applyConfig(config) {
  config.blocks.requiredBlocks = [];
  config.blocks.blocksConfig.socialbottom = {
    id: 'socialbottom',
    title: 'Socialbuttons',
    icon: _plone_volto_icons_show_svg__WEBPACK_IMPORTED_MODULE_4___default.a,
    group: 'common',
    view: _package_components__WEBPACK_IMPORTED_MODULE_1__["SocialBottomViewBlock"],
    edit: _package_components__WEBPACK_IMPORTED_MODULE_1__["SocialBottomEditBlock"],
    restricted: false,
    mostUsed: false,
    security: {
      addPermission: [],
      view: []
    }
  }, config.blocks.blocksConfig.emptyline = {
    id: 'emptyline',
    title: 'Empty Line',
    icon: _plone_volto_icons_dots_svg__WEBPACK_IMPORTED_MODULE_3___default.a,
    group: 'text',
    view: _package_components__WEBPACK_IMPORTED_MODULE_1__["EmptylineViewBlock"],
    edit: _package_components__WEBPACK_IMPORTED_MODULE_1__["EmptylineEditBlock"],
    restricted: false,
    mostUsed: false,
    security: {
      addPermission: [],
      view: []
    }
  }, config.blocks.blocksConfig.nutezien = {
    id: 'nutezien',
    title: 'Nutezien',
    icon: _plone_volto_icons_presentation_svg__WEBPACK_IMPORTED_MODULE_5___default.a,
    group: 'common',
    view: _package_components__WEBPACK_IMPORTED_MODULE_1__["NutezienViewBlock"],
    edit: _package_components__WEBPACK_IMPORTED_MODULE_1__["NutezienEditBlock"],
    restricted: false,
    mostUsed: false,
    security: {
      addPermission: [],
      view: []
    }
  }, config.blocks.blocksConfig.photodescription = {
    id: 'photodescription',
    title: 'Photo Info',
    icon: _plone_volto_icons_editing_svg__WEBPACK_IMPORTED_MODULE_6___default.a,
    group: 'media',
    view: _package_components__WEBPACK_IMPORTED_MODULE_1__["PhotoDescriptionViewBlock"],
    edit: _package_components__WEBPACK_IMPORTED_MODULE_1__["PhotoDescriptionEditBlock"],
    restricted: false,
    mostUsed: false,
    security: {
      addPermission: [],
      view: []
    }
  };
  config.views = _objectSpread(_objectSpread(_objectSpread({}, config.views), {}, {
    contentTypesViews: _objectSpread(_objectSpread({}, config.views.contentTypesViews), {}, {
      Folder: _package_components__WEBPACK_IMPORTED_MODULE_1__["SliderPage"],
      ListingView: customizations_components_theme_View_ListingView__WEBPACK_IMPORTED_MODULE_10__["default"]
    })
  }, config.views), {}, {
    layoutViews: {
      'listing_view': customizations_components_theme_View_ListingView__WEBPACK_IMPORTED_MODULE_10__["default"],
      'tabular_view': _omelette_src_components_theme_View_TabularView__WEBPACK_IMPORTED_MODULE_11__["default"],
      'block_view': customizations_components_theme_View_RenderBlocks__WEBPACK_IMPORTED_MODULE_9__["default"],
      'slider_view': _package_components__WEBPACK_IMPORTED_MODULE_1__["SliderPage"]
    }
  });
  {
    console.log(config.views.layoutViews);
  } // Add here your project's configuration here by modifying `config` accordingly

  return config;
}

/***/ })

};
//# sourceMappingURL=server.28d2076fa30afab539ae.hot-update.js.map