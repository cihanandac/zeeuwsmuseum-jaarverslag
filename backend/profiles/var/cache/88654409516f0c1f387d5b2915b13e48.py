# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/viewlets/toc.pt'

__tokens = {104: ('view/enabled', 2, 19)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info

_static_4982044608 = {'class': 'portletItem', }
_static_4982046240 = {'class': 'portletContent', }
_static_4982035152 = {'class': 'portletHeader', }
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4982041296 = {'id': 'document-toc', 'class': 'portlet toc', 'role': 'section', 'style': 'display: none', }

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

            # <Static value=<ast.Dict object at 0x128f3ead0> name=None at 128f3f010> -> __attrs_4982031216
            __attrs_4982031216 = _static_4982041296

            # <Value 'view/enabled' (2:19)> -> __condition
            __token = 104
            try:
                __zt_tmp = __attrs_4982031216
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('path', 'view/enabled', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4982035968 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="document-toc" class="portlet toc"  role="section" style="display: none">\n  ')

                # <Static value=<ast.Dict object at 0x128f3d2d0> name=None at 128f3fdc0> -> __attrs_4982044080
                __attrs_4982044080 = _static_4982035152

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="portletHeader">')
                __stream_4982041056 = []
                __append_4982041056 = __stream_4982041056.append
                __append_4982041056('Contents')
                __msgid_4982041056 = __re_whitespace(''.join(__stream_4982041056)).strip()
                if 'label_tableofcontents':
                    __append(translate('label_tableofcontents', mapping=None, default=__msgid_4982041056, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n  ')

                # <Static value=<ast.Dict object at 0x128f3fe20> name=None at 128f3d540> -> __attrs_4982042688
                __attrs_4982042688 = _static_4982046240

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section class="portletContent">\n\t  ')

                # <Static value=<ast.Dict object at 0x128f3f7c0> name=None at 128f3d2a0> -> __attrs_4982041632
                __attrs_4982041632 = _static_4982044608

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="portletItem">\n\t  </div>\n  </section>\n</section>')
                __i18n_domain = __previous_i18n_domain_4982035968
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }