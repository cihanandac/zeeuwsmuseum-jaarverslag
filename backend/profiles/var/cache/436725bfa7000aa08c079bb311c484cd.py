# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/registry/browser/templates/records.pt'

__tokens = {400: ("python:request.set('disable_border', 1)", 10, 31), 484: (" python:request.set('disable_plone.leftcolumn', 1", 11, 43), 578: ("o python:request.set('disable_plone.rightcolumn', ", 12, 42), 741: ('view/records', 17, 22), 1430: ('request/qp|nothing', 36, 37), 1485: (' request/q|nothin', 37, 35), 1853: ('python: qp or q', 45, 46), 2690: ('python: sorted(view.prefixes.keys())', 64, 47), 2885: ('prefixes', 66, 59), 2980: ("python: 'prefix:' + (view.prefixes[prefix] or '')", 68, 48), 3083: ('value', 69, 52), 3134: ('prefix', 70, 43), 4322: ('records', 102, 43), 4377: ('repeat/record/odd', 103, 45), 4439: (' record/field/originalField | record/fiel', 104, 43), 4531: ("python:oddrow and 'odd' or 'even'", 105, 48), 4815: ('string:${context/absolute_url}/edit/${record/__name__}', 109, 54), 4719: ("python:record.__name__.replace('.', ' ')", 108, 46), 4982: ('field/title', 112, 43), 5070: ('field/description', 113, 53), 5160: ('field/__class__/__name__', 114, 43), 5304: ('record/value|nothing', 116, 47), 5374: ('string:?', 117, 48), 5492: ('not: record/interfaceName|nothing', 119, 58), 5604: ('${context/absolute_url}/@@delete-record?name=${record/__name__}', 121, 39), 5606: ('context/absolute_url', 121, 41), 5651: ('record/__name__', 121, 86), 6024: ('python: records.numpages > 1', 130, 36), 6134: ('records', 132, 56), 6192: ('here/batch_macros/macros/navigation', 133, 48), 6192: ('here/batch_macros/macros/navigation', 133, 48), 6893: ("python:context.restrictedTraverse('@@configuration_registry_export_xml')()", 150, 38), 7848: ('context/@@ploneform-macros/titlelessform', 168, 34), 7848: ('context/@@ploneform-macros/titlelessform', 168, 34), 261: ('context/@@prefs_main_template/macros/master', 6, 23), 261: ('context/@@prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tal import ErrorInfo as _ErrorInfo
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque

_static_4905776800 = 'titlelessform'
_static_4900477376 = {'class': 'tab', }
_static_4900474112 = {'class': 'btn btn-primary', 'type': 'submit', }
_static_4900478672 = {'class': 'formControls mt-3', }
_static_4900471472 = {'type': 'hidden', 'name': 'button.importregistry', 'value': 'true', }
_static_4900476272 = {'type': 'file', 'name': 'file', 'id': 'exportFile', 'class': 'form-control', }
_static_4900476560 = {'for': 'exportFile', 'class': 'form-label', }
_static_4900471616 = {'class': 'mb-3 field', }
_static_4900527296 = {'method': 'POST', 'enctype': 'multipart/form-data', }
_static_4900532144 = {'class': 'tab', }
_static_4900534256 = {'class': 'btn btn-primary', 'type': 'submit', }
_static_4900522352 = {'class': 'formControls', }
_static_4900529264 = {'type': 'hidden', 'name': 'button.exportregistry', 'value': 'true', }
_static_4900521296 = {'method': 'POST', }
_static_4897897728 = {'class': 'tab', }
_static_4897895520 = 'navigation'
_static_4897883904 = {'colspan': '5', }
_static_4897885824 = {'href': '${context/absolute_url}/@@delete-record?name=${record/__name__}', 'class': 'recordsDeleteLink', }
_static_4900978448 = {'class': 'value', }
_static_4900976432 = {'data-label': 'Value', }
_static_4900971776 = {'data-label': 'Type', }
_static_4900962704 = {'data-label': 'Description', }
_static_4900973504 = {'data-label': 'Title', }
_static_4900966592 = {'class': 'recordsEditLink', 'href': 'string:${context/absolute_url}/edit/${record/__name__}', }
_static_4900965680 = {'data-label': 'Name', }
_static_4900083824 = {'class': "python:oddrow and 'odd' or 'even'", }
_static_4900203168 = {'class': 'table table-responsive table-bordered table-striped', }
_static_4900197888 = {'class': 'btn btn-secondary', 'type': 'reset', }
_static_4900206192 = {'id': 'clear-filter', }
_static_4900205088 = {'class': 'mb-3 col-auto', }
_static_4900194384 = {'value': 'value', }
_static_4900206000 = {'value': '', }
_static_4900006224 = {'class': 'form-select', 'name': 'qp', }
_static_4900002144 = {'class': 'col-form-label me-2', }
_static_4900007472 = {'class': 'input-group', }
_static_4900001808 = {'class': 'mb-3 col-auto', }
_static_4900010352 = {'class': 'row justify-content-between', }
_static_4899996528 = {'class': 'btn btn-primary', 'type': 'submit', 'value': 'Filter', }
_static_4899117120 = {'class': 'input-group-append', }
_static_4899117168 = {'class': 'form-control', 'name': 'q', 'id': 'q', 'placeholder': 'filter by...', 'value': 'python: qp or q', }
_static_4899111120 = {'class': 'input-group', }
_static_4909721312 = {'class': 'mb-3', }
_static_4909718720 = {'id': 'registry-filter', }
_static_4909723856 = {'id': 'searchrow', }
_static_4909724576 = {'id': 'recordsTable', 'class': 'pat-registry', }
_static_4909720640 = {'id': 'recordsContainer', 'class': 'tab', }
_static_4895396704 = {'class': 'pat-autotoc autotabs', 'data-pat-autotoc': 'section:.tab;levels:h2;', }
_static_4895395696 = {'id': 'content-core', }
_static_4897002480 = {'class': 'lead', }
_static_4897008528 = {'class': 'documentFirstHeading', }
_static_4893282592 = {'id': 'content', }
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
_static_4894576592 = 'master'
_static_4428767312 = {}

import re
import functools
from itertools import chain as __chain
from sys import intern
__default = intern('__default__')
__marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
__re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def initialize(modules, nothing, tales, zope_version_5_6_0_):

    def render(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
        __append = __stream.append
        __re_amp = g_re_amp
        __token = None
        __re_needs_escape = g_re_needs_escape

        def __convert(target):
            if (target is None):
                return
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except AttributeError:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            target = target()
            return target

        def __quote(target, quote, quote_entity, default, default_marker):
            if (target is None):
                return
            if (target is default_marker):
                return default
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            return target()
                if (target is not None):
                    try:
                        escape = (__re_needs_escape(target) is not None)
                    except TypeError:
                        pass
                    else:
                        if escape:
                            if ('&' in target):
                                target = target.replace('&', '&amp;')
                            if ('<' in target):
                                target = target.replace('<', '&lt;')
                            if ('>' in target):
                                target = target.replace('>', '&gt;')
                            if ((quote is not None) and (quote in target)):
                                target = target.replace(quote, quote_entity)
            return target
        translate = econtext['__translate']
        decode = econtext['__decode']
        convert = econtext['__convert']
        on_error_handler = econtext['__on_error_handler']
        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4894586288
            __attrs_4894586288 = _static_4428767312
            __previous_i18n_domain_4894582496 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4909912896 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x123bd4fd0> name=None at 123bd7580> -> __value
            __value = _static_4894576592
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4894583168
                __attrs_4894583168 = _static_4428767312
                __append('\n')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4894580528
                __attrs_4894580528 = _static_4428767312
                __backup_dummy_4909721744 = get('dummy', __marker)

                # <Value "python:request.set('disable_border', 1)" (10:31)> -> __value
                __token = 400
                try:
                    __zt_tmp = __attrs_4894580528
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', "request.set('disable_border', 1)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['dummy'] = __value
                __backup_disable_column_one_4909711712 = get('disable_column_one', __marker)

                # <Value "python:request.set('disable_plone.leftcolumn', 1)" (11:43)> -> __value
                __token = 484
                try:
                    __zt_tmp = __attrs_4894580528
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', "request.set('disable_plone.leftcolumn', 1)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['disable_column_one'] = __value
                __backup_disable_column_two_4909727552 = get('disable_column_two', __marker)

                # <Value "python:request.set('disable_plone.rightcolumn', 0)" (12:42)> -> __value
                __token = 578
                try:
                    __zt_tmp = __attrs_4894580528
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', "request.set('disable_plone.rightcolumn', 0)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['disable_column_two'] = __value
                if (__backup_disable_column_two_4909727552 is __marker):
                    del econtext['disable_column_two']
                else:
                    econtext['disable_column_two'] = __backup_disable_column_two_4909727552
                if (__backup_disable_column_one_4909711712 is __marker):
                    del econtext['disable_column_one']
                else:
                    econtext['disable_column_one'] = __backup_disable_column_one_4909711712
                if (__backup_dummy_4909721744 is __marker):
                    del econtext['dummy']
                else:
                    econtext['dummy'] = __backup_dummy_4909721744
                __append('\n')
            _slots = econtext['__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x123a99120> name=None at 123a9bf10> -> __attrs_4893279952
                __attrs_4893279952 = _static_4893282592
                __backup_records_4916884528 = get('records', __marker)

                # <Value 'view/records' (17:22)> -> __value
                __token = 741
                try:
                    __zt_tmp = __attrs_4893279952
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'view/records', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['records'] = __value

                # <article ... (0:0)
                # --------------------------------------------------------
                __append('<article id="content">\n\n  ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4897007088
                __attrs_4897007088 = _static_4428767312

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n    ')

                # <Static value=<ast.Dict object at 0x123e26b90> name=None at 123e25d50> -> __attrs_4897003536
                __attrs_4897003536 = _static_4897008528

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">')
                __stream_4897002384 = []
                __append_4897002384 = __stream_4897002384.append
                __append_4897002384('Configuration Registry')
                __msgid_4897002384 = __re_whitespace(''.join(__stream_4897002384)).strip()
                if 'heading_registry':
                    __append(translate('heading_registry', mapping=None, default=__msgid_4897002384, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n\n    ')

                # <Static value=<ast.Dict object at 0x123e253f0> name=None at 123e24f70> -> __attrs_4895401024
                __attrs_4895401024 = _static_4897002480

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="lead">')
                __stream_4897001856 = []
                __append_4897001856 = __stream_4897001856.append
                __append_4897001856('\n        The table below shows record currently managed by the configuration\n        registry. Click on a record to edit it.\n    ')
                __msgid_4897001856 = __re_whitespace(''.join(__stream_4897001856)).strip()
                if 'description_registry':
                    __append(translate('description_registry', mapping=None, default=__msgid_4897001856, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n  </header>\n    ')

                # <Static value=<ast.Dict object at 0x123c9cf70> name=None at 123c9e8c0> -> __attrs_4895397088
                __attrs_4895397088 = _static_4895395696

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n      ')

                # <Static value=<ast.Dict object at 0x123c9d360> name=None at 123c9dc60> -> __attrs_4895405104
                __attrs_4895405104 = _static_4895396704

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="pat-autotoc autotabs" data-pat-autotoc="section:.tab;levels:h2;">\n        ')

                # <Static value=<ast.Dict object at 0x124a46440> name=None at 124a46c50> -> __attrs_4909712816
                __attrs_4909712816 = _static_4909720640

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="recordsContainer" class="tab">\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4909727408
                __attrs_4909727408 = _static_4428767312

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2>')
                __stream_4909719344 = []
                __append_4909719344 = __stream_4909719344.append
                __append_4909719344('Records')
                __msgid_4909719344 = __re_whitespace(''.join(__stream_4909719344)).strip()
                if 'heading_records':
                    __append(translate('heading_records', mapping=None, default=__msgid_4909719344, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h2>\n          ')

                # <Static value=<ast.Dict object at 0x124a473a0> name=None at 124a473d0> -> __attrs_4909711904
                __attrs_4909711904 = _static_4909724576

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="recordsTable" class="pat-registry">\n\n            ')

                # <Static value=<ast.Dict object at 0x124a470d0> name=None at 124a47250> -> __attrs_4909715312
                __attrs_4909715312 = _static_4909723856

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="searchrow">\n\n                ')

                # <Static value=<ast.Dict object at 0x124a45cc0> name=None at 124a45d80> -> __attrs_4909718000
                __attrs_4909718000 = _static_4909718720
                __backup_qp_4678192480 = get('qp', __marker)

                # <Value 'request/qp|nothing' (36:37)> -> __value
                __token = 1430
                try:
                    __zt_tmp = __attrs_4909718000
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'request/qp|nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['qp'] = __value
                __backup_q_4680592656 = get('q', __marker)

                # <Value 'request/q|nothing' (37:35)> -> __value
                __token = 1485
                try:
                    __zt_tmp = __attrs_4909718000
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'request/q|nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['q'] = __value

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form id="registry-filter">\n\n                  ')

                # <Static value=<ast.Dict object at 0x124a466e0> name=None at 124a46080> -> __attrs_4909727072
                __attrs_4909727072 = _static_4909721312

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="mb-3">\n                    ')

                # <Static value=<ast.Dict object at 0x1240280d0> name=None at 124a47160> -> __attrs_4899117840
                __attrs_4899117840 = _static_4899111120

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="input-group">\n                      ')

                # <Static value=<ast.Dict object at 0x124029870> name=None at 12402b8e0> -> __attrs_4899122400
                __attrs_4899122400 = _static_4899117168

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="form-control" name="q" id="q"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4899118608
                __default_4899118608 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x12402a3e0> at 12402ada0> -> __attr_placeholder
                __attr_placeholder = 'filter by...'
                __attr_placeholder = translate(__attr_placeholder, default=__attr_placeholder, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_placeholder is not None):
                    __append((' placeholder="%s"' % __attr_placeholder))

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4899124944
                __default_4899124944 = _DEFAULT_MARKER

                # <Substitution 'python: qp or q' (45:46)> -> __attr_value
                __token = 1853
                try:
                    __zt_tmp = __attrs_4899122400
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('python', ' qp or q', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n                      ')

                # <Static value=<ast.Dict object at 0x124029840> name=None at 12402add0> -> __attrs_4900002528
                __attrs_4900002528 = _static_4899117120

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="input-group-append">\n                        ')

                # <Static value=<ast.Dict object at 0x124100370> name=None at 124101840> -> __attrs_4899995904
                __attrs_4899995904 = _static_4899996528

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="btn btn-primary" type="submit"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900004592
                __default_4900004592 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x124101720> at 124103f70> -> __attr_value
                __attr_value = 'Filter'
                __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append('>')
                __stream_4900008912 = []
                __append_4900008912 = __stream_4900008912.append
                __append_4900008912('\n                          Filter\n                        ')
                __msgid_4900008912 = __re_whitespace(''.join(__stream_4900008912)).strip()
                if __msgid_4900008912:
                    __append(translate(__msgid_4900008912, mapping=None, default=__msgid_4900008912, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</button>\n                      </div>\n                    </div>\n                  </div>\n\n                  ')

                # <Static value=<ast.Dict object at 0x124103970> name=None at 124101e70> -> __attrs_4900002048
                __attrs_4900002048 = _static_4900010352

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="row justify-content-between">\n                    ')

                # <Static value=<ast.Dict object at 0x124101810> name=None at 1241024d0> -> __attrs_4899998544
                __attrs_4899998544 = _static_4900001808

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="mb-3 col-auto">\n                      ')

                # <Static value=<ast.Dict object at 0x124102e30> name=None at 124100130> -> __attrs_4900009488
                __attrs_4900009488 = _static_4900007472

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="input-group">\n                        ')

                # <Static value=<ast.Dict object at 0x124101960> name=None at 124101360> -> __attrs_4900008720
                __attrs_4900008720 = _static_4900002144

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="col-form-label me-2">')
                __stream_4900001424 = []
                __append_4900001424 = __stream_4900001424.append
                __append_4900001424('or')
                __msgid_4900001424 = __re_whitespace(''.join(__stream_4900001424)).strip()
                if 'or':
                    __append(translate('or', mapping=None, default=__msgid_4900001424, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>\n                        ')

                # <Static value=<ast.Dict object at 0x124102950> name=None at 124101780> -> __attrs_4900008048
                __attrs_4900008048 = _static_4900006224
                __backup_prefixes_4894101024 = get('prefixes', __marker)

                # <Value 'python: sorted(view.prefixes.keys())' (64:47)> -> __value
                __token = 2690
                try:
                    __zt_tmp = __attrs_4900008048
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', ' sorted(view.prefixes.keys())', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['prefixes'] = __value

                # <select ... (0:0)
                # --------------------------------------------------------
                __append('<select class="form-select" name="qp">\n                          ')

                # <Static value=<ast.Dict object at 0x1241335b0> name=None at 1241339d0> -> __attrs_4900199760
                __attrs_4900199760 = _static_4900206000

                # <option ... (0:0)
                # --------------------------------------------------------
                __append('<option value="">')
                __stream_4900201632 = []
                __append_4900201632 = __stream_4900201632.append
                __append_4900201632('Select Prefix')
                __msgid_4900201632 = __re_whitespace(''.join(__stream_4900201632)).strip()
                if 'select_prefix':
                    __append(translate('select_prefix', mapping=None, default=__msgid_4900201632, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</option>\n                          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900208544
                __attrs_4900208544 = _static_4428767312
                __backup_prefix_4896999456 = get('prefix', __marker)

                # <Value 'prefixes' (66:59)> -> __iterator
                __token = 2885
                try:
                    __zt_tmp = __attrs_4900208544
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4427992992('path', 'prefixes', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                (__iterator, ____index_4900207728, ) = getname('repeat')('prefix', __iterator)
                econtext['prefix'] = None
                for __item in __iterator:
                    econtext['prefix'] = __item
                    __append('\n                            ')

                    # <Static value=<ast.Dict object at 0x124130850> name=None at 124132830> -> __attrs_4900206480
                    __attrs_4900206480 = _static_4900194384
                    __backup_value_4900114672 = get('value', __marker)

                    # <Value "python: 'prefix:' + (view.prefixes[prefix] or '')" (68:48)> -> __value
                    __token = 2980
                    try:
                        __zt_tmp = __attrs_4900206480
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4427992992('python', " 'prefix:' + (view.prefixes[prefix] or '')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    econtext['value'] = __value

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append('<option')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900206384
                    __default_4900206384 = _DEFAULT_MARKER

                    # <Substitution 'value' (69:52)> -> __attr_value
                    __token = 3083
                    try:
                        __zt_tmp = __attrs_4900206480
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_4427992992('path', 'value', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900205184
                    __default_4900205184 = _DEFAULT_MARKER

                    # <Value 'prefix' (70:43)> -> __cache_4900194144
                    __token = 3134
                    try:
                        __zt_tmp = __attrs_4900206480
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4900194144 = _static_4427992992('path', 'prefix', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'prefix' (70:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 124130040> -> __condition
                    __expression = __cache_4900194144

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4900194144
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</option>')
                    if (__backup_value_4900114672 is __marker):
                        del econtext['value']
                    else:
                        econtext['value'] = __backup_value_4900114672
                    __append('\n                          ')
                    ____index_4900207728 -= 1
                    if (____index_4900207728 > 0):
                        __append('')
                if (__backup_prefix_4896999456 is __marker):
                    del econtext['prefix']
                else:
                    econtext['prefix'] = __backup_prefix_4896999456
                __append('\n                        </select>')
                if (__backup_prefixes_4894101024 is __marker):
                    del econtext['prefixes']
                else:
                    econtext['prefixes'] = __backup_prefixes_4894101024
                __append('\n                      </div>\n                    </div>\n                    ')

                # <Static value=<ast.Dict object at 0x124133220> name=None at 1241312d0> -> __attrs_4900203456
                __attrs_4900203456 = _static_4900205088

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="mb-3 col-auto">\n                      ')

                # <Static value=<ast.Dict object at 0x124133670> name=None at 124130880> -> __attrs_4900197600
                __attrs_4900197600 = _static_4900206192

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form id="clear-filter">\n                          ')

                # <Static value=<ast.Dict object at 0x124131600> name=None at 124131ea0> -> __attrs_4900199712
                __attrs_4900199712 = _static_4900197888

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="btn btn-secondary" type="reset">')
                __stream_4900194336 = []
                __append_4900194336 = __stream_4900194336.append
                __append_4900194336('\n                              Clear filter\n                          ')
                __msgid_4900194336 = __re_whitespace(''.join(__stream_4900194336)).strip()
                if 'clear_filter':
                    __append(translate('clear_filter', mapping=None, default=__msgid_4900194336, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</button>\n                      </form>\n                    </div>\n                  </div>\n\n                </form>')
                if (__backup_q_4680592656 is __marker):
                    del econtext['q']
                else:
                    econtext['q'] = __backup_q_4680592656
                if (__backup_qp_4678192480 is __marker):
                    del econtext['qp']
                else:
                    econtext['qp'] = __backup_qp_4678192480
                __append('\n\n\n            </div>\n\n          ')

                # <Static value=<ast.Dict object at 0x124132aa0> name=None at 1241334f0> -> __attrs_4900077776
                __attrs_4900077776 = _static_4900203168

                # <table ... (0:0)
                # --------------------------------------------------------
                __append('<table class="table table-responsive table-bordered table-striped">\n              ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900085648
                __attrs_4900085648 = _static_4428767312

                # <thead ... (0:0)
                # --------------------------------------------------------
                __append('<thead>\n                  ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900088096
                __attrs_4900088096 = _static_4428767312

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n                      ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900092272
                __attrs_4900092272 = _static_4428767312

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>')
                __stream_4900083440 = []
                __append_4900083440 = __stream_4900083440.append
                __append_4900083440('Name')
                __msgid_4900083440 = __re_whitespace(''.join(__stream_4900083440)).strip()
                if 'heading_name':
                    __append(translate('heading_name', mapping=None, default=__msgid_4900083440, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</th>\n                      ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900084400
                __attrs_4900084400 = _static_4428767312

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>')
                __stream_4900091936 = []
                __append_4900091936 = __stream_4900091936.append
                __append_4900091936('Title')
                __msgid_4900091936 = __re_whitespace(''.join(__stream_4900091936)).strip()
                if 'heading_title':
                    __append(translate('heading_title', mapping=None, default=__msgid_4900091936, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</th>\n                      ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900078400
                __attrs_4900078400 = _static_4428767312

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>')
                __stream_4900087568 = []
                __append_4900087568 = __stream_4900087568.append
                __append_4900087568('Description')
                __msgid_4900087568 = __re_whitespace(''.join(__stream_4900087568)).strip()
                if 'heading_description':
                    __append(translate('heading_description', mapping=None, default=__msgid_4900087568, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</th>\n                      ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900092704
                __attrs_4900092704 = _static_4428767312

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>')
                __stream_4900092560 = []
                __append_4900092560 = __stream_4900092560.append
                __append_4900092560('Type')
                __msgid_4900092560 = __re_whitespace(''.join(__stream_4900092560)).strip()
                if 'heading_type':
                    __append(translate('heading_type', mapping=None, default=__msgid_4900092560, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</th>\n                      ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900090736
                __attrs_4900090736 = _static_4428767312

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>')
                __stream_4900089104 = []
                __append_4900089104 = __stream_4900089104.append
                __append_4900089104('Value')
                __msgid_4900089104 = __re_whitespace(''.join(__stream_4900089104)).strip()
                if 'heading_value':
                    __append(translate('heading_value', mapping=None, default=__msgid_4900089104, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</th>\n                  </tr>\n              </thead>\n              ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900090784
                __attrs_4900090784 = _static_4428767312

                # <tbody ... (0:0)
                # --------------------------------------------------------
                __append('<tbody>\n                  ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900083056
                __attrs_4900083056 = _static_4428767312
                __backup_record_4895398720 = get('record', __marker)

                # <Value 'records' (102:43)> -> __iterator
                __token = 4322
                try:
                    __zt_tmp = __attrs_4900083056
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4427992992('path', 'records', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                (__iterator, ____index_4900087136, ) = getname('repeat')('record', __iterator)
                econtext['record'] = None
                for __item in __iterator:
                    econtext['record'] = __item
                    __append('\n                      ')

                    # <Static value=<ast.Dict object at 0x124115870> name=None at 124116410> -> __attrs_4900972496
                    __attrs_4900972496 = _static_4900083824
                    __backup_oddrow_4894105536 = get('oddrow', __marker)

                    # <Value 'repeat/record/odd' (103:45)> -> __value
                    __token = 4377
                    try:
                        __zt_tmp = __attrs_4900972496
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4427992992('path', 'repeat/record/odd', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    econtext['oddrow'] = __value
                    __backup_field_4894108752 = get('field', __marker)

                    # <Value 'record/field/originalField | record/field' (104:43)> -> __value
                    __token = 4439
                    try:
                        __zt_tmp = __attrs_4900972496
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4427992992('path', 'record/field/originalField | record/field', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    econtext['field'] = __value

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900081616
                    __default_4900081616 = _DEFAULT_MARKER

                    # <Substitution "python:oddrow and 'odd' or 'even'" (105:48)> -> __attr_class
                    __token = 4531
                    try:
                        __zt_tmp = __attrs_4900972496
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4427992992('python', "oddrow and 'odd' or 'even'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n                          ')

                    # <Static value=<ast.Dict object at 0x1241ecd30> name=None at 1241ec9a0> -> __attrs_4900968272
                    __attrs_4900968272 = _static_4900965680

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td data-label="Name">\n                              ')

                    # <Static value=<ast.Dict object at 0x1241ed0c0> name=None at 123bfa800> -> __attrs_4900965296
                    __attrs_4900965296 = _static_4900966592

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a class="recordsEditLink"')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900973840
                    __default_4900973840 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/absolute_url}/edit/${record/__name__}' (109:54)> -> __attr_href
                    __token = 4815
                    try:
                        __zt_tmp = __attrs_4900965296
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4427992992('string', '${context/absolute_url}/edit/${record/__name__}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900977968
                    __default_4900977968 = _DEFAULT_MARKER

                    # <Value "python:record.__name__.replace('.', ' ')" (108:46)> -> __cache_4900974464
                    __token = 4719
                    try:
                        __zt_tmp = __attrs_4900965296
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4900974464 = _static_4427992992('python', "record.__name__.replace('.', ' ')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:record.__name__.replace('.', ' ')" (108:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1241ee9e0> -> __condition
                    __expression = __cache_4900974464

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4900974464
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</a>\n                          </td>\n                          ')

                    # <Static value=<ast.Dict object at 0x1241eebc0> name=None at 1241ee140> -> __attrs_4900968320
                    __attrs_4900968320 = _static_4900973504

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td data-label="Title">')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900965248
                    __default_4900965248 = _DEFAULT_MARKER

                    # <Value 'field/title' (112:43)> -> __cache_4900968416
                    __token = 4982
                    try:
                        __zt_tmp = __attrs_4900968320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4900968416 = _static_4427992992('path', 'field/title', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'field/title' (112:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1241eca00> -> __condition
                    __expression = __cache_4900968416

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4900968416
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</td>\n                          ')

                    # <Static value=<ast.Dict object at 0x1241ec190> name=None at 1241ee5f0> -> __attrs_4900966448
                    __attrs_4900966448 = _static_4900962704

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td data-label="Description">')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900965008
                    __default_4900965008 = _DEFAULT_MARKER

                    # <Value 'field/description' (113:53)> -> __cache_4900975904
                    __token = 5070
                    try:
                        __zt_tmp = __attrs_4900966448
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4900975904 = _static_4427992992('path', 'field/description', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'field/description' (113:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1241edc00> -> __condition
                    __expression = __cache_4900975904

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4900975904
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</td>\n                          ')

                    # <Static value=<ast.Dict object at 0x1241ee500> name=None at 1241eef20> -> __attrs_4900974896
                    __attrs_4900974896 = _static_4900971776

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td data-label="Type">')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900971392
                    __default_4900971392 = _DEFAULT_MARKER

                    # <Value 'field/__class__/__name__' (114:43)> -> __cache_4900968848
                    __token = 5160
                    try:
                        __zt_tmp = __attrs_4900974896
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4900968848 = _static_4427992992('path', 'field/__class__/__name__', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'field/__class__/__name__' (114:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1241ee6e0> -> __condition
                    __expression = __cache_4900968848

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4900968848
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</td>\n                          ')

                    # <Static value=<ast.Dict object at 0x1241ef730> name=None at 1241ee200> -> __attrs_4900974320
                    __attrs_4900974320 = _static_4900976432

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td data-label="Value">\n                            ')
                    ____fallback_4596941616 = len(__stream)
                    try:

                        # <Static value=<ast.Dict object at 0x1241eff10> name=None at 1241ed630> -> __attrs_4900970624
                        __attrs_4900970624 = _static_4900978448

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="value">')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900964480
                        __default_4900964480 = _DEFAULT_MARKER

                        # <Value 'record/value|nothing' (116:47)> -> __cache_4900976624
                        __token = 5304
                        try:
                            __zt_tmp = __attrs_4900970624
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4900976624 = _static_4427992992('path', 'record/value|nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value 'record/value|nothing' (116:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1241ee620> -> __condition
                        __expression = __cache_4900976624

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4900976624
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>')
                    except (Exception, ) as __exc:
                        econtext['error'] = _ErrorInfo(__exc, __tokens[__token][1:3])
                        if (on_error_handler is not None):
                            on_error_handler(__exc)
                        del __stream[____fallback_4596941616:]

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="value">')

                        # <Value 'string:?' (117:48)> -> __content
                        __token = 5374
                        try:
                            __zt_tmp = __attrs_4900974320
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content = _static_4427992992('string', '?', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                        __append('</span>')

                    __append('\n                            ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4897883664
                    __attrs_4897883664 = _static_4428767312

                    # <Value 'not: record/interfaceName|nothing' (119:58)> -> __condition
                    __token = 5492
                    try:
                        __zt_tmp = __attrs_4897883664
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('not', ' record/interfaceName|nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:
                        __append('\n                              ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4897884864
                        __attrs_4897884864 = _static_4428767312

                        # <br ... (0:0)
                        # --------------------------------------------------------
                        __append('<br />\n                             (')

                        # <Static value=<ast.Dict object at 0x123efce80> name=None at 123efd990> -> __attrs_4897882896
                        __attrs_4897882896 = _static_4897885824

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4897896912
                        __default_4897896912 = _DEFAULT_MARKER

                        # <Interpolation value=<Substitution '${context/absolute_url}/@@delete-record?name=${record/__name__}' (121:39)> braces_required=True translation=False default='"?"' default_marker='"?"' at 123efe320> -> __attr_href
                        __token = 5604
                        __token = 5606
                        try:
                            __zt_tmp = __attrs_4897882896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4427992992('path', 'context/absolute_url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        __token = 5651
                        try:
                            __zt_tmp = __attrs_4897882896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href_5649 = _static_4427992992('path', 'record/__name__', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_href_5649 = __quote(__attr_href_5649, '"', '&quot;', None, _DEFAULT_MARKER)
                        __attr_href = ('%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/@@delete-record?name=', (__attr_href_5649 if (__attr_href_5649 is not None) else ''), ))
                        if (__attr_href is None):
                            pass
                        else:
                            if (__attr_href is _DEFAULT_MARKER):
                                __attr_href = None
                            else:
                                __tt = type(__attr_href)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __attr_href = str(__attr_href)
                                else:
                                    if (__tt is bytes):
                                        __attr_href = decode(__attr_href)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __attr_href = __attr_href.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__attr_href)
                                                __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                            else:
                                                __attr_href = __attr_href()
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' class="recordsDeleteLink">')
                        __stream_4897890240 = []
                        __append_4897890240 = __stream_4897890240.append
                        __append_4897890240('\n                                 Delete record\n                              ')
                        __msgid_4897890240 = __re_whitespace(''.join(__stream_4897890240)).strip()
                        if __msgid_4897890240:
                            __append(translate(__msgid_4897890240, mapping=None, default=__msgid_4897890240, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</a>)\n                            ')
                    __append('\n                          </td>\n                      </tr>')
                    if (__backup_field_4894108752 is __marker):
                        del econtext['field']
                    else:
                        econtext['field'] = __backup_field_4894108752
                    if (__backup_oddrow_4894105536 is __marker):
                        del econtext['oddrow']
                    else:
                        econtext['oddrow'] = __backup_oddrow_4894105536
                    __append('\n                  ')
                    ____index_4900087136 -= 1
                    if (____index_4900087136 > 0):
                        __append('')
                if (__backup_record_4895398720 is __marker):
                    del econtext['record']
                else:
                    econtext['record'] = __backup_record_4895398720
                __append('\n              </tbody>\n              ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900967216
                __attrs_4900967216 = _static_4428767312

                # <Value 'python: records.numpages > 1' (130:36)> -> __condition
                __token = 6024
                try:
                    __zt_tmp = __attrs_4900967216
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('python', ' records.numpages > 1', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <tfoot ... (0:0)
                    # --------------------------------------------------------
                    __append('<tfoot>\n                  ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4897894416
                    __attrs_4897894416 = _static_4428767312

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr>\n                      ')

                    # <Static value=<ast.Dict object at 0x123efc700> name=None at 123efd3c0> -> __attrs_4897893600
                    __attrs_4897893600 = _static_4897883904
                    __backup_batch_4897012800 = get('batch', __marker)

                    # <Value 'records' (132:56)> -> __value
                    __token = 6134
                    try:
                        __zt_tmp = __attrs_4897893600
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4427992992('path', 'records', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    econtext['batch'] = __value

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th colspan="5">\n                          ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900525328
                    __attrs_4900525328 = _static_4428767312
                    __backup_macroname_4905051584 = get('macroname', __marker)

                    # <Static value=<ast.Constant object at 0x123eff460> name=None at 123eff6d0> -> __value
                    __value = _static_4897895520
                    econtext['macroname'] = __value

                    # <Value 'here/batch_macros/macros/navigation' (133:48)> -> __macro
                    __token = 6192
                    try:
                        __zt_tmp = __attrs_4900525328
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __macro = _static_4427992992('path', 'here/batch_macros/macros/navigation', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __token = 6192
                    __m = __macro.include
                    __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    if (__backup_macroname_4905051584 is __marker):
                        del econtext['macroname']
                    else:
                        econtext['macroname'] = __backup_macroname_4905051584
                    __append('\n                      </th>')
                    if (__backup_batch_4897012800 is __marker):
                        del econtext['batch']
                    else:
                        econtext['batch'] = __backup_batch_4897012800
                    __append('\n                  </tr>\n              </tfoot>')
                __append('\n          </table>\n        </div>\n        </div>\n        ')

                # <Static value=<ast.Dict object at 0x123effd00> name=None at 123eff8b0> -> __attrs_4900527584
                __attrs_4900527584 = _static_4897897728

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="tab">\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900520576
                __attrs_4900520576 = _static_4428767312

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2>')
                __stream_4900524704 = []
                __append_4900524704 = __stream_4900524704.append
                __append_4900524704('Export')
                __msgid_4900524704 = __re_whitespace(''.join(__stream_4900524704)).strip()
                if 'export':
                    __append(translate('export', mapping=None, default=__msgid_4900524704, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h2>\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900531424
                __attrs_4900531424 = _static_4428767312

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p>')
                __stream_4900527440 = []
                __append_4900527440 = __stream_4900527440.append
                __append_4900527440('Will export the entire registry into a single XML file.')
                __msgid_4900527440 = __re_whitespace(''.join(__stream_4900527440)).strip()
                if 'registry_export_text':
                    __append(translate('registry_export_text', mapping=None, default=__msgid_4900527440, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n          ')

                # <Static value=<ast.Dict object at 0x124180550> name=None at 124180b20> -> __attrs_4900535120
                __attrs_4900535120 = _static_4900521296

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form method="POST">\n            ')

                # <Static value=<ast.Dict object at 0x124182470> name=None at 124183790> -> __attrs_4900530992
                __attrs_4900530992 = _static_4900529264

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="button.exportregistry" value="true"/>\n            ')

                # <Static value=<ast.Dict object at 0x124180970> name=None at 124180a60> -> __attrs_4900524272
                __attrs_4900524272 = _static_4900522352

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="formControls">\n              ')

                # <Static value=<ast.Dict object at 0x1241837f0> name=None at 1241807c0> -> __attrs_4900521728
                __attrs_4900521728 = _static_4900534256

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="btn btn-primary" type="submit">')
                __stream_4900528256 = []
                __append_4900528256 = __stream_4900528256.append
                __append_4900528256('Export Now')
                __msgid_4900528256 = __re_whitespace(''.join(__stream_4900528256)).strip()
                if 'export_button':
                    __append(translate('export_button', mapping=None, default=__msgid_4900528256, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</button>\n            </div>\n          </form>\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900531808
                __attrs_4900531808 = _static_4428767312

                # <hr ... (0:0)
                # --------------------------------------------------------
                __append('<hr />\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900527824
                __attrs_4900527824 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900529888
                __default_4900529888 = _DEFAULT_MARKER

                # <Value "python:context.restrictedTraverse('@@configuration_registry_export_xml')()" (150:38)> -> __cache_4900535456
                __token = 6893
                try:
                    __zt_tmp = __attrs_4900527824
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4900535456 = _static_4427992992('python', "context.restrictedTraverse('@@configuration_registry_export_xml')()", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value "python:context.restrictedTraverse('@@configuration_registry_export_xml')()" (150:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 124183160> -> __condition
                __expression = __cache_4900535456

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div />')
                else:
                    __content = __cache_4900535456
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n        </div>\n        ')

                # <Static value=<ast.Dict object at 0x124182fb0> name=None at 1241833d0> -> __attrs_4900536032
                __attrs_4900536032 = _static_4900532144

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="tab">\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900533488
                __attrs_4900533488 = _static_4428767312

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2>')
                __stream_4900533152 = []
                __append_4900533152 = __stream_4900533152.append
                __append_4900533152('Import')
                __msgid_4900533152 = __re_whitespace(''.join(__stream_4900533152)).strip()
                if 'import':
                    __append(translate('import', mapping=None, default=__msgid_4900533152, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h2>\n          ')

                # <Static value=<ast.Dict object at 0x124181cc0> name=None at 124181ea0> -> __attrs_4900525376
                __attrs_4900525376 = _static_4900527296

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form method="POST" enctype=\'multipart/form-data\'>\n            ')

                # <Static value=<ast.Dict object at 0x124174340> name=None at 1241771c0> -> __attrs_4900477616
                __attrs_4900477616 = _static_4900471616

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="mb-3 field">\n              ')

                # <Static value=<ast.Dict object at 0x124175690> name=None at 1241748e0> -> __attrs_4900484288
                __attrs_4900484288 = _static_4900476560

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label for="exportFile" class="form-label">')
                __stream_4900482608 = []
                __append_4900482608 = __stream_4900482608.append
                __append_4900482608('Registry XML File')
                __msgid_4900482608 = __re_whitespace(''.join(__stream_4900482608)).strip()
                if __msgid_4900482608:
                    __append(translate(__msgid_4900482608, mapping=None, default=__msgid_4900482608, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>\n              ')

                # <Static value=<ast.Dict object at 0x124175570> name=None at 1241775e0> -> __attrs_4900481024
                __attrs_4900481024 = _static_4900476272

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="file" name="file" id="exportFile" class="form-control" />\n            </div>\n            ')

                # <Static value=<ast.Dict object at 0x1241742b0> name=None at 1241744c0> -> __attrs_4900472576
                __attrs_4900472576 = _static_4900471472

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="button.importregistry" value="true"/>\n            ')

                # <Static value=<ast.Dict object at 0x124175ed0> name=None at 1241779d0> -> __attrs_4900478912
                __attrs_4900478912 = _static_4900478672

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="formControls mt-3">\n              ')

                # <Static value=<ast.Dict object at 0x124174d00> name=None at 124177c10> -> __attrs_4900472960
                __attrs_4900472960 = _static_4900474112

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="btn btn-primary" type="submit">')
                __stream_4900483760 = []
                __append_4900483760 = __stream_4900483760.append
                __append_4900483760('Import File')
                __msgid_4900483760 = __re_whitespace(''.join(__stream_4900483760)).strip()
                if 'import_button':
                    __append(translate('import_button', mapping=None, default=__msgid_4900483760, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</button>\n            </div>\n          </form>\n        </div>\n        ')

                # <Static value=<ast.Dict object at 0x1241759c0> name=None at 124177040> -> __attrs_4900473968
                __attrs_4900473968 = _static_4900477376

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="tab">\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900474832
                __attrs_4900474832 = _static_4428767312

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2>')
                __stream_4900476896 = []
                __append_4900476896 = __stream_4900476896.append
                __append_4900476896('Add new record')
                __msgid_4900476896 = __re_whitespace(''.join(__stream_4900476896)).strip()
                if 'registry_add_record_label':
                    __append(translate('registry_add_record_label', mapping=None, default=__msgid_4900476896, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h2>\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900481696
                __attrs_4900481696 = _static_4428767312

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p>')
                __stream_4900481168 = []
                __append_4900481168 = __stream_4900481168.append
                __msgid_4900481168 = __re_whitespace(''.join(__stream_4900481168)).strip()
                if 'registry_add_record_text':
                    __append(translate('registry_add_record_text', mapping=None, default=__msgid_4900481168, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4905763792
                __attrs_4905763792 = _static_4428767312
                __backup_macroname_4905018112 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x1246836a0> name=None at 124680d60> -> __value
                __value = _static_4905776800
                econtext['macroname'] = __value

                # <Value 'context/@@ploneform-macros/titlelessform' (168:34)> -> __macro
                __token = 7848
                try:
                    __zt_tmp = __attrs_4905763792
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_4427992992('path', 'context/@@ploneform-macros/titlelessform', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __token = 7848
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_4905018112 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_4905018112
                __append('\n        </div>\n      </div>\n    </div>\n</article>')
                if (__backup_records_4916884528 is __marker):
                    del econtext['records']
                else:
                    econtext['records'] = __backup_records_4916884528
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'context/@@prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_4894586288
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4427992992('path', 'context/@@prefs_main_template/macros/master', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4909912896 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4909912896
            __i18n_domain = __previous_i18n_domain_4894582496
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }