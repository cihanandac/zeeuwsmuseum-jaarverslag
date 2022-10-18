# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/dexterity/browser/default_page_warning.pt'

__tokens = {144: ('context/@@plone_context_state/is_default_page|nothing', 5, 19), 499: ('string:${context/aq_inner/aq_parent/absolute_url}/edit', 11, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_5176285488 = {'href': '', }
_static_5101828128 = __C2ZContextWrapper
_static_5101822992 = __compile_zt_expr
_static_5176295376 = {'class': 'alert alert-info', 'role': 'alert', }
_static_5101990720 = {}

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

            # <Static value=<ast.Dict object at 0x1301a3340> name=None at 1301a00d0> -> __attrs_5176293696
            __attrs_5176293696 = _static_5101990720
            __previous_i18n_domain_5176293840 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n')

            # <Static value=<ast.Dict object at 0x13487ffd0> name=None at 13487fc40> -> __attrs_5176426608
            __attrs_5176426608 = _static_5176295376

            # <Value 'context/@@plone_context_state/is_default_page|nothing' (5:19)> -> __condition
            __token = 144
            try:
                __zt_tmp = __attrs_5176426608
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_5101822992('path', 'context/@@plone_context_state/is_default_page|nothing', econtext=econtext)(_static_5101828128(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="alert alert-info" role="alert">\n  ')

                # <Static value=<ast.Dict object at 0x1301a3340> name=None at 1301a00d0> -> __attrs_5176427952
                __attrs_5176427952 = _static_5101990720

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')
                __stream_5163551648_go_here = ''
                __stream_5176427472 = []
                __append_5176427472 = __stream_5176427472.append
                __append_5176427472('\n      You are editing the default view of a container. If you wanted to edit the container itself,\n     ')
                __stream_5163551648_go_here = []
                __append_5163551648_go_here = __stream_5163551648_go_here.append

                # <Static value=<ast.Dict object at 0x13487d930> name=None at 13487dc90> -> __attrs_5176290144
                __attrs_5176290144 = _static_5176285488

                # <a ... (0:0)
                # --------------------------------------------------------
                __append_5163551648_go_here('<a')

                # <Symbol value=<DEFAULT> at 130202920> -> __default_5176286400
                __default_5176286400 = _DEFAULT_MARKER

                # <Substitution 'string:${context/aq_inner/aq_parent/absolute_url}/edit' (11:29)> -> __attr_href
                __token = 499
                try:
                    __zt_tmp = __attrs_5176290144
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_5101822992('string', '${context/aq_inner/aq_parent/absolute_url}/edit', econtext=econtext)(_static_5101828128(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append_5163551648_go_here((' href="%s"' % __attr_href))
                __append_5163551648_go_here('>')
                __stream_5176285008 = []
                __append_5176285008 = __stream_5176285008.append
                __append_5176285008('go here')
                __msgid_5176285008 = __re_whitespace(''.join(__stream_5176285008)).strip()
                if 'label_edit_default_view_container_go_here':
                    __append_5163551648_go_here(translate('label_edit_default_view_container_go_here', mapping=None, default=__msgid_5176285008, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append_5163551648_go_here('</a>')
                __append_5176427472('${go_here}')
                __stream_5163551648_go_here = ''.join(__stream_5163551648_go_here)
                __append_5176427472('.\n  ')
                __msgid_5176427472 = __re_whitespace(''.join(__stream_5176427472)).strip()
                if 'label_edit_default_view_container':
                    __append(translate('label_edit_default_view_container', mapping={'go_here': __stream_5163551648_go_here, }, default=__msgid_5176427472, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</span>\n</div>')
            __append('\n')
            __i18n_domain = __previous_i18n_domain_5176293840
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }