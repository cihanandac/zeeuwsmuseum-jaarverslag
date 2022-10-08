# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/z3cform/templates/singlecheckboxbool_input.pt'

__tokens = {139: ('view/items', 4, 23), 173: (' python:list(items', 5, 22), 225: ('x python:len(items) ==', 6, 31), 341: ('python:len(items) > 0', 9, 20), 304: ('single_checkbox', 8, 19), 276: ('view/id', 7, 24), 414: ('items', 11, 24), 447: ('python:single_checkbox and view.id or None', 12, 26), 674: ('item/checked', 16, 24), 716: ('item/id', 17, 28), 754: (' item/nam', 18, 29), 873: ('ss string:form-check-input ${view/kla', 20, 28), 1898: ('        ', 41, 5), 1026: ('title view', 23, 25), 1669: ('          tab', 36, 15), 1621: ('         disa', 35, 16), 1855: ('             ', 40, 11), 1942: ('              ', 42, 10), 942: ('lue item/v', 21, 27), 798: ("d python:view.required and 'required' or No", 19, 32), 984: ('tyle view/', 22, 26), 1067: ('  lang vi', 24, 23), 1110: ('onclick view', 25, 25), 1159: ('dblclick view/o', 26, 27), 1212: ('mousedown view/o', 27, 27), 1264: (' onmouseup vie', 28, 24), 1316: ('onmouseover view', 29, 25), 1370: (' onmousemove vie', 30, 24), 1423: ('   onmouseout v', 31, 22), 1475: ('    onkeypress ', 32, 21), 1526: ('      onkeydow', 33, 19), 1574: ('         onk', 34, 16), 1716: ('            ', 37, 13), 1761: ('           ', 38, 11), 1807: ('             ', 39, 12), 1991: ('             ', 43, 8), 2202: ('not:item/checked', 47, 24), 2248: ('item/id', 48, 28), 2286: (' item/nam', 49, 29), 2405: ('ss string:form-check-input ${view/kla', 51, 28), 3430: ('        ', 72, 5), 2558: ('title view', 54, 25), 3201: ('          tab', 67, 15), 3153: ('         disa', 66, 16), 3387: ('             ', 71, 11), 3474: ('              ', 73, 10), 2474: ('lue item/v', 52, 27), 2330: ("d python:view.required and 'required' or No", 50, 32), 2516: ('tyle view/', 53, 26), 2599: ('  lang vi', 55, 23), 2642: ('onclick view', 56, 25), 2691: ('dblclick view/o', 57, 27), 2744: ('mousedown view/o', 58, 27), 2796: (' onmouseup vie', 59, 24), 2848: ('onmouseover view', 60, 25), 2902: (' onmousemove vie', 61, 24), 2955: ('   onmouseout v', 62, 22), 3007: ('    onkeypress ', 63, 21), 3058: ('      onkeydow', 64, 19), 3106: ('         onk', 65, 16), 3248: ('            ', 68, 13), 3293: ('           ', 69, 11), 3339: ('             ', 70, 12), 3523: ('             ', 74, 8), 3637: ('item/id', 76, 29), 3670: ('item/label', 77, 23), 3785: ('item/required', 80, 25), 3923: ('item/description', 83, 48), 4061: ('string:${view/name}-empty-marker', 89, 28)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4485009072 = {'name': 'field-empty-marker', 'type': 'hidden', 'value': '1', }
_static_4485017808 = {'class': 'form-text', }
_static_4485014208 = {'class': 'required horizontal', 'title': 'Required', }
_static_4418309904 = {}
_static_4485158784 = {'for': '', 'class': 'form-check-label', }
_static_4481063600 = {'id': '', 'name': '', 'class': '', 'alt': '', 'title': '', 'tabindex': '', 'disabled': '', 'readonly': '', 'accesskey': '', 'value': '', 'type': 'checkbox', 'required': "python:view.required and 'required' or None", 'style': 'view/style', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'onselect': 'view/onselect', }
_static_4485461232 = {'type': 'checkbox', 'id': '', 'name': '', 'class': '', 'alt': '', 'title': '', 'tabindex': '', 'disabled': '', 'readonly': '', 'accesskey': '', 'value': '', 'checked': 'checked', 'required': "python:view.required and 'required' or None", 'style': 'view/style', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'onselect': 'view/onselect', }
_static_4485452304 = {'class': 'form-check', 'id': 'python:single_checkbox and view.id or None', }
_static_4476035632 = {'id': 'view/id', }
_static_4417565216 = __C2ZContextWrapper
_static_4417553984 = __compile_zt_expr
_static_4476029344 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x10acac9a0> name=None at 10acacf70> -> __attrs_4476030160
            __attrs_4476030160 = _static_4476029344
            __backup_items_4480125056 = get('items', __marker)

            # <Value 'view/items' (4:23)> -> __value
            __token = 139
            try:
                __zt_tmp = __attrs_4476030160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4417553984('path', 'view/items', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            econtext['items'] = __value
            __backup_items_4480371056 = get('items', __marker)

            # <Value 'python:list(items)' (5:22)> -> __value
            __token = 173
            try:
                __zt_tmp = __attrs_4476030160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4417553984('python', 'list(items)', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            econtext['items'] = __value
            __backup_single_checkbox_4485611824 = get('single_checkbox', __marker)

            # <Value 'python:len(items) == 1' (6:31)> -> __value
            __token = 225
            try:
                __zt_tmp = __attrs_4476030160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4417553984('python', 'len(items) == 1', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            econtext['single_checkbox'] = __value
            __append('\n')

            # <Static value=<ast.Dict object at 0x10acae230> name=None at 10acac910> -> __attrs_4485454848
            __attrs_4485454848 = _static_4476035632

            # <Value 'python:len(items) > 0' (9:20)> -> __condition
            __token = 341
            try:
                __zt_tmp = __attrs_4485454848
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4417553984('python', 'len(items) > 0', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            if __condition:

                # <Negate value=<Value 'single_checkbox' (8:19)> at 10b5a8d60> -> __cache_4485451104

                # <Value 'single_checkbox' (8:19)> -> __cache_4485451104
                __token = 304
                try:
                    __zt_tmp = __attrs_4485454848
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4485451104 = _static_4417553984('path', 'single_checkbox', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                __cache_4485451104 = not __cache_4485451104
                __condition = __cache_4485451104
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')

                    # <Symbol value=<DEFAULT> at 107619600> -> __default_4485455616
                    __default_4485455616 = _DEFAULT_MARKER

                    # <Substitution 'view/id' (7:24)> -> __attr_id
                    __token = 276
                    try:
                        __zt_tmp = __attrs_4485454848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_4417553984('path', 'view/id', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))
                    __append('>')
                __append('\n ')

                # <Static value=<ast.Dict object at 0x10b5a9210> name=None at 10b5a9690> -> __attrs_4485453216
                __attrs_4485453216 = _static_4485452304
                __backup_item_4480574576 = get('item', __marker)

                # <Value 'items' (11:24)> -> __iterator
                __token = 414
                try:
                    __zt_tmp = __attrs_4485453216
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4417553984('path', 'items', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                (__iterator, ____index_4485457152, ) = getname('repeat')('item', __iterator)
                econtext['item'] = None
                for __item in __iterator:
                    econtext['item'] = __item

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-check"')

                    # <Symbol value=<DEFAULT> at 107619600> -> __default_4485454464
                    __default_4485454464 = _DEFAULT_MARKER

                    # <Substitution 'python:single_checkbox and view.id or None' (12:26)> -> __attr_id
                    __token = 447
                    try:
                        __zt_tmp = __attrs_4485453216
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_4417553984('python', 'single_checkbox and view.id or None', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))
                    __append('>\n  ')

                    # <Static value=<ast.Dict object at 0x10b5ab4f0> name=None at 10b5ab7f0> -> __attrs_4476939248
                    __attrs_4476939248 = _static_4485461232

                    # <Value 'item/checked' (16:24)> -> __condition
                    __token = 674
                    try:
                        __zt_tmp = __attrs_4476939248
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4417553984('path', 'item/checked', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="checkbox"')

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485449856
                        __default_4485449856 = _DEFAULT_MARKER

                        # <Substitution 'item/id' (17:28)> -> __attr_id
                        __token = 716
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_4417553984('path', 'item/id', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((' id="%s"' % __attr_id))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485463680
                        __default_4485463680 = _DEFAULT_MARKER

                        # <Substitution 'item/name' (18:29)> -> __attr_name
                        __token = 754
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_4417553984('path', 'item/name', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485462864
                        __default_4485462864 = _DEFAULT_MARKER

                        # <Substitution 'string:form-check-input ${view/klass}' (20:28)> -> __attr_class
                        __token = 873
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_4417553984('string', 'form-check-input ${view/klass}', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485461904
                        __default_4485461904 = _DEFAULT_MARKER

                        # <Substitution 'view/alt' (41:5)> -> __attr_alt
                        __token = 1898
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_alt = _static_4417553984('path', 'view/alt', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_alt is not None):
                            __append((' alt="%s"' % __attr_alt))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485457008
                        __default_4485457008 = _DEFAULT_MARKER

                        # <Substitution 'view/title' (23:25)> -> __attr_title
                        __token = 1026
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_4417553984('path', 'view/title', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485458016
                        __default_4485458016 = _DEFAULT_MARKER

                        # <Substitution 'view/tabindex' (36:15)> -> __attr_tabindex
                        __token = 1669
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_tabindex = _static_4417553984('path', 'view/tabindex', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_tabindex is not None):
                            __append((' tabindex="%s"' % __attr_tabindex))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485462048
                        __default_4485462048 = _DEFAULT_MARKER

                        # <Boolean 'view/disabled' (35:16)> -> __attr_disabled
                        __token = 1621
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_disabled = _static_4417553984('path', 'view/disabled', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        if (__attr_disabled is _DEFAULT_MARKER):
                            __attr_disabled = ''
                        else:
                            if __attr_disabled:
                                __attr_disabled = 'disabled'
                            else:
                                __attr_disabled = None
                        if (__attr_disabled is not None):
                            __append((' disabled="%s"' % __attr_disabled))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485461136
                        __default_4485461136 = _DEFAULT_MARKER

                        # <Boolean 'view/readonly' (40:11)> -> __attr_readonly
                        __token = 1855
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_readonly = _static_4417553984('path', 'view/readonly', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        if (__attr_readonly is _DEFAULT_MARKER):
                            __attr_readonly = ''
                        else:
                            if __attr_readonly:
                                __attr_readonly = 'readonly'
                            else:
                                __attr_readonly = None
                        if (__attr_readonly is not None):
                            __append((' readonly="%s"' % __attr_readonly))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485458976
                        __default_4485458976 = _DEFAULT_MARKER

                        # <Substitution 'view/accesskey' (42:10)> -> __attr_accesskey
                        __token = 1942
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_accesskey = _static_4417553984('path', 'view/accesskey', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_accesskey is not None):
                            __append((' accesskey="%s"' % __attr_accesskey))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485456000
                        __default_4485456000 = _DEFAULT_MARKER

                        # <Substitution 'item/value' (21:27)> -> __attr_value
                        __token = 942
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_4417553984('path', 'item/value', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' checked="checked"')

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485459552
                        __default_4485459552 = _DEFAULT_MARKER

                        # <Substitution "python:view.required and 'required' or None" (19:32)> -> __attr_required
                        __token = 798
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_required = _static_4417553984('python', "view.required and 'required' or None", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_required = __quote(__attr_required, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_required is not None):
                            __append((' required="%s"' % __attr_required))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485453744
                        __default_4485453744 = _DEFAULT_MARKER

                        # <Substitution 'view/style' (22:26)> -> __attr_style
                        __token = 984
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_style = _static_4417553984('path', 'view/style', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_style is not None):
                            __append((' style="%s"' % __attr_style))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485455760
                        __default_4485455760 = _DEFAULT_MARKER

                        # <Substitution 'view/lang' (24:23)> -> __attr_lang
                        __token = 1067
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_lang = _static_4417553984('path', 'view/lang', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_lang is not None):
                            __append((' lang="%s"' % __attr_lang))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485452832
                        __default_4485452832 = _DEFAULT_MARKER

                        # <Substitution 'view/onclick' (25:25)> -> __attr_onclick
                        __token = 1110
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onclick = _static_4417553984('path', 'view/onclick', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onclick is not None):
                            __append((' onclick="%s"' % __attr_onclick))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485448080
                        __default_4485448080 = _DEFAULT_MARKER

                        # <Substitution 'view/ondblclick' (26:27)> -> __attr_ondblclick
                        __token = 1159
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_ondblclick = _static_4417553984('path', 'view/ondblclick', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_ondblclick is not None):
                            __append((' ondblclick="%s"' % __attr_ondblclick))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485449136
                        __default_4485449136 = _DEFAULT_MARKER

                        # <Substitution 'view/onmousedown' (27:27)> -> __attr_onmousedown
                        __token = 1212
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousedown = _static_4417553984('path', 'view/onmousedown', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousedown is not None):
                            __append((' onmousedown="%s"' % __attr_onmousedown))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485449232
                        __default_4485449232 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseup' (28:24)> -> __attr_onmouseup
                        __token = 1264
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseup = _static_4417553984('path', 'view/onmouseup', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseup is not None):
                            __append((' onmouseup="%s"' % __attr_onmouseup))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485448944
                        __default_4485448944 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseover' (29:25)> -> __attr_onmouseover
                        __token = 1316
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseover = _static_4417553984('path', 'view/onmouseover', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseover is not None):
                            __append((' onmouseover="%s"' % __attr_onmouseover))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485449616
                        __default_4485449616 = _DEFAULT_MARKER

                        # <Substitution 'view/onmousemove' (30:24)> -> __attr_onmousemove
                        __token = 1370
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousemove = _static_4417553984('path', 'view/onmousemove', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousemove is not None):
                            __append((' onmousemove="%s"' % __attr_onmousemove))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485450816
                        __default_4485450816 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseout' (31:22)> -> __attr_onmouseout
                        __token = 1423
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseout = _static_4417553984('path', 'view/onmouseout', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseout is not None):
                            __append((' onmouseout="%s"' % __attr_onmouseout))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485450384
                        __default_4485450384 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeypress' (32:21)> -> __attr_onkeypress
                        __token = 1475
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeypress = _static_4417553984('path', 'view/onkeypress', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeypress is not None):
                            __append((' onkeypress="%s"' % __attr_onkeypress))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485448848
                        __default_4485448848 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeydown' (33:19)> -> __attr_onkeydown
                        __token = 1526
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeydown = _static_4417553984('path', 'view/onkeydown', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeydown is not None):
                            __append((' onkeydown="%s"' % __attr_onkeydown))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485450192
                        __default_4485450192 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeyup' (34:16)> -> __attr_onkeyup
                        __token = 1574
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeyup = _static_4417553984('path', 'view/onkeyup', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeyup is not None):
                            __append((' onkeyup="%s"' % __attr_onkeyup))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4481427120
                        __default_4481427120 = _DEFAULT_MARKER

                        # <Substitution 'view/onfocus' (37:13)> -> __attr_onfocus
                        __token = 1716
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onfocus = _static_4417553984('path', 'view/onfocus', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onfocus is not None):
                            __append((' onfocus="%s"' % __attr_onfocus))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4481430192
                        __default_4481430192 = _DEFAULT_MARKER

                        # <Substitution 'view/onblur' (38:11)> -> __attr_onblur
                        __token = 1761
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onblur = _static_4417553984('path', 'view/onblur', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onblur is not None):
                            __append((' onblur="%s"' % __attr_onblur))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4481427312
                        __default_4481427312 = _DEFAULT_MARKER

                        # <Substitution 'view/onchange' (39:12)> -> __attr_onchange
                        __token = 1807
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onchange = _static_4417553984('path', 'view/onchange', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onchange is not None):
                            __append((' onchange="%s"' % __attr_onchange))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4481418336
                        __default_4481418336 = _DEFAULT_MARKER

                        # <Substitution 'view/onselect' (43:8)> -> __attr_onselect
                        __token = 1991
                        try:
                            __zt_tmp = __attrs_4476939248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onselect = _static_4417553984('path', 'view/onselect', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onselect is not None):
                            __append((' onselect="%s"' % __attr_onselect))
                        __append(' />')

                    # <Static value=<ast.Dict object at 0x10b179ab0> name=None at 10b178220> -> __attrs_4485154896
                    __attrs_4485154896 = _static_4481063600

                    # <Value 'not:item/checked' (47:24)> -> __condition
                    __token = 2202
                    try:
                        __zt_tmp = __attrs_4485154896
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4417553984('not', 'item/checked', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input')

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4476932144
                        __default_4476932144 = _DEFAULT_MARKER

                        # <Substitution 'item/id' (48:28)> -> __attr_id
                        __token = 2248
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_4417553984('path', 'item/id', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((' id="%s"' % __attr_id))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485158352
                        __default_4485158352 = _DEFAULT_MARKER

                        # <Substitution 'item/name' (49:29)> -> __attr_name
                        __token = 2286
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_4417553984('path', 'item/name', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485161280
                        __default_4485161280 = _DEFAULT_MARKER

                        # <Substitution 'string:form-check-input ${view/klass}' (51:28)> -> __attr_class
                        __token = 2405
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_4417553984('string', 'form-check-input ${view/klass}', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485164688
                        __default_4485164688 = _DEFAULT_MARKER

                        # <Substitution 'view/alt' (72:5)> -> __attr_alt
                        __token = 3430
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_alt = _static_4417553984('path', 'view/alt', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_alt is not None):
                            __append((' alt="%s"' % __attr_alt))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485156000
                        __default_4485156000 = _DEFAULT_MARKER

                        # <Substitution 'view/title' (54:25)> -> __attr_title
                        __token = 2558
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_4417553984('path', 'view/title', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485154512
                        __default_4485154512 = _DEFAULT_MARKER

                        # <Substitution 'view/tabindex' (67:15)> -> __attr_tabindex
                        __token = 3201
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_tabindex = _static_4417553984('path', 'view/tabindex', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_tabindex is not None):
                            __append((' tabindex="%s"' % __attr_tabindex))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485162192
                        __default_4485162192 = _DEFAULT_MARKER

                        # <Boolean 'view/disabled' (66:16)> -> __attr_disabled
                        __token = 3153
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_disabled = _static_4417553984('path', 'view/disabled', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        if (__attr_disabled is _DEFAULT_MARKER):
                            __attr_disabled = ''
                        else:
                            if __attr_disabled:
                                __attr_disabled = 'disabled'
                            else:
                                __attr_disabled = None
                        if (__attr_disabled is not None):
                            __append((' disabled="%s"' % __attr_disabled))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485161808
                        __default_4485161808 = _DEFAULT_MARKER

                        # <Boolean 'view/readonly' (71:11)> -> __attr_readonly
                        __token = 3387
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_readonly = _static_4417553984('path', 'view/readonly', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        if (__attr_readonly is _DEFAULT_MARKER):
                            __attr_readonly = ''
                        else:
                            if __attr_readonly:
                                __attr_readonly = 'readonly'
                            else:
                                __attr_readonly = None
                        if (__attr_readonly is not None):
                            __append((' readonly="%s"' % __attr_readonly))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485154464
                        __default_4485154464 = _DEFAULT_MARKER

                        # <Substitution 'view/accesskey' (73:10)> -> __attr_accesskey
                        __token = 3474
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_accesskey = _static_4417553984('path', 'view/accesskey', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_accesskey is not None):
                            __append((' accesskey="%s"' % __attr_accesskey))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485155136
                        __default_4485155136 = _DEFAULT_MARKER

                        # <Substitution 'item/value' (52:27)> -> __attr_value
                        __token = 2474
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_4417553984('path', 'item/value', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' type="checkbox"')

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485164496
                        __default_4485164496 = _DEFAULT_MARKER

                        # <Substitution "python:view.required and 'required' or None" (50:32)> -> __attr_required
                        __token = 2330
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_required = _static_4417553984('python', "view.required and 'required' or None", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_required = __quote(__attr_required, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_required is not None):
                            __append((' required="%s"' % __attr_required))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485158736
                        __default_4485158736 = _DEFAULT_MARKER

                        # <Substitution 'view/style' (53:26)> -> __attr_style
                        __token = 2516
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_style = _static_4417553984('path', 'view/style', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_style is not None):
                            __append((' style="%s"' % __attr_style))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485153936
                        __default_4485153936 = _DEFAULT_MARKER

                        # <Substitution 'view/lang' (55:23)> -> __attr_lang
                        __token = 2599
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_lang = _static_4417553984('path', 'view/lang', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_lang is not None):
                            __append((' lang="%s"' % __attr_lang))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485158832
                        __default_4485158832 = _DEFAULT_MARKER

                        # <Substitution 'view/onclick' (56:25)> -> __attr_onclick
                        __token = 2642
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onclick = _static_4417553984('path', 'view/onclick', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onclick is not None):
                            __append((' onclick="%s"' % __attr_onclick))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485156048
                        __default_4485156048 = _DEFAULT_MARKER

                        # <Substitution 'view/ondblclick' (57:27)> -> __attr_ondblclick
                        __token = 2691
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_ondblclick = _static_4417553984('path', 'view/ondblclick', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_ondblclick is not None):
                            __append((' ondblclick="%s"' % __attr_ondblclick))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485154800
                        __default_4485154800 = _DEFAULT_MARKER

                        # <Substitution 'view/onmousedown' (58:27)> -> __attr_onmousedown
                        __token = 2744
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousedown = _static_4417553984('path', 'view/onmousedown', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousedown is not None):
                            __append((' onmousedown="%s"' % __attr_onmousedown))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485156960
                        __default_4485156960 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseup' (59:24)> -> __attr_onmouseup
                        __token = 2796
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseup = _static_4417553984('path', 'view/onmouseup', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseup is not None):
                            __append((' onmouseup="%s"' % __attr_onmouseup))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485159888
                        __default_4485159888 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseover' (60:25)> -> __attr_onmouseover
                        __token = 2848
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseover = _static_4417553984('path', 'view/onmouseover', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseover is not None):
                            __append((' onmouseover="%s"' % __attr_onmouseover))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485160320
                        __default_4485160320 = _DEFAULT_MARKER

                        # <Substitution 'view/onmousemove' (61:24)> -> __attr_onmousemove
                        __token = 2902
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousemove = _static_4417553984('path', 'view/onmousemove', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousemove is not None):
                            __append((' onmousemove="%s"' % __attr_onmousemove))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485153888
                        __default_4485153888 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseout' (62:22)> -> __attr_onmouseout
                        __token = 2955
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseout = _static_4417553984('path', 'view/onmouseout', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseout is not None):
                            __append((' onmouseout="%s"' % __attr_onmouseout))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485152832
                        __default_4485152832 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeypress' (63:21)> -> __attr_onkeypress
                        __token = 3007
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeypress = _static_4417553984('path', 'view/onkeypress', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeypress is not None):
                            __append((' onkeypress="%s"' % __attr_onkeypress))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485156768
                        __default_4485156768 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeydown' (64:19)> -> __attr_onkeydown
                        __token = 3058
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeydown = _static_4417553984('path', 'view/onkeydown', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeydown is not None):
                            __append((' onkeydown="%s"' % __attr_onkeydown))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485159840
                        __default_4485159840 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeyup' (65:16)> -> __attr_onkeyup
                        __token = 3106
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeyup = _static_4417553984('path', 'view/onkeyup', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeyup is not None):
                            __append((' onkeyup="%s"' % __attr_onkeyup))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485157632
                        __default_4485157632 = _DEFAULT_MARKER

                        # <Substitution 'view/onfocus' (68:13)> -> __attr_onfocus
                        __token = 3248
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onfocus = _static_4417553984('path', 'view/onfocus', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onfocus is not None):
                            __append((' onfocus="%s"' % __attr_onfocus))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485154176
                        __default_4485154176 = _DEFAULT_MARKER

                        # <Substitution 'view/onblur' (69:11)> -> __attr_onblur
                        __token = 3293
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onblur = _static_4417553984('path', 'view/onblur', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onblur is not None):
                            __append((' onblur="%s"' % __attr_onblur))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485155232
                        __default_4485155232 = _DEFAULT_MARKER

                        # <Substitution 'view/onchange' (70:12)> -> __attr_onchange
                        __token = 3339
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onchange = _static_4417553984('path', 'view/onchange', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onchange is not None):
                            __append((' onchange="%s"' % __attr_onchange))

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485152928
                        __default_4485152928 = _DEFAULT_MARKER

                        # <Substitution 'view/onselect' (74:8)> -> __attr_onselect
                        __token = 3523
                        try:
                            __zt_tmp = __attrs_4485154896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onselect = _static_4417553984('path', 'view/onselect', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onselect is not None):
                            __append((' onselect="%s"' % __attr_onselect))
                        __append(' />')
                    __append('\n  ')

                    # <Static value=<ast.Dict object at 0x10b561780> name=None at 10b5630a0> -> __attrs_4485166128
                    __attrs_4485166128 = _static_4485158784

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append('<label')

                    # <Symbol value=<DEFAULT> at 107619600> -> __default_4485156480
                    __default_4485156480 = _DEFAULT_MARKER

                    # <Substitution 'item/id' (76:29)> -> __attr_for
                    __token = 3637
                    try:
                        __zt_tmp = __attrs_4485166128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_for = _static_4417553984('path', 'item/id', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    __attr_for = __quote(__attr_for, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_for is not None):
                        __append((' for="%s"' % __attr_for))
                    __append(' class="form-check-label">\n    ')

                    # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4485019632
                    __attrs_4485019632 = _static_4418309904

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')

                    # <Symbol value=<DEFAULT> at 107619600> -> __default_4485167808
                    __default_4485167808 = _DEFAULT_MARKER

                    # <Value 'item/label' (77:23)> -> __cache_4485167472
                    __token = 3670
                    try:
                        __zt_tmp = __attrs_4485019632
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4485167472 = _static_4417553984('path', 'item/label', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))

                    # <BinOp left=<Value 'item/label' (77:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107619600> at 10b563a90> -> __condition
                    __expression = __cache_4485167472

                    # <Symbol value=<DEFAULT> at 107619600> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Label')
                    else:
                        __content = __cache_4485167472
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n    ')

                    # <Static value=<ast.Dict object at 0x10b53e2c0> name=None at 10b53c8b0> -> __attrs_4485014832
                    __attrs_4485014832 = _static_4485014208

                    # <Value 'item/required' (80:25)> -> __condition
                    __token = 3785
                    try:
                        __zt_tmp = __attrs_4485014832
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4417553984('path', 'item/required', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="required horizontal"')

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485020784
                        __default_4485020784 = _DEFAULT_MARKER

                        # <Translate msgid='title_required' node=<ast.Constant object at 0x10b53fbe0> at 10b53f250> -> __attr_title
                        __attr_title = 'Required'
                        __attr_title = translate('title_required', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))
                        __append('>&nbsp;</span>')
                    __append('\n  </label>\n  ')

                    # <Static value=<ast.Dict object at 0x10b53f0d0> name=None at 10b53eec0> -> __attrs_4485014112
                    __attrs_4485014112 = _static_4485017808

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-text">')

                    # <Symbol value=<DEFAULT> at 107619600> -> __default_4485014400
                    __default_4485014400 = _DEFAULT_MARKER

                    # <Value 'item/description' (83:48)> -> __cache_4485018000
                    __token = 3923
                    try:
                        __zt_tmp = __attrs_4485014112
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4485018000 = _static_4417553984('path', 'item/description', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))

                    # <BinOp left=<Value 'item/description' (83:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107619600> at 10b53d720> -> __condition
                    __expression = __cache_4485018000

                    # <Symbol value=<DEFAULT> at 107619600> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Description')
                    else:
                        __content = __cache_4485018000
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n </div>')
                    ____index_4485457152 -= 1
                    if (____index_4485457152 > 0):
                        __append('\n ')
                if (__backup_item_4480574576 is __marker):
                    del econtext['item']
                else:
                    econtext['item'] = __backup_item_4480574576
                __append('\n\n')
                __condition = __cache_4485451104
                if __condition:
                    __append('</div>')
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x10b53ceb0> name=None at 10b53da20> -> __attrs_4485016464
            __attrs_4485016464 = _static_4485009072

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input')

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485009648
            __default_4485009648 = _DEFAULT_MARKER

            # <Substitution 'string:${view/name}-empty-marker' (89:28)> -> __attr_name
            __token = 4061
            try:
                __zt_tmp = __attrs_4485016464
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_4417553984('string', '${view/name}-empty-marker', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', 'field-empty-marker', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))
            __append(' type="hidden" value="1" />\n')
            if (__backup_single_checkbox_4485611824 is __marker):
                del econtext['single_checkbox']
            else:
                econtext['single_checkbox'] = __backup_single_checkbox_4485611824
            if (__backup_items_4480371056 is __marker):
                del econtext['items']
            else:
                econtext['items'] = __backup_items_4480371056
            if (__backup_items_4480125056 is __marker):
                del econtext['items']
            else:
                econtext['items'] = __backup_items_4480125056
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }