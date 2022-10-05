# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/links/rsslink.pt'

__tokens = {28: ('view/rsslinks', 1, 28), 162: ('link/url', 4, 31), 203: (' link/titl', 5, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4771512384 = {'rel': 'alternate', 'href': '', 'title': 'RSS 1.0', 'type': 'application/rss+xml', }
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

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982185344
            __attrs_4982185344 = _static_4753720080
            __backup_link_4771664736 = get('link', __marker)

            # <Value 'view/rsslinks' (1:28)> -> __iterator
            __token = 28
            try:
                __zt_tmp = __attrs_4982185344
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4754050160('path', 'view/rsslinks', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            (__iterator, ____index_4982185584, ) = getname('repeat')('link', __iterator)
            econtext['link'] = None
            for __item in __iterator:
                econtext['link'] = __item
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x11c678040> name=None at 11c62ff40> -> __attrs_4982179296
                __attrs_4982179296 = _static_4771512384

                # <link ... (0:0)
                # --------------------------------------------------------
                __append('<link rel="alternate"')

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982188992
                __default_4982188992 = _DEFAULT_MARKER

                # <Substitution 'link/url' (4:31)> -> __attr_href
                __token = 162
                try:
                    __zt_tmp = __attrs_4982179296
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4754050160('path', 'link/url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982184864
                __default_4982184864 = _DEFAULT_MARKER

                # <Substitution 'link/title' (5:31)> -> __attr_title
                __token = 203
                try:
                    __zt_tmp = __attrs_4982179296
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_title = _static_4754050160('path', 'link/title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                __attr_title = __quote(__attr_title, '"', '&quot;', 'RSS 1.0', _DEFAULT_MARKER)
                if (__attr_title is not None):
                    __append((' title="%s"' % __attr_title))
                __append(' type="application/rss+xml" />\n')
                ____index_4982185584 -= 1
                if (____index_4982185584 > 0):
                    __append('')
            if (__backup_link_4771664736 is __marker):
                del econtext['link']
            else:
                econtext['link'] = __backup_link_4771664736
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }