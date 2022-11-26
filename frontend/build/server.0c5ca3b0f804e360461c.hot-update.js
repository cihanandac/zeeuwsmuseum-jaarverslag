exports.id = "server";
exports.modules = {

/***/ "./src/customizations/components/theme/View/NewsItemView.jsx":
/*!*******************************************************************!*\
  !*** ./src/customizations/components/theme/View/NewsItemView.jsx ***!
  \*******************************************************************/
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
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var _plone_volto_components_theme_View_RenderBlocks__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @plone/volto/components/theme/View/RenderBlocks */ "./src/customizations/components/theme/View/RenderBlocks.jsx");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__);
var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/customizations/components/theme/View/NewsItemView.jsx";

/**
 * NewsItemView view component.
 * @module components/theme/View/NewsItemView
 */





/**
 * NewsItemView view component class.
 * @function NewsItemView
 * @params {object} content Content object.
 * @returns {string} Markup of the component.
 */




const NewsItemView = ({
  content
}) => Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_3__["hasBlocksData"])(content) ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__["jsx"])("div", {
  id: "page-document",
  className: "ui container viewwrapper event-view",
  children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__["jsx"])(_plone_volto_components_theme_View_RenderBlocks__WEBPACK_IMPORTED_MODULE_4__["default"], {
    content: content
  })
}) : /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Container"], {
  className: "view-wrapper",
  children: [content.title && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__["jsxs"])("h1", {
    className: "documentFirstHeading",
    children: [content.title, content.subtitle && ` - ${content.subtitle}`]
  }), content.description && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__["jsx"])("p", {
    className: "documentDescription",
    children: content.description
  }), content.image && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Image"], {
    className: "documentImage",
    alt: content.title,
    title: content.title,
    src: content.image['content-type'] === 'image/svg+xml' ? Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_3__["flattenToAppURL"])(content.image.download) : Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_3__["flattenToAppURL"])(content.image.scales.mini.download),
    floated: "right"
  }), content.text && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_5__["jsx"])("div", {
    dangerouslySetInnerHTML: {
      __html: Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_3__["flattenHTMLToAppURL"])(content.text.data)
    }
  })]
});
/**
 * Property types.
 * @property {Object} propTypes Property types.
 * @static
 */


NewsItemView.propTypes = {
  content: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.shape({
    title: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,
    description: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,
    text: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.shape({
      data: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string
    })
  }).isRequired
};
/* harmony default export */ __webpack_exports__["default"] = (NewsItemView);

/***/ })

};
//# sourceMappingURL=server.0c5ca3b0f804e360461c.hot-update.js.map