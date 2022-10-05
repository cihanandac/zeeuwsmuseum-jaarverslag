# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/viewlets/globalstatusmessage.pt'

__tokens = {33: ('nocall: context/@@iconresolver', 1, 33), 100: ('python:view.messages', 2, 35), 151: ('message/type | nothing', 4, 27), 208: (' python:view.display_info_for_mtype(mtype', 5, 33), 277: ('mtype', 6, 24), 300: ("portalMessage ${python:display_info['cssclass']}", 7, 16), 316: ("python:display_info['cssclass']", 7, 32), 414: ("python:icons.tag(display_info['icon'], tag_alt=display_info['msg'], tag_class='statusmessage-icon mb-1 me-2')", 9, 41), 544: ("${python:display_info['msg']}", 10, 16), 546: ("python:display_info['msg']", 10, 18), 640: ('message/message | nothing', 12, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4982345680 = {'class': 'content', }
_static_4982353936 = {'class': "portalMessage ${python:display_info['cssclass']}", 'role': 'alert', }
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

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982357200
            __attrs_4982357200 = _static_4753720080
            __backup_icons_4975061856 = get('icons', __marker)

            # <Value 'nocall: context/@@iconresolver' (1:33)> -> __value
            __token = 33
            try:
                __zt_tmp = __attrs_4982357200
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('nocall', ' context/@@iconresolver', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_message_4771660656 = get('message', __marker)

            # <Value 'python:view.messages' (2:35)> -> __iterator
            __token = 100
            try:
                __zt_tmp = __attrs_4982357200
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4754050160('python', 'view.messages', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            (__iterator, ____index_4982346976, ) = getname('repeat')('message', __iterator)
            econtext['message'] = None
            for __item in __iterator:
                econtext['message'] = __item
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x128f8b010> name=None at 128f886d0> -> __attrs_4982352400
                __attrs_4982352400 = _static_4982353936
                __backup_mtype_4975319296 = get('mtype', __marker)

                # <Value 'message/type | nothing' (4:27)> -> __value
                __token = 151
                try:
                    __zt_tmp = __attrs_4982352400
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('path', 'message/type | nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['mtype'] = __value
                __backup_display_info_4771671696 = get('display_info', __marker)

                # <Value 'python:view.display_info_for_mtype(mtype)' (5:33)> -> __value
                __token = 208
                try:
                    __zt_tmp = __attrs_4982352400
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('python', 'view.display_info_for_mtype(mtype)', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['display_info'] = __value

                # <Value 'mtype' (6:24)> -> __condition
                __token = 277
                try:
                    __zt_tmp = __attrs_4982352400
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4754050160('path', 'mtype', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982342848
                    __default_4982342848 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "portalMessage ${python:display_info['cssclass']}" (7:16)> braces_required=True translation=False default='"?"' default_marker='"?"' at 128f8ad10> -> __attr_class
                    __token = 300
                    __token = 316
                    try:
                        __zt_tmp = __attrs_4982352400
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4754050160('python', "display_info['cssclass']", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s' % ('portalMessage ', (__attr_class if (__attr_class is not None) else ''), ))
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
                    __append(' role="alert">\n        ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982344336
                    __attrs_4982344336 = _static_4753720080

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982343424
                    __default_4982343424 = _DEFAULT_MARKER

                    # <Value "python:icons.tag(display_info['icon'], tag_alt=display_info['msg'], tag_class='statusmessage-icon mb-1 me-2')" (9:41)> -> __cache_4982357968
                    __token = 414
                    try:
                        __zt_tmp = __attrs_4982344336
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4982357968 = _static_4754050160('python', "icons.tag(display_info['icon'], tag_alt=display_info['msg'], tag_class='statusmessage-icon mb-1 me-2')", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag(display_info['icon'], tag_alt=display_info['msg'], tag_class='statusmessage-icon mb-1 me-2')" (9:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f89d20> -> __condition
                    __expression = __cache_4982357968

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4982357968
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982356048
                    __attrs_4982356048 = _static_4753720080

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')

                    # <Interpolation value=<Substitution "${python:display_info['msg']}" (10:16)> braces_required=True translation=False default='"?"' default_marker='"?"' at 128f8b5e0> -> __content_4355604080
                    __token = 544
                    __token = 546
                    try:
                        __zt_tmp = __attrs_4982356048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_4355604080 = _static_4754050160('python', "display_info['msg']", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
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
                    __append('</strong>\n        ')

                    # <Static value=<ast.Dict object at 0x128f88fd0> name=None at 128f88970> -> __attrs_4982357920
                    __attrs_4982357920 = _static_4982345680

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982343088
                    __default_4982343088 = _DEFAULT_MARKER

                    # <Value 'message/message | nothing' (12:27)> -> __cache_4982350336
                    __token = 640
                    try:
                        __zt_tmp = __attrs_4982357920
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4982350336 = _static_4754050160('path', 'message/message | nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'message/message | nothing' (12:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f885e0> -> __condition
                    __expression = __cache_4982350336

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="content">\n            The status message.\n        </span>')
                    else:
                        __content = __cache_4982350336
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n    </div>')
                if (__backup_display_info_4771671696 is __marker):
                    del econtext['display_info']
                else:
                    econtext['display_info'] = __backup_display_info_4771671696
                if (__backup_mtype_4975319296 is __marker):
                    del econtext['mtype']
                else:
                    econtext['mtype'] = __backup_mtype_4975319296
                __append('\n\n')
                ____index_4982346976 -= 1
                if (____index_4982346976 > 0):
                    __append('')
            if (__backup_message_4771660656 is __marker):
                del econtext['message']
            else:
                econtext['message'] = __backup_message_4771660656
            if (__backup_icons_4975061856 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_4975061856
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }