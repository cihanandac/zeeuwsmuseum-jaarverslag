# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/viewlets/logo.pt'

__tokens = {110: (' view/navigation_root_titl', 4, 24), 60: ('view/navigation_root_url', 3, 24), 341: ('c view/img_s', 10, 27), 249: ('view/logo_title', 8, 23), 296: (' view/logo_titl', 9, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4981915504 = {'src': 'plone-logo.svg', 'alt': '', 'title': 'view/logo_title', }
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4981906240 = {'id': 'portal-logo', 'title': 'Home', 'href': 'view/navigation_root_url', }

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

            # <Static value=<ast.Dict object at 0x128f1db40> name=None at 128f1d8a0> -> __attrs_4981909984
            __attrs_4981909984 = _static_4981906240
            __previous_i18n_domain_4981912048 = __i18n_domain
            __i18n_domain = 'plone'

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a id="portal-logo"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981906096
            __default_4981906096 = _DEFAULT_MARKER

            # <Translate msgid=None node=<Substitution 'view/navigation_root_title' (4:24)> at 128f1d060> -> __attr_title

            # <Substitution 'view/navigation_root_title' (4:24)> -> __attr_title
            __token = 110
            try:
                __zt_tmp = __attrs_4981909984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_4754050160('path', 'view/navigation_root_title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', 'Home', _DEFAULT_MARKER)
            __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981910176
            __default_4981910176 = _DEFAULT_MARKER

            # <Substitution 'view/navigation_root_url' (3:24)> -> __attr_href
            __token = 60
            try:
                __zt_tmp = __attrs_4981909984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4754050160('path', 'view/navigation_root_url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append('>\n   ')

            # <Static value=<ast.Dict object at 0x128f1ff70> name=None at 128f1ee30> -> __attrs_4981912096
            __attrs_4981912096 = _static_4981915504

            # <img ... (0:0)
            # --------------------------------------------------------
            __append('<img')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981910128
            __default_4981910128 = _DEFAULT_MARKER

            # <Substitution 'view/img_src' (10:27)> -> __attr_src
            __token = 341
            try:
                __zt_tmp = __attrs_4981912096
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_4754050160('path', 'view/img_src', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', 'plone-logo.svg', _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((' src="%s"' % __attr_src))

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981900288
            __default_4981900288 = _DEFAULT_MARKER

            # <Substitution 'view/logo_title' (8:23)> -> __attr_alt
            __token = 249
            try:
                __zt_tmp = __attrs_4981912096
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_alt = _static_4754050160('path', 'view/logo_title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_alt is not None):
                __append((' alt="%s"' % __attr_alt))

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981908592
            __default_4981908592 = _DEFAULT_MARKER

            # <Substitution 'view/logo_title' (9:30)> -> __attr_title
            __token = 296
            try:
                __zt_tmp = __attrs_4981912096
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_4754050160('path', 'view/logo_title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append(' /></a>')
            __i18n_domain = __previous_i18n_domain_4981912048
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }