# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/content/browser/templates/select_default_page.pt'

__tokens = {385: ("python:request.set('disable_border',1)", 9, 31), 929: ('string:${context/absolute_url}/select_default_page', 24, 39), 1088: ('view/get_selectable_items', 28, 37), 1154: (' context/getDefaultPage|nothin', 29, 39), 1275: ('python:len(items)', 31, 42), 1326: (' portal_state/membe', 32, 32), 1391: ('s context/portal_properties/site_properties/visible_ids|nothi', 33, 43), 1498: ("ds python:member.getProperty('visible_ids', context.portal_memberdata.getProperty('visible_ids", 34, 42), 1226: ('items', 30, 37), 1662: ('items', 36, 43), 1726: ('python:plone_view.normalizeString(item.portal_type)', 37, 56), 1826: (" python:'(%s)' % item.getId if (portal_visible_ids and member_visible_ids) else '", 38, 47), 2038: ('item/getId', 40, 54), 2100: (' item/getI', 41, 50), 2167: ("d python: (n_items==1 or item.getId==cur_page) and 'checked' or No", 42, 54), 2295: ('item/getId', 43, 55), 2363: (' string:contenttype-${normalized_type', 44, 56), 2451: ('string:${item/pretty_title_or_id} $item_id', 45, 48), 2647: ('item/Description', 49, 41), 3535: ('not:nocall:items', 72, 36), 255: ('context/main_template/macros/master', 5, 23), 255: ('context/main_template/macros/master', 5, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque

_static_4887825904 = {'class': 'context btn btn-primary', 'type': 'submit', 'name': 'form.button.Cancel', 'value': 'Ok', }
_static_4887830224 = {'class': 'formControls mb-3', }
_static_4887824752 = {'class': 'btn btn-secondary', 'type': 'submit', 'name': 'form.buttons.Cancel', 'value': 'Cancel', }
_static_4853276512 = {'class': 'context btn btn-primary', 'type': 'submit', 'name': 'form.buttons.Save', 'value': 'Save', }
_static_4902710016 = {'class': 'formControls mb-3', }
_static_4902710928 = {'for': 'item/getId', 'class': 'string:contenttype-${normalized_type}', }
_static_4902706320 = {'type': 'radio', 'name': 'objectId', 'value': '', 'id': 'item/getId', 'checked': "python: (n_items==1 or item.getId==cur_page) and 'checked' or None", }
_static_4840688944 = {'type': 'hidden', 'name': 'form.submitted', 'value': '1', }
_static_4854458368 = {'name': 'default_page_form', 'method': 'post', 'action': 'string:${context/absolute_url}/select_default_page', }
_static_4900367440 = {'id': 'content-core', }
_static_4900366576 = {'class': 'documentDescription', }
_static_4902162768 = {'class': 'documentFirstHeading', }
_static_4439051040 = __C2ZContextWrapper
_static_4439058528 = __compile_zt_expr
_static_4850969008 = 'master'
_static_4438893776 = {}

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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4850962528
            __attrs_4850962528 = _static_4438893776
            __previous_i18n_domain_4850967760 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4853218688 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x12123e9b0> name=None at 12123ce80> -> __value
            __value = _static_4850969008
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4856153904
                __attrs_4856153904 = _static_4438893776
                __backup_dummy_4850971456 = get('dummy', __marker)

                # <Value "python:request.set('disable_border',1)" (9:31)> -> __value
                __token = 385
                try:
                    __zt_tmp = __attrs_4856153904
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', "request.set('disable_border',1)", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['dummy'] = __value
                if (__backup_dummy_4850971456 is __marker):
                    del econtext['dummy']
                else:
                    econtext['dummy'] = __backup_dummy_4850971456
            _slots = econtext['__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4902158544
                __attrs_4902158544 = _static_4438893776
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x124311150> name=None at 124310070> -> __attrs_4900370416
                __attrs_4900370416 = _static_4902162768

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">')
                __stream_4902165168 = []
                __append_4902165168 = __stream_4902165168.append
                __append_4902165168('Select default page')
                __msgid_4902165168 = __re_whitespace(''.join(__stream_4902165168)).strip()
                if 'heading_select_default_page':
                    __append(translate('heading_select_default_page', mapping=None, default=__msgid_4902165168, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n\n      ')

                # <Static value=<ast.Dict object at 0x12415a8f0> name=None at 12415bfd0> -> __attrs_4900372048
                __attrs_4900372048 = _static_4900366576

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="documentDescription">')
                __stream_4900360144 = []
                __append_4900360144 = __stream_4900360144.append
                __append_4900360144('\n        Please select item which will be displayed as the default page of the\n        folder.\n      ')
                __msgid_4900360144 = __re_whitespace(''.join(__stream_4900360144)).strip()
                if 'description_select_default_page':
                    __append(translate('description_select_default_page', mapping=None, default=__msgid_4900360144, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</div>\n      ')

                # <Static value=<ast.Dict object at 0x12415ac50> name=None at 12415b160> -> __attrs_4900368832
                __attrs_4900368832 = _static_4900367440

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n          ')

                # <Static value=<ast.Dict object at 0x121592800> name=None at 121590fd0> -> __attrs_4690268928
                __attrs_4690268928 = _static_4854458368

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form name="default_page_form" method="post"')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4854909008
                __default_4854909008 = _DEFAULT_MARKER

                # <Substitution 'string:${context/absolute_url}/select_default_page' (24:39)> -> __attr_action
                __token = 929
                try:
                    __zt_tmp = __attrs_4690268928
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_action = _static_4439058528('string', '${context/absolute_url}/select_default_page', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_action is not None):
                    __append((' action="%s"' % __attr_action))
                __append('>\n\n            ')

                # <Static value=<ast.Dict object at 0x120870d30> name=None at 1208731f0> -> __attrs_4900470848
                __attrs_4900470848 = _static_4840688944

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="form.submitted" value="1"/>\n\n            ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900473680
                __attrs_4900473680 = _static_4438893776
                __backup_items_4850971072 = get('items', __marker)

                # <Value 'view/get_selectable_items' (28:37)> -> __value
                __token = 1088
                try:
                    __zt_tmp = __attrs_4900473680
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'view/get_selectable_items', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['items'] = __value
                __backup_cur_page_4697394240 = get('cur_page', __marker)

                # <Value 'context/getDefaultPage|nothing' (29:39)> -> __value
                __token = 1154
                try:
                    __zt_tmp = __attrs_4900473680
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'context/getDefaultPage|nothing', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['cur_page'] = __value
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4902713232
                __attrs_4902713232 = _static_4438893776
                __backup_n_items_4854912896 = get('n_items', __marker)

                # <Value 'python:len(items)' (31:42)> -> __value
                __token = 1275
                try:
                    __zt_tmp = __attrs_4902713232
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', 'len(items)', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['n_items'] = __value
                __backup_member_4881040528 = get('member', __marker)

                # <Value 'portal_state/member' (32:32)> -> __value
                __token = 1326
                try:
                    __zt_tmp = __attrs_4902713232
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'portal_state/member', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['member'] = __value
                __backup_portal_visible_ids_4637604592 = get('portal_visible_ids', __marker)

                # <Value 'context/portal_properties/site_properties/visible_ids|nothing' (33:43)> -> __value
                __token = 1391
                try:
                    __zt_tmp = __attrs_4902713232
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'context/portal_properties/site_properties/visible_ids|nothing', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['portal_visible_ids'] = __value
                __backup_member_visible_ids_4854912128 = get('member_visible_ids', __marker)

                # <Value "python:member.getProperty('visible_ids', context.portal_memberdata.getProperty('visible_ids'))" (34:42)> -> __value
                __token = 1498
                try:
                    __zt_tmp = __attrs_4902713232
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', "member.getProperty('visible_ids', context.portal_memberdata.getProperty('visible_ids'))", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['member_visible_ids'] = __value

                # <Value 'items' (30:37)> -> __condition
                __token = 1226
                try:
                    __zt_tmp = __attrs_4902713232
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('path', 'items', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4902714768
                    __attrs_4902714768 = _static_4438893776

                    # <dl ... (0:0)
                    # --------------------------------------------------------
                    __append('<dl>\n                    ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4902700416
                    __attrs_4902700416 = _static_4438893776
                    __backup_item_4880705680 = get('item', __marker)

                    # <Value 'items' (36:43)> -> __iterator
                    __token = 1662
                    try:
                        __zt_tmp = __attrs_4902700416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_4439058528('path', 'items', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    (__iterator, ____index_4902704016, ) = getname('repeat')('item', __iterator)
                    econtext['item'] = None
                    for __item in __iterator:
                        econtext['item'] = __item
                        __append('\n                        ')

                        # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4902708048
                        __attrs_4902708048 = _static_4438893776
                        __backup_normalized_type_4682451408 = get('normalized_type', __marker)

                        # <Value 'python:plone_view.normalizeString(item.portal_type)' (37:56)> -> __value
                        __token = 1726
                        try:
                            __zt_tmp = __attrs_4902708048
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4439058528('python', 'plone_view.normalizeString(item.portal_type)', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        econtext['normalized_type'] = __value
                        __backup_item_id_4881537856 = get('item_id', __marker)

                        # <Value "python:'(%s)' % item.getId if (portal_visible_ids and member_visible_ids) else ''" (38:47)> -> __value
                        __token = 1826
                        try:
                            __zt_tmp = __attrs_4902708048
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4439058528('python', "'(%s)' % item.getId if (portal_visible_ids and member_visible_ids) else ''", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        econtext['item_id'] = __value

                        # <dt ... (0:0)
                        # --------------------------------------------------------
                        __append('<dt>\n                            ')

                        # <Static value=<ast.Dict object at 0x124395c90> name=None at 124397e80> -> __attrs_4902706128
                        __attrs_4902706128 = _static_4902706320

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="radio" name="objectId"')

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4902714480
                        __default_4902714480 = _DEFAULT_MARKER

                        # <Substitution 'item/getId' (40:54)> -> __attr_value
                        __token = 2038
                        try:
                            __zt_tmp = __attrs_4902706128
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_4439058528('path', 'item/getId', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4902703152
                        __default_4902703152 = _DEFAULT_MARKER

                        # <Substitution 'item/getId' (41:50)> -> __attr_id
                        __token = 2100
                        try:
                            __zt_tmp = __attrs_4902706128
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_4439058528('path', 'item/getId', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((' id="%s"' % __attr_id))

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4902709920
                        __default_4902709920 = _DEFAULT_MARKER

                        # <Boolean "python: (n_items==1 or item.getId==cur_page) and 'checked' or None" (42:54)> -> __attr_checked
                        __token = 2167
                        try:
                            __zt_tmp = __attrs_4902706128
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_checked = _static_4439058528('python', " (n_items==1 or item.getId==cur_page) and 'checked' or None", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        if (__attr_checked is _DEFAULT_MARKER):
                            __attr_checked = None
                        else:
                            if __attr_checked:
                                __attr_checked = 'checked'
                            else:
                                __attr_checked = None
                        if (__attr_checked is not None):
                            __append((' checked="%s"' % __attr_checked))
                        __append('/>\n                            ')

                        # <Static value=<ast.Dict object at 0x124396e90> name=None at 124396c80> -> __attrs_4888046480
                        __attrs_4888046480 = _static_4902710928

                        # <label ... (0:0)
                        # --------------------------------------------------------
                        __append('<label')

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4902714192
                        __default_4902714192 = _DEFAULT_MARKER

                        # <Substitution 'item/getId' (43:55)> -> __attr_for
                        __token = 2295
                        try:
                            __zt_tmp = __attrs_4888046480
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_for = _static_4439058528('path', 'item/getId', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_for is not None):
                            __append((' for="%s"' % __attr_for))

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4888049456
                        __default_4888049456 = _DEFAULT_MARKER

                        # <Substitution 'string:contenttype-${normalized_type}' (44:56)> -> __attr_class
                        __token = 2363
                        try:
                            __zt_tmp = __attrs_4888046480
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_4439058528('string', 'contenttype-${normalized_type}', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))
                        __append('>')

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4902714816
                        __default_4902714816 = _DEFAULT_MARKER

                        # <Value 'string:${item/pretty_title_or_id} $item_id' (45:48)> -> __cache_4902709536
                        __token = 2451
                        try:
                            __zt_tmp = __attrs_4888046480
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4902709536 = _static_4439058528('string', '${item/pretty_title_or_id} $item_id', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                        # <BinOp left=<Value 'string:${item/pretty_title_or_id} $item_id' (45:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 124395450> -> __condition
                        __expression = __cache_4902709536

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n                                Item title\n                            ')
                        else:
                            __content = __cache_4902709536
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</label>\n                        </dt>')
                        if (__backup_item_id_4881537856 is __marker):
                            del econtext['item_id']
                        else:
                            econtext['item_id'] = __backup_item_id_4881537856
                        if (__backup_normalized_type_4682451408 is __marker):
                            del econtext['normalized_type']
                        else:
                            econtext['normalized_type'] = __backup_normalized_type_4682451408
                        __append('\n                        ')

                        # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4888050032
                        __attrs_4888050032 = _static_4438893776

                        # <dd ... (0:0)
                        # --------------------------------------------------------
                        __append('<dd>')

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4888036352
                        __default_4888036352 = _DEFAULT_MARKER

                        # <Value 'item/Description' (49:41)> -> __cache_4888037024
                        __token = 2647
                        try:
                            __zt_tmp = __attrs_4888050032
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4888037024 = _static_4439058528('path', 'item/Description', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                        # <BinOp left=<Value 'item/Description' (49:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 12359ad40> -> __condition
                        __expression = __cache_4888037024

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n                            Item Description\n                        ')
                        else:
                            __content = __cache_4888037024
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</dd>\n                    ')
                        ____index_4902704016 -= 1
                        if (____index_4902704016 > 0):
                            __append('')
                    if (__backup_item_4880705680 is __marker):
                        del econtext['item']
                    else:
                        econtext['item'] = __backup_item_4880705680
                    __append('\n\n                </dl>\n\n              ')

                    # <Static value=<ast.Dict object at 0x124396b00> name=None at 124396d70> -> __attrs_4888044800
                    __attrs_4888044800 = _static_4902710016

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="formControls mb-3">\n                ')

                    # <Static value=<ast.Dict object at 0x121471f60> name=None at 112976200> -> __attrs_4887829168
                    __attrs_4887829168 = _static_4853276512

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="context btn btn-primary" type="submit" name="form.buttons.Save"')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4888046432
                    __default_4888046432 = _DEFAULT_MARKER

                    # <Translate msgid='label_save' node=<ast.Constant object at 0x12359b220> at 12359b6d0> -> __attr_value
                    __attr_value = 'Save'
                    __attr_value = translate('label_save', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append('>')
                    __stream_4888043360 = []
                    __append_4888043360 = __stream_4888043360.append
                    __append_4888043360('Save')
                    __msgid_4888043360 = __re_whitespace(''.join(__stream_4888043360)).strip()
                    if 'label_save':
                        __append(translate('label_save', mapping=None, default=__msgid_4888043360, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n                ')

                    # <Static value=<ast.Dict object at 0x123564970> name=None at 123564760> -> __attrs_4887822400
                    __attrs_4887822400 = _static_4887824752

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="btn btn-secondary" type="submit" name="form.buttons.Cancel"')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4887823696
                    __default_4887823696 = _DEFAULT_MARKER

                    # <Translate msgid='label_cancel' node=<ast.Constant object at 0x1235656c0> at 123564520> -> __attr_value
                    __attr_value = 'Cancel'
                    __attr_value = translate('label_cancel', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append('>')
                    __stream_4887827968 = []
                    __append_4887827968 = __stream_4887827968.append
                    __append_4887827968('Cancel')
                    __msgid_4887827968 = __re_whitespace(''.join(__stream_4887827968)).strip()
                    if 'label_cancel':
                        __append(translate('label_cancel', mapping=None, default=__msgid_4887827968, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n              </div>\n\n            ')
                if (__backup_member_visible_ids_4854912128 is __marker):
                    del econtext['member_visible_ids']
                else:
                    econtext['member_visible_ids'] = __backup_member_visible_ids_4854912128
                if (__backup_portal_visible_ids_4637604592 is __marker):
                    del econtext['portal_visible_ids']
                else:
                    econtext['portal_visible_ids'] = __backup_portal_visible_ids_4637604592
                if (__backup_member_4881040528 is __marker):
                    del econtext['member']
                else:
                    econtext['member'] = __backup_member_4881040528
                if (__backup_n_items_4854912896 is __marker):
                    del econtext['n_items']
                else:
                    econtext['n_items'] = __backup_n_items_4854912896
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4887827776
                __attrs_4887827776 = _static_4438893776

                # <Value 'not:nocall:items' (72:36)> -> __condition
                __token = 3535
                try:
                    __zt_tmp = __attrs_4887827776
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('not', 'nocall:items', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:
                    __append('\n              ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4887830176
                    __attrs_4887830176 = _static_4438893776

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div>')
                    __stream_4887830032 = []
                    __append_4887830032 = __stream_4887830032.append
                    __append_4887830032('\n                 There are no items in this folder that can be selected as\n                 a default view page.\n              ')
                    __msgid_4887830032 = __re_whitespace(''.join(__stream_4887830032)).strip()
                    if 'help_no_selectable_default_pages':
                        __append(translate('help_no_selectable_default_pages', mapping=None, default=__msgid_4887830032, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</div>\n              ')

                    # <Static value=<ast.Dict object at 0x123565ed0> name=None at 123565fc0> -> __attrs_4887831376
                    __attrs_4887831376 = _static_4887830224

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="formControls mb-3">\n                    ')

                    # <Static value=<ast.Dict object at 0x123564df0> name=None at 123564a30> -> __attrs_4887830944
                    __attrs_4887830944 = _static_4887825904

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="context btn btn-primary" type="submit" name="form.button.Cancel"')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4887827104
                    __default_4887827104 = _DEFAULT_MARKER

                    # <Translate msgid='label_ok' node=<ast.Constant object at 0x123564ac0> at 123564e20> -> __attr_value
                    __attr_value = 'Ok'
                    __attr_value = translate('label_ok', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append('>')
                    __stream_4887831664 = []
                    __append_4887831664 = __stream_4887831664.append
                    __append_4887831664('Ok')
                    __msgid_4887831664 = __re_whitespace(''.join(__stream_4887831664)).strip()
                    if 'label_ok':
                        __append(translate('label_ok', mapping=None, default=__msgid_4887831664, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n              </div>\n            ')
                __append('\n            ')
                if (__backup_cur_page_4697394240 is __marker):
                    del econtext['cur_page']
                else:
                    econtext['cur_page'] = __backup_cur_page_4697394240
                if (__backup_items_4850971072 is __marker):
                    del econtext['items']
                else:
                    econtext['items'] = __backup_items_4850971072
                __append('\n\n          </form>\n      </div>\n\n    ')
            _slots = econtext['__slot_main'] = _deque((__fill_main, ))

            # <Value 'context/main_template/macros/master' (5:23)> -> __macro
            __token = 255
            try:
                __zt_tmp = __attrs_4850962528
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4439058528('path', 'context/main_template/macros/master', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __token = 255
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4853218688 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4853218688
            __i18n_domain = __previous_i18n_domain_4850967760
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }