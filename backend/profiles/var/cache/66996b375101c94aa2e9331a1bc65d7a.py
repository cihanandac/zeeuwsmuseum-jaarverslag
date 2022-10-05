# -*- coding: utf-8 -*-
__filename = 'index_html'

__tokens = {56: ('template/title', 4, 24), 170: ('context/title_or_id', 9, 27), 247: ('template/title', 10, 29), 290: ('template/title', 11, 27), 386: ('template/id', 13, 43)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4799912480 = {'charset': 'utf-8', }
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4753720080 = {}

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
            __append('<!DOCTYPE html>\n')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4799906480
            __attrs_4799906480 = _static_4753720080

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html>\n  ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4799909792
            __attrs_4799909792 = _static_4753720080

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n    ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4799911136
            __attrs_4799911136 = _static_4753720080

            # <title ... (0:0)
            # --------------------------------------------------------
            __append('<title>')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4799910608
            __default_4799910608 = _DEFAULT_MARKER

            # <Value 'template/title' (4:24)> -> __cache_4799910128
            __token = 56
            try:
                __zt_tmp = __attrs_4799911136
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4799910128 = _static_4754050160('path', 'template/title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

            # <BinOp left=<Value 'template/title' (4:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 11e18d1b0> -> __condition
            __expression = __cache_4799910128

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('The title')
            else:
                __content = __cache_4799910128
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</title>\n    ')

            # <Static value=<ast.Dict object at 0x11e18da20> name=None at 11e18da50> -> __attrs_4799912384
            __attrs_4799912384 = _static_4799912480

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta charset="utf-8" />\n  </head>\n  ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4799913152
            __attrs_4799913152 = _static_4753720080

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n    \n    ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4799914304
            __attrs_4799914304 = _static_4753720080

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append('<h2>')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4799915792
            __attrs_4799915792 = _static_4753720080

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4799915600
            __default_4799915600 = _DEFAULT_MARKER

            # <Value 'context/title_or_id' (9:27)> -> __cache_4799915120
            __token = 170
            try:
                __zt_tmp = __attrs_4799915792
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4799915120 = _static_4754050160('path', 'context/title_or_id', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/title_or_id' (9:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 11e18e530> -> __condition
            __expression = __cache_4799915120

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>content title or id</span>')
            else:
                __content = __cache_4799915120
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4799917328
            __attrs_4799917328 = _static_4753720080

            # <Value 'template/title' (10:29)> -> __condition
            __token = 247
            try:
                __zt_tmp = __attrs_4799917328
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('path', 'template/title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4799917136
                __default_4799917136 = _DEFAULT_MARKER

                # <Value 'template/title' (11:27)> -> __cache_4799916656
                __token = 290
                try:
                    __zt_tmp = __attrs_4799917328
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4799916656 = _static_4754050160('path', 'template/title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                # <BinOp left=<Value 'template/title' (11:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 11e18eb30> -> __condition
                __expression = __cache_4799916656

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>optional template title</span>')
                else:
                    __content = __cache_4799916656
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
            __append('</h2>\n\n    This is Page Template ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4799918864
            __attrs_4799918864 = _static_4753720080

            # <em ... (0:0)
            # --------------------------------------------------------
            __append('<em>')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4799918288
            __default_4799918288 = _DEFAULT_MARKER

            # <Value 'template/id' (13:43)> -> __cache_4799917520
            __token = 386
            try:
                __zt_tmp = __attrs_4799918864
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4799917520 = _static_4754050160('path', 'template/id', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

            # <BinOp left=<Value 'template/id' (13:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 11e18efb0> -> __condition
            __expression = __cache_4799917520

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('template id')
            else:
                __content = __cache_4799917520
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</em>.\n  </body>\n</html>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }