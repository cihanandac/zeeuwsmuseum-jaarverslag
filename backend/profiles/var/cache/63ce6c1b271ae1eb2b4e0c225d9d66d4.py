# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/contentmenu/contentmenu.pt'

__tokens = {72: ('view/menu', 3, 17), 100: (" python:context.restrictedTraverse('@@iconresolver'", 4, 17), 176: ('s view/toolbar_positi', 5, 22), 39: ('view/available', 2, 15), 256: ('menu', 7, 30), 292: ('menuItem/submenu', 8, 29), 341: (' menuItem/extra/i', 9, 31), 374: ('${menuItem/extra/id}', 10, 12), 376: ('menuItem/extra/id', 10, 14), 403: ("${menuItem/extra/li_class|nothing} ${python:'dropend' if (submenu and toolbar_pos == 'side') else ''}", 10, 41), 405: ('menuItem/extra/li_class|nothing', 10, 43), 440: ("python:'dropend' if (submenu and toolbar_pos == 'side') else ''", 10, 78), 849: ('menuItem/extra/class | nothing', 17, 34), 914: (" python:'label-%s' % state_class if state_class else '", 18, 33), 592: ("python:menuItem['action'] or 'javascript:void(0)'", 14, 31), 988: ("${python:'nav-link dropdown-toggle' if submenu else 'nav-link'}", 19, 17), 990: ("python:'nav-link dropdown-toggle' if submenu else 'nav-link'", 19, 19), 1145: ("${python:'false' if submenu else ''}", 22, 25), 1147: ("python:'false' if submenu else ''", 22, 27), 674: (" python:'cursor: default;; pointer-events: none' if not menuItem['action'] else No", 15, 31), 789: ('le menuItem/descript', 16, 29), 1226: ("python:icons.tag(menuItem.get('icon','') and menuItem['icon'] or 'toolbar-action', tag_class='')", 24, 41), 1440: ('menuItem/title', 29, 27), 1569: ('${state_class}', 34, 21), 1571: ('state_class', 34, 23), 1612: ('menuItem/extra/stateTitle | nothing', 35, 27), 1772: ('submenu | nothing', 42, 47), 1843: ('${menuItem/title}', 44, 38), 1845: ('menuItem/title', 44, 40), 1916: ('submenu', 46, 36), 1967: ('subMenuItem/extra/class | string:', 47, 41), 2420: ('subMenuItem/action', 55, 29), 2023: ('nav-link dropdown-item ${extra_class}', 48, 20), 2048: ('extra_class', 48, 45), 2158: ('subMenuItem/action', 51, 35), 2213: (' subMenuItem/descriptio', 52, 35), 2270: ('d subMenuItem/extra/id | nothi', 53, 31), 2352: ('al subMenuItem/extra/modal | noth', 54, 48), 2489: ("python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))", 57, 47), 2645: ('subMenuItem/title', 60, 35), 2887: ('not:subMenuItem/action', 66, 31), 2773: ('${extra_class}', 64, 25), 2775: ('extra_class', 64, 27), 2824: ('subMenuItem/extra/id | nothing', 65, 35), 2953: ("python:'active' in extra_class", 67, 41), 3034: ("python:icons.tag('check')", 68, 49), 3163: ('subMenuItem/title', 71, 41)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4982400832 = {'class': '${extra_class}', 'id': 'subMenuItem/extra/id | nothing', }
_static_4803157424 = {'class': 'nav-link dropdown-item ${extra_class}', 'href': '#', 'title': 'subMenuItem/description', 'id': 'subMenuItem/extra/id | nothing', 'data-pat-plone-modal': 'subMenuItem/extra/modal | nothing', }
_static_4803164384 = {'class': 'dropdown-header', }
_static_4975126384 = {'class': 'dropdown-menu', }
_static_4975129888 = {'class': '${state_class}', }
_static_4975126816 = {'class': 'toolbar-label', }
_static_4975127056 = {'href': '#', 'class': "${python:'nav-link dropdown-toggle' if submenu else 'nav-link'}", 'data-bs-toggle': 'dropdown', 'data-bs-offset': '0,0', 'aria-expanded': "${python:'false' if submenu else ''}", 'style': "python:'cursor: default; pointer-events: none' if not menuItem['action'] else None", 'title': 'menuItem/description', }
_static_4975121008 = {'id': '${menuItem/extra/id}', 'class': "${menuItem/extra/li_class|nothing} ${python:'dropend' if (submenu and toolbar_pos == 'side') else ''}", }
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4753720080 = {}

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

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982515280
            __attrs_4982515280 = _static_4753720080
            __backup_menu_4974773728 = get('menu', __marker)

            # <Value 'view/menu' (3:17)> -> __value
            __token = 72
            try:
                __zt_tmp = __attrs_4982515280
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/menu', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['menu'] = __value
            __backup_icons_4975061952 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (4:17)> -> __value
            __token = 100
            try:
                __zt_tmp = __attrs_4982515280
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_toolbar_pos_4771661184 = get('toolbar_pos', __marker)

            # <Value 'view/toolbar_position' (5:22)> -> __value
            __token = 176
            try:
                __zt_tmp = __attrs_4982515280
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/toolbar_position', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['toolbar_pos'] = __value

            # <Value 'view/available' (2:15)> -> __condition
            __token = 39
            try:
                __zt_tmp = __attrs_4982515280
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('path', 'view/available', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4982519744 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982511632
                __attrs_4982511632 = _static_4753720080
                __backup_menuItem_4975064592 = get('menuItem', __marker)

                # <Value 'menu' (7:30)> -> __iterator
                __token = 256
                try:
                    __zt_tmp = __attrs_4982511632
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4754050160('path', 'menu', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                (__iterator, ____index_4982516816, ) = getname('repeat')('menuItem', __iterator)
                econtext['menuItem'] = None
                for __item in __iterator:
                    econtext['menuItem'] = __item
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4981937568
                    __attrs_4981937568 = _static_4753720080
                    __backup_submenu_4771661568 = get('submenu', __marker)

                    # <Value 'menuItem/submenu' (8:29)> -> __value
                    __token = 292
                    try:
                        __zt_tmp = __attrs_4981937568
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('path', 'menuItem/submenu', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['submenu'] = __value
                    __backup_identifier_4975064976 = get('identifier', __marker)

                    # <Value 'menuItem/extra/id' (9:31)> -> __value
                    __token = 341
                    try:
                        __zt_tmp = __attrs_4981937568
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('path', 'menuItem/extra/id', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['identifier'] = __value
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x1288a5270> name=None at 1288a5060> -> __attrs_4975130416
                    __attrs_4975130416 = _static_4975121008

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975117552
                    __default_4975117552 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution '${menuItem/extra/id}' (10:12)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1288a4730> -> __attr_id
                    __token = 374
                    __token = 376
                    try:
                        __zt_tmp = __attrs_4975130416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_4754050160('path', 'menuItem/extra/id', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_id = __attr_id
                    if (__attr_id is None):
                        pass
                    else:
                        if (__attr_id is _DEFAULT_MARKER):
                            __attr_id = None
                        else:
                            __tt = type(__attr_id)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_id = str(__attr_id)
                            else:
                                if (__tt is bytes):
                                    __attr_id = decode(__attr_id)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_id = __attr_id.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_id)
                                            __attr_id = (str(__attr_id) if (__attr_id is __converted) else __converted)
                                        else:
                                            __attr_id = __attr_id()
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975120912
                    __default_4975120912 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "${menuItem/extra/li_class|nothing} ${python:'dropend' if (submenu and toolbar_pos == 'side') else ''}" (10:41)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1288a7be0> -> __attr_class
                    __token = 403
                    __token = 405
                    try:
                        __zt_tmp = __attrs_4975130416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4754050160('path', 'menuItem/extra/li_class|nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __token = 440
                    try:
                        __zt_tmp = __attrs_4975130416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class_438 = _static_4754050160('python', "'dropend' if (submenu and toolbar_pos == 'side') else ''", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_class_438 = __quote(__attr_class_438, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s%s' % ((__attr_class if (__attr_class is not None) else ''), ' ', (__attr_class_438 if (__attr_class_438 is not None) else ''), ))
                    if (__attr_class is None):
                        pass
                    else:
                        if (__attr_class is _DEFAULT_MARKER):
                            __attr_class = None
                        else:
                            __tt = type(__attr_class)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_class = str(__attr_class)
                            else:
                                if (__tt is bytes):
                                    __attr_class = decode(__attr_class)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_class = __attr_class.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_class)
                                            __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                        else:
                                            __attr_class = __attr_class()
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n\n      ')

                    # <Static value=<ast.Dict object at 0x1288a6a10> name=None at 1288a7fd0> -> __attrs_4975121728
                    __attrs_4975121728 = _static_4975127056
                    __backup_state_class_4771668864 = get('state_class', __marker)

                    # <Value 'menuItem/extra/class | nothing' (17:34)> -> __value
                    __token = 849
                    try:
                        __zt_tmp = __attrs_4975121728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('path', 'menuItem/extra/class | nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['state_class'] = __value
                    __backup_state_class_4975057488 = get('state_class', __marker)

                    # <Value "python:'label-%s' % state_class if state_class else ''" (18:33)> -> __value
                    __token = 914
                    try:
                        __zt_tmp = __attrs_4975121728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('python', "'label-%s' % state_class if state_class else ''", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['state_class'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975120096
                    __default_4975120096 = _DEFAULT_MARKER

                    # <Substitution "python:menuItem['action'] or 'javascript:void(0)'" (14:31)> -> __attr_href
                    __token = 592
                    try:
                        __zt_tmp = __attrs_4975121728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4754050160('python', "menuItem['action'] or 'javascript:void(0)'", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975127104
                    __default_4975127104 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "${python:'nav-link dropdown-toggle' if submenu else 'nav-link'}" (19:17)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1288a6110> -> __attr_class
                    __token = 988
                    __token = 990
                    try:
                        __zt_tmp = __attrs_4975121728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4754050160('python', "'nav-link dropdown-toggle' if submenu else 'nav-link'", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = __attr_class
                    if (__attr_class is None):
                        pass
                    else:
                        if (__attr_class is _DEFAULT_MARKER):
                            __attr_class = None
                        else:
                            __tt = type(__attr_class)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_class = str(__attr_class)
                            else:
                                if (__tt is bytes):
                                    __attr_class = decode(__attr_class)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_class = __attr_class.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_class)
                                            __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                        else:
                                            __attr_class = __attr_class()
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append(' data-bs-toggle="dropdown" data-bs-offset="0,0"')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975125280
                    __default_4975125280 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "${python:'false' if submenu else ''}" (22:25)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1288a5930> -> __attr_aria_expanded
                    __token = 1145
                    __token = 1147
                    try:
                        __zt_tmp = __attrs_4975121728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_aria_expanded = _static_4754050160('python', "'false' if submenu else ''", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_aria_expanded = __quote(__attr_aria_expanded, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_aria_expanded = __attr_aria_expanded
                    if (__attr_aria_expanded is None):
                        pass
                    else:
                        if (__attr_aria_expanded is _DEFAULT_MARKER):
                            __attr_aria_expanded = None
                        else:
                            __tt = type(__attr_aria_expanded)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_aria_expanded = str(__attr_aria_expanded)
                            else:
                                if (__tt is bytes):
                                    __attr_aria_expanded = decode(__attr_aria_expanded)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_aria_expanded = __attr_aria_expanded.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_aria_expanded)
                                            __attr_aria_expanded = (str(__attr_aria_expanded) if (__attr_aria_expanded is __converted) else __converted)
                                        else:
                                            __attr_aria_expanded = __attr_aria_expanded()
                    if (__attr_aria_expanded is not None):
                        __append((' aria-expanded="%s"' % __attr_aria_expanded))

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975118992
                    __default_4975118992 = _DEFAULT_MARKER

                    # <Substitution "python:'cursor: default; pointer-events: none' if not menuItem['action'] else None" (15:31)> -> __attr_style
                    __token = 674
                    try:
                        __zt_tmp = __attrs_4975121728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_style = _static_4754050160('python', "'cursor: default; pointer-events: none' if not menuItem['action'] else None", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_style is not None):
                        __append((' style="%s"' % __attr_style))

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975130080
                    __default_4975130080 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<Substitution 'menuItem/description' (16:29)> at 1288a4340> -> __attr_title

                    # <Substitution 'menuItem/description' (16:29)> -> __attr_title
                    __token = 789
                    try:
                        __zt_tmp = __attrs_4975121728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_4754050160('path', 'menuItem/description', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append('>\n\n        ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975131856
                    __attrs_4975131856 = _static_4753720080

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975131040
                    __default_4975131040 = _DEFAULT_MARKER

                    # <Value "python:icons.tag(menuItem.get('icon','') and menuItem['icon'] or 'toolbar-action', tag_class='')" (24:41)> -> __cache_4975131232
                    __token = 1226
                    try:
                        __zt_tmp = __attrs_4975131856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4975131232 = _static_4754050160('python', "icons.tag(menuItem.get('icon','') and menuItem['icon'] or 'toolbar-action', tag_class='')", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag(menuItem.get('icon','') and menuItem['icon'] or 'toolbar-action', tag_class='')" (24:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 1288a5f60> -> __condition
                    __expression = __cache_4975131232

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4975131232
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n\n        ')

                    # <Static value=<ast.Dict object at 0x1288a6920> name=None at 1288a6c20> -> __attrs_4975130704
                    __attrs_4975130704 = _static_4975126816

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="toolbar-label">\n          ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975131280
                    __attrs_4975131280 = _static_4753720080

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975131664
                    __default_4975131664 = _DEFAULT_MARKER

                    # <Value 'menuItem/title' (29:27)> -> __cache_4975123600
                    __token = 1440
                    try:
                        __zt_tmp = __attrs_4975131280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4975123600 = _static_4754050160('path', 'menuItem/title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'menuItem/title' (29:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 1288a6f50> -> __condition
                    __expression = __cache_4975123600

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>\n              Menu Title\n          </span>')
                    else:
                        __content = __cache_4975123600
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x1288a7520> name=None at 1288a7ca0> -> __attrs_4975120432
                    __attrs_4975120432 = _static_4975129888

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975116880
                    __default_4975116880 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution '${state_class}' (34:21)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1288a6230> -> __attr_class
                    __token = 1569
                    __token = 1571
                    try:
                        __zt_tmp = __attrs_4975120432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4754050160('path', 'state_class', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = __attr_class
                    if (__attr_class is None):
                        pass
                    else:
                        if (__attr_class is _DEFAULT_MARKER):
                            __attr_class = None
                        else:
                            __tt = type(__attr_class)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_class = str(__attr_class)
                            else:
                                if (__tt is bytes):
                                    __attr_class = decode(__attr_class)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_class = __attr_class.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_class)
                                            __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                        else:
                                            __attr_class = __attr_class()
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975128112
                    __default_4975128112 = _DEFAULT_MARKER

                    # <Value 'menuItem/extra/stateTitle | nothing' (35:27)> -> __cache_4975128160
                    __token = 1612
                    try:
                        __zt_tmp = __attrs_4975120432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4975128160 = _static_4754050160('path', 'menuItem/extra/stateTitle | nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'menuItem/extra/stateTitle | nothing' (35:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 1288a6dd0> -> __condition
                    __expression = __cache_4975128160

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                State title\n          ')
                    else:
                        __content = __cache_4975128160
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n        </span>\n\n      </a>')
                    if (__backup_state_class_4975057488 is __marker):
                        del econtext['state_class']
                    else:
                        econtext['state_class'] = __backup_state_class_4975057488
                    if (__backup_state_class_4771668864 is __marker):
                        del econtext['state_class']
                    else:
                        econtext['state_class'] = __backup_state_class_4771668864
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x1288a6770> name=None at 1288a6ad0> -> __attrs_4975122928
                    __attrs_4975122928 = _static_4975126384

                    # <Value 'submenu | nothing' (42:47)> -> __condition
                    __token = 1772
                    try:
                        __zt_tmp = __attrs_4975122928
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4754050160('path', 'submenu | nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    if __condition:

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append('<ul class="dropdown-menu">\n        ')

                        # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4803163520
                        __attrs_4803163520 = _static_4753720080

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li>\n          ')

                        # <Static value=<ast.Dict object at 0x11e4a78e0> name=None at 11e4a73d0> -> __attrs_4803150272
                        __attrs_4803150272 = _static_4803164384

                        # <h6 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h6 class="dropdown-header">')

                        # <Interpolation value=<Substitution '${menuItem/title}' (44:38)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11e4a4850> -> __content_4355604080
                        __token = 1843
                        __token = 1845
                        try:
                            __zt_tmp = __attrs_4803150272
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_4355604080 = _static_4754050160('path', 'menuItem/title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
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
                        __append('</h6>\n        </li>\n        ')

                        # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4803162560
                        __attrs_4803162560 = _static_4753720080
                        __backup_subMenuItem_4975066800 = get('subMenuItem', __marker)

                        # <Value 'submenu' (46:36)> -> __iterator
                        __token = 1916
                        try:
                            __zt_tmp = __attrs_4803162560
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_4754050160('path', 'submenu', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                        (__iterator, ____index_4803157328, ) = getname('repeat')('subMenuItem', __iterator)
                        econtext['subMenuItem'] = None
                        for __item in __iterator:
                            econtext['subMenuItem'] = __item

                            # <li ... (0:0)
                            # --------------------------------------------------------
                            __append('<li>\n          ')

                            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4803152624
                            __attrs_4803152624 = _static_4753720080
                            __backup_extra_class_4771661328 = get('extra_class', __marker)

                            # <Value 'subMenuItem/extra/class | string:' (47:41)> -> __value
                            __token = 1967
                            try:
                                __zt_tmp = __attrs_4803152624
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4754050160('path', 'subMenuItem/extra/class | string:', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                            econtext['extra_class'] = __value
                            __append('\n          ')

                            # <Static value=<ast.Dict object at 0x11e4a5db0> name=None at 11e4a5e70> -> __attrs_4803161552
                            __attrs_4803161552 = _static_4803157424

                            # <Value 'subMenuItem/action' (55:29)> -> __condition
                            __token = 2420
                            try:
                                __zt_tmp = __attrs_4803161552
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4754050160('path', 'subMenuItem/action', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                            if __condition:

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append('<a')

                                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4803159968
                                __default_4803159968 = _DEFAULT_MARKER

                                # <Interpolation value=<Substitution 'nav-link dropdown-item ${extra_class}' (48:20)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11e4a4730> -> __attr_class
                                __token = 2023
                                __token = 2048
                                try:
                                    __zt_tmp = __attrs_4803161552
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_class = _static_4754050160('path', 'extra_class', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                __attr_class = ('%s%s' % ('nav-link dropdown-item ', (__attr_class if (__attr_class is not None) else ''), ))
                                if (__attr_class is None):
                                    pass
                                else:
                                    if (__attr_class is _DEFAULT_MARKER):
                                        __attr_class = None
                                    else:
                                        __tt = type(__attr_class)
                                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                                            __attr_class = str(__attr_class)
                                        else:
                                            if (__tt is bytes):
                                                __attr_class = decode(__attr_class)
                                            else:
                                                if (__tt is not str):
                                                    try:
                                                        __attr_class = __attr_class.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__attr_class)
                                                        __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                                    else:
                                                        __attr_class = __attr_class()
                                if (__attr_class is not None):
                                    __append((' class="%s"' % __attr_class))

                                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4803157472
                                __default_4803157472 = _DEFAULT_MARKER

                                # <Substitution 'subMenuItem/action' (51:35)> -> __attr_href
                                __token = 2158
                                try:
                                    __zt_tmp = __attrs_4803161552
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_4754050160('path', 'subMenuItem/action', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                                if (__attr_href is not None):
                                    __append((' href="%s"' % __attr_href))

                                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4803165488
                                __default_4803165488 = _DEFAULT_MARKER

                                # <Translate msgid=None node=<Substitution 'subMenuItem/description' (52:35)> at 11e4a7070> -> __attr_title

                                # <Substitution 'subMenuItem/description' (52:35)> -> __attr_title
                                __token = 2213
                                try:
                                    __zt_tmp = __attrs_4803161552
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_title = _static_4754050160('path', 'subMenuItem/description', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                                __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                                __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                if (__attr_title is not None):
                                    __append((' title="%s"' % __attr_title))

                                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4803150944
                                __default_4803150944 = _DEFAULT_MARKER

                                # <Substitution 'subMenuItem/extra/id | nothing' (53:31)> -> __attr_id
                                __token = 2270
                                try:
                                    __zt_tmp = __attrs_4803161552
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_id = _static_4754050160('path', 'subMenuItem/extra/id | nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_id is not None):
                                    __append((' id="%s"' % __attr_id))

                                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4803151472
                                __default_4803151472 = _DEFAULT_MARKER

                                # <Substitution 'subMenuItem/extra/modal | nothing' (54:48)> -> __attr_data_pat_plone_modal
                                __token = 2352
                                try:
                                    __zt_tmp = __attrs_4803161552
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_data_pat_plone_modal = _static_4754050160('path', 'subMenuItem/extra/modal | nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                                __attr_data_pat_plone_modal = __quote(__attr_data_pat_plone_modal, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_data_pat_plone_modal is not None):
                                    __append((' data-pat-plone-modal="%s"' % __attr_data_pat_plone_modal))
                                __append('>\n\n              ')

                                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982401888
                                __attrs_4982401888 = _static_4753720080

                                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982403376
                                __default_4982403376 = _DEFAULT_MARKER

                                # <Value "python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))" (57:47)> -> __cache_4982393728
                                __token = 2489
                                try:
                                    __zt_tmp = __attrs_4982401888
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_4982393728 = _static_4754050160('python', "icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                                # <BinOp left=<Value "python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))" (57:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f977c0> -> __condition
                                __expression = __cache_4982393728

                                # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_4982393728
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append('\n\n            ')

                                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982394064
                                __attrs_4982394064 = _static_4753720080

                                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982400688
                                __default_4982400688 = _DEFAULT_MARKER

                                # <Value 'subMenuItem/title' (60:35)> -> __cache_4982398336
                                __token = 2645
                                try:
                                    __zt_tmp = __attrs_4982394064
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_4982398336 = _static_4754050160('path', 'subMenuItem/title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                                # <BinOp left=<Value 'subMenuItem/title' (60:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f96800> -> __condition
                                __expression = __cache_4982398336

                                # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append('\n                  Title\n            ')
                                else:
                                    __content = __cache_4982398336
                                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append('\n            ')

                                # <Static value=<ast.Dict object at 0x128f96740> name=None at 128f95cf0> -> __attrs_4982393344
                                __attrs_4982393344 = _static_4982400832

                                # <Value 'not:subMenuItem/action' (66:31)> -> __condition
                                __token = 2887
                                try:
                                    __zt_tmp = __attrs_4982393344
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_4754050160('not', 'subMenuItem/action', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                                if __condition:

                                    # <span ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<span')

                                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982395408
                                    __default_4982395408 = _DEFAULT_MARKER

                                    # <Interpolation value=<Substitution '${extra_class}' (64:25)> braces_required=True translation=False default='"?"' default_marker='"?"' at 128f97d90> -> __attr_class
                                    __token = 2773
                                    __token = 2775
                                    try:
                                        __zt_tmp = __attrs_4982393344
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_class = _static_4754050160('path', 'extra_class', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                    __attr_class = __attr_class
                                    if (__attr_class is None):
                                        pass
                                    else:
                                        if (__attr_class is _DEFAULT_MARKER):
                                            __attr_class = None
                                        else:
                                            __tt = type(__attr_class)
                                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                                __attr_class = str(__attr_class)
                                            else:
                                                if (__tt is bytes):
                                                    __attr_class = decode(__attr_class)
                                                else:
                                                    if (__tt is not str):
                                                        try:
                                                            __attr_class = __attr_class.__html__
                                                        except get('AttributeError', AttributeError):
                                                            __converted = convert(__attr_class)
                                                            __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                                        else:
                                                            __attr_class = __attr_class()
                                    if (__attr_class is not None):
                                        __append((' class="%s"' % __attr_class))

                                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982394352
                                    __default_4982394352 = _DEFAULT_MARKER

                                    # <Substitution 'subMenuItem/extra/id | nothing' (65:35)> -> __attr_id
                                    __token = 2824
                                    try:
                                        __zt_tmp = __attrs_4982393344
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_4754050160('path', 'subMenuItem/extra/id | nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((' id="%s"' % __attr_id))
                                    __append('>\n                ')

                                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982402800
                                    __attrs_4982402800 = _static_4753720080

                                    # <Value "python:'active' in extra_class" (67:41)> -> __condition
                                    __token = 2953
                                    try:
                                        __zt_tmp = __attrs_4982402800
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __condition = _static_4754050160('python', "'active' in extra_class", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                                    if __condition:

                                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982395024
                                        __default_4982395024 = _DEFAULT_MARKER

                                        # <Value "python:icons.tag('check')" (68:49)> -> __cache_4982395888
                                        __token = 3034
                                        try:
                                            __zt_tmp = __attrs_4982402800
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __cache_4982395888 = _static_4754050160('python', "icons.tag('check')", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                                        # <BinOp left=<Value "python:icons.tag('check')" (68:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f96170> -> __condition
                                        __expression = __cache_4982395888

                                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                                        __value = _DEFAULT_MARKER
                                        __condition = (__expression is __value)
                                        if __condition:
                                            pass
                                        else:
                                            __content = __cache_4982395888
                                            __content = __convert(__content)
                                            if (__content is not None):
                                                __append(__content)
                                    __append('\n                ')

                                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982394928
                                    __attrs_4982394928 = _static_4753720080

                                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982395984
                                    __default_4982395984 = _DEFAULT_MARKER

                                    # <Value 'subMenuItem/title' (71:41)> -> __cache_4982402608
                                    __token = 3163
                                    try:
                                        __zt_tmp = __attrs_4982394928
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_4982402608 = _static_4754050160('path', 'subMenuItem/title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                                    # <BinOp left=<Value 'subMenuItem/title' (71:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f97160> -> __condition
                                    __expression = __cache_4982402608

                                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:

                                        # <span ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<span>\n                    Title\n                </span>')
                                    else:
                                        __content = __cache_4982402608
                                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                        __content = __convert(__content)
                                        if (__content is not None):
                                            __append(__content)
                                    __append('\n            </span>')
                                __append('\n          </a>')
                            __append('\n          ')
                            if (__backup_extra_class_4771661328 is __marker):
                                del econtext['extra_class']
                            else:
                                econtext['extra_class'] = __backup_extra_class_4771661328
                            __append('\n        </li>')
                            ____index_4803157328 -= 1
                            if (____index_4803157328 > 0):
                                __append('\n        ')
                        if (__backup_subMenuItem_4975066800 is __marker):
                            del econtext['subMenuItem']
                        else:
                            econtext['subMenuItem'] = __backup_subMenuItem_4975066800
                        __append('\n      </ul>')
                    __append('\n\n    </li>\n    ')
                    if (__backup_identifier_4975064976 is __marker):
                        del econtext['identifier']
                    else:
                        econtext['identifier'] = __backup_identifier_4975064976
                    if (__backup_submenu_4771661568 is __marker):
                        del econtext['submenu']
                    else:
                        econtext['submenu'] = __backup_submenu_4771661568
                    __append('\n  ')
                    ____index_4982516816 -= 1
                    if (____index_4982516816 > 0):
                        __append('')
                if (__backup_menuItem_4975064592 is __marker):
                    del econtext['menuItem']
                else:
                    econtext['menuItem'] = __backup_menuItem_4975064592
                __append('\n')
                __i18n_domain = __previous_i18n_domain_4982519744
            if (__backup_toolbar_pos_4771661184 is __marker):
                del econtext['toolbar_pos']
            else:
                econtext['toolbar_pos'] = __backup_toolbar_pos_4771661184
            if (__backup_icons_4975061952 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_4975061952
            if (__backup_menu_4974773728 is __marker):
                del econtext['menu']
            else:
                econtext['menu'] = __backup_menu_4974773728
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }