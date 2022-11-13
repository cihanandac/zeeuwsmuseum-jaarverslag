# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/dexterity/browser/folder_listing.pt'

__tokens = {489: ('view/batch', 14, 31), 532: ('batch', 15, 30), 4853: ('context/batch_macros/macros/navigation', 98, 30), 4853: ('context/batch_macros/macros/navigation', 98, 30), 5034: ('not: view/batch', 104, 27), 5076: ('view/no_items_message', 105, 25), 633: ('batch', 17, 35), 709: ('item/getObject', 18, 39), 749: (' item/getUR', 19, 24), 785: ('d item/get', 20, 22), 823: ('le item/Ti', 21, 24), 867: ('ion item/Descrip', 22, 29), 910: ('type item/Porta', 23, 21), 956: ('ified item/Modificati', 24, 24), 1007: ('reated item/Creat', 25, 22), 1057: ("e_class python:'contenttype-' + view.normalizeString(it", 26, 24), 1143: ('wf_state item/rev', 27, 21), 1197: ("ate_class python:'state-' + view.normalizeString(item", 28, 26), 1280: ('em_creator i', 29, 18), 1319: ("  item_link python:item_type in view.use_view_action and item_url+'/view'", 30, 14), 1424: ('em_has_image python', 31, 18), 4575: ('item_description', 88, 37), 4628: ('item_description', 89, 35), 1668: ('item_type', 35, 64), 1725: ('item_link', 36, 45), 1827: ('item_has_image', 38, 44), 1893: ('string:$item_url/@@images/image/tile', 39, 50), 2005: ('item_link', 41, 46), 2062: (' string:$item_type_class $item_wf_state_class ur', 42, 46), 2158: ('e item_ty', 43, 45), 2210: ('python: item_title or item_id', 44, 39), 2508: ('view/show_about', 51, 47), 2674: ('python:view.pas_member.info(item_creator)', 54, 49), 2777: (' author/usernam', 55, 60), 2853: ('m string:?author=${author/usernam', 56, 58), 2947: ("id python:'/' in creator_short_f", 57, 57), 3033: ('_id python:(creator_short_form, creator_long_form)[creator_is_ope', 58, 49), 2611: ('item_creator', 53, 51), 3424: ('not:author', 63, 46), 3255: ('string:${view/navigation_root_url}/author/${item_creator}', 61, 52), 3359: ('author/name_or_id', 62, 45), 3857: ('python:view.toLocalizedTime(item_modified,long_format=1)', 73, 47), 4180: ('nothing', 79, 50), 251: ('context/@@main_template/macros/master', 6, 21), 251: ('context/@@main_template/macros/master', 6, 21)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_4901250208 = 'master'
_static_4901616704 = {'href': 'string:${view/navigation_root_url}/author/${item_creator}', }
_static_4901605376 = {'class': 'documentByLine', }
_static_4900692288 = {'href': 'item_link', 'class': 'string:$item_type_class $item_wf_state_class url', 'title': 'item_type', }
_static_4900696128 = {'class': 'image-tile', 'src': 'string:$item_url/@@images/image/tile', }
_static_4900695840 = {'href': 'item_link', }
_static_4900695024 = {'class': 'summary', 'title': 'item_type', }
_static_4901615840 = {'class': 'description discreet', }
_static_4900683984 = {'class': 'entry', }
_static_4900721120 = {'class': 'discreet', }
_static_4900694352 = 'navigation'
_static_4901256688 = {'class': 'entries', }
_static_4439051040 = __C2ZContextWrapper
_static_4439058528 = __compile_zt_expr
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

    def render_content_core(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901255008
            __attrs_4901255008 = _static_4438893776
            __append('\n\n  ')
            __token = None
            render_listing(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_listing(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_entries = econtext['__slot_entries'].pop()
        except:
            __slot_entries = None

        try:
            __slot_no_items_in_listing = econtext['__slot_no_items_in_listing'].pop()
        except:
            __slot_no_items_in_listing = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901254096
            __attrs_4901254096 = _static_4438893776
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901252080
            __attrs_4901252080 = _static_4438893776
            __backup_batch_4638433840 = get('batch', __marker)

            # <Value 'view/batch' (14:31)> -> __value
            __token = 489
            try:
                __zt_tmp = __attrs_4901252080
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'view/batch', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['batch'] = __value
            __append('\n      ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901255920
            __attrs_4901255920 = _static_4438893776

            # <Value 'batch' (15:30)> -> __condition
            __token = 532
            try:
                __zt_tmp = __attrs_4901255920
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4439058528('path', 'batch', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            if __condition:
                __append('\n        ')
                if (__slot_entries is None):

                    # <Static value=<ast.Dict object at 0x124233df0> name=None at 124231c00> -> __attrs_4900694544
                    __attrs_4900694544 = _static_4901256688

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="entries">\n          ')
                    __token = None
                    render_entries(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    __append('\n        </div>')
                else:
                    __slot_entries(__stream, econtext.copy(), rcontext)
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900699968
                __attrs_4900699968 = _static_4438893776
                __backup_macroname_4902387072 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x1241aa950> name=None at 1241aa0e0> -> __value
                __value = _static_4900694352
                econtext['macroname'] = __value

                # <Value 'context/batch_macros/macros/navigation' (98:30)> -> __macro
                __token = 4853
                try:
                    __zt_tmp = __attrs_4900699968
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_4439058528('path', 'context/batch_macros/macros/navigation', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __token = 4853
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_4902387072 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_4902387072
                __append('\n\n      ')
            __append('\n\n      ')
            if (__slot_no_items_in_listing is None):

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900688976
                __attrs_4900688976 = _static_4438893776
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x1241b11e0> name=None at 1241b0fa0> -> __attrs_4900717136
                __attrs_4900717136 = _static_4900721120

                # <Value 'not: view/batch' (104:27)> -> __condition
                __token = 5034
                try:
                    __zt_tmp = __attrs_4900717136
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('not', ' view/batch', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="discreet">')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900730624
                    __default_4900730624 = _DEFAULT_MARKER

                    # <Value 'view/no_items_message' (105:25)> -> __cache_4900720496
                    __token = 5076
                    try:
                        __zt_tmp = __attrs_4900717136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4900720496 = _static_4439058528('path', 'view/no_items_message', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/no_items_message' (105:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1241b1c90> -> __condition
                    __expression = __cache_4900720496

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n          There are currently no items in this folder.\n        ')
                    else:
                        __content = __cache_4900720496
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</p>')
                __append('\n      ')
            else:
                __slot_no_items_in_listing(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')
            if (__backup_batch_4638433840 is __marker):
                del econtext['batch']
            else:
                econtext['batch'] = __backup_batch_4638433840
            __append('\n  ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_entries(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_entry = econtext['__slot_entry'].pop()
        except:
            __slot_entry = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900692240
            __attrs_4900692240 = _static_4438893776
            __backup_item_4638435136 = get('item', __marker)

            # <Value 'batch' (17:35)> -> __iterator
            __token = 633
            try:
                __zt_tmp = __attrs_4900692240
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4439058528('path', 'batch', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            (__iterator, ____index_4900693680, ) = getname('repeat')('item', __iterator)
            econtext['item'] = None
            for __item in __iterator:
                econtext['item'] = __item
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900698720
                __attrs_4900698720 = _static_4438893776
                __backup_obj_4880698096 = get('obj', __marker)

                # <Value 'item/getObject' (18:39)> -> __value
                __token = 709
                try:
                    __zt_tmp = __attrs_4900698720
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'item/getObject', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['obj'] = __value
                __backup_item_url_4874873456 = get('item_url', __marker)

                # <Value 'item/getURL' (19:24)> -> __value
                __token = 749
                try:
                    __zt_tmp = __attrs_4900698720
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'item/getURL', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['item_url'] = __value
                __backup_item_id_4900474400 = get('item_id', __marker)

                # <Value 'item/getId' (20:22)> -> __value
                __token = 785
                try:
                    __zt_tmp = __attrs_4900698720
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'item/getId', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['item_id'] = __value
                __backup_item_title_4850898672 = get('item_title', __marker)

                # <Value 'item/Title' (21:24)> -> __value
                __token = 823
                try:
                    __zt_tmp = __attrs_4900698720
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'item/Title', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['item_title'] = __value
                __backup_item_description_4874875088 = get('item_description', __marker)

                # <Value 'item/Description' (22:29)> -> __value
                __token = 867
                try:
                    __zt_tmp = __attrs_4900698720
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'item/Description', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['item_description'] = __value
                __backup_item_type_4879973152 = get('item_type', __marker)

                # <Value 'item/PortalType' (23:21)> -> __value
                __token = 910
                try:
                    __zt_tmp = __attrs_4900698720
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'item/PortalType', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['item_type'] = __value
                __backup_item_modified_4879973248 = get('item_modified', __marker)

                # <Value 'item/ModificationDate' (24:24)> -> __value
                __token = 956
                try:
                    __zt_tmp = __attrs_4900698720
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'item/ModificationDate', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['item_modified'] = __value
                __backup_item_created_4879973488 = get('item_created', __marker)

                # <Value 'item/CreationDate' (25:22)> -> __value
                __token = 1007
                try:
                    __zt_tmp = __attrs_4900698720
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'item/CreationDate', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['item_created'] = __value
                __backup_item_type_class_4875792976 = get('item_type_class', __marker)

                # <Value "python:'contenttype-' + view.normalizeString(item_type)" (26:24)> -> __value
                __token = 1057
                try:
                    __zt_tmp = __attrs_4900698720
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', "'contenttype-' + view.normalizeString(item_type)", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['item_type_class'] = __value
                __backup_item_wf_state_4875791824 = get('item_wf_state', __marker)

                # <Value 'item/review_state' (27:21)> -> __value
                __token = 1143
                try:
                    __zt_tmp = __attrs_4900698720
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'item/review_state', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['item_wf_state'] = __value
                __backup_item_wf_state_class_4875788752 = get('item_wf_state_class', __marker)

                # <Value "python:'state-' + view.normalizeString(item_wf_state)" (28:26)> -> __value
                __token = 1197
                try:
                    __zt_tmp = __attrs_4900698720
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', "'state-' + view.normalizeString(item_wf_state)", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['item_wf_state_class'] = __value
                __backup_item_creator_4840696048 = get('item_creator', __marker)

                # <Value 'item/Creator' (29:18)> -> __value
                __token = 1280
                try:
                    __zt_tmp = __attrs_4900698720
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'item/Creator', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['item_creator'] = __value
                __backup_item_link_4840688896 = get('item_link', __marker)

                # <Value "python:item_type in view.use_view_action and item_url+'/view' or item_url" (30:14)> -> __value
                __token = 1319
                try:
                    __zt_tmp = __attrs_4900698720
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', "item_type in view.use_view_action and item_url+'/view' or item_url", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['item_link'] = __value
                __backup_item_has_image_4840701856 = get('item_has_image', __marker)

                # <Value 'python:item.getIcon' (31:18)> -> __value
                __token = 1424
                try:
                    __zt_tmp = __attrs_4900698720
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', 'item.getIcon', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['item_has_image'] = __value
                __append('\n              ')
                if (__slot_entry is None):

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900689792
                    __attrs_4900689792 = _static_4438893776
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x1241a80d0> name=None at 1241a8490> -> __attrs_4900686768
                    __attrs_4900686768 = _static_4900683984

                    # <article ... (0:0)
                    # --------------------------------------------------------
                    __append('<article class="entry">\n                  ')
                    __token = None
                    render_listitem(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    __append('\n                  ')

                    # <Static value=<ast.Dict object at 0x12428b8e0> name=None at 124289e40> -> __attrs_4901615504
                    __attrs_4901615504 = _static_4901615840

                    # <Value 'item_description' (88:37)> -> __condition
                    __token = 4575
                    try:
                        __zt_tmp = __attrs_4901615504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4439058528('path', 'item_description', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    if __condition:

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append('<p class="description discreet">')

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901603936
                        __default_4901603936 = _DEFAULT_MARKER

                        # <Value 'item_description' (89:35)> -> __cache_4901607200
                        __token = 4628
                        try:
                            __zt_tmp = __attrs_4901615504
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4901607200 = _static_4439058528('path', 'item_description', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                        # <BinOp left=<Value 'item_description' (89:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 12428b2e0> -> __condition
                        __expression = __cache_4901607200

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n                    description\n                  ')
                        else:
                            __content = __cache_4901607200
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</p>')
                    __append('\n                </article>\n              ')
                else:
                    __slot_entry(__stream, econtext.copy(), rcontext)
                __append('\n            ')
                if (__backup_item_has_image_4840701856 is __marker):
                    del econtext['item_has_image']
                else:
                    econtext['item_has_image'] = __backup_item_has_image_4840701856
                if (__backup_item_link_4840688896 is __marker):
                    del econtext['item_link']
                else:
                    econtext['item_link'] = __backup_item_link_4840688896
                if (__backup_item_creator_4840696048 is __marker):
                    del econtext['item_creator']
                else:
                    econtext['item_creator'] = __backup_item_creator_4840696048
                if (__backup_item_wf_state_class_4875788752 is __marker):
                    del econtext['item_wf_state_class']
                else:
                    econtext['item_wf_state_class'] = __backup_item_wf_state_class_4875788752
                if (__backup_item_wf_state_4875791824 is __marker):
                    del econtext['item_wf_state']
                else:
                    econtext['item_wf_state'] = __backup_item_wf_state_4875791824
                if (__backup_item_type_class_4875792976 is __marker):
                    del econtext['item_type_class']
                else:
                    econtext['item_type_class'] = __backup_item_type_class_4875792976
                if (__backup_item_created_4879973488 is __marker):
                    del econtext['item_created']
                else:
                    econtext['item_created'] = __backup_item_created_4879973488
                if (__backup_item_modified_4879973248 is __marker):
                    del econtext['item_modified']
                else:
                    econtext['item_modified'] = __backup_item_modified_4879973248
                if (__backup_item_type_4879973152 is __marker):
                    del econtext['item_type']
                else:
                    econtext['item_type'] = __backup_item_type_4879973152
                if (__backup_item_description_4874875088 is __marker):
                    del econtext['item_description']
                else:
                    econtext['item_description'] = __backup_item_description_4874875088
                if (__backup_item_title_4850898672 is __marker):
                    del econtext['item_title']
                else:
                    econtext['item_title'] = __backup_item_title_4850898672
                if (__backup_item_id_4900474400 is __marker):
                    del econtext['item_id']
                else:
                    econtext['item_id'] = __backup_item_id_4900474400
                if (__backup_item_url_4874873456 is __marker):
                    del econtext['item_url']
                else:
                    econtext['item_url'] = __backup_item_url_4874873456
                if (__backup_obj_4880698096 is __marker):
                    del econtext['obj']
                else:
                    econtext['obj'] = __backup_obj_4880698096
                __append('\n          ')
                ____index_4900693680 -= 1
                if (____index_4900693680 > 0):
                    __append('')
            if (__backup_item_4638435136 is __marker):
                del econtext['item']
            else:
                econtext['item'] = __backup_item_4638435136
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_listitem(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900689168
            __attrs_4900689168 = _static_4438893776

            # <header ... (0:0)
            # --------------------------------------------------------
            __append('<header>\n                    ')

            # <Static value=<ast.Dict object at 0x1241aabf0> name=None at 1241a9270> -> __attrs_4900694256
            __attrs_4900694256 = _static_4900695024

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span class="summary"')

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900689408
            __default_4900689408 = _DEFAULT_MARKER

            # <Substitution 'item_type' (35:64)> -> __attr_title
            __token = 1668
            try:
                __zt_tmp = __attrs_4900694256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_4439058528('path', 'item_type', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append('>\n                     ')

            # <Static value=<ast.Dict object at 0x1241aaf20> name=None at 1241ab430> -> __attrs_4900699296
            __attrs_4900699296 = _static_4900695840

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900698288
            __default_4900698288 = _DEFAULT_MARKER

            # <Substitution 'item_link' (36:45)> -> __attr_href
            __token = 1725
            try:
                __zt_tmp = __attrs_4900699296
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4439058528('path', 'item_link', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append('>\n                      ')

            # <Static value=<ast.Dict object at 0x1241ab040> name=None at 1241ab7c0> -> __attrs_4900699824
            __attrs_4900699824 = _static_4900696128

            # <Value 'item_has_image' (38:44)> -> __condition
            __token = 1827
            try:
                __zt_tmp = __attrs_4900699824
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4439058528('path', 'item_has_image', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            if __condition:

                # <img ... (0:0)
                # --------------------------------------------------------
                __append('<img class="image-tile"')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900698432
                __default_4900698432 = _DEFAULT_MARKER

                # <Substitution 'string:$item_url/@@images/image/tile' (39:50)> -> __attr_src
                __token = 1893
                try:
                    __zt_tmp = __attrs_4900699824
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_src = _static_4439058528('string', '$item_url/@@images/image/tile', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_src is not None):
                    __append((' src="%s"' % __attr_src))
                __append('>')
            __append('\n                      </a>\n                      ')

            # <Static value=<ast.Dict object at 0x1241aa140> name=None at 1241a9ed0> -> __attrs_4901615072
            __attrs_4901615072 = _static_4900692288

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900697568
            __default_4900697568 = _DEFAULT_MARKER

            # <Substitution 'item_link' (41:46)> -> __attr_href
            __token = 2005
            try:
                __zt_tmp = __attrs_4901615072
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4439058528('path', 'item_link', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901611904
            __default_4901611904 = _DEFAULT_MARKER

            # <Substitution 'string:$item_type_class $item_wf_state_class url' (42:46)> -> __attr_class
            __token = 2062
            try:
                __zt_tmp = __attrs_4901615072
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4439058528('string', '$item_type_class $item_wf_state_class url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901617568
            __default_4901617568 = _DEFAULT_MARKER

            # <Substitution 'item_type' (43:45)> -> __attr_title
            __token = 2158
            try:
                __zt_tmp = __attrs_4901615072
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_4439058528('path', 'item_type', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append('>')

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900692720
            __default_4900692720 = _DEFAULT_MARKER

            # <Value 'python: item_title or item_id' (44:39)> -> __cache_4900691376
            __token = 2210
            try:
                __zt_tmp = __attrs_4901615072
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4900691376 = _static_4439058528('python', ' item_title or item_id', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

            # <BinOp left=<Value 'python: item_title or item_id' (44:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1241a9f60> -> __condition
            __expression = __cache_4900691376

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('\n\n                             Item Title\n                      ')
            else:
                __content = __cache_4900691376
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</a>\n                     </span>\n                    ')
            __token = None
            render_document_byline(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n                  </header>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_document_byline(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_description_slot = econtext['__slot_description_slot'].pop()
        except:
            __slot_description_slot = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901612864
            __attrs_4901612864 = _static_4438893776
            __append('\n                      ')

            # <Static value=<ast.Dict object at 0x124289000> name=None at 1242893c0> -> __attrs_4901611616
            __attrs_4901611616 = _static_4901605376

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="documentByLine">\n                        ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901605520
            __attrs_4901605520 = _static_4438893776

            # <Value 'view/show_about' (51:47)> -> __condition
            __token = 2508
            try:
                __zt_tmp = __attrs_4901605520
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4439058528('path', 'view/show_about', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            if __condition:
                __append('\n                          &mdash;\n                          ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901616800
                __attrs_4901616800 = _static_4438893776
                __backup_author_4851428144 = get('author', __marker)

                # <Value 'python:view.pas_member.info(item_creator)' (54:49)> -> __value
                __token = 2674
                try:
                    __zt_tmp = __attrs_4901616800
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', 'view.pas_member.info(item_creator)', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['author'] = __value
                __backup_creator_short_form_4636972064 = get('creator_short_form', __marker)

                # <Value 'author/username' (55:60)> -> __value
                __token = 2777
                try:
                    __zt_tmp = __attrs_4901616800
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'author/username', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['creator_short_form'] = __value
                __backup_creator_long_form_4682921536 = get('creator_long_form', __marker)

                # <Value 'string:?author=${author/username}' (56:58)> -> __value
                __token = 2853
                try:
                    __zt_tmp = __attrs_4901616800
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('string', '?author=${author/username}', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['creator_long_form'] = __value
                __backup_creator_is_openid_4879767472 = get('creator_is_openid', __marker)

                # <Value "python:'/' in creator_short_form" (57:57)> -> __value
                __token = 2947
                try:
                    __zt_tmp = __attrs_4901616800
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', "'/' in creator_short_form", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['creator_is_openid'] = __value
                __backup_creator_id_4879768192 = get('creator_id', __marker)

                # <Value 'python:(creator_short_form, creator_long_form)[creator_is_openid]' (58:49)> -> __value
                __token = 3033
                try:
                    __zt_tmp = __attrs_4901616800
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', '(creator_short_form, creator_long_form)[creator_is_openid]', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['creator_id'] = __value

                # <Value 'item_creator' (53:51)> -> __condition
                __token = 2611
                try:
                    __zt_tmp = __attrs_4901616800
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('path', 'item_creator', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:
                    __append('\n                          ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901612192
                    __attrs_4901612192 = _static_4438893776

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_4900565312_author = ''
                    __stream_4901601728 = []
                    __append_4901601728 = __stream_4901601728.append
                    __append_4901601728('\n                            by\n                            ')
                    __stream_4900565312_author = []
                    __append_4900565312_author = __stream_4900565312_author.append

                    # <Static value=<ast.Dict object at 0x12428bc40> name=None at 12428a020> -> __attrs_4901608544
                    __attrs_4901608544 = _static_4901616704

                    # <Negate value=<Value 'not:author' (63:46)> at 12428aef0> -> __cache_4901613296

                    # <Value 'not:author' (63:46)> -> __cache_4901613296
                    __token = 3424
                    try:
                        __zt_tmp = __attrs_4901608544
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4901613296 = _static_4439058528('not', 'author', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    __cache_4901613296 = not __cache_4901613296
                    __condition = __cache_4901613296
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append_4900565312_author('<a')

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901602592
                        __default_4901602592 = _DEFAULT_MARKER

                        # <Substitution 'string:${view/navigation_root_url}/author/${item_creator}' (61:52)> -> __attr_href
                        __token = 3255
                        try:
                            __zt_tmp = __attrs_4901608544
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4439058528('string', '${view/navigation_root_url}/author/${item_creator}', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append_4900565312_author((' href="%s"' % __attr_href))
                        __append_4900565312_author('>')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901616224
                    __default_4901616224 = _DEFAULT_MARKER

                    # <Value 'author/name_or_id' (62:45)> -> __cache_4901617376
                    __token = 3359
                    try:
                        __zt_tmp = __attrs_4901608544
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4901617376 = _static_4439058528('path', 'author/name_or_id', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value 'author/name_or_id' (62:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 12428a800> -> __condition
                    __expression = __cache_4901617376

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append_4900565312_author('\n                              Bob Dobalina\n                            ')
                    else:
                        __content = __cache_4901617376
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_4900565312_author(__content)
                    __condition = __cache_4901613296
                    if __condition:
                        __append_4900565312_author('</a>')
                    __append_4901601728('${author}')
                    __stream_4900565312_author = ''.join(__stream_4900565312_author)
                    __append_4901601728('\n                          ')
                    __msgid_4901601728 = __re_whitespace(''.join(__stream_4901601728)).strip()
                    if 'label_by_author':
                        __append(translate('label_by_author', mapping={'author': __stream_4900565312_author, }, default=__msgid_4901601728, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n                          ')
                if (__backup_creator_id_4879768192 is __marker):
                    del econtext['creator_id']
                else:
                    econtext['creator_id'] = __backup_creator_id_4879768192
                if (__backup_creator_is_openid_4879767472 is __marker):
                    del econtext['creator_is_openid']
                else:
                    econtext['creator_is_openid'] = __backup_creator_is_openid_4879767472
                if (__backup_creator_long_form_4682921536 is __marker):
                    del econtext['creator_long_form']
                else:
                    econtext['creator_long_form'] = __backup_creator_long_form_4682921536
                if (__backup_creator_short_form_4636972064 is __marker):
                    del econtext['creator_short_form']
                else:
                    econtext['creator_short_form'] = __backup_creator_short_form_4636972064
                if (__backup_author_4851428144 is __marker):
                    del econtext['author']
                else:
                    econtext['author'] = __backup_author_4851428144
                __append('\n\n                          ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901609936
                __attrs_4901609936 = _static_4438893776
                __append('\n                            &mdash;\n                            ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901604992
                __attrs_4901604992 = _static_4438893776
                __stream_4901610176 = []
                __append_4901610176 = __stream_4901610176.append
                __append_4901610176('last modified')
                __msgid_4901610176 = __re_whitespace(''.join(__stream_4901610176)).strip()
                if 'box_last_modified':
                    __append(translate('box_last_modified', mapping=None, default=__msgid_4901610176, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n                            ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901611184
                __attrs_4901611184 = _static_4438893776

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901605952
                __default_4901605952 = _DEFAULT_MARKER

                # <Value 'python:view.toLocalizedTime(item_modified,long_format=1)' (73:47)> -> __cache_4901605856
                __token = 3857
                try:
                    __zt_tmp = __attrs_4901611184
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4901605856 = _static_4439058528('python', 'view.toLocalizedTime(item_modified,long_format=1)', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:view.toLocalizedTime(item_modified,long_format=1)' (73:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 124288b80> -> __condition
                __expression = __cache_4901605856

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>\n                              August 16, 2001 at 23:35:59\n                            </span>')
                else:
                    __content = __cache_4901605856
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('\n                          \n\n                          ')
                if (__slot_description_slot is None):

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901615696
                    __attrs_4901615696 = _static_4438893776
                    __append('\n                            ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901615408
                    __attrs_4901615408 = _static_4438893776

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901605424
                    __default_4901605424 = _DEFAULT_MARKER

                    # <Value 'nothing' (79:50)> -> __cache_4901603360
                    __token = 4180
                    try:
                        __zt_tmp = __attrs_4901615408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4901603360 = _static_4439058528('path', 'nothing', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (79:50)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 124288790> -> __condition
                    __expression = __cache_4901603360

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                              Place custom listing info for custom types here\n                            ')
                    else:
                        __content = __cache_4901603360
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n                          ')
                else:
                    __slot_description_slot(__stream, econtext.copy(), rcontext)
                __append('\n                        ')
            __append('\n                      </div>\n                    ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901249824
            __attrs_4901249824 = _static_4438893776
            __previous_i18n_domain_4901246272 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4902547200 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x1242324a0> name=None at 124230d00> -> __value
            __value = _static_4901250208
            econtext['macroname'] = __value

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901251600
                __attrs_4901251600 = _static_4438893776
                __append('\n')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/@@main_template/macros/master' (6:21)> -> __macro
            __token = 251
            try:
                __zt_tmp = __attrs_4901249824
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4439058528('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __token = 251
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4902547200 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4902547200
            __i18n_domain = __previous_i18n_domain_4901246272
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render_listing': render_listing, 'render_entries': render_entries, 'render_listitem': render_listitem, 'render_document_byline': render_document_byline, 'render': render, }