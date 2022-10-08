# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/z3cform/templates/password_input.pt'

__tokens = {299: ('view/id', 7, 26), 335: (' view/nam', 8, 27), 374: ("s python:'form-control {0}{1}'.format(view.klass, view.error and ' is-invalid' or '", 9, 27), 527: ('tle view/t', 11, 25), 566: ('lang view', 12, 23), 1098: ('       disabl', 23, 16), 1322: ('            r', 28, 11), 1363: ('        ', 29, 5), 1144: ('        tabin', 24, 15), 1405: ('             a', 30, 10), 1494: ('         ', 32, 3), 1537: ('              ', 33, 7), 487: ('le view/st', 10, 26), 607: ('click view/o', 13, 25), 654: ('lclick view/ond', 14, 27), 705: ('usedown view/onm', 15, 27), 755: ('nmouseup view/', 16, 24), 805: ('mouseover view/o', 17, 25), 857: ('nmousemove view/', 18, 24), 908: (' onmouseout vie', 19, 22), 958: ('  onkeypress vi', 20, 21), 1007: ('    onkeydown ', 21, 19), 1053: ('       onkey', 22, 16), 1189: ('          on', 25, 13), 1232: ('           ', 26, 11), 1276: ('           on', 27, 12), 1452: ('             ', 31, 8), 1587: ('               p', 34, 8), 1642: ('             autoca', 35, 10)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4459175296 = __C2ZContextWrapper
_static_4459168576 = __compile_zt_expr
_static_4710084624 = {'id': '', 'name': '', 'class': '', 'title': '', 'lang': '', 'disabled': '', 'readonly': '', 'alt': '', 'tabindex': '', 'accesskey': '', 'size': '', 'maxlength': '', 'type': 'password', 'style': 'view/style', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'onselect': 'view/onselect', 'placeholder': 'view/placeholder', 'autocapitalize': 'view/autocapitalize', }
_static_4710084000 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x118be2da0> name=None at 118be0c70> -> __attrs_4710084912
            __attrs_4710084912 = _static_4710084000
            __append('\n')

            # <Static value=<ast.Dict object at 0x118be3010> name=None at 118be2a10> -> __attrs_4709819264
            __attrs_4709819264 = _static_4710084624

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input')

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710077328
            __default_4710077328 = _DEFAULT_MARKER

            # <Substitution 'view/id' (7:26)> -> __attr_id
            __token = 299
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_4459168576('path', 'view/id', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710083280
            __default_4710083280 = _DEFAULT_MARKER

            # <Substitution 'view/name' (8:27)> -> __attr_name
            __token = 335
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_4459168576('path', 'view/name', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709822672
            __default_4709822672 = _DEFAULT_MARKER

            # <Substitution "python:'form-control {0}{1}'.format(view.klass, view.error and ' is-invalid' or '')" (9:27)> -> __attr_class
            __token = 374
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4459168576('python', "'form-control {0}{1}'.format(view.klass, view.error and ' is-invalid' or '')", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709819024
            __default_4709819024 = _DEFAULT_MARKER

            # <Substitution 'view/title' (11:25)> -> __attr_title
            __token = 527
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_4459168576('path', 'view/title', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709816912
            __default_4709816912 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (12:23)> -> __attr_lang
            __token = 566
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_4459168576('path', 'view/lang', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709811968
            __default_4709811968 = _DEFAULT_MARKER

            # <Boolean 'view/disabled' (23:16)> -> __attr_disabled
            __token = 1098
            try:
                __zt_tmp = __attrs_4709819264
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

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709811248
            __default_4709811248 = _DEFAULT_MARKER

            # <Boolean 'view/readonly' (28:11)> -> __attr_readonly
            __token = 1322
            try:
                __zt_tmp = __attrs_4709819264
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

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709811008
            __default_4709811008 = _DEFAULT_MARKER

            # <Substitution 'view/alt' (29:5)> -> __attr_alt
            __token = 1363
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_alt = _static_4459168576('path', 'view/alt', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_alt is not None):
                __append((' alt="%s"' % __attr_alt))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709817392
            __default_4709817392 = _DEFAULT_MARKER

            # <Substitution 'view/tabindex' (24:15)> -> __attr_tabindex
            __token = 1144
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_tabindex = _static_4459168576('path', 'view/tabindex', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_tabindex is not None):
                __append((' tabindex="%s"' % __attr_tabindex))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709811104
            __default_4709811104 = _DEFAULT_MARKER

            # <Substitution 'view/accesskey' (30:10)> -> __attr_accesskey
            __token = 1405
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_accesskey = _static_4459168576('path', 'view/accesskey', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_accesskey is not None):
                __append((' accesskey="%s"' % __attr_accesskey))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709813024
            __default_4709813024 = _DEFAULT_MARKER

            # <Substitution 'view/size' (32:3)> -> __attr_size
            __token = 1494
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_size = _static_4459168576('path', 'view/size', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_size = __quote(__attr_size, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_size is not None):
                __append((' size="%s"' % __attr_size))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709813168
            __default_4709813168 = _DEFAULT_MARKER

            # <Substitution 'view/maxlength' (33:7)> -> __attr_maxlength
            __token = 1537
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_maxlength = _static_4459168576('path', 'view/maxlength', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_maxlength = __quote(__attr_maxlength, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_maxlength is not None):
                __append((' maxlength="%s"' % __attr_maxlength))
            __append(' type="password"')

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709811776
            __default_4709811776 = _DEFAULT_MARKER

            # <Substitution 'view/style' (10:26)> -> __attr_style
            __token = 487
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_4459168576('path', 'view/style', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709818256
            __default_4709818256 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (13:25)> -> __attr_onclick
            __token = 607
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_4459168576('path', 'view/onclick', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709817872
            __default_4709817872 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (14:27)> -> __attr_ondblclick
            __token = 654
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_4459168576('path', 'view/ondblclick', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709815808
            __default_4709815808 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (15:27)> -> __attr_onmousedown
            __token = 705
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_4459168576('path', 'view/onmousedown', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709810816
            __default_4709810816 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (16:24)> -> __attr_onmouseup
            __token = 755
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_4459168576('path', 'view/onmouseup', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709813744
            __default_4709813744 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (17:25)> -> __attr_onmouseover
            __token = 805
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_4459168576('path', 'view/onmouseover', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709815232
            __default_4709815232 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (18:24)> -> __attr_onmousemove
            __token = 857
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_4459168576('path', 'view/onmousemove', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709814896
            __default_4709814896 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (19:22)> -> __attr_onmouseout
            __token = 908
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_4459168576('path', 'view/onmouseout', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709812064
            __default_4709812064 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (20:21)> -> __attr_onkeypress
            __token = 958
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_4459168576('path', 'view/onkeypress', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709811296
            __default_4709811296 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (21:19)> -> __attr_onkeydown
            __token = 1007
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_4459168576('path', 'view/onkeydown', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709811440
            __default_4709811440 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (22:16)> -> __attr_onkeyup
            __token = 1053
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_4459168576('path', 'view/onkeyup', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709813456
            __default_4709813456 = _DEFAULT_MARKER

            # <Substitution 'view/onfocus' (25:13)> -> __attr_onfocus
            __token = 1189
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_4459168576('path', 'view/onfocus', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709819648
            __default_4709819648 = _DEFAULT_MARKER

            # <Substitution 'view/onblur' (26:11)> -> __attr_onblur
            __token = 1232
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_4459168576('path', 'view/onblur', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709819072
            __default_4709819072 = _DEFAULT_MARKER

            # <Substitution 'view/onchange' (27:12)> -> __attr_onchange
            __token = 1276
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_4459168576('path', 'view/onchange', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((' onchange="%s"' % __attr_onchange))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709817920
            __default_4709817920 = _DEFAULT_MARKER

            # <Substitution 'view/onselect' (31:8)> -> __attr_onselect
            __token = 1452
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onselect = _static_4459168576('path', 'view/onselect', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onselect is not None):
                __append((' onselect="%s"' % __attr_onselect))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709822384
            __default_4709822384 = _DEFAULT_MARKER

            # <Substitution 'view/placeholder' (34:8)> -> __attr_placeholder
            __token = 1587
            try:
                __zt_tmp = __attrs_4709819264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_placeholder = _static_4459168576('path', 'view/placeholder', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_placeholder = __quote(__attr_placeholder, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_placeholder is not None):
                __append((' placeholder="%s"' % __attr_placeholder))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709822048
            __default_4709822048 = _DEFAULT_MARKER

            # <Substitution 'view/autocapitalize' (35:10)> -> __attr_autocapitalize
            __token = 1642
            try:
                __zt_tmp = __attrs_4709819264
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