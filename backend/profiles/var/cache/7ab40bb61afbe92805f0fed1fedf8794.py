# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/z3cform/templates/submit_input.pt'

__tokens = {172: ("python:'btn-secondary ' if not 'btn-' in view.klass else ''", 5, 31), 260: ('view/id', 6, 27), 297: (' view/nam', 7, 28), 337: ('s string:btn ${bsFallback}${view/klas', 8, 28), 405: ('ue view/va', 9, 27), 446: ('yle view/s', 10, 26), 486: ('lang view', 11, 24), 528: ('click view/o', 12, 26), 576: ('lclick view/ond', 13, 28), 628: ('usedown view/onm', 14, 28), 679: ('nmouseup view/', 15, 25), 730: ('mouseover view/o', 16, 26), 783: ('nmousemove view/', 17, 25), 835: (' onmouseout vie', 18, 23), 886: ('  onkeypress vi', 19, 22), 936: ('    onkeydown ', 20, 20), 983: ('       onkey', 21, 17), 1029: ('       disabl', 22, 17), 1076: ('        tabin', 23, 16), 1122: ('          on', 24, 14), 1166: ('           ', 25, 12), 1211: ('           on', 26, 13), 1258: ('            r', 27, 12), 1300: ('        ', 28, 6), 1343: ('             a', 29, 11), 1391: ('             ', 30, 9), 1444: ('          formnovalidate python:view.ignoreReq', 31, 14), 1538: ('view/value', 32, 21)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4459175296 = __C2ZContextWrapper
_static_4459168576 = __compile_zt_expr
_static_4710276192 = {'type': 'submit', 'id': 'view/id', 'name': 'view/name', 'class': 'string:btn ${bsFallback}${view/klass}', 'value': 'view/value', 'style': 'view/style', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'disabled': 'view/disabled', 'tabindex': 'view/tabindex', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'readonly': 'view/readonly', 'alt': 'view/alt', 'accesskey': 'view/accesskey', 'onselect': 'view/onselect', 'formnovalidate': 'python:view.ignoreRequiredOnValidation or None', }
_static_4710280800 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x118c12e60> name=None at 118c12590> -> __attrs_4710280512
            __attrs_4710280512 = _static_4710280800
            __append('\n')

            # <Static value=<ast.Dict object at 0x118c11c60> name=None at 118c12fb0> -> __attrs_4710010256
            __attrs_4710010256 = _static_4710276192
            __backup_bsFallback_4709822480 = get('bsFallback', __marker)

            # <Value "python:'btn-secondary ' if not 'btn-' in view.klass else ''" (5:31)> -> __value
            __token = 172
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('python', "'btn-secondary ' if not 'btn-' in view.klass else ''", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['bsFallback'] = __value

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button type="submit"')

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710282720
            __default_4710282720 = _DEFAULT_MARKER

            # <Substitution 'view/id' (6:27)> -> __attr_id
            __token = 260
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_4459168576('path', 'view/id', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710277824
            __default_4710277824 = _DEFAULT_MARKER

            # <Substitution 'view/name' (7:28)> -> __attr_name
            __token = 297
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_4459168576('path', 'view/name', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710277056
            __default_4710277056 = _DEFAULT_MARKER

            # <Substitution 'string:btn ${bsFallback}${view/klass}' (8:28)> -> __attr_class
            __token = 337
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4459168576('string', 'btn ${bsFallback}${view/klass}', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710283920
            __default_4710283920 = _DEFAULT_MARKER

            # <Substitution 'view/value' (9:27)> -> __attr_value
            __token = 405
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_4459168576('path', 'view/value', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710275808
            __default_4710275808 = _DEFAULT_MARKER

            # <Substitution 'view/style' (10:26)> -> __attr_style
            __token = 446
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_4459168576('path', 'view/style', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710277440
            __default_4710277440 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (11:24)> -> __attr_lang
            __token = 486
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_4459168576('path', 'view/lang', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710285072
            __default_4710285072 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (12:26)> -> __attr_onclick
            __token = 528
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_4459168576('path', 'view/onclick', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710282912
            __default_4710282912 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (13:28)> -> __attr_ondblclick
            __token = 576
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_4459168576('path', 'view/ondblclick', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710271776
            __default_4710271776 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (14:28)> -> __attr_onmousedown
            __token = 628
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_4459168576('path', 'view/onmousedown', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710277152
            __default_4710277152 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (15:25)> -> __attr_onmouseup
            __token = 679
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_4459168576('path', 'view/onmouseup', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710281424
            __default_4710281424 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (16:26)> -> __attr_onmouseover
            __token = 730
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_4459168576('path', 'view/onmouseover', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710271056
            __default_4710271056 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (17:25)> -> __attr_onmousemove
            __token = 783
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_4459168576('path', 'view/onmousemove', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710273216
            __default_4710273216 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (18:23)> -> __attr_onmouseout
            __token = 835
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_4459168576('path', 'view/onmouseout', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710284064
            __default_4710284064 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (19:22)> -> __attr_onkeypress
            __token = 886
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_4459168576('path', 'view/onkeypress', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710270672
            __default_4710270672 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (20:20)> -> __attr_onkeydown
            __token = 936
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_4459168576('path', 'view/onkeydown', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710272352
            __default_4710272352 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (21:17)> -> __attr_onkeyup
            __token = 983
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_4459168576('path', 'view/onkeyup', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710274560
            __default_4710274560 = _DEFAULT_MARKER

            # <Boolean 'view/disabled' (22:17)> -> __attr_disabled
            __token = 1029
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_disabled = _static_4459168576('path', 'view/disabled', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            if (__attr_disabled is _DEFAULT_MARKER):
                __attr_disabled = None
            else:
                if __attr_disabled:
                    __attr_disabled = 'disabled'
                else:
                    __attr_disabled = None
            if (__attr_disabled is not None):
                __append((' disabled="%s"' % __attr_disabled))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710274944
            __default_4710274944 = _DEFAULT_MARKER

            # <Substitution 'view/tabindex' (23:16)> -> __attr_tabindex
            __token = 1076
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_tabindex = _static_4459168576('path', 'view/tabindex', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_tabindex is not None):
                __append((' tabindex="%s"' % __attr_tabindex))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710274224
            __default_4710274224 = _DEFAULT_MARKER

            # <Substitution 'view/onfocus' (24:14)> -> __attr_onfocus
            __token = 1122
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_4459168576('path', 'view/onfocus', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710271536
            __default_4710271536 = _DEFAULT_MARKER

            # <Substitution 'view/onblur' (25:12)> -> __attr_onblur
            __token = 1166
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_4459168576('path', 'view/onblur', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710284448
            __default_4710284448 = _DEFAULT_MARKER

            # <Substitution 'view/onchange' (26:13)> -> __attr_onchange
            __token = 1211
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_4459168576('path', 'view/onchange', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((' onchange="%s"' % __attr_onchange))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710281088
            __default_4710281088 = _DEFAULT_MARKER

            # <Boolean 'view/readonly' (27:12)> -> __attr_readonly
            __token = 1258
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_readonly = _static_4459168576('path', 'view/readonly', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            if (__attr_readonly is _DEFAULT_MARKER):
                __attr_readonly = None
            else:
                if __attr_readonly:
                    __attr_readonly = 'readonly'
                else:
                    __attr_readonly = None
            if (__attr_readonly is not None):
                __append((' readonly="%s"' % __attr_readonly))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710277632
            __default_4710277632 = _DEFAULT_MARKER

            # <Substitution 'view/alt' (28:6)> -> __attr_alt
            __token = 1300
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_alt = _static_4459168576('path', 'view/alt', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_alt = __quote(__attr_alt, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_alt is not None):
                __append((' alt="%s"' % __attr_alt))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710019328
            __default_4710019328 = _DEFAULT_MARKER

            # <Substitution 'view/accesskey' (29:11)> -> __attr_accesskey
            __token = 1343
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_accesskey = _static_4459168576('path', 'view/accesskey', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_accesskey is not None):
                __append((' accesskey="%s"' % __attr_accesskey))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710007280
            __default_4710007280 = _DEFAULT_MARKER

            # <Substitution 'view/onselect' (30:9)> -> __attr_onselect
            __token = 1391
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onselect = _static_4459168576('path', 'view/onselect', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onselect is not None):
                __append((' onselect="%s"' % __attr_onselect))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710007856
            __default_4710007856 = _DEFAULT_MARKER

            # <Substitution 'python:view.ignoreRequiredOnValidation or None' (31:14)> -> __attr_formnovalidate
            __token = 1444
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_formnovalidate = _static_4459168576('python', 'view.ignoreRequiredOnValidation or None', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_formnovalidate = __quote(__attr_formnovalidate, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_formnovalidate is not None):
                __append((' formnovalidate="%s"' % __attr_formnovalidate))
            __append('>')

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710282048
            __default_4710282048 = _DEFAULT_MARKER

            # <Value 'view/value' (32:21)> -> __cache_4710284160
            __token = 1538
            try:
                __zt_tmp = __attrs_4710010256
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4710284160 = _static_4459168576('path', 'view/value', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/value' (32:21)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118c13c40> -> __condition
            __expression = __cache_4710284160

            # <Symbol value=<DEFAULT> at 109c89f90> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('value')
            else:
                __content = __cache_4710284160
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</button>')
            if (__backup_bsFallback_4709822480 is __marker):
                del econtext['bsFallback']
            else:
                econtext['bsFallback'] = __backup_bsFallback_4709822480
            __append('\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }