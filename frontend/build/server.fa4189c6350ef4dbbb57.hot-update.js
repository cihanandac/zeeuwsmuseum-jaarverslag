exports.id = "server";
exports.modules = {

/***/ "./src/components/Blocks/Mainslider/Edit.jsx":
/*!***************************************************!*\
  !*** ./src/components/Blocks/Mainslider/Edit.jsx ***!
  \***************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/defineProperty */ "@babel/runtime/helpers/defineProperty");
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _View__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./View */ "./src/components/Blocks/Mainslider/View.jsx");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__);

var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/components/Blocks/Mainslider/Edit.jsx";

function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); if (enumerableOnly) { symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; }); } keys.push.apply(keys, symbols); } return keys; }

function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i] != null ? arguments[i] : {}; if (i % 2) { ownKeys(Object(source), true).forEach(function (key) { _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(target, key, source[key]); }); } else if (Object.getOwnPropertyDescriptors) { Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)); } else { ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } } return target; }





const Edit = props => {
  return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsx"])(_View__WEBPACK_IMPORTED_MODULE_2__["default"], _objectSpread({}, props));
};

/* harmony default export */ __webpack_exports__["default"] = (Edit);

/***/ }),

/***/ "./src/components/Blocks/Mainslider/View.jsx":
/*!***************************************************!*\
  !*** ./src/components/Blocks/Mainslider/View.jsx ***!
  \***************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1__);
var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/components/Blocks/Mainslider/View.jsx";
// import React from 'react';
// import Slider from 'react-slick';
// import { Link } from 'react-router-dom';
// import { Button } from 'semantic-ui-react';
// import { Icon } from '@plone/volto/components';
// // import sliderPNG from './slider-image.png';
// import rightSVG from '@plone/volto/icons/right-key.svg';
// import leftSVG from '@plone/volto/icons/left-key.svg';
// import { withBlockExtensions } from '@plone/volto/helpers';
// const NextArrow = ({ className, style, onClick }) => (
//   <Button
//     className={className}
//     style={{ ...style, display: 'block' }}
//     onClick={onClick}
//   >
//     <Icon name={rightSVG} size="70px" color="#fff" />
//   </Button>
// );
// const PrevArrow = ({ className, style, onClick }) => (
//   <Button
//     className={className}
//     style={{ ...style, display: 'block' }}
//     onClick={onClick}
//   >
//     <Icon name={leftSVG} size="70px" color="#fff" />
//   </Button>
// );
// const View = (props) => {
//   return (
//     <div
//       className="block view mainslider full-width"
//       style={{
//         background: `black center no-repeat`,
//       }}
//     >
//       <Slider
//         customPaging={(dot) => <div />}
//         dots={true}
//         fade
//         dotsClass="slick-dots slick-thumb"
//         infinite
//         speed={500}
//         slidesToShow={1}
//         slidesToScroll={1}
//         nextArrow={<NextArrow />}
//         prevArrow={<PrevArrow />}
//       >
//         <div>
//           <div className="slide slide1">
//             <h3>Plone</h3>
//             <h1>
//               The Ultimate <br />
//               Open Source Enterprise CMS
//             </h1>
//             <Link to="/plone5">Learn about Plone 5</Link>
//           </div>
//         </div>
//       </Slider>
//     </div>
//   );
// };
// export default View;



const View = props => {
  return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1__["jsx"])("div", {
    children: "I'm the MainSlider view component!"
  });
};

/* harmony default export */ __webpack_exports__["default"] = (View);

/***/ }),

/***/ "./src/components/index.js":
/*!*********************************!*\
  !*** ./src/components/index.js ***!
  \*********************************/
/*! exports provided: MainSliderViewBlock, MainSliderEditBlock */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _Blocks_Mainslider_View__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./Blocks/Mainslider/View */ "./src/components/Blocks/Mainslider/View.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "MainSliderViewBlock", function() { return _Blocks_Mainslider_View__WEBPACK_IMPORTED_MODULE_0__["default"]; });

/* harmony import */ var _Blocks_Mainslider_Edit__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./Blocks/Mainslider/Edit */ "./src/components/Blocks/Mainslider/Edit.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "MainSliderEditBlock", function() { return _Blocks_Mainslider_Edit__WEBPACK_IMPORTED_MODULE_1__["default"]; });

/**
 * Add your components here.
 * 
 * @module components
 * @example
 * import Footer from './Footer/Footer';
 *
 * export {
 *   Footer,
 * };
 */




/***/ })

};
//# sourceMappingURL=server.fa4189c6350ef4dbbb57.hot-update.js.map