# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/viewlets/membertools.pt'

__tokens = {95: ('here/@@plone_context_state/is_toolbar_visible', 3, 33), 165: (' view/anonymou', 4, 23), 203: ('python:not isAnon and not toolbar_visible', 5, 20), 420: ('python:view.user_actions and not view.anonymous', 10, 21), 583: ('view/homelink_url', 13, 30), 631: ('view/user_name', 14, 28), 816: ('view/user_actions', 18, 33), 868: ('string:membertools-${action/id}', 19, 33), 987: ('action/href', 21, 38), 1039: (' action/link_target|nothin', 22, 39), 1098: ('action/title', 23, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4981802896 = {'href': '', 'class': 'dropdown-item', 'target': 'action/link_target|nothing', }
_static_4981811488 = {'id': 'string:membertools-${action/id}', }
_static_4983940256 = {'class': 'dropdown-menu', 'role': 'menu', 'aria-labelledby': 'dropdownMenu', }
_static_4983945440 = {'class': 'caret', }
_static_4753720080 = {}
_static_4983933584 = {'id': 'user-name', 'class': 'dropdown-toggle', 'data-bs-toggle': 'dropdown', 'href': 'view/homelink_url', }
_static_4983933152 = {'class': 'dropdown dropdown-menu-end', 'id': 'portal-membertools', }
_static_4983935312 = {'class': 'hiddenStructure', }
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4983936656 = {'id': 'portal-membertools-wrapper', }

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

            # <Static value=<ast.Dict object at 0x12910d690> name=None at 12910f7f0> -> __attrs_4983939344
            __attrs_4983939344 = _static_4983936656
            __backup_toolbar_visible_4975058928 = get('toolbar_visible', __marker)

            # <Value 'here/@@plone_context_state/is_toolbar_visible' (3:33)> -> __value
            __token = 95
            try:
                __zt_tmp = __attrs_4983939344
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'here/@@plone_context_state/is_toolbar_visible', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['toolbar_visible'] = __value
            __backup_isAnon_4975053120 = get('isAnon', __marker)

            # <Value 'view/anonymous' (4:23)> -> __value
            __token = 165
            try:
                __zt_tmp = __attrs_4983939344
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/anonymous', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['isAnon'] = __value

            # <Value 'python:not isAnon and not toolbar_visible' (5:20)> -> __condition
            __token = 203
            try:
                __zt_tmp = __attrs_4983939344
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('python', 'not isAnon and not toolbar_visible', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4983937376 = __i18n_domain
                __i18n_domain = 'plone'

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="portal-membertools-wrapper">\n\n  ')

                # <Static value=<ast.Dict object at 0x12910d150> name=None at 12910ff10> -> __attrs_4983932096
                __attrs_4983932096 = _static_4983935312

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="hiddenStructure">')
                __stream_4983935744 = []
                __append_4983935744 = __stream_4983935744.append
                __append_4983935744('Member tools')
                __msgid_4983935744 = __re_whitespace(''.join(__stream_4983935744)).strip()
                if 'heading_member_tools':
                    __append(translate('heading_member_tools', mapping=None, default=__msgid_4983935744, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n\n  ')

                # <Static value=<ast.Dict object at 0x12910c8e0> name=None at 12910de10> -> __attrs_4983943424
                __attrs_4983943424 = _static_4983933152

                # <Value 'python:view.user_actions and not view.anonymous' (10:21)> -> __condition
                __token = 420
                try:
                    __zt_tmp = __attrs_4983943424
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4754050160('python', 'view.user_actions and not view.anonymous', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="dropdown dropdown-menu-end" id="portal-membertools">\n      ')

                    # <Static value=<ast.Dict object at 0x12910ca90> name=None at 12910d7e0> -> __attrs_4983945056
                    __attrs_4983945056 = _static_4983933584

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a id="user-name" class="dropdown-toggle" data-bs-toggle="dropdown"')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4983935792
                    __default_4983935792 = _DEFAULT_MARKER

                    # <Substitution 'view/homelink_url' (13:30)> -> __attr_href
                    __token = 583
                    try:
                        __zt_tmp = __attrs_4983945056
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4754050160('path', 'view/homelink_url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append('>\n         ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4983942896
                    __attrs_4983942896 = _static_4753720080

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4983932384
                    __default_4983932384 = _DEFAULT_MARKER

                    # <Value 'view/user_name' (14:28)> -> __cache_4983933824
                    __token = 631
                    try:
                        __zt_tmp = __attrs_4983942896
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4983933824 = _static_4754050160('path', 'view/user_name', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/user_name' (14:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 12910f730> -> __condition
                    __expression = __cache_4983933824

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>John</span>')
                    else:
                        __content = __cache_4983933824
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n         ')

                    # <Static value=<ast.Dict object at 0x12910f8e0> name=None at 12910ca30> -> __attrs_4983942848
                    __attrs_4983942848 = _static_4983945440

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="caret"></span>\n      </a>\n      ')

                    # <Static value=<ast.Dict object at 0x12910e4a0> name=None at 12910d1b0> -> __attrs_4981806976
                    __attrs_4981806976 = _static_4983940256

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu">\n          ')

                    # <Static value=<ast.Dict object at 0x128f06920> name=None at 128f048e0> -> __attrs_4981806448
                    __attrs_4981806448 = _static_4981811488
                    __backup_action_4975057536 = get('action', __marker)

                    # <Value 'view/user_actions' (18:33)> -> __iterator
                    __token = 816
                    try:
                        __zt_tmp = __attrs_4981806448
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_4754050160('path', 'view/user_actions', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    (__iterator, ____index_4981804480, ) = getname('repeat')('action', __iterator)
                    econtext['action'] = None
                    for __item in __iterator:
                        econtext['action'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li')

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981806736
                        __default_4981806736 = _DEFAULT_MARKER

                        # <Substitution 'string:membertools-${action/id}' (19:33)> -> __attr_id
                        __token = 868
                        try:
                            __zt_tmp = __attrs_4981806448
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_4754050160('string', 'membertools-${action/id}', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((' id="%s"' % __attr_id))
                        __append('>\n              ')

                        # <Static value=<ast.Dict object at 0x128f04790> name=None at 128f07160> -> __attrs_4981816576
                        __attrs_4981816576 = _static_4981802896

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981806352
                        __default_4981806352 = _DEFAULT_MARKER

                        # <Substitution 'action/href' (21:38)> -> __attr_href
                        __token = 987
                        try:
                            __zt_tmp = __attrs_4981816576
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4754050160('path', 'action/href', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' class="dropdown-item"')

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981802848
                        __default_4981802848 = _DEFAULT_MARKER

                        # <Substitution 'action/link_target|nothing' (22:39)> -> __attr_target
                        __token = 1039
                        try:
                            __zt_tmp = __attrs_4981816576
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_target = _static_4754050160('path', 'action/link_target|nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                        __attr_target = __quote(__attr_target, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_target is not None):
                            __append((' target="%s"' % __attr_target))
                        __append('>')

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981802656
                        __default_4981802656 = _DEFAULT_MARKER

                        # <Value 'action/title' (23:30)> -> __cache_4981811440
                        __token = 1098
                        try:
                            __zt_tmp = __attrs_4981816576
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4981811440 = _static_4754050160('path', 'action/title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                        # <BinOp left=<Value 'action/title' (23:30)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f06080> -> __condition
                        __expression = __cache_4981811440

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n                  action title\n              ')
                        else:
                            __content = __cache_4981811440
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</a>\n          </li>')
                        ____index_4981804480 -= 1
                        if (____index_4981804480 > 0):
                            __append('\n          ')
                    if (__backup_action_4975057536 is __marker):
                        del econtext['action']
                    else:
                        econtext['action'] = __backup_action_4975057536
                    __append('\n      </ul>\n  </div>')
                __append('\n\n</div>')
                __i18n_domain = __previous_i18n_domain_4983937376
            if (__backup_isAnon_4975053120 is __marker):
                del econtext['isAnon']
            else:
                econtext['isAnon'] = __backup_isAnon_4975053120
            if (__backup_toolbar_visible_4975058928 is __marker):
                del econtext['toolbar_visible']
            else:
                econtext['toolbar_visible'] = __backup_toolbar_visible_4975058928
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }