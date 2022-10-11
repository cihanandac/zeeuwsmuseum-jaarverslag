exports.ids = ["vendors~PDFViewer"];
exports.modules = {

/***/ "./node_modules/@eeacms/volto-pdf-block/src/components/manage/PDFViewer/PDFViewer.jsx":
/*!********************************************************************************************!*\
  !*** ./node_modules/@eeacms/volto-pdf-block/src/components/manage/PDFViewer/PDFViewer.jsx ***!
  \********************************************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! prop-types */ "prop-types");
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(prop_types__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _plone_volto_registry__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @plone/volto/registry */ "./node_modules/@plone/volto/src/registry.js");
/* harmony import */ var _react_pdf__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./react-pdf */ "./node_modules/@eeacms/volto-pdf-block/src/components/manage/PDFViewer/react-pdf.js");
/* harmony import */ var classnames__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! classnames */ "classnames");
/* harmony import */ var classnames__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(classnames__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var _plone_volto_icons_add_svg__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @plone/volto/icons/add.svg */ "./node_modules/@plone/volto/src/icons/add.svg");
/* harmony import */ var _plone_volto_icons_add_svg__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_add_svg__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _plone_volto_icons_remove_svg__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @plone/volto/icons/remove.svg */ "./node_modules/@plone/volto/src/icons/remove.svg");
/* harmony import */ var _plone_volto_icons_remove_svg__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_remove_svg__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _plone_volto_icons_move_down_svg__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @plone/volto/icons/move-down.svg */ "./node_modules/@plone/volto/src/icons/move-down.svg");
/* harmony import */ var _plone_volto_icons_move_down_svg__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_move_down_svg__WEBPACK_IMPORTED_MODULE_8__);
/* harmony import */ var _pdf_styling_css__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./pdf-styling.css */ "./node_modules/@eeacms/volto-pdf-block/src/components/manage/PDFViewer/pdf-styling.css");
/* harmony import */ var _pdf_styling_css__WEBPACK_IMPORTED_MODULE_9___default = /*#__PURE__*/__webpack_require__.n(_pdf_styling_css__WEBPACK_IMPORTED_MODULE_9__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__);
var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/node_modules/@eeacms/volto-pdf-block/src/components/manage/PDFViewer/PDFViewer.jsx";


 // import PDF from '@mikecousins/react-pdf';







 // Based on
// https://raw.githubusercontent.com/MGrin/mgr-pdf-viewer-react/master/src/index.js



const mgrpdfStyles = {};
mgrpdfStyles.wrapper = {
  textAlign: 'center',
  width: '100%'
};

const LoaderComponent = ({
  children
}) => /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])("div", {
  className: "block pdf_viewer selected",
  tabindex: "-1",
  style: {
    outline: 'none',
    height: '100%'
  },
  children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsxs"])("div", {
    className: "ui message",
    children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])("div", {
      className: "ui active transition visible dimmer",
      style: {
        display: 'flex !important;'
      }
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])("div", {
      className: "ui active transition visible dimmer",
      style: {
        display: 'flex !important;'
      },
      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])("div", {
        className: "content",
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])("div", {
          className: "ui indeterminate text loader"
        })
      })
    }), children]
  })
});

const PDFToolbar = ({
  downloadUrl,
  onScaleUp,
  onScaleDown,
  scale_ratio
}) => /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsxs"])("div", {
  className: "pdf-toolbar pdf-toolbar-top",
  children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsxs"])("div", {
    children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])("button", {
      className: "pdf-toolbar-btn",
      title: "Zoom In",
      onClick: onScaleUp,
      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_5__["Icon"], {
        name: _plone_volto_icons_add_svg__WEBPACK_IMPORTED_MODULE_6___default.a,
        size: "15px"
      })
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])("div", {
      className: "scale-separator"
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])("button", {
      className: "pdf-toolbar-btn",
      title: "Zoom Out",
      onClick: onScaleDown,
      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_5__["Icon"], {
        name: _plone_volto_icons_remove_svg__WEBPACK_IMPORTED_MODULE_7___default.a,
        size: "15px"
      })
    }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])("p", {
      className: "scale-ratio",
      children: scale_ratio + '%'
    })]
  }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])("div", {
    children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])("a", {
      href: downloadUrl,
      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])("button", {
        className: "pdf-toolbar-btn",
        title: "Download",
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_5__["Icon"], {
          name: _plone_volto_icons_move_down_svg__WEBPACK_IMPORTED_MODULE_8___default.a,
          size: "20px"
        })
      })
    })
  })]
});

function PDFViewer({
  page = 1,
  initialScale = 1.0,
  initial_scale_ratio = 100,
  loader,
  navigation: NavigationToolbar,
  css,
  document: source,
  showNavbar = true,
  showToolbar = true,
  enableScroll = true,
  fitPageWidth = false,
  onPageRenderSuccess
}) {
  const [totalPages, setTotalPages] = react__WEBPACK_IMPORTED_MODULE_0___default.a.useState(0);
  const [currentPage, setCurrentPage] = react__WEBPACK_IMPORTED_MODULE_0___default.a.useState(page);
  const [loading, setLoading] = react__WEBPACK_IMPORTED_MODULE_0___default.a.useState(true);
  const [loaded, setLoaded] = react__WEBPACK_IMPORTED_MODULE_0___default.a.useState(false);
  const nodeRef = react__WEBPACK_IMPORTED_MODULE_0___default.a.useRef();
  const [scale_ratio, setScale_ratio] = react__WEBPACK_IMPORTED_MODULE_0___default.a.useState(initial_scale_ratio);
  const [scale, setScale] = react__WEBPACK_IMPORTED_MODULE_0___default.a.useState(initialScale);
  const [baseWidth, setBaseWidth] = react__WEBPACK_IMPORTED_MODULE_0___default.a.useState();
  react__WEBPACK_IMPORTED_MODULE_0___default.a.useLayoutEffect(() => {
    setBaseWidth(nodeRef.current.clientWidth);
  }, []);
  react__WEBPACK_IMPORTED_MODULE_0___default.a.useEffect(() => {
    setCurrentPage(page || 1);
  }, [page]);

  const increaseScale = () => {
    setScale(scale + 0.1);
    setScale_ratio(scale_ratio + 10);
  };

  const decreaseScale = () => {
    setScale(scale - 0.1);
    setScale_ratio(scale_ratio - 10);
  };

  const handlePrevClick = () => {
    if (currentPage === 1) return;
    setCurrentPage(currentPage - 1);
  };

  const handleNextClick = () => {
    if (currentPage === totalPages) return;
    setCurrentPage(currentPage + 1);
  };

  react__WEBPACK_IMPORTED_MODULE_0___default.a.useLayoutEffect(() => {
    if (!enableScroll) return;

    function handleWheel(event) {
      if (event.deltaY < 0) {
        setCurrentPage(Math.max(currentPage - 1, 1));
      } else if (event.deltaY > 0) {
        setCurrentPage(Math.min(currentPage + 1, totalPages));
      }

      event.preventDefault();
    }

    const pdfWrapper = document.querySelector('.pdf-wrapper');

    if (pdfWrapper) {
      pdfWrapper.addEventListener('wheel', handleWheel);
    }

    return () => {
      const pdfWrapper = document.querySelector('.pdf-wrapper');

      if (pdfWrapper) {
        pdfWrapper.removeEventListener('wheel', handleWheel);
      }
    };
  }, [currentPage, totalPages, enableScroll]);
  return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsxs"])("div", {
    ref: nodeRef,
    className: !loading && css ? classnames__WEBPACK_IMPORTED_MODULE_4___default()(css, 'pdf-wrapper') : classnames__WEBPACK_IMPORTED_MODULE_4___default()('mgrpdf__wrapper', 'pdf-wrapper'),
    style: mgrpdfStyles.wrapper,
    children: [showToolbar && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])(PDFToolbar, {
      onScaleUp: increaseScale,
      onScaleDown: decreaseScale,
      downloadUrl: source.url,
      scale_ratio: scale_ratio
    }), baseWidth && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])(_react_pdf__WEBPACK_IMPORTED_MODULE_3__["default"], {
      baseWidth: fitPageWidth ? baseWidth : undefined,
      file: source.file || source.url,
      content: source.base64,
      binaryContent: source.binary,
      documentInitParameters: source.connection,
      loading: loader || loading,
      page: currentPage,
      scale: scale,
      onPageRenderSuccess: (page, canvasEl, viewport) => {
        setLoading(false);
        setLoaded(true);
        onPageRenderSuccess && onPageRenderSuccess(page, canvasEl, viewport);
      },
      onPageRenderFail: () => {
        setLoading(false);
        setLoaded(false);
      },
      workerSrc: _plone_volto_registry__WEBPACK_IMPORTED_MODULE_2__["default"].settings.pdfWorkerSrc,
      onDocumentLoadSuccess: pdfDoc => {
        setLoaded(true);
        setTotalPages(pdfDoc.numPages);
      },
      children: ({
        pdfDocument,
        pdfPage,
        canvas
      }) => {
        return loaded ? canvas : /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])(LoaderComponent, {
          children: canvas
        });
      }
    }), showNavbar && totalPages > 1 ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])(NavigationToolbar, {
      page: currentPage,
      pages: totalPages,
      handleNextClick: handleNextClick,
      handlePrevClick: handlePrevClick
    }) : null]
  });
}

PDFViewer.propTypes = {
  document: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.shape({
    file: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.any,
    // File object,
    url: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,
    connection: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.shape({
      url: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string.isRequired // URL to fetch the pdf

    }),
    base64: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,
    // PDF file encoded in base64
    binary: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.shape({
      // UInt8Array
      data: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.any
    })
  }).isRequired,
  loader: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.node,
  page: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.number,
  scale: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.number,
  css: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,
  // onDocumentClick: PropTypes.func,
  // onDocumentComplete: PropTypes.func,
  hideNavbar: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.bool,
  navigation: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.oneOfType([// Can be an object with css classes or react elements to be rendered
  prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.shape({
    css: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.shape({
      previousPageBtn: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,
      nextPageBtn: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,
      pages: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,
      wrapper: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string
    }),
    elements: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.shape({
      previousPageBtn: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.any,
      nextPageBtn: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.any,
      pages: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.any
    })
  }), // Or a full navigation component
  prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.any])
};
PDFViewer.defaultProps = {
  scale: 1
};
/* harmony default export */ __webpack_exports__["default"] = (PDFViewer);

/***/ }),

/***/ "./node_modules/@eeacms/volto-pdf-block/src/components/manage/PDFViewer/react-pdf.js":
/*!*******************************************************************************************!*\
  !*** ./node_modules/@eeacms/volto-pdf-block/src/components/manage/PDFViewer/react-pdf.js ***!
  \*******************************************************************************************/
/*! exports provided: usePdf, default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "usePdf", function() { return usePdf; });
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/defineProperty */ "@babel/runtime/helpers/defineProperty");
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _babel_runtime_helpers_objectWithoutProperties__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @babel/runtime/helpers/objectWithoutProperties */ "@babel/runtime/helpers/objectWithoutProperties");
/* harmony import */ var _babel_runtime_helpers_objectWithoutProperties__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_objectWithoutProperties__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _bundled_es_modules_pdfjs_dist__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @bundled-es-modules/pdfjs-dist */ "@bundled-es-modules/pdfjs-dist");
/* harmony import */ var _bundled_es_modules_pdfjs_dist__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_bundled_es_modules_pdfjs_dist__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__);


var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/node_modules/@eeacms/volto-pdf-block/src/components/manage/PDFViewer/react-pdf.js";
const _excluded = ["file", "onDocumentLoadSuccess", "onDocumentLoadFail", "onPageLoadSuccess", "onPageLoadFail", "onPageRenderSuccess", "onPageRenderFail", "page", "scale", "rotate", "cMapUrl", "cMapPacked", "workerSrc", "withCredentials", "baseWidth", "children"];

function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); if (enumerableOnly) { symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; }); } keys.push.apply(keys, symbols); } return keys; }

function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i] != null ? arguments[i] : {}; if (i % 2) { ownKeys(Object(source), true).forEach(function (key) { _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(target, key, source[key]); }); } else if (Object.getOwnPropertyDescriptors) { Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)); } else { ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } } return target; }

// Adopted copy of MIT licensed
// https://github.com/mikecousins/react-pdf-js/blob/9afbc77a15105fb8b0332dc0e531e27ec049dad2/src/index.tsx




function isFunction(value) {
  return typeof value === 'function';
}

const Pdf = /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_3___default.a.forwardRef((_ref, ref) => {
  let {
    file,
    onDocumentLoadSuccess,
    onDocumentLoadFail,
    onPageLoadSuccess,
    onPageLoadFail,
    onPageRenderSuccess,
    onPageRenderFail,
    page,
    scale,
    rotate,
    cMapUrl,
    cMapPacked,
    workerSrc,
    withCredentials,
    baseWidth,
    children
  } = _ref,
      canvasProps = _babel_runtime_helpers_objectWithoutProperties__WEBPACK_IMPORTED_MODULE_1___default()(_ref, _excluded);

  const canvasRef = Object(react__WEBPACK_IMPORTED_MODULE_3__["useRef"])();
  Object(react__WEBPACK_IMPORTED_MODULE_3__["useImperativeHandle"])(ref, () => canvasRef.current);
  const pdfData = usePdf({
    canvasRef,
    file,
    onDocumentLoadSuccess,
    onDocumentLoadFail,
    onPageLoadSuccess,
    onPageLoadFail,
    onPageRenderSuccess,
    onPageRenderFail,
    page,
    scale,
    rotate,
    cMapUrl,
    cMapPacked,
    workerSrc,
    withCredentials,
    baseWidth
  });

  const canvas = /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_4__["jsx"])("canvas", _objectSpread(_objectSpread({}, canvasProps), {}, {
    ref: canvasRef
  }));

  if (isFunction(children)) {
    return children(_objectSpread({
      canvas
    }, pdfData));
  }

  return canvas;
});
const usePdf = ({
  canvasRef,
  file,
  onDocumentLoadSuccess,
  onDocumentLoadFail,
  onPageLoadSuccess,
  onPageLoadFail,
  onPageRenderSuccess,
  onPageRenderFail,
  scale = 1,
  rotate = 0,
  page = 1,
  cMapUrl,
  cMapPacked,
  workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${_bundled_es_modules_pdfjs_dist__WEBPACK_IMPORTED_MODULE_2___default.a.version}/pdf.worker.js`,
  withCredentials = false,
  baseWidth
}) => {
  const [pdfDocument, setPdfDocument] = Object(react__WEBPACK_IMPORTED_MODULE_3__["useState"])();
  const [pdfPage, setPdfPage] = Object(react__WEBPACK_IMPORTED_MODULE_3__["useState"])();
  const renderTask = Object(react__WEBPACK_IMPORTED_MODULE_3__["useRef"])(null);
  const onDocumentLoadSuccessRef = Object(react__WEBPACK_IMPORTED_MODULE_3__["useRef"])(onDocumentLoadSuccess);
  const onDocumentLoadFailRef = Object(react__WEBPACK_IMPORTED_MODULE_3__["useRef"])(onDocumentLoadFail);
  const onPageLoadSuccessRef = Object(react__WEBPACK_IMPORTED_MODULE_3__["useRef"])(onPageLoadSuccess);
  const onPageLoadFailRef = Object(react__WEBPACK_IMPORTED_MODULE_3__["useRef"])(onPageLoadFail);
  const onPageRenderSuccessRef = Object(react__WEBPACK_IMPORTED_MODULE_3__["useRef"])(onPageRenderSuccess);
  const onPageRenderFailRef = Object(react__WEBPACK_IMPORTED_MODULE_3__["useRef"])(onPageRenderFail); // assign callbacks to refs to avoid redrawing

  Object(react__WEBPACK_IMPORTED_MODULE_3__["useEffect"])(() => {
    onDocumentLoadSuccessRef.current = onDocumentLoadSuccess;
  }, [onDocumentLoadSuccess]);
  Object(react__WEBPACK_IMPORTED_MODULE_3__["useEffect"])(() => {
    onDocumentLoadFailRef.current = onDocumentLoadFail;
  }, [onDocumentLoadFail]);
  Object(react__WEBPACK_IMPORTED_MODULE_3__["useEffect"])(() => {
    onPageLoadSuccessRef.current = onPageLoadSuccess;
  }, [onPageLoadSuccess]);
  Object(react__WEBPACK_IMPORTED_MODULE_3__["useEffect"])(() => {
    onPageLoadFailRef.current = onPageLoadFail;
  }, [onPageLoadFail]);
  Object(react__WEBPACK_IMPORTED_MODULE_3__["useEffect"])(() => {
    onPageRenderSuccessRef.current = onPageRenderSuccess;
  }, [onPageRenderSuccess]);
  Object(react__WEBPACK_IMPORTED_MODULE_3__["useEffect"])(() => {
    onPageRenderFailRef.current = onPageRenderFail;
  }, [onPageRenderFail]);
  Object(react__WEBPACK_IMPORTED_MODULE_3__["useEffect"])(() => {
    _bundled_es_modules_pdfjs_dist__WEBPACK_IMPORTED_MODULE_2___default.a.GlobalWorkerOptions.workerSrc = workerSrc;
  }, [workerSrc]);
  Object(react__WEBPACK_IMPORTED_MODULE_3__["useEffect"])(() => {
    const config = {
      url: file,
      withCredentials
    };

    if (cMapUrl) {
      config.cMapUrl = cMapUrl;
      config.cMapPacked = cMapPacked;
    }

    _bundled_es_modules_pdfjs_dist__WEBPACK_IMPORTED_MODULE_2___default.a.getDocument(config).promise.then(loadedPdfDocument => {
      setPdfDocument(loadedPdfDocument);

      if (isFunction(onDocumentLoadSuccessRef.current)) {
        onDocumentLoadSuccessRef.current(loadedPdfDocument);
      }
    }, () => {
      if (isFunction(onDocumentLoadFailRef.current)) {
        onDocumentLoadFailRef.current();
      }
    });
  }, [file, withCredentials, cMapUrl, cMapPacked]);
  Object(react__WEBPACK_IMPORTED_MODULE_3__["useEffect"])(() => {
    // draw a page of the pdf
    const drawPDF = page => {
      // Because this page's rotation option overwrites pdf default rotation value,
      // calculating page rotation option value from pdf default and this component prop rotate.
      const rotation = rotate === 0 ? page.rotate : page.rotate + rotate;
      const dpRatio = window.devicePixelRatio;
      const CSS_UNITS = 96 / 72;
      let adjustedScale = scale * dpRatio;
      adjustedScale = baseWidth ? baseWidth / page.getViewport({
        scale: 1,
        rotation
      }).width * CSS_UNITS * 1.0 // coeficient to make it look good
      : adjustedScale;
      const viewport = page.getViewport({
        scale: adjustedScale,
        rotation
      });
      const canvasEl = canvasRef.current;

      if (!canvasEl) {
        return;
      }

      const canvasContext = canvasEl.getContext('2d');

      if (!canvasContext) {
        return;
      }

      canvasEl.style.width = `${viewport.width / dpRatio}px`;
      canvasEl.style.height = `${viewport.height / dpRatio}px`;
      canvasEl.height = viewport.height;
      canvasEl.width = viewport.width; // if previous render isn't done yet, we cancel it

      if (renderTask.current) {
        renderTask.current.cancel();
        return;
      }

      renderTask.current = page.render({
        canvasContext,
        viewport
      });
      return renderTask.current.promise.then(() => {
        renderTask.current = null;

        if (isFunction(onPageRenderSuccessRef.current)) {
          onPageRenderSuccessRef.current(page, canvasEl, viewport);
        }
      }, err => {
        renderTask.current = null; // @ts-ignore typings are outdated

        if (err && err.name === 'RenderingCancelledException') {
          drawPDF(page);
        } else if (isFunction(onPageRenderFailRef.current)) {
          onPageRenderFailRef.current();
        }
      });
    };

    if (pdfDocument) {
      pdfDocument.getPage(page).then(loadedPdfPage => {
        setPdfPage(loadedPdfPage);

        if (isFunction(onPageLoadSuccessRef.current)) {
          onPageLoadSuccessRef.current(loadedPdfPage);
        }

        drawPDF(loadedPdfPage);
      }, () => {
        if (isFunction(onPageLoadFailRef.current)) {
          onPageLoadFailRef.current();
        }
      });
    }
  }, [canvasRef, page, pdfDocument, rotate, scale, baseWidth]);
  return {
    pdfDocument,
    pdfPage
  };
};
/* harmony default export */ __webpack_exports__["default"] = (Pdf);

/***/ })

};;
//# sourceMappingURL=vendors~PDFViewer.js.map