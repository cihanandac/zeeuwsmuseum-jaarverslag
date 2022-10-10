# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/Products/CMFPlone/controlpanel/browser/redirects-controlpanel.pt'

__tokens = {573: ('view/csv_errors|nothing', 18, 28), 1074: ('view/csv_errors', 29, 34), 1307: ('${error/line_number}', 35, 16), 1309: ('error/line_number', 35, 18), 1507: ('${error/line}', 41, 16), 1509: ('error/line', 41, 18), 1576: ('${error/message}', 44, 16), 1578: ('error/message', 44, 18), 1726: ('${view/view_url}', 53, 18), 1728: ('view/view_url', 53, 20), 2141: ('view/form_errors/redirection|nothing', 64, 33), 2216: ("python:error and 'field mb-3 error' or 'field mb-3'", 65, 37), 2890: (" python:error and 'form-control is-invalid' or 'form-control", 83, 37), 2822: ('request/redirection | nothing', 82, 38), 3061: ('error', 87, 29), 3025: ('error', 86, 27), 3525: ('view/form_errors/target_path|nothing', 99, 33), 3600: ("python:error and 'field mb-3 error' or 'field mb-3'", 100, 37), 4449: ('error', 122, 29), 4413: ('error', 121, 27), 5036: ("python:icons.tag('plus', tag_alt='Add')", 138, 47), 5234: ('${view/view_url}', 147, 18), 5236: ('view/view_url', 147, 20), 6380: ('view/form_errors/file|nothing', 170, 33), 6448: ("python:error and 'field mb-3 error' or 'field mb-3'", 171, 37), 6991: ("python:error and 'form-control is-invalid' or 'form-control'", 186, 36), 7162: ('error', 190, 29), 7126: ('error', 189, 27), 7488: ("python:icons.tag('upload', tag_alt='Upload')", 202, 47), 7693: ('${view/view_url}#manage-existing-aliases', 210, 18), 7695: ('view/view_url', 210, 20), 7858: ('view/redirects', 214, 28), 8281: ("python:icons.tag('download', tag_alt='Download')", 225, 49), 8770: ("python:request.form.get('q', '/')", 236, 38), 9103: ("python:request.form.get('manual', '')", 243, 31), 9264: ("python:chosen==''", 244, 121), 9504: ("python:chosen=='no'", 246, 121), 9755: ("python:chosen=='yes'", 248, 123), 10178: ("python:request.form.get('datetime', '')", 256, 32), 10482: ("python:icons.tag('filter', tag_alt='Filter')", 265, 47), 10676: ('view/form_errors/remove_redirects|nothing', 270, 33), 10874: ('error', 273, 30), 10756: ("python:error and 'field mb-3 error' or 'field mb-3'", 271, 37), 10837: ('error', 272, 28), 11133: ('batch', 277, 42), 11398: ('${redirect/redirect}', 284, 25), 11400: ('redirect/redirect', 284, 27), 11437: ('${redirect/path} &rarr; ${redirect/redirect-to}', 285, 14), 11439: ('redirect/path', 285, 16), 11463: ('redirect/redirect-to', 285, 40), 11510: ('(${redirect/datetime}, ${redirect/manual})', 285, 87), 11513: ('redirect/datetime', 285, 90), 11535: ('redirect/manual', 285, 112), 11725: ('python:batch.numpages > 1', 292, 30), 11790: ('view/batching', 293, 38), 12075: ("python:icons.tag('trash', tag_alt='Trash')", 302, 49), 12408: ("python:icons.tag('trash', tag_alt='Trash')", 308, 49), 261: ('context/prefs_main_template/macros/master', 6, 23), 261: ('context/prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4681949216 = {'class': 'btn btn-danger', 'type': 'submit', 'value': 'Remove all that match filter', 'name': 'form.button.MatchRemove', }
_static_4680511600 = {'class': 'btn btn-danger', 'type': 'submit', 'value': 'Remove selected', 'name': 'form.button.Remove', }
_static_4680499360 = {'class': 'formControls', }
_static_4680812240 = {'class': 'justify-content-center mb-4', }
_static_4680505696 = {'class': 'text-muted', }
_static_4680514336 = {'type': 'checkbox', 'class': 'form-check-input noborder', 'name': 'redirects:tuple', 'value': '${redirect/redirect}', }
_static_4680501424 = {'class': 'form-check-label', }
_static_4680817136 = {'class': 'form-check', }
_static_4680817808 = {'class': 'text-muted', }
_static_4680811712 = {'class': 'mb-4', }
_static_4680819728 = {'class': 'field mb-3', }
_static_4680821600 = {'class': 'btn btn-primary', 'type': 'submit', 'value': 'Filter', 'name': 'form.button.filter', }
_static_4681903520 = {'class': 'formControls mb-4', }
_static_4681897712 = {'type': 'date', 'id': 'filter-existing-aliases-date', 'class': 'form-control', 'name': 'datetime', 'value': "python:request.form.get('datetime', '')", }
_static_4681902704 = {'class': 'form-label', 'for': 'filter-existing-aliases-date', }
_static_4681902800 = {'class': 'mb-3', }
_static_4681894160 = {'for': 'manual-yes', 'class': 'form-check-label', }
_static_4678231872 = {'type': 'radio', 'name': 'manual', 'id': 'manual-yes', 'class': 'form-check-input', 'value': 'yes', 'checked': "python:chosen=='yes'", }
_static_4677987120 = {'for': 'manual-no', 'class': 'form-check-label', }
_static_4680446784 = {'type': 'radio', 'name': 'manual', 'id': 'manual-no', 'class': 'form-check-input', 'value': 'no', 'checked': "python:chosen=='no'", }
_static_4680446112 = {'for': 'manual-both', 'class': 'form-check-label', }
_static_4680444240 = {'type': 'radio', 'name': 'manual', 'id': 'manual-both', 'class': 'form-check-input', 'value': '', 'checked': "python:chosen==''", }
_static_4680438624 = {'class': 'form-check', 'id': 'filter-existing-aliases-manual', }
_static_4680448080 = {'class': 'form-label', 'for': 'filter-existing-aliases-manual', }
_static_4680442896 = {'class': 'mb-3', }
_static_4678277952 = {'class': 'form-control', 'type': 'text', 'name': 'q', 'value': '', 'id': 'filter-existing-aliases-q', }
_static_4678283904 = {'class': 'form-label', 'for': 'filter-existing-aliases-q', }
_static_4680560848 = {'class': 'mb-3', }
_static_4680561472 = {'class': 'btn btn-primary context', 'type': 'submit', 'value': 'Download all as CSV', 'name': 'form.button.Download', }
_static_4680562864 = {'class': 'mb-4', }
_static_4680561280 = {'class': 'mb-3', }
_static_4678295488 = {'class': 'mb-4', 'action': '${view/view_url}#manage-existing-aliases', 'method': 'post', 'id': 'manage-existing-aliases', }
_static_4677775424 = {'class': 'btn btn-success', 'type': 'submit', 'value': 'Upload', 'name': 'form.button.Upload', }
_static_4678294048 = {'class': 'formControls', }
_static_4678293760 = {'class': 'invalid-feedback', }
_static_4678292656 = {'class': 'form-control', 'type': 'file', 'name': 'file', 'required': '', }
_static_4678298944 = {'class': 'required fieldRequired', 'title': 'Required', }
_static_4680358480 = {'class': 'form-label', 'for': 'file', }
_static_4680357040 = {'class': 'field mb-3', }
_static_4680355792 = {'class': 'text-muted', }
_static_4680354016 = {'class': 'mb-3', }
_static_4678022288 = {'class': 'mb-4', 'action': '${view/view_url}', 'method': 'post', 'enctype': 'multipart/form-data', }
_static_4680781968 = {'class': 'btn btn-success', 'type': 'submit', 'value': 'Add', 'name': 'form.button.Add', }
_static_4680780432 = {'class': 'formControls', }
_static_4680787440 = {'class': 'formHelp form-text text-muted', }
_static_4680783792 = {'class': 'invalid-feedback', }
_static_4680793680 = {'class': 'required fieldRequired', 'title': 'Required', }
_static_4680781584 = {'class': 'form-label', 'for': 'target_path', }
_static_4680777936 = {'class': 'field mb-3', }
_static_4680783456 = {'class': 'formHelp form-text text-muted', }
_static_4680589392 = {'class': 'invalid-feedback', }
_static_4680594192 = {'class': 'form-control', 'type': 'text', 'name': 'redirection', 'value': '', 'size': '40', 'required': '', }
_static_4680582864 = {'class': 'required fieldRequired', 'title': 'Required', }
_static_4680596352 = {'class': 'form-label', 'for': 'redirection', }
_static_4680589104 = {'class': 'field mb-3', }
_static_4681930624 = {'class': 'text-muted', }
_static_4681924720 = {'class': 'mb-3', }
_static_4681933696 = {'class': 'mb-4', 'action': '${view/view_url}', 'method': 'post', }
_static_4681927792 = {'nowrap': 'nowrap', }
_static_4681926880 = {'style': 'vertical-align: top', }
_static_4680539664 = {'class': 'text-break', 'style': 'text-align: left; vertical-align: top', 'border': '0', 'cellpadding': '2', 'cellspacing': '0', }
_static_4680545232 = {'class': 'font-weight-bold', }
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
_static_4680543984 = {'class': 'alert alert-danger mt-3 mb-4', 'role': 'alert', }
_static_4680477584 = 'master'
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

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680536640
            __attrs_4680536640 = _static_4428767312
            __previous_i18n_domain_4680536736 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4671392000 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x116fa6b90> name=None at 116fb4f40> -> __value
            __value = _static_4680477584
            econtext['macroname'] = __value

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680539376
                __attrs_4680539376 = _static_4428767312
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680533760
                __attrs_4680533760 = _static_4428767312

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n\n        ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680544704
                __attrs_4680544704 = _static_4428767312

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>')
                __stream_4680541536 = []
                __append_4680541536 = __stream_4680541536.append
                __append_4680541536('\n          URL Management\n        ')
                __msgid_4680541536 = __re_whitespace(''.join(__stream_4680541536)).strip()
                if __msgid_4680541536:
                    __append(translate(__msgid_4680541536, mapping=None, default=__msgid_4680541536, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n\n        ')

                # <Static value=<ast.Dict object at 0x116fb6ef0> name=None at 116fb6680> -> __attrs_4680544416
                __attrs_4680544416 = _static_4680543984

                # <Value 'view/csv_errors|nothing' (18:28)> -> __condition
                __token = 573
                try:
                    __zt_tmp = __attrs_4680544416
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'view/csv_errors|nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-danger mt-3 mb-4" role="alert">\n          ')

                    # <Static value=<ast.Dict object at 0x116fb73d0> name=None at 116fb74f0> -> __attrs_4680540624
                    __attrs_4680540624 = _static_4680545232

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="font-weight-bold">')
                    __stream_4680543456 = []
                    __append_4680543456 = __stream_4680543456.append
                    __append_4680543456('Error')
                    __msgid_4680543456 = __re_whitespace(''.join(__stream_4680543456)).strip()
                    if __msgid_4680543456:
                        __append(translate(__msgid_4680543456, mapping=None, default=__msgid_4680543456, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</div>\n          ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680535296
                    __attrs_4680535296 = _static_4428767312

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_4680542352 = []
                    __append_4680542352 = __stream_4680542352.append
                    __append_4680542352('\n            No alternative urls were added. Please correct these errors in your CSV file and try again:\n          ')
                    __msgid_4680542352 = __re_whitespace(''.join(__stream_4680542352)).strip()
                    if 'error_bulk_upload':
                        __append(translate('error_bulk_upload', mapping=None, default=__msgid_4680542352, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n          ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680534240
                    __attrs_4680534240 = _static_4428767312

                    # <hr ... (0:0)
                    # --------------------------------------------------------
                    __append('<hr>\n          ')

                    # <Static value=<ast.Dict object at 0x116fb5e10> name=None at 116fb5d20> -> __attrs_4681936336
                    __attrs_4681936336 = _static_4680539664

                    # <table ... (0:0)
                    # --------------------------------------------------------
                    __append('<table class="text-break" style="text-align: left; vertical-align: top" border="0" cellpadding="2" cellspacing="0">\n            ')

                    # <Static value=<ast.Dict object at 0x1171088e0> name=None at 11710b850> -> __attrs_4681938592
                    __attrs_4681938592 = _static_4681926880
                    __backup_error_4681952864 = get('error', __marker)

                    # <Value 'view/csv_errors' (29:34)> -> __iterator
                    __token = 1074
                    try:
                        __zt_tmp = __attrs_4681938592
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_4427992992('path', 'view/csv_errors', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    (__iterator, ____index_4681929232, ) = getname('repeat')('error', __iterator)
                    econtext['error'] = None
                    for __item in __iterator:
                        econtext['error'] = __item

                        # <tr ... (0:0)
                        # --------------------------------------------------------
                        __append('<tr style="vertical-align: top">\n              ')

                        # <Static value=<ast.Dict object at 0x117108c70> name=None at 117108d00> -> __attrs_4681925632
                        __attrs_4681925632 = _static_4681927792

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td nowrap="nowrap">\n                ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4681931200
                        __attrs_4681931200 = _static_4428767312
                        __stream_4681932880 = []
                        __append_4681932880 = __stream_4681932880.append
                        __append_4681932880('\n                  Line\n                ')
                        __msgid_4681932880 = __re_whitespace(''.join(__stream_4681932880)).strip()
                        if 'label_bulk_upload_line':
                            __append(translate('label_bulk_upload_line', mapping=None, default=__msgid_4681932880, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))

                        # <Interpolation value=<Substitution '\n                ${error/line_number}\n                ' (34:28)> braces_required=True translation=False default='"?"' default_marker='"?"' at 117108280> -> __content_4353737008
                        __token = 1307
                        __token = 1309
                        try:
                            __zt_tmp = __attrs_4681925632
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_4353737008 = _static_4427992992('path', 'error/line_number', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __content_4353737008 = __quote(__content_4353737008, '\x00', '&#0;', None, None)
                        __content_4353737008 = ('%s%s%s' % ('\n                ', (__content_4353737008 if (__content_4353737008 is not None) else ''), '\n                ', ))
                        if (__content_4353737008 is None):
                            pass
                        else:
                            if (__content_4353737008 is None):
                                __content_4353737008 = None
                            else:
                                __tt = type(__content_4353737008)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __content_4353737008 = str(__content_4353737008)
                                else:
                                    if (__tt is bytes):
                                        __content_4353737008 = decode(__content_4353737008)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __content_4353737008 = __content_4353737008.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__content_4353737008)
                                                __content_4353737008 = (str(__content_4353737008) if (__content_4353737008 is __converted) else __converted)
                                            else:
                                                __content_4353737008 = __content_4353737008()
                        if (__content_4353737008 is not None):
                            __append(__content_4353737008)

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4681926016
                        __attrs_4681926016 = _static_4428767312
                        __stream_4681931104 = []
                        __append_4681931104 = __stream_4681931104.append
                        __append_4681931104('\n                  :\n                ')
                        __msgid_4681931104 = __re_whitespace(''.join(__stream_4681931104)).strip()
                        if 'label_bulk_upload_line_suffix':
                            __append(translate('label_bulk_upload_line_suffix', mapping=None, default=__msgid_4681931104, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('\n              </td>\n              ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4681932832
                        __attrs_4681932832 = _static_4428767312

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td>')

                        # <Interpolation value=<Substitution '\n                ${error/line}\n              ' (40:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11710aad0> -> __content_4353737008
                        __token = 1507
                        __token = 1509
                        try:
                            __zt_tmp = __attrs_4681932832
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_4353737008 = _static_4427992992('path', 'error/line', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __content_4353737008 = __quote(__content_4353737008, '\x00', '&#0;', None, None)
                        __content_4353737008 = ('%s%s%s' % ('\n                ', (__content_4353737008 if (__content_4353737008 is not None) else ''), '\n              ', ))
                        if (__content_4353737008 is None):
                            pass
                        else:
                            if (__content_4353737008 is None):
                                __content_4353737008 = None
                            else:
                                __tt = type(__content_4353737008)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __content_4353737008 = str(__content_4353737008)
                                else:
                                    if (__tt is bytes):
                                        __content_4353737008 = decode(__content_4353737008)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __content_4353737008 = __content_4353737008.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__content_4353737008)
                                                __content_4353737008 = (str(__content_4353737008) if (__content_4353737008 is __converted) else __converted)
                                            else:
                                                __content_4353737008 = __content_4353737008()
                        if (__content_4353737008 is not None):
                            __append(__content_4353737008)
                        __append('</td>\n              ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4681940032
                        __attrs_4681940032 = _static_4428767312

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td>')

                        # <Interpolation value=<Substitution '\n                ${error/message}\n              ' (43:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11710b010> -> __content_4353737008
                        __token = 1576
                        __token = 1578
                        try:
                            __zt_tmp = __attrs_4681940032
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_4353737008 = _static_4427992992('path', 'error/message', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __content_4353737008 = __quote(__content_4353737008, '\x00', '&#0;', None, None)
                        __content_4353737008 = ('%s%s%s' % ('\n                ', (__content_4353737008 if (__content_4353737008 is not None) else ''), '\n              ', ))
                        if (__content_4353737008 is None):
                            pass
                        else:
                            if (__content_4353737008 is None):
                                __content_4353737008 = None
                            else:
                                __tt = type(__content_4353737008)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __content_4353737008 = str(__content_4353737008)
                                else:
                                    if (__tt is bytes):
                                        __content_4353737008 = decode(__content_4353737008)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __content_4353737008 = __content_4353737008.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__content_4353737008)
                                                __content_4353737008 = (str(__content_4353737008) if (__content_4353737008 is __converted) else __converted)
                                            else:
                                                __content_4353737008 = __content_4353737008()
                        if (__content_4353737008 is not None):
                            __append(__content_4353737008)
                        __append('</td>\n            </tr>')
                        ____index_4681929232 -= 1
                        if (____index_4681929232 > 0):
                            __append('\n            ')
                    if (__backup_error_4681952864 is __marker):
                        del econtext['error']
                    else:
                        econtext['error'] = __backup_error_4681952864
                    __append('\n          </table>\n\n        </div>')
                __append('\n\n      </header>\n      ')

                # <Static value=<ast.Dict object at 0x11710a380> name=None at 11710a410> -> __attrs_4681930672
                __attrs_4681930672 = _static_4681933696

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form class="mb-4"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4681928992
                __default_4681928992 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${view/view_url}' (53:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11710a620> -> __attr_action
                __token = 1726
                __token = 1728
                try:
                    __zt_tmp = __attrs_4681930672
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_action = _static_4427992992('path', 'view/view_url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_action = __attr_action
                if (__attr_action is None):
                    pass
                else:
                    if (__attr_action is _DEFAULT_MARKER):
                        __attr_action = None
                    else:
                        __tt = type(__attr_action)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __attr_action = str(__attr_action)
                        else:
                            if (__tt is bytes):
                                __attr_action = decode(__attr_action)
                            else:
                                if (__tt is not str):
                                    try:
                                        __attr_action = __attr_action.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__attr_action)
                                        __attr_action = (str(__attr_action) if (__attr_action is __converted) else __converted)
                                    else:
                                        __attr_action = __attr_action()
                if (__attr_action is not None):
                    __append((' action="%s"' % __attr_action))
                __append(' method="post">\n        ')

                # <Static value=<ast.Dict object at 0x117108070> name=None at 1171080a0> -> __attrs_4681935760
                __attrs_4681935760 = _static_4681924720

                # <fieldset ... (0:0)
                # --------------------------------------------------------
                __append('<fieldset class="mb-3">\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4681940608
                __attrs_4681940608 = _static_4428767312

                # <legend ... (0:0)
                # --------------------------------------------------------
                __append('<legend>')
                __stream_4681928368 = []
                __append_4681928368 = __stream_4681928368.append
                __append_4681928368('\n            Add a new alternative url\n          ')
                __msgid_4681928368 = __re_whitespace(''.join(__stream_4681928368)).strip()
                if 'add_alias':
                    __append(translate('add_alias', mapping=None, default=__msgid_4681928368, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</legend>\n          ')

                # <Static value=<ast.Dict object at 0x117109780> name=None at 1171096f0> -> __attrs_4680587856
                __attrs_4680587856 = _static_4681930624

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="text-muted">')
                __stream_4681925920 = []
                __append_4681925920 = __stream_4681925920.append
                __append_4681925920('\n            To change the primary url of content, use Actions > Rename.\n          ')
                __msgid_4681925920 = __re_whitespace(''.join(__stream_4681925920)).strip()
                if 'description_change_primary_url':
                    __append(translate('description_change_primary_url', mapping=None, default=__msgid_4681925920, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n\n          ')

                # <Static value=<ast.Dict object at 0x116fc1f30> name=None at 116fc1f60> -> __attrs_4680586848
                __attrs_4680586848 = _static_4680589104
                __backup_error_4681951808 = get('error', __marker)

                # <Value 'view/form_errors/redirection|nothing' (64:33)> -> __value
                __token = 2141
                try:
                    __zt_tmp = __attrs_4680586848
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'view/form_errors/redirection|nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['error'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680589248
                __default_4680589248 = _DEFAULT_MARKER

                # <Substitution "python:error and 'field mb-3 error' or 'field mb-3'" (65:37)> -> __attr_class
                __token = 2216
                try:
                    __zt_tmp = __attrs_4680586848
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_4427992992('python', "error and 'field mb-3 error' or 'field mb-3'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', 'field mb-3', _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append('>\n\n            ')

                # <Static value=<ast.Dict object at 0x116fc3b80> name=None at 116fc03a0> -> __attrs_4680596496
                __attrs_4680596496 = _static_4680596352

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="form-label" for="redirection">\n              ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680592656
                __attrs_4680592656 = _static_4428767312

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')
                __stream_4680595440 = []
                __append_4680595440 = __stream_4680595440.append
                __append_4680595440('Alternative url path')
                __msgid_4680595440 = __re_whitespace(''.join(__stream_4680595440)).strip()
                if 'label_alias':
                    __append(translate('label_alias', mapping=None, default=__msgid_4680595440, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</span>\n              ')

                # <Static value=<ast.Dict object at 0x116fc06d0> name=None at 116fc0610> -> __attrs_4680594912
                __attrs_4680594912 = _static_4680582864

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span class="required fieldRequired"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680581280
                __default_4680581280 = _DEFAULT_MARKER

                # <Translate msgid='label_required' node=<ast.Constant object at 0x116fc2f20> at 116fc2fe0> -> __attr_title
                __attr_title = 'Required'
                __attr_title = translate('label_required', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_title is not None):
                    __append((' title="%s"' % __attr_title))
                __append('>\n              </span>\n            </label>\n\n            ')

                # <Static value=<ast.Dict object at 0x116fc3310> name=None at 116fc3370> -> __attrs_4680582144
                __attrs_4680582144 = _static_4680594192

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680591888
                __default_4680591888 = _DEFAULT_MARKER

                # <Substitution "python:error and 'form-control is-invalid' or 'form-control'" (83:37)> -> __attr_class
                __token = 2890
                try:
                    __zt_tmp = __attrs_4680582144
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_4427992992('python', "error and 'form-control is-invalid' or 'form-control'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', 'form-control', _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append(' type="text" name="redirection"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680588576
                __default_4680588576 = _DEFAULT_MARKER

                # <Substitution 'request/redirection | nothing' (82:38)> -> __attr_value
                __token = 2822
                try:
                    __zt_tmp = __attrs_4680582144
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'request/redirection | nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' size="40" required/>\n\n            ')

                # <Static value=<ast.Dict object at 0x116fc2050> name=None at 116fc20e0> -> __attrs_4680591360
                __attrs_4680591360 = _static_4680589392

                # <Value 'error' (87:29)> -> __condition
                __token = 3061
                try:
                    __zt_tmp = __attrs_4680591360
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="invalid-feedback">')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680591840
                    __default_4680591840 = _DEFAULT_MARKER

                    # <Value 'error' (86:27)> -> __cache_4680590112
                    __token = 3025
                    try:
                        __zt_tmp = __attrs_4680591360
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4680590112 = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'error' (86:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116fc2c50> -> __condition
                    __expression = __cache_4680590112

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n              Validation error output\n            ')
                    else:
                        __content = __cache_4680590112
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>')
                __append('\n\n            ')

                # <Static value=<ast.Dict object at 0x116ff1660> name=None at 116fc3910> -> __attrs_4680791280
                __attrs_4680791280 = _static_4680783456

                # <small ... (0:0)
                # --------------------------------------------------------
                __append('<small class="formHelp form-text text-muted">')
                __stream_4680595872 = []
                __append_4680595872 = __stream_4680595872.append
                __append_4680595872("\n              Enter the absolute path where the alternative url should exist. The path must start with '/'.\n              Only urls that result in a 404 not found page will result in a redirect occurring.\n            ")
                __msgid_4680595872 = __re_whitespace(''.join(__stream_4680595872)).strip()
                if 'help_alias':
                    __append(translate('help_alias', mapping=None, default=__msgid_4680595872, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</small>\n\n          </div>')
                if (__backup_error_4681951808 is __marker):
                    del econtext['error']
                else:
                    econtext['error'] = __backup_error_4681951808
                __append('\n\n          ')

                # <Static value=<ast.Dict object at 0x116ff00d0> name=None at 116ff0190> -> __attrs_4680786672
                __attrs_4680786672 = _static_4680777936
                __backup_error_4681952048 = get('error', __marker)

                # <Value 'view/form_errors/target_path|nothing' (99:33)> -> __value
                __token = 3525
                try:
                    __zt_tmp = __attrs_4680786672
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'view/form_errors/target_path|nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['error'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680778272
                __default_4680778272 = _DEFAULT_MARKER

                # <Substitution "python:error and 'field mb-3 error' or 'field mb-3'" (100:37)> -> __attr_class
                __token = 3600
                try:
                    __zt_tmp = __attrs_4680786672
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_4427992992('python', "error and 'field mb-3 error' or 'field mb-3'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', 'field mb-3', _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append('>\n\n            ')

                # <Static value=<ast.Dict object at 0x116ff0f10> name=None at 116ff2c50> -> __attrs_4680781392
                __attrs_4680781392 = _static_4680781584

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="form-label" for="target_path">\n              ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680784464
                __attrs_4680784464 = _static_4428767312

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')
                __stream_4680792528 = []
                __append_4680792528 = __stream_4680792528.append
                __append_4680792528('Target Path')
                __msgid_4680792528 = __re_whitespace(''.join(__stream_4680792528)).strip()
                if 'label_target_path':
                    __append(translate('label_target_path', mapping=None, default=__msgid_4680792528, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</span>\n              ')

                # <Static value=<ast.Dict object at 0x116ff3e50> name=None at 116ff1e40> -> __attrs_4680785088
                __attrs_4680785088 = _static_4680793680

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span class="required fieldRequired"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680790656
                __default_4680790656 = _DEFAULT_MARKER

                # <Translate msgid='label_required' node=<ast.Constant object at 0x116ff3220> at 116ff3190> -> __attr_title
                __attr_title = 'Required'
                __attr_title = translate('label_required', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_title is not None):
                    __append((' title="%s"' % __attr_title))
                __append('>\n              </span>\n            </label>\n\n            <input class="form-control"\n                type="text"\n                name="target_path"\n                value=""\n                size="40"\n                required\n                tal:attributes="value request/target_path | nothing;\n                                class python:error and \'form-control is-invalid\' or \'form-control\'""/>\n\n            ')

                # <Static value=<ast.Dict object at 0x116ff17b0> name=None at 116ff0790> -> __attrs_4680779424
                __attrs_4680779424 = _static_4680783792

                # <Value 'error' (122:29)> -> __condition
                __token = 4449
                try:
                    __zt_tmp = __attrs_4680779424
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="invalid-feedback">')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680789696
                    __default_4680789696 = _DEFAULT_MARKER

                    # <Value 'error' (121:27)> -> __cache_4680780000
                    __token = 4413
                    try:
                        __zt_tmp = __attrs_4680779424
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4680780000 = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'error' (121:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116ff0100> -> __condition
                    __expression = __cache_4680780000

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n              Validation error output\n            ')
                    else:
                        __content = __cache_4680780000
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>')
                __append('\n\n            ')

                # <Static value=<ast.Dict object at 0x116ff25f0> name=None at 116ff04c0> -> __attrs_4680789552
                __attrs_4680789552 = _static_4680787440

                # <small ... (0:0)
                # --------------------------------------------------------
                __append('<small class="formHelp form-text text-muted">')
                __stream_4680778800 = []
                __append_4680778800 = __stream_4680778800.append
                __append_4680778800("\n              Enter the absolute path of the target. The path must start with '/'.\n              Target must exist or be an existing alternative url path to the target.\n            ")
                __msgid_4680778800 = __re_whitespace(''.join(__stream_4680778800)).strip()
                if 'help_target_path':
                    __append(translate('help_target_path', mapping=None, default=__msgid_4680778800, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</small>\n\n          </div>')
                if (__backup_error_4681952048 is __marker):
                    del econtext['error']
                else:
                    econtext['error'] = __backup_error_4681952048
                __append('\n\n          ')

                # <Static value=<ast.Dict object at 0x116ff0a90> name=None at 116ff0a30> -> __attrs_4680791760
                __attrs_4680791760 = _static_4680780432

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="formControls">\n            ')

                # <Static value=<ast.Dict object at 0x116ff1090> name=None at 115c813c0> -> __attrs_4678009952
                __attrs_4678009952 = _static_4680781968

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="btn btn-success" type="submit" value="Add" name="form.button.Add">\n              ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4678014560
                __attrs_4678014560 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678024880
                __default_4678024880 = _DEFAULT_MARKER

                # <Value "python:icons.tag('plus', tag_alt='Add')" (138:47)> -> __cache_4678024064
                __token = 5036
                try:
                    __zt_tmp = __attrs_4678014560
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4678024064 = _static_4427992992('python', "icons.tag('plus', tag_alt='Add')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('plus', tag_alt='Add')" (138:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116d4c5e0> -> __condition
                __expression = __cache_4678024064

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4678024064
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(' ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4678022192
                __attrs_4678022192 = _static_4428767312

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')
                __stream_4678011392 = []
                __append_4678011392 = __stream_4678011392.append
                __append_4678011392('Add')
                __msgid_4678011392 = __re_whitespace(''.join(__stream_4678011392)).strip()
                if __msgid_4678011392:
                    __append(translate(__msgid_4678011392, mapping=None, default=__msgid_4678011392, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</span>\n            </button>\n          </div>\n\n        </fieldset>\n      </form>\n\n\n      ')

                # <Static value=<ast.Dict object at 0x116d4f490> name=None at 116d4eaa0> -> __attrs_4680352864
                __attrs_4680352864 = _static_4678022288

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form class="mb-4"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680365584
                __default_4680365584 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${view/view_url}' (147:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 116f8bb20> -> __attr_action
                __token = 5234
                __token = 5236
                try:
                    __zt_tmp = __attrs_4680352864
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_action = _static_4427992992('path', 'view/view_url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_action = __attr_action
                if (__attr_action is None):
                    pass
                else:
                    if (__attr_action is _DEFAULT_MARKER):
                        __attr_action = None
                    else:
                        __tt = type(__attr_action)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __attr_action = str(__attr_action)
                        else:
                            if (__tt is bytes):
                                __attr_action = decode(__attr_action)
                            else:
                                if (__tt is not str):
                                    try:
                                        __attr_action = __attr_action.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__attr_action)
                                        __attr_action = (str(__attr_action) if (__attr_action is __converted) else __converted)
                                    else:
                                        __attr_action = __attr_action()
                if (__attr_action is not None):
                    __append((' action="%s"' % __attr_action))
                __append(' method="post" enctype="multipart/form-data">\n        ')

                # <Static value=<ast.Dict object at 0x116f888e0> name=None at 116f889a0> -> __attrs_4680351856
                __attrs_4680351856 = _static_4680354016

                # <fieldset ... (0:0)
                # --------------------------------------------------------
                __append('<fieldset class="mb-3">\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680360304
                __attrs_4680360304 = _static_4428767312

                # <legend ... (0:0)
                # --------------------------------------------------------
                __append('<legend>')
                __stream_4680367216 = []
                __append_4680367216 = __stream_4680367216.append
                __append_4680367216('\n            Bulk-upload alternative urls\n          ')
                __msgid_4680367216 = __re_whitespace(''.join(__stream_4680367216)).strip()
                if 'legend_bulk_upload':
                    __append(translate('legend_bulk_upload', mapping=None, default=__msgid_4680367216, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</legend>\n\n          ')

                # <Static value=<ast.Dict object at 0x116f88fd0> name=None at 116f89060> -> __attrs_4680364672
                __attrs_4680364672 = _static_4680355792

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="text-muted">')
                __stream_4680354880 = []
                __append_4680354880 = __stream_4680354880.append
                __append_4680354880('\n            Add many alternative urls at once by uploading a CSV file. The first column should be the path to\n            redirect from; the second, the path to redirect to. Both paths must be Plone-site-relative,\n            starting with a slash (/). An optional third colum can contain a date and time.\n            An optional fourth column can contain a boolean to mark as a manual redirect (default true).\n          ')
                __msgid_4680354880 = __re_whitespace(''.join(__stream_4680354880)).strip()
                if 'description_bulk_upload':
                    __append(translate('description_bulk_upload', mapping=None, default=__msgid_4680354880, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680362176
                __attrs_4680362176 = _static_4428767312

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p>\n            ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680359344
                __attrs_4680359344 = _static_4428767312
                __stream_4680356368 = []
                __append_4680356368 = __stream_4680356368.append
                __append_4680356368('Example:')
                __msgid_4680356368 = __re_whitespace(''.join(__stream_4680356368)).strip()
                if 'example_caption_bulk_upload':
                    __append(translate('example_caption_bulk_upload', mapping=None, default=__msgid_4680356368, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680358816
                __attrs_4680358816 = _static_4428767312

                # <br ... (0:0)
                # --------------------------------------------------------
                __append('<br />\n            ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680365680
                __attrs_4680365680 = _static_4428767312

                # <code ... (0:0)
                # --------------------------------------------------------
                __append('<code>')
                __stream_4680363088 = []
                __append_4680363088 = __stream_4680363088.append
                __append_4680363088('\n              /old-home-page.asp,/front-page,2019/01/27 10:42:59 GMT+1,true')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680367984
                __attrs_4680367984 = _static_4428767312

                # <br ... (0:0)
                # --------------------------------------------------------
                __append_4680363088('<br />\n              /people/JoeT,/Users/joe-thurston,2018-12-31,false\n            ')
                __msgid_4680363088 = __re_whitespace(''.join(__stream_4680363088)).strip()
                if 'example_bulk_upload':
                    __append(translate('example_bulk_upload', mapping=None, default=__msgid_4680363088, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</code>\n          </p>\n\n          ')

                # <Static value=<ast.Dict object at 0x116f894b0> name=None at 116f89540> -> __attrs_4680365200
                __attrs_4680365200 = _static_4680357040
                __backup_error_4680352720 = get('error', __marker)

                # <Value 'view/form_errors/file|nothing' (170:33)> -> __value
                __token = 6380
                try:
                    __zt_tmp = __attrs_4680365200
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'view/form_errors/file|nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['error'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680356992
                __default_4680356992 = _DEFAULT_MARKER

                # <Substitution "python:error and 'field mb-3 error' or 'field mb-3'" (171:37)> -> __attr_class
                __token = 6448
                try:
                    __zt_tmp = __attrs_4680365200
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_4427992992('python', "error and 'field mb-3 error' or 'field mb-3'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', 'field mb-3', _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append('>\n\n            ')

                # <Static value=<ast.Dict object at 0x116f89a50> name=None at 116f886a0> -> __attrs_4678287520
                __attrs_4678287520 = _static_4680358480

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="form-label" for="file" class="form-label">\n              ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4678303456
                __attrs_4678303456 = _static_4428767312

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')
                __stream_4678289296 = []
                __append_4678289296 = __stream_4678289296.append
                __append_4678289296('CSV file')
                __msgid_4678289296 = __re_whitespace(''.join(__stream_4678289296)).strip()
                if 'label_csv_file':
                    __append(translate('label_csv_file', mapping=None, default=__msgid_4678289296, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</span>\n              ')

                # <Static value=<ast.Dict object at 0x116d92d40> name=None at 116d924d0> -> __attrs_4678291552
                __attrs_4678291552 = _static_4678298944

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span class="required fieldRequired"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678290496
                __default_4678290496 = _DEFAULT_MARKER

                # <Translate msgid='label_required' node=<ast.Constant object at 0x116d901f0> at 116d90160> -> __attr_title
                __attr_title = 'Required'
                __attr_title = translate('label_required', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_title is not None):
                    __append((' title="%s"' % __attr_title))
                __append('>\n              </span>\n            </label>\n\n            ')

                # <Static value=<ast.Dict object at 0x116d914b0> name=None at 116d914e0> -> __attrs_4678300912
                __attrs_4678300912 = _static_4678292656

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678292800
                __default_4678292800 = _DEFAULT_MARKER

                # <Substitution "python:error and 'form-control is-invalid' or 'form-control'" (186:36)> -> __attr_class
                __token = 6991
                try:
                    __zt_tmp = __attrs_4678300912
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_4427992992('python', "error and 'form-control is-invalid' or 'form-control'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', 'form-control', _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append(' type="file" name="file" required />\n\n            ')

                # <Static value=<ast.Dict object at 0x116d91900> name=None at 116d92b30> -> __attrs_4678299520
                __attrs_4678299520 = _static_4678293760

                # <Value 'error' (190:29)> -> __condition
                __token = 7162
                try:
                    __zt_tmp = __attrs_4678299520
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="invalid-feedback">')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678288624
                    __default_4678288624 = _DEFAULT_MARKER

                    # <Value 'error' (189:27)> -> __cache_4678293328
                    __token = 7126
                    try:
                        __zt_tmp = __attrs_4678299520
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4678293328 = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'error' (189:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116d90430> -> __condition
                    __expression = __cache_4678293328

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                Validation error output\n            ')
                    else:
                        __content = __cache_4678293328
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>')
                __append('\n\n          </div>')
                if (__backup_error_4680352720 is __marker):
                    del econtext['error']
                else:
                    econtext['error'] = __backup_error_4680352720
                __append('\n\n          ')

                # <Static value=<ast.Dict object at 0x116d91a20> name=None at 116d91d80> -> __attrs_4678296112
                __attrs_4678296112 = _static_4678294048

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="formControls">\n            ')

                # <Static value=<ast.Dict object at 0x116d13040> name=None at 116d102e0> -> __attrs_4678240960
                __attrs_4678240960 = _static_4677775424

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="btn btn-success" type="submit" value="Upload" name="form.button.Upload">\n              ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680552784
                __attrs_4680552784 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680552352
                __default_4680552352 = _DEFAULT_MARKER

                # <Value "python:icons.tag('upload', tag_alt='Upload')" (202:47)> -> __cache_4678245472
                __token = 7488
                try:
                    __zt_tmp = __attrs_4680552784
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4678245472 = _static_4427992992('python', "icons.tag('upload', tag_alt='Upload')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('upload', tag_alt='Upload')" (202:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116d4be20> -> __condition
                __expression = __cache_4678245472

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4678245472
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(' ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680560176
                __attrs_4680560176 = _static_4428767312

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')
                __stream_4680552688 = []
                __append_4680552688 = __stream_4680552688.append
                __append_4680552688('Upload')
                __msgid_4680552688 = __re_whitespace(''.join(__stream_4680552688)).strip()
                if __msgid_4680552688:
                    __append(translate(__msgid_4680552688, mapping=None, default=__msgid_4680552688, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</span>\n            </button>\n          </div>\n\n        </fieldset>\n      </form>\n\n      ')

                # <Static value=<ast.Dict object at 0x116d91fc0> name=None at 116d855a0> -> __attrs_4680554560
                __attrs_4680554560 = _static_4678295488

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form class="mb-4"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680560032
                __default_4680560032 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${view/view_url}#manage-existing-aliases' (210:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 116fbacb0> -> __attr_action
                __token = 7693
                __token = 7695
                try:
                    __zt_tmp = __attrs_4680554560
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_action = _static_4427992992('path', 'view/view_url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_action = ('%s%s' % ((__attr_action if (__attr_action is not None) else ''), '#manage-existing-aliases', ))
                if (__attr_action is None):
                    pass
                else:
                    if (__attr_action is _DEFAULT_MARKER):
                        __attr_action = None
                    else:
                        __tt = type(__attr_action)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __attr_action = str(__attr_action)
                        else:
                            if (__tt is bytes):
                                __attr_action = decode(__attr_action)
                            else:
                                if (__tt is not str):
                                    try:
                                        __attr_action = __attr_action.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__attr_action)
                                        __attr_action = (str(__attr_action) if (__attr_action is __converted) else __converted)
                                    else:
                                        __attr_action = __attr_action()
                if (__attr_action is not None):
                    __append((' action="%s"' % __attr_action))
                __append(' method="post" id="manage-existing-aliases">\n        ')

                # <Static value=<ast.Dict object at 0x116fbb280> name=None at 116fbb2e0> -> __attrs_4680551248
                __attrs_4680551248 = _static_4680561280
                __backup_batch_4678203232 = get('batch', __marker)

                # <Value 'view/redirects' (214:28)> -> __value
                __token = 7858
                try:
                    __zt_tmp = __attrs_4680551248
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'view/redirects', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['batch'] = __value

                # <fieldset ... (0:0)
                # --------------------------------------------------------
                __append('<fieldset class="mb-3">\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680549280
                __attrs_4680549280 = _static_4428767312

                # <legend ... (0:0)
                # --------------------------------------------------------
                __append('<legend>')
                __stream_4680554224 = []
                __append_4680554224 = __stream_4680554224.append
                __append_4680554224('\n            All existing alternative urls for this site\n          ')
                __msgid_4680554224 = __re_whitespace(''.join(__stream_4680554224)).strip()
                if 'legend_all_existing_aliases':
                    __append(translate('legend_all_existing_aliases', mapping=None, default=__msgid_4680554224, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</legend>\n\n          ')

                # <Static value=<ast.Dict object at 0x116fbb8b0> name=None at 116fbb940> -> __attrs_4680556768
                __attrs_4680556768 = _static_4680562864

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="mb-4">\n            ')

                # <Static value=<ast.Dict object at 0x116fbb340> name=None at 116fbb5e0> -> __attrs_4680553024
                __attrs_4680553024 = _static_4680561472

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="btn btn-primary context" type="submit" value="Download all as CSV" name="form.button.Download">\n                ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680558448
                __attrs_4680558448 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680557248
                __default_4680557248 = _DEFAULT_MARKER

                # <Value "python:icons.tag('download', tag_alt='Download')" (225:49)> -> __cache_4680564016
                __token = 8281
                try:
                    __zt_tmp = __attrs_4680558448
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4680564016 = _static_4427992992('python', "icons.tag('download', tag_alt='Download')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('download', tag_alt='Download')" (225:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116fbbc40> -> __condition
                __expression = __cache_4680564016

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4680564016
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(' ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680557296
                __attrs_4680557296 = _static_4428767312

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')
                __stream_4680558064 = []
                __append_4680558064 = __stream_4680558064.append
                __append_4680558064('Download all as CSV')
                __msgid_4680558064 = __re_whitespace(''.join(__stream_4680558064)).strip()
                if __msgid_4680558064:
                    __append(translate(__msgid_4680558064, mapping=None, default=__msgid_4680558064, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</span>\n            </button>\n          </div>\n\n          ')

                # <Static value=<ast.Dict object at 0x116fbb0d0> name=None at 116fba980> -> __attrs_4680558784
                __attrs_4680558784 = _static_4680560848

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="mb-3">\n            ')

                # <Static value=<ast.Dict object at 0x116d8f280> name=None at 116d8df90> -> __attrs_4678286592
                __attrs_4678286592 = _static_4678283904

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="form-label" for="filter-existing-aliases-q">')
                __stream_4678285776 = []
                __append_4678285776 = __stream_4678285776.append
                __append_4678285776('Filter by prefix')
                __msgid_4678285776 = __re_whitespace(''.join(__stream_4678285776)).strip()
                if __msgid_4678285776:
                    __append(translate(__msgid_4678285776, mapping=None, default=__msgid_4678285776, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>\n            ')

                # <Static value=<ast.Dict object at 0x116d8db40> name=None at 116d8d3c0> -> __attrs_4680434256
                __attrs_4680434256 = _static_4678277952

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="form-control" type="text" name="q"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680434352
                __default_4680434352 = _DEFAULT_MARKER

                # <Substitution "python:request.form.get('q', '/')" (236:38)> -> __attr_value
                __token = 8770
                try:
                    __zt_tmp = __attrs_4680434256
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('python', "request.form.get('q', '/')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' id="filter-existing-aliases-q"/>\n          </div>\n\n          ')

                # <Static value=<ast.Dict object at 0x116f9e410> name=None at 116f9e6b0> -> __attrs_4680443088
                __attrs_4680443088 = _static_4680442896

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="mb-3">\n            ')

                # <Static value=<ast.Dict object at 0x116f9f850> name=None at 116f9d9c0> -> __attrs_4680440736
                __attrs_4680440736 = _static_4680448080

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="form-label" for="filter-existing-aliases-manual">')
                __stream_4680441504 = []
                __append_4680441504 = __stream_4680441504.append
                __append_4680441504('Manually or automatically added?')
                __msgid_4680441504 = __re_whitespace(''.join(__stream_4680441504)).strip()
                if __msgid_4680441504:
                    __append(translate(__msgid_4680441504, mapping=None, default=__msgid_4680441504, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>\n            ')

                # <Static value=<ast.Dict object at 0x116f9d360> name=None at 116f9d420> -> __attrs_4680438576
                __attrs_4680438576 = _static_4680438624
                __backup_chosen_4681952720 = get('chosen', __marker)

                # <Value "python:request.form.get('manual', '')" (243:31)> -> __value
                __token = 9103
                try:
                    __zt_tmp = __attrs_4680438576
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', "request.form.get('manual', '')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['chosen'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-check" id="filter-existing-aliases-manual">\n            ')

                # <Static value=<ast.Dict object at 0x116f9e950> name=None at 116f9e830> -> __attrs_4680443904
                __attrs_4680443904 = _static_4680444240

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="radio" name="manual" id="manual-both" class="form-check-input" value=""')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680440064
                __default_4680440064 = _DEFAULT_MARKER

                # <Boolean "python:chosen==''" (244:121)> -> __attr_checked
                __token = 9264
                try:
                    __zt_tmp = __attrs_4680443904
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_checked = _static_4427992992('python', "chosen==''", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if (__attr_checked is _DEFAULT_MARKER):
                    __attr_checked = None
                else:
                    if __attr_checked:
                        __attr_checked = 'checked'
                    else:
                        __attr_checked = None
                if (__attr_checked is not None):
                    __append((' checked="%s"' % __attr_checked))
                __append('>\n            ')

                # <Static value=<ast.Dict object at 0x116f9f0a0> name=None at 116f9d6c0> -> __attrs_4680439392
                __attrs_4680439392 = _static_4680446112

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label for="manual-both" class="form-check-label">')
                __stream_4680445488 = []
                __append_4680445488 = __stream_4680445488.append
                __append_4680445488('Both')
                __msgid_4680445488 = __re_whitespace(''.join(__stream_4680445488)).strip()
                if __msgid_4680445488:
                    __append(translate(__msgid_4680445488, mapping=None, default=__msgid_4680445488, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680435168
                __attrs_4680435168 = _static_4428767312

                # <br ... (0:0)
                # --------------------------------------------------------
                __append('<br />\n            ')

                # <Static value=<ast.Dict object at 0x116f9f340> name=None at 116f9f3a0> -> __attrs_4677981408
                __attrs_4677981408 = _static_4680446784

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="radio" name="manual" id="manual-no" class="form-check-input" value="no"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678201600
                __default_4678201600 = _DEFAULT_MARKER

                # <Boolean "python:chosen=='no'" (246:121)> -> __attr_checked
                __token = 9504
                try:
                    __zt_tmp = __attrs_4677981408
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_checked = _static_4427992992('python', "chosen=='no'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if (__attr_checked is _DEFAULT_MARKER):
                    __attr_checked = None
                else:
                    if __attr_checked:
                        __attr_checked = 'checked'
                    else:
                        __attr_checked = None
                if (__attr_checked is not None):
                    __append((' checked="%s"' % __attr_checked))
                __append('>\n            ')

                # <Static value=<ast.Dict object at 0x116d46b30> name=None at 116d46650> -> __attrs_4678225296
                __attrs_4678225296 = _static_4677987120

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label for="manual-no" class="form-check-label">')
                __stream_4677978144 = []
                __append_4677978144 = __stream_4677978144.append
                __append_4677978144('Automatically')
                __msgid_4677978144 = __re_whitespace(''.join(__stream_4677978144)).strip()
                if __msgid_4677978144:
                    __append(translate(__msgid_4677978144, mapping=None, default=__msgid_4677978144, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4678226208
                __attrs_4678226208 = _static_4428767312

                # <br ... (0:0)
                # --------------------------------------------------------
                __append('<br />\n            ')

                # <Static value=<ast.Dict object at 0x116d82740> name=None at 116d824d0> -> __attrs_4681907120
                __attrs_4681907120 = _static_4678231872

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="radio" name="manual" id="manual-yes" class="form-check-input" value="yes"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4681906352
                __default_4681906352 = _DEFAULT_MARKER

                # <Boolean "python:chosen=='yes'" (248:123)> -> __attr_checked
                __token = 9755
                try:
                    __zt_tmp = __attrs_4681907120
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_checked = _static_4427992992('python', "chosen=='yes'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if (__attr_checked is _DEFAULT_MARKER):
                    __attr_checked = None
                else:
                    if __attr_checked:
                        __attr_checked = 'checked'
                    else:
                        __attr_checked = None
                if (__attr_checked is not None):
                    __append((' checked="%s"' % __attr_checked))
                __append('>\n            ')

                # <Static value=<ast.Dict object at 0x117100910> name=None at 1171027a0> -> __attrs_4681902080
                __attrs_4681902080 = _static_4681894160

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label for="manual-yes" class="form-check-label">')
                __stream_4681900400 = []
                __append_4681900400 = __stream_4681900400.append
                __append_4681900400('Manually')
                __msgid_4681900400 = __re_whitespace(''.join(__stream_4681900400)).strip()
                if __msgid_4681900400:
                    __append(translate(__msgid_4681900400, mapping=None, default=__msgid_4681900400, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>\n          </div>')
                if (__backup_chosen_4681952720 is __marker):
                    del econtext['chosen']
                else:
                    econtext['chosen'] = __backup_chosen_4681952720
                __append('\n        </div>\n\n        ')

                # <Static value=<ast.Dict object at 0x117102ad0> name=None at 1171029e0> -> __attrs_4681895216
                __attrs_4681895216 = _static_4681902800

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="mb-3">\n          ')

                # <Static value=<ast.Dict object at 0x117102a70> name=None at 117102c50> -> __attrs_4681903952
                __attrs_4681903952 = _static_4681902704

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="form-label" for="filter-existing-aliases-date">')
                __stream_4681896512 = []
                __append_4681896512 = __stream_4681896512.append
                __append_4681896512('Created before')
                __msgid_4681896512 = __re_whitespace(''.join(__stream_4681896512)).strip()
                if __msgid_4681896512:
                    __append(translate(__msgid_4681896512, mapping=None, default=__msgid_4681896512, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>\n          ')

                # <Static value=<ast.Dict object at 0x1171016f0> name=None at 117101720> -> __attrs_4681897904
                __attrs_4681897904 = _static_4681897712

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="date" id="filter-existing-aliases-date" class="form-control" name="datetime"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4681898960
                __default_4681898960 = _DEFAULT_MARKER

                # <Substitution "python:request.form.get('datetime', '')" (256:32)> -> __attr_value
                __token = 10178
                try:
                    __zt_tmp = __attrs_4681897904
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('python', "request.form.get('datetime', '')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append('/>\n        </div>\n\n          ')

                # <Static value=<ast.Dict object at 0x117102da0> name=None at 117102dd0> -> __attrs_4680813776
                __attrs_4680813776 = _static_4681903520

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="formControls mb-4">\n            ')

                # <Static value=<ast.Dict object at 0x116ffab60> name=None at 116ffab30> -> __attrs_4680813296
                __attrs_4680813296 = _static_4680821600

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="btn btn-primary" type="submit" value="Filter" name="form.button.filter">\n              ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680813680
                __attrs_4680813680 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680825488
                __default_4680825488 = _DEFAULT_MARKER

                # <Value "python:icons.tag('filter', tag_alt='Filter')" (265:47)> -> __cache_4680824288
                __token = 10482
                try:
                    __zt_tmp = __attrs_4680813680
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4680824288 = _static_4427992992('python', "icons.tag('filter', tag_alt='Filter')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('filter', tag_alt='Filter')" (265:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116ffb730> -> __condition
                __expression = __cache_4680824288

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4680824288
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(' ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680822512
                __attrs_4680822512 = _static_4428767312

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')
                __stream_4680813824 = []
                __append_4680813824 = __stream_4680813824.append
                __append_4680813824('Filter')
                __msgid_4680813824 = __re_whitespace(''.join(__stream_4680813824)).strip()
                if __msgid_4680813824:
                    __append(translate(__msgid_4680813824, mapping=None, default=__msgid_4680813824, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</span>\n            </button>\n          </div>\n\n          ')

                # <Static value=<ast.Dict object at 0x116ffa410> name=None at 116ffa5f0> -> __attrs_4680823040
                __attrs_4680823040 = _static_4680819728
                __backup_error_4680541296 = get('error', __marker)

                # <Value 'view/form_errors/remove_redirects|nothing' (270:33)> -> __value
                __token = 10676
                try:
                    __zt_tmp = __attrs_4680823040
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'view/form_errors/remove_redirects|nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['error'] = __value

                # <Value 'error' (273:30)> -> __condition
                __token = 10874
                try:
                    __zt_tmp = __attrs_4680823040
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680820304
                    __default_4680820304 = _DEFAULT_MARKER

                    # <Substitution "python:error and 'field mb-3 error' or 'field mb-3'" (271:37)> -> __attr_class
                    __token = 10756
                    try:
                        __zt_tmp = __attrs_4680823040
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4427992992('python', "error and 'field mb-3 error' or 'field mb-3'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', 'field mb-3', _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680824672
                    __default_4680824672 = _DEFAULT_MARKER

                    # <Value 'error' (272:28)> -> __cache_4680815024
                    __token = 10837
                    try:
                        __zt_tmp = __attrs_4680823040
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4680815024 = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'error' (272:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116ffa980> -> __condition
                    __expression = __cache_4680815024

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4680815024
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>')
                if (__backup_error_4680541296 is __marker):
                    del econtext['error']
                else:
                    econtext['error'] = __backup_error_4680541296
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x116ff84c0> name=None at 116ff8310> -> __attrs_4680818576
                __attrs_4680818576 = _static_4680811712

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="mb-4">\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680819344
                __attrs_4680819344 = _static_4428767312

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p>')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680815936
                __attrs_4680815936 = _static_4428767312

                # <small ... (0:0)
                # --------------------------------------------------------
                __append('<small>')
                __stream_4680812624 = []
                __append_4680812624 = __stream_4680812624.append
                __append_4680812624('Alternative url path &rarr; target url path ')

                # <Static value=<ast.Dict object at 0x116ff9c90> name=None at 116ff9cf0> -> __attrs_4680823616
                __attrs_4680823616 = _static_4680817808

                # <span ... (0:0)
                # --------------------------------------------------------
                __append_4680812624('<span class="text-muted">(date and time of creation, manually created yes/no)</span>')
                __msgid_4680812624 = __re_whitespace(''.join(__stream_4680812624)).strip()
                if __msgid_4680812624:
                    __append(translate(__msgid_4680812624, mapping=None, default=__msgid_4680812624, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</small></p>\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680817280
                __attrs_4680817280 = _static_4428767312
                __backup_redirect_4680532848 = get('redirect', __marker)

                # <Value 'batch' (277:42)> -> __iterator
                __token = 11133
                try:
                    __zt_tmp = __attrs_4680817280
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4427992992('path', 'batch', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                (__iterator, ____index_4680817568, ) = getname('repeat')('redirect', __iterator)
                econtext['redirect'] = None
                for __item in __iterator:
                    econtext['redirect'] = __item
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x116ff99f0> name=None at 116ff9a50> -> __attrs_4680507760
                    __attrs_4680507760 = _static_4680817136

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-check">\n              ')

                    # <Static value=<ast.Dict object at 0x116fac8b0> name=None at 116fac940> -> __attrs_4680509488
                    __attrs_4680509488 = _static_4680501424

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append('<label class="form-check-label">\n              ')

                    # <Static value=<ast.Dict object at 0x116fafb20> name=None at 116fafd00> -> __attrs_4680506080
                    __attrs_4680506080 = _static_4680514336

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="checkbox" class="form-check-input noborder" name="redirects:tuple"')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680503584
                    __default_4680503584 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution '${redirect/redirect}' (284:25)> braces_required=True translation=False default='"?"' default_marker='"?"' at 116fad0f0> -> __attr_value
                    __token = 11398
                    __token = 11400
                    try:
                        __zt_tmp = __attrs_4680506080
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_4427992992('path', 'redirect/redirect', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_value = __attr_value
                    if (__attr_value is None):
                        pass
                    else:
                        if (__attr_value is _DEFAULT_MARKER):
                            __attr_value = None
                        else:
                            __tt = type(__attr_value)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_value = str(__attr_value)
                            else:
                                if (__tt is bytes):
                                    __attr_value = decode(__attr_value)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_value = __attr_value.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_value)
                                            __attr_value = (str(__attr_value) if (__attr_value is __converted) else __converted)
                                        else:
                                            __attr_value = __attr_value()
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />')

                    # <Interpolation value=<Substitution '\n              ${redirect/path} &rarr; ${redirect/redirect-to} ' (284:49)> braces_required=True translation=False default='"?"' default_marker='"?"' at 116fada20> -> __content_4353737008
                    __token = 11437
                    __token = 11439
                    try:
                        __zt_tmp = __attrs_4680509488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_4353737008 = _static_4427992992('path', 'redirect/path', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __content_4353737008 = __quote(__content_4353737008, '\x00', '&#0;', None, None)
                    __token = 11463
                    try:
                        __zt_tmp = __attrs_4680509488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_4353737008_11461 = _static_4427992992('path', 'redirect/redirect-to', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __content_4353737008_11461 = __quote(__content_4353737008_11461, '\x00', '&#0;', None, None)
                    __content_4353737008 = ('%s%s%s%s%s' % ('\n              ', (__content_4353737008 if (__content_4353737008 is not None) else ''), ' &rarr; ', (__content_4353737008_11461 if (__content_4353737008_11461 is not None) else ''), ' ', ))
                    if (__content_4353737008 is None):
                        pass
                    else:
                        if (__content_4353737008 is None):
                            __content_4353737008 = None
                        else:
                            __tt = type(__content_4353737008)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_4353737008 = str(__content_4353737008)
                            else:
                                if (__tt is bytes):
                                    __content_4353737008 = decode(__content_4353737008)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_4353737008 = __content_4353737008.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_4353737008)
                                            __content_4353737008 = (str(__content_4353737008) if (__content_4353737008 is __converted) else __converted)
                                        else:
                                            __content_4353737008 = __content_4353737008()
                    if (__content_4353737008 is not None):
                        __append(__content_4353737008)

                    # <Static value=<ast.Dict object at 0x116fad960> name=None at 116fad000> -> __attrs_4680502720
                    __attrs_4680502720 = _static_4680505696

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="text-muted">')

                    # <Interpolation value=<Substitution '(${redirect/datetime}, ${redirect/manual})' (285:87)> braces_required=True translation=False default='"?"' default_marker='"?"' at 116faec50> -> __content_4353737008
                    __token = 11510
                    __token = 11513
                    try:
                        __zt_tmp = __attrs_4680502720
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_4353737008 = _static_4427992992('path', 'redirect/datetime', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __content_4353737008 = __quote(__content_4353737008, '\x00', '&#0;', None, None)
                    __token = 11535
                    try:
                        __zt_tmp = __attrs_4680502720
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_4353737008_11533 = _static_4427992992('path', 'redirect/manual', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __content_4353737008_11533 = __quote(__content_4353737008_11533, '\x00', '&#0;', None, None)
                    __content_4353737008 = ('%s%s%s%s%s' % ('(', (__content_4353737008 if (__content_4353737008 is not None) else ''), ', ', (__content_4353737008_11533 if (__content_4353737008_11533 is not None) else ''), ')', ))
                    if (__content_4353737008 is None):
                        pass
                    else:
                        if (__content_4353737008 is None):
                            __content_4353737008 = None
                        else:
                            __tt = type(__content_4353737008)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_4353737008 = str(__content_4353737008)
                            else:
                                if (__tt is bytes):
                                    __content_4353737008 = decode(__content_4353737008)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_4353737008 = __content_4353737008.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_4353737008)
                                            __content_4353737008 = (str(__content_4353737008) if (__content_4353737008 is __converted) else __converted)
                                        else:
                                            __content_4353737008 = __content_4353737008()
                    if (__content_4353737008 is not None):
                        __append(__content_4353737008)
                    __append('</span>\n              </label>\n            </div>\n          ')
                    ____index_4680817568 -= 1
                    if (____index_4680817568 > 0):
                        __append('')
                if (__backup_redirect_4680532848 is __marker):
                    del econtext['redirect']
                else:
                    econtext['redirect'] = __backup_redirect_4680532848
                __append('\n        </div>\n\n        ')

                # <Static value=<ast.Dict object at 0x116ff86d0> name=None at 116ff95a0> -> __attrs_4680500080
                __attrs_4680500080 = _static_4680812240

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="justify-content-center mb-4">\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680508672
                __attrs_4680508672 = _static_4428767312

                # <Value 'python:batch.numpages > 1' (292:30)> -> __condition
                __token = 11725
                try:
                    __zt_tmp = __attrs_4680508672
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('python', 'batch.numpages > 1', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680508336
                    __default_4680508336 = _DEFAULT_MARKER

                    # <Value 'view/batching' (293:38)> -> __cache_4680515056
                    __token = 11790
                    try:
                        __zt_tmp = __attrs_4680508672
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4680515056 = _static_4427992992('path', 'view/batching', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/batching' (293:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116fad3f0> -> __condition
                    __expression = __cache_4680515056

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div>\n          </div>')
                    else:
                        __content = __cache_4680515056
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                __append('\n        </div>\n\n          ')

                # <Static value=<ast.Dict object at 0x116fac0a0> name=None at 116fac130> -> __attrs_4680508816
                __attrs_4680508816 = _static_4680499360

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="formControls">\n            ')

                # <Static value=<ast.Dict object at 0x116faf070> name=None at 116faefe0> -> __attrs_4681950800
                __attrs_4681950800 = _static_4680511600

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="btn btn-danger" type="submit" value="Remove selected" name="form.button.Remove">\n                ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4681955072
                __attrs_4681955072 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4681954928
                __default_4681954928 = _DEFAULT_MARKER

                # <Value "python:icons.tag('trash', tag_alt='Trash')" (302:49)> -> __cache_4681944368
                __token = 12075
                try:
                    __zt_tmp = __attrs_4681955072
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4681944368 = _static_4427992992('python', "icons.tag('trash', tag_alt='Trash')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('trash', tag_alt='Trash')" (302:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 11710ce20> -> __condition
                __expression = __cache_4681944368

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4681944368
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(' ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4681942016
                __attrs_4681942016 = _static_4428767312

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')
                __stream_4681955264 = []
                __append_4681955264 = __stream_4681955264.append
                __append_4681955264('Remove selected')
                __msgid_4681955264 = __re_whitespace(''.join(__stream_4681955264)).strip()
                if __msgid_4681955264:
                    __append(translate(__msgid_4681955264, mapping=None, default=__msgid_4681955264, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</span>\n            </button>\n            ')

                # <Static value=<ast.Dict object at 0x11710e020> name=None at 11710de70> -> __attrs_4681947776
                __attrs_4681947776 = _static_4681949216

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="btn btn-danger" type="submit" value="Remove all that match filter" name="form.button.MatchRemove">\n                ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4681949888
                __attrs_4681949888 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4681949648
                __default_4681949648 = _DEFAULT_MARKER

                # <Value "python:icons.tag('trash', tag_alt='Trash')" (308:49)> -> __cache_4681948928
                __token = 12408
                try:
                    __zt_tmp = __attrs_4681949888
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4681948928 = _static_4427992992('python', "icons.tag('trash', tag_alt='Trash')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('trash', tag_alt='Trash')" (308:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 11710d630> -> __condition
                __expression = __cache_4681948928

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4681948928
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(' ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4681952480
                __attrs_4681952480 = _static_4428767312

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')
                __stream_4681951616 = []
                __append_4681951616 = __stream_4681951616.append
                __append_4681951616('Remove all that match filter')
                __msgid_4681951616 = __re_whitespace(''.join(__stream_4681951616)).strip()
                if __msgid_4681951616:
                    __append(translate(__msgid_4681951616, mapping=None, default=__msgid_4681951616, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</span>\n            </button>\n          </div>\n\n        </fieldset>')
                if (__backup_batch_4678203232 is __marker):
                    del econtext['batch']
                else:
                    econtext['batch'] = __backup_batch_4678203232
                __append('\n      </form>\n    ')
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'context/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_4680536640
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4427992992('path', 'context/prefs_main_template/macros/master', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4671392000 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4671392000
            __i18n_domain = __previous_i18n_domain_4680536736
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }