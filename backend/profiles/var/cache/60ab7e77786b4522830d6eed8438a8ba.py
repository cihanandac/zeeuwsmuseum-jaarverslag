# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/portlets/portlets/actions.pt'

__tokens = {273: ('context/@@plone_portal_state/portal_url', 8, 29), 361: ('view/showTitle', 10, 44), 405: ('view/title', 11, 27), 430: ('view/title', 11, 52), 558: ('string:actions-${view/category}', 17, 32), 627: ('view/actionLinks', 18, 35), 707: ('nocall:link/icon', 20, 29), 780: ('link/modal|nothing', 22, 32), 835: ('link/url', 23, 35), 880: (" python:'pat-plone-modal' if modal else Non", 24, 35), 975: ('l python:modal if modal else No', 25, 49), 1045: ('not:icon', 26, 33), 1084: ('link/title', 27, 29), 1255: ('icon/absolute_url|icon', 32, 37), 1171: ('icon', 30, 33), 1317: ('string:background-image:url($icon_url);', 33, 38), 1206: ('link/title', 31, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4982437152 = {'style': 'string:background-image:url($icon_url);', }
_static_4982025968 = {'href': '#', 'class': "python:'pat-plone-modal' if modal else None", 'data-pat-plone-modal': 'python:modal if modal else None', }
_static_4982023664 = {'class': 'portletItem', }
_static_4982019344 = {'class': 'string:actions-${view/category}', }
_static_4982019008 = {'class': 'card-body portletContent', }
_static_4753720080 = {}
_static_4982026928 = {'class': 'card-header', }
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4974774448 = {'class': 'card portlet portletActions', }
_static_4771514064 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x11c6786d0> name=None at 11c678430> -> __attrs_4803220512
            __attrs_4803220512 = _static_4771514064
            __previous_i18n_domain_4779168416 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x1288508b0> name=None at 128853250> -> __attrs_4982023184
            __attrs_4982023184 = _static_4974774448
            __backup_portal_url_4975248000 = get('portal_url', __marker)

            # <Value 'context/@@plone_portal_state/portal_url' (8:29)> -> __value
            __token = 273
            try:
                __zt_tmp = __attrs_4982023184
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'context/@@plone_portal_state/portal_url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['portal_url'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card portlet portletActions">\n\n    ')

            # <Static value=<ast.Dict object at 0x128f3b2b0> name=None at 128f3bfa0> -> __attrs_4982023808
            __attrs_4982023808 = _static_4982026928

            # <Value 'view/showTitle' (10:44)> -> __condition
            __token = 361
            try:
                __zt_tmp = __attrs_4982023808
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('path', 'view/showTitle', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="card-header">\n      ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982014112
                __attrs_4982014112 = _static_4753720080

                # <Value 'view/title' (11:27)> -> __condition
                __token = 405
                try:
                    __zt_tmp = __attrs_4982014112
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4754050160('path', 'view/title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                if __condition:

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982029712
                    __default_4982029712 = _DEFAULT_MARKER

                    # <Value 'view/title' (11:52)> -> __cache_4982021696
                    __token = 430
                    try:
                        __zt_tmp = __attrs_4982014112
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4982021696 = _static_4754050160('path', 'view/title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/title' (11:52)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f3aad0> -> __condition
                    __expression = __cache_4982021696

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>\n        Title\n      </span>')
                    else:
                        __content = __cache_4982021696
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                __append('\n    </div>')
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x128f393c0> name=None at 128f3aa40> -> __attrs_4982014064
            __attrs_4982014064 = _static_4982019008

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card-body portletContent">\n      ')

            # <Static value=<ast.Dict object at 0x128f39510> name=None at 128f39f60> -> __attrs_4982024624
            __attrs_4982024624 = _static_4982019344

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append('<ul')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982018528
            __default_4982018528 = _DEFAULT_MARKER

            # <Substitution 'string:actions-${view/category}' (17:32)> -> __attr_class
            __token = 558
            try:
                __zt_tmp = __attrs_4982024624
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4754050160('string', 'actions-${view/category}', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))
            __append('>\n        ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982015984
            __attrs_4982015984 = _static_4753720080
            __backup_link_4982028224 = get('link', __marker)

            # <Value 'view/actionLinks' (18:35)> -> __iterator
            __token = 627
            try:
                __zt_tmp = __attrs_4982015984
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4754050160('path', 'view/actionLinks', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            (__iterator, ____index_4982017232, ) = getname('repeat')('link', __iterator)
            econtext['link'] = None
            for __item in __iterator:
                econtext['link'] = __item
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x128f3a5f0> name=None at 128f3b310> -> __attrs_4982027168
                __attrs_4982027168 = _static_4982023664
                __backup_icon_4982014208 = get('icon', __marker)

                # <Value 'nocall:link/icon' (20:29)> -> __value
                __token = 707
                try:
                    __zt_tmp = __attrs_4982027168
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('nocall', 'link/icon', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['icon'] = __value

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li class="portletItem">\n          ')

                # <Static value=<ast.Dict object at 0x128f3aef0> name=None at 128f3b8b0> -> __attrs_4982439120
                __attrs_4982439120 = _static_4982025968
                __backup_modal_4982028128 = get('modal', __marker)

                # <Value 'link/modal|nothing' (22:32)> -> __value
                __token = 780
                try:
                    __zt_tmp = __attrs_4982439120
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('path', 'link/modal|nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['modal'] = __value

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982024720
                __default_4982024720 = _DEFAULT_MARKER

                # <Substitution 'link/url' (23:35)> -> __attr_href
                __token = 835
                try:
                    __zt_tmp = __attrs_4982439120
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4754050160('path', 'link/url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982030000
                __default_4982030000 = _DEFAULT_MARKER

                # <Substitution "python:'pat-plone-modal' if modal else None" (24:35)> -> __attr_class
                __token = 880
                try:
                    __zt_tmp = __attrs_4982439120
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_4754050160('python', "'pat-plone-modal' if modal else None", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982022944
                __default_4982022944 = _DEFAULT_MARKER

                # <Substitution 'python:modal if modal else None' (25:49)> -> __attr_data_pat_plone_modal
                __token = 975
                try:
                    __zt_tmp = __attrs_4982439120
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_pat_plone_modal = _static_4754050160('python', 'modal if modal else None', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                __attr_data_pat_plone_modal = __quote(__attr_data_pat_plone_modal, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_data_pat_plone_modal is not None):
                    __append((' data-pat-plone-modal="%s"' % __attr_data_pat_plone_modal))
                __append('>\n            ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982431536
                __attrs_4982431536 = _static_4753720080

                # <Value 'not:icon' (26:33)> -> __condition
                __token = 1045
                try:
                    __zt_tmp = __attrs_4982431536
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4754050160('not', 'icon', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982424672
                    __default_4982424672 = _DEFAULT_MARKER

                    # <Value 'link/title' (27:29)> -> __cache_4982427072
                    __token = 1084
                    try:
                        __zt_tmp = __attrs_4982431536
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4982427072 = _static_4754050160('path', 'link/title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'link/title' (27:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f9f3d0> -> __condition
                    __expression = __cache_4982427072

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n              Action\n            ')
                    else:
                        __content = __cache_4982427072
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>')
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x128f9f520> name=None at 128f9dde0> -> __attrs_4982429520
                __attrs_4982429520 = _static_4982437152
                __backup_icon_url_4982272064 = get('icon_url', __marker)

                # <Value 'icon/absolute_url|icon' (32:37)> -> __value
                __token = 1255
                try:
                    __zt_tmp = __attrs_4982429520
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('path', 'icon/absolute_url|icon', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['icon_url'] = __value

                # <Value 'icon' (30:33)> -> __condition
                __token = 1171
                try:
                    __zt_tmp = __attrs_4982429520
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4754050160('path', 'icon', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982434512
                    __default_4982434512 = _DEFAULT_MARKER

                    # <Substitution 'string:background-image:url($icon_url);' (33:38)> -> __attr_style
                    __token = 1317
                    try:
                        __zt_tmp = __attrs_4982429520
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_style = _static_4754050160('string', 'background-image:url($icon_url);', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_style is not None):
                        __append((' style="%s"' % __attr_style))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982432448
                    __default_4982432448 = _DEFAULT_MARKER

                    # <Value 'link/title' (31:29)> -> __cache_4982426208
                    __token = 1206
                    try:
                        __zt_tmp = __attrs_4982429520
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4982426208 = _static_4754050160('path', 'link/title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'link/title' (31:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f9cd00> -> __condition
                    __expression = __cache_4982426208

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n              Action\n            ')
                    else:
                        __content = __cache_4982426208
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>')
                if (__backup_icon_url_4982272064 is __marker):
                    del econtext['icon_url']
                else:
                    econtext['icon_url'] = __backup_icon_url_4982272064
                __append('\n          </a>')
                if (__backup_modal_4982028128 is __marker):
                    del econtext['modal']
                else:
                    econtext['modal'] = __backup_modal_4982028128
                __append('\n        </li>')
                if (__backup_icon_4982014208 is __marker):
                    del econtext['icon']
                else:
                    econtext['icon'] = __backup_icon_4982014208
                __append('\n        ')
                ____index_4982017232 -= 1
                if (____index_4982017232 > 0):
                    __append('')
            if (__backup_link_4982028224 is __marker):
                del econtext['link']
            else:
                econtext['link'] = __backup_link_4982028224
            __append('\n      </ul>\n    </div>\n\n  </div>')
            if (__backup_portal_url_4975248000 is __marker):
                del econtext['portal_url']
            else:
                econtext['portal_url'] = __backup_portal_url_4975248000
            __append('\n\n')
            __i18n_domain = __previous_i18n_domain_4779168416
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }