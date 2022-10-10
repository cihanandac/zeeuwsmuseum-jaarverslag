# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/registry/browser/templates/controlpanel_layout.pt'

__tokens = {425: ('view/label', 14, 21), 488: ('view/description | nothing', 15, 35), 539: ('view/description', 15, 86), 616: ('context/@@global_statusmessage/macros/portal_message', 19, 24), 616: ('context/@@global_statusmessage/macros/portal_message', 19, 24), 799: ('view/contents', 25, 35), 261: ('context/@@prefs_main_template/macros/master', 6, 23), 261: ('context/@@prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4682736992 = {'id': 'layout-contents', }
_static_4682741360 = {'id': 'content-core', }
_static_4682743520 = 'portal_message'
_static_4682743088 = {'class': 'lead', }
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
_static_4678271472 = 'master'
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

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682738576
            __attrs_4682738576 = _static_4428767312
            __previous_i18n_domain_4682738480 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4678728000 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x116d8c1f0> name=None at 116d8d960> -> __value
            __value = _static_4678271472
            econtext['macroname'] = __value

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682729168
                __attrs_4682729168 = _static_4428767312
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682735312
                __attrs_4682735312 = _static_4428767312

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682737280
                __attrs_4682737280 = _static_4428767312

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682729744
                __default_4682729744 = _DEFAULT_MARKER

                # <Value 'view/label' (14:21)> -> __cache_4682739248
                __token = 425
                try:
                    __zt_tmp = __attrs_4682737280
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4682739248 = _static_4427992992('path', 'view/label', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/label' (14:21)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1171cee00> -> __condition
                __expression = __cache_4682739248

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('View Title')
                else:
                    __content = __cache_4682739248
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</h1>\n    ')

                # <Static value=<ast.Dict object at 0x1171cfd30> name=None at 1171cc5b0> -> __attrs_4682743424
                __attrs_4682743424 = _static_4682743088

                # <Value 'view/description | nothing' (15:35)> -> __condition
                __token = 488
                try:
                    __zt_tmp = __attrs_4682743424
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'view/description | nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="lead">')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682743280
                    __default_4682743280 = _DEFAULT_MARKER

                    # <Value 'view/description' (15:86)> -> __cache_4682728976
                    __token = 539
                    try:
                        __zt_tmp = __attrs_4682743424
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4682728976 = _static_4427992992('path', 'view/description', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/description' (15:86)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1171cdba0> -> __condition
                    __expression = __cache_4682728976

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('View Description')
                    else:
                        __content = __cache_4682728976
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</p>')
                __append('\n\n  </header>\n\n  ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682728688
                __attrs_4682728688 = _static_4428767312
                __backup_macroname_4680800384 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x1171cfee0> name=None at 1171ccb20> -> __value
                __value = _static_4682743520
                econtext['macroname'] = __value

                # <Value 'context/@@global_statusmessage/macros/portal_message' (19:24)> -> __macro
                __token = 616
                try:
                    __zt_tmp = __attrs_4682728688
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_4427992992('path', 'context/@@global_statusmessage/macros/portal_message', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __token = 616
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_4680800384 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_4680800384
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x1171cf670> name=None at 1171cd060> -> __attrs_4682738288
                __attrs_4682738288 = _static_4682741360

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n    ')

                # <Static value=<ast.Dict object at 0x1171ce560> name=None at 1171cde70> -> __attrs_4682741264
                __attrs_4682741264 = _static_4682736992

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="layout-contents">\n      ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682729936
                __attrs_4682729936 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682735744
                __default_4682735744 = _DEFAULT_MARKER

                # <Value 'view/contents' (25:35)> -> __cache_4682727632
                __token = 799
                try:
                    __zt_tmp = __attrs_4682729936
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4682727632 = _static_4427992992('path', 'view/contents', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/contents' (25:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1171cc850> -> __condition
                __expression = __cache_4682727632

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span />')
                else:
                    __content = __cache_4682727632
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n    </div>\n  </div>\n\n')
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'context/@@prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_4682738576
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4427992992('path', 'context/@@prefs_main_template/macros/master', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4678728000 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4678728000
            __i18n_domain = __previous_i18n_domain_4682738480
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }