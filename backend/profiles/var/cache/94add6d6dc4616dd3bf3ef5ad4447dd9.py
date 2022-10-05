# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/links/author.pt'

__tokens = {185: ('view/navigation_root_url', 4, 37), 419: ('string:${navigation_root_url}/author/${context/Creator|nothing}', 11, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4982216384 = {'rel': 'author', 'href': '', 'title': 'Author information', }
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4982211392 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x128f68340> name=None at 128f686d0> -> __attrs_4982211248
            __attrs_4982211248 = _static_4982211392
            __backup_navigation_root_url_4771673568 = get('navigation_root_url', __marker)

            # <Value 'view/navigation_root_url' (4:37)> -> __value
            __token = 185
            try:
                __zt_tmp = __attrs_4982211248
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/navigation_root_url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['navigation_root_url'] = __value
            __previous_i18n_domain_4982214800 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x128f696c0> name=None at 128f69720> -> __attrs_4982221712
            __attrs_4982221712 = _static_4982216384

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="author"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982215904
            __default_4982215904 = _DEFAULT_MARKER

            # <Substitution 'string:${navigation_root_url}/author/${context/Creator|nothing}' (11:31)> -> __attr_href
            __token = 419
            try:
                __zt_tmp = __attrs_4982221712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4754050160('string', '${navigation_root_url}/author/${context/Creator|nothing}', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982217872
            __default_4982217872 = _DEFAULT_MARKER

            # <Translate msgid='title_author_info' node=<ast.Constant object at 0x128f69b40> at 128f697e0> -> __attr_title
            __attr_title = 'Author information'
            __attr_title = translate('title_author_info', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append(' />\n')
            __i18n_domain = __previous_i18n_domain_4982214800
            if (__backup_navigation_root_url_4771673568 is __marker):
                del econtext['navigation_root_url']
            else:
                econtext['navigation_root_url'] = __backup_navigation_root_url_4771673568
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }