# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/contenttypes/browser/templates/full_view.pt'

__tokens = {427: ('context/@@uuid | nothing', 11, 58), 694: ('python: item.UID != uuid', 18, 54), 752: ('item/getObject', 19, 31), 792: ('obj/@@full_view_item | nothing', 19, 71), 599: ('context/@@listing_view/macros/entries', 16, 30), 599: ('context/@@listing_view/macros/entries', 16, 30), 483: ('context/@@listing_view/macros/content-core', 13, 28), 483: ('context/@@listing_view/macros/content-core', 13, 28), 251: ('context/@@main_template/macros/master', 6, 21), 251: ('context/@@main_template/macros/master', 6, 21)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4902708096 = 'master'
_static_4902713616 = 'entries'
_static_4906350096 = 'content-core'
_static_4439051040 = __C2ZContextWrapper
_static_4439058528 = __compile_zt_expr
_static_4438893776 = {}

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

    def render_content_core(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4906349664
            __attrs_4906349664 = _static_4438893776
            __backup_uuid_4882758672 = get('uuid', __marker)

            # <Value 'context/@@uuid | nothing' (11:58)> -> __value
            __token = 427
            try:
                __zt_tmp = __attrs_4906349664
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'context/@@uuid | nothing', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['uuid'] = __value
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4902713520
            __attrs_4902713520 = _static_4438893776
            __backup_macroname_4900512576 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x12470f610> name=None at 12470f5b0> -> __value
            __value = _static_4906350096
            econtext['macroname'] = __value

            def __fill_entries(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4902714960
                __attrs_4902714960 = _static_4438893776
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4902700512
                __attrs_4902700512 = _static_4438893776
                __backup_macroname_4609499200 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x124397910> name=None at 1243951e0> -> __value
                __value = _static_4902713616
                econtext['macroname'] = __value

                def __fill_entry(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                    getname = econtext.get_name
                    get = econtext.get

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901034480
                    __attrs_4901034480 = _static_4438893776

                    # <Value 'python: item.UID != uuid' (18:54)> -> __condition
                    __token = 694
                    try:
                        __zt_tmp = __attrs_4901034480
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4439058528('python', ' item.UID != uuid', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    if __condition:
                        __append('\n          ')

                        # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4881066368
                        __attrs_4881066368 = _static_4438893776
                        __backup_obj_4856892528 = get('obj', __marker)

                        # <Value 'item/getObject' (19:31)> -> __value
                        __token = 752
                        try:
                            __zt_tmp = __attrs_4881066368
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4439058528('path', 'item/getObject', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        econtext['obj'] = __value

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4881057200
                        __default_4881057200 = _DEFAULT_MARKER

                        # <Value 'obj/@@full_view_item | nothing' (19:71)> -> __cache_4902767344
                        __token = 792
                        try:
                            __zt_tmp = __attrs_4881066368
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4902767344 = _static_4439058528('path', 'obj/@@full_view_item | nothing', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                        # <BinOp left=<Value 'obj/@@full_view_item | nothing' (19:71)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 122ef06a0> -> __condition
                        __expression = __cache_4902767344

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div />')
                        else:
                            __content = __cache_4902767344
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        if (__backup_obj_4856892528 is __marker):
                            del econtext['obj']
                        else:
                            econtext['obj'] = __backup_obj_4856892528
                        __append('\n        ')
                _slots = econtext['__slot_entry'] = _deque((__fill_entry, ))

                # <Value 'context/@@listing_view/macros/entries' (16:30)> -> __macro
                __token = 599
                try:
                    __zt_tmp = __attrs_4902700512
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_4439058528('path', 'context/@@listing_view/macros/entries', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __token = 599
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_4609499200 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_4609499200
                __append('\n\n    ')
            _slots = econtext['__slot_entries'] = _deque((__fill_entries, ))

            # <Value 'context/@@listing_view/macros/content-core' (13:28)> -> __macro
            __token = 483
            try:
                __zt_tmp = __attrs_4902713520
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4439058528('path', 'context/@@listing_view/macros/content-core', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __token = 483
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4900512576 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4900512576
            __append('\n\n')
            if (__backup_uuid_4882758672 is __marker):
                del econtext['uuid']
            else:
                econtext['uuid'] = __backup_uuid_4882758672
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4902703056
            __attrs_4902703056 = _static_4438893776
            __previous_i18n_domain_4902705168 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4903522048 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x124396380> name=None at 124397700> -> __value
            __value = _static_4902708096
            econtext['macroname'] = __value

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4906351680
                __attrs_4906351680 = _static_4438893776
                __append('\n')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/@@main_template/macros/master' (6:21)> -> __macro
            __token = 251
            try:
                __zt_tmp = __attrs_4902703056
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4439058528('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __token = 251
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4903522048 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4903522048
            __i18n_domain = __previous_i18n_domain_4902705168
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render': render, }