exports.id = "server";
exports.modules = {

/***/ "./src/customizations/components/theme/Navigation/Accordion.jsx":
/*!**********************************************************************!*\
  !*** ./src/customizations/components/theme/Navigation/Accordion.jsx ***!
  \**********************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "default", function() { return AccordionMenu; });
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/defineProperty */ "@babel/runtime/helpers/defineProperty");
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! semantic-ui-react */ "semantic-ui-react");
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__);

var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/customizations/components/theme/Navigation/Accordion.jsx";





const ColorForm = /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"], {
  children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"].Group, {
    grouped: true,
    children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"].Checkbox, {
      label: "Red",
      name: "color",
      value: "red"
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"].Checkbox, {
      label: "Orange",
      name: "color",
      value: "orange"
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"].Checkbox, {
      label: "Green",
      name: "color",
      value: "green"
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"].Checkbox, {
      label: "Blue",
      name: "color",
      value: "blue"
    })]
  })
});

const SizeForm = /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"], {
  children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"].Group, {
    grouped: true,
    children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"].Radio, {
      label: "Small",
      name: "size",
      type: "radio",
      value: "small"
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"].Radio, {
      label: "Medium",
      name: "size",
      type: "radio",
      value: "medium"
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"].Radio, {
      label: "Large",
      name: "size",
      type: "radio",
      value: "large"
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"].Radio, {
      label: "X-Large",
      name: "size",
      type: "radio",
      value: "x-large"
    })]
  })
});

class AccordionMenu extends react__WEBPACK_IMPORTED_MODULE_1__["Component"] {
  constructor(...args) {
    super(...args);

    _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(this, "state", {
      activeIndex: 0
    });

    _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(this, "handleClick", (e, titleProps) => {
      const {
        index
      } = titleProps;
      const {
        activeIndex
      } = this.state;
      const newIndex = activeIndex === index ? -1 : index;
      this.setState({
        activeIndex: newIndex
      });
    });
  }

  render() {
    const {
      activeIndex
    } = this.state;
    return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Accordion"], {
      as: semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Menu"],
      vertical: true,
      children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Menu"].Item, {
        children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Accordion"].Title, {
          active: activeIndex === 0,
          content: "Size",
          index: 0,
          onClick: this.handleClick
        }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Accordion"].Content, {
          active: activeIndex === 0,
          content: SizeForm
        })]
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Menu"].Item, {
        children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Accordion"].Title, {
          active: activeIndex === 1,
          content: "Colors",
          index: 1,
          onClick: this.handleClick
        }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_3__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Accordion"].Content, {
          active: activeIndex === 1,
          content: ColorForm
        })]
      })]
    });
  }

}

/***/ }),

/***/ "./src/customizations/components/theme/Navigation/NavItem.jsx":
/*!********************************************************************!*\
  !*** ./src/customizations/components/theme/Navigation/NavItem.jsx ***!
  \********************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react-router-dom */ "react-router-dom");
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react_router_dom__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var _plone_volto_registry__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @plone/volto/registry */ "./node_modules/@plone/volto/src/registry.js");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__);
var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/customizations/components/theme/Navigation/NavItem.jsx";







const NavItem = ({
  item,
  lang
}) => {
  const {
    settings
  } = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_3__["default"]; // The item.url in the root is ''
  // TODO: make more consistent it everywhere (eg. reducers to return '/' instead of '')

  if (Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_2__["isInternalURL"])(item.url) || item.url === '') {
    return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsxs"])(NavItem, {
      children: ["to=", item.url === '' ? '/' : item.url, "key=", item.url, "className=\"item\" activeClassName=\"active\" exact=", settings.isMultilingual ? item.url === `/${lang}` : item.url === '', ">", item.title]
    });
  } else {
    return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])("a", {
      href: item.url,
      className: "item",
      rel: "noopener noreferrer",
      children: item.title
    }, item.url);
  }
};

/* harmony default export */ __webpack_exports__["default"] = (NavItem);

/***/ }),

/***/ "./src/customizations/components/theme/Navigation/NavItems.jsx":
/*!*********************************************************************!*\
  !*** ./src/customizations/components/theme/Navigation/NavItems.jsx ***!
  \*********************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _NavItem__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./NavItem */ "./src/customizations/components/theme/Navigation/NavItem.jsx");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_2__);
var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/customizations/components/theme/Navigation/NavItems.jsx";





const NavItems = ({
  items,
  lang
}) => {
  return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_2__["jsx"])(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_2__["Fragment"], {
    children: items.map(item => /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_2__["jsx"])(_NavItem__WEBPACK_IMPORTED_MODULE_1__["default"], {
      item: item,
      lang: lang
    }, item.url))
  });
};

/* harmony default export */ __webpack_exports__["default"] = (NavItems); // import React from 'react';
// import NavItem from '@plone/volto/components/theme/Navigation/NavItem';
// import { Dropdown } from 'semantic-ui-react';
// const NavItems = ({ items, lang }) => {
//   return (
//     <>
//       {items.map((item) =>
//         item && item.items && item.items.length > 0 ? (
//           <Dropdown text={item.title} className="item" key={item.url}>
//             <Dropdown.Menu key={item.url}>
//               {item.items.map((dropdownitem) => (
//                 <NavItem
//                   item={dropdownitem}
//                   lang={lang}
//                   key={dropdownitem.url}
//                 />
//               ))}
//             </Dropdown.Menu>
//           </Dropdown>
//         ) : (
//           <NavItem item={item} lang={lang} key={item.url} />
//         ),
//       )}
//     </>
//   );
// };
// export default NavItems;

/***/ }),

/***/ "./src/customizations/components/theme/Navigation/Navigation.jsx":
/*!***********************************************************************!*\
  !*** ./src/customizations/components/theme/Navigation/Navigation.jsx ***!
  \***********************************************************************/
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
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-redux */ "react-redux");
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react_redux__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var redux__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! redux */ "redux");
/* harmony import */ var redux__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(redux__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! react-intl */ "react-intl");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(react_intl__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! semantic-ui-react */ "semantic-ui-react");
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var classnames__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! classnames */ "classnames");
/* harmony import */ var classnames__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(classnames__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var _plone_volto_registry__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @plone/volto/registry */ "./node_modules/@plone/volto/src/registry.js");
/* harmony import */ var _plone_volto_actions__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @plone/volto/actions */ "./node_modules/@plone/volto/src/actions/index.js");
/* harmony import */ var react_transition_group__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! react-transition-group */ "react-transition-group");
/* harmony import */ var react_transition_group__WEBPACK_IMPORTED_MODULE_11___default = /*#__PURE__*/__webpack_require__.n(react_transition_group__WEBPACK_IMPORTED_MODULE_11__);
/* harmony import */ var _plone_volto_components_theme_Navigation_NavItems__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! @plone/volto/components/theme/Navigation/NavItems */ "./src/customizations/components/theme/Navigation/NavItems.jsx");
/* harmony import */ var react_icons_fa__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! react-icons/fa */ "react-icons/fa");
/* harmony import */ var react_icons_fa__WEBPACK_IMPORTED_MODULE_13___default = /*#__PURE__*/__webpack_require__.n(react_icons_fa__WEBPACK_IMPORTED_MODULE_13__);
/* harmony import */ var _Accordion__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! ./Accordion */ "./src/customizations/components/theme/Navigation/Accordion.jsx");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__);

var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/customizations/components/theme/Navigation/Navigation.jsx";

/**
 * Navigation components.
 * @module components/theme/Navigation/Navigation
 */
// import { BsChevronDown } from 'react-icons/bs';
















const messages = Object(react_intl__WEBPACK_IMPORTED_MODULE_5__["defineMessages"])({
  closeMobileMenu: {
    "id": "Close menu",
    "defaultMessage": "Close menu"
  },
  openMobileMenu: {
    "id": "Open menu",
    "defaultMessage": "Open menu"
  }
});
/**
 * Navigation container class.
 * @class Navigation
 * @extends Component
 */

class Navigation extends react__WEBPACK_IMPORTED_MODULE_1__["Component"] {
  /**
   * Property types.
   * @property {Object} propTypes Property types.
   * @static
   */

  /**
   * Constructor
   * @method constructor
   * @param {Object} props Component properties
   * @constructs Navigation
   */
  constructor(props) {
    super(props);
    this.toggleMobileMenu = this.toggleMobileMenu.bind(this);
    this.closeMobileMenu = this.closeMobileMenu.bind(this);
    this.state = {
      isMobileMenuOpen: false
    };
  }

  componentDidMount() {
    const {
      settings
    } = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_9__["default"];

    if (!Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_8__["hasApiExpander"])('navigation', Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_8__["getBaseUrl"])(this.props.pathname))) {
      this.props.getNavigation(Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_8__["getBaseUrl"])(this.props.pathname), settings.navDepth);
    }
  }
  /**
   * Component will receive props
   * @method componentWillReceiveProps
   * @param {Object} nextProps Next properties
   * @returns {undefined}
   */


  UNSAFE_componentWillReceiveProps(nextProps) {
    const {
      settings
    } = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_9__["default"];

    if (nextProps.pathname !== this.props.pathname || nextProps.token !== this.props.token) {
      if (!Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_8__["hasApiExpander"])('navigation', Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_8__["getBaseUrl"])(this.props.pathname))) {
        this.props.getNavigation(Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_8__["getBaseUrl"])(nextProps.pathname), settings.navDepth);
      }
    }
  }
  /**
   * Toggle mobile menu's open state
   * @method toggleMobileMenu
   * @returns {undefined}
   */


  toggleMobileMenu() {
    this.setState({
      isMobileMenuOpen: !this.state.isMobileMenuOpen
    });
  }
  /**
   * Close mobile menu
   * @method closeMobileMenu
   * @returns {undefined}
   */


  closeMobileMenu() {
    if (!this.state.isMobileMenuOpen) {
      return;
    }

    this.setState({
      isMobileMenuOpen: false
    });
  }
  /**
   * Render method.
   * @method render
   * @returns {string} Markup for the component.
   */


  render() {
    const {
      activeIndex
    } = this.state;

    const PlanContent = /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsxs"])("div", {
      children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
          href: "https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/praktische-info",
          children: "Praktische informatie"
        })
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
          href: "https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/nu-in-het-museum",
          children: "Zien en doen"
        })
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
          href: "https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/kinderen-klas-of-groep",
          children: "Families, groupen en scholen"
        })
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
          href: "https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/leukdagjeuit",
          children: "Dagje uit Middelburg"
        })
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
          href: "https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/boek-je-bezoek",
          children: "Boek je bezoek"
        })
      })]
    });

    const OntdekContent = /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsxs"])("div", {
      children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
          href: "https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/praktische-info",
          children: "Praktische informatie"
        })
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
          href: "https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/nu-in-het-museum",
          children: "Zien en doen"
        })
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
          href: "https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/kinderen-klas-of-groep",
          children: "Families, groupen en scholen"
        })
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
          href: "https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/leukdagjeuit",
          children: "Dagje uit Middelburg"
        })
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
          href: "https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/boek-je-bezoek",
          children: "Boek je bezoek"
        })
      })]
    });

    const OverContent = /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsxs"])("div", {
      children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
          href: "https://www.zeeuwsmuseum.nl/nl/over-het-museum/steun-het-museum",
          children: "Steun het museum"
        })
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
          href: "https://www.zeeuwsmuseum.nl/nl/over-het-museum/pers",
          children: "Pers"
        })
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsxs"])("div", {
        children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
          href: "https://www.zeeuwsmuseum.nl/nl/over-het-museum/organisatie",
          children: "Organisatie"
        }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
          children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
            href: "https://www.zeeuwsmuseum.nl/nl/over-het-museum/publicaties",
            children: "Publicaties"
          })
        })]
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
          href: "https://www.zeeuwsmuseum.nl/nl/over-het-museum/voorwaarden",
          children: "Voorwaarden"
        })
      })]
    });

    const rootPanels = [{
      key: 'panel-1',
      title: 'PLAN JE BEZOEK',
      content: {
        content: PlanContent
      }
    }, {
      key: 'panel-2',
      title: 'ONTDEK',
      content: {
        content: OntdekContent
      }
    }, {
      key: 'panel-2',
      title: 'OVER HET MUSEUM',
      content: {
        content: OverContent
      }
    }];
    return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsxs"])("nav", {
      className: "navigation",
      id: "navigation",
      "aria-label": "navigation",
      children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
        className: "hamburger-wrapper mobile tablet only",
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("button", {
          className: classnames__WEBPACK_IMPORTED_MODULE_7___default()('hamburger hamburger--spin', {
            'is-active': this.state.isMobileMenuOpen
          }),
          "aria-label": this.state.isMobileMenuOpen ? this.props.intl.formatMessage(messages.closeMobileMenu, {
            type: this.props.type
          }) : this.props.intl.formatMessage(messages.openMobileMenu, {
            type: this.props.type
          }),
          title: this.state.isMobileMenuOpen ? this.props.intl.formatMessage(messages.closeMobileMenu, {
            type: this.props.type
          }) : this.props.intl.formatMessage(messages.openMobileMenu, {
            type: this.props.type
          }),
          type: "button",
          onClick: this.toggleMobileMenu,
          children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("span", {
            className: "hamburger-box",
            children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("span", {
              className: "hamburger-inner"
            })
          })
        })
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Menu"], {
        stackable: true,
        pointing: true,
        secondary: true,
        className: "computer large screen widescreen only",
        onClick: this.closeMobileMenu,
        children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Menu"].Item, {
          name: "editorials",
          onClick: this.handleItemClick,
          href: "http://volto.cihanandac.net",
          children: "JAARVERSLAG"
        }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"], {
          item: true,
          icon: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(react_icons_fa__WEBPACK_IMPORTED_MODULE_13__["FaChevronDown"], {}),
          simple: true,
          text: "PLAN JE BEZOEK",
          children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Menu, {
            children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Item, {
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
                href: "https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/praktische-info",
                children: "Praktische informatie"
              })
            }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Item, {
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
                href: "https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/nu-in-het-museum",
                children: "Zien en doen"
              })
            }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Item, {
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
                href: "https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/kinderen-klas-of-groep",
                children: "Families, groupen en scholen"
              })
            }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Item, {
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
                href: "https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/leukdagjeuit",
                children: "Dagje uit Middelburg"
              })
            }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Item, {
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
                href: "https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/boek-je-bezoek",
                children: "Boek je bezoek"
              })
            })]
          })
        }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"], {
          item: true,
          icon: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(react_icons_fa__WEBPACK_IMPORTED_MODULE_13__["FaChevronDown"], {}),
          simple: true,
          text: "ONTDEK",
          children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Menu, {
            children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Item, {
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
                href: "https://www.zeeuwsmuseum.nl/nl/videotheek",
                children: "Videotheek"
              })
            }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Item, {
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
                href: "https://www.zeeuwsmuseum.nl/nl/collectie/mode-en-streekdracht",
                children: "Mode en streekdracht"
              })
            }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Item, {
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
                href: "https://www.zeeuwsmuseum.nl/nl/collectie/wandtapijten",
                children: "Wandtapijten"
              })
            }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Item, {
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
                href: "https://www.zeeuwsmuseum.nl/nl/collectie/geschiedenis-en-archeologie",
                children: "Geschiedenis en archeologie"
              })
            }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Item, {
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
                href: "https://www.zeeuwsmuseum.nl/nl/collectie/kunst",
                children: "Kunst"
              })
            }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Item, {
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
                href: "https://www.zeeuwsmuseum.nl/nl/collectie/kunstnijverheid",
                children: "Kunstnijverheid"
              })
            }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Item, {
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
                href: "https://www.zeeuwsmuseum.nl/nl/collectie/natuurhistorie",
                children: "Natuurhistorie"
              })
            })]
          })
        }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"], {
          item: true,
          icon: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(react_icons_fa__WEBPACK_IMPORTED_MODULE_13__["FaChevronDown"], {}),
          simple: true,
          text: "OVER HET MUSEUM",
          children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Menu, {
            children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Item, {
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
                href: "https://www.zeeuwsmuseum.nl/nl/over-het-museum/steun-het-museum",
                children: "Steun het museum"
              })
            }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Item, {
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
                href: "https://www.zeeuwsmuseum.nl/nl/over-het-museum/pers",
                children: "Pers"
              })
            }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Item, {
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
                href: "https://www.zeeuwsmuseum.nl/nl/over-het-museum/organisatie",
                children: "Organisatie"
              })
            }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Item, {
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
                href: "https://www.zeeuwsmuseum.nl/nl/over-het-museum/publicaties",
                children: "Publicaties"
              })
            }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Dropdown"].Item, {
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("a", {
                href: "https://www.zeeuwsmuseum.nl/nl/over-het-museum/voorwaarden",
                children: "Voorwaarden"
              })
            })]
          })
        }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Menu"].Item, {
          name: "editorials",
          onClick: this.handleItemClick,
          href: "https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/boek-je-bezoek",
          children: "TICKETS"
        })]
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(react_transition_group__WEBPACK_IMPORTED_MODULE_11__["CSSTransition"], {
        in: this.state.isMobileMenuOpen,
        timeout: 500,
        classNames: "mobile-menu",
        unmountOnExit: true,
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsxs"])("div", {
          className: "mobile-menu",
          children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_8__["BodyClass"], {
            className: "has-mobile-menu-open"
          }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsxs"])("div", {
            className: "mobile-menu-nav",
            children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Menu"].Item, {
                name: "editorials",
                onClick: this.handleItemClick,
                href: "http://volto.cihanandac.net",
                children: "JAARVERSLAG"
              })
            }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])("div", {
              children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Accordion"], {
                className: "accordion",
                children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Accordion"].Title, {
                  content: "sdfasdfsdf",
                  onClick: this.handleClick
                }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Accordion"].Content, {
                  content: PlanContent
                }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Accordion"].Title, {
                  content: "Colors",
                  onClick: this.handleClick
                }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_15__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_6__["Accordion"].Content, {
                  content: PlanContent
                })]
              })
            })]
          })]
        }, "mobile-menu-key")
      })]
    });
  }

}

_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(Navigation, "propTypes", {
  getNavigation: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.func.isRequired,
  pathname: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string.isRequired,
  items: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.arrayOf(prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.shape({
    title: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string,
    url: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string
  })).isRequired,
  lang: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string.isRequired
});

/* harmony default export */ __webpack_exports__["default"] = (Object(redux__WEBPACK_IMPORTED_MODULE_4__["compose"])(react_intl__WEBPACK_IMPORTED_MODULE_5__["injectIntl"], Object(react_redux__WEBPACK_IMPORTED_MODULE_3__["connect"])(state => ({
  token: state.userSession.token,
  items: state.navigation.items,
  lang: state.intl.locale
}), {
  getNavigation: _plone_volto_actions__WEBPACK_IMPORTED_MODULE_10__["getNavigation"]
}))(Navigation));

/***/ })

};
//# sourceMappingURL=server.69d832196334f79ca387.hot-update.js.map