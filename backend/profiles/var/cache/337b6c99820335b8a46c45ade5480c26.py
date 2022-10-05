# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/viewlets/social_tags.pt'

__tokens = {22: ('view/tags', 1, 22), 49: ('tag', 1, 49)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info

_static_4982187264 = set([])
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

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982180736
            __attrs_4982180736 = _static_4753720080
            __backup_tag_4974774112 = get('tag', __marker)

            # <Value 'view/tags' (1:22)> -> __iterator
            __token = 22
            try:
                __zt_tmp = __attrs_4982180736
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4754050160('path', 'view/tags', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            (__iterator, ____index_4982180208, ) = getname('repeat')('tag', __iterator)
            econtext['tag'] = None
            for __item in __iterator:
                econtext['tag'] = __item

                # <meta ... (0:0)
                # --------------------------------------------------------
                __append('<meta')

                # <Value 'tag' (1:49)> -> __cache_4982181648
                __token = 49
                try:
                    __zt_tmp = __attrs_4982180736
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4982181648 = _static_4754050160('path', 'tag', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                __attr_4982181504 = __cache_4982181648
                for (name, value, ) in __attr_4982181504.items():
                    if ((name not in _static_4982187264) and (value is not None)):
                        __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
                __append(' />')
                ____index_4982180208 -= 1
                if (____index_4982180208 > 0):
                    __append('\n')
            if (__backup_tag_4974774112 is __marker):
                del econtext['tag']
            else:
                econtext['tag'] = __backup_tag_4974774112
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }