# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/viewlets/document_relateditems.pt'

__tokens = {74: ('view/related_items', 2, 24), 104: (' nocall:context/@@plon', 2, 54), 156: ('t nocall:context/@@plone_layo', 3, 27), 218: ('ng nocall:plone_view/normalizeStr', 4, 29), 282: ('ate nocall:context/@@plone_context_s', 5, 26), 351: ("tion python:context.portal_registry.get('types_use_view_action_in_listings'", 6, 27), 453: ('related', 7, 19), 640: ('related', 14, 32), 708: ('item/Description', 15, 58), 735: (' item/portal_typ', 15, 85), 768: ("s python:'contenttype-' + normalizeString(item_typ", 15, 118), 833: ('te item/review_state|python: context_state.workflow_stat', 15, 183), 910: ("ass python: 'state-' + normalizeString(item_wf_st", 15, 260), 969: ('_url item/getURL|item/absolut', 15, 319), 1008: ("m_url python:(item_type in use_view_action) and item_url+'/view' or it", 15, 358), 1094: ('_image python:item.', 15, 444), 1178: ('${item_url}', 18, 22), 1180: ('item_url', 18, 24), 1217: ('${item/pretty_title_or_id}', 18, 61), 1219: ('item/pretty_title_or_id', 18, 63), 1269: ('${item/Description}', 19, 15), 1271: ('item/Description', 19, 17), 1362: ("python:item.getURL() +'/@@images/image/thumb'", 22, 51), 1424: ('item_has_image', 22, 113), 1460: ('string:$getIcon', 22, 149), 1480: (' item/Descriptio', 22, 169)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4981910656 = {'src': '', 'class': 'ms-3', 'alt': 'item/Description', }
_static_4981172224 = {'href': '${item_url}', 'class': 'h6 stretched-link', }
_static_4982406832 = {'class': 'media-body', }
_static_4982404624 = {'class': 'media position-relative', }
_static_4753720080 = {}
_static_4982392480 = {'class': 'section-heading', }
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4982392624 = {'id': 'section-related', }

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

            # <Static value=<ast.Dict object at 0x128f94730> name=None at 128f970a0> -> __attrs_4982394592
            __attrs_4982394592 = _static_4982392624
            __backup_related_4981801888 = get('related', __marker)

            # <Value 'view/related_items' (2:24)> -> __value
            __token = 74
            try:
                __zt_tmp = __attrs_4982394592
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/related_items', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['related'] = __value
            __backup_plone_view_4977863952 = get('plone_view', __marker)

            # <Value 'nocall:context/@@plone' (2:54)> -> __value
            __token = 104
            try:
                __zt_tmp = __attrs_4982394592
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('nocall', 'context/@@plone', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['plone_view'] = __value
            __backup_plone_layout_4981903792 = get('plone_layout', __marker)

            # <Value 'nocall:context/@@plone_layout' (3:27)> -> __value
            __token = 156
            try:
                __zt_tmp = __attrs_4982394592
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('nocall', 'context/@@plone_layout', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['plone_layout'] = __value
            __backup_normalizeString_4760146976 = get('normalizeString', __marker)

            # <Value 'nocall:plone_view/normalizeString' (4:29)> -> __value
            __token = 218
            try:
                __zt_tmp = __attrs_4982394592
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('nocall', 'plone_view/normalizeString', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['normalizeString'] = __value
            __backup_context_state_4982319296 = get('context_state', __marker)

            # <Value 'nocall:context/@@plone_context_state' (5:26)> -> __value
            __token = 282
            try:
                __zt_tmp = __attrs_4982394592
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('nocall', 'context/@@plone_context_state', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['context_state'] = __value
            __backup_use_view_action_4981810048 = get('use_view_action', __marker)

            # <Value "python:context.portal_registry.get('types_use_view_action_in_listings', [])" (6:27)> -> __value
            __token = 351
            try:
                __zt_tmp = __attrs_4982394592
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', "context.portal_registry.get('types_use_view_action_in_listings', [])", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['use_view_action'] = __value

            # <Value 'related' (7:19)> -> __condition
            __token = 453
            try:
                __zt_tmp = __attrs_4982394592
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('path', 'related', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4982401072 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-related">\n\n    ')

                # <Static value=<ast.Dict object at 0x128f946a0> name=None at 128f97040> -> __attrs_4982399440
                __attrs_4982399440 = _static_4982392480

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="section-heading">')
                __stream_4982393968 = []
                __append_4982393968 = __stream_4982393968.append
                __append_4982393968('\n      Related content\n    ')
                __msgid_4982393968 = __re_whitespace(''.join(__stream_4982393968)).strip()
                if 'section_related_heading':
                    __append(translate('section_related_heading', mapping=None, default=__msgid_4982393968, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n\n    <!-- section content -->\n    ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982391520
                __attrs_4982391520 = _static_4753720080
                __backup_item_4982403040 = get('item', __marker)

                # <Value 'related' (14:32)> -> __iterator
                __token = 640
                try:
                    __zt_tmp = __attrs_4982391520
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4754050160('path', 'related', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                (__iterator, ____index_4982393104, ) = getname('repeat')('item', __iterator)
                econtext['item'] = None
                for __item in __iterator:
                    econtext['item'] = __item
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x128f97610> name=None at 128f97e50> -> __attrs_4982398144
                    __attrs_4982398144 = _static_4982404624
                    __backup_desc_4982399008 = get('desc', __marker)

                    # <Value 'item/Description' (15:58)> -> __value
                    __token = 708
                    try:
                        __zt_tmp = __attrs_4982398144
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('path', 'item/Description', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['desc'] = __value
                    __backup_item_type_4982392864 = get('item_type', __marker)

                    # <Value 'item/portal_type' (15:85)> -> __value
                    __token = 735
                    try:
                        __zt_tmp = __attrs_4982398144
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('path', 'item/portal_type', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['item_type'] = __value
                    __backup_item_type_class_4982394784 = get('item_type_class', __marker)

                    # <Value "python:'contenttype-' + normalizeString(item_type)" (15:118)> -> __value
                    __token = 768
                    try:
                        __zt_tmp = __attrs_4982398144
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('python', "'contenttype-' + normalizeString(item_type)", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['item_type_class'] = __value
                    __backup_item_wf_state_4982398000 = get('item_wf_state', __marker)

                    # <Value 'item/review_state|python: context_state.workflow_state()' (15:183)> -> __value
                    __token = 833
                    try:
                        __zt_tmp = __attrs_4982398144
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('path', 'item/review_state|python: context_state.workflow_state()', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['item_wf_state'] = __value
                    __backup_item_wf_state_class_4982396752 = get('item_wf_state_class', __marker)

                    # <Value "python: 'state-' + normalizeString(item_wf_state)" (15:260)> -> __value
                    __token = 910
                    try:
                        __zt_tmp = __attrs_4982398144
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('python', " 'state-' + normalizeString(item_wf_state)", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['item_wf_state_class'] = __value
                    __backup_item_url_4982393392 = get('item_url', __marker)

                    # <Value 'item/getURL|item/absolute_url' (15:319)> -> __value
                    __token = 969
                    try:
                        __zt_tmp = __attrs_4982398144
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('path', 'item/getURL|item/absolute_url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['item_url'] = __value
                    __backup_item_url_4982391040 = get('item_url', __marker)

                    # <Value "python:(item_type in use_view_action) and item_url+'/view' or item_url" (15:358)> -> __value
                    __token = 1008
                    try:
                        __zt_tmp = __attrs_4982398144
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('python', "(item_type in use_view_action) and item_url+'/view' or item_url", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['item_url'] = __value
                    __backup_item_has_image_4982404384 = get('item_has_image', __marker)

                    # <Value 'python:item.getIcon' (15:444)> -> __value
                    __token = 1094
                    try:
                        __zt_tmp = __attrs_4982398144
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('python', 'item.getIcon', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['item_has_image'] = __value

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="media position-relative">\n\n      ')

                    # <Static value=<ast.Dict object at 0x128f97eb0> name=None at 128f94af0> -> __attrs_4982400208
                    __attrs_4982400208 = _static_4982406832

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="media-body">\n        ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4974773488
                    __attrs_4974773488 = _static_4753720080

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div>')

                    # <Static value=<ast.Dict object at 0x128e6a800> name=None at 128e6a1a0> -> __attrs_4981902208
                    __attrs_4981902208 = _static_4981172224

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4974776656
                    __default_4974776656 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution '${item_url}' (18:22)> braces_required=True translation=False default='"?"' default_marker='"?"' at 128e6a140> -> __attr_href
                    __token = 1178
                    __token = 1180
                    try:
                        __zt_tmp = __attrs_4981902208
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4754050160('path', 'item_url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
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
                    __append(' class="h6 stretched-link">')

                    # <Interpolation value=<Substitution '${item/pretty_title_or_id}' (18:61)> braces_required=True translation=False default='"?"' default_marker='"?"' at 128f1efe0> -> __content_4355604080
                    __token = 1217
                    __token = 1219
                    try:
                        __zt_tmp = __attrs_4981902208
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_4355604080 = _static_4754050160('path', 'item/pretty_title_or_id', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __content_4355604080 = __quote(__content_4355604080, '\x00', '&#0;', None, None)
                    __content_4355604080 = __content_4355604080
                    if (__content_4355604080 is None):
                        pass
                    else:
                        if (__content_4355604080 is None):
                            __content_4355604080 = None
                        else:
                            __tt = type(__content_4355604080)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_4355604080 = str(__content_4355604080)
                            else:
                                if (__tt is bytes):
                                    __content_4355604080 = decode(__content_4355604080)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_4355604080 = __content_4355604080.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_4355604080)
                                            __content_4355604080 = (str(__content_4355604080) if (__content_4355604080 is __converted) else __converted)
                                        else:
                                            __content_4355604080 = __content_4355604080()
                    if (__content_4355604080 is not None):
                        __append(__content_4355604080)
                    __append('</a></div>\n        ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4981903888
                    __attrs_4981903888 = _static_4753720080

                    # <small ... (0:0)
                    # --------------------------------------------------------
                    __append('<small>')

                    # <Interpolation value=<Substitution '${item/Description}' (19:15)> braces_required=True translation=False default='"?"' default_marker='"?"' at 128f1d9c0> -> __content_4355604080
                    __token = 1269
                    __token = 1271
                    try:
                        __zt_tmp = __attrs_4981903888
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_4355604080 = _static_4754050160('path', 'item/Description', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __content_4355604080 = __quote(__content_4355604080, '\x00', '&#0;', None, None)
                    __content_4355604080 = __content_4355604080
                    if (__content_4355604080 is None):
                        pass
                    else:
                        if (__content_4355604080 is None):
                            __content_4355604080 = None
                        else:
                            __tt = type(__content_4355604080)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_4355604080 = str(__content_4355604080)
                            else:
                                if (__tt is bytes):
                                    __content_4355604080 = decode(__content_4355604080)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_4355604080 = __content_4355604080.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_4355604080)
                                            __content_4355604080 = (str(__content_4355604080) if (__content_4355604080 is __converted) else __converted)
                                        else:
                                            __content_4355604080 = __content_4355604080()
                    if (__content_4355604080 is not None):
                        __append(__content_4355604080)
                    __append('</small>\n      </div>\n\n      ')

                    # <Static value=<ast.Dict object at 0x128f1ec80> name=None at 128f1fe20> -> __attrs_4981907728
                    __attrs_4981907728 = _static_4981910656
                    __backup_getIcon_4974686032 = get('getIcon', __marker)

                    # <Value "python:item.getURL() +'/@@images/image/thumb'" (22:51)> -> __value
                    __token = 1362
                    try:
                        __zt_tmp = __attrs_4981907728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('python', "item.getURL() +'/@@images/image/thumb'", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['getIcon'] = __value

                    # <Value 'item_has_image' (22:113)> -> __condition
                    __token = 1424
                    try:
                        __zt_tmp = __attrs_4981907728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4754050160('path', 'item_has_image', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    if __condition:

                        # <img ... (0:0)
                        # --------------------------------------------------------
                        __append('<img')

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981902496
                        __default_4981902496 = _DEFAULT_MARKER

                        # <Substitution 'string:$getIcon' (22:149)> -> __attr_src
                        __token = 1460
                        try:
                            __zt_tmp = __attrs_4981907728
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_src = _static_4754050160('string', '$getIcon', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                        __attr_src = __quote(__attr_src, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_src is not None):
                            __append((' src="%s"' % __attr_src))
                        __append(' class="ms-3"')

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981900192
                        __default_4981900192 = _DEFAULT_MARKER

                        # <Substitution 'item/Description' (22:169)> -> __attr_alt
                        __token = 1480
                        try:
                            __zt_tmp = __attrs_4981907728
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_alt = _static_4754050160('path', 'item/Description', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                        __attr_alt = __quote(__attr_alt, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_alt is not None):
                            __append((' alt="%s"' % __attr_alt))
                        __append('>')
                    if (__backup_getIcon_4974686032 is __marker):
                        del econtext['getIcon']
                    else:
                        econtext['getIcon'] = __backup_getIcon_4974686032
                    __append('\n\n    </div>')
                    if (__backup_item_has_image_4982404384 is __marker):
                        del econtext['item_has_image']
                    else:
                        econtext['item_has_image'] = __backup_item_has_image_4982404384
                    if (__backup_item_url_4982391040 is __marker):
                        del econtext['item_url']
                    else:
                        econtext['item_url'] = __backup_item_url_4982391040
                    if (__backup_item_url_4982393392 is __marker):
                        del econtext['item_url']
                    else:
                        econtext['item_url'] = __backup_item_url_4982393392
                    if (__backup_item_wf_state_class_4982396752 is __marker):
                        del econtext['item_wf_state_class']
                    else:
                        econtext['item_wf_state_class'] = __backup_item_wf_state_class_4982396752
                    if (__backup_item_wf_state_4982398000 is __marker):
                        del econtext['item_wf_state']
                    else:
                        econtext['item_wf_state'] = __backup_item_wf_state_4982398000
                    if (__backup_item_type_class_4982394784 is __marker):
                        del econtext['item_type_class']
                    else:
                        econtext['item_type_class'] = __backup_item_type_class_4982394784
                    if (__backup_item_type_4982392864 is __marker):
                        del econtext['item_type']
                    else:
                        econtext['item_type'] = __backup_item_type_4982392864
                    if (__backup_desc_4982399008 is __marker):
                        del econtext['desc']
                    else:
                        econtext['desc'] = __backup_desc_4982399008
                    __append('\n    ')
                    ____index_4982393104 -= 1
                    if (____index_4982393104 > 0):
                        __append('')
                if (__backup_item_4982403040 is __marker):
                    del econtext['item']
                else:
                    econtext['item'] = __backup_item_4982403040
                __append('\n\n</section>')
                __i18n_domain = __previous_i18n_domain_4982401072
            if (__backup_use_view_action_4981810048 is __marker):
                del econtext['use_view_action']
            else:
                econtext['use_view_action'] = __backup_use_view_action_4981810048
            if (__backup_context_state_4982319296 is __marker):
                del econtext['context_state']
            else:
                econtext['context_state'] = __backup_context_state_4982319296
            if (__backup_normalizeString_4760146976 is __marker):
                del econtext['normalizeString']
            else:
                econtext['normalizeString'] = __backup_normalizeString_4760146976
            if (__backup_plone_layout_4981903792 is __marker):
                del econtext['plone_layout']
            else:
                econtext['plone_layout'] = __backup_plone_layout_4981903792
            if (__backup_plone_view_4977863952 is __marker):
                del econtext['plone_view']
            else:
                econtext['plone_view'] = __backup_plone_view_4977863952
            if (__backup_related_4981801888 is __marker):
                del econtext['related']
            else:
                econtext['related'] = __backup_related_4981801888
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }