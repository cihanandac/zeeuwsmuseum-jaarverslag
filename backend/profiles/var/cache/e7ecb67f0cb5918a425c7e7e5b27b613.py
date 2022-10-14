# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/linkintegrity/browser/delete_confirmation_info.pt'

__tokens = {318: ('python:view.breaches', 8, 43), 363: ('breaches', 10, 21), 498: ('breaches', 14, 22), 782: ('context/@@authenticator/token', 20, 27), 848: ('breaches', 21, 34), 925: ('breach/target', 23, 40), 968: ('${target/url}', 24, 27), 970: ('target/url', 24, 29), 996: ('target/title', 24, 55), 1162: ('target/type_title', 27, 62), 1340: ("python:breach['sources']", 34, 33), 1423: ('source/accessible', 35, 36), 1481: ('source/url', 36, 38), 1506: ('source/title', 36, 63), 1580: ('string:${source/url}/edit?_authenticator=${token}', 38, 39), 1836: ('not: source/accessible', 43, 27), 2082: ('view/breach_count', 52, 36), 2116: ('breach_count', 52, 70), 2248: ('python:len(breach_count)', 56, 33), 2414: ('refs', 58, 78), 2527: ('python:breach_count', 62, 34), 2669: ('content', 64, 41), 2813: ('view/objects', 67, 38), 2862: ('python:range(3)', 68, 35), 2916: ('python: breach_count[content][item]', 69, 35), 2975: ('python: objects[item]', 69, 94), 3108: ('breaches', 77, 24)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4932380720 = {'target': '_blank', 'href': 'string:${source/url}/edit?_authenticator=${token}', }
_static_4932486576 = {'href': 'source/url', }
_static_4932653104 = {'class': 'breach-item', }
_static_4909524896 = {'href': '${target/url}', }
_static_5110160768 = {'class': 'breach-container', }
_static_4685938064 = {'id': 'content-core', }
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
_static_4428767312 = {}
_static_5108951136 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'xml:lang': 'en', 'lang': 'en', }

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

            # <Static value=<ast.Dict object at 0x130846860> name=None at 1257cbc40> -> __attrs_4907241088
            __attrs_4907241088 = _static_5108951136
            __previous_i18n_domain_4907240656 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4923845952
            __attrs_4923845952 = _static_4428767312
            __backup_breaches_4923885744 = get('breaches', __marker)

            # <Value 'python:view.breaches' (8:43)> -> __value
            __token = 318
            try:
                __zt_tmp = __attrs_4923845952
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', 'view.breaches', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['breaches'] = __value
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4921577664
            __attrs_4921577664 = _static_4428767312

            # <Value 'breaches' (10:21)> -> __condition
            __token = 363
            try:
                __zt_tmp = __attrs_4921577664
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'breaches', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2>')
                __stream_4923845520 = []
                __append_4923845520 = __stream_4923845520.append
                __append_4923845520('Potential link breakage')
                __msgid_4923845520 = __re_whitespace(''.join(__stream_4923845520)).strip()
                if 'linkintegrity_breaches_title':
                    __append(translate('linkintegrity_breaches_title', mapping=None, default=__msgid_4923845520, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h2>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x1174dbd90> name=None at 107fde4d0> -> __attrs_4923926048
            __attrs_4923926048 = _static_4685938064

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="content-core">\n\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4923917120
            __attrs_4923917120 = _static_4428767312

            # <Value 'breaches' (14:22)> -> __condition
            __token = 498
            try:
                __zt_tmp = __attrs_4923917120
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'breaches', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p>')
                __stream_4923930608 = []
                __append_4923930608 = __stream_4923930608.append
                __append_4923930608('\n      By deleting this item, you will break links that exist in the items listed\n      below. If this is indeed what you want to do, we recommend that you remove\n      these references first.\n    ')
                __msgid_4923930608 = __re_whitespace(''.join(__stream_4923930608)).strip()
                if 'linkintegrity_instructions':
                    __append(translate('linkintegrity_instructions', mapping=None, default=__msgid_4923930608, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>')
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5110157024
            __attrs_5110157024 = _static_4428767312
            __backup_token_4923840048 = get('token', __marker)

            # <Value 'context/@@authenticator/token' (20:27)> -> __value
            __token = 782
            try:
                __zt_tmp = __attrs_5110157024
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'context/@@authenticator/token', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['token'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div>\n      ')

            # <Static value=<ast.Dict object at 0x13096dd80> name=None at 13096dd50> -> __attrs_5110163072
            __attrs_5110163072 = _static_5110160768
            __backup_breach_4921574256 = get('breach', __marker)

            # <Value 'breaches' (21:34)> -> __iterator
            __token = 848
            try:
                __zt_tmp = __attrs_5110163072
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4427992992('path', 'breaches', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            (__iterator, ____index_5110162352, ) = getname('repeat')('breach', __iterator)
            econtext['breach'] = None
            for __item in __iterator:
                econtext['breach'] = __item

                # <article ... (0:0)
                # --------------------------------------------------------
                __append('<article class="breach-container">\n\n        ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4899916624
                __attrs_4899916624 = _static_4428767312
                __backup_target_5110157792 = get('target', __marker)

                # <Value 'breach/target' (23:40)> -> __value
                __token = 925
                try:
                    __zt_tmp = __attrs_4899916624
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'breach/target', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['target'] = __value
                __append('\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4960114368
                __attrs_4960114368 = _static_4428767312

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>')

                # <Static value=<ast.Dict object at 0x124a167a0> name=None at 124a17580> -> __attrs_4909522448
                __attrs_4909522448 = _static_4909524896

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4909528544
                __default_4909528544 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${target/url}' (24:27)> braces_required=True translation=False default='"?"' default_marker='"?"' at 124a16860> -> __attr_href
                __token = 968
                __token = 970
                try:
                    __zt_tmp = __attrs_4909522448
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4427992992('path', 'target/url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_href = __attr_href
                if (__attr_href is None):
                    pass
                else:
                    if (__attr_href is _DEFAULT_MARKER):
                        __attr_href = None
                    else:
                        __tt = type(__attr_href)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __attr_href = str(__attr_href)
                        else:
                            if (__tt is bytes):
                                __attr_href = decode(__attr_href)
                            else:
                                if (__tt is not str):
                                    try:
                                        __attr_href = __attr_href.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__attr_href)
                                        __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                    else:
                                        __attr_href = __attr_href()
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append('>')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4908146000
                __default_4908146000 = _DEFAULT_MARKER

                # <Value 'target/title' (24:55)> -> __cache_4959215792
                __token = 996
                try:
                    __zt_tmp = __attrs_4909522448
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4959215792 = _static_4427992992('path', 'target/title', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'target/title' (24:55)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1248c4190> -> __condition
                __expression = __cache_4959215792

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4959215792
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</a></header>\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4909521776
                __attrs_4909521776 = _static_4428767312

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p>\n            ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4932730160
                __attrs_4932730160 = _static_4428767312

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')
                __stream_5111230112_portal_type = ''
                __stream_4909518128 = []
                __append_4909518128 = __stream_4909518128.append
                __append_4909518128('\n              This ')
                __stream_5111230112_portal_type = []
                __append_5111230112_portal_type = __stream_5111230112_portal_type.append

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4932725936
                __attrs_4932725936 = _static_4428767312

                # <span ... (0:0)
                # --------------------------------------------------------
                __append_5111230112_portal_type('<span>')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4932730544
                __default_4932730544 = _DEFAULT_MARKER

                # <Value 'target/type_title' (27:62)> -> __cache_4932716288
                __token = 1162
                try:
                    __zt_tmp = __attrs_4932725936
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4932716288 = _static_4427992992('path', 'target/type_title', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'target/type_title' (27:62)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 126034f40> -> __condition
                __expression = __cache_4932716288

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4932716288
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append_5111230112_portal_type(__content)
                __append_5111230112_portal_type('</span>')
                __append_4909518128('${portal_type}')
                __stream_5111230112_portal_type = ''.join(__stream_5111230112_portal_type)
                __append_4909518128('\n              is referenced by the following items:\n            ')
                __msgid_4909518128 = __re_whitespace(''.join(__stream_4909518128)).strip()
                if 'linkintegrity_is_referenced':
                    __append(translate('linkintegrity_is_referenced', mapping={'portal_type': __stream_5111230112_portal_type, }, default=__msgid_4909518128, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</span>\n          </p>\n        ')
                if (__backup_target_5110157792 is __marker):
                    del econtext['target']
                else:
                    econtext['target'] = __backup_target_5110157792
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4932725072
                __attrs_4932725072 = _static_4428767312

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul>\n          ')

                # <Static value=<ast.Dict object at 0x126025030> name=None at 126027850> -> __attrs_4932522512
                __attrs_4932522512 = _static_4932653104
                __backup_source_4899926128 = get('source', __marker)

                # <Value "python:breach['sources']" (34:33)> -> __iterator
                __token = 1340
                try:
                    __zt_tmp = __attrs_4932522512
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4427992992('python', "breach['sources']", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                (__iterator, ____index_4932530768, ) = getname('repeat')('source', __iterator)
                econtext['source'] = None
                for __item in __iterator:
                    econtext['source'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="breach-item">\n            ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4932524384
                    __attrs_4932524384 = _static_4428767312

                    # <Value 'source/accessible' (35:36)> -> __condition
                    __token = 1423
                    try:
                        __zt_tmp = __attrs_4932524384
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('path', 'source/accessible', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:
                        __append('\n              ')

                        # <Static value=<ast.Dict object at 0x125ffc5b0> name=None at 125ffe620> -> __attrs_4943224960
                        __attrs_4943224960 = _static_4932486576

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900530176
                        __default_4900530176 = _DEFAULT_MARKER

                        # <Substitution 'source/url' (36:38)> -> __attr_href
                        __token = 1481
                        try:
                            __zt_tmp = __attrs_4943224960
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4427992992('path', 'source/url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4932496464
                        __default_4932496464 = _DEFAULT_MARKER

                        # <Value 'source/title' (36:63)> -> __cache_4932499248
                        __token = 1506
                        try:
                            __zt_tmp = __attrs_4943224960
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4932499248 = _static_4427992992('path', 'source/title', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value 'source/title' (36:63)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 125ffc310> -> __condition
                        __expression = __cache_4932499248

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4932499248
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</a>\n              [')

                        # <Static value=<ast.Dict object at 0x125fe2830> name=None at 125fe3520> -> __attrs_4922823328
                        __attrs_4922823328 = _static_4932380720

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a target="_blank"')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4932386048
                        __default_4932386048 = _DEFAULT_MARKER

                        # <Substitution 'string:${source/url}/edit?_authenticator=${token}' (38:39)> -> __attr_href
                        __token = 1580
                        try:
                            __zt_tmp = __attrs_4922823328
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4427992992('string', '${source/url}/edit?_authenticator=${token}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>')
                        __stream_4932378608 = []
                        __append_4932378608 = __stream_4932378608.append
                        __append_4932378608('Edit in new window')
                        __msgid_4932378608 = __re_whitespace(''.join(__stream_4932378608)).strip()
                        if 'linkintegrity_edit_in_new_window':
                            __append(translate('linkintegrity_edit_in_new_window', mapping=None, default=__msgid_4932378608, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</a>]\n            ')
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4922910432
                    __attrs_4922910432 = _static_4428767312

                    # <Value 'not: source/accessible' (43:27)> -> __condition
                    __token = 1836
                    try:
                        __zt_tmp = __attrs_4922910432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('not', ' source/accessible', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:
                        __stream_4932523040 = []
                        __append_4932523040 = __stream_4932523040.append
                        __append_4932523040('\n              The item is not accessible.\n            ')
                        __msgid_4932523040 = __re_whitespace(''.join(__stream_4932523040)).strip()
                        if 'linkintegrity_item_not_accessible':
                            __append(translate('linkintegrity_item_not_accessible', mapping=None, default=__msgid_4932523040, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n          </li>')
                    ____index_4932530768 -= 1
                    if (____index_4932530768 > 0):
                        __append('\n          ')
                if (__backup_source_4899926128 is __marker):
                    del econtext['source']
                else:
                    econtext['source'] = __backup_source_4899926128
                __append('\n        </ul>\n\n      </article>')
                ____index_5110162352 -= 1
                if (____index_5110162352 > 0):
                    __append('\n      ')
            if (__backup_breach_4921574256 is __marker):
                del econtext['breach']
            else:
                econtext['breach'] = __backup_breach_4921574256
            __append('\n\n      ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4932460624
            __attrs_4932460624 = _static_4428767312
            __backup_breach_count_4921583904 = get('breach_count', __marker)

            # <Value 'view/breach_count' (52:36)> -> __value
            __token = 2082
            try:
                __zt_tmp = __attrs_4932460624
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'view/breach_count', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['breach_count'] = __value

            # <Value 'breach_count' (52:70)> -> __condition
            __token = 2116
            try:
                __zt_tmp = __attrs_4932460624
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'breach_count', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n\n        ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4943753328
                __attrs_4943753328 = _static_4428767312

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2 >')
                __stream_4943754096 = []
                __append_4943754096 = __stream_4943754096.append
                __append_4943754096('Deleting overview')
                __msgid_4943754096 = __re_whitespace(''.join(__stream_4943754096)).strip()
                if 'deleting_overview':
                    __append(translate('deleting_overview', mapping=None, default=__msgid_4943754096, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h2>\n        ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4943750256
                __attrs_4943750256 = _static_4428767312

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p>\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4893842672
                __attrs_4893842672 = _static_4428767312
                __backup_refs_4960119456 = get('refs', __marker)

                # <Value 'python:len(breach_count)' (56:33)> -> __value
                __token = 2248
                try:
                    __zt_tmp = __attrs_4893842672
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'len(breach_count)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['refs'] = __value

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')
                __stream_4940370816_refs = ''
                __stream_4943751888 = []
                __append_4943751888 = __stream_4943751888.append
                __append_4943751888('\n            Number of selected, non-empty folders: ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4943828816
                __attrs_4943828816 = _static_4428767312

                # <strong ... (0:0)
                # --------------------------------------------------------
                __append_4943751888('<strong>')
                __stream_4940370816_refs = []
                __append_4940370816_refs = __stream_4940370816_refs.append

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4897426352
                __attrs_4897426352 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4943827376
                __default_4943827376 = _DEFAULT_MARKER

                # <Value 'refs' (58:78)> -> __cache_4943832848
                __token = 2414
                try:
                    __zt_tmp = __attrs_4897426352
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4943832848 = _static_4427992992('path', 'refs', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'refs' (58:78)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 126acc790> -> __condition
                __expression = __cache_4943832848

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_4940370816_refs('<span />')
                else:
                    __content = __cache_4943832848
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append_4940370816_refs(__content)
                __append_4943751888('${refs}')
                __stream_4940370816_refs = ''.join(__stream_4940370816_refs)
                __append_4943751888('</strong>\n          ')
                __msgid_4943751888 = __re_whitespace(''.join(__stream_4943751888)).strip()
                if 'selected_folders_with_content':
                    __append(translate('selected_folders_with_content', mapping={'refs': __stream_4940370816_refs, }, default=__msgid_4943751888, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</span>')
                if (__backup_refs_4960119456 is __marker):
                    del econtext['refs']
                else:
                    econtext['refs'] = __backup_refs_4960119456
                __append('\n        </p>\n        ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4957764240
                __attrs_4957764240 = _static_4428767312

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul>\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4948196560
                __attrs_4948196560 = _static_4428767312
                __backup_content_4932664576 = get('content', __marker)

                # <Value 'python:breach_count' (62:34)> -> __iterator
                __token = 2527
                try:
                    __zt_tmp = __attrs_4948196560
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4427992992('python', 'breach_count', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                (__iterator, ____index_4948194256, ) = getname('repeat')('content', __iterator)
                econtext['content'] = None
                for __item in __iterator:
                    econtext['content'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li>\n            ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4948182640
                    __attrs_4948182640 = _static_4428767312

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_5111224736_content = ''
                    __stream_4948183120 = []
                    __append_4948183120 = __stream_4948183120.append
                    __append_4948183120(' Following content within\n              ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4958416480
                    __attrs_4958416480 = _static_4428767312

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append_4948183120('<strong>')
                    __stream_5111224736_content = []
                    __append_5111224736_content = __stream_5111224736_content.append

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109664592
                    __attrs_5109664592 = _static_4428767312

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109676112
                    __default_5109676112 = _DEFAULT_MARKER

                    # <Value 'content' (64:41)> -> __cache_4958411872
                    __token = 2669
                    try:
                        __zt_tmp = __attrs_5109664592
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4958411872 = _static_4427992992('path', 'content', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'content' (64:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1308f6440> -> __condition
                    __expression = __cache_4958411872

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append_5111224736_content('<span />')
                    else:
                        __content = __cache_4958411872
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_5111224736_content(__content)
                    __append_4948183120('${content}')
                    __stream_5111224736_content = ''.join(__stream_5111224736_content)
                    __append_4948183120('</strong>  will also be deleted:\n            ')
                    __msgid_4948183120 = __re_whitespace(''.join(__stream_4948183120)).strip()
                    if 'deleting_contents':
                        __append(translate('deleting_contents', mapping={'content': __stream_5111224736_content, }, default=__msgid_4948183120, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109663296
                    __attrs_5109663296 = _static_4428767312

                    # <br ... (0:0)
                    # --------------------------------------------------------
                    __append('<br/>\n            ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109664640
                    __attrs_5109664640 = _static_4428767312

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul>\n              ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109675008
                    __attrs_5109675008 = _static_4428767312
                    __backup_objects_4932664000 = get('objects', __marker)

                    # <Value 'view/objects' (67:38)> -> __value
                    __token = 2813
                    try:
                        __zt_tmp = __attrs_5109675008
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4427992992('path', 'view/objects', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    econtext['objects'] = __value
                    __backup_item_4943825600 = get('item', __marker)

                    # <Value 'python:range(3) ' (68:35)> -> __iterator
                    __token = 2862
                    try:
                        __zt_tmp = __attrs_5109675008
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_4427992992('python', 'range(3) ', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    (__iterator, ____index_5109675296, ) = getname('repeat')('item', __iterator)
                    econtext['item'] = None
                    for __item in __iterator:
                        econtext['item'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li>\n                ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109667808
                        __attrs_5109667808 = _static_4428767312

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109669536
                        __default_5109669536 = _DEFAULT_MARKER

                        # <Value 'python: breach_count[content][item]' (69:35)> -> __cache_5109669872
                        __token = 2916
                        try:
                            __zt_tmp = __attrs_5109667808
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_5109669872 = _static_4427992992('python', ' breach_count[content][item]', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value 'python: breach_count[content][item]' (69:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1308f6f80> -> __condition
                        __expression = __cache_5109669872

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span />')
                        else:
                            __content = __cache_5109669872
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(' ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109673712
                        __attrs_5109673712 = _static_4428767312

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109674096
                        __default_5109674096 = _DEFAULT_MARKER

                        # <Value 'python: objects[item]' (69:94)> -> __cache_5109662288
                        __token = 2975
                        try:
                            __zt_tmp = __attrs_5109673712
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_5109662288 = _static_4427992992('python', ' objects[item]', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value 'python: objects[item]' (69:94)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1308f6c80> -> __condition
                        __expression = __cache_5109662288

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span />')
                        else:
                            __content = __cache_5109662288
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n              </li>')
                        ____index_5109675296 -= 1
                        if (____index_5109675296 > 0):
                            __append('\n              ')
                    if (__backup_item_4943825600 is __marker):
                        del econtext['item']
                    else:
                        econtext['item'] = __backup_item_4943825600
                    if (__backup_objects_4932664000 is __marker):
                        del econtext['objects']
                    else:
                        econtext['objects'] = __backup_objects_4932664000
                    __append('\n            </ul>\n          </li>')
                    ____index_4948194256 -= 1
                    if (____index_4948194256 > 0):
                        __append('\n          ')
                if (__backup_content_4932664576 is __marker):
                    del econtext['content']
                else:
                    econtext['content'] = __backup_content_4932664576
                __append('\n        </ul>\n\n      </div>')
            if (__backup_breach_count_4921583904 is __marker):
                del econtext['breach_count']
            else:
                econtext['breach_count'] = __backup_breach_count_4921583904
            __append('\n\n      ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109667088
            __attrs_5109667088 = _static_4428767312

            # <Value 'breaches' (77:24)> -> __condition
            __token = 3108
            try:
                __zt_tmp = __attrs_5109667088
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'breaches', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p>')
                __stream_4948193536 = []
                __append_4948193536 = __stream_4948193536.append
                __append_4948193536('\n        Would you like to delete it anyway?\n      ')
                __msgid_4948193536 = __re_whitespace(''.join(__stream_4948193536)).strip()
                if 'linkintegrity_delete_anyway':
                    __append(translate('linkintegrity_delete_anyway', mapping=None, default=__msgid_4948193536, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>')
            __append('\n\n    </div>')
            if (__backup_token_4923840048 is __marker):
                del econtext['token']
            else:
                econtext['token'] = __backup_token_4923840048
            __append('\n\n  </div>\n\n')
            if (__backup_breaches_4923885744 is __marker):
                del econtext['breaches']
            else:
                econtext['breaches'] = __backup_breaches_4923885744
            __append('\n')
            __i18n_domain = __previous_i18n_domain_4907240656
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }