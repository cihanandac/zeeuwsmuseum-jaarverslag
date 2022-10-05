# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/links/favicon.pt'

__tokens = {49: ('${python: view.mimetype}', 2, 35), 51: ('python: view.mimetype', 2, 37), 106: ('python: view.favicon_path', 3, 31), 183: ('python: view.favicon_path', 4, 47)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4981792944 = {'rel': 'mask-icon', 'href': 'python: view.favicon_path', }
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4981794048 = {'rel': 'preload icon', 'type': '${python: view.mimetype}', 'href': 'python: view.favicon_path', }
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

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4981799328
            __attrs_4981799328 = _static_4753720080
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x128f02500> name=None at 128f02560> -> __attrs_4981789920
            __attrs_4981789920 = _static_4981794048

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="preload icon"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981797888
            __default_4981797888 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${python: view.mimetype}' (2:35)> braces_required=True translation=False default='"?"' default_marker='"?"' at 128f02a40> -> __attr_type
            __token = 49
            __token = 51
            try:
                __zt_tmp = __attrs_4981789920
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_type = _static_4754050160('python', ' view.mimetype', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_type = __quote(__attr_type, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_type = __attr_type
            if (__attr_type is None):
                pass
            else:
                if (__attr_type is _DEFAULT_MARKER):
                    __attr_type = None
                else:
                    __tt = type(__attr_type)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_type = str(__attr_type)
                    else:
                        if (__tt is bytes):
                            __attr_type = decode(__attr_type)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_type = __attr_type.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_type)
                                    __attr_type = (str(__attr_type) if (__attr_type is __converted) else __converted)
                                else:
                                    __attr_type = __attr_type()
            if (__attr_type is not None):
                __append((' type="%s"' % __attr_type))

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981788672
            __default_4981788672 = _DEFAULT_MARKER

            # <Substitution 'python: view.favicon_path' (3:31)> -> __attr_href
            __token = 106
            try:
                __zt_tmp = __attrs_4981789920
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4754050160('python', ' view.favicon_path', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' />\n    ')

            # <Static value=<ast.Dict object at 0x128f020b0> name=None at 128f03c40> -> __attrs_4981796496
            __attrs_4981796496 = _static_4981792944

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="mask-icon"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981795008
            __default_4981795008 = _DEFAULT_MARKER

            # <Substitution 'python: view.favicon_path' (4:47)> -> __attr_href
            __token = 183
            try:
                __zt_tmp = __attrs_4981796496
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4754050160('python', ' view.favicon_path', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' />\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }