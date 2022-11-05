exports.id = "server";
exports.modules = {

/***/ "./src/components/Blocks/PhotoDescription/BlockSchema.js":
/*!***************************************************************!*\
  !*** ./src/components/Blocks/PhotoDescription/BlockSchema.js ***!
  \***************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (() => ({
  title: 'Educal Banner Area Block',
  fieldsets: [{
    id: 'default',
    title: 'Default',
    fields: ['photoName', 'headingLine1']
  }],
  properties: {
    tag: {
      title: 'tag',
      type: 'string'
    },
    headingLine1: {
      title: 'Heading1',
      type: 'string'
    },
    headingLine2: {
      title: 'Heading2',
      type: 'string'
    },
    showActionButton: {
      title: 'Enable button',
      type: 'boolean'
    },
    actionButtonText: {
      title: 'Button text',
      type: 'string'
    },
    actionButtonUrl: {
      title: 'Button redirect url',
      type: 'string'
    },
    foregroundImage: {
      title: 'Foreground Image',
      widget: 'attachedimage'
    },
    backgroundImage: {
      title: 'Background Image',
      widget: 'attachedimage'
    }
  },
  required: []
}));

/***/ })

};
//# sourceMappingURL=server.c93de138cd1bb6f30cf8.hot-update.js.map