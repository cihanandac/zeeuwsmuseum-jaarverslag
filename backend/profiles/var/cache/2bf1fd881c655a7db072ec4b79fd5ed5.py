# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/textfield/widget_textarea_display.pt'

__tokens = {151: ("python:getattr(view.field, 'output_mime_type', None) == 'text/x-html-safe'", 4, 33), 282: ('view/id', 6, 29), 322: (' view/klas', 7, 31), 365: ('e view/sty', 8, 30), 408: ('le view/ti', 9, 29), 450: ('ang view/', 10, 27), 494: ('lick view/on', 11, 29), 544: ('click view/ondb', 12, 31), 598: ('sedown view/onmo', 13, 31), 651: ('mouseup view/o', 14, 28), 704: ('ouseover view/on', 15, 29), 759: ('mousemove view/o', 16, 28), 813: ('onmouseout view', 17, 26), 866: (' onkeypress vie', 18, 25), 918: ('   onkeydown v', 19, 23), 967: ('      onkeyu', 20, 20), 1027: ('view/value', 21, 21), 1077: ('safe_structure', 22, 27), 1124: ('view/value', 23, 31), 1193: ('not: safe_structure', 25, 23), 1235: ('view/value', 26, 21)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4474799872 = {}
_static_4559629104 = {'id': '', 'class': '', 'style': 'view/style', 'title': 'view/title', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', }
_static_4474873376 = __C2ZContextWrapper
_static_4474870304 = __compile_zt_expr
_static_4559914320 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x10fcac550> name=None at 10fcaeda0> -> __attrs_4559620944
            __attrs_4559620944 = _static_4559914320
            __backup_safe_structure_4556978064 = get('safe_structure', __marker)

            # <Value "python:getattr(view.field, 'output_mime_type', None) == 'text/x-html-safe'" (4:33)> -> __value
            __token = 151
            try:
                __zt_tmp = __attrs_4559620944
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4474870304('python', "getattr(view.field, 'output_mime_type', None) == 'text/x-html-safe'", econtext=econtext)(_static_4474873376(econtext, __zt_tmp))
            econtext['safe_structure'] = __value
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x10fc66b30> name=None at 10fc66b60> -> __attrs_4559633904
            __attrs_4559633904 = _static_4559629104

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span')

            # <Symbol value=<DEFAULT> at 10ab82140> -> __default_4559630160
            __default_4559630160 = _DEFAULT_MARKER

            # <Substitution 'view/id' (6:29)> -> __attr_id
            __token = 282
            try:
                __zt_tmp = __attrs_4559633904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_4474870304('path', 'view/id', econtext=econtext)(_static_4474873376(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 10ab82140> -> __default_4559618256
            __default_4559618256 = _DEFAULT_MARKER

            # <Substitution 'view/klass' (7:31)> -> __attr_class
            __token = 322
            try:
                __zt_tmp = __attrs_4559633904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4474870304('path', 'view/klass', econtext=econtext)(_static_4474873376(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 10ab82140> -> __default_4559632176
            __default_4559632176 = _DEFAULT_MARKER

            # <Substitution 'view/style' (8:30)> -> __attr_style
            __token = 365
            try:
                __zt_tmp = __attrs_4559633904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_4474870304('path', 'view/style', econtext=econtext)(_static_4474873376(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 10ab82140> -> __default_4559619552
            __default_4559619552 = _DEFAULT_MARKER

            # <Substitution 'view/title' (9:29)> -> __attr_title
            __token = 408
            try:
                __zt_tmp = __attrs_4559633904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_4474870304('path', 'view/title', econtext=econtext)(_static_4474873376(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 10ab82140> -> __default_4559630112
            __default_4559630112 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (10:27)> -> __attr_lang
            __token = 450
            try:
                __zt_tmp = __attrs_4559633904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_4474870304('path', 'view/lang', econtext=econtext)(_static_4474873376(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 10ab82140> -> __default_4559632320
            __default_4559632320 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (11:29)> -> __attr_onclick
            __token = 494
            try:
                __zt_tmp = __attrs_4559633904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_4474870304('path', 'view/onclick', econtext=econtext)(_static_4474873376(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 10ab82140> -> __default_4559632464
            __default_4559632464 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (12:31)> -> __attr_ondblclick
            __token = 544
            try:
                __zt_tmp = __attrs_4559633904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_4474870304('path', 'view/ondblclick', econtext=econtext)(_static_4474873376(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 10ab82140> -> __default_4559632224
            __default_4559632224 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (13:31)> -> __attr_onmousedown
            __token = 598
            try:
                __zt_tmp = __attrs_4559633904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_4474870304('path', 'view/onmousedown', econtext=econtext)(_static_4474873376(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 10ab82140> -> __default_4559620656
            __default_4559620656 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (14:28)> -> __attr_onmouseup
            __token = 651
            try:
                __zt_tmp = __attrs_4559633904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_4474870304('path', 'view/onmouseup', econtext=econtext)(_static_4474873376(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 10ab82140> -> __default_4559631600
            __default_4559631600 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (15:29)> -> __attr_onmouseover
            __token = 704
            try:
                __zt_tmp = __attrs_4559633904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_4474870304('path', 'view/onmouseover', econtext=econtext)(_static_4474873376(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 10ab82140> -> __default_4559630784
            __default_4559630784 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (16:28)> -> __attr_onmousemove
            __token = 759
            try:
                __zt_tmp = __attrs_4559633904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_4474870304('path', 'view/onmousemove', econtext=econtext)(_static_4474873376(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 10ab82140> -> __default_4559631216
            __default_4559631216 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (17:26)> -> __attr_onmouseout
            __token = 813
            try:
                __zt_tmp = __attrs_4559633904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_4474870304('path', 'view/onmouseout', econtext=econtext)(_static_4474873376(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 10ab82140> -> __default_4559630496
            __default_4559630496 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (18:25)> -> __attr_onkeypress
            __token = 866
            try:
                __zt_tmp = __attrs_4559633904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_4474870304('path', 'view/onkeypress', econtext=econtext)(_static_4474873376(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 10ab82140> -> __default_4559619024
            __default_4559619024 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (19:23)> -> __attr_onkeydown
            __token = 918
            try:
                __zt_tmp = __attrs_4559633904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_4474870304('path', 'view/onkeydown', econtext=econtext)(_static_4474873376(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 10ab82140> -> __default_4559633472
            __default_4559633472 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (20:20)> -> __attr_onkeyup
            __token = 967
            try:
                __zt_tmp = __attrs_4559633904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_4474870304('path', 'view/onkeyup', econtext=econtext)(_static_4474873376(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))
            __append('>')

            # <Static value=<ast.Dict object at 0x10ab80700> name=None at 10ab80f40> -> __attrs_4559866896
            __attrs_4559866896 = _static_4474799872

            # <Value 'view/value' (21:21)> -> __condition
            __token = 1027
            try:
                __zt_tmp = __attrs_4559866896
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4474870304('path', 'view/value', econtext=econtext)(_static_4474873376(econtext, __zt_tmp))
            if __condition:

                # <Static value=<ast.Dict object at 0x10ab80700> name=None at 10ab80f40> -> __attrs_4559874432
                __attrs_4559874432 = _static_4474799872

                # <Value 'safe_structure' (22:27)> -> __condition
                __token = 1077
                try:
                    __zt_tmp = __attrs_4559874432
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4474870304('path', 'safe_structure', econtext=econtext)(_static_4474873376(econtext, __zt_tmp))
                if __condition:

                    # <Symbol value=<DEFAULT> at 10ab82140> -> __default_4559874096
                    __default_4559874096 = _DEFAULT_MARKER

                    # <Value 'view/value' (23:31)> -> __cache_4559870208
                    __token = 1124
                    try:
                        __zt_tmp = __attrs_4559874432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4559870208 = _static_4474870304('path', 'view/value', econtext=econtext)(_static_4474873376(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/value' (23:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 10ab82140> at 10fca2590> -> __condition
                    __expression = __cache_4559870208

                    # <Symbol value=<DEFAULT> at 10ab82140> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4559870208
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)

                # <Static value=<ast.Dict object at 0x10ab80700> name=None at 10ab80f40> -> __attrs_4559873184
                __attrs_4559873184 = _static_4474799872

                # <Value 'not: safe_structure' (25:23)> -> __condition
                __token = 1193
                try:
                    __zt_tmp = __attrs_4559873184
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4474870304('not', ' safe_structure', econtext=econtext)(_static_4474873376(econtext, __zt_tmp))
                if __condition:

                    # <Symbol value=<DEFAULT> at 10ab82140> -> __default_4559873712
                    __default_4559873712 = _DEFAULT_MARKER

                    # <Value 'view/value' (26:21)> -> __cache_4559872848
                    __token = 1235
                    try:
                        __zt_tmp = __attrs_4559873184
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4559872848 = _static_4474870304('path', 'view/value', econtext=econtext)(_static_4474873376(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/value' (26:21)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 10ab82140> at 10fca07f0> -> __condition
                    __expression = __cache_4559872848

                    # <Symbol value=<DEFAULT> at 10ab82140> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4559872848
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
            __append('</span>\n')
            if (__backup_safe_structure_4556978064 is __marker):
                del econtext['safe_structure']
            else:
                econtext['safe_structure'] = __backup_safe_structure_4556978064
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }