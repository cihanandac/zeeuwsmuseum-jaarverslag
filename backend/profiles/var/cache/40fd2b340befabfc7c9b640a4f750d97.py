# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/portlets/portlets/navigation_recurse.pt'

__tokens = {567: ('context/@@plone_portal_state/portal', 12, 23), 634: (' portal/@@image_scal', 13, 30), 684: ('children', 14, 26), 727: ('node/show_children', 15, 32), 778: (' node/childre', 16, 31), 824: ('  node/getU', 17, 30), 868: ('rl node/getRemote', 18, 29), 918: ('rl  node/useRemoteUrl | not', 19, 28), 978: ('     node/portal', 20, 27), 1027: ('      nod', 21, 26), 1069: ('       item/', 22, 25), 1114: ('nt      node/cur', 23, 24), 1163: ('ath      node/curr', 24, 23), 1214: ("ss        python:' navTreeCurrentNode' if is_curre", 25, 22), 1297: ("tr_class   python:' navTreeItemInPath' if is_in_p", 26, 21), 1379: ("older_class python:' navTreeFolderish' if show_chil", 27, 20), 1464: ('python:bottomLevel &lt;= 0 or level &lt;= botto', 28, 19), 1545: ('string:navTreeItem visualNoMarker${li_class}${li_extr_class}${li_folder_class} section-${node/normalized_id}', 29, 26), 1691: ('string:state-${node/normalized_review_state}', 31, 34), 1775: (" python:'contenttype-%s' % normalizeString(item_type) if not supress_icon else '", 32, 38), 1890: ("s python:'%s navTreeCurrentItem' % item_class if is_current else item_cla", 33, 32), 2002: ('python:item_remote_url if use_remote_url else item_url', 35, 33), 2090: (' node/Descriptio', 36, 32), 2140: ('s string:${item_class}${li_class}${li_extr_class}${li_folder_class} ${item_type_clas', 37, 31), 2267: ("python: not supress_icon and item_type != 'File'", 39, 37), 2362: ("python:icons.tag(f'contenttype/{normalizeString(item_type)}')", 40, 45), 2466: ("python: not supress_icon and item_type == 'File'", 42, 37), 2561: ("python:icons.tag(f'mimetype-{item.mime_type}')", 43, 45), 2645: ('python:has_thumb and thumb_scale', 45, 32), 2719: ("python:image_scale.tag(item, 'image', scale=thumb_scale, css_class='float-end thumb-'+thumb_scale)", 46, 40), 2852: ('node/Title', 48, 31), 2937: ('children', 50, 33), 3054: ('python: children and show_children and bottomLevel and level < bottomLevel or bottomLevel == 0', 52, 31), 2986: ('string:navTree navTreeLevel${level}', 51, 38), 3196: ('python:view.recurse(children=children, level=level+1, bottomLevel=bottomLevel)', 53, 45), 26: ('options/level | python:0', 1, 26), 80: (' options/children | nothin', 2, 28), 139: ('l options/bottomLevel | nothi', 3, 30), 205: ('   view/data/no_ic', 4, 33), 260: ('b   view/data/no_th', 5, 32), 312: ('cale view/thumb_', 6, 27), 355: ('icons nocall:context/@@iconre', 7, 20), 421: ('String nocall: context/plone_utils/normaliz', 8, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4496231584 = {'class': 'string:navTree navTreeLevel${level}', }
_static_4497143456 = {'href': 'python:item_remote_url if use_remote_url else item_url', 'title': 'node/Description', 'class': 'string:${item_class}${li_class}${li_extr_class}${li_folder_class} ${item_type_class}', }
_static_4497130784 = {'class': 'string:navTreeItem visualNoMarker${li_class}${li_extr_class}${li_folder_class} section-${node/normalized_id}', }
_static_4438741184 = __C2ZContextWrapper
_static_4438540496 = __compile_zt_expr
_static_4438430896 = {}

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

    def render_nav_main(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4497133568
            __attrs_4497133568 = _static_4438430896
            __backup_portal_4496238064 = get('portal', __marker)

            # <Value 'context/@@plone_portal_state/portal' (12:23)> -> __value
            __token = 567
            try:
                __zt_tmp = __attrs_4497133568
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('path', 'context/@@plone_portal_state/portal', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['portal'] = __value
            __backup_image_scale_4495956560 = get('image_scale', __marker)

            # <Value 'portal/@@image_scale' (13:30)> -> __value
            __token = 634
            try:
                __zt_tmp = __attrs_4497133568
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('path', 'portal/@@image_scale', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['image_scale'] = __value
            __append('\n')

            # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4497130496
            __attrs_4497130496 = _static_4438430896
            __backup_node_4497133664 = get('node', __marker)

            # <Value 'children' (14:26)> -> __iterator
            __token = 684
            try:
                __zt_tmp = __attrs_4497130496
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4438540496('path', 'children', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            (__iterator, ____index_4497131984, ) = getname('repeat')('node', __iterator)
            econtext['node'] = None
            for __item in __iterator:
                econtext['node'] = __item
                __append('\n')

                # <Static value=<ast.Dict object at 0x10c0cc520> name=None at 10c0cc550> -> __attrs_4497132512
                __attrs_4497132512 = _static_4497130784
                __backup_show_children_4497130256 = get('show_children', __marker)

                # <Value 'node/show_children' (15:32)> -> __value
                __token = 727
                try:
                    __zt_tmp = __attrs_4497132512
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4438540496('path', 'node/show_children', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                econtext['show_children'] = __value
                __backup_children_4497130544 = get('children', __marker)

                # <Value 'node/children' (16:31)> -> __value
                __token = 778
                try:
                    __zt_tmp = __attrs_4497132512
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4438540496('path', 'node/children', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                econtext['children'] = __value
                __backup_item_url_4497132128 = get('item_url', __marker)

                # <Value 'node/getURL' (17:30)> -> __value
                __token = 824
                try:
                    __zt_tmp = __attrs_4497132512
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4438540496('path', 'node/getURL', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                econtext['item_url'] = __value
                __backup_item_remote_url_4497129824 = get('item_remote_url', __marker)

                # <Value 'node/getRemoteUrl' (18:29)> -> __value
                __token = 868
                try:
                    __zt_tmp = __attrs_4497132512
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4438540496('path', 'node/getRemoteUrl', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                econtext['item_remote_url'] = __value
                __backup_use_remote_url_4497129776 = get('use_remote_url', __marker)

                # <Value 'node/useRemoteUrl | nothing' (19:28)> -> __value
                __token = 918
                try:
                    __zt_tmp = __attrs_4497132512
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4438540496('path', 'node/useRemoteUrl | nothing', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                econtext['use_remote_url'] = __value
                __backup_item_type_4497132320 = get('item_type', __marker)

                # <Value 'node/portal_type' (20:27)> -> __value
                __token = 978
                try:
                    __zt_tmp = __attrs_4497132512
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4438540496('path', 'node/portal_type', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                econtext['item_type'] = __value
                __backup_item_4497130064 = get('item', __marker)

                # <Value 'node/item' (21:26)> -> __value
                __token = 1027
                try:
                    __zt_tmp = __attrs_4497132512
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4438540496('path', 'node/item', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                econtext['item'] = __value
                __backup_has_thumb_4497129968 = get('has_thumb', __marker)

                # <Value 'item/getIcon' (22:25)> -> __value
                __token = 1069
                try:
                    __zt_tmp = __attrs_4497132512
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4438540496('path', 'item/getIcon', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                econtext['has_thumb'] = __value
                __backup_is_current_4497133136 = get('is_current', __marker)

                # <Value 'node/currentItem' (23:24)> -> __value
                __token = 1114
                try:
                    __zt_tmp = __attrs_4497132512
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4438540496('path', 'node/currentItem', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                econtext['is_current'] = __value
                __backup_is_in_path_4497133040 = get('is_in_path', __marker)

                # <Value 'node/currentParent' (24:23)> -> __value
                __token = 1163
                try:
                    __zt_tmp = __attrs_4497132512
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4438540496('path', 'node/currentParent', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                econtext['is_in_path'] = __value
                __backup_li_class_4497133088 = get('li_class', __marker)

                # <Value "python:' navTreeCurrentNode' if is_current else ''" (25:22)> -> __value
                __token = 1214
                try:
                    __zt_tmp = __attrs_4497132512
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4438540496('python', "' navTreeCurrentNode' if is_current else ''", econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                econtext['li_class'] = __value
                __backup_li_extr_class_4497133424 = get('li_extr_class', __marker)

                # <Value "python:' navTreeItemInPath' if is_in_path else ''" (26:21)> -> __value
                __token = 1297
                try:
                    __zt_tmp = __attrs_4497132512
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4438540496('python', "' navTreeItemInPath' if is_in_path else ''", econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                econtext['li_extr_class'] = __value
                __backup_li_folder_class_4497133232 = get('li_folder_class', __marker)

                # <Value "python:' navTreeFolderish' if show_children else ''" (27:20)> -> __value
                __token = 1379
                try:
                    __zt_tmp = __attrs_4497132512
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4438540496('python', "' navTreeFolderish' if show_children else ''", econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                econtext['li_folder_class'] = __value

                # <Value 'python:bottomLevel <= 0 or level <= bottomLevel' (28:19)> -> __condition
                __token = 1464
                try:
                    __zt_tmp = __attrs_4497132512
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4438540496('python', 'bottomLevel <= 0 or level <= bottomLevel', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                if __condition:

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li')

                    # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4497131552
                    __default_4497131552 = _DEFAULT_MARKER

                    # <Substitution 'string:navTreeItem visualNoMarker${li_class}${li_extr_class}${li_folder_class} section-${node/normalized_id}' (29:26)> -> __attr_class
                    __token = 1545
                    try:
                        __zt_tmp = __attrs_4497132512
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4438540496('string', 'navTreeItem visualNoMarker${li_class}${li_extr_class}${li_folder_class} section-${node/normalized_id}', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n\n    ')

                    # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4497135008
                    __attrs_4497135008 = _static_4438430896
                    __backup_item_class_4496207312 = get('item_class', __marker)

                    # <Value 'string:state-${node/normalized_review_state}' (31:34)> -> __value
                    __token = 1691
                    try:
                        __zt_tmp = __attrs_4497135008
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4438540496('string', 'state-${node/normalized_review_state}', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                    econtext['item_class'] = __value
                    __backup_item_type_class_4496239024 = get('item_type_class', __marker)

                    # <Value "python:'contenttype-%s' % normalizeString(item_type) if not supress_icon else ''" (32:38)> -> __value
                    __token = 1775
                    try:
                        __zt_tmp = __attrs_4497135008
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4438540496('python', "'contenttype-%s' % normalizeString(item_type) if not supress_icon else ''", econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                    econtext['item_type_class'] = __value
                    __backup_item_class_4496554688 = get('item_class', __marker)

                    # <Value "python:'%s navTreeCurrentItem' % item_class if is_current else item_class" (33:32)> -> __value
                    __token = 1890
                    try:
                        __zt_tmp = __attrs_4497135008
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4438540496('python', "'%s navTreeCurrentItem' % item_class if is_current else item_class", econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                    econtext['item_class'] = __value
                    __append('\n\n        ')

                    # <Static value=<ast.Dict object at 0x10c0cf6a0> name=None at 10c0cf670> -> __attrs_4497142400
                    __attrs_4497142400 = _static_4497143456

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4497143936
                    __default_4497143936 = _DEFAULT_MARKER

                    # <Substitution 'python:item_remote_url if use_remote_url else item_url' (35:33)> -> __attr_href
                    __token = 2002
                    try:
                        __zt_tmp = __attrs_4497142400
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4438540496('python', 'item_remote_url if use_remote_url else item_url', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4497143264
                    __default_4497143264 = _DEFAULT_MARKER

                    # <Substitution 'node/Description' (36:32)> -> __attr_title
                    __token = 2090
                    try:
                        __zt_tmp = __attrs_4497142400
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_4438540496('path', 'node/Description', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4497142928
                    __default_4497142928 = _DEFAULT_MARKER

                    # <Substitution 'string:${item_class}${li_class}${li_extr_class}${li_folder_class} ${item_type_class}' (37:31)> -> __attr_class
                    __token = 2140
                    try:
                        __zt_tmp = __attrs_4497142400
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4438540496('string', '${item_class}${li_class}${li_extr_class}${li_folder_class} ${item_type_class}', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n\n            ')

                    # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4497140960
                    __attrs_4497140960 = _static_4438430896

                    # <Value "python: not supress_icon and item_type != 'File'" (39:37)> -> __condition
                    __token = 2267
                    try:
                        __zt_tmp = __attrs_4497140960
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4438540496('python', " not supress_icon and item_type != 'File'", econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4497141152
                        __default_4497141152 = _DEFAULT_MARKER

                        # <Value "python:icons.tag(f'contenttype/{normalizeString(item_type)}')" (40:45)> -> __cache_4497141632
                        __token = 2362
                        try:
                            __zt_tmp = __attrs_4497140960
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4497141632 = _static_4438540496('python', "icons.tag(f'contenttype/{normalizeString(item_type)}')", econtext=econtext)(_static_4438741184(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:icons.tag(f'contenttype/{normalizeString(item_type)}')" (40:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088d2740> at 10c0ceec0> -> __condition
                        __expression = __cache_4497141632

                        # <Symbol value=<DEFAULT> at 1088d2740> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4497141632
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                    __append('\n\n            ')

                    # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4497139328
                    __attrs_4497139328 = _static_4438430896

                    # <Value "python: not supress_icon and item_type == 'File'" (42:37)> -> __condition
                    __token = 2466
                    try:
                        __zt_tmp = __attrs_4497139328
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4438540496('python', " not supress_icon and item_type == 'File'", econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4497138512
                        __default_4497138512 = _DEFAULT_MARKER

                        # <Value "python:icons.tag(f'mimetype-{item.mime_type}')" (43:45)> -> __cache_4497140384
                        __token = 2561
                        try:
                            __zt_tmp = __attrs_4497139328
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4497140384 = _static_4438540496('python', "icons.tag(f'mimetype-{item.mime_type}')", econtext=econtext)(_static_4438741184(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:icons.tag(f'mimetype-{item.mime_type}')" (43:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088d2740> at 10c0ce9b0> -> __condition
                        __expression = __cache_4497140384

                        # <Symbol value=<DEFAULT> at 1088d2740> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4497140384
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                    __append('\n\n            ')

                    # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4496229280
                    __attrs_4496229280 = _static_4438430896

                    # <Value 'python:has_thumb and thumb_scale' (45:32)> -> __condition
                    __token = 2645
                    try:
                        __zt_tmp = __attrs_4496229280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4438540496('python', 'has_thumb and thumb_scale', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4496244448
                        __default_4496244448 = _DEFAULT_MARKER

                        # <Value "python:image_scale.tag(item, 'image', scale=thumb_scale, css_class='float-end thumb-'+thumb_scale)" (46:40)> -> __cache_4497135824
                        __token = 2719
                        try:
                            __zt_tmp = __attrs_4496229280
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4497135824 = _static_4438540496('python', "image_scale.tag(item, 'image', scale=thumb_scale, css_class='float-end thumb-'+thumb_scale)", econtext=econtext)(_static_4438741184(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:image_scale.tag(item, 'image', scale=thumb_scale, css_class='float-end thumb-'+thumb_scale)" (46:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088d2740> at 10c0cd930> -> __condition
                        __expression = __cache_4497135824

                        # <Symbol value=<DEFAULT> at 1088d2740> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <img ... (0:0)
                            # --------------------------------------------------------
                            __append('<img>')
                        else:
                            __content = __cache_4497135824
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                    __append('\n\n            ')

                    # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4496237920
                    __attrs_4496237920 = _static_4438430896

                    # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4496237872
                    __default_4496237872 = _DEFAULT_MARKER

                    # <Value 'node/Title' (48:31)> -> __cache_4496232400
                    __token = 2852
                    try:
                        __zt_tmp = __attrs_4496237920
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4496232400 = _static_4438540496('path', 'node/Title', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))

                    # <BinOp left=<Value 'node/Title' (48:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088d2740> at 10bff2830> -> __condition
                    __expression = __cache_4496232400

                    # <Symbol value=<DEFAULT> at 1088d2740> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>Selected Item Title</span>')
                    else:
                        __content = __cache_4496232400
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n        </a>\n        ')

                    # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4496237392
                    __attrs_4496237392 = _static_4438430896

                    # <Value 'children' (50:33)> -> __condition
                    __token = 2937
                    try:
                        __zt_tmp = __attrs_4496237392
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4438540496('path', 'children', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                    if __condition:
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x10bff0ca0> name=None at 10bff33a0> -> __attrs_4496235184
                        __attrs_4496235184 = _static_4496231584

                        # <Value 'python: children and show_children and bottomLevel and level < bottomLevel or bottomLevel == 0' (52:31)> -> __condition
                        __token = 3054
                        try:
                            __zt_tmp = __attrs_4496235184
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4438540496('python', ' children and show_children and bottomLevel and level < bottomLevel or bottomLevel == 0', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                        if __condition:

                            # <ul ... (0:0)
                            # --------------------------------------------------------
                            __append('<ul')

                            # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4496231824
                            __default_4496231824 = _DEFAULT_MARKER

                            # <Substitution 'string:navTree navTreeLevel${level}' (51:38)> -> __attr_class
                            __token = 2986
                            try:
                                __zt_tmp = __attrs_4496235184
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_4438540496('string', 'navTree navTreeLevel${level}', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((' class="%s"' % __attr_class))
                            __append('>\n                ')

                            # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4496236528
                            __attrs_4496236528 = _static_4438430896

                            # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4496229472
                            __default_4496229472 = _DEFAULT_MARKER

                            # <Value 'python:view.recurse(children=children, level=level+1, bottomLevel=bottomLevel)' (53:45)> -> __cache_4496230624
                            __token = 3196
                            try:
                                __zt_tmp = __attrs_4496236528
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4496230624 = _static_4438540496('python', 'view.recurse(children=children, level=level+1, bottomLevel=bottomLevel)', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))

                            # <BinOp left=<Value 'python:view.recurse(children=children, level=level+1, bottomLevel=bottomLevel)' (53:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088d2740> at 10bff0d30> -> __condition
                            __expression = __cache_4496230624

                            # <Symbol value=<DEFAULT> at 1088d2740> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span />')
                            else:
                                __content = __cache_4496230624
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append('\n            </ul>')
                        __append('\n        ')
                    __append('\n\n    ')
                    if (__backup_item_class_4496554688 is __marker):
                        del econtext['item_class']
                    else:
                        econtext['item_class'] = __backup_item_class_4496554688
                    if (__backup_item_type_class_4496239024 is __marker):
                        del econtext['item_type_class']
                    else:
                        econtext['item_type_class'] = __backup_item_type_class_4496239024
                    if (__backup_item_class_4496207312 is __marker):
                        del econtext['item_class']
                    else:
                        econtext['item_class'] = __backup_item_class_4496207312
                    __append('\n</li>')
                if (__backup_li_folder_class_4497133232 is __marker):
                    del econtext['li_folder_class']
                else:
                    econtext['li_folder_class'] = __backup_li_folder_class_4497133232
                if (__backup_li_extr_class_4497133424 is __marker):
                    del econtext['li_extr_class']
                else:
                    econtext['li_extr_class'] = __backup_li_extr_class_4497133424
                if (__backup_li_class_4497133088 is __marker):
                    del econtext['li_class']
                else:
                    econtext['li_class'] = __backup_li_class_4497133088
                if (__backup_is_in_path_4497133040 is __marker):
                    del econtext['is_in_path']
                else:
                    econtext['is_in_path'] = __backup_is_in_path_4497133040
                if (__backup_is_current_4497133136 is __marker):
                    del econtext['is_current']
                else:
                    econtext['is_current'] = __backup_is_current_4497133136
                if (__backup_has_thumb_4497129968 is __marker):
                    del econtext['has_thumb']
                else:
                    econtext['has_thumb'] = __backup_has_thumb_4497129968
                if (__backup_item_4497130064 is __marker):
                    del econtext['item']
                else:
                    econtext['item'] = __backup_item_4497130064
                if (__backup_item_type_4497132320 is __marker):
                    del econtext['item_type']
                else:
                    econtext['item_type'] = __backup_item_type_4497132320
                if (__backup_use_remote_url_4497129776 is __marker):
                    del econtext['use_remote_url']
                else:
                    econtext['use_remote_url'] = __backup_use_remote_url_4497129776
                if (__backup_item_remote_url_4497129824 is __marker):
                    del econtext['item_remote_url']
                else:
                    econtext['item_remote_url'] = __backup_item_remote_url_4497129824
                if (__backup_item_url_4497132128 is __marker):
                    del econtext['item_url']
                else:
                    econtext['item_url'] = __backup_item_url_4497132128
                if (__backup_children_4497130544 is __marker):
                    del econtext['children']
                else:
                    econtext['children'] = __backup_children_4497130544
                if (__backup_show_children_4497130256 is __marker):
                    del econtext['show_children']
                else:
                    econtext['show_children'] = __backup_show_children_4497130256
                __append('\n')
                ____index_4497131984 -= 1
                if (____index_4497131984 > 0):
                    __append('')
            if (__backup_node_4497133664 is __marker):
                del econtext['node']
            else:
                econtext['node'] = __backup_node_4497133664
            __append('\n')
            if (__backup_image_scale_4495956560 is __marker):
                del econtext['image_scale']
            else:
                econtext['image_scale'] = __backup_image_scale_4495956560
            if (__backup_portal_4496238064 is __marker):
                del econtext['portal']
            else:
                econtext['portal'] = __backup_portal_4496238064
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

            # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4495565120
            __attrs_4495565120 = _static_4438430896
            __backup_level_4495957520 = get('level', __marker)

            # <Value 'options/level | python:0' (1:26)> -> __value
            __token = 26
            try:
                __zt_tmp = __attrs_4495565120
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('path', 'options/level | python:0', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['level'] = __value
            __backup_children_4495956464 = get('children', __marker)

            # <Value 'options/children | nothing' (2:28)> -> __value
            __token = 80
            try:
                __zt_tmp = __attrs_4495565120
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('path', 'options/children | nothing', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['children'] = __value
            __backup_bottomLevel_4495956368 = get('bottomLevel', __marker)

            # <Value 'options/bottomLevel | nothing' (3:30)> -> __value
            __token = 139
            try:
                __zt_tmp = __attrs_4495565120
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('path', 'options/bottomLevel | nothing', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['bottomLevel'] = __value
            __backup_supress_icon_4495963136 = get('supress_icon', __marker)

            # <Value 'view/data/no_icons' (4:33)> -> __value
            __token = 205
            try:
                __zt_tmp = __attrs_4495565120
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('path', 'view/data/no_icons', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['supress_icon'] = __value
            __backup_supress_thumb_4495955072 = get('supress_thumb', __marker)

            # <Value 'view/data/no_thumbs' (5:32)> -> __value
            __token = 260
            try:
                __zt_tmp = __attrs_4495565120
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('path', 'view/data/no_thumbs', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['supress_thumb'] = __value
            __backup_thumb_scale_4495951376 = get('thumb_scale', __marker)

            # <Value 'view/thumb_scale' (6:27)> -> __value
            __token = 312
            try:
                __zt_tmp = __attrs_4495565120
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('path', 'view/thumb_scale', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['thumb_scale'] = __value
            __backup_icons_4495955216 = get('icons', __marker)

            # <Value 'nocall:context/@@iconresolver' (7:20)> -> __value
            __token = 355
            try:
                __zt_tmp = __attrs_4495565120
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('nocall', 'context/@@iconresolver', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_normalizeString_4496545328 = get('normalizeString', __marker)

            # <Value 'nocall: context/plone_utils/normalizeString' (8:29)> -> __value
            __token = 421
            try:
                __zt_tmp = __attrs_4495565120
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('nocall', ' context/plone_utils/normalizeString', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['normalizeString'] = __value
            __previous_i18n_domain_4497132896 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n\n')
            __token = None
            render_nav_main(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n')
            __i18n_domain = __previous_i18n_domain_4497132896
            if (__backup_normalizeString_4496545328 is __marker):
                del econtext['normalizeString']
            else:
                econtext['normalizeString'] = __backup_normalizeString_4496545328
            if (__backup_icons_4495955216 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_4495955216
            if (__backup_thumb_scale_4495951376 is __marker):
                del econtext['thumb_scale']
            else:
                econtext['thumb_scale'] = __backup_thumb_scale_4495951376
            if (__backup_supress_thumb_4495955072 is __marker):
                del econtext['supress_thumb']
            else:
                econtext['supress_thumb'] = __backup_supress_thumb_4495955072
            if (__backup_supress_icon_4495963136 is __marker):
                del econtext['supress_icon']
            else:
                econtext['supress_icon'] = __backup_supress_icon_4495963136
            if (__backup_bottomLevel_4495956368 is __marker):
                del econtext['bottomLevel']
            else:
                econtext['bottomLevel'] = __backup_bottomLevel_4495956368
            if (__backup_children_4495956464 is __marker):
                del econtext['children']
            else:
                econtext['children'] = __backup_children_4495956464
            if (__backup_level_4495957520 is __marker):
                del econtext['level']
            else:
                econtext['level'] = __backup_level_4495957520
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_nav_main': render_nav_main, 'render': render, }