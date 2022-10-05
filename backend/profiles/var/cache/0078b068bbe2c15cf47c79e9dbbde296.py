# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/viewlets/contentviews.pt'

__tokens = {40: ('context/@@plone', 1, 40), 91: ('ploneview/showToolbar', 2, 33), 183: ('view/tabSet1', 5, 29), 231: ('python: view.menu_template(actions=actions)', 6, 32), 380: ('provider:plone.contentmenu', 12, 32), 495: ('view/tabSet2', 17, 29), 543: ('python: view.menu_template(actions=actions)', 18, 32)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4982038512 = {'class': 'border-top my-2', }
_static_4982042304 = {'class': 'border-top my-2', }
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

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982034336
            __attrs_4982034336 = _static_4753720080
            __backup_ploneview_4771662096 = get('ploneview', __marker)

            # <Value 'context/@@plone' (1:40)> -> __value
            __token = 40
            try:
                __zt_tmp = __attrs_4982034336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'context/@@plone', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['ploneview'] = __value

            # <Value 'ploneview/showToolbar' (2:33)> -> __condition
            __token = 91
            try:
                __zt_tmp = __attrs_4982034336
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('path', 'ploneview/showToolbar', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4982045280 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982034576
                __attrs_4982034576 = _static_4753720080
                __backup_actions_4771661520 = get('actions', __marker)

                # <Value 'view/tabSet1' (5:29)> -> __value
                __token = 183
                try:
                    __zt_tmp = __attrs_4982034576
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('path', 'view/tabSet1', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['actions'] = __value
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982036256
                __attrs_4982036256 = _static_4753720080

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982046672
                __default_4982046672 = _DEFAULT_MARKER

                # <Value 'python: view.menu_template(actions=actions)' (6:32)> -> __cache_4982035968
                __token = 231
                try:
                    __zt_tmp = __attrs_4982036256
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4982035968 = _static_4754050160('python', ' view.menu_template(actions=actions)', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                # <BinOp left=<Value 'python: view.menu_template(actions=actions)' (6:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f3f370> -> __condition
                __expression = __cache_4982035968

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div />')
                else:
                    __content = __cache_4982035968
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n  ')
                if (__backup_actions_4771661520 is __marker):
                    del econtext['actions']
                else:
                    econtext['actions'] = __backup_actions_4771661520
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x128f3eec0> name=None at 128f3eef0> -> __attrs_4982041296
                __attrs_4982041296 = _static_4982042304

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li class="border-top my-2">\n\n  ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982041152
                __attrs_4982041152 = _static_4753720080
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982039808
                __attrs_4982039808 = _static_4753720080

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982039424
                __default_4982039424 = _DEFAULT_MARKER

                # <Value 'provider:plone.contentmenu' (12:32)> -> __cache_4982040240
                __token = 380
                try:
                    __zt_tmp = __attrs_4982039808
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4982040240 = _static_4754050160('provider', 'plone.contentmenu', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                # <BinOp left=<Value 'provider:plone.contentmenu' (12:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f3e440> -> __condition
                __expression = __cache_4982040240

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div />')
                else:
                    __content = __cache_4982040240
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n  \n\n  ')

                # <Static value=<ast.Dict object at 0x128f3dff0> name=None at 128f3df90> -> __attrs_4982041776
                __attrs_4982041776 = _static_4982038512

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li class="border-top my-2">\n\n  ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982035056
                __attrs_4982035056 = _static_4753720080
                __backup_actions_4975055808 = get('actions', __marker)

                # <Value 'view/tabSet2' (17:29)> -> __value
                __token = 495
                try:
                    __zt_tmp = __attrs_4982035056
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('path', 'view/tabSet2', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['actions'] = __value
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982033376
                __attrs_4982033376 = _static_4753720080

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982033760
                __default_4982033760 = _DEFAULT_MARKER

                # <Value 'python: view.menu_template(actions=actions)' (18:32)> -> __cache_4982032032
                __token = 543
                try:
                    __zt_tmp = __attrs_4982033376
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4982032032 = _static_4754050160('python', ' view.menu_template(actions=actions)', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                # <BinOp left=<Value 'python: view.menu_template(actions=actions)' (18:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f3ca00> -> __condition
                __expression = __cache_4982032032

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div />')
                else:
                    __content = __cache_4982032032
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n  ')
                if (__backup_actions_4975055808 is __marker):
                    del econtext['actions']
                else:
                    econtext['actions'] = __backup_actions_4975055808
                __append('\n\n')
                __i18n_domain = __previous_i18n_domain_4982045280
            if (__backup_ploneview_4771662096 is __marker):
                del econtext['ploneview']
            else:
                econtext['ploneview'] = __backup_ploneview_4771662096
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }