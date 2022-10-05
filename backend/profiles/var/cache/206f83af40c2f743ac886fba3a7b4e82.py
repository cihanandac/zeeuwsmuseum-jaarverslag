# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/viewlets/anontools.pt'

__tokens = {42: ('python:view.user_actions and view.anonymous', 1, 42), 167: ('view/user_actions', 3, 52), 230: ('action', 5, 26), 261: ('action/title', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4975253136 = set([])
_static_4982503504 = {'href': '', }
_static_4982493472 = {'class': 'list-inline-item', }
_static_4982496304 = {'class': 'list-inline', }
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4982497888 = {'id': 'portal-anontools', }

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

            # <Static value=<ast.Dict object at 0x128fae260> name=None at 128f63e50> -> __attrs_4982502064
            __attrs_4982502064 = _static_4982497888

            # <Value 'python:view.user_actions and view.anonymous' (1:42)> -> __condition
            __token = 42
            try:
                __zt_tmp = __attrs_4982502064
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('python', 'view.user_actions and view.anonymous', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="portal-anontools">\n  ')

                # <Static value=<ast.Dict object at 0x128fadc30> name=None at 128faf910> -> __attrs_4982493616
                __attrs_4982493616 = _static_4982496304

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="list-inline">\n    ')

                # <Static value=<ast.Dict object at 0x128fad120> name=None at 128fac8b0> -> __attrs_4982496160
                __attrs_4982496160 = _static_4982493472
                __backup_action_4975066656 = get('action', __marker)

                # <Value 'view/user_actions' (3:52)> -> __iterator
                __token = 167
                try:
                    __zt_tmp = __attrs_4982496160
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4754050160('path', 'view/user_actions', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                (__iterator, ____index_4982505184, ) = getname('repeat')('action', __iterator)
                econtext['action'] = None
                for __item in __iterator:
                    econtext['action'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="list-inline-item">\n      ')

                    # <Static value=<ast.Dict object at 0x128faf850> name=None at 128faec20> -> __attrs_4982489920
                    __attrs_4982489920 = _static_4982503504

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Value 'action' (5:26)> -> __cache_4982502688
                    __token = 230
                    try:
                        __zt_tmp = __attrs_4982489920
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4982502688 = _static_4754050160('path', 'action', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    if ('href' not in __chain(__cache_4982502688)):
                        __append(' href=""')
                    __attr_4982504656 = __cache_4982502688
                    for (name, value, ) in __attr_4982504656.items():
                        if ((name not in _static_4975253136) and (value is not None)):
                            __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982495728
                    __default_4982495728 = _DEFAULT_MARKER

                    # <Value 'action/title' (6:23)> -> __cache_4982497024
                    __token = 261
                    try:
                        __zt_tmp = __attrs_4982489920
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4982497024 = _static_4754050160('path', 'action/title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'action/title' (6:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128fafa90> -> __condition
                    __expression = __cache_4982497024

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n          action title\n      ')
                    else:
                        __content = __cache_4982497024
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</a>\n    </li>')
                    ____index_4982505184 -= 1
                    if (____index_4982505184 > 0):
                        __append('\n    ')
                if (__backup_action_4975066656 is __marker):
                    del econtext['action']
                else:
                    econtext['action'] = __backup_action_4975066656
                __append('\n  </ul>\n</div>')
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }