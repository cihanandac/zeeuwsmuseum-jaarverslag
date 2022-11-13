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
/* harmony import */ var react_icons_fa__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react-icons/fa */ "react-icons/fa");
/* harmony import */ var react_icons_fa__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react_icons_fa__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_icons_io__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react-icons/io */ "react-icons/io");
/* harmony import */ var react_icons_io__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react_icons_io__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var react_icons_im__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react-icons/im */ "react-icons/im");
/* harmony import */ var react_icons_im__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(react_icons_im__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! semantic-ui-react */ "semantic-ui-react");
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(semantic_ui_react__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! react-intl */ "react-intl");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(react_intl__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! react-redux */ "react-redux");
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(react_redux__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _plone_volto_registry__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @plone/volto/registry */ "./node_modules/@plone/volto/src/registry.js");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__);
var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/customizations/components/theme/Footer/Footer.jsx";

/**
 * Footer component.
 * @module components/theme/Footer/Footer
 */












const messages = Object(react_intl__WEBPACK_IMPORTED_MODULE_6__["defineMessages"])({
  copyright: {
    "id": "Copyright",
    "defaultMessage": "Copyright"
  }
}); // const pagetype = document.getElementById('field-Page_Type').childNodes[1].children[0].children[0].children[0].firstChild.wholeText;

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
  } = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_8__["default"];
  const lang = Object(react_redux__WEBPACK_IMPORTED_MODULE_7__["useSelector"])(state => state.intl.locale); // {
  //   document.getElementById('field-Page_Type').childNodes[1].children[0]
  //     .children[0].children[0].firstChild.wholeText === 'Jaarverslag Folder' ?
  //     (document.getElementById('footer').className = 'invisibleFooter') : (document.getElementById('footer').className = 'visibleFooter');
  // }

  {
    pagetype == "Jaarverslag Folder" ? console.log("yes") : console.log("no");
  }
  ;
  return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsxs"])("container", {
    id: "footer",
    children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("div", {
      id: "top-footer",
      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsxs"])("div", {
        className: "top-wrapper",
        id: "top-wrap",
        children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsxs"])("div", {
          className: "footerInfoBox",
          children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("div", {
            className: "titleWrapper",
            children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("a", {
              href: "https://www.zeeuwsmuseum.nl/nl/zeeuws-museum-v4/#",
              children: "BEZOKADRES"
            })
          }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("p", {
            children: "Abdij (Plein)"
          }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("p", {
            id: "address",
            children: "4331 BK, Middleburg"
          }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("a", {
            href: "https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/praktische-info",
            className: "text-button",
            children: "Plan een bezoek"
          })]
        }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsxs"])("div", {
          className: "footerInfoBox",
          children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("div", {
            className: "titleWrapper",
            children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("a", {
              href: "https://www.zeeuwsmuseum.nl/nl/contact",
              children: "CONTACT ALGEMEEN"
            })
          }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("p", {
            id: "phoneNumber",
            children: "+31 (0) 118 653000"
          }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("a", {
            id: "mailadress",
            "data-linktype": "email",
            href: "mailto:info@zeeuwsmuseum.nl?subject=Contact%20via Zeeuws Museum website",
            "data-val": "info@zeeuwsmuseum.nl",
            "data-subject": "Contact via Zeeuws Museum website",
            children: "info@zeeuwsmuseum.nl"
          }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("a", {
            href: "https://www.zeeuwsmuseum.nl/nl/contact",
            className: "text-button",
            children: "Contact"
          }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("a", {
            href: "https://twitter.com/Zeeuwsmuseum",
            target: "_blank",
            children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])(react_icons_io__WEBPACK_IMPORTED_MODULE_1__["IoLogoTwitter"], {
              className: "social"
            })
          }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("a", {
            href: "https://www.facebook.com/ZeeuwsMuseum",
            target: "_blank",
            children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])(react_icons_fa__WEBPACK_IMPORTED_MODULE_0__["FaFacebookF"], {
              className: "social"
            })
          }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("a", {
            href: "https://www.instagram.com/zeeuws_museum",
            target: "_blank",
            children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])(react_icons_im__WEBPACK_IMPORTED_MODULE_2__["ImInstagram"], {
              className: "social"
            })
          })]
        }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsxs"])("div", {
          id: "footermail",
          className: "footerInfoBox",
          children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("div", {
            className: "titleWrapper",
            children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("a", {
              id: "footerTitle3",
              href: "",
              children: "NIEUWSBRIEF"
            })
          }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("p", {
            children: " Schrijf je in voor onze nieuwsbrief en blijf op de hoogte. "
          }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("dd", {
            className: "portletItem odd",
            children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("form", {
              id: "newsletter-subscriber-form",
              method: "get",
              action: "https://zeeuwsmuseum.us13.list-manage.com/subscribe/post-json?c=?",
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsxs"])("div", {
                className: "input-group",
                children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("input", {
                  type: "text",
                  className: "text-widget required form-control input-lg textline-field",
                  placeholder: "Email",
                  id: "form-widgets-email",
                  name: "EMAIL",
                  "aria-label": "mailchimp-email"
                }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("input", {
                  type: "hidden",
                  value: "88e39abc49bff280b2ff566d0",
                  name: "u"
                }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("input", {
                  type: "hidden",
                  value: "5978f9fd67",
                  name: "id"
                }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("span", {
                  className: "input-group-btn",
                  children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("button", {
                    className: "submit-button",
                    name: "form.buttons.subscribe",
                    type: "submit",
                    "aria-label": "mailchimp-submit",
                    children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])(react_icons_fa__WEBPACK_IMPORTED_MODULE_0__["FaChevronRight"], {})
                  })
                })]
              })
            })
          })]
        })]
      })
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("div", {
      id: "bottom-footer",
      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("div", {
        id: "footerdown",
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_5__["Logo"], {
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
/* harmony default export */ __webpack_exports__["default"] = (Object(react_intl__WEBPACK_IMPORTED_MODULE_6__["injectIntl"])(Footer));

/***/ })

};
//# sourceMappingURL=server.e7edce74f0f79ecc426b.hot-update.js.map