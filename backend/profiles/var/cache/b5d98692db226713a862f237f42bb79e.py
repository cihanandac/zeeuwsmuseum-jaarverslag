# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/nextprevious/links.pt'

__tokens = {173: ('view/enabled|nothing', 4, 25), 226: (' view/isViewTemplate|nothin', 5, 31), 276: ('python:enabled and isViewTemplate', 6, 20), 446: ('view/previous', 12, 31), 486: ('previous', 13, 25), 581: ('previous/url', 15, 31), 699: ('view/next', 20, 27), 735: ('next', 21, 25), 822: ('next/url', 23, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4981791072 = {'rel': 'next', 'href': '', 'title': 'Go to next item', }
_static_4981794960 = {'rel': 'previous', 'href': '', 'title': 'Go to previous item', }
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4981799136 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x128f038e0> name=None at 128f02650> -> __attrs_4981789248
            __attrs_4981789248 = _static_4981799136
            __backup_enabled_4771676016 = get('enabled', __marker)

            # <Value 'view/enabled|nothing' (4:25)> -> __value
            __token = 173
            try:
                __zt_tmp = __attrs_4981789248
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/enabled|nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['enabled'] = __value
            __backup_isViewTemplate_4771666560 = get('isViewTemplate', __marker)

            # <Value 'view/isViewTemplate|nothing' (5:31)> -> __value
            __token = 226
            try:
                __zt_tmp = __attrs_4981789248
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/isViewTemplate|nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['isViewTemplate'] = __value

            # <Value 'python:enabled and isViewTemplate' (6:20)> -> __condition
            __token = 276
            try:
                __zt_tmp = __attrs_4981789248
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('python', 'enabled and isViewTemplate', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x128f02890> name=None at 128f00040> -> __attrs_4981792224
                __attrs_4981792224 = _static_4981794960
                __backup_previous_4771672656 = get('previous', __marker)

                # <Value 'view/previous' (12:31)> -> __value
                __token = 446
                try:
                    __zt_tmp = __attrs_4981792224
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('path', 'view/previous', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['previous'] = __value

                # <Value 'previous' (13:25)> -> __condition
                __token = 486
                try:
                    __zt_tmp = __attrs_4981792224
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4754050160('path', 'previous', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                if __condition:

                    # <link ... (0:0)
                    # --------------------------------------------------------
                    __append('<link rel="previous"')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981796208
                    __default_4981796208 = _DEFAULT_MARKER

                    # <Substitution 'previous/url' (15:31)> -> __attr_href
                    __token = 581
                    try:
                        __zt_tmp = __attrs_4981792224
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4754050160('path', 'previous/url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981791744
                    __default_4981791744 = _DEFAULT_MARKER

                    # <Translate msgid='title_previous_item' node=<ast.Constant object at 0x128f01930> at 128f02dd0> -> __attr_title
                    __attr_title = 'Go to previous item'
                    __attr_title = translate('title_previous_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' />')
                if (__backup_previous_4771672656 is __marker):
                    del econtext['previous']
                else:
                    econtext['previous'] = __backup_previous_4771672656
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x128f01960> name=None at 128f02cb0> -> __attrs_4981798224
                __attrs_4981798224 = _static_4981791072
                __backup_next_4771673328 = get('next', __marker)

                # <Value 'view/next' (20:27)> -> __value
                __token = 699
                try:
                    __zt_tmp = __attrs_4981798224
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('path', 'view/next', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['next'] = __value

                # <Value 'next' (21:25)> -> __condition
                __token = 735
                try:
                    __zt_tmp = __attrs_4981798224
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4754050160('path', 'next', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                if __condition:

                    # <link ... (0:0)
                    # --------------------------------------------------------
                    __append('<link rel="next"')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981790544
                    __default_4981790544 = _DEFAULT_MARKER

                    # <Substitution 'next/url' (23:31)> -> __attr_href
                    __token = 822
                    try:
                        __zt_tmp = __attrs_4981798224
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4754050160('path', 'next/url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981798032
                    __default_4981798032 = _DEFAULT_MARKER

                    # <Translate msgid='title_next_item' node=<ast.Constant object at 0x128f01330> at 128f03430> -> __attr_title
                    __attr_title = 'Go to next item'
                    __attr_title = translate('title_next_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' />')
                if (__backup_next_4771673328 is __marker):
                    del econtext['next']
                else:
                    econtext['next'] = __backup_next_4771673328
                __append('\n\n')
            if (__backup_isViewTemplate_4771666560 is __marker):
                del econtext['isViewTemplate']
            else:
                econtext['isViewTemplate'] = __backup_isViewTemplate_4771666560
            if (__backup_enabled_4771676016 is __marker):
                del econtext['enabled']
            else:
                econtext['enabled'] = __backup_enabled_4771676016
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }