# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/Products/Five/utilities/browser/manage_interfaces.pt'

__tokens = {27: ('context/manage_page_header', 1, 27), 99: ('context/manage_tabs', 2, 27), 193: ('context/@@edit-markers.html/main', 6, 30), 193: ('context/@@edit-markers.html/main', 6, 30), 267: ('context/manage_page_footer', 10, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4902165552 = 'main'
_static_4902159312 = {'class': 'container-fluid', }
_static_4439051040 = __C2ZContextWrapper
_static_4439058528 = __compile_zt_expr
_static_4438893776 = {}

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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4902168000
            __attrs_4902168000 = _static_4438893776

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4902171504
            __default_4902171504 = _DEFAULT_MARKER

            # <Value 'context/manage_page_header' (1:27)> -> __cache_4902165648
            __token = 27
            try:
                __zt_tmp = __attrs_4902168000
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4902165648 = _static_4439058528('path', 'context/manage_page_header', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/manage_page_header' (1:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1243111b0> -> __condition
            __expression = __cache_4902165648

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>PAGE HEADER</h1>')
            else:
                __content = __cache_4902165648
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4902171696
            __attrs_4902171696 = _static_4438893776

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4902160080
            __default_4902160080 = _DEFAULT_MARKER

            # <Value 'context/manage_tabs' (2:27)> -> __cache_4902159840
            __token = 99
            try:
                __zt_tmp = __attrs_4902171696
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4902159840 = _static_4439058528('path', 'context/manage_tabs', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/manage_tabs' (2:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1243108e0> -> __condition
            __expression = __cache_4902159840

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2>TABS</h2>')
            else:
                __content = __cache_4902159840
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x1243103d0> name=None at 1243112a0> -> __attrs_4902158784
            __attrs_4902158784 = _static_4902159312

            # <main ... (0:0)
            # --------------------------------------------------------
            __append('<main class="container-fluid">\n\n')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4902170592
            __attrs_4902170592 = _static_4438893776
            __backup_macroname_4903475968 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x124311c30> name=None at 124311b70> -> __value
            __value = _static_4902165552
            econtext['macroname'] = __value

            # <Value 'context/@@edit-markers.html/main' (6:30)> -> __macro
            __token = 193
            try:
                __zt_tmp = __attrs_4902170592
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4439058528('path', 'context/@@edit-markers.html/main', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __token = 193
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4903475968 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4903475968
            __append('\n\n</main>\n\n')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4902160656
            __attrs_4902160656 = _static_4438893776

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4902173232
            __default_4902173232 = _DEFAULT_MARKER

            # <Value 'context/manage_page_footer' (10:27)> -> __cache_4902169248
            __token = 267
            try:
                __zt_tmp = __attrs_4902160656
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4902169248 = _static_4439058528('path', 'context/manage_page_footer', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/manage_page_footer' (10:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1243115a0> -> __condition
            __expression = __cache_4902169248

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>PAGE FOOTER</h1>')
            else:
                __content = __cache_4902169248
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }