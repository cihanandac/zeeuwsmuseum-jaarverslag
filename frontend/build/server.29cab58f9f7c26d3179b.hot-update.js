exports.id = "server";
exports.modules = {

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
/* harmony import */ var _omelette_src_components_theme_View_RenderBlocks__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ../omelette/src/components/theme/View/RenderBlocks */ "./node_modules/@plone/volto/src/components/theme/View/RenderBlocks.jsx");
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
  config.views = _objectSpread(_objectSpread({}, config.views), {}, {
    contentTypesViews: _objectSpread(_objectSpread({}, config.views.contentTypesViews), {}, {
      Folder: _package_components__WEBPACK_IMPORTED_MODULE_1__["SliderPage"]
    })
  });
  {
    console.log(config.views.layoutViews);
  } // Add here your project's configuration here by modifying `config` accordingly

  return config;
}

/***/ })

};
//# sourceMappingURL=server.29cab58f9f7c26d3179b.hot-update.js.map