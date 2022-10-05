# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/viewlets/document_rights.pt'

__tokens = {87: ('context/Rights', 1, 87), 118: ('rights', 1, 118), 257: ('rights', 7, 24)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4753720080 = {}
_static_4981905040 = {'class': 'section-heading', }
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4981914544 = {'id': 'section-rights', 'class': 'text-muted', }

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

            # <Static value=<ast.Dict object at 0x128f1fbb0> name=None at 128f1ead0> -> __attrs_4981901008
            __attrs_4981901008 = _static_4981914544
            __backup_rights_4981900624 = get('rights', __marker)

            # <Value 'context/Rights' (1:87)> -> __value
            __token = 87
            try:
                __zt_tmp = __attrs_4981901008
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'context/Rights', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['rights'] = __value

            # <Value 'rights' (1:118)> -> __condition
            __token = 118
            try:
                __zt_tmp = __attrs_4981901008
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('path', 'rights', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4981911520 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-rights" class="text-muted">\n\n    ')

                # <Static value=<ast.Dict object at 0x128f1d690> name=None at 128f1c580> -> __attrs_4981912288
                __attrs_4981912288 = _static_4981905040

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="section-heading">')
                __stream_4981914208 = []
                __append_4981914208 = __stream_4981914208.append
                __append_4981914208('\n      Rights\n    ')
                __msgid_4981914208 = __re_whitespace(''.join(__stream_4981914208)).strip()
                if 'section_rights_heading':
                    __append(translate('section_rights_heading', mapping=None, default=__msgid_4981914208, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n\n    ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4981906864
                __attrs_4981906864 = _static_4753720080

                # <small ... (0:0)
                # --------------------------------------------------------
                __append('<small>')

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981906528
                __default_4981906528 = _DEFAULT_MARKER

                # <Value 'rights' (7:24)> -> __cache_4981912528
                __token = 257
                try:
                    __zt_tmp = __attrs_4981906864
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4981912528 = _static_4754050160('path', 'rights', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                # <BinOp left=<Value 'rights' (7:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f1f3a0> -> __condition
                __expression = __cache_4981912528

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Copyleft NiceCorp Inc.')
                else:
                    __content = __cache_4981912528
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</small>\n\n</section>')
                __i18n_domain = __previous_i18n_domain_4981911520
            if (__backup_rights_4981900624 is __marker):
                del econtext['rights']
            else:
                econtext['rights'] = __backup_rights_4981900624
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }