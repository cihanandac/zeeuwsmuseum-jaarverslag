# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/z3cform/templates/checkbox_input.pt'

__tokens = {139: ('view/items', 4, 23), 173: (' python:list(items', 5, 22), 225: ('x python:len(items) ==', 6, 31), 341: ('python:len(items) > 0', 9, 20), 304: ('single_checkbox', 8, 19), 276: ('view/id', 7, 24), 414: ('items', 11, 24), 447: ('python:single_checkbox and view.id or None', 12, 26), 674: ('item/checked', 16, 24), 716: ('item/id', 17, 28), 754: (' item/nam', 18, 29), 795: ('s string:form-check-input ${view/klas', 19, 29), 1820: ('        ', 40, 6), 948: ('itle view/', 22, 26), 1591: ('         tabi', 35, 16), 1543: ('        disab', 34, 17), 1777: ('             ', 39, 12), 1864: ('              ', 41, 11), 864: ('ue item/va', 20, 28), 906: ('yle view/s', 21, 27), 989: (' lang vie', 23, 24), 1032: ('nclick view/', 24, 26), 1081: ('blclick view/on', 25, 28), 1134: ('ousedown view/on', 26, 28), 1186: ('onmouseup view', 27, 25), 1238: ('nmouseover view/', 28, 26), 1292: ('onmousemove view', 29, 25), 1345: ('  onmouseout vi', 30, 23), 1397: ('   onkeypress v', 31, 22), 1448: ('     onkeydown', 32, 20), 1496: ('        onke', 33, 17), 1638: ('           o', 36, 14), 1683: ('           ', 37, 12), 1729: ('            o', 38, 13), 1913: ('             ', 42, 9), 2123: ('not:item/checked', 46, 24), 2169: ('item/id', 47, 28), 2207: (' item/nam', 48, 29), 2248: ('s string:form-check-input ${view/klas', 49, 29), 3273: ('        ', 70, 6), 2401: ('itle view/', 52, 26), 3044: ('         tabi', 65, 16), 2996: ('        disab', 64, 17), 3230: ('             ', 69, 12), 3317: ('              ', 71, 11), 2317: ('ue item/va', 50, 28), 2359: ('yle view/s', 51, 27), 2442: (' lang vie', 53, 24), 2485: ('nclick view/', 54, 26), 2534: ('blclick view/on', 55, 28), 2587: ('ousedown view/on', 56, 28), 2639: ('onmouseup view', 57, 25), 2691: ('nmouseover view/', 58, 26), 2745: ('onmousemove view', 59, 25), 2798: ('  onmouseout vi', 60, 23), 2850: ('   onkeypress v', 61, 22), 2901: ('     onkeydown', 62, 20), 2949: ('        onke', 63, 17), 3091: ('           o', 66, 14), 3136: ('           ', 67, 12), 3182: ('            o', 68, 13), 3366: ('             ', 72, 9), 3479: ('item/id', 74, 29), 3526: ('item/label', 75, 37), 3662: ('string:${view/name}-empty-marker', 80, 28)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4680554032 = {'name': 'field-empty-marker', 'type': 'hidden', 'value': '1', }
_static_4680552208 = {'class': 'label', }
_static_4680557776 = {'class': 'form-check-label', 'for': '', }
_static_4677385664 = {'id': '', 'name': '', 'class': '', 'alt': '', 'title': '', 'tabindex': '', 'disabled': '', 'readonly': '', 'accesskey': '', 'value': '', 'type': 'checkbox', 'style': 'view/style', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'onselect': 'view/onselect', }
_static_4677689664 = {'type': 'checkbox', 'id': '', 'name': '', 'class': '', 'alt': '', 'title': '', 'tabindex': '', 'disabled': '', 'readonly': '', 'accesskey': '', 'value': '', 'checked': 'checked', 'style': 'view/style', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'onselect': 'view/onselect', }
_static_4677684048 = {'class': 'form-check', 'id': 'python:single_checkbox and view.id or None', }
_static_4678204672 = {'id': 'view/id', }
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
_static_4678194832 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x116d79690> name=None at 116d79180> -> __attrs_4678197520
            __attrs_4678197520 = _static_4678194832
            __backup_items_4683178448 = get('items', __marker)

            # <Value 'view/items' (4:23)> -> __value
            __token = 139
            try:
                __zt_tmp = __attrs_4678197520
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'view/items', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['items'] = __value
            __backup_items_4678054816 = get('items', __marker)

            # <Value 'python:list(items)' (5:22)> -> __value
            __token = 173
            try:
                __zt_tmp = __attrs_4678197520
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', 'list(items)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['items'] = __value
            __backup_single_checkbox_4682730800 = get('single_checkbox', __marker)

            # <Value 'python:len(items) == 1' (6:31)> -> __value
            __token = 225
            try:
                __zt_tmp = __attrs_4678197520
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', 'len(items) == 1', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['single_checkbox'] = __value
            __append('\n')

            # <Static value=<ast.Dict object at 0x116d7bd00> name=None at 116d795d0> -> __attrs_4678198768
            __attrs_4678198768 = _static_4678204672

            # <Value 'python:len(items) > 0' (9:20)> -> __condition
            __token = 341
            try:
                __zt_tmp = __attrs_4678198768
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('python', 'len(items) > 0', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <Negate value=<Value 'single_checkbox' (8:19)> at 116d791e0> -> __cache_4678193632

                # <Value 'single_checkbox' (8:19)> -> __cache_4678193632
                __token = 304
                try:
                    __zt_tmp = __attrs_4678198768
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4678193632 = _static_4427992992('path', 'single_checkbox', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __cache_4678193632 = not __cache_4678193632
                __condition = __cache_4678193632
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678196704
                    __default_4678196704 = _DEFAULT_MARKER

                    # <Substitution 'view/id' (7:24)> -> __attr_id
                    __token = 276
                    try:
                        __zt_tmp = __attrs_4678198768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_4427992992('path', 'view/id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))
                    __append('>')
                __append('\n ')

                # <Static value=<ast.Dict object at 0x116cfcb50> name=None at 116cfdea0> -> __attrs_4677683376
                __attrs_4677683376 = _static_4677684048
                __backup_item_4681905488 = get('item', __marker)

                # <Value 'items' (11:24)> -> __iterator
                __token = 414
                try:
                    __zt_tmp = __attrs_4677683376
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4427992992('path', 'items', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                (__iterator, ____index_4677695760, ) = getname('repeat')('item', __iterator)
                econtext['item'] = None
                for __item in __iterator:
                    econtext['item'] = __item

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-check"')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4677691920
                    __default_4677691920 = _DEFAULT_MARKER

                    # <Substitution 'python:single_checkbox and view.id or None' (12:26)> -> __attr_id
                    __token = 447
                    try:
                        __zt_tmp = __attrs_4677683376
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_4427992992('python', 'single_checkbox and view.id or None', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))
                    __append('>\n  ')

                    # <Static value=<ast.Dict object at 0x116cfe140> name=None at 116cfff10> -> __attrs_4672878288
                    __attrs_4672878288 = _static_4677689664

                    # <Value 'item/checked' (16:24)> -> __condition
                    __token = 674
                    try:
                        __zt_tmp = __attrs_4672878288
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('path', 'item/checked', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="checkbox"')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4677684720
                        __default_4677684720 = _DEFAULT_MARKER

                        # <Substitution 'item/id' (17:28)> -> __attr_id
                        __token = 716
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_4427992992('path', 'item/id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((' id="%s"' % __attr_id))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4677690528
                        __default_4677690528 = _DEFAULT_MARKER

                        # <Substitution 'item/name' (18:29)> -> __attr_name
                        __token = 754
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_4427992992('path', 'item/name', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4677690240
                        __default_4677690240 = _DEFAULT_MARKER

                        # <Substitution 'string:form-check-input ${view/klass}' (19:29)> -> __attr_class
                        __token = 795
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_4427992992('string', 'form-check-input ${view/klass}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4677694464
                        __default_4677694464 = _DEFAULT_MARKER

                        # <Substitution 'view/alt' (40:6)> -> __attr_alt
                        __token = 1820
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_alt = _static_4427992992('path', 'view/alt', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_alt is not None):
                            __append((' alt="%s"' % __attr_alt))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678026528
                        __default_4678026528 = _DEFAULT_MARKER

                        # <Substitution 'view/title' (22:26)> -> __attr_title
                        __token = 948
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_4427992992('path', 'view/title', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678026816
                        __default_4678026816 = _DEFAULT_MARKER

                        # <Substitution 'view/tabindex' (35:16)> -> __attr_tabindex
                        __token = 1591
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_tabindex = _static_4427992992('path', 'view/tabindex', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_tabindex is not None):
                            __append((' tabindex="%s"' % __attr_tabindex))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678036176
                        __default_4678036176 = _DEFAULT_MARKER

                        # <Boolean 'view/disabled' (34:17)> -> __attr_disabled
                        __token = 1543
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_disabled = _static_4427992992('path', 'view/disabled', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        if (__attr_disabled is _DEFAULT_MARKER):
                            __attr_disabled = ''
                        else:
                            if __attr_disabled:
                                __attr_disabled = 'disabled'
                            else:
                                __attr_disabled = None
                        if (__attr_disabled is not None):
                            __append((' disabled="%s"' % __attr_disabled))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678028496
                        __default_4678028496 = _DEFAULT_MARKER

                        # <Boolean 'view/readonly' (39:12)> -> __attr_readonly
                        __token = 1777
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_readonly = _static_4427992992('path', 'view/readonly', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        if (__attr_readonly is _DEFAULT_MARKER):
                            __attr_readonly = ''
                        else:
                            if __attr_readonly:
                                __attr_readonly = 'readonly'
                            else:
                                __attr_readonly = None
                        if (__attr_readonly is not None):
                            __append((' readonly="%s"' % __attr_readonly))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678027488
                        __default_4678027488 = _DEFAULT_MARKER

                        # <Substitution 'view/accesskey' (41:11)> -> __attr_accesskey
                        __token = 1864
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_accesskey = _static_4427992992('path', 'view/accesskey', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_accesskey is not None):
                            __append((' accesskey="%s"' % __attr_accesskey))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678031952
                        __default_4678031952 = _DEFAULT_MARKER

                        # <Substitution 'item/value' (20:28)> -> __attr_value
                        __token = 864
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_4427992992('path', 'item/value', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' checked="checked"')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678032336
                        __default_4678032336 = _DEFAULT_MARKER

                        # <Substitution 'view/style' (21:27)> -> __attr_style
                        __token = 906
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_style = _static_4427992992('path', 'view/style', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_style is not None):
                            __append((' style="%s"' % __attr_style))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678037664
                        __default_4678037664 = _DEFAULT_MARKER

                        # <Substitution 'view/lang' (23:24)> -> __attr_lang
                        __token = 989
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_lang = _static_4427992992('path', 'view/lang', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_lang is not None):
                            __append((' lang="%s"' % __attr_lang))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678039536
                        __default_4678039536 = _DEFAULT_MARKER

                        # <Substitution 'view/onclick' (24:26)> -> __attr_onclick
                        __token = 1032
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onclick = _static_4427992992('path', 'view/onclick', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onclick is not None):
                            __append((' onclick="%s"' % __attr_onclick))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678029168
                        __default_4678029168 = _DEFAULT_MARKER

                        # <Substitution 'view/ondblclick' (25:28)> -> __attr_ondblclick
                        __token = 1081
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_ondblclick = _static_4427992992('path', 'view/ondblclick', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_ondblclick is not None):
                            __append((' ondblclick="%s"' % __attr_ondblclick))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678027536
                        __default_4678027536 = _DEFAULT_MARKER

                        # <Substitution 'view/onmousedown' (26:28)> -> __attr_onmousedown
                        __token = 1134
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousedown = _static_4427992992('path', 'view/onmousedown', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousedown is not None):
                            __append((' onmousedown="%s"' % __attr_onmousedown))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678030272
                        __default_4678030272 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseup' (27:25)> -> __attr_onmouseup
                        __token = 1186
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseup = _static_4427992992('path', 'view/onmouseup', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseup is not None):
                            __append((' onmouseup="%s"' % __attr_onmouseup))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678037472
                        __default_4678037472 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseover' (28:26)> -> __attr_onmouseover
                        __token = 1238
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseover = _static_4427992992('path', 'view/onmouseover', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseover is not None):
                            __append((' onmouseover="%s"' % __attr_onmouseover))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678026336
                        __default_4678026336 = _DEFAULT_MARKER

                        # <Substitution 'view/onmousemove' (29:25)> -> __attr_onmousemove
                        __token = 1292
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousemove = _static_4427992992('path', 'view/onmousemove', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousemove is not None):
                            __append((' onmousemove="%s"' % __attr_onmousemove))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678040976
                        __default_4678040976 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseout' (30:23)> -> __attr_onmouseout
                        __token = 1345
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseout = _static_4427992992('path', 'view/onmouseout', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseout is not None):
                            __append((' onmouseout="%s"' % __attr_onmouseout))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678032768
                        __default_4678032768 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeypress' (31:22)> -> __attr_onkeypress
                        __token = 1397
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeypress = _static_4427992992('path', 'view/onkeypress', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeypress is not None):
                            __append((' onkeypress="%s"' % __attr_onkeypress))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678041456
                        __default_4678041456 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeydown' (32:20)> -> __attr_onkeydown
                        __token = 1448
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeydown = _static_4427992992('path', 'view/onkeydown', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeydown is not None):
                            __append((' onkeydown="%s"' % __attr_onkeydown))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678032912
                        __default_4678032912 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeyup' (33:17)> -> __attr_onkeyup
                        __token = 1496
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeyup = _static_4427992992('path', 'view/onkeyup', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeyup is not None):
                            __append((' onkeyup="%s"' % __attr_onkeyup))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678039392
                        __default_4678039392 = _DEFAULT_MARKER

                        # <Substitution 'view/onfocus' (36:14)> -> __attr_onfocus
                        __token = 1638
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onfocus = _static_4427992992('path', 'view/onfocus', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onfocus is not None):
                            __append((' onfocus="%s"' % __attr_onfocus))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4672872192
                        __default_4672872192 = _DEFAULT_MARKER

                        # <Substitution 'view/onblur' (37:12)> -> __attr_onblur
                        __token = 1683
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onblur = _static_4427992992('path', 'view/onblur', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onblur is not None):
                            __append((' onblur="%s"' % __attr_onblur))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4672875504
                        __default_4672875504 = _DEFAULT_MARKER

                        # <Substitution 'view/onchange' (38:13)> -> __attr_onchange
                        __token = 1729
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onchange = _static_4427992992('path', 'view/onchange', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onchange is not None):
                            __append((' onchange="%s"' % __attr_onchange))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4672879344
                        __default_4672879344 = _DEFAULT_MARKER

                        # <Substitution 'view/onselect' (42:9)> -> __attr_onselect
                        __token = 1913
                        try:
                            __zt_tmp = __attrs_4672878288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onselect = _static_4427992992('path', 'view/onselect', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onselect is not None):
                            __append((' onselect="%s"' % __attr_onselect))
                        __append(' />')

                    # <Static value=<ast.Dict object at 0x116cb3dc0> name=None at 116cb3010> -> __attrs_4680550288
                    __attrs_4680550288 = _static_4677385664

                    # <Value 'not:item/checked' (46:24)> -> __condition
                    __token = 2123
                    try:
                        __zt_tmp = __attrs_4680550288
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('not', 'item/checked', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4677373232
                        __default_4677373232 = _DEFAULT_MARKER

                        # <Substitution 'item/id' (47:28)> -> __attr_id
                        __token = 2169
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_4427992992('path', 'item/id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((' id="%s"' % __attr_id))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4677382400
                        __default_4677382400 = _DEFAULT_MARKER

                        # <Substitution 'item/name' (48:29)> -> __attr_name
                        __token = 2207
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_4427992992('path', 'item/name', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4677374624
                        __default_4677374624 = _DEFAULT_MARKER

                        # <Substitution 'string:form-check-input ${view/klass}' (49:29)> -> __attr_class
                        __token = 2248
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_4427992992('string', 'form-check-input ${view/klass}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4677373376
                        __default_4677373376 = _DEFAULT_MARKER

                        # <Substitution 'view/alt' (70:6)> -> __attr_alt
                        __token = 3273
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_alt = _static_4427992992('path', 'view/alt', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_alt is not None):
                            __append((' alt="%s"' % __attr_alt))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4677381728
                        __default_4677381728 = _DEFAULT_MARKER

                        # <Substitution 'view/title' (52:26)> -> __attr_title
                        __token = 2401
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_4427992992('path', 'view/title', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678057456
                        __default_4678057456 = _DEFAULT_MARKER

                        # <Substitution 'view/tabindex' (65:16)> -> __attr_tabindex
                        __token = 3044
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_tabindex = _static_4427992992('path', 'view/tabindex', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_tabindex is not None):
                            __append((' tabindex="%s"' % __attr_tabindex))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678042576
                        __default_4678042576 = _DEFAULT_MARKER

                        # <Boolean 'view/disabled' (64:17)> -> __attr_disabled
                        __token = 2996
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_disabled = _static_4427992992('path', 'view/disabled', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        if (__attr_disabled is _DEFAULT_MARKER):
                            __attr_disabled = ''
                        else:
                            if __attr_disabled:
                                __attr_disabled = 'disabled'
                            else:
                                __attr_disabled = None
                        if (__attr_disabled is not None):
                            __append((' disabled="%s"' % __attr_disabled))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678052944
                        __default_4678052944 = _DEFAULT_MARKER

                        # <Boolean 'view/readonly' (69:12)> -> __attr_readonly
                        __token = 3230
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_readonly = _static_4427992992('path', 'view/readonly', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        if (__attr_readonly is _DEFAULT_MARKER):
                            __attr_readonly = ''
                        else:
                            if __attr_readonly:
                                __attr_readonly = 'readonly'
                            else:
                                __attr_readonly = None
                        if (__attr_readonly is not None):
                            __append((' readonly="%s"' % __attr_readonly))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678042768
                        __default_4678042768 = _DEFAULT_MARKER

                        # <Substitution 'view/accesskey' (71:11)> -> __attr_accesskey
                        __token = 3317
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_accesskey = _static_4427992992('path', 'view/accesskey', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_accesskey is not None):
                            __append((' accesskey="%s"' % __attr_accesskey))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678044496
                        __default_4678044496 = _DEFAULT_MARKER

                        # <Substitution 'item/value' (50:28)> -> __attr_value
                        __token = 2317
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_4427992992('path', 'item/value', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' type="checkbox"')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678053328
                        __default_4678053328 = _DEFAULT_MARKER

                        # <Substitution 'view/style' (51:27)> -> __attr_style
                        __token = 2359
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_style = _static_4427992992('path', 'view/style', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_style is not None):
                            __append((' style="%s"' % __attr_style))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678053424
                        __default_4678053424 = _DEFAULT_MARKER

                        # <Substitution 'view/lang' (53:24)> -> __attr_lang
                        __token = 2442
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_lang = _static_4427992992('path', 'view/lang', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_lang is not None):
                            __append((' lang="%s"' % __attr_lang))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678053184
                        __default_4678053184 = _DEFAULT_MARKER

                        # <Substitution 'view/onclick' (54:26)> -> __attr_onclick
                        __token = 2485
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onclick = _static_4427992992('path', 'view/onclick', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onclick is not None):
                            __append((' onclick="%s"' % __attr_onclick))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678044016
                        __default_4678044016 = _DEFAULT_MARKER

                        # <Substitution 'view/ondblclick' (55:28)> -> __attr_ondblclick
                        __token = 2534
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_ondblclick = _static_4427992992('path', 'view/ondblclick', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_ondblclick is not None):
                            __append((' ondblclick="%s"' % __attr_ondblclick))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678048432
                        __default_4678048432 = _DEFAULT_MARKER

                        # <Substitution 'view/onmousedown' (56:28)> -> __attr_onmousedown
                        __token = 2587
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousedown = _static_4427992992('path', 'view/onmousedown', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousedown is not None):
                            __append((' onmousedown="%s"' % __attr_onmousedown))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678042000
                        __default_4678042000 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseup' (57:25)> -> __attr_onmouseup
                        __token = 2639
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseup = _static_4427992992('path', 'view/onmouseup', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseup is not None):
                            __append((' onmouseup="%s"' % __attr_onmouseup))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678051984
                        __default_4678051984 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseover' (58:26)> -> __attr_onmouseover
                        __token = 2691
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseover = _static_4427992992('path', 'view/onmouseover', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseover is not None):
                            __append((' onmouseover="%s"' % __attr_onmouseover))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678045024
                        __default_4678045024 = _DEFAULT_MARKER

                        # <Substitution 'view/onmousemove' (59:25)> -> __attr_onmousemove
                        __token = 2745
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousemove = _static_4427992992('path', 'view/onmousemove', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousemove is not None):
                            __append((' onmousemove="%s"' % __attr_onmousemove))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678052992
                        __default_4678052992 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseout' (60:23)> -> __attr_onmouseout
                        __token = 2798
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseout = _static_4427992992('path', 'view/onmouseout', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseout is not None):
                            __append((' onmouseout="%s"' % __attr_onmouseout))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678056496
                        __default_4678056496 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeypress' (61:22)> -> __attr_onkeypress
                        __token = 2850
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeypress = _static_4427992992('path', 'view/onkeypress', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeypress is not None):
                            __append((' onkeypress="%s"' % __attr_onkeypress))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678052416
                        __default_4678052416 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeydown' (62:20)> -> __attr_onkeydown
                        __token = 2901
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeydown = _static_4427992992('path', 'view/onkeydown', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeydown is not None):
                            __append((' onkeydown="%s"' % __attr_onkeydown))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678052752
                        __default_4678052752 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeyup' (63:17)> -> __attr_onkeyup
                        __token = 2949
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeyup = _static_4427992992('path', 'view/onkeyup', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeyup is not None):
                            __append((' onkeyup="%s"' % __attr_onkeyup))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678048720
                        __default_4678048720 = _DEFAULT_MARKER

                        # <Substitution 'view/onfocus' (66:14)> -> __attr_onfocus
                        __token = 3091
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onfocus = _static_4427992992('path', 'view/onfocus', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onfocus is not None):
                            __append((' onfocus="%s"' % __attr_onfocus))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678042960
                        __default_4678042960 = _DEFAULT_MARKER

                        # <Substitution 'view/onblur' (67:12)> -> __attr_onblur
                        __token = 3136
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onblur = _static_4427992992('path', 'view/onblur', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onblur is not None):
                            __append((' onblur="%s"' % __attr_onblur))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678056064
                        __default_4678056064 = _DEFAULT_MARKER

                        # <Substitution 'view/onchange' (68:13)> -> __attr_onchange
                        __token = 3182
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onchange = _static_4427992992('path', 'view/onchange', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onchange is not None):
                            __append((' onchange="%s"' % __attr_onchange))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680562432
                        __default_4680562432 = _DEFAULT_MARKER

                        # <Substitution 'view/onselect' (72:9)> -> __attr_onselect
                        __token = 3366
                        try:
                            __zt_tmp = __attrs_4680550288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onselect = _static_4427992992('path', 'view/onselect', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onselect is not None):
                            __append((' onselect="%s"' % __attr_onselect))
                        __append(' />')
                    __append('\n  ')

                    # <Static value=<ast.Dict object at 0x116fba4d0> name=None at 116fba290> -> __attrs_4680557728
                    __attrs_4680557728 = _static_4680557776

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append('<label class="form-check-label"')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680561760
                    __default_4680561760 = _DEFAULT_MARKER

                    # <Substitution 'item/id' (74:29)> -> __attr_for
                    __token = 3479
                    try:
                        __zt_tmp = __attrs_4680557728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_for = _static_4427992992('path', 'item/id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_for = __quote(__attr_for, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_for is not None):
                        __append((' for="%s"' % __attr_for))
                    __append('>\n    ')

                    # <Static value=<ast.Dict object at 0x116fb8f10> name=None at 116fb8fa0> -> __attrs_4680558832
                    __attrs_4680558832 = _static_4680552208

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="label">')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680560224
                    __default_4680560224 = _DEFAULT_MARKER

                    # <Value 'item/label' (75:37)> -> __cache_4680561904
                    __token = 3526
                    try:
                        __zt_tmp = __attrs_4680558832
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4680561904 = _static_4427992992('path', 'item/label', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'item/label' (75:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116fbadd0> -> __condition
                    __expression = __cache_4680561904

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Label')
                    else:
                        __content = __cache_4680561904
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n  </label>\n </div>')
                    ____index_4677695760 -= 1
                    if (____index_4677695760 > 0):
                        __append('\n ')
                if (__backup_item_4681905488 is __marker):
                    del econtext['item']
                else:
                    econtext['item'] = __backup_item_4681905488
                __append('\n')
                __condition = __cache_4678193632
                if __condition:
                    __append('</div>')
            __append('\n')

            # <Static value=<ast.Dict object at 0x116fb9630> name=None at 116fb9690> -> __attrs_4680551440
            __attrs_4680551440 = _static_4680554032

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680549088
            __default_4680549088 = _DEFAULT_MARKER

            # <Substitution 'string:${view/name}-empty-marker' (80:28)> -> __attr_name
            __token = 3662
            try:
                __zt_tmp = __attrs_4680551440
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_4427992992('string', '${view/name}-empty-marker', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', 'field-empty-marker', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))
            __append(' type="hidden" value="1" />\n')
            if (__backup_single_checkbox_4682730800 is __marker):
                del econtext['single_checkbox']
            else:
                econtext['single_checkbox'] = __backup_single_checkbox_4682730800
            if (__backup_items_4678054816 is __marker):
                del econtext['items']
            else:
                econtext['items'] = __backup_items_4678054816
            if (__backup_items_4683178448 is __marker):
                del econtext['items']
            else:
                econtext['items'] = __backup_items_4683178448
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }