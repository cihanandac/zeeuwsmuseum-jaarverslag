exports.id = "server";
exports.modules = {

/***/ "./node_modules/@kitconcept/volto-slider-block/src/components/View.jsx":
/*!*****************************************************************************!*\
  !*** ./node_modules/@kitconcept/volto-slider-block/src/components/View.jsx ***!
  \*****************************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/defineProperty */ "@babel/runtime/helpers/defineProperty");
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! semantic-ui-react */ "semantic-ui-react");
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react_slick__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-slick */ "react-slick");
/* harmony import */ var react_slick__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react_slick__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var classnames__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! classnames */ "classnames");
/* harmony import */ var classnames__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(classnames__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! react-intl */ "react-intl");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(react_intl__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _Body__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./Body */ "./node_modules/@kitconcept/volto-slider-block/src/components/Body.jsx");
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var _plone_volto_icons_right_key_svg__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @plone/volto/icons/right-key.svg */ "./node_modules/@plone/volto/src/icons/right-key.svg");
/* harmony import */ var _plone_volto_icons_right_key_svg__WEBPACK_IMPORTED_MODULE_9___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_right_key_svg__WEBPACK_IMPORTED_MODULE_9__);
/* harmony import */ var _plone_volto_icons_left_key_svg__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @plone/volto/icons/left-key.svg */ "./node_modules/@plone/volto/src/icons/left-key.svg");
/* harmony import */ var _plone_volto_icons_left_key_svg__WEBPACK_IMPORTED_MODULE_10___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_left_key_svg__WEBPACK_IMPORTED_MODULE_10__);
/* harmony import */ var _icons_teaser_template_svg__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! ../icons/teaser-template.svg */ "./node_modules/@kitconcept/volto-slider-block/src/icons/teaser-template.svg");
/* harmony import */ var _icons_teaser_template_svg__WEBPACK_IMPORTED_MODULE_11___default = /*#__PURE__*/__webpack_require__.n(_icons_teaser_template_svg__WEBPACK_IMPORTED_MODULE_11__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__);

var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/node_modules/@kitconcept/volto-slider-block/src/components/View.jsx";

function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); if (enumerableOnly) { symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; }); } keys.push.apply(keys, symbols); } return keys; }

function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i] != null ? arguments[i] : {}; if (i % 2) { ownKeys(Object(source), true).forEach(function (key) { _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(target, key, source[key]); }); } else if (Object.getOwnPropertyDescriptors) { Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)); } else { ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } } return target; }















const messages = Object(react_intl__WEBPACK_IMPORTED_MODULE_5__["defineMessages"])({
  PleaseChooseContent: {
    "id": "Please choose an existing content as source for this element",
    "defaultMessage": "Please choose an existing content as source for this element"
  }
});

const PrevArrow = ({
  className,
  style,
  onClick
}) => /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])("button", {
  className: className,
  style: _objectSpread(_objectSpread({}, style), {}, {
    display: 'block'
  }),
  onClick: onClick,
  children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_8__["Icon"], {
    name: _plone_volto_icons_left_key_svg__WEBPACK_IMPORTED_MODULE_10___default.a,
    size: "48px"
  })
});

const NextArrow = ({
  className,
  style,
  onClick
}) => /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])("button", {
  className: className,
  style: _objectSpread(_objectSpread({}, style), {}, {
    display: 'block'
  }),
  onClick: onClick,
  children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_8__["Icon"], {
    name: _plone_volto_icons_right_key_svg__WEBPACK_IMPORTED_MODULE_9___default.a,
    size: "48px"
  })
});

const SliderView = props => {
  var _data$slides, _data$slides2;

  const {
    className,
    data,
    isEditMode,
    block,
    openObjectBrowser,
    onChangeBlock,
    slideIndex,
    setSlideIndex
  } = props;
  const intl = Object(react_intl__WEBPACK_IMPORTED_MODULE_5__["useIntl"])();
  const sliderRef = react__WEBPACK_IMPORTED_MODULE_1___default.a.useRef();

  if (sliderRef.current && isEditMode) {
    // This syncs the current slide with the objectwidget (or other sources
    // able to access the slider context)
    // that can modify the SliderContext (and come here via props slideIndex)
    sliderRef.current.slickGoTo(slideIndex);
  }

  return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsxs"])("div", {
    className: classnames__WEBPACK_IMPORTED_MODULE_4___default()('block slider', className),
    children: [(((_data$slides = data.slides) === null || _data$slides === void 0 ? void 0 : _data$slides.length) === 0 || !data.slides) && isEditMode && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Message"], {
      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsxs"])("div", {
        className: "teaser-item default",
        children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])("img", {
          src: _icons_teaser_template_svg__WEBPACK_IMPORTED_MODULE_11___default.a,
          alt: ""
        }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])("p", {
          children: intl.formatMessage(messages.PleaseChooseContent)
        })]
      })
    }), ((_data$slides2 = data.slides) === null || _data$slides2 === void 0 ? void 0 : _data$slides2.length) > 0 && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])(react_slick__WEBPACK_IMPORTED_MODULE_3___default.a, {
      ref: sliderRef,
      dots: true,
      infinite: true,
      speed: 500,
      slidesToShow: 1,
      slidesToScroll: 1,
      draggable: false,
      nextArrow: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])(NextArrow, {}),
      prevArrow: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])(PrevArrow, {}),
      slideWidth: "1200px" // This syncs the current slide with the SliderContext state
      // responding to the slide change event from the slider itself
      // (the dots or the arrows)
      // There's also the option of doing it before instead than after:
      // beforeChange={(current, next) => setSlideIndex(next)}
      ,
      afterChange: current => isEditMode && setSlideIndex(current),
      children: data.slides && data.slides.map((item, index) => /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_12__["jsx"])("div", {
        children: /*#__PURE__*/Object(react__WEBPACK_IMPORTED_MODULE_1__["createElement"])(_Body__WEBPACK_IMPORTED_MODULE_6__["default"], _objectSpread(_objectSpread({}, props), {}, {
          key: item['@id'],
          data: item,
          isEditMode: isEditMode,
          dataBlock: data,
          index: index,
          block: block,
          openObjectBrowser: openObjectBrowser,
          onChangeBlock: onChangeBlock,
          __source: {
            fileName: _jsxFileName,
            lineNumber: 95,
            columnNumber: 17
          }
        }))
      }, item['@id']))
    })]
  });
};

/* harmony default export */ __webpack_exports__["default"] = (Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_7__["withBlockExtensions"])(SliderView));

/***/ })

};
//# sourceMappingURL=server.5c4d3be156e01d8f8179.hot-update.js.map