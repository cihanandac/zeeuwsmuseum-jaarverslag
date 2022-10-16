exports.id = "server";
exports.modules = {

/***/ "./node_modules/@plone/volto/src/components/manage/Blocks/Block/BlocksForm.jsx":
/*!*************************************************************************************!*\
  !*** ./node_modules/@plone/volto/src/components/manage/Blocks/Block/BlocksForm.jsx ***!
  \*************************************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/defineProperty */ "@babel/runtime/helpers/defineProperty");
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _Edit__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/Block/Edit.jsx");
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var _EditBlockWrapper__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./EditBlockWrapper */ "./node_modules/@plone/volto/src/components/manage/Blocks/Block/EditBlockWrapper.jsx");
/* harmony import */ var _plone_volto_actions__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @plone/volto/actions */ "./node_modules/@plone/volto/src/actions/index.js");
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! react-redux */ "react-redux");
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(react_redux__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _plone_volto_registry__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @plone/volto/registry */ "./node_modules/@plone/volto/src/registry.js");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__);

var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/node_modules/@plone/volto/src/components/manage/Blocks/Block/BlocksForm.jsx";

function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); if (enumerableOnly) { symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; }); } keys.push.apply(keys, symbols); } return keys; }

function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i] != null ? arguments[i] : {}; if (i % 2) { ownKeys(Object(source), true).forEach(function (key) { _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(target, key, source[key]); }); } else if (Object.getOwnPropertyDescriptors) { Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)); } else { ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } } return target; }














const BlocksForm = props => {
  const {
    pathname,
    onChangeField,
    properties,
    onChangeFormData,
    selectedBlock,
    multiSelected,
    onSelectBlock,
    allowedBlocks,
    showRestricted,
    title,
    description,
    metadata,
    manage,
    children,
    isMainForm = true,
    blocksConfig = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_8__["default"].blocks.blocksConfig,
    editable = true
  } = props;
  const blockList = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_4__["getBlocks"])(properties);
  const dispatch = Object(react_redux__WEBPACK_IMPORTED_MODULE_7__["useDispatch"])();

  const ClickOutsideListener = () => {
    onSelectBlock(null);
    dispatch(Object(_plone_volto_actions__WEBPACK_IMPORTED_MODULE_6__["setSidebarTab"])(0));
  };

  const ref = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_4__["useDetectClickOutside"])({
    onTriggered: ClickOutsideListener,
    triggerKeys: ['Escape'],
    // Disabled feature for now https://github.com/plone/volto/pull/2389#issuecomment-830027413
    disableClick: true,
    disableKeys: !isMainForm
  });

  const handleKeyDown = (e, index, block, node, {
    disableEnter = false,
    disableArrowUp = false,
    disableArrowDown = false
  } = {}) => {
    const isMultipleSelection = e.shiftKey;

    if (e.key === 'ArrowUp' && !disableArrowUp) {
      onFocusPreviousBlock(block, node, isMultipleSelection);
      e.preventDefault();
    }

    if (e.key === 'ArrowDown' && !disableArrowDown) {
      onFocusNextBlock(block, node, isMultipleSelection);
      e.preventDefault();
    }

    if (e.key === 'Enter' && !disableEnter) {
      onAddBlock(_plone_volto_registry__WEBPACK_IMPORTED_MODULE_8__["default"].settings.defaultBlockType, index + 1);
      e.preventDefault();
    }
  };

  const onFocusPreviousBlock = (currentBlock, blockNode, isMultipleSelection) => {
    const prev = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_4__["previousBlockId"])(properties, currentBlock);
    if (prev === null) return;
    blockNode.blur();
    onSelectBlock(prev, isMultipleSelection);
  };

  const onFocusNextBlock = (currentBlock, blockNode, isMultipleSelection) => {
    const next = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_4__["nextBlockId"])(properties, currentBlock);
    if (next === null) return;
    blockNode.blur();
    onSelectBlock(next, isMultipleSelection);
  };

  const onMutateBlock = (id, value) => {
    const newFormData = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_4__["mutateBlock"])(properties, id, value);
    onChangeFormData(newFormData);
  };

  const onInsertBlock = (id, value, current) => {
    const [newId, newFormData] = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_4__["insertBlock"])(properties, id, value, current);
    onChangeFormData(newFormData);
    return newId;
  };

  const onAddBlock = (type, index) => {
    if (editable) {
      const [id, newFormData] = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_4__["addBlock"])(properties, type, index);
      onChangeFormData(newFormData);
      return id;
    }
  };

  const onChangeBlock = (id, value) => {
    const newFormData = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_4__["changeBlock"])(properties, id, value);
    onChangeFormData(newFormData);
  };

  const onDeleteBlock = (id, selectPrev) => {
    const previous = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_4__["previousBlockId"])(properties, id);
    const newFormData = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_4__["deleteBlock"])(properties, id);
    onChangeFormData(newFormData);
    onSelectBlock(selectPrev ? previous : null);
  };

  const onMoveBlock = (dragIndex, hoverIndex) => {
    const newFormData = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_4__["moveBlock"])(properties, dragIndex, hoverIndex);
    onChangeFormData(newFormData);
  };

  const defaultBlockWrapper = ({
    draginfo
  }, editBlock, blockProps) => /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])(_EditBlockWrapper__WEBPACK_IMPORTED_MODULE_5__["default"], {
    draginfo: draginfo,
    blockProps: blockProps,
    children: editBlock
  });

  const editBlockWrapper = children || defaultBlockWrapper;
  return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsxs"])("div", {
    className: "blocks-form",
    ref: ref,
    children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("fieldset", {
      className: "invisible",
      disabled: !editable,
      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_3__["DragDropList"], {
        childList: blockList,
        onMoveItem: result => {
          const {
            source,
            destination
          } = result;

          if (!destination) {
            return;
          }

          const newFormData = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_4__["moveBlock"])(properties, source.index, destination.index);
          onChangeFormData(newFormData);
          return true;
        },
        children: dragProps => {
          const {
            child,
            childId,
            index
          } = dragProps;
          const blockProps = {
            allowedBlocks,
            showRestricted,
            block: childId,
            data: child,
            handleKeyDown,
            id: childId,
            formTitle: title,
            formDescription: description,
            index,
            manage,
            onAddBlock,
            onInsertBlock,
            onChangeBlock,
            onChangeField,
            onChangeFormData,
            onDeleteBlock,
            onFocusNextBlock,
            onFocusPreviousBlock,
            onMoveBlock,
            onMutateBlock,
            onSelectBlock,
            pathname,
            metadata,
            properties,
            blocksConfig,
            selected: selectedBlock === childId,
            multiSelected: multiSelected === null || multiSelected === void 0 ? void 0 : multiSelected.includes(childId),
            type: child['@type'],
            editable
          };
          return editBlockWrapper(dragProps, /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])(_Edit__WEBPACK_IMPORTED_MODULE_2__["default"], _objectSpread({}, blockProps), childId), blockProps);
        }
      })
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("div", {
      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_9__["jsx"])("p", {
        children: "this is a test"
      })
    })]
  });
};

/* harmony default export */ __webpack_exports__["default"] = (BlocksForm);

/***/ })

};
//# sourceMappingURL=server.cde49f747f6527426e30.hot-update.js.map