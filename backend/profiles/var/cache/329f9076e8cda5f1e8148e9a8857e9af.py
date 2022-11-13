# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/viewlets/history_view.pt'

__tokens = {534: ('here/@@contenthistory', 15, 36), 261: ('context/main_template/macros/master', 6, 23), 261: ('context/main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque

_static_4439051040 = __C2ZContextWrapper
_static_4439058528 = __compile_zt_expr
_static_4900162576 = 'master'
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900168288
            __attrs_4900168288 = _static_4438893776
            __previous_i18n_domain_4900165600 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4898963584 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x124128c10> name=None at 124129480> -> __value
            __value = _static_4900162576
            econtext['macroname'] = __value

            def __fill_content_description(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900170016
                __attrs_4900170016 = _static_4438893776
            _slots = econtext['__slot_content_description'] = _deque((__fill_content_description, ))

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900163440
                __attrs_4900163440 = _static_4438893776
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900171552
                __attrs_4900171552 = _static_4438893776

                # <h3 ... (0:0)
                # --------------------------------------------------------
                __append('<h3>')
                __stream_4900170256 = []
                __append_4900170256 = __stream_4900170256.append
                __append_4900170256('History')
                __msgid_4900170256 = __re_whitespace(''.join(__stream_4900170256)).strip()
                if 'label_history':
                    __append(translate('label_history', mapping=None, default=__msgid_4900170256, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h3>\n        ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900173088
                __attrs_4900173088 = _static_4438893776

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900172896
                __default_4900172896 = _DEFAULT_MARKER

                # <Value 'here/@@contenthistory' (15:36)> -> __cache_4900172416
                __token = 534
                try:
                    __zt_tmp = __attrs_4900173088
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4900172416 = _static_4439058528('path', 'here/@@contenthistory', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'here/@@contenthistory' (15:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 12412b340> -> __condition
                __expression = __cache_4900172416

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div>Content History</div>')
                else:
                    __content = __cache_4900172416
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n    ')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_4900168288
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4439058528('path', 'context/main_template/macros/master', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4898963584 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4898963584
            __i18n_domain = __previous_i18n_domain_4900165600
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }