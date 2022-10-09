exports.id = "server";
exports.modules = {

/***/ "./node_modules/@plone/volto/src/config/Blocks.jsx":
/*!*********************************************************!*\
  !*** ./node_modules/@plone/volto/src/config/Blocks.jsx ***!
  \*********************************************************/
/*! exports provided: groupBlocksOrder, requiredBlocks, blocksConfig, initialBlocks, initialBlocksFocus */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "groupBlocksOrder", function() { return groupBlocksOrder; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "requiredBlocks", function() { return requiredBlocks; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "blocksConfig", function() { return blocksConfig; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "initialBlocks", function() { return initialBlocks; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "initialBlocksFocus", function() { return initialBlocksFocus; });
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/defineProperty */ "@babel/runtime/helpers/defineProperty");
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react-intl */ "react-intl");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react_intl__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _plone_volto_components_manage_Blocks_Title_View__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Title/View */ "./node_modules/@plone/volto/src/components/manage/Blocks/Title/View.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Description_View__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Description/View */ "./node_modules/@plone/volto/src/components/manage/Blocks/Description/View.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_ToC_View__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/ToC/View */ "./node_modules/@plone/volto/src/components/manage/Blocks/ToC/View.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Text_View__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Text/View */ "./node_modules/@plone/volto/src/components/manage/Blocks/Text/View.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Image_View__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Image/View */ "./node_modules/@plone/volto/src/components/manage/Blocks/Image/View.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_LeadImage_View__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/LeadImage/View */ "./node_modules/@plone/volto/src/components/manage/Blocks/LeadImage/View.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Listing_View__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Listing/View */ "./node_modules/@plone/volto/src/components/manage/Blocks/Listing/View.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Video_View__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Video/View */ "./node_modules/@plone/volto/src/components/manage/Blocks/Video/View.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_HeroImageLeft_View__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/HeroImageLeft/View */ "./node_modules/@plone/volto/src/components/manage/Blocks/HeroImageLeft/View.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Maps_View__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Maps/View */ "./node_modules/@plone/volto/src/components/manage/Blocks/Maps/View.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_HTML_View__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/HTML/View */ "./node_modules/@plone/volto/src/components/manage/Blocks/HTML/View.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Table_View__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Table/View */ "./node_modules/@plone/volto/src/components/manage/Blocks/Table/View.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Title_Edit__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Title/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/Title/Edit.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Description_Edit__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Description/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/Description/Edit.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_ToC_Edit__WEBPACK_IMPORTED_MODULE_16__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/ToC/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/ToC/Edit.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Text_Edit__WEBPACK_IMPORTED_MODULE_17__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Text/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/Text/Edit.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Image_Edit__WEBPACK_IMPORTED_MODULE_18__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Image/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/Image/Edit.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_LeadImage_Edit__WEBPACK_IMPORTED_MODULE_19__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/LeadImage/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/LeadImage/Edit.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Listing_Edit__WEBPACK_IMPORTED_MODULE_20__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Listing/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/Listing/Edit.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Listing_DefaultTemplate__WEBPACK_IMPORTED_MODULE_21__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Listing/DefaultTemplate */ "./node_modules/@plone/volto/src/components/manage/Blocks/Listing/DefaultTemplate.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Listing_SummaryTemplate__WEBPACK_IMPORTED_MODULE_22__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Listing/SummaryTemplate */ "./node_modules/@plone/volto/src/components/manage/Blocks/Listing/SummaryTemplate.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Video_Edit__WEBPACK_IMPORTED_MODULE_23__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Video/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/Video/Edit.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_HeroImageLeft_Edit__WEBPACK_IMPORTED_MODULE_24__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/HeroImageLeft/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/HeroImageLeft/Edit.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Maps_Edit__WEBPACK_IMPORTED_MODULE_25__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Maps/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/Maps/Edit.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_HTML_Edit__WEBPACK_IMPORTED_MODULE_26__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/HTML/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/HTML/Edit.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Table_Edit__WEBPACK_IMPORTED_MODULE_27__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Table/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/Table/Edit.jsx");
/* harmony import */ var _plone_volto_icons_description_svg__WEBPACK_IMPORTED_MODULE_28__ = __webpack_require__(/*! @plone/volto/icons/description.svg */ "./node_modules/@plone/volto/src/icons/description.svg");
/* harmony import */ var _plone_volto_icons_description_svg__WEBPACK_IMPORTED_MODULE_28___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_description_svg__WEBPACK_IMPORTED_MODULE_28__);
/* harmony import */ var _plone_volto_icons_text_svg__WEBPACK_IMPORTED_MODULE_29__ = __webpack_require__(/*! @plone/volto/icons/text.svg */ "./node_modules/@plone/volto/src/icons/text.svg");
/* harmony import */ var _plone_volto_icons_text_svg__WEBPACK_IMPORTED_MODULE_29___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_text_svg__WEBPACK_IMPORTED_MODULE_29__);
/* harmony import */ var _plone_volto_icons_subtext_svg__WEBPACK_IMPORTED_MODULE_30__ = __webpack_require__(/*! @plone/volto/icons/subtext.svg */ "./node_modules/@plone/volto/src/icons/subtext.svg");
/* harmony import */ var _plone_volto_icons_subtext_svg__WEBPACK_IMPORTED_MODULE_30___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_subtext_svg__WEBPACK_IMPORTED_MODULE_30__);
/* harmony import */ var _plone_volto_icons_camera_svg__WEBPACK_IMPORTED_MODULE_31__ = __webpack_require__(/*! @plone/volto/icons/camera.svg */ "./node_modules/@plone/volto/src/icons/camera.svg");
/* harmony import */ var _plone_volto_icons_camera_svg__WEBPACK_IMPORTED_MODULE_31___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_camera_svg__WEBPACK_IMPORTED_MODULE_31__);
/* harmony import */ var _plone_volto_icons_videocamera_svg__WEBPACK_IMPORTED_MODULE_32__ = __webpack_require__(/*! @plone/volto/icons/videocamera.svg */ "./node_modules/@plone/volto/src/icons/videocamera.svg");
/* harmony import */ var _plone_volto_icons_videocamera_svg__WEBPACK_IMPORTED_MODULE_32___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_videocamera_svg__WEBPACK_IMPORTED_MODULE_32__);
/* harmony import */ var _plone_volto_icons_globe_svg__WEBPACK_IMPORTED_MODULE_33__ = __webpack_require__(/*! @plone/volto/icons/globe.svg */ "./node_modules/@plone/volto/src/icons/globe.svg");
/* harmony import */ var _plone_volto_icons_globe_svg__WEBPACK_IMPORTED_MODULE_33___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_globe_svg__WEBPACK_IMPORTED_MODULE_33__);
/* harmony import */ var _plone_volto_icons_code_svg__WEBPACK_IMPORTED_MODULE_34__ = __webpack_require__(/*! @plone/volto/icons/code.svg */ "./node_modules/@plone/volto/src/icons/code.svg");
/* harmony import */ var _plone_volto_icons_code_svg__WEBPACK_IMPORTED_MODULE_34___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_code_svg__WEBPACK_IMPORTED_MODULE_34__);
/* harmony import */ var _plone_volto_icons_hero_svg__WEBPACK_IMPORTED_MODULE_35__ = __webpack_require__(/*! @plone/volto/icons/hero.svg */ "./node_modules/@plone/volto/src/icons/hero.svg");
/* harmony import */ var _plone_volto_icons_hero_svg__WEBPACK_IMPORTED_MODULE_35___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_hero_svg__WEBPACK_IMPORTED_MODULE_35__);
/* harmony import */ var _plone_volto_icons_table_svg__WEBPACK_IMPORTED_MODULE_36__ = __webpack_require__(/*! @plone/volto/icons/table.svg */ "./node_modules/@plone/volto/src/icons/table.svg");
/* harmony import */ var _plone_volto_icons_table_svg__WEBPACK_IMPORTED_MODULE_36___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_table_svg__WEBPACK_IMPORTED_MODULE_36__);
/* harmony import */ var _plone_volto_icons_list_bullet_svg__WEBPACK_IMPORTED_MODULE_37__ = __webpack_require__(/*! @plone/volto/icons/list-bullet.svg */ "./node_modules/@plone/volto/src/icons/list-bullet.svg");
/* harmony import */ var _plone_volto_icons_list_bullet_svg__WEBPACK_IMPORTED_MODULE_37___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_list_bullet_svg__WEBPACK_IMPORTED_MODULE_37__);
/* harmony import */ var _plone_volto_icons_zoom_svg__WEBPACK_IMPORTED_MODULE_38__ = __webpack_require__(/*! @plone/volto/icons/zoom.svg */ "./node_modules/@plone/volto/src/icons/zoom.svg");
/* harmony import */ var _plone_volto_icons_zoom_svg__WEBPACK_IMPORTED_MODULE_38___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_zoom_svg__WEBPACK_IMPORTED_MODULE_38__);
/* harmony import */ var _plone_volto_components_manage_Blocks_Listing_ImageGallery__WEBPACK_IMPORTED_MODULE_39__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Listing/ImageGallery */ "./node_modules/@plone/volto/src/components/manage/Blocks/Listing/ImageGallery.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Block_Schema__WEBPACK_IMPORTED_MODULE_40__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Block/Schema */ "./node_modules/@plone/volto/src/components/manage/Blocks/Block/Schema.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Text_Schema__WEBPACK_IMPORTED_MODULE_41__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Text/Schema */ "./node_modules/@plone/volto/src/components/manage/Blocks/Text/Schema.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Image_Schema__WEBPACK_IMPORTED_MODULE_42__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Image/Schema */ "./node_modules/@plone/volto/src/components/manage/Blocks/Image/Schema.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_ToC_Schema__WEBPACK_IMPORTED_MODULE_43__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/ToC/Schema */ "./node_modules/@plone/volto/src/components/manage/Blocks/ToC/Schema.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Search_SearchBlockView__WEBPACK_IMPORTED_MODULE_44__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Search/SearchBlockView */ "./node_modules/@plone/volto/src/components/manage/Blocks/Search/SearchBlockView.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Search_SearchBlockEdit__WEBPACK_IMPORTED_MODULE_45__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Search/SearchBlockEdit */ "./node_modules/@plone/volto/src/components/manage/Blocks/Search/SearchBlockEdit.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Search_layout_RightColumnFacets__WEBPACK_IMPORTED_MODULE_46__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Search/layout/RightColumnFacets */ "./node_modules/@plone/volto/src/components/manage/Blocks/Search/layout/RightColumnFacets.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Search_layout_LeftColumnFacets__WEBPACK_IMPORTED_MODULE_47__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Search/layout/LeftColumnFacets */ "./node_modules/@plone/volto/src/components/manage/Blocks/Search/layout/LeftColumnFacets.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Search_layout_TopSideFacets__WEBPACK_IMPORTED_MODULE_48__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Search/layout/TopSideFacets */ "./node_modules/@plone/volto/src/components/manage/Blocks/Search/layout/TopSideFacets.jsx");
/* harmony import */ var _plone_volto_components_manage_Blocks_Search_components__WEBPACK_IMPORTED_MODULE_49__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Search/components */ "./node_modules/@plone/volto/src/components/manage/Blocks/Search/components/index.js");
/* harmony import */ var _plone_volto_components_manage_Blocks_Listing_getAsyncData__WEBPACK_IMPORTED_MODULE_50__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Listing/getAsyncData */ "./node_modules/@plone/volto/src/components/manage/Blocks/Listing/getAsyncData.js");
/* harmony import */ var _plone_volto_components_manage_Blocks_HeroImageLeft_schema__WEBPACK_IMPORTED_MODULE_51__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/HeroImageLeft/schema */ "./node_modules/@plone/volto/src/components/manage/Blocks/HeroImageLeft/schema.js");
/* harmony import */ var _plone_volto_components_manage_Blocks_Listing_schema__WEBPACK_IMPORTED_MODULE_52__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Listing/schema */ "./node_modules/@plone/volto/src/components/manage/Blocks/Listing/schema.js");
/* harmony import */ var _plone_volto_components_manage_Blocks_Search_schema__WEBPACK_IMPORTED_MODULE_53__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Search/schema */ "./node_modules/@plone/volto/src/components/manage/Blocks/Search/schema.js");


function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); if (enumerableOnly) { symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; }); } keys.push.apply(keys, symbols); } return keys; }

function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i] != null ? arguments[i] : {}; if (i % 2) { ownKeys(Object(source), true).forEach(function (key) { _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(target, key, source[key]); }); } else if (Object.getOwnPropertyDescriptors) { Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)); } else { ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } } return target; }



















































 // block sidebar schemas (not the Dexterity Layout block settings schemas)




Object(react_intl__WEBPACK_IMPORTED_MODULE_1__["defineMessages"])({
  title: {
    "id": "title",
    "defaultMessage": "Title"
  },
  description: {
    "id": "description",
    "defaultMessage": "Description"
  },
  text: {
    "id": "text",
    "defaultMessage": "Text"
  },
  toc: {
    "id": "toc",
    "defaultMessage": "Table of Contents"
  },
  image: {
    "id": "image",
    "defaultMessage": "Image"
  },
  video: {
    "id": "video",
    "defaultMessage": "Video"
  },
  hero: {
    "id": "hero",
    "defaultMessage": "Hero"
  },
  table: {
    "id": "table",
    "defaultMessage": "Table"
  },
  maps: {
    "id": "maps",
    "defaultMessage": "Maps"
  },
  html: {
    "id": "html",
    "defaultMessage": "HTML"
  },
  leadimage: {
    "id": "leadimage",
    "defaultMessage": "Lead Image Field"
  },
  listing: {
    "id": "listing",
    "defaultMessage": "Listing"
  },
  // Groups
  mostUsed: {
    "id": "mostUsed",
    "defaultMessage": "Most used"
  },
  media: {
    "id": "media",
    "defaultMessage": "Media"
  },
  common: {
    "id": "common",
    "defaultMessage": "Common"
  },
  // Listing block variations
  summary: {
    "id": "Summary",
    "defaultMessage": "Summary"
  },
  imageGallery: {
    "id": "Image gallery",
    "defaultMessage": "Image gallery"
  },
  // Search block variations
  facetsRightSide: {
    "id": "Facets on right side",
    "defaultMessage": "Facets on right side"
  },
  facetsLeftSide: {
    "id": "Facets on left side",
    "defaultMessage": "Facets on left side"
  },
  facetsTopSide: {
    "id": "Facets on top",
    "defaultMessage": "Facets on top"
  }
});
const groupBlocksOrder = [{
  id: 'mostUsed',
  title: 'Most used'
}, {
  id: 'text',
  title: 'Text'
}, {
  id: 'media',
  title: 'Media'
}, {
  id: 'common',
  title: 'Common'
}];
const blocksConfig = {
  title: {
    id: 'title',
    title: 'Title',
    icon: _plone_volto_icons_text_svg__WEBPACK_IMPORTED_MODULE_29___default.a,
    group: 'text',
    view: _plone_volto_components_manage_Blocks_Title_View__WEBPACK_IMPORTED_MODULE_2__["default"],
    edit: _plone_volto_components_manage_Blocks_Title_Edit__WEBPACK_IMPORTED_MODULE_14__["default"],
    schema: _plone_volto_components_manage_Blocks_Block_Schema__WEBPACK_IMPORTED_MODULE_40__["default"],
    restricted: ({
      properties,
      block
    }) => {
      var _properties$blocks_la, _properties$blocks_la2;

      return (_properties$blocks_la = properties.blocks_layout) === null || _properties$blocks_la === void 0 ? void 0 : (_properties$blocks_la2 = _properties$blocks_la.items) === null || _properties$blocks_la2 === void 0 ? void 0 : _properties$blocks_la2.find(uid => {
        var _properties$blocks, _properties$blocks$ui;

        return ((_properties$blocks = properties.blocks) === null || _properties$blocks === void 0 ? void 0 : (_properties$blocks$ui = _properties$blocks[uid]) === null || _properties$blocks$ui === void 0 ? void 0 : _properties$blocks$ui['@type']) === block.id;
      });
    },
    mostUsed: false,
    blockHasOwnFocusManagement: true,
    sidebarTab: 0,
    security: {
      addPermission: [],
      view: []
    }
  },
  description: {
    id: 'description',
    title: 'Description',
    icon: _plone_volto_icons_description_svg__WEBPACK_IMPORTED_MODULE_28___default.a,
    group: 'text',
    view: _plone_volto_components_manage_Blocks_Description_View__WEBPACK_IMPORTED_MODULE_3__["default"],
    edit: _plone_volto_components_manage_Blocks_Description_Edit__WEBPACK_IMPORTED_MODULE_15__["default"],
    schema: _plone_volto_components_manage_Blocks_Block_Schema__WEBPACK_IMPORTED_MODULE_40__["default"],
    restricted: true,
    mostUsed: false,
    blockHasOwnFocusManagement: true,
    sidebarTab: 0,
    security: {
      addPermission: [],
      view: []
    }
  },
  text: {
    id: 'text',
    title: 'Text',
    icon: _plone_volto_icons_subtext_svg__WEBPACK_IMPORTED_MODULE_30___default.a,
    group: 'text',
    view: _plone_volto_components_manage_Blocks_Text_View__WEBPACK_IMPORTED_MODULE_5__["default"],
    edit: _plone_volto_components_manage_Blocks_Text_Edit__WEBPACK_IMPORTED_MODULE_17__["default"],
    schema: _plone_volto_components_manage_Blocks_Text_Schema__WEBPACK_IMPORTED_MODULE_41__["default"],
    restricted: false,
    mostUsed: false,
    blockHasOwnFocusManagement: true,
    sidebarTab: 0,
    security: {
      addPermission: [],
      view: []
    },
    blockHasValue: data => {
      var _data$text, _data$text$blocks;

      const isEmpty = !data.text || ((_data$text = data.text) === null || _data$text === void 0 ? void 0 : (_data$text$blocks = _data$text.blocks) === null || _data$text$blocks === void 0 ? void 0 : _data$text$blocks.length) === 1 && data.text.blocks[0].text === '';
      return !isEmpty;
    }
  },
  image: {
    id: 'image',
    title: 'Image',
    icon: _plone_volto_icons_camera_svg__WEBPACK_IMPORTED_MODULE_31___default.a,
    group: 'media',
    view: _plone_volto_components_manage_Blocks_Image_View__WEBPACK_IMPORTED_MODULE_6__["default"],
    edit: _plone_volto_components_manage_Blocks_Image_Edit__WEBPACK_IMPORTED_MODULE_18__["default"],
    schema: _plone_volto_components_manage_Blocks_Image_Schema__WEBPACK_IMPORTED_MODULE_42__["default"],
    restricted: false,
    mostUsed: true,
    sidebarTab: 1,
    security: {
      addPermission: [],
      view: []
    }
  },
  leadimage: {
    id: 'leadimage',
    title: 'Lead Image Field',
    icon: _plone_volto_icons_camera_svg__WEBPACK_IMPORTED_MODULE_31___default.a,
    group: 'media',
    view: _plone_volto_components_manage_Blocks_LeadImage_View__WEBPACK_IMPORTED_MODULE_7__["default"],
    edit: _plone_volto_components_manage_Blocks_LeadImage_Edit__WEBPACK_IMPORTED_MODULE_19__["default"],
    schema: _plone_volto_components_manage_Blocks_Block_Schema__WEBPACK_IMPORTED_MODULE_40__["default"],
    restricted: ({
      properties
    }) => !properties.hasOwnProperty('image'),
    mostUsed: false,
    sidebarTab: 1,
    security: {
      addPermission: [],
      view: []
    }
  },
  listing: {
    id: 'listing',
    title: 'Listing',
    icon: _plone_volto_icons_list_bullet_svg__WEBPACK_IMPORTED_MODULE_37___default.a,
    group: 'common',
    view: _plone_volto_components_manage_Blocks_Listing_View__WEBPACK_IMPORTED_MODULE_8__["default"],
    edit: _plone_volto_components_manage_Blocks_Listing_Edit__WEBPACK_IMPORTED_MODULE_20__["default"],
    schema: _plone_volto_components_manage_Blocks_Block_Schema__WEBPACK_IMPORTED_MODULE_40__["default"],
    blockSchema: _plone_volto_components_manage_Blocks_Listing_schema__WEBPACK_IMPORTED_MODULE_52__["default"],
    restricted: false,
    mostUsed: true,
    sidebarTab: 1,
    showLinkMore: false,
    security: {
      addPermission: [],
      view: []
    },
    variations: [{
      id: 'default',
      isDefault: true,
      title: 'Default',
      template: _plone_volto_components_manage_Blocks_Listing_DefaultTemplate__WEBPACK_IMPORTED_MODULE_21__["default"]
    }, {
      id: 'imageGallery',
      title: 'Image gallery',
      template: _plone_volto_components_manage_Blocks_Listing_ImageGallery__WEBPACK_IMPORTED_MODULE_39__["default"]
    }, {
      id: 'summary',
      title: 'Summary',
      template: _plone_volto_components_manage_Blocks_Listing_SummaryTemplate__WEBPACK_IMPORTED_MODULE_22__["default"]
    }],
    getAsyncData: _plone_volto_components_manage_Blocks_Listing_getAsyncData__WEBPACK_IMPORTED_MODULE_50__["default"]
  },
  video: {
    id: 'video',
    title: 'Video',
    icon: _plone_volto_icons_videocamera_svg__WEBPACK_IMPORTED_MODULE_32___default.a,
    group: 'media',
    view: _plone_volto_components_manage_Blocks_Video_View__WEBPACK_IMPORTED_MODULE_9__["default"],
    edit: _plone_volto_components_manage_Blocks_Video_Edit__WEBPACK_IMPORTED_MODULE_23__["default"],
    schema: _plone_volto_components_manage_Blocks_Block_Schema__WEBPACK_IMPORTED_MODULE_40__["default"],
    restricted: false,
    mostUsed: true,
    sidebarTab: 1,
    security: {
      addPermission: [],
      view: []
    }
  },
  toc: {
    id: 'toc',
    title: 'Table of Contents',
    icon: _plone_volto_icons_list_bullet_svg__WEBPACK_IMPORTED_MODULE_37___default.a,
    group: 'common',
    view: _plone_volto_components_manage_Blocks_ToC_View__WEBPACK_IMPORTED_MODULE_4__["default"],
    edit: _plone_volto_components_manage_Blocks_ToC_Edit__WEBPACK_IMPORTED_MODULE_16__["default"],
    schema: _plone_volto_components_manage_Blocks_ToC_Schema__WEBPACK_IMPORTED_MODULE_43__["default"],
    restricted: false,
    mostUsed: false,
    sidebarTab: 0,
    security: {
      addPermission: [],
      view: []
    }
  },
  hero: {
    id: 'hero',
    title: 'Hero',
    icon: _plone_volto_icons_hero_svg__WEBPACK_IMPORTED_MODULE_35___default.a,
    group: 'common',
    view: _plone_volto_components_manage_Blocks_HeroImageLeft_View__WEBPACK_IMPORTED_MODULE_10__["default"],
    edit: _plone_volto_components_manage_Blocks_HeroImageLeft_Edit__WEBPACK_IMPORTED_MODULE_24__["default"],
    schema: _plone_volto_components_manage_Blocks_Block_Schema__WEBPACK_IMPORTED_MODULE_40__["default"],
    blockSchema: _plone_volto_components_manage_Blocks_HeroImageLeft_schema__WEBPACK_IMPORTED_MODULE_51__["default"],
    restricted: false,
    mostUsed: false,
    blockHasOwnFocusManagement: true,
    sidebarTab: 1,
    security: {
      addPermission: [],
      view: []
    }
  },
  maps: {
    id: 'maps',
    title: 'Maps',
    icon: _plone_volto_icons_globe_svg__WEBPACK_IMPORTED_MODULE_33___default.a,
    group: 'common',
    view: _plone_volto_components_manage_Blocks_Maps_View__WEBPACK_IMPORTED_MODULE_11__["default"],
    edit: _plone_volto_components_manage_Blocks_Maps_Edit__WEBPACK_IMPORTED_MODULE_25__["default"],
    schema: _plone_volto_components_manage_Blocks_Block_Schema__WEBPACK_IMPORTED_MODULE_40__["default"],
    restricted: false,
    mostUsed: false,
    sidebarTab: 1,
    security: {
      addPermission: [],
      view: []
    }
  },
  html: {
    id: 'html',
    title: 'HTML',
    icon: _plone_volto_icons_code_svg__WEBPACK_IMPORTED_MODULE_34___default.a,
    group: 'common',
    view: _plone_volto_components_manage_Blocks_HTML_View__WEBPACK_IMPORTED_MODULE_12__["default"],
    edit: _plone_volto_components_manage_Blocks_HTML_Edit__WEBPACK_IMPORTED_MODULE_26__["default"],
    schema: _plone_volto_components_manage_Blocks_Block_Schema__WEBPACK_IMPORTED_MODULE_40__["default"],
    restricted: false,
    mostUsed: false,
    sidebarTab: 0,
    security: {
      addPermission: [],
      view: []
    }
  },
  table: {
    id: 'table',
    title: 'Table',
    icon: _plone_volto_icons_table_svg__WEBPACK_IMPORTED_MODULE_36___default.a,
    group: 'common',
    view: _plone_volto_components_manage_Blocks_Table_View__WEBPACK_IMPORTED_MODULE_13__["default"],
    edit: _plone_volto_components_manage_Blocks_Table_Edit__WEBPACK_IMPORTED_MODULE_27__["default"],
    schema: _plone_volto_components_manage_Blocks_Block_Schema__WEBPACK_IMPORTED_MODULE_40__["default"],
    restricted: false,
    mostUsed: false,
    blockHasOwnFocusManagement: true,
    sidebarTab: 1,
    security: {
      addPermission: [],
      view: []
    }
  },
  search: {
    id: 'search',
    title: 'Search',
    icon: _plone_volto_icons_zoom_svg__WEBPACK_IMPORTED_MODULE_38___default.a,
    group: 'common',
    view: _plone_volto_components_manage_Blocks_Search_SearchBlockView__WEBPACK_IMPORTED_MODULE_44__["default"],
    edit: _plone_volto_components_manage_Blocks_Search_SearchBlockEdit__WEBPACK_IMPORTED_MODULE_45__["default"],
    blockSchema: _plone_volto_components_manage_Blocks_Search_schema__WEBPACK_IMPORTED_MODULE_53__["default"],
    restricted: false,
    mostUsed: false,
    sidebarTab: 1,
    security: {
      addPermission: [],
      view: []
    },
    variations: [{
      id: 'facetsRightSide',
      title: 'Facets on right side',
      view: _plone_volto_components_manage_Blocks_Search_layout_RightColumnFacets__WEBPACK_IMPORTED_MODULE_46__["default"],
      isDefault: true
    }, {
      id: 'facetsLeftSide',
      title: 'Facets on left side',
      view: _plone_volto_components_manage_Blocks_Search_layout_LeftColumnFacets__WEBPACK_IMPORTED_MODULE_47__["default"],
      isDefault: false
    }, {
      id: 'facetsTopSide',
      title: 'Facets on top',
      view: _plone_volto_components_manage_Blocks_Search_layout_TopSideFacets__WEBPACK_IMPORTED_MODULE_48__["default"],
      isDefault: false
    }],
    extensions: {
      facetWidgets: {
        rewriteOptions: (name, choices) => {
          return name === 'review_state' ? choices.map(opt => _objectSpread(_objectSpread({}, opt), {}, {
            label: opt.label.replace(/\[.+\]/, '').trim()
          })) : choices;
        },
        types: [{
          id: 'selectFacet',
          title: 'Select',
          view: _plone_volto_components_manage_Blocks_Search_components__WEBPACK_IMPORTED_MODULE_49__["SelectFacet"],
          isDefault: true,
          schemaEnhancer: _plone_volto_components_manage_Blocks_Search_components__WEBPACK_IMPORTED_MODULE_49__["SelectFacet"].schemaEnhancer,
          stateToValue: _plone_volto_components_manage_Blocks_Search_components__WEBPACK_IMPORTED_MODULE_49__["SelectFacet"].stateToValue,
          valueToQuery: _plone_volto_components_manage_Blocks_Search_components__WEBPACK_IMPORTED_MODULE_49__["SelectFacet"].valueToQuery,
          filterListComponent: _plone_volto_components_manage_Blocks_Search_components__WEBPACK_IMPORTED_MODULE_49__["SelectFacetFilterListEntry"]
        }, {
          id: 'checkboxFacet',
          title: 'Checkbox',
          view: _plone_volto_components_manage_Blocks_Search_components__WEBPACK_IMPORTED_MODULE_49__["CheckboxFacet"],
          isDefault: false,
          schemaEnhancer: _plone_volto_components_manage_Blocks_Search_components__WEBPACK_IMPORTED_MODULE_49__["CheckboxFacet"].schemaEnhancer,
          stateToValue: _plone_volto_components_manage_Blocks_Search_components__WEBPACK_IMPORTED_MODULE_49__["CheckboxFacet"].stateToValue,
          valueToQuery: _plone_volto_components_manage_Blocks_Search_components__WEBPACK_IMPORTED_MODULE_49__["CheckboxFacet"].valueToQuery,
          filterListComponent: _plone_volto_components_manage_Blocks_Search_components__WEBPACK_IMPORTED_MODULE_49__["SelectFacetFilterListEntry"]
        }, {
          id: 'daterangeFacet',
          title: 'Date range',
          view: _plone_volto_components_manage_Blocks_Search_components__WEBPACK_IMPORTED_MODULE_49__["DateRangeFacet"],
          isDefault: false,
          stateToValue: _plone_volto_components_manage_Blocks_Search_components__WEBPACK_IMPORTED_MODULE_49__["DateRangeFacet"].stateToValue,
          valueToQuery: _plone_volto_components_manage_Blocks_Search_components__WEBPACK_IMPORTED_MODULE_49__["DateRangeFacet"].valueToQuery,
          filterListComponent: _plone_volto_components_manage_Blocks_Search_components__WEBPACK_IMPORTED_MODULE_49__["DateRangeFacetFilterListEntry"]
        }, {
          id: 'toggleFacet',
          title: 'Toggle',
          view: _plone_volto_components_manage_Blocks_Search_components__WEBPACK_IMPORTED_MODULE_49__["ToggleFacet"],
          isDefault: false,
          stateToValue: _plone_volto_components_manage_Blocks_Search_components__WEBPACK_IMPORTED_MODULE_49__["ToggleFacet"].stateToValue,
          valueToQuery: _plone_volto_components_manage_Blocks_Search_components__WEBPACK_IMPORTED_MODULE_49__["ToggleFacet"].valueToQuery,
          filterListComponent: _plone_volto_components_manage_Blocks_Search_components__WEBPACK_IMPORTED_MODULE_49__["ToggleFacetFilterListEntry"]
        }]
      }
    }
  }
};
const requiredBlocks = [];
const initialBlocks = {};
const initialBlocksFocus = {}; //{Document:'title'}



/***/ })

};
//# sourceMappingURL=server.8dfeb7114daa55666b7d.hot-update.js.map