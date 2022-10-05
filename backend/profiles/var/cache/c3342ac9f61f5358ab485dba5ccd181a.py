# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/viewlets/toolbar.pt'

__tokens = {73: ('view/context_state', 2, 35), 119: (" python:context.restrictedTraverse('@@iconresolver'", 3, 26), 205: ('r python: view.get_personal_bar', 4, 32), 270: ('os view/toolbar_posit', 5, 30), 320: ('context_state/is_toolbar_visible', 6, 24), 635: ("python:icons.tag('arrow-bar-left')", 15, 41), 805: ("python:icons.tag('arrow-bar-right')", 18, 41), 952: ('view/base_render', 23, 33), 993: ('toolbar_main', 24, 23), 1041: ('toolbar_main', 25, 33), 1103: ('personal_bar/user_actions', 29, 24), 1137: ("personaltools-wrapper nav ${python:'dropend' if toolbar_pos == 'side' else ''}", 29, 58), 1165: ("python:'dropend' if toolbar_pos == 'side' else ''", 29, 86), 1424: ('personal_bar/homelink_url', 36, 30), 1493: ("python:icons.tag('toolbar-action/personaltools', tag_class='')", 37, 41), 1609: ('personal_bar/user_name', 38, 49), 1830: ('${personal_bar/user_name}', 45, 38), 1832: ('personal_bar/user_name', 45, 40), 1906: ('personal_bar/user_actions', 47, 31), 1953: ('${action/href}', 48, 19), 1955: ('action/href', 48, 21), 2042: ("python:icons.tag(action.get('icon', 'dot'), tag_class='')", 49, 41), 2145: ('action/title', 50, 41)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4982224496 = {'href': '${action/href}', 'class': 'nav-link dropdown-item', }
_static_4982218880 = {'class': 'dropdown-header', }
_static_4982215376 = {'id': 'collapse-personaltools', 'class': 'dropdown-menu', 'aria-labelledby': 'personaltools-menulink', }
_static_4982217008 = {'class': 'toolbar-label', }
_static_4982403568 = {'id': 'personaltools-menulink', 'class': 'nav-link dropdown-toggle', 'data-bs-toggle': 'dropdown', 'data-bs-offset': '0,0', 'aria-expanded': 'false', 'href': 'personal_bar/homelink_url', }
_static_4982397232 = {'class': "personaltools-wrapper nav ${python:'dropend' if toolbar_pos == 'side' else ''}", }
_static_4982407024 = {'class': 'nav flex-column plone-toolbar-main', }
_static_4982399824 = {'class': 'toolbar-expand', 'aria-label': 'Pin', }
_static_4753720080 = {}
_static_4982404240 = {'class': 'toolbar-collapse', 'aria-label': 'Unpin', }
_static_4982403184 = {'class': 'toolbar-header nav', }
_static_4982519744 = {'id': 'edit-zone', 'role': 'toolbar', 'class': 'pat-toolbar', 'data-bs-scroll': 'true', }
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4982512208 = {'id': 'edit-bar', 'role': 'toolbar', }

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

            # <Static value=<ast.Dict object at 0x128fb1a50> name=None at 128fb2c20> -> __attrs_4982518736
            __attrs_4982518736 = _static_4982512208
            __backup_context_state_4974776560 = get('context_state', __marker)

            # <Value 'view/context_state' (2:35)> -> __value
            __token = 73
            try:
                __zt_tmp = __attrs_4982518736
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/context_state', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['context_state'] = __value
            __backup_icons_4981797072 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (3:26)> -> __value
            __token = 119
            try:
                __zt_tmp = __attrs_4982518736
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_personal_bar_4974780064 = get('personal_bar', __marker)

            # <Value 'python: view.get_personal_bar()' (4:32)> -> __value
            __token = 205
            try:
                __zt_tmp = __attrs_4982518736
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', ' view.get_personal_bar()', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['personal_bar'] = __value
            __backup_toolbar_pos_4771668480 = get('toolbar_pos', __marker)

            # <Value 'view/toolbar_position' (5:30)> -> __value
            __token = 270
            try:
                __zt_tmp = __attrs_4982518736
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/toolbar_position', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['toolbar_pos'] = __value

            # <Value 'context_state/is_toolbar_visible' (6:24)> -> __condition
            __token = 320
            try:
                __zt_tmp = __attrs_4982518736
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('path', 'context_state/is_toolbar_visible', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4982521280 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="edit-bar" role="toolbar">\n\n\n  ')

                # <Static value=<ast.Dict object at 0x128fb37c0> name=None at 128fb1000> -> __attrs_4982513984
                __attrs_4982513984 = _static_4982519744

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="edit-zone" role="toolbar" class="pat-toolbar" data-bs-scroll="true">\n\n    ')

                # <Static value=<ast.Dict object at 0x128f97070> name=None at 128fb2830> -> __attrs_4982401456
                __attrs_4982401456 = _static_4982403184

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="toolbar-header nav">\n      ')

                # <Static value=<ast.Dict object at 0x128f97490> name=None at 128f96ad0> -> __attrs_4982397856
                __attrs_4982397856 = _static_4982404240

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="toolbar-collapse"')

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982390896
                __default_4982390896 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x128f94f40> at 128f94190> -> __attr_aria_label
                __attr_aria_label = 'Unpin'
                __attr_aria_label = translate(__attr_aria_label, default=__attr_aria_label, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_aria_label is not None):
                    __append((' aria-label="%s"' % __attr_aria_label))
                __append('>\n        ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982401360
                __attrs_4982401360 = _static_4753720080

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982394736
                __default_4982394736 = _DEFAULT_MARKER

                # <Value "python:icons.tag('arrow-bar-left')" (15:41)> -> __cache_4982405200
                __token = 635
                try:
                    __zt_tmp = __attrs_4982401360
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4982405200 = _static_4754050160('python', "icons.tag('arrow-bar-left')", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('arrow-bar-left')" (15:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f95e10> -> __condition
                __expression = __cache_4982405200

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4982405200
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      </a>\n      ')

                # <Static value=<ast.Dict object at 0x128f96350> name=None at 128f96da0> -> __attrs_4982395552
                __attrs_4982395552 = _static_4982399824

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="toolbar-expand"')

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982398864
                __default_4982398864 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x128f96bf0> at 128f943d0> -> __attr_aria_label
                __attr_aria_label = 'Pin'
                __attr_aria_label = translate(__attr_aria_label, default=__attr_aria_label, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_aria_label is not None):
                    __append((' aria-label="%s"' % __attr_aria_label))
                __append('>\n        ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982397472
                __attrs_4982397472 = _static_4753720080

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982400832
                __default_4982400832 = _DEFAULT_MARKER

                # <Value "python:icons.tag('arrow-bar-right')" (18:41)> -> __cache_4982395312
                __token = 805
                try:
                    __zt_tmp = __attrs_4982397472
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4982395312 = _static_4754050160('python', "icons.tag('arrow-bar-right')", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('arrow-bar-right')" (18:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f95c30> -> __condition
                __expression = __cache_4982395312

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4982395312
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      </a>\n    </div>\n\n    ')

                # <Static value=<ast.Dict object at 0x128f97f70> name=None at 128f95600> -> __attrs_4982406016
                __attrs_4982406016 = _static_4982407024
                __backup_toolbar_main_4771670976 = get('toolbar_main', __marker)

                # <Value 'view/base_render' (23:33)> -> __value
                __token = 952
                try:
                    __zt_tmp = __attrs_4982406016
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('path', 'view/base_render', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['toolbar_main'] = __value

                # <Value 'toolbar_main' (24:23)> -> __condition
                __token = 993
                try:
                    __zt_tmp = __attrs_4982406016
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4754050160('path', 'toolbar_main', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                if __condition:

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="nav flex-column plone-toolbar-main">\n      ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982395072
                    __attrs_4982395072 = _static_4753720080

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982391856
                    __default_4982391856 = _DEFAULT_MARKER

                    # <Value 'toolbar_main' (25:33)> -> __cache_4982397712
                    __token = 1041
                    try:
                        __zt_tmp = __attrs_4982395072
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4982397712 = _static_4754050160('path', 'toolbar_main', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'toolbar_main' (25:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f94940> -> __condition
                    __expression = __cache_4982397712

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li>\n      </li>')
                    else:
                        __content = __cache_4982397712
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n    </ul>')
                if (__backup_toolbar_main_4771670976 is __marker):
                    del econtext['toolbar_main']
                else:
                    econtext['toolbar_main'] = __backup_toolbar_main_4771670976
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x128f95930> name=None at 128f958d0> -> __attrs_4982404528
                __attrs_4982404528 = _static_4982397232

                # <Value 'personal_bar/user_actions' (29:24)> -> __condition
                __token = 1103
                try:
                    __zt_tmp = __attrs_4982404528
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4754050160('path', 'personal_bar/user_actions', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982401072
                    __default_4982401072 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "personaltools-wrapper nav ${python:'dropend' if toolbar_pos == 'side' else ''}" (29:58)> braces_required=True translation=False default='"?"' default_marker='"?"' at 128f96d70> -> __attr_class
                    __token = 1137
                    __token = 1165
                    try:
                        __zt_tmp = __attrs_4982404528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4754050160('python', "'dropend' if toolbar_pos == 'side' else ''", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s' % ('personaltools-wrapper nav ', (__attr_class if (__attr_class is not None) else ''), ))
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

                    # <Static value=<ast.Dict object at 0x128f971f0> name=None at 128f94730> -> __attrs_4982210960
                    __attrs_4982210960 = _static_4982403568

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a id="personaltools-menulink" class="nav-link dropdown-toggle" data-bs-toggle="dropdown" data-bs-offset="0,0" aria-expanded="false"')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982404384
                    __default_4982404384 = _DEFAULT_MARKER

                    # <Substitution 'personal_bar/homelink_url' (36:30)> -> __attr_href
                    __token = 1424
                    try:
                        __zt_tmp = __attrs_4982210960
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4754050160('path', 'personal_bar/homelink_url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append('>\n        ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982214704
                    __attrs_4982214704 = _static_4753720080

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982217248
                    __default_4982217248 = _DEFAULT_MARKER

                    # <Value "python:icons.tag('toolbar-action/personaltools', tag_class='')" (37:41)> -> __cache_4982211488
                    __token = 1493
                    try:
                        __zt_tmp = __attrs_4982214704
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4982211488 = _static_4754050160('python', "icons.tag('toolbar-action/personaltools', tag_class='')", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag('toolbar-action/personaltools', tag_class='')" (37:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f6aa10> -> __condition
                    __expression = __cache_4982211488

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4982211488
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x128f69930> name=None at 128f69960> -> __attrs_4982225504
                    __attrs_4982225504 = _static_4982217008

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="toolbar-label">')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982225648
                    __default_4982225648 = _DEFAULT_MARKER

                    # <Value 'personal_bar/user_name' (38:49)> -> __cache_4982213120
                    __token = 1609
                    try:
                        __zt_tmp = __attrs_4982225504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4982213120 = _static_4754050160('path', 'personal_bar/user_name', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'personal_bar/user_name' (38:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f6a680> -> __condition
                    __expression = __cache_4982213120

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('User')
                    else:
                        __content = __cache_4982213120
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n      </a>\n\n      ')

                    # <Static value=<ast.Dict object at 0x128f692d0> name=None at 128f68160> -> __attrs_4982223248
                    __attrs_4982223248 = _static_4982215376

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul id="collapse-personaltools" class="dropdown-menu" aria-labelledby="personaltools-menulink">\n        ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982225072
                    __attrs_4982225072 = _static_4753720080

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li>\n          ')

                    # <Static value=<ast.Dict object at 0x128f6a080> name=None at 128f69300> -> __attrs_4982221376
                    __attrs_4982221376 = _static_4982218880

                    # <h6 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h6 class="dropdown-header">')

                    # <Interpolation value=<Substitution '${personal_bar/user_name}' (45:38)> braces_required=True translation=False default='"?"' default_marker='"?"' at 128f68940> -> __content_4355604080
                    __token = 1830
                    __token = 1832
                    try:
                        __zt_tmp = __attrs_4982221376
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_4355604080 = _static_4754050160('path', 'personal_bar/user_name', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
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

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982216576
                    __attrs_4982216576 = _static_4753720080
                    __backup_action_4771662528 = get('action', __marker)

                    # <Value 'personal_bar/user_actions' (47:31)> -> __iterator
                    __token = 1906
                    try:
                        __zt_tmp = __attrs_4982216576
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_4754050160('path', 'personal_bar/user_actions', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    (__iterator, ____index_4982213984, ) = getname('repeat')('action', __iterator)
                    econtext['action'] = None
                    for __item in __iterator:
                        econtext['action'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li>\n          ')

                        # <Static value=<ast.Dict object at 0x128f6b670> name=None at 128f69660> -> __attrs_4982222576
                        __attrs_4982222576 = _static_4982224496

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982222624
                        __default_4982222624 = _DEFAULT_MARKER

                        # <Interpolation value=<Substitution '${action/href}' (48:19)> braces_required=True translation=False default='"?"' default_marker='"?"' at 128f69fc0> -> __attr_href
                        __token = 1953
                        __token = 1955
                        try:
                            __zt_tmp = __attrs_4982222576
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4754050160('path', 'action/href', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
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
                        __append(' class="nav-link dropdown-item">\n            ')

                        # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982224832
                        __attrs_4982224832 = _static_4753720080

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982219312
                        __default_4982219312 = _DEFAULT_MARKER

                        # <Value "python:icons.tag(action.get('icon', 'dot'), tag_class='')" (49:41)> -> __cache_4982225936
                        __token = 2042
                        try:
                            __zt_tmp = __attrs_4982224832
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4982225936 = _static_4754050160('python', "icons.tag(action.get('icon', 'dot'), tag_class='')", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:icons.tag(action.get('icon', 'dot'), tag_class='')" (49:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f6b460> -> __condition
                        __expression = __cache_4982225936

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4982225936
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982226320
                        __attrs_4982226320 = _static_4753720080

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982215616
                        __default_4982215616 = _DEFAULT_MARKER

                        # <Value 'action/title' (50:41)> -> __cache_4982216000
                        __token = 2145
                        try:
                            __zt_tmp = __attrs_4982226320
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4982216000 = _static_4754050160('path', 'action/title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                        # <BinOp left=<Value 'action/title' (50:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f68d90> -> __condition
                        __expression = __cache_4982216000

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n              action title\n            ')
                        else:
                            __content = __cache_4982216000
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n          </a>\n        </li>')
                        ____index_4982213984 -= 1
                        if (____index_4982213984 > 0):
                            __append('\n        ')
                    if (__backup_action_4771662528 is __marker):
                        del econtext['action']
                    else:
                        econtext['action'] = __backup_action_4771662528
                    __append('\n      </ul>\n\n    </div>')
                __append('\n  </div>\n</section>')
                __i18n_domain = __previous_i18n_domain_4982521280
            if (__backup_toolbar_pos_4771668480 is __marker):
                del econtext['toolbar_pos']
            else:
                econtext['toolbar_pos'] = __backup_toolbar_pos_4771668480
            if (__backup_personal_bar_4974780064 is __marker):
                del econtext['personal_bar']
            else:
                econtext['personal_bar'] = __backup_personal_bar_4974780064
            if (__backup_icons_4981797072 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_4981797072
            if (__backup_context_state_4974776560 is __marker):
                del econtext['context_state']
            else:
                econtext['context_state'] = __backup_context_state_4974776560
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }