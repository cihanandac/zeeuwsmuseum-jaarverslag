exports.ids = ["plone-volto-components-theme-View-EventView"];
exports.modules = {

/***/ "./node_modules/@plone/volto/src/components/theme/View/EventView.jsx":
/*!***************************************************************************!*\
  !*** ./node_modules/@plone/volto/src/components/theme/View/EventView.jsx ***!
  \***************************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/defineProperty */ "@babel/runtime/helpers/defineProperty");
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! prop-types */ "prop-types");
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(prop_types__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! semantic-ui-react */ "semantic-ui-react");
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(semantic_ui_react__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _plone_volto_components_theme_View_RenderBlocks__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @plone/volto/components/theme/View/RenderBlocks */ "./node_modules/@plone/volto/src/components/theme/View/RenderBlocks.jsx");
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__);

var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/node_modules/@plone/volto/src/components/theme/View/EventView.jsx";

function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); if (enumerableOnly) { symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; }); } keys.push.apply(keys, symbols); } return keys; }

function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i] != null ? arguments[i] : {}; if (i % 2) { ownKeys(Object(source), true).forEach(function (key) { _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(target, key, source[key]); }); } else if (Object.getOwnPropertyDescriptors) { Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)); } else { ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } } return target; }

/**
 * EventView view component.
 * @module components/theme/View/EventView
 */










const EventTextfieldView = ({
  content
}) => /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsxs"])(react__WEBPACK_IMPORTED_MODULE_1___default.a.Fragment, {
  children: [content.title && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])("h1", {
    className: "documentFirstHeading",
    children: content.title
  }), content.description && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])("p", {
    className: "documentDescription",
    children: content.description
  }), content.image && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_4__["Image"], {
    className: "document-image",
    src: content.image.scales.thumb.download,
    floated: "right"
  }), content.text && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])("div", {
    dangerouslySetInnerHTML: {
      __html: Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_3__["flattenHTMLToAppURL"])(content.text.data)
    }
  })]
});
/**
 * EventView view component class.
 * @function EventView
 * @params {object} content Content object.
 * @returns {string} Markup of the component.
 */


const EventView = props => {
  const {
    content
  } = props;
  return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])("div", {
    id: "page-document",
    className: "ui container viewwrapper event-view",
    children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_4__["Grid"], {
      children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_4__["Grid"].Column, {
        width: 7,
        className: "mobile hidden",
        children: Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_3__["hasBlocksData"])(content) ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])(_plone_volto_components_theme_View_RenderBlocks__WEBPACK_IMPORTED_MODULE_5__["default"], _objectSpread({}, props)) : /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])(EventTextfieldView, _objectSpread({}, props))
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_4__["Grid"].Column, {
        width: 5,
        className: "mobile hidden",
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_6__["EventDetails"], {
          content: content
        })
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_4__["Grid"].Column, {
        width: 12,
        only: "mobile",
        children: Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_3__["hasBlocksData"])(content) ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsxs"])(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["Fragment"], {
          children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])(_plone_volto_components_theme_View_RenderBlocks__WEBPACK_IMPORTED_MODULE_5__["default"], _objectSpread(_objectSpread({}, props), {}, {
            content: _objectSpread(_objectSpread({}, content), {}, {
              blocks_layout: {
                items: props.content.blocks_layout.items.slice(0, 1)
              }
            })
          })), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_6__["EventDetails"], {
            content: content,
            display_as: "div"
          }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])(_plone_volto_components_theme_View_RenderBlocks__WEBPACK_IMPORTED_MODULE_5__["default"], _objectSpread(_objectSpread({}, props), {}, {
            content: _objectSpread(_objectSpread({}, content), {}, {
              blocks_layout: {
                items: props.content.blocks_layout.items.slice(1)
              }
            })
          }))]
        }) : /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])(EventTextfieldView, _objectSpread({}, props))
      })]
    })
  });
};
/**
 * Property types.
 * @property {Object} propTypes Property types.
 * @static
 */


EventView.propTypes = {
  content: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.shape({
    title: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string,
    description: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string,
    text: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.shape({
      data: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string
    }),
    attendees: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.arrayOf(prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string).isRequired,
    contact_email: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string,
    contact_name: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string,
    contact_phone: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string,
    end: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string.isRequired,
    event_url: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string,
    location: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string,
    open_end: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.bool,
    recurrence: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.any,
    start: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string.isRequired,
    subjects: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.arrayOf(prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string).isRequired,
    whole_day: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.bool
  }).isRequired
};
/* harmony default export */ __webpack_exports__["default"] = (EventView);

/***/ })

};;
//# sourceMappingURL=plone-volto-components-theme-View-EventView.js.map