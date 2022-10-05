# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/viewlets/dublin_core.pt'

__tokens = {25: ('view/metatags', 1, 25), 67: ('python:keyval[0]', 2, 27), 92: (' python:keyval[1', 2, 52)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4982399344 = {'name': 'python:keyval[0]', 'content': 'python:keyval[1]', }

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

            # <Static value=<ast.Dict object at 0x128f96170> name=None at 128f96230> -> __attrs_4982403712
            __attrs_4982403712 = _static_4982399344
            __backup_keyval_4982518256 = get('keyval', __marker)

            # <Value 'view/metatags' (1:25)> -> __iterator
            __token = 25
            try:
                __zt_tmp = __attrs_4982403712
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4754050160('path', 'view/metatags', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            (__iterator, ____index_4982403424, ) = getname('repeat')('keyval', __iterator)
            econtext['keyval'] = None
            for __item in __iterator:
                econtext['keyval'] = __item

                # <meta ... (0:0)
                # --------------------------------------------------------
                __append('<meta')

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982404336
                __default_4982404336 = _DEFAULT_MARKER

                # <Substitution 'python:keyval[0]' (2:27)> -> __attr_name
                __token = 67
                try:
                    __zt_tmp = __attrs_4982403712
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_4754050160('python', 'keyval[0]', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982399632
                __default_4982399632 = _DEFAULT_MARKER

                # <Substitution 'python:keyval[1]' (2:52)> -> __attr_content
                __token = 92
                try:
                    __zt_tmp = __attrs_4982403712
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_content = _static_4754050160('python', 'keyval[1]', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                __attr_content = __quote(__attr_content, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_content is not None):
                    __append((' content="%s"' % __attr_content))
                __append(' />')
                ____index_4982403424 -= 1
                if (____index_4982403424 > 0):
                    __append('\n')
            if (__backup_keyval_4982518256 is __marker):
                del econtext['keyval']
            else:
                econtext['keyval'] = __backup_keyval_4982518256
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }