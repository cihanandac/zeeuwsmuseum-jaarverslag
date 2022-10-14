# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/z3cform/templates/orderedselect_input.pt'

__tokens = {333: ('view/id', 8, 26), 455: ('string:${view/id}-from', 12, 29), 509: (' string:${view/name}.fro', 13, 30), 566: ('s string:form-control ${view/klas', 14, 30), 1521: ('            m', 33, 14), 1566: ('         ', 34, 9), 632: ('le view/st', 15, 29), 675: ('tle view/t', 16, 28), 717: ('lang view', 17, 26), 761: ('click view/o', 18, 28), 811: ('lclick view/ond', 19, 30), 865: ('usedown view/onm', 20, 30), 918: ('nmouseup view/', 21, 27), 971: ('mouseover view/o', 22, 28), 1026: ('nmousemove view/', 23, 27), 1080: (' onmouseout vie', 24, 25), 1133: ('  onkeypress vi', 25, 24), 1185: ('    onkeydown ', 26, 22), 1234: ('       onkey', 27, 19), 1282: ('       disabl', 28, 19), 1331: ('        tabin', 29, 18), 1379: ('          on', 30, 16), 1425: ('           ', 31, 14), 1472: ('           on', 32, 15), 1634: ('view/notselectedItems', 35, 34), 1695: ('entry/value', 36, 38), 1737: ('nocall:entry/content', 37, 29), 2002: ("string:javascript:from2to('${view/id}')", 43, 38), 2271: ("string:javascript:to2from('${view/id}')", 48, 38), 2449: ('string:${view/id}-to', 53, 29), 2501: (' string:${view/name}.t', 54, 30), 2556: ('s string:form-control ${view/klas', 55, 30), 3511: ('            m', 74, 14), 3556: ('         ', 75, 9), 2622: ('le view/st', 56, 29), 2665: ('tle view/t', 57, 28), 2707: ('lang view', 58, 26), 2751: ('click view/o', 59, 28), 2801: ('lclick view/ond', 60, 30), 2855: ('usedown view/onm', 61, 30), 2908: ('nmouseup view/', 62, 27), 2961: ('mouseover view/o', 63, 28), 3016: ('nmousemove view/', 64, 27), 3070: (' onmouseout vie', 65, 25), 3123: ('  onkeypress vi', 66, 24), 3175: ('    onkeydown ', 67, 22), 3224: ('       onkey', 68, 19), 3272: ('       disabl', 69, 19), 3321: ('        tabin', 70, 18), 3369: ('          on', 71, 16), 3415: ('           ', 72, 14), 3462: ('           on', 73, 15), 3624: ('view/selectedItems', 76, 34), 3682: ('entry/value', 77, 38), 3724: ('nocall:entry/content', 78, 29), 3862: ('string:${view/name}-empty-marker', 81, 29), 3984: ('string:${view/id}-toDataContainer', 83, 31), 4072: ("string:copyDataForSubmit('${view/id}');", 84, 52), 4128: ('<![CDATA[ */\n          // initial copying of field "field.to" --> "field"\n          copyDataForSubmit("<i tal:replace="${view/id}"/>");\n          /* ]]>', 85, 14), 4249: ('view/id', 87, 47), 4519: ("string:javascript:moveUp('${view/id}')", 96, 34), 4787: ("string:javascript:moveDown('${view/id}')", 102, 34)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_5109094272 = {'onClick': 'javascript:moveDown()', 'class': 'btn btn-sm btn-outline-secondary', 'name': 'downButton', 'type': 'button', 'value': '&darr;', }
_static_5109093600 = {'onClick': 'javascript:moveUp()', 'class': 'btn btn-sm btn-outline-secondary', 'name': 'upButton', 'type': 'button', 'value': '&uarr;', }
_static_4899650384 = {'type': 'text/javascript', }
_static_4961500128 = {'id': 'toDataContainer', 'style': 'display: none', }
_static_4961488512 = {'name': 'foo-empty-marker', 'type': 'hidden', }
_static_4961484960 = {'value': 'entry/value', }
_static_4959661664 = {'id': 'to', 'name': 'to', 'class': '', 'multiple': '', 'size': '5', 'style': 'view/style', 'title': 'view/title', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'disabled': 'view/disabled', 'tabindex': 'view/tabindex', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', }
_static_4960369776 = {'onClick': 'javascript:to2from()', 'class': 'btn btn-sm btn-outline-secondary', 'name': 'to2fromButton', 'type': 'button', 'value': '&larr;', }
_static_5108965984 = {'onClick': 'javascript:from2to()', 'class': 'btn btn-sm btn-outline-secondary', 'name': 'from2toButton', 'type': 'button', 'value': '&rarr;', }
_static_5108972512 = {'value': 'entry/value', }
_static_4899675616 = {'id': 'from', 'name': 'from', 'class': '', 'multiple': '', 'size': '5', 'style': 'view/style', 'title': 'view/title', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'disabled': 'view/disabled', 'tabindex': 'view/tabindex', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', }
_static_4428767312 = {}
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
_static_5110155392 = {'border': '0', 'class': 'ordered-selection-field', 'id': 'view/id', }
_static_5110160384 = {'type': 'text/javascript', 'src': '++resource++orderedselect_input.js', }
_static_5110154480 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x13096c4f0> name=None at 13096d3c0> -> __attrs_5110156736
            __attrs_5110156736 = _static_5110154480
            __append('\n')

            # <Static value=<ast.Dict object at 0x13096dc00> name=None at 13096dc30> -> __attrs_5110154240
            __attrs_5110154240 = _static_5110160384

            # <script ... (0:0)
            # --------------------------------------------------------
            __append('<script type="text/javascript" src="++resource++orderedselect_input.js"></script>\n\n')

            # <Static value=<ast.Dict object at 0x13096c880> name=None at 13096e770> -> __attrs_5110162832
            __attrs_5110162832 = _static_5110155392

            # <table ... (0:0)
            # --------------------------------------------------------
            __append('<table border="0" class="ordered-selection-field"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5110169168
            __default_5110169168 = _DEFAULT_MARKER

            # <Substitution 'view/id' (8:26)> -> __attr_id
            __token = 333
            try:
                __zt_tmp = __attrs_5110162832
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_4427992992('path', 'view/id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))
            __append('>\n  ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5110157744
            __attrs_5110157744 = _static_4428767312

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append('<tr>\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5110157552
            __attrs_5110157552 = _static_4428767312

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>\n      ')

            # <Static value=<ast.Dict object at 0x1240b1de0> name=None at 1240b3e20> -> __attrs_5108963536
            __attrs_5108963536 = _static_4899675616

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4916430016
            __default_4916430016 = _DEFAULT_MARKER

            # <Substitution 'string:${view/id}-from' (12:29)> -> __attr_id
            __token = 455
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_4427992992('string', '${view/id}-from', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', 'from', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4892037168
            __default_4892037168 = _DEFAULT_MARKER

            # <Substitution 'string:${view/name}.from' (13:30)> -> __attr_name
            __token = 509
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_4427992992('string', '${view/name}.from', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', 'from', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4958323616
            __default_4958323616 = _DEFAULT_MARKER

            # <Substitution 'string:form-control ${view/klass}' (14:30)> -> __attr_class
            __token = 566
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4427992992('string', 'form-control ${view/klass}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4958336912
            __default_4958336912 = _DEFAULT_MARKER

            # <Boolean 'view/multiple' (33:14)> -> __attr_multiple
            __token = 1521
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_multiple = _static_4427992992('path', 'view/multiple', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if (__attr_multiple is _DEFAULT_MARKER):
                __attr_multiple = ''
            else:
                if __attr_multiple:
                    __attr_multiple = 'multiple'
                else:
                    __attr_multiple = None
            if (__attr_multiple is not None):
                __append(('  multiple="%s"' % __attr_multiple))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5110161680
            __default_5110161680 = _DEFAULT_MARKER

            # <Substitution 'view/size' (34:9)> -> __attr_size
            __token = 1566
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_size = _static_4427992992('path', 'view/size', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_size = __quote(__attr_size, '"', '&quot;', '5', _DEFAULT_MARKER)
            if (__attr_size is not None):
                __append((' size="%s"' % __attr_size))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5110165040
            __default_5110165040 = _DEFAULT_MARKER

            # <Substitution 'view/style' (15:29)> -> __attr_style
            __token = 632
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_4427992992('path', 'view/style', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5110169312
            __default_5110169312 = _DEFAULT_MARKER

            # <Substitution 'view/title' (16:28)> -> __attr_title
            __token = 675
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_4427992992('path', 'view/title', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5110160720
            __default_5110160720 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (17:26)> -> __attr_lang
            __token = 717
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_4427992992('path', 'view/lang', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108681072
            __default_5108681072 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (18:28)> -> __attr_onclick
            __token = 761
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_4427992992('path', 'view/onclick', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108687792
            __default_5108687792 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (19:30)> -> __attr_ondblclick
            __token = 811
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_4427992992('path', 'view/ondblclick', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108687504
            __default_5108687504 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (20:30)> -> __attr_onmousedown
            __token = 865
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_4427992992('path', 'view/onmousedown', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108691680
            __default_5108691680 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (21:27)> -> __attr_onmouseup
            __token = 918
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_4427992992('path', 'view/onmouseup', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108689232
            __default_5108689232 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (22:28)> -> __attr_onmouseover
            __token = 971
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_4427992992('path', 'view/onmouseover', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108683712
            __default_5108683712 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (23:27)> -> __attr_onmousemove
            __token = 1026
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_4427992992('path', 'view/onmousemove', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108692112
            __default_5108692112 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (24:25)> -> __attr_onmouseout
            __token = 1080
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_4427992992('path', 'view/onmouseout', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108693168
            __default_5108693168 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (25:24)> -> __attr_onkeypress
            __token = 1133
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_4427992992('path', 'view/onkeypress', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4958412736
            __default_4958412736 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (26:22)> -> __attr_onkeydown
            __token = 1185
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_4427992992('path', 'view/onkeydown', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4958407888
            __default_4958407888 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (27:19)> -> __attr_onkeyup
            __token = 1234
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_4427992992('path', 'view/onkeyup', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4958408560
            __default_4958408560 = _DEFAULT_MARKER

            # <Boolean 'view/disabled' (28:19)> -> __attr_disabled
            __token = 1282
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_disabled = _static_4427992992('path', 'view/disabled', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if (__attr_disabled is _DEFAULT_MARKER):
                __attr_disabled = None
            else:
                if __attr_disabled:
                    __attr_disabled = 'disabled'
                else:
                    __attr_disabled = None
            if (__attr_disabled is not None):
                __append((' disabled="%s"' % __attr_disabled))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4958416480
            __default_4958416480 = _DEFAULT_MARKER

            # <Substitution 'view/tabindex' (29:18)> -> __attr_tabindex
            __token = 1331
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_tabindex = _static_4427992992('path', 'view/tabindex', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_tabindex is not None):
                __append((' tabindex="%s"' % __attr_tabindex))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4915627104
            __default_4915627104 = _DEFAULT_MARKER

            # <Substitution 'view/onfocus' (30:16)> -> __attr_onfocus
            __token = 1379
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_4427992992('path', 'view/onfocus', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4915641600
            __default_4915641600 = _DEFAULT_MARKER

            # <Substitution 'view/onblur' (31:14)> -> __attr_onblur
            __token = 1425
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_4427992992('path', 'view/onblur', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108972608
            __default_5108972608 = _DEFAULT_MARKER

            # <Substitution 'view/onchange' (32:15)> -> __attr_onchange
            __token = 1472
            try:
                __zt_tmp = __attrs_5108963536
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_4427992992('path', 'view/onchange', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((' onchange="%s"' % __attr_onchange))
            __append('>\n        ')

            # <Static value=<ast.Dict object at 0x13084bbe0> name=None at 130849c00> -> __attrs_5108966560
            __attrs_5108966560 = _static_5108972512
            __backup_entry_4943225056 = get('entry', __marker)

            # <Value 'view/notselectedItems' (35:34)> -> __iterator
            __token = 1634
            try:
                __zt_tmp = __attrs_5108966560
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4427992992('path', 'view/notselectedItems', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            (__iterator, ____index_5108966800, ) = getname('repeat')('entry', __iterator)
            econtext['entry'] = None
            for __item in __iterator:
                econtext['entry'] = __item

                # <option ... (0:0)
                # --------------------------------------------------------
                __append('<option')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108960848
                __default_5108960848 = _DEFAULT_MARKER

                # <Substitution 'entry/value' (36:38)> -> __attr_value
                __token = 1695
                try:
                    __zt_tmp = __attrs_5108966560
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'entry/value', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append('>')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108966128
                __default_5108966128 = _DEFAULT_MARKER

                # <Value 'nocall:entry/content' (37:29)> -> __cache_5108967376
                __token = 1737
                try:
                    __zt_tmp = __attrs_5108966560
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_5108967376 = _static_4427992992('nocall', 'entry/content', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'nocall:entry/content' (37:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 13084a770> -> __condition
                __expression = __cache_5108967376

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_5108967376
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</option>')
                ____index_5108966800 -= 1
                if (____index_5108966800 > 0):
                    __append('\n        ')
            if (__backup_entry_4943225056 is __marker):
                del econtext['entry']
            else:
                econtext['entry'] = __backup_entry_4943225056
            __append('\n      </select>\n    </td>\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5108968432
            __attrs_5108968432 = _static_4428767312

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>\n      ')

            # <Static value=<ast.Dict object at 0x13084a260> name=None at 130849690> -> __attrs_5108968624
            __attrs_5108968624 = _static_5108965984

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108960128
            __default_5108960128 = _DEFAULT_MARKER

            # <Substitution "string:javascript:from2to('${view/id}')" (43:38)> -> __attr_onClick
            __token = 2002
            try:
                __zt_tmp = __attrs_5108968624
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onClick = _static_4427992992('string', "javascript:from2to('${view/id}')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onClick = __quote(__attr_onClick, '"', '&quot;', 'javascript:from2to()', _DEFAULT_MARKER)
            if (__attr_onClick is not None):
                __append((' onClick="%s"' % __attr_onClick))
            __append(' class="btn btn-sm btn-outline-secondary" name="from2toButton" type="button" value="&rarr;" >&rarr;</button>\n      ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4960362384
            __attrs_4960362384 = _static_4428767312

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br />\n      ')

            # <Static value=<ast.Dict object at 0x127a93c70> name=None at 127a91090> -> __attrs_4959658064
            __attrs_4959658064 = _static_4960369776

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4960356048
            __default_4960356048 = _DEFAULT_MARKER

            # <Substitution "string:javascript:to2from('${view/id}')" (48:38)> -> __attr_onClick
            __token = 2271
            try:
                __zt_tmp = __attrs_4959658064
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onClick = _static_4427992992('string', "javascript:to2from('${view/id}')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onClick = __quote(__attr_onClick, '"', '&quot;', 'javascript:to2from()', _DEFAULT_MARKER)
            if (__attr_onClick is not None):
                __append((' onClick="%s"' % __attr_onClick))
            __append(' class="btn btn-sm btn-outline-secondary" name="to2fromButton" type="button" value="&larr;" >&larr;</button>\n    </td>\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4959657776
            __attrs_4959657776 = _static_4428767312

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>\n      ')

            # <Static value=<ast.Dict object at 0x1279e6e60> name=None at 1279e5c00> -> __attrs_4961840112
            __attrs_4961840112 = _static_4959661664

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4959656576
            __default_4959656576 = _DEFAULT_MARKER

            # <Substitution 'string:${view/id}-to' (53:29)> -> __attr_id
            __token = 2449
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_4427992992('string', '${view/id}-to', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', 'to', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4959656528
            __default_4959656528 = _DEFAULT_MARKER

            # <Substitution 'string:${view/name}.to' (54:30)> -> __attr_name
            __token = 2501
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_4427992992('string', '${view/name}.to', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', 'to', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109501376
            __default_5109501376 = _DEFAULT_MARKER

            # <Substitution 'string:form-control ${view/klass}' (55:30)> -> __attr_class
            __token = 2556
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4427992992('string', 'form-control ${view/klass}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109503392
            __default_5109503392 = _DEFAULT_MARKER

            # <Boolean 'view/multiple' (74:14)> -> __attr_multiple
            __token = 3511
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_multiple = _static_4427992992('path', 'view/multiple', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if (__attr_multiple is _DEFAULT_MARKER):
                __attr_multiple = ''
            else:
                if __attr_multiple:
                    __attr_multiple = 'multiple'
                else:
                    __attr_multiple = None
            if (__attr_multiple is not None):
                __append((' multiple="%s"' % __attr_multiple))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109498112
            __default_5109498112 = _DEFAULT_MARKER

            # <Substitution 'view/size' (75:9)> -> __attr_size
            __token = 3556
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_size = _static_4427992992('path', 'view/size', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_size = __quote(__attr_size, '"', '&quot;', '5', _DEFAULT_MARKER)
            if (__attr_size is not None):
                __append((' size="%s"' % __attr_size))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109507088
            __default_5109507088 = _DEFAULT_MARKER

            # <Substitution 'view/style' (56:29)> -> __attr_style
            __token = 2622
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_4427992992('path', 'view/style', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109502432
            __default_5109502432 = _DEFAULT_MARKER

            # <Substitution 'view/title' (57:28)> -> __attr_title
            __token = 2665
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_4427992992('path', 'view/title', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109507904
            __default_5109507904 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (58:26)> -> __attr_lang
            __token = 2707
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_4427992992('path', 'view/lang', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109507184
            __default_5109507184 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (59:28)> -> __attr_onclick
            __token = 2751
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_4427992992('path', 'view/onclick', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109502864
            __default_5109502864 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (60:30)> -> __attr_ondblclick
            __token = 2801
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_4427992992('path', 'view/ondblclick', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109508720
            __default_5109508720 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (61:30)> -> __attr_onmousedown
            __token = 2855
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_4427992992('path', 'view/onmousedown', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109508000
            __default_5109508000 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (62:27)> -> __attr_onmouseup
            __token = 2908
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_4427992992('path', 'view/onmouseup', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109507760
            __default_5109507760 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (63:28)> -> __attr_onmouseover
            __token = 2961
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_4427992992('path', 'view/onmouseover', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109499456
            __default_5109499456 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (64:27)> -> __attr_onmousemove
            __token = 3016
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_4427992992('path', 'view/onmousemove', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109499792
            __default_5109499792 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (65:25)> -> __attr_onmouseout
            __token = 3070
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_4427992992('path', 'view/onmouseout', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109503728
            __default_5109503728 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (66:24)> -> __attr_onkeypress
            __token = 3123
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_4427992992('path', 'view/onkeypress', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109503296
            __default_5109503296 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (67:22)> -> __attr_onkeydown
            __token = 3175
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_4427992992('path', 'view/onkeydown', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4932609232
            __default_4932609232 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (68:19)> -> __attr_onkeyup
            __token = 3224
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_4427992992('path', 'view/onkeyup', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4932613408
            __default_4932613408 = _DEFAULT_MARKER

            # <Boolean 'view/disabled' (69:19)> -> __attr_disabled
            __token = 3272
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_disabled = _static_4427992992('path', 'view/disabled', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if (__attr_disabled is _DEFAULT_MARKER):
                __attr_disabled = None
            else:
                if __attr_disabled:
                    __attr_disabled = 'disabled'
                else:
                    __attr_disabled = None
            if (__attr_disabled is not None):
                __append((' disabled="%s"' % __attr_disabled))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4932607504
            __default_4932607504 = _DEFAULT_MARKER

            # <Substitution 'view/tabindex' (70:18)> -> __attr_tabindex
            __token = 3321
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_tabindex = _static_4427992992('path', 'view/tabindex', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_tabindex is not None):
                __append((' tabindex="%s"' % __attr_tabindex))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4932606400
            __default_4932606400 = _DEFAULT_MARKER

            # <Substitution 'view/onfocus' (71:16)> -> __attr_onfocus
            __token = 3369
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_4427992992('path', 'view/onfocus', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4932604000
            __default_4932604000 = _DEFAULT_MARKER

            # <Substitution 'view/onblur' (72:14)> -> __attr_onblur
            __token = 3415
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_4427992992('path', 'view/onblur', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4907583232
            __default_4907583232 = _DEFAULT_MARKER

            # <Substitution 'view/onchange' (73:15)> -> __attr_onchange
            __token = 3462
            try:
                __zt_tmp = __attrs_4961840112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_4427992992('path', 'view/onchange', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((' onchange="%s"' % __attr_onchange))
            __append('>\n        ')

            # <Static value=<ast.Dict object at 0x127ba40a0> name=None at 127ba4400> -> __attrs_4961498784
            __attrs_4961498784 = _static_4961484960
            __backup_entry_5108867392 = get('entry', __marker)

            # <Value 'view/selectedItems' (76:34)> -> __iterator
            __token = 3624
            try:
                __zt_tmp = __attrs_4961498784
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4427992992('path', 'view/selectedItems', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            (__iterator, ____index_4961487648, ) = getname('repeat')('entry', __iterator)
            econtext['entry'] = None
            for __item in __iterator:
                econtext['entry'] = __item

                # <option ... (0:0)
                # --------------------------------------------------------
                __append('<option')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961487072
                __default_4961487072 = _DEFAULT_MARKER

                # <Substitution 'entry/value' (77:38)> -> __attr_value
                __token = 3682
                try:
                    __zt_tmp = __attrs_4961498784
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'entry/value', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append('>')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961490480
                __default_4961490480 = _DEFAULT_MARKER

                # <Value 'nocall:entry/content' (78:29)> -> __cache_4961487168
                __token = 3724
                try:
                    __zt_tmp = __attrs_4961498784
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4961487168 = _static_4427992992('nocall', 'entry/content', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'nocall:entry/content' (78:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 127ba6500> -> __condition
                __expression = __cache_4961487168

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4961487168
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</option>')
                ____index_4961487648 -= 1
                if (____index_4961487648 > 0):
                    __append('\n        ')
            if (__backup_entry_5108867392 is __marker):
                del econtext['entry']
            else:
                econtext['entry'] = __backup_entry_5108867392
            __append('\n      </select>\n      ')

            # <Static value=<ast.Dict object at 0x127ba4e80> name=None at 127ba74f0> -> __attrs_4961486112
            __attrs_4961486112 = _static_4961488512

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961499552
            __default_4961499552 = _DEFAULT_MARKER

            # <Substitution 'string:${view/name}-empty-marker' (81:29)> -> __attr_name
            __token = 3862
            try:
                __zt_tmp = __attrs_4961486112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_4427992992('string', '${view/name}-empty-marker', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', 'foo-empty-marker', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))
            __append(' type="hidden"/>\n      ')

            # <Static value=<ast.Dict object at 0x127ba7be0> name=None at 127ba6590> -> __attrs_4961494128
            __attrs_4961494128 = _static_4961500128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961493264
            __default_4961493264 = _DEFAULT_MARKER

            # <Substitution 'string:${view/id}-toDataContainer' (83:31)> -> __attr_id
            __token = 3984
            try:
                __zt_tmp = __attrs_4961494128
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_4427992992('string', '${view/id}-toDataContainer', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', 'toDataContainer', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))
            __append(' style="display: none">\n        ')

            # <Static value=<ast.Dict object at 0x1240abb50> name=None at 1308277c0> -> __attrs_4899643520
            __attrs_4899643520 = _static_4899650384

            # <script ... (0:0)
            # --------------------------------------------------------
            __append('<script type="text/javascript">')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108822224
            __default_5108822224 = _DEFAULT_MARKER

            # <Value "string:copyDataForSubmit('${view/id}');" (84:52)> -> __cache_5108813824
            __token = 4072
            try:
                __zt_tmp = __attrs_4899643520
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_5108813824 = _static_4427992992('string', "copyDataForSubmit('${view/id}');", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value "string:copyDataForSubmit('${view/id}');" (84:52)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 130825420> -> __condition
            __expression = __cache_5108813824

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('\n          /*  ')

                # <Interpolation value=<Substitution '<![CDATA[ */\n          // initial copying of field "field.to" --> "field"\n          copyDataForSubmit("<i tal:replace="${view/id}"/>");\n          /* ]]>' (85:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1240aae60> -> __content_4353737008
                __token = 4128
                __token = 4249
                try:
                    __zt_tmp = __attrs_4899643520
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_4353737008 = _static_4427992992('path', 'view/id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
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
                __content_4353737008 = ('%s%s%s' % ('<![CDATA[ */\n          // initial copying of field "field.to" --> "field"\n          copyDataForSubmit("<i tal:replace="', (__content_4353737008 if (__content_4353737008 is not None) else ''), '"/>");\n          /* ]]>', ))
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
                __append(' */\n        ')
            else:
                __content = __cache_5108813824
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</script>\n      </span>\n    </td>\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109089904
            __attrs_5109089904 = _static_4428767312

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>\n      ')

            # <Static value=<ast.Dict object at 0x1308694e0> name=None at 130869480> -> __attrs_5109093024
            __attrs_5109093024 = _static_5109093600

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109088992
            __default_5109088992 = _DEFAULT_MARKER

            # <Substitution "string:javascript:moveUp('${view/id}')" (96:34)> -> __attr_onClick
            __token = 4519
            try:
                __zt_tmp = __attrs_5109093024
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onClick = _static_4427992992('string', "javascript:moveUp('${view/id}')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onClick = __quote(__attr_onClick, '"', '&quot;', 'javascript:moveUp()', _DEFAULT_MARKER)
            if (__attr_onClick is not None):
                __append((' onClick="%s"' % __attr_onClick))
            __append(' class="btn btn-sm btn-outline-secondary" name="upButton" type="button" value="&uarr;" >&uarr;</button>\n      ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109101856
            __attrs_5109101856 = _static_4428767312

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br />\n      ')

            # <Static value=<ast.Dict object at 0x130869780> name=None at 13086b070> -> __attrs_5109101760
            __attrs_5109101760 = _static_5109094272

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109099024
            __default_5109099024 = _DEFAULT_MARKER

            # <Substitution "string:javascript:moveDown('${view/id}')" (102:34)> -> __attr_onClick
            __token = 4787
            try:
                __zt_tmp = __attrs_5109101760
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onClick = _static_4427992992('string', "javascript:moveDown('${view/id}')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_onClick = __quote(__attr_onClick, '"', '&quot;', 'javascript:moveDown()', _DEFAULT_MARKER)
            if (__attr_onClick is not None):
                __append((' onClick="%s"' % __attr_onClick))
            __append(' class="btn btn-sm btn-outline-secondary" name="downButton" type="button" value="&darr;" >&darr;</button>\n    </td>\n  </tr>\n</table>\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }