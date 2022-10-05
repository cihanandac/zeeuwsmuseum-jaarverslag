# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/viewlets/menu.pt'

__tokens = {40: ('context/@@plone', 1, 40), 93: (' view/locked_ico', 2, 36), 146: ("s python:context.restrictedTraverse('@@iconresolver", 3, 34), 235: ('ploneview/showToolbar', 4, 33), 331: ('options/actions', 6, 34), 433: ('action/id', 8, 29), 472: (' action/selected | python:Fals', 9, 28), 361: ('contentview-${action/id}', 7, 12), 375: ('action/id', 7, 26), 709: ('action/url', 12, 32), 534: ("nav-link ${python:'locked' if locked and actionid == 'history' else ''} ${action/cssClass | nothing} ${python:'active' if selected else None}", 11, 27), 545: ("python:'locked' if locked and actionid == 'history' else ''", 11, 38), 608: ('action/cssClass | nothing', 11, 101), 637: ("python:'active' if selected else None", 11, 130), 754: (' action/link_target|nothin', 13, 33), 815: ("python:actionid != 'history'", 15, 29), 883: ("python:action['icon']", 16, 37), 951: ("python:icons.tag(action['icon'] or 'toolbar-action', tag_class='me-1')", 17, 45), 1079: ('action/title', 18, 53), 1182: ("python:actionid == 'history'", 21, 33), 1258: ("python:icons.tag('lock' if locked else action['icon'], tag_class='me-1')", 22, 45), 1524: ('${context/ModificationDate}', 27, 26), 1526: ('context/ModificationDate', 27, 28), 1582: ('', 28, 29), 1584: ('${context/ModificationDate}', 28, 31), 1586: ('context/ModificationDate', 28, 33)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4981206288 = {'class': 'pat-display-time', 'data-pat-display-time': 'output-format: L LTS', 'datetime': '${context/ModificationDate}', }
_static_4981199184 = {'class': 'toolbar-label', }
_static_4983939536 = {'class': 'toolbar-label', }
_static_4983942272 = {'href': '#', 'class': "nav-link ${python:'locked' if locked and actionid == 'history' else ''} ${action/cssClass | nothing} ${python:'active' if selected else None}", 'target': 'action/link_target|nothing', }
_static_4983937760 = {'id': 'contentview-${action/id}', 'class': 'nav-item', }
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

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4983941024
            __attrs_4983941024 = _static_4753720080
            __backup_ploneview_4975067040 = get('ploneview', __marker)

            # <Value 'context/@@plone' (1:40)> -> __value
            __token = 40
            try:
                __zt_tmp = __attrs_4983941024
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'context/@@plone', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['ploneview'] = __value
            __backup_locked_4975066464 = get('locked', __marker)

            # <Value 'view/locked_icon' (2:36)> -> __value
            __token = 93
            try:
                __zt_tmp = __attrs_4983941024
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/locked_icon', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['locked'] = __value
            __backup_icons_4975067088 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (3:34)> -> __value
            __token = 146
            try:
                __zt_tmp = __attrs_4983941024
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['icons'] = __value

            # <Value 'ploneview/showToolbar' (4:33)> -> __condition
            __token = 235
            try:
                __zt_tmp = __attrs_4983941024
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('path', 'ploneview/showToolbar', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4983946832 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4983933344
                __attrs_4983933344 = _static_4753720080
                __backup_action_4975066656 = get('action', __marker)

                # <Value 'options/actions' (6:34)> -> __iterator
                __token = 331
                try:
                    __zt_tmp = __attrs_4983933344
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4754050160('path', 'options/actions', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                (__iterator, ____index_4983937856, ) = getname('repeat')('action', __iterator)
                econtext['action'] = None
                for __item in __iterator:
                    econtext['action'] = __item
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x12910dae0> name=None at 12910c6a0> -> __attrs_4983933968
                    __attrs_4983933968 = _static_4983937760
                    __backup_actionid_4975062144 = get('actionid', __marker)

                    # <Value 'action/id' (8:29)> -> __value
                    __token = 433
                    try:
                        __zt_tmp = __attrs_4983933968
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('path', 'action/id', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['actionid'] = __value
                    __backup_selected_4975066896 = get('selected', __marker)

                    # <Value 'action/selected | python:False' (9:28)> -> __value
                    __token = 472
                    try:
                        __zt_tmp = __attrs_4983933968
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('path', 'action/selected | python:False', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['selected'] = __value

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4983945104
                    __default_4983945104 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution 'contentview-${action/id}' (7:12)> braces_required=True translation=False default='"?"' default_marker='"?"' at 12910f700> -> __attr_id
                    __token = 361
                    __token = 375
                    try:
                        __zt_tmp = __attrs_4983933968
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_4754050160('path', 'action/id', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_id = ('%s%s' % ('contentview-', (__attr_id if (__attr_id is not None) else ''), ))
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
                    __append(' class="nav-item">\n\n        ')

                    # <Static value=<ast.Dict object at 0x12910ec80> name=None at 12910ea70> -> __attrs_4983940832
                    __attrs_4983940832 = _static_4983942272

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4983945776
                    __default_4983945776 = _DEFAULT_MARKER

                    # <Substitution 'action/url' (12:32)> -> __attr_href
                    __token = 709
                    try:
                        __zt_tmp = __attrs_4983940832
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4754050160('path', 'action/url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4983946592
                    __default_4983946592 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "nav-link ${python:'locked' if locked and actionid == 'history' else ''} ${action/cssClass | nothing} ${python:'active' if selected else None}" (11:27)> braces_required=True translation=False default='"?"' default_marker='"?"' at 12910d840> -> __attr_class
                    __token = 534
                    __token = 545
                    try:
                        __zt_tmp = __attrs_4983940832
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4754050160('python', "'locked' if locked and actionid == 'history' else ''", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __token = 608
                    try:
                        __zt_tmp = __attrs_4983940832
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class_606 = _static_4754050160('path', 'action/cssClass | nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_class_606 = __quote(__attr_class_606, '"', '&quot;', None, _DEFAULT_MARKER)
                    __token = 637
                    try:
                        __zt_tmp = __attrs_4983940832
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class_635 = _static_4754050160('python', "'active' if selected else None", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_class_635 = __quote(__attr_class_635, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s%s%s%s%s' % ('nav-link ', (__attr_class if (__attr_class is not None) else ''), ' ', (__attr_class_606 if (__attr_class_606 is not None) else ''), ' ', (__attr_class_635 if (__attr_class_635 is not None) else ''), ))
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

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4983935888
                    __default_4983935888 = _DEFAULT_MARKER

                    # <Substitution 'action/link_target|nothing' (13:33)> -> __attr_target
                    __token = 754
                    try:
                        __zt_tmp = __attrs_4983940832
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_target = _static_4754050160('path', 'action/link_target|nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_target = __quote(__attr_target, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_target is not None):
                        __append((' target="%s"' % __attr_target))
                    __append('>\n\n          ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4983932720
                    __attrs_4983932720 = _static_4753720080

                    # <Value "python:actionid != 'history'" (15:29)> -> __condition
                    __token = 815
                    try:
                        __zt_tmp = __attrs_4983932720
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4754050160('python', "actionid != 'history'", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    if __condition:
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4983934976
                        __attrs_4983934976 = _static_4753720080

                        # <Value "python:action['icon']" (16:37)> -> __condition
                        __token = 883
                        try:
                            __zt_tmp = __attrs_4983934976
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4754050160('python', "action['icon']", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                        if __condition:

                            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4983944240
                            __default_4983944240 = _DEFAULT_MARKER

                            # <Value "python:icons.tag(action['icon'] or 'toolbar-action', tag_class='me-1')" (17:45)> -> __cache_4983932000
                            __token = 951
                            try:
                                __zt_tmp = __attrs_4983934976
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4983932000 = _static_4754050160('python', "icons.tag(action['icon'] or 'toolbar-action', tag_class='me-1')", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                            # <BinOp left=<Value "python:icons.tag(action['icon'] or 'toolbar-action', tag_class='me-1')" (17:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 12910c3d0> -> __condition
                            __expression = __cache_4983932000

                            # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_4983932000
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x12910e1d0> name=None at 12910c790> -> __attrs_4983941984
                        __attrs_4983941984 = _static_4983939536

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="toolbar-label">')

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4983946256
                        __default_4983946256 = _DEFAULT_MARKER

                        # <Value 'action/title' (18:53)> -> __cache_4983935696
                        __token = 1079
                        try:
                            __zt_tmp = __attrs_4983941984
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4983935696 = _static_4754050160('path', 'action/title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                        # <BinOp left=<Value 'action/title' (18:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 12910ecb0> -> __condition
                        __expression = __cache_4983935696

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('View name')
                        else:
                            __content = __cache_4983935696
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>\n          ')
                    __append('\n\n          ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4983934928
                    __attrs_4983934928 = _static_4753720080

                    # <Value "python:actionid == 'history'" (21:33)> -> __condition
                    __token = 1182
                    try:
                        __zt_tmp = __attrs_4983934928
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4754050160('python', "actionid == 'history'", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    if __condition:
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4981196352
                        __attrs_4981196352 = _static_4753720080

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981203600
                        __default_4981203600 = _DEFAULT_MARKER

                        # <Value "python:icons.tag('lock' if locked else action['icon'], tag_class='me-1')" (22:45)> -> __cache_4981206528
                        __token = 1258
                        try:
                            __zt_tmp = __attrs_4981196352
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4981206528 = _static_4754050160('python', "icons.tag('lock' if locked else action['icon'], tag_class='me-1')", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:icons.tag('lock' if locked else action['icon'], tag_class='me-1')" (22:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128e73ca0> -> __condition
                        __expression = __cache_4981206528

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4981206528
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x128e71150> name=None at 128e70d30> -> __attrs_4981205952
                        __attrs_4981205952 = _static_4981199184

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="toolbar-label">\n              ')

                        # <Static value=<ast.Dict object at 0x128e72d10> name=None at 128e71f90> -> __attrs_4981201584
                        __attrs_4981201584 = _static_4981206288

                        # <time ... (0:0)
                        # --------------------------------------------------------
                        __append('<time class="pat-display-time" data-pat-display-time="output-format: L LTS"')

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981207488
                        __default_4981207488 = _DEFAULT_MARKER

                        # <Interpolation value=<Substitution '${context/ModificationDate}' (27:26)> braces_required=True translation=False default='"?"' default_marker='"?"' at 128e71cc0> -> __attr_datetime
                        __token = 1524
                        __token = 1526
                        try:
                            __zt_tmp = __attrs_4981201584
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_datetime = _static_4754050160('path', 'context/ModificationDate', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                        __attr_datetime = __quote(__attr_datetime, '"', '&quot;', None, _DEFAULT_MARKER)
                        __attr_datetime = __attr_datetime
                        if (__attr_datetime is None):
                            pass
                        else:
                            if (__attr_datetime is _DEFAULT_MARKER):
                                __attr_datetime = None
                            else:
                                __tt = type(__attr_datetime)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __attr_datetime = str(__attr_datetime)
                                else:
                                    if (__tt is bytes):
                                        __attr_datetime = decode(__attr_datetime)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __attr_datetime = __attr_datetime.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__attr_datetime)
                                                __attr_datetime = (str(__attr_datetime) if (__attr_datetime is __converted) else __converted)
                                            else:
                                                __attr_datetime = __attr_datetime()
                        if (__attr_datetime is not None):
                            __append((' datetime="%s"' % __attr_datetime))
                        __append('>')

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981199136
                        __default_4981199136 = _DEFAULT_MARKER

                        # <Value '' (28:29)> -> __cache_4981208784
                        __token = 1582
                        try:
                            __zt_tmp = __attrs_4981201584
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4981208784 = _static_4754050160('path', '', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                        # <BinOp left=<Value '' (28:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128e72c50> -> __condition
                        __expression = __cache_4981208784

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <Interpolation value=<Substitution '${context/ModificationDate}' (28:31)> braces_required=True translation=False default='"?"' default_marker='"?"' at 128e71180> -> __content_4355604080
                            __token = 1584
                            __token = 1586
                            try:
                                __zt_tmp = __attrs_4981201584
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __content_4355604080 = _static_4754050160('path', 'context/ModificationDate', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
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
                        else:
                            __content = __cache_4981208784
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</time>\n            </span>\n          ')
                    __append('\n\n        </a>\n\n    </li>')
                    if (__backup_selected_4975066896 is __marker):
                        del econtext['selected']
                    else:
                        econtext['selected'] = __backup_selected_4975066896
                    if (__backup_actionid_4975062144 is __marker):
                        del econtext['actionid']
                    else:
                        econtext['actionid'] = __backup_actionid_4975062144
                    __append('\n  ')
                    ____index_4983937856 -= 1
                    if (____index_4983937856 > 0):
                        __append('')
                if (__backup_action_4975066656 is __marker):
                    del econtext['action']
                else:
                    econtext['action'] = __backup_action_4975066656
                __append('\n')
                __i18n_domain = __previous_i18n_domain_4983946832
            if (__backup_icons_4975067088 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_4975067088
            if (__backup_locked_4975066464 is __marker):
                del econtext['locked']
            else:
                econtext['locked'] = __backup_locked_4975066464
            if (__backup_ploneview_4975067040 is __marker):
                del econtext['ploneview']
            else:
                econtext['ploneview'] = __backup_ploneview_4975067040
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }