exports.ids = ["vendors~plone-volto-components-manage-Widgets-DatetimeWidget~plone-volto-components-manage-Widgets-R~a875f490"];
exports.modules = {

/***/ "./node_modules/@plone/volto/src/components/manage/Widgets/DatetimeWidget.jsx":
/*!************************************************************************************!*\
  !*** ./node_modules/@plone/volto/src/components/manage/Widgets/DatetimeWidget.jsx ***!
  \************************************************************************************/
/*! exports provided: DatetimeWidgetComponent, default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "DatetimeWidgetComponent", function() { return DatetimeWidgetComponent; });
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/defineProperty */ "@babel/runtime/helpers/defineProperty");
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var redux__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! redux */ "redux");
/* harmony import */ var redux__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(redux__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! prop-types */ "prop-types");
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(prop_types__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react-intl */ "react-intl");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react_intl__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! react-redux */ "react-redux");
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(react_redux__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _loadable_component__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @loadable/component */ "@loadable/component");
/* harmony import */ var _loadable_component__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_loadable_component__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var classnames__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! classnames */ "classnames");
/* harmony import */ var classnames__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(classnames__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var _plone_volto_helpers_Loadable_Loadable__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @plone/volto/helpers/Loadable/Loadable */ "./node_modules/@plone/volto/src/helpers/Loadable/Loadable.js");
/* harmony import */ var _plone_volto_icons_left_key_svg__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! @plone/volto/icons/left-key.svg */ "./node_modules/@plone/volto/src/icons/left-key.svg");
/* harmony import */ var _plone_volto_icons_left_key_svg__WEBPACK_IMPORTED_MODULE_11___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_left_key_svg__WEBPACK_IMPORTED_MODULE_11__);
/* harmony import */ var _plone_volto_icons_right_key_svg__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! @plone/volto/icons/right-key.svg */ "./node_modules/@plone/volto/src/icons/right-key.svg");
/* harmony import */ var _plone_volto_icons_right_key_svg__WEBPACK_IMPORTED_MODULE_12___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_right_key_svg__WEBPACK_IMPORTED_MODULE_12__);
/* harmony import */ var _plone_volto_icons_clear_svg__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! @plone/volto/icons/clear.svg */ "./node_modules/@plone/volto/src/icons/clear.svg");
/* harmony import */ var _plone_volto_icons_clear_svg__WEBPACK_IMPORTED_MODULE_13___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_clear_svg__WEBPACK_IMPORTED_MODULE_13__);
/* harmony import */ var rc_time_picker_assets_index_css__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! rc-time-picker/assets/index.css */ "./node_modules/rc-time-picker/assets/index.css");
/* harmony import */ var rc_time_picker_assets_index_css__WEBPACK_IMPORTED_MODULE_14___default = /*#__PURE__*/__webpack_require__.n(rc_time_picker_assets_index_css__WEBPACK_IMPORTED_MODULE_14__);
/* harmony import */ var react_dates_initialize__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! react-dates/initialize */ "react-dates/initialize");
/* harmony import */ var react_dates_initialize__WEBPACK_IMPORTED_MODULE_15___default = /*#__PURE__*/__webpack_require__.n(react_dates_initialize__WEBPACK_IMPORTED_MODULE_15__);
/* harmony import */ var react_dates_lib_css_datepicker_css__WEBPACK_IMPORTED_MODULE_16__ = __webpack_require__(/*! react-dates/lib/css/_datepicker.css */ "./node_modules/react-dates/lib/css/_datepicker.css");
/* harmony import */ var react_dates_lib_css_datepicker_css__WEBPACK_IMPORTED_MODULE_16___default = /*#__PURE__*/__webpack_require__.n(react_dates_lib_css_datepicker_css__WEBPACK_IMPORTED_MODULE_16__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_17__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_17___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_17__);

var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/node_modules/@plone/volto/src/components/manage/Widgets/DatetimeWidget.jsx";

function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); if (enumerableOnly) { symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; }); } keys.push.apply(keys, symbols); } return keys; }

function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i] != null ? arguments[i] : {}; if (i % 2) { ownKeys(Object(source), true).forEach(function (key) { _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(target, key, source[key]); }); } else if (Object.getOwnPropertyDescriptors) { Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)); } else { ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } } return target; }

/**
 * DatetimeWidget component.
 * @module components/manage/Widgets/DatetimeWidget
 */


















const TimePicker = _loadable_component__WEBPACK_IMPORTED_MODULE_6___default()({
  resolved: {},

  chunkName() {
    return "rc-time-picker";
  },

  isReady(props) {
    const key = this.resolve(props);

    if (this.resolved[key] !== true) {
      return false;
    }

    if (true) {
      return !!__webpack_require__.m[key];
    }

    return false;
  },

  importAsync: () => Promise.resolve(/*! import() */).then(__webpack_require__.t.bind(null, /*! rc-time-picker */ "rc-time-picker", 7)),

  requireAsync(props) {
    const key = this.resolve(props);
    this.resolved[key] = false;
    return this.importAsync(props).then(resolved => {
      this.resolved[key] = true;
      return resolved;
    });
  },

  requireSync(props) {
    const id = this.resolve(props);

    if (true) {
      return __webpack_require__(id);
    }

    return eval('module.require')(id);
  },

  resolve() {
    if (true) {
      return /*require.resolve*/(/*! rc-time-picker */ "rc-time-picker");
    }

    return eval('require.resolve')("rc-time-picker");
  }

});
const messages = Object(react_intl__WEBPACK_IMPORTED_MODULE_4__["defineMessages"])({
  date: {
    "id": "Date",
    "defaultMessage": "Date"
  },
  time: {
    "id": "Time",
    "defaultMessage": "Time"
  }
});

const PrevIcon = () => /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_17__["jsx"])("div", {
  style: {
    color: '#000',
    left: '22px',
    padding: '5px',
    position: 'absolute',
    top: '15px'
  } // eslint-disable-next-line jsx-a11y/no-noninteractive-tabindex
  ,
  tabIndex: "0",
  children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_17__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_8__["Icon"], {
    name: _plone_volto_icons_left_key_svg__WEBPACK_IMPORTED_MODULE_11___default.a,
    size: "30px"
  })
});

const NextIcon = () => /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_17__["jsx"])("div", {
  style: {
    color: '#000',
    right: '22px',
    padding: '5px',
    position: 'absolute',
    top: '15px'
  } // eslint-disable-next-line jsx-a11y/no-noninteractive-tabindex
  ,
  tabIndex: "0",
  children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_17__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_8__["Icon"], {
    name: _plone_volto_icons_right_key_svg__WEBPACK_IMPORTED_MODULE_12___default.a,
    size: "30px"
  })
});

const defaultTimeDateOnly = {
  hour: 12,
  minute: 0,
  second: 0
};
/**
 * DatetimeWidget component class
 * @class DatetimeWidget
 * @extends Component
 *
 * To use it, in schema properties, declare a field like:
 *
 * ```jsx
 * {
 *  title: "Publish date",
 *  type: 'datetime',
 * }
 * ```
 */

class DatetimeWidgetComponent extends react__WEBPACK_IMPORTED_MODULE_1__["Component"] {
  /**
   * Constructor
   * @method constructor
   * @param {Object} props Component properties
   * @constructs DatetimeWidget
   */
  constructor(props) {
    var _parseDateTime;

    super(props);

    _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(this, "onDateChange", date => {
      if (date) {
        const moment = this.props.moment.default;
        const isDateOnly = this.getDateOnly();
        const base = (this.getInternalValue() || moment()).set(_objectSpread({
          year: date.year(),
          month: date.month(),
          date: date.date()
        }, isDateOnly ? defaultTimeDateOnly : {}));
        const dateValue = isDateOnly ? base.format('YYYY-MM-DD') : base.toISOString();
        this.props.onChange(this.props.id, dateValue);
      }

      this.setState({
        isDefault: false
      });
    });

    _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(this, "onTimeChange", time => {
      const moment = this.props.moment.default;

      if (time) {
        var _time$hours, _time$minutes;

        const base = (this.getInternalValue() || moment()).set({
          hours: (_time$hours = time === null || time === void 0 ? void 0 : time.hours()) !== null && _time$hours !== void 0 ? _time$hours : 0,
          minutes: (_time$minutes = time === null || time === void 0 ? void 0 : time.minutes()) !== null && _time$minutes !== void 0 ? _time$minutes : 0,
          seconds: 0
        });
        const dateValue = base.toISOString();
        this.props.onChange(this.props.id, dateValue);
      }
    });

    _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(this, "onResetDates", () => {
      this.setState({
        isDefault: false
      });
      this.props.onChange(this.props.id, null);
    });

    _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(this, "onFocusChange", ({
      focused
    }) => this.setState({
      focused
    }));

    this.moment = props.moment.default;
    this.state = {
      focused: false,
      // if passed value matches the construction time, we guess it's a default
      isDefault: ((_parseDateTime = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_9__["parseDateTime"])(this.props.lang, this.props.value, undefined, this.moment)) === null || _parseDateTime === void 0 ? void 0 : _parseDateTime.toISOString()) === this.moment().utc().toISOString()
    };
  }

  getInternalValue() {
    return Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_9__["parseDateTime"])(this.props.lang, this.props.value, undefined, this.moment);
  }

  getDateOnly() {
    return this.props.dateOnly || this.props.widget === 'date';
  }
  /**
   * Update date storage
   * @method onDateChange
   * @param {Object} date updated momentjs Object for date
   * @returns {undefined}
   */


  render() {
    var _widgetOptions$patter;

    const {
      id,
      resettable,
      intl,
      reactDates,
      widgetOptions,
      lang
    } = this.props;
    const noPastDates = this.props.noPastDates || (widgetOptions === null || widgetOptions === void 0 ? void 0 : (_widgetOptions$patter = widgetOptions.pattern_options) === null || _widgetOptions$patter === void 0 ? void 0 : _widgetOptions$patter.noPastDates);
    const moment = this.props.moment.default;
    const datetime = this.getInternalValue();
    const dateOnly = this.getDateOnly();
    const {
      SingleDatePicker
    } = reactDates;
    return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_17__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_8__["FormFieldWrapper"], _objectSpread(_objectSpread({}, this.props), {}, {
      children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_17__["jsxs"])("div", {
        className: "date-time-widget-wrapper",
        children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_17__["jsx"])("div", {
          className: classnames__WEBPACK_IMPORTED_MODULE_7___default()('ui input date-input', {
            'default-date': this.state.isDefault
          }),
          children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_17__["jsx"])(SingleDatePicker, _objectSpread(_objectSpread({
            date: datetime,
            disabled: this.props.isDisabled,
            onDateChange: this.onDateChange,
            focused: this.state.focused,
            numberOfMonths: 1
          }, noPastDates ? {} : {
            isOutsideRange: () => false
          }), {}, {
            onFocusChange: this.onFocusChange,
            noBorder: true,
            displayFormat: moment.localeData(lang).longDateFormat('L'),
            navPrev: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_17__["jsx"])(PrevIcon, {}),
            navNext: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_17__["jsx"])(NextIcon, {}),
            id: `${id}-date`,
            placeholder: intl.formatMessage(messages.date)
          }))
        }), !dateOnly && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_17__["jsx"])("div", {
          className: classnames__WEBPACK_IMPORTED_MODULE_7___default()('ui input time-input', {
            'default-date': this.state.isDefault
          }),
          children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_17__["jsx"])(TimePicker, {
            disabled: this.props.isDisabled,
            defaultValue: datetime,
            value: datetime,
            onChange: this.onTimeChange,
            allowEmpty: false,
            showSecond: false,
            use12Hours: lang === 'en',
            id: `${id}-time`,
            format: moment.localeData(lang).longDateFormat('LT'),
            placeholder: intl.formatMessage(messages.time),
            focusOnOpen: true,
            placement: "bottomRight"
          })
        }), resettable && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_17__["jsx"])("button", {
          disabled: this.props.isDisabled || !datetime,
          onClick: () => this.onResetDates(),
          className: "item ui noborder button",
          children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_17__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_8__["Icon"], {
            name: _plone_volto_icons_clear_svg__WEBPACK_IMPORTED_MODULE_13___default.a,
            size: "24px",
            className: "close"
          })
        })]
      })
    }));
  }

}
/**
 * Property types.
 * @property {Object} propTypes Property types.
 * @static
 */

DatetimeWidgetComponent.propTypes = {
  id: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.string.isRequired,
  title: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.string.isRequired,
  description: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.string,
  required: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.bool,
  error: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.arrayOf(prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.string),
  dateOnly: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.bool,
  noPastDates: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.bool,
  value: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.string,
  onChange: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.func.isRequired,
  wrapped: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.bool,
  resettable: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.bool
};
/**
 * Default properties.
 * @property {Object} defaultProps Default properties.
 * @static
 */

DatetimeWidgetComponent.defaultProps = {
  description: null,
  required: false,
  error: [],
  dateOnly: false,
  noPastDates: false,
  value: null,
  resettable: true
};
/* harmony default export */ __webpack_exports__["default"] = (Object(redux__WEBPACK_IMPORTED_MODULE_2__["compose"])(Object(_plone_volto_helpers_Loadable_Loadable__WEBPACK_IMPORTED_MODULE_10__["injectLazyLibs"])(['reactDates', 'moment']), Object(react_redux__WEBPACK_IMPORTED_MODULE_5__["connect"])(state => ({
  lang: state.intl.locale
})), react_intl__WEBPACK_IMPORTED_MODULE_4__["injectIntl"])(DatetimeWidgetComponent));

/***/ }),

/***/ "./node_modules/rc-time-picker/assets/index.css":
/*!******************************************************!*\
  !*** ./node_modules/rc-time-picker/assets/index.css ***!
  \******************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

// Exports
module.exports = {};


/***/ })

};;
//# sourceMappingURL=vendors~plone-volto-components-manage-Widgets-DatetimeWidget~plone-volto-components-manage-Widgets-R~a875f490.js.map