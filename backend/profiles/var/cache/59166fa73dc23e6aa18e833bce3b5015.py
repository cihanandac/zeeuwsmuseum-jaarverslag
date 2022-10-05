# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/portlets/portlets/classic.pt'

__tokens = {33: ('view/use_macro', 1, 33), 87: (' view/path_expressio', 2, 38), 136: ('use_macro', 4, 24), 182: ('python:path(path_expression)', 5, 34), 182: ('python:path(path_expression)', 5, 34), 255: ('not:use_macro', 8, 24), 303: ('python:path(path_expression)', 9, 32)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4982394592 = 'python:path(path_expression)'
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

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4981128352
            __attrs_4981128352 = _static_4753720080
            __backup_use_macro_4982399344 = get('use_macro', __marker)

            # <Value 'view/use_macro' (1:33)> -> __value
            __token = 33
            try:
                __zt_tmp = __attrs_4981128352
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/use_macro', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['use_macro'] = __value
            __backup_path_expression_4982391424 = get('path_expression', __marker)

            # <Value 'view/path_expression' (2:38)> -> __value
            __token = 87
            try:
                __zt_tmp = __attrs_4981128352
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/path_expression', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['path_expression'] = __value
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982401264
            __attrs_4982401264 = _static_4753720080

            # <Value 'use_macro' (4:24)> -> __condition
            __token = 136
            try:
                __zt_tmp = __attrs_4982401264
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('path', 'use_macro', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982393920
                __attrs_4982393920 = _static_4753720080
                __backup_macroname_4759636928 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x128f94ee0> name=None at 128f96b00> -> __value
                __value = _static_4982394592
                econtext['macroname'] = __value

                # <Value 'python:path(path_expression)' (5:34)> -> __macro
                __token = 182
                try:
                    __zt_tmp = __attrs_4982393920
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_4754050160('python', 'path(path_expression)', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                __token = 182
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_4759636928 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_4759636928
                __append('\n  ')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982397424
            __attrs_4982397424 = _static_4753720080

            # <Value 'not:use_macro' (8:24)> -> __condition
            __token = 255
            try:
                __zt_tmp = __attrs_4982397424
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('not', 'use_macro', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982395888
                __attrs_4982395888 = _static_4753720080

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982394640
                __default_4982394640 = _DEFAULT_MARKER

                # <Value 'python:path(path_expression)' (9:32)> -> __cache_4982400544
                __token = 303
                try:
                    __zt_tmp = __attrs_4982395888
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4982400544 = _static_4754050160('python', 'path(path_expression)', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:path(path_expression)' (9:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f95b40> -> __condition
                __expression = __cache_4982400544

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div />')
                else:
                    __content = __cache_4982400544
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n  ')
            __append('\n\n')
            if (__backup_path_expression_4982391424 is __marker):
                del econtext['path_expression']
            else:
                econtext['path_expression'] = __backup_path_expression_4982391424
            if (__backup_use_macro_4982399344 is __marker):
                del econtext['use_macro']
            else:
                econtext['use_macro'] = __backup_use_macro_4982399344
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }