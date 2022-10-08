# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/z3cform/templates/textarea_input.pt'

__tokens = {245: ('view/id', 7, 22), 277: (' view/nam', 8, 23), 312: ('s string:form-control ${view/klas', 9, 23), 1130: ('         ', 28, 3), 1164: ('         ', 29, 2), 972: ('        tabin', 24, 11), 930: ('       disabl', 23, 12), 1202: ('             ', 30, 5), 1245: ('              ', 31, 5), 371: ('le view/st', 10, 22), 407: ('tle view/t', 11, 21), 442: ('lang view', 12, 19), 479: ('click view/o', 13, 21), 522: ('lclick view/ond', 14, 23), 569: ('usedown view/onm', 15, 23), 615: ('nmouseup view/', 16, 20), 661: ('mouseover view/o', 17, 21), 709: ('nmousemove view/', 18, 20), 756: (' onmouseout vie', 19, 18), 802: ('  onkeypress vi', 20, 17), 847: ('    onkeydown ', 21, 15), 889: ('       onkey', 22, 12), 1013: ('          on', 25, 9), 1052: ('           ', 26, 7), 1092: ('           on', 27, 8), 1288: ('             ', 32, 3), 1344: ('view/value', 33, 16)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4417565216 = __C2ZContextWrapper
_static_4417553984 = __compile_zt_expr
_static_4482868528 = {'id': '', 'name': '', 'class': '', 'cols': '', 'rows': '', 'tabindex': '', 'disabled': '', 'readonly': '', 'accesskey': '', 'style': 'view/style', 'title': 'view/title', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'onselect': 'view/onselect', }
_static_4482871168 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x10b332f80> name=None at 10b331060> -> __attrs_4482871408
            __attrs_4482871408 = _static_4482871168
            __append('\n')

            # <Static value=<ast.Dict object at 0x10b332530> name=None at 10b3307c0> -> __attrs_4482928976
            __attrs_4482928976 = _static_4482868528

            # <textarea ... (0:0)
            # --------------------------------------------------------
            __append('<textarea')

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482872944
            __default_4482872944 = _DEFAULT_MARKER

            # <Substitution 'view/id' (7:22)> -> __attr_id
            __token = 245
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_4417553984('path', 'view/id', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482873280
            __default_4482873280 = _DEFAULT_MARKER

            # <Substitution 'view/name' (8:23)> -> __attr_name
            __token = 277
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_4417553984('path', 'view/name', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482867760
            __default_4482867760 = _DEFAULT_MARKER

            # <Substitution 'string:form-control ${view/klass}' (9:23)> -> __attr_class
            __token = 312
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4417553984('string', 'form-control ${view/klass}', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482861040
            __default_4482861040 = _DEFAULT_MARKER

            # <Substitution 'view/cols' (28:3)> -> __attr_cols
            __token = 1130
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_cols = _static_4417553984('path', 'view/cols', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_cols = __quote(__attr_cols, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_cols is not None):
                __append((' cols="%s"' % __attr_cols))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482859840
            __default_4482859840 = _DEFAULT_MARKER

            # <Substitution 'view/rows' (29:2)> -> __attr_rows
            __token = 1164
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_rows = _static_4417553984('path', 'view/rows', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_rows = __quote(__attr_rows, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_rows is not None):
                __append((' rows="%s"' % __attr_rows))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482864784
            __default_4482864784 = _DEFAULT_MARKER

            # <Substitution 'view/tabindex' (24:11)> -> __attr_tabindex
            __token = 972
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_tabindex = _static_4417553984('path', 'view/tabindex', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_tabindex is not None):
                __append((' tabindex="%s"' % __attr_tabindex))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482867472
            __default_4482867472 = _DEFAULT_MARKER

            # <Boolean 'view/disabled' (23:12)> -> __attr_disabled
            __token = 930
            try:
                __zt_tmp = __attrs_4482928976
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

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482874144
            __default_4482874144 = _DEFAULT_MARKER

            # <Boolean 'view/readonly' (30:5)> -> __attr_readonly
            __token = 1202
            try:
                __zt_tmp = __attrs_4482928976
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

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482874096
            __default_4482874096 = _DEFAULT_MARKER

            # <Substitution 'view/accesskey' (31:5)> -> __attr_accesskey
            __token = 1245
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_accesskey = _static_4417553984('path', 'view/accesskey', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_accesskey is not None):
                __append((' accesskey="%s"' % __attr_accesskey))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482873568
            __default_4482873568 = _DEFAULT_MARKER

            # <Substitution 'view/style' (10:22)> -> __attr_style
            __token = 371
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_4417553984('path', 'view/style', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482873760
            __default_4482873760 = _DEFAULT_MARKER

            # <Substitution 'view/title' (11:21)> -> __attr_title
            __token = 407
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_4417553984('path', 'view/title', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482875056
            __default_4482875056 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (12:19)> -> __attr_lang
            __token = 442
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_4417553984('path', 'view/lang', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482874432
            __default_4482874432 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (13:21)> -> __attr_onclick
            __token = 479
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_4417553984('path', 'view/onclick', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482861520
            __default_4482861520 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (14:23)> -> __attr_ondblclick
            __token = 522
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_4417553984('path', 'view/ondblclick', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482861232
            __default_4482861232 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (15:23)> -> __attr_onmousedown
            __token = 569
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_4417553984('path', 'view/onmousedown', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482860272
            __default_4482860272 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (16:20)> -> __attr_onmouseup
            __token = 615
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_4417553984('path', 'view/onmouseup', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482936224
            __default_4482936224 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (17:21)> -> __attr_onmouseover
            __token = 661
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_4417553984('path', 'view/onmouseover', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482936080
            __default_4482936080 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (18:20)> -> __attr_onmousemove
            __token = 709
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_4417553984('path', 'view/onmousemove', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482869680
            __default_4482869680 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (19:18)> -> __attr_onmouseout
            __token = 756
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_4417553984('path', 'view/onmouseout', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482935552
            __default_4482935552 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (20:17)> -> __attr_onkeypress
            __token = 802
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_4417553984('path', 'view/onkeypress', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482935168
            __default_4482935168 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (21:15)> -> __attr_onkeydown
            __token = 847
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_4417553984('path', 'view/onkeydown', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482932672
            __default_4482932672 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (22:12)> -> __attr_onkeyup
            __token = 889
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_4417553984('path', 'view/onkeyup', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482932768
            __default_4482932768 = _DEFAULT_MARKER

            # <Substitution 'view/onfocus' (25:9)> -> __attr_onfocus
            __token = 1013
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_4417553984('path', 'view/onfocus', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482933248
            __default_4482933248 = _DEFAULT_MARKER

            # <Substitution 'view/onblur' (26:7)> -> __attr_onblur
            __token = 1052
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_4417553984('path', 'view/onblur', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482933104
            __default_4482933104 = _DEFAULT_MARKER

            # <Substitution 'view/onchange' (27:8)> -> __attr_onchange
            __token = 1092
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_4417553984('path', 'view/onchange', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((' onchange="%s"' % __attr_onchange))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482926432
            __default_4482926432 = _DEFAULT_MARKER

            # <Substitution 'view/onselect' (32:3)> -> __attr_onselect
            __token = 1288
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onselect = _static_4417553984('path', 'view/onselect', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onselect is not None):
                __append((' onselect="%s"' % __attr_onselect))
            __append('>')

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4482872464
            __default_4482872464 = _DEFAULT_MARKER

            # <Value 'view/value' (33:16)> -> __cache_4482871984
            __token = 1344
            try:
                __zt_tmp = __attrs_4482928976
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4482871984 = _static_4417553984('path', 'view/value', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/value' (33:16)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107619600> at 10b333370> -> __condition
            __expression = __cache_4482871984

            # <Symbol value=<DEFAULT> at 107619600> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4482871984
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</textarea>\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }