# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/analytics/view.pt'

__tokens = {55: ('view/webstats_js', 2, 29), 93: ('webstats_js', 3, 20), 134: ('webstats_js', 4, 28)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4760149520 = {'id': 'plone-analytics', }

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

            # <Static value=<ast.Dict object at 0x11bba1e10> name=None at 11bba0f10> -> __attrs_4760143808
            __attrs_4760143808 = _static_4760149520
            __backup_webstats_js_4974688672 = get('webstats_js', __marker)

            # <Value 'view/webstats_js' (2:29)> -> __value
            __token = 55
            try:
                __zt_tmp = __attrs_4760143808
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/webstats_js', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['webstats_js'] = __value

            # <Value 'webstats_js' (3:20)> -> __condition
            __token = 93
            try:
                __zt_tmp = __attrs_4760143808
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('path', 'webstats_js', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="plone-analytics" >')

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4760151200
                __default_4760151200 = _DEFAULT_MARKER

                # <Value 'webstats_js' (4:28)> -> __cache_4760144816
                __token = 134
                try:
                    __zt_tmp = __attrs_4760143808
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4760144816 = _static_4754050160('path', 'webstats_js', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                # <BinOp left=<Value 'webstats_js' (4:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 11bba1b10> -> __condition
                __expression = __cache_4760144816

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n  Here goes the webstats_js\n')
                else:
                    __content = __cache_4760144816
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('</div>')
            if (__backup_webstats_js_4974688672 is __marker):
                del econtext['webstats_js']
            else:
                econtext['webstats_js'] = __backup_webstats_js_4974688672
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }