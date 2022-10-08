# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/z3cform/templates/text_input.pt'

__tokens = {329: ('view/id', 7, 30), 369: (' view/nam', 8, 31), 492: ("ss python:'form-control {0}{1}'.format(view.klass, view.error and ' is-invalid' or ", 10, 30), 653: ('itle view/', 12, 28), 696: (' lang vie', 13, 26), 1316: ('         disa', 25, 18), 1560: ('             ', 30, 13), 1605: ('        ', 31, 7), 1366: ('          tab', 26, 17), 1651: ('              ', 32, 12), 1748: ('         ', 34, 5), 1795: ('              ', 35, 9), 609: ('yle view/s', 11, 29), 1269: ('          ', 24, 16), 415: ("d python:view.required and 'required' or No", 9, 34), 741: ('nclick view/', 14, 28), 792: ('blclick view/on', 15, 30), 847: ('ousedown view/on', 16, 30), 901: ('onmouseup view', 17, 27), 955: ('nmouseover view/', 18, 28), 1011: ('onmousemove view', 19, 27), 1066: ('  onmouseout vi', 20, 25), 1120: ('   onkeypress v', 21, 24), 1173: ('     onkeydown', 22, 22), 1223: ('        onke', 23, 19), 1415: ('            ', 27, 15), 1462: ('           ', 28, 13), 1510: ('             ', 29, 14), 1702: ('             ', 33, 10), 1849: ('                ', 36, 10), 1908: ('               auto', 37, 12)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4459175296 = __C2ZContextWrapper
_static_4459168576 = __compile_zt_expr
_static_4709737776 = {'id': '', 'name': '', 'class': '', 'title': '', 'lang': '', 'disabled': '', 'readonly': '', 'alt': '', 'tabindex': '', 'accesskey': '', 'size': '', 'maxlength': '', 'style': '', 'value': '', 'type': 'text', 'required': "python:view.required and 'required' or None", 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'onselect': 'view/onselect', 'placeholder': 'view/placeholder', 'autocapitalize': 'view/autocapitalize', }
_static_4709740176 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x118b8ee90> name=None at 118b8ffd0> -> __attrs_4709741568
            __attrs_4709741568 = _static_4709740176
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x118b8e530> name=None at 118b8e4d0> -> __attrs_4708442672
            __attrs_4708442672 = _static_4709737776

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input')

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709742192
            __default_4709742192 = _DEFAULT_MARKER

            # <Substitution 'view/id' (7:30)> -> __attr_id
            __token = 329
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_4459168576('path', 'view/id', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709743248
            __default_4709743248 = _DEFAULT_MARKER

            # <Substitution 'view/name' (8:31)> -> __attr_name
            __token = 369
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_4459168576('path', 'view/name', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709735616
            __default_4709735616 = _DEFAULT_MARKER

            # <Substitution "python:'form-control {0}{1}'.format(view.klass, view.error and ' is-invalid' or '')" (10:30)> -> __attr_class
            __token = 492
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4459168576('python', "'form-control {0}{1}'.format(view.klass, view.error and ' is-invalid' or '')", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709735712
            __default_4709735712 = _DEFAULT_MARKER

            # <Substitution 'view/title' (12:28)> -> __attr_title
            __token = 653
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_4459168576('path', 'view/title', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709742624
            __default_4709742624 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (13:26)> -> __attr_lang
            __token = 696
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_4459168576('path', 'view/lang', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709744208
            __default_4709744208 = _DEFAULT_MARKER

            # <Boolean 'view/disabled' (25:18)> -> __attr_disabled
            __token = 1316
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_disabled = _static_4459168576('path', 'view/disabled', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            if (__attr_disabled is _DEFAULT_MARKER):
                __attr_disabled = ''
            else:
                if __attr_disabled:
                    __attr_disabled = 'disabled'
                else:
                    __attr_disabled = None
            if (__attr_disabled is not None):
                __append((' disabled="%s"' % __attr_disabled))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709731536
            __default_4709731536 = _DEFAULT_MARKER

            # <Boolean 'view/readonly' (30:13)> -> __attr_readonly
            __token = 1560
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_readonly = _static_4459168576('path', 'view/readonly', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            if (__attr_readonly is _DEFAULT_MARKER):
                __attr_readonly = ''
            else:
                if __attr_readonly:
                    __attr_readonly = 'readonly'
                else:
                    __attr_readonly = None
            if (__attr_readonly is not None):
                __append((' readonly="%s"' % __attr_readonly))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708434080
            __default_4708434080 = _DEFAULT_MARKER

            # <Substitution 'view/alt' (31:7)> -> __attr_alt
            __token = 1605
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_alt = _static_4459168576('path', 'view/alt', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_alt is not None):
                __append((' alt="%s"' % __attr_alt))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708436384
            __default_4708436384 = _DEFAULT_MARKER

            # <Substitution 'view/tabindex' (26:17)> -> __attr_tabindex
            __token = 1366
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_tabindex = _static_4459168576('path', 'view/tabindex', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_tabindex is not None):
                __append((' tabindex="%s"' % __attr_tabindex))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708443056
            __default_4708443056 = _DEFAULT_MARKER

            # <Substitution 'view/accesskey' (32:12)> -> __attr_accesskey
            __token = 1651
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_accesskey = _static_4459168576('path', 'view/accesskey', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_accesskey is not None):
                __append((' accesskey="%s"' % __attr_accesskey))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708444448
            __default_4708444448 = _DEFAULT_MARKER

            # <Substitution 'view/size' (34:5)> -> __attr_size
            __token = 1748
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_size = _static_4459168576('path', 'view/size', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_size = __quote(__attr_size, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_size is not None):
                __append((' size="%s"' % __attr_size))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708437680
            __default_4708437680 = _DEFAULT_MARKER

            # <Substitution 'view/maxlength' (35:9)> -> __attr_maxlength
            __token = 1795
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_maxlength = _static_4459168576('path', 'view/maxlength', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_maxlength = __quote(__attr_maxlength, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_maxlength is not None):
                __append((' maxlength="%s"' % __attr_maxlength))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708434704
            __default_4708434704 = _DEFAULT_MARKER

            # <Substitution 'view/style' (11:29)> -> __attr_style
            __token = 609
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_4459168576('path', 'view/style', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708449344
            __default_4708449344 = _DEFAULT_MARKER

            # <Substitution 'view/value' (24:16)> -> __attr_value
            __token = 1269
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_4459168576('path', 'view/value', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' type="text"')

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708440128
            __default_4708440128 = _DEFAULT_MARKER

            # <Substitution "python:view.required and 'required' or None" (9:34)> -> __attr_required
            __token = 415
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_required = _static_4459168576('python', "view.required and 'required' or None", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_required = __quote(__attr_required, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_required is not None):
                __append((' required="%s"' % __attr_required))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708441232
            __default_4708441232 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (14:28)> -> __attr_onclick
            __token = 741
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_4459168576('path', 'view/onclick', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708443536
            __default_4708443536 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (15:30)> -> __attr_ondblclick
            __token = 792
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_4459168576('path', 'view/ondblclick', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708448768
            __default_4708448768 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (16:30)> -> __attr_onmousedown
            __token = 847
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_4459168576('path', 'view/onmousedown', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708448672
            __default_4708448672 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (17:27)> -> __attr_onmouseup
            __token = 901
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_4459168576('path', 'view/onmouseup', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708445024
            __default_4708445024 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (18:28)> -> __attr_onmouseover
            __token = 955
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_4459168576('path', 'view/onmouseover', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708442192
            __default_4708442192 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (19:27)> -> __attr_onmousemove
            __token = 1011
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_4459168576('path', 'view/onmousemove', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708445072
            __default_4708445072 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (20:25)> -> __attr_onmouseout
            __token = 1066
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_4459168576('path', 'view/onmouseout', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708442288
            __default_4708442288 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (21:24)> -> __attr_onkeypress
            __token = 1120
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_4459168576('path', 'view/onkeypress', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708441616
            __default_4708441616 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (22:22)> -> __attr_onkeydown
            __token = 1173
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_4459168576('path', 'view/onkeydown', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708447808
            __default_4708447808 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (23:19)> -> __attr_onkeyup
            __token = 1223
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_4459168576('path', 'view/onkeyup', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708436096
            __default_4708436096 = _DEFAULT_MARKER

            # <Substitution 'view/onfocus' (27:15)> -> __attr_onfocus
            __token = 1415
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_4459168576('path', 'view/onfocus', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708444016
            __default_4708444016 = _DEFAULT_MARKER

            # <Substitution 'view/onblur' (28:13)> -> __attr_onblur
            __token = 1462
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_4459168576('path', 'view/onblur', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708440368
            __default_4708440368 = _DEFAULT_MARKER

            # <Substitution 'view/onchange' (29:14)> -> __attr_onchange
            __token = 1510
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_4459168576('path', 'view/onchange', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((' onchange="%s"' % __attr_onchange))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708439792
            __default_4708439792 = _DEFAULT_MARKER

            # <Substitution 'view/onselect' (33:10)> -> __attr_onselect
            __token = 1702
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onselect = _static_4459168576('path', 'view/onselect', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onselect is not None):
                __append((' onselect="%s"' % __attr_onselect))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708439408
            __default_4708439408 = _DEFAULT_MARKER

            # <Substitution 'view/placeholder' (36:10)> -> __attr_placeholder
            __token = 1849
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_placeholder = _static_4459168576('path', 'view/placeholder', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_placeholder = __quote(__attr_placeholder, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_placeholder is not None):
                __append((' placeholder="%s"' % __attr_placeholder))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708439552
            __default_4708439552 = _DEFAULT_MARKER

            # <Substitution 'view/autocapitalize' (37:12)> -> __attr_autocapitalize
            __token = 1908
            try:
                __zt_tmp = __attrs_4708442672
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_autocapitalize = _static_4459168576('path', 'view/autocapitalize', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_autocapitalize = __quote(__attr_autocapitalize, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_autocapitalize is not None):
                __append((' autocapitalize="%s"' % __attr_autocapitalize))
            __append(' />\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }