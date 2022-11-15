exports.id = "server";
exports.modules = {

/***/ "./src/customizations/components/theme/View/ListingView.jsx":
/*!******************************************************************!*\
  !*** ./src/customizations/components/theme/View/ListingView.jsx ***!
  \******************************************************************/
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
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__);
var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/customizations/components/theme/View/ListingView.jsx";

/**
 * Document view component.
 * @module components/theme/View/ListingView
 */




/**
 * List view component class.
 * @function ListingView
 * @params {object} content Content object.
 * @returns {string} Markup of the component.
 */




const ListingView = ({
  content
}) => /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Container"], {
  id: "page-home",
  children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])("section", {
    id: "content-core",
    children: content.items.map(item => /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Segment"], {
      className: "listing-item",
      children: [item.image_field && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_3__["PreviewImage"], {
        item: item,
        size: "thumb",
        alt: item.image_caption ? item.image_caption : item.title,
        className: "ui image"
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Container"], {
        children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])("h2", {
          children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsxs"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_3__["UniversalLink"], {
            item: item,
            title: item['@type'],
            children: ["()", item.title]
          })
        }), item.description && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])("p", {
          children: item.description
        })]
      })]
    }, item.url))
  })
});
/**
 * Property types.
 * @property {Object} propTypes Property types.
 * @static
 */


ListingView.propTypes = {
  content: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.shape({
    title: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,
    description: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,
    items: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.arrayOf(prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.shape({
      '@id': prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,
      '@type': prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,
      description: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,
      review_state: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,
      title: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,
      url: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string
    }))
  }).isRequired
};
/* harmony default export */ __webpack_exports__["default"] = (ListingView);

/***/ })

};
//# sourceMappingURL=server.2c82f2a81d0f605bf94a.hot-update.js.map