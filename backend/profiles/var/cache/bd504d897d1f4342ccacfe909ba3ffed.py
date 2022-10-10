# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/dexterity/browser/types_listing_row.pt'

__tokens = {24: ('view/getCombinedWidgets', 1, 24), 74: (' context/@@plone_portal_state/porta', 2, 25), 136: ('t portal/@@plone_layo', 3, 24), 188: ('es view/getNiceTit', 4, 27), 234: ('tups', 5, 23), 266: ('python:tup[0].error', 7, 24), 308: (' repeat/tup/inde', 8, 21), 353: ('e nocall: context/@@plone/normalizeStri', 9, 26), 425: ("python:'field' + (error and ' error' or '') + (tup[0].__name__ == 'view_item_count' and ' count' or '')", 10, 28), 561: ('tup', 11, 30), 609: ('python:view.context.context.link(view.getContent(), widget.field.__name__)', 16, 24), 719: (" python:'contenttype-' + normalize(view.getContent().id", 17, 34), 798: ("python:widget.mode == 'input' or link is None", 18, 21), 873: ('link', 19, 28), 907: (' string:$item_type_clas', 20, 28), 975: ('not:error', 22, 40), 1015: ('error', 23, 28), 1045: ('error/render', 23, 58), 1112: ('widget/render', 24, 50)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4677126848 = {'type': 'text', }
_static_4682789312 = {'class': 'error', }
_static_4682789696 = {'href': '', 'class': 'string:$item_type_class', }
_static_4682781680 = {'class': "python:'field' + (error and ' error' or '') + (tup[0].__name__ == 'view_item_count' and ' count' or '')", }
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
_static_4428767312 = {}

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

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682785568
            __attrs_4682785568 = _static_4428767312
            __backup_tups_4677136352 = get('tups', __marker)

            # <Value 'view/getCombinedWidgets' (1:24)> -> __value
            __token = 24
            try:
                __zt_tmp = __attrs_4682785568
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'view/getCombinedWidgets', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['tups'] = __value
            __backup_portal_4682896176 = get('portal', __marker)

            # <Value 'context/@@plone_portal_state/portal' (2:25)> -> __value
            __token = 74
            try:
                __zt_tmp = __attrs_4682785568
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'context/@@plone_portal_state/portal', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['portal'] = __value
            __backup_layout_4677136064 = get('layout', __marker)

            # <Value 'portal/@@plone_layout' (3:24)> -> __value
            __token = 136
            try:
                __zt_tmp = __attrs_4682785568
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'portal/@@plone_layout', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['layout'] = __value
            __backup_niceTitles_4677132560 = get('niceTitles', __marker)

            # <Value 'view/getNiceTitles' (4:27)> -> __value
            __token = 188
            try:
                __zt_tmp = __attrs_4682785568
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'view/getNiceTitles', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['niceTitles'] = __value
            __backup_tup_4677125504 = get('tup', __marker)

            # <Value 'tups' (5:23)> -> __iterator
            __token = 234
            try:
                __zt_tmp = __attrs_4682785568
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4427992992('path', 'tups', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            (__iterator, ____index_4682784752, ) = getname('repeat')('tup', __iterator)
            econtext['tup'] = None
            for __item in __iterator:
                econtext['tup'] = __item
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x1171d93f0> name=None at 1171d8370> -> __attrs_4682792048
                __attrs_4682792048 = _static_4682781680
                __backup_error_4677127616 = get('error', __marker)

                # <Value 'python:tup[0].error' (7:24)> -> __value
                __token = 266
                try:
                    __zt_tmp = __attrs_4682792048
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'tup[0].error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['error'] = __value
                __backup_idx_4677135776 = get('idx', __marker)

                # <Value 'repeat/tup/index' (8:21)> -> __value
                __token = 308
                try:
                    __zt_tmp = __attrs_4682792048
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'repeat/tup/index', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['idx'] = __value
                __backup_normalize_4677134960 = get('normalize', __marker)

                # <Value 'nocall: context/@@plone/normalizeString' (9:26)> -> __value
                __token = 353
                try:
                    __zt_tmp = __attrs_4682792048
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('nocall', ' context/@@plone/normalizeString', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['normalize'] = __value

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682789024
                __default_4682789024 = _DEFAULT_MARKER

                # <Substitution "python:'field' + (error and ' error' or '') + (tup[0].__name__ == 'view_item_count' and ' count' or '')" (10:28)> -> __attr_class
                __token = 425
                try:
                    __zt_tmp = __attrs_4682792048
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_4427992992('python', "'field' + (error and ' error' or '') + (tup[0].__name__ == 'view_item_count' and ' count' or '')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append('>\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682787248
                __attrs_4682787248 = _static_4428767312
                __backup_widget_4677124688 = get('widget', __marker)

                # <Value 'tup' (11:30)> -> __iterator
                __token = 561
                try:
                    __zt_tmp = __attrs_4682787248
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4427992992('path', 'tup', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                (__iterator, ____index_4682792384, ) = getname('repeat')('widget', __iterator)
                econtext['widget'] = None
                for __item in __iterator:
                    econtext['widget'] = __item
                    __append('\n\n\n\n    ')

                    # <Static value=<ast.Dict object at 0x1171db340> name=None at 1171d8910> -> __attrs_4682781296
                    __attrs_4682781296 = _static_4682789696
                    __backup_link_4677129056 = get('link', __marker)

                    # <Value 'python:view.context.context.link(view.getContent(), widget.field.__name__)' (16:24)> -> __value
                    __token = 609
                    try:
                        __zt_tmp = __attrs_4682781296
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4427992992('python', 'view.context.context.link(view.getContent(), widget.field.__name__)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    econtext['link'] = __value
                    __backup_item_type_class_4677138416 = get('item_type_class', __marker)

                    # <Value "python:'contenttype-' + normalize(view.getContent().id)" (17:34)> -> __value
                    __token = 719
                    try:
                        __zt_tmp = __attrs_4682781296
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4427992992('python', "'contenttype-' + normalize(view.getContent().id)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    econtext['item_type_class'] = __value

                    # <Negate value=<Value "python:widget.mode == 'input' or link is None" (18:21)> at 1171d88e0> -> __cache_4682778848

                    # <Value "python:widget.mode == 'input' or link is None" (18:21)> -> __cache_4682778848
                    __token = 798
                    try:
                        __zt_tmp = __attrs_4682781296
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4682778848 = _static_4427992992('python', "widget.mode == 'input' or link is None", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __cache_4682778848 = not __cache_4682778848
                    __condition = __cache_4682778848
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682784656
                        __default_4682784656 = _DEFAULT_MARKER

                        # <Substitution 'link' (19:28)> -> __attr_href
                        __token = 873
                        try:
                            __zt_tmp = __attrs_4682781296
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4427992992('path', 'link', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682784080
                        __default_4682784080 = _DEFAULT_MARKER

                        # <Substitution 'string:$item_type_class' (20:28)> -> __attr_class
                        __token = 907
                        try:
                            __zt_tmp = __attrs_4682781296
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_4427992992('string', '$item_type_class', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))
                        __append('>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x1171db1c0> name=None at 1171daf20> -> __attrs_4682779904
                    __attrs_4682779904 = _static_4682789312

                    # <Negate value=<Value 'not:error' (22:40)> at 1171d95a0> -> __cache_4682782112

                    # <Value 'not:error' (22:40)> -> __cache_4682782112
                    __token = 975
                    try:
                        __zt_tmp = __attrs_4682779904
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4682782112 = _static_4427992992('not', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __cache_4682782112 = not __cache_4682782112
                    __condition = __cache_4682782112
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="error">')
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4677131696
                    __attrs_4677131696 = _static_4428767312

                    # <Value 'error' (23:28)> -> __condition
                    __token = 1015
                    try:
                        __zt_tmp = __attrs_4677131696
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4677127136
                        __default_4677127136 = _DEFAULT_MARKER

                        # <Value 'error/render' (23:58)> -> __cache_4682785520
                        __token = 1045
                        try:
                            __zt_tmp = __attrs_4677131696
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4682785520 = _static_4427992992('path', 'error/render', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value 'error/render' (23:58)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116c770d0> -> __condition
                        __expression = __cache_4682785520

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div />')
                        else:
                            __content = __cache_4682785520
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x116c74ac0> name=None at 116c74b20> -> __attrs_4677126560
                    __attrs_4677126560 = _static_4677126848

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4677135200
                    __default_4677135200 = _DEFAULT_MARKER

                    # <Value 'widget/render' (24:50)> -> __cache_4677133472
                    __token = 1112
                    try:
                        __zt_tmp = __attrs_4677126560
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4677133472 = _static_4427992992('path', 'widget/render', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'widget/render' (24:50)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116c74310> -> __condition
                    __expression = __cache_4677133472

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="text" />')
                    else:
                        __content = __cache_4677133472
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')
                    __condition = __cache_4682782112
                    if __condition:
                        __append('</span>')
                    __append('\n\n    ')
                    __condition = __cache_4682778848
                    if __condition:
                        __append('</a>')
                    if (__backup_item_type_class_4677138416 is __marker):
                        del econtext['item_type_class']
                    else:
                        econtext['item_type_class'] = __backup_item_type_class_4677138416
                    if (__backup_link_4677129056 is __marker):
                        del econtext['link']
                    else:
                        econtext['link'] = __backup_link_4677129056
                    __append('\n    ')
                    ____index_4682792384 -= 1
                    if (____index_4682792384 > 0):
                        __append('')
                if (__backup_widget_4677124688 is __marker):
                    del econtext['widget']
                else:
                    econtext['widget'] = __backup_widget_4677124688
                __append('\n\n  </td>')
                if (__backup_normalize_4677134960 is __marker):
                    del econtext['normalize']
                else:
                    econtext['normalize'] = __backup_normalize_4677134960
                if (__backup_idx_4677135776 is __marker):
                    del econtext['idx']
                else:
                    econtext['idx'] = __backup_idx_4677135776
                if (__backup_error_4677127616 is __marker):
                    del econtext['error']
                else:
                    econtext['error'] = __backup_error_4677127616
                __append('\n')
                ____index_4682784752 -= 1
                if (____index_4682784752 > 0):
                    __append('')
            if (__backup_tup_4677125504 is __marker):
                del econtext['tup']
            else:
                econtext['tup'] = __backup_tup_4677125504
            if (__backup_niceTitles_4677132560 is __marker):
                del econtext['niceTitles']
            else:
                econtext['niceTitles'] = __backup_niceTitles_4677132560
            if (__backup_layout_4677136064 is __marker):
                del econtext['layout']
            else:
                econtext['layout'] = __backup_layout_4677136064
            if (__backup_portal_4682896176 is __marker):
                del econtext['portal']
            else:
                econtext['portal'] = __backup_portal_4682896176
            if (__backup_tups_4677136352 is __marker):
                del econtext['tups']
            else:
                econtext['tups'] = __backup_tups_4677136352
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }