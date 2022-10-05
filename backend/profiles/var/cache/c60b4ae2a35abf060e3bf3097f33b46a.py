# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/viewlets/document_actions.pt'

__tokens = {82: ('view/actions', 3, 19), 365: ('nocall: context/@@plone/normalizeString', 12, 64), 449: ('view/actions', 13, 42), 504: ("python:'document-action-' + normalizeString(daction['id'])", 14, 41), 644: ('daction/url', 16, 46), 704: (' daction/link_target|nothin', 17, 47), 779: ('e daction/descripti', 18, 45), 840: ('daction/title', 19, 38)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4975172032 = {'href': '', 'target': 'daction/link_target|nothing', 'title': 'daction/description', }
_static_4975177552 = {'id': "python:'document-action-' + normalizeString(daction['id'])", }
_static_4975173040 = {'class': 'list-inline', }
_static_4975180096 = {'class': 'd-none', }
_static_4753720080 = {}
_static_4975166128 = {'class': 'viewlet viewlet-document-actions', }
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4975181728 = {'id': 'section-document-actions', }

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

            # <Static value=<ast.Dict object at 0x1288b3fa0> name=None at 1288b1ea0> -> __attrs_4975177744
            __attrs_4975177744 = _static_4975181728

            # <Value 'view/actions' (3:19)> -> __condition
            __token = 82
            try:
                __zt_tmp = __attrs_4975177744
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('path', 'view/actions', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4975167856 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-document-actions">\n\n    ')

                # <Static value=<ast.Dict object at 0x1288b02b0> name=None at 1288b0d60> -> __attrs_4975181488
                __attrs_4975181488 = _static_4975166128

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="viewlet viewlet-document-actions">\n        ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975175392
                __attrs_4975175392 = _static_4753720080
                __append('\n\n            ')

                # <Static value=<ast.Dict object at 0x1288b3940> name=None at 1288b3e20> -> __attrs_4975175776
                __attrs_4975175776 = _static_4975180096

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="d-none">')
                __stream_4975175104 = []
                __append_4975175104 = __stream_4975175104.append
                __append_4975175104('\n              Document Actions\n            ')
                __msgid_4975175104 = __re_whitespace(''.join(__stream_4975175104)).strip()
                if 'heading_document_actions':
                    __append(translate('heading_document_actions', mapping=None, default=__msgid_4975175104, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</div>\n\n            ')

                # <Static value=<ast.Dict object at 0x1288b1db0> name=None at 1288b2b30> -> __attrs_4975181680
                __attrs_4975181680 = _static_4975173040
                __backup_normalizeString_4977853056 = get('normalizeString', __marker)

                # <Value 'nocall: context/@@plone/normalizeString' (12:64)> -> __value
                __token = 365
                try:
                    __zt_tmp = __attrs_4975181680
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('nocall', ' context/@@plone/normalizeString', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['normalizeString'] = __value

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="list-inline">\n                  ')

                # <Static value=<ast.Dict object at 0x1288b2f50> name=None at 1288b2c20> -> __attrs_4975169632
                __attrs_4975169632 = _static_4975177552
                __backup_daction_4975170928 = get('daction', __marker)

                # <Value 'view/actions' (13:42)> -> __iterator
                __token = 449
                try:
                    __zt_tmp = __attrs_4975169632
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4754050160('path', 'view/actions', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                (__iterator, ____index_4975167136, ) = getname('repeat')('daction', __iterator)
                econtext['daction'] = None
                for __item in __iterator:
                    econtext['daction'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975174288
                    __default_4975174288 = _DEFAULT_MARKER

                    # <Substitution "python:'document-action-' + normalizeString(daction['id'])" (14:41)> -> __attr_id
                    __token = 504
                    try:
                        __zt_tmp = __attrs_4975169632
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_4754050160('python', "'document-action-' + normalizeString(daction['id'])", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))
                    __append('>\n                      ')

                    # <Static value=<ast.Dict object at 0x1288b19c0> name=None at 1288b16f0> -> __attrs_4975179136
                    __attrs_4975179136 = _static_4975172032

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975172848
                    __default_4975172848 = _DEFAULT_MARKER

                    # <Substitution 'daction/url' (16:46)> -> __attr_href
                    __token = 644
                    try:
                        __zt_tmp = __attrs_4975179136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4754050160('path', 'daction/url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975181392
                    __default_4975181392 = _DEFAULT_MARKER

                    # <Substitution 'daction/link_target|nothing' (17:47)> -> __attr_target
                    __token = 704
                    try:
                        __zt_tmp = __attrs_4975179136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_target = _static_4754050160('path', 'daction/link_target|nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_target = __quote(__attr_target, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_target is not None):
                        __append((' target="%s"' % __attr_target))

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975168288
                    __default_4975168288 = _DEFAULT_MARKER

                    # <Substitution 'daction/description' (18:45)> -> __attr_title
                    __token = 779
                    try:
                        __zt_tmp = __attrs_4975179136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_4754050160('path', 'daction/description', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975167760
                    __default_4975167760 = _DEFAULT_MARKER

                    # <Value 'daction/title' (19:38)> -> __cache_4975172080
                    __token = 840
                    try:
                        __zt_tmp = __attrs_4975179136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4975172080 = _static_4754050160('path', 'daction/title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'daction/title' (19:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 1288b2230> -> __condition
                    __expression = __cache_4975172080

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                      ')
                    else:
                        __content = __cache_4975172080
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</a>\n                  </li>')
                    ____index_4975167136 -= 1
                    if (____index_4975167136 > 0):
                        __append('\n                  ')
                if (__backup_daction_4975170928 is __marker):
                    del econtext['daction']
                else:
                    econtext['daction'] = __backup_daction_4975170928
                __append('\n            </ul>')
                if (__backup_normalizeString_4977853056 is __marker):
                    del econtext['normalizeString']
                else:
                    econtext['normalizeString'] = __backup_normalizeString_4977853056
                __append('\n        \n\n    </div>\n</section>')
                __i18n_domain = __previous_i18n_domain_4975167856
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }