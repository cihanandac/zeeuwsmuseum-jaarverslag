# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/batching/batch_macros.pt'

__tokens = {314: ('batch|nothing', 10, 23), 359: (' batchformkeys|nothin', 11, 30), 447: ('nocall:context/@@batchnavigation', 14, 36), 512: ('python:batchnavigation(batch, batchformkeys)', 15, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4905525712 = {'xmlns': 'http://www.w3.org/1999/xhtml', }
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
_static_4428767312 = {}

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

    def render_navigation(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4905525952
            __attrs_4905525952 = _static_4428767312
            __backup_batch_4905476368 = get('batch', __marker)

            # <Value 'batch|nothing' (10:23)> -> __value
            __token = 314
            try:
                __zt_tmp = __attrs_4905525952
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'batch|nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['batch'] = __value
            __backup_batchformkeys_4905484144 = get('batchformkeys', __marker)

            # <Value 'batchformkeys|nothing' (11:30)> -> __value
            __token = 359
            try:
                __zt_tmp = __attrs_4905525952
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'batchformkeys|nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['batchformkeys'] = __value
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4905530032
            __attrs_4905530032 = _static_4428767312
            __backup_batchnavigation_4905474928 = get('batchnavigation', __marker)

            # <Value 'nocall:context/@@batchnavigation' (14:36)> -> __value
            __token = 447
            try:
                __zt_tmp = __attrs_4905530032
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('nocall', 'context/@@batchnavigation', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['batchnavigation'] = __value

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4905521920
            __default_4905521920 = _DEFAULT_MARKER

            # <Value 'python:batchnavigation(batch, batchformkeys)' (15:31)> -> __cache_4905517456
            __token = 512
            try:
                __zt_tmp = __attrs_4905530032
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4905517456 = _static_4427992992('python', 'batchnavigation(batch, batchformkeys)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'python:batchnavigation(batch, batchformkeys)' (15:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 124644940> -> __condition
            __expression = __cache_4905517456

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4905517456
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            if (__backup_batchnavigation_4905474928 is __marker):
                del econtext['batchnavigation']
            else:
                econtext['batchnavigation'] = __backup_batchnavigation_4905474928
            __append('\n\n')
            if (__backup_batchformkeys_4905484144 is __marker):
                del econtext['batchformkeys']
            else:
                econtext['batchformkeys'] = __backup_batchformkeys_4905484144
            if (__backup_batch_4905476368 is __marker):
                del econtext['batch']
            else:
                econtext['batch'] = __backup_batch_4905476368
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

            # <Static value=<ast.Dict object at 0x1246461d0> name=None at 124644a90> -> __attrs_4905523888
            __attrs_4905523888 = _static_4905525712
            __previous_i18n_domain_4905523072 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml">\n')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4905531664
            __attrs_4905531664 = _static_4428767312

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n\n')
            __token = None
            render_navigation(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n</body>\n</html>')
            __i18n_domain = __previous_i18n_domain_4905523072
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_navigation': render_navigation, 'render': render, }