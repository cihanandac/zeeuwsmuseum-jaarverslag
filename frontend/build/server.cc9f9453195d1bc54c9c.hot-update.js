exports.id = "server";
exports.modules = {

/***/ "./src/customizations/components/theme/Footer/Footer.jsx":
/*!***************************************************************!*\
  !*** ./src/customizations/components/theme/Footer/Footer.jsx ***!
  \***************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! semantic-ui-react */ "semantic-ui-react");
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(semantic_ui_react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-intl */ "react-intl");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react_intl__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react-redux */ "react-redux");
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react_redux__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _plone_volto_registry__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @plone/volto/registry */ "./node_modules/@plone/volto/src/registry.js");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_6__);
var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/customizations/components/theme/Footer/Footer.jsx";

/**
 * Footer component.
 * @module components/theme/Footer/Footer
 */









const messages = Object(react_intl__WEBPACK_IMPORTED_MODULE_3__["defineMessages"])({
  copyright: {
    "id": "Copyright",
    "defaultMessage": "Copyright"
  }
});
/**
 * Component to display the footer.
 * @function Footer
 * @param {Object} intl Intl object
 * @returns {string} Markup of the component
 */

const Footer = ({
  intl
}) => {
  const {
    settings
  } = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_5__["default"];
  const lang = Object(react_redux__WEBPACK_IMPORTED_MODULE_4__["useSelector"])(state => state.intl.locale);
  return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_6__["jsxs"])("container", {
    id: "footer",
    children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_6__["jsxs"])("div", {
      id: "top-footer",
      children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_6__["jsxs"])("div", {
        className: "footerInfoBox",
        children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_6__["jsx"])("a", {
          className: "footerHeader",
          href: "#",
          children: "BEZOKADRES"
        }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_6__["jsx"])("p", {
          children: "Abdij (Plein)"
        }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_6__["jsx"])("p", {
          children: "4331 BK, Middleburg"
        }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_6__["jsx"])("a", {
          "data-val": "c803c1d94ddb4ad1a70433bafe800b6b",
          href: "https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/praktische-info",
          "data-linktype": "internal",
          className: "text-button",
          children: "Plan een bezoek"
        })]
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_6__["jsxs"])("div", {
        className: "footerInfoBox",
        children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_6__["jsx"])("a", {
          href: "#",
          children: "CONTACT ALGEMEEN"
        }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_6__["jsx"])("p", {
          id: "photoNumber",
          children: "+31 (0) 118 653000"
        }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_6__["jsx"])("a", {
          href: "info@zeeuwsmuseum.nl",
          children: "info@zeeuwsmuseum.nl"
        }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_6__["jsx"])("a", {
          "data-val": "b1eeaf8ca0ec43da9e8b294608d759a5",
          href: "https://www.zeeuwsmuseum.nl/nl/contact",
          "data-linktype": "internal",
          className: "text-button",
          children: "Contact"
        })]
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_6__["jsxs"])("div", {
        id: "footermail",
        className: "footerInfoBox",
        children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_6__["jsx"])("a", {
          href: "#",
          children: "NIEUWSBRIEF"
        }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_6__["jsx"])("p", {
          children: " Schrijf je in voor onze nieuwsbrief en blijf op de hoogte. "
        })]
      })]
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_6__["jsx"])("div", {
      id: "bottom-footer",
      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_6__["jsx"])("div", {
        id: "footerdown",
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_6__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_2__["Logo"], {
          id: "footerLogo"
        })
      })
    })]
  });
};
/**
 * Property types.
 * @property {Object} propTypes Property types.
 * @static
 */


Footer.propTypes = {
  /**
   * i18n object
   */
};
/* harmony default export */ __webpack_exports__["default"] = (Object(react_intl__WEBPACK_IMPORTED_MODULE_3__["injectIntl"])(Footer));

/***/ })

};
//# sourceMappingURL=server.cc9f9453195d1bc54c9c.hot-update.js.map