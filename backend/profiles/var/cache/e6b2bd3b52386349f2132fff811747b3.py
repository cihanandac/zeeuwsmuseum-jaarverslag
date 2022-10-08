# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/z3cform/templates/layout.pt'

__tokens = {469: ('view/label', 12, 58), 550: ('view/contents', 13, 58), 261: ('here/main_template/macros/master', 6, 23), 261: ('here/main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4480086464 = 'master'
_static_4480079024 = {'id': 'content-core', }
_static_4417565216 = __C2ZContextWrapper
_static_4417553984 = __compile_zt_expr
_static_4480075232 = {'class': 'documentFirstHeading', }
_static_4418309904 = {}

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

    def render_main(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4480086080
            __attrs_4480086080 = _static_4418309904
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x10b0885e0> name=None at 10b088ee0> -> __attrs_4480088048
            __attrs_4480088048 = _static_4480075232

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1 class="documentFirstHeading">')

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4480085072
            __default_4480085072 = _DEFAULT_MARKER

            # <Value 'view/label' (12:58)> -> __cache_4480086416
            __token = 469
            try:
                __zt_tmp = __attrs_4480088048
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4480086416 = _static_4417553984('path', 'view/label', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/label' (12:58)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107619600> at 10b08bb50> -> __condition
            __expression = __cache_4480086416

            # <Symbol value=<DEFAULT> at 107619600> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('Title')
            else:
                __content = __cache_4480086416
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</h1>\n            ')

            # <Static value=<ast.Dict object at 0x10b0894b0> name=None at 10b08b820> -> __attrs_4480087952
            __attrs_4480087952 = _static_4480079024

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="content-core">')

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4480078736
            __default_4480078736 = _DEFAULT_MARKER

            # <Value 'view/contents' (13:58)> -> __cache_4480087616
            __token = 550
            try:
                __zt_tmp = __attrs_4480087952
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4480087616 = _static_4417553984('path', 'view/contents', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/contents' (13:58)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107619600> at 10b089900> -> __condition
            __expression = __cache_4480087616

            # <Symbol value=<DEFAULT> at 107619600> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4480087616
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n        ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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

            # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4480077968
            __attrs_4480077968 = _static_4418309904
            __previous_i18n_domain_4480087184 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4480353920 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x10b08b1c0> name=None at 10b089600> -> __value
            __value = _static_4480086464
            econtext['macroname'] = __value

            def __fill_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4480083248
                __attrs_4480083248 = _static_4418309904
                __append('\n        ')
                __token = None
                render_main(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n    ')
            _slots = econtext['__slot_main'] = _deque((__fill_main, ))

            # <Value 'here/main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_4480077968
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4417553984('path', 'here/main_template/macros/master', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4480353920 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4480353920
            __i18n_domain = __previous_i18n_domain_4480087184
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_main': render_main, 'render': render, }