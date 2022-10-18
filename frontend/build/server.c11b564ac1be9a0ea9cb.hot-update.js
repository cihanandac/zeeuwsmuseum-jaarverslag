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
/* harmony import */ var react_icons_fa__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-icons/fa */ "react-icons/fa");
/* harmony import */ var react_icons_fa__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react_icons_fa__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__);

var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/src/customizations/components/theme/Navigation/Accordion.jsx";






const ColorForm = /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"], {
  children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"].Group, {
    grouped: true,
    children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"].Checkbox, {
      label: "Red",
      name: "color",
      value: "red"
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"].Checkbox, {
      label: "Orange",
      name: "color",
      value: "orange"
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"].Checkbox, {
      label: "Green",
      name: "color",
      value: "green"
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"].Checkbox, {
      label: "Blue",
      name: "color",
      value: "blue"
    })]
  })
});

const SizeForm = /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"], {
  children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"].Group, {
    grouped: true,
    children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"].Radio, {
      label: "Small",
      name: "size",
      type: "radio",
      value: "small"
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"].Radio, {
      label: "Medium",
      name: "size",
      type: "radio",
      value: "medium"
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"].Radio, {
      label: "Large",
      name: "size",
      type: "radio",
      value: "large"
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Form"].Radio, {
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
    return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Accordion"], {
      as: semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Menu"],
      vertical: true,
      children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Menu"].Item, {
        children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Accordion"].Title, {
          icon: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])(react_icons_fa__WEBPACK_IMPORTED_MODULE_3__["FaChevronDown"], {}),
          active: activeIndex === 0,
          content: "Size",
          index: 0,
          onClick: this.handleClick
        }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Accordion"].Content, {
          active: activeIndex === 0,
          content: SizeForm
        })]
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsxs"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Menu"].Item, {
        children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Accordion"].Title, {
          icon: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])(react_icons_fa__WEBPACK_IMPORTED_MODULE_3__["FaChevronDown"], {}),
          active: activeIndex === 1,
          content: "Colors",
          index: 1,
          onClick: this.handleClick
        }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_2__["Accordion"].Content, {
          active: activeIndex === 1,
          content: ColorForm
        })]
      })]
    });
  }

}

/***/ })

};
//# sourceMappingURL=server.c11b564ac1be9a0ea9cb.hot-update.js.map