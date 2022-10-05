# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/locking/browser/info.pt'

__tokens = {77: ('view/info/is_locked_for_current_user', 3, 24), 141: (' view/lock_is_stealabl', 4, 26), 194: ('s view/lock_in', 5, 28), 238: ('locked', 6, 24), 398: ('lock_details/author_page', 11, 27), 647: ('lock_details/author_page', 16, 34), 590: ('lock_details/fullname', 15, 26), 738: ('lock_details/time_difference', 18, 29), 858: ('not:lock_details/author_page', 21, 27), 1060: ('lock_details/fullname', 25, 29), 1148: ('lock_details/time_difference', 27, 29), 1245: ('stealable', 29, 29), 1293: ('string:${context/absolute_url}/@@plone_lock_operations/force_unlock', 30, 37)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4982344384 = {'type': 'submit', 'value': 'Unlock', }
_static_4982265824 = {'method': 'POST', 'action': 'string:${context/absolute_url}/@@plone_lock_operations/force_unlock', }
_static_4982266208 = {'href': 'lock_details/author_page', }
_static_4982267696 = {'class': 'portalMessage info', }
_static_4753720080 = {}
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4982267360 = {'id': 'plone-lock-status', }

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

            # <Static value=<ast.Dict object at 0x128f75de0> name=None at 128f77d60> -> __attrs_4982264912
            __attrs_4982264912 = _static_4982267360
            __backup_locked_4975055904 = get('locked', __marker)

            # <Value 'view/info/is_locked_for_current_user' (3:24)> -> __value
            __token = 77
            try:
                __zt_tmp = __attrs_4982264912
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/info/is_locked_for_current_user', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['locked'] = __value
            __backup_stealable_4975063104 = get('stealable', __marker)

            # <Value 'view/lock_is_stealable' (4:26)> -> __value
            __token = 141
            try:
                __zt_tmp = __attrs_4982264912
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/lock_is_stealable', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['stealable'] = __value
            __backup_lock_details_4975052304 = get('lock_details', __marker)

            # <Value 'view/lock_info' (5:28)> -> __value
            __token = 194
            try:
                __zt_tmp = __attrs_4982264912
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/lock_info', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['lock_details'] = __value
            __previous_i18n_domain_4982264336 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="plone-lock-status">\n  ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982273984
            __attrs_4982273984 = _static_4753720080

            # <Value 'locked' (6:24)> -> __condition
            __token = 238
            try:
                __zt_tmp = __attrs_4982273984
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('path', 'locked', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x128f75f30> name=None at 128f74cd0> -> __attrs_4982262800
                __attrs_4982262800 = _static_4982267696

                # <dl ... (0:0)
                # --------------------------------------------------------
                __append('<dl class="portalMessage info">\n      ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982273600
                __attrs_4982273600 = _static_4753720080

                # <dt ... (0:0)
                # --------------------------------------------------------
                __append('<dt>')
                __stream_4982274848 = []
                __append_4982274848 = __stream_4982274848.append
                __append_4982274848('Locked')
                __msgid_4982274848 = __re_whitespace(''.join(__stream_4982274848)).strip()
                if 'label_locked':
                    __append(translate('label_locked', mapping=None, default=__msgid_4982274848, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</dt>\n      ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982267024
                __attrs_4982267024 = _static_4753720080

                # <dd ... (0:0)
                # --------------------------------------------------------
                __append('<dd>\n        ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982262224
                __attrs_4982262224 = _static_4753720080

                # <Value 'lock_details/author_page' (11:27)> -> __condition
                __token = 398
                try:
                    __zt_tmp = __attrs_4982262224
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4754050160('path', 'lock_details/author_page', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                if __condition:
                    __stream_4984152224_time = ''
                    __stream_4984152224_author = ''
                    __stream_4982262560 = []
                    __append_4982262560 = __stream_4982262560.append
                    __append_4982262560('\n          This item was locked by\n          ')
                    __stream_4984152224_author = []
                    __append_4984152224_author = __stream_4984152224_author.append

                    # <Static value=<ast.Dict object at 0x128f75960> name=None at 128f74850> -> __attrs_4982265440
                    __attrs_4982265440 = _static_4982266208

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_4984152224_author('<a')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982263328
                    __default_4982263328 = _DEFAULT_MARKER

                    # <Substitution 'lock_details/author_page' (16:34)> -> __attr_href
                    __token = 647
                    try:
                        __zt_tmp = __attrs_4982265440
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4754050160('path', 'lock_details/author_page', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_4984152224_author((' href="%s"' % __attr_href))
                    __append_4984152224_author('>')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982271488
                    __default_4982271488 = _DEFAULT_MARKER

                    # <Value 'lock_details/fullname' (15:26)> -> __cache_4982265488
                    __token = 590
                    try:
                        __zt_tmp = __attrs_4982265440
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4982265488 = _static_4754050160('path', 'lock_details/fullname', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/fullname' (15:26)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f75300> -> __condition
                    __expression = __cache_4982265488

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4982265488
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_4984152224_author(__content)
                    __append_4984152224_author('</a>')
                    __append_4982262560('${author}')
                    __stream_4984152224_author = ''.join(__stream_4984152224_author)
                    __append_4982262560('\n          ')
                    __stream_4984152224_time = []
                    __append_4984152224_time = __stream_4984152224_time.append

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982274752
                    __attrs_4982274752 = _static_4753720080

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_4984152224_time('<span>')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982275280
                    __default_4982275280 = _DEFAULT_MARKER

                    # <Value 'lock_details/time_difference' (18:29)> -> __cache_4982266640
                    __token = 738
                    try:
                        __zt_tmp = __attrs_4982274752
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4982266640 = _static_4754050160('path', 'lock_details/time_difference', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/time_difference' (18:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f740d0> -> __condition
                    __expression = __cache_4982266640

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4982266640
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_4984152224_time(__content)
                    __append_4984152224_time('</span>')
                    __append_4982262560('${time}')
                    __stream_4984152224_time = ''.join(__stream_4984152224_time)
                    __append_4982262560(' ago.\n        ')
                    __msgid_4982262560 = __re_whitespace(''.join(__stream_4982262560)).strip()
                    if 'description_webdav_locked_by_author_on_time':
                        __append(translate('description_webdav_locked_by_author_on_time', mapping={'author': __stream_4984152224_author, 'time': __stream_4984152224_time, }, default=__msgid_4982262560, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982272352
                __attrs_4982272352 = _static_4753720080

                # <Value 'not:lock_details/author_page' (21:27)> -> __condition
                __token = 858
                try:
                    __zt_tmp = __attrs_4982272352
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4754050160('not', 'lock_details/author_page', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                if __condition:
                    __stream_4984152224_time = ''
                    __stream_4984152224_author = ''
                    __stream_4982264816 = []
                    __append_4982264816 = __stream_4982264816.append
                    __append_4982264816('\n          This item was locked by\n          ')
                    __stream_4984152224_author = []
                    __append_4984152224_author = __stream_4984152224_author.append

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982356336
                    __attrs_4982356336 = _static_4753720080

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_4984152224_author('<span>')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982262368
                    __default_4982262368 = _DEFAULT_MARKER

                    # <Value 'lock_details/fullname' (25:29)> -> __cache_4982268464
                    __token = 1060
                    try:
                        __zt_tmp = __attrs_4982356336
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4982268464 = _static_4754050160('path', 'lock_details/fullname', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/fullname' (25:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f741c0> -> __condition
                    __expression = __cache_4982268464

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4982268464
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_4984152224_author(__content)
                    __append_4984152224_author('</span>')
                    __append_4982264816('${author}')
                    __stream_4984152224_author = ''.join(__stream_4984152224_author)
                    __append_4982264816('\n          ')
                    __stream_4984152224_time = []
                    __append_4984152224_time = __stream_4984152224_time.append

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982342320
                    __attrs_4982342320 = _static_4753720080

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_4984152224_time('<span>')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982357824
                    __default_4982357824 = _DEFAULT_MARKER

                    # <Value 'lock_details/time_difference' (27:29)> -> __cache_4982354464
                    __token = 1148
                    try:
                        __zt_tmp = __attrs_4982342320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4982354464 = _static_4754050160('path', 'lock_details/time_difference', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/time_difference' (27:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f8a7d0> -> __condition
                    __expression = __cache_4982354464

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4982354464
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_4984152224_time(__content)
                    __append_4984152224_time('</span>')
                    __append_4982264816('${time}')
                    __stream_4984152224_time = ''.join(__stream_4984152224_time)
                    __append_4982264816(' ago.\n        ')
                    __msgid_4982264816 = __re_whitespace(''.join(__stream_4982264816)).strip()
                    if 'description_webdav_locked_by_author_on_time':
                        __append(translate('description_webdav_locked_by_author_on_time', mapping={'author': __stream_4984152224_author, 'time': __stream_4984152224_time, }, default=__msgid_4982264816, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x128f757e0> name=None at 128f742e0> -> __attrs_4982356432
                __attrs_4982356432 = _static_4982265824

                # <Value 'stealable' (29:29)> -> __condition
                __token = 1245
                try:
                    __zt_tmp = __attrs_4982356432
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4754050160('path', 'stealable', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                if __condition:

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form method="POST"')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982349376
                    __default_4982349376 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/absolute_url}/@@plone_lock_operations/force_unlock' (30:37)> -> __attr_action
                    __token = 1293
                    try:
                        __zt_tmp = __attrs_4982356432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_4754050160('string', '${context/absolute_url}/@@plone_lock_operations/force_unlock', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((' action="%s"' % __attr_action))
                    __append('>\n          ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982353168
                    __attrs_4982353168 = _static_4753720080

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_4984153120_unlock_button = ''
                    __stream_4982348080 = []
                    __append_4982348080 = __stream_4982348080.append
                    __append_4982348080('\n            If you are certain this user has abandoned the object,\n            you may\n            ')
                    __stream_4984153120_unlock_button = []
                    __append_4984153120_unlock_button = __stream_4984153120_unlock_button.append

                    # <Static value=<ast.Dict object at 0x128f88ac0> name=None at 128f8a950> -> __attrs_4982354848
                    __attrs_4982354848 = _static_4982344384

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append_4984153120_unlock_button('<input type="submit"')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982345872
                    __default_4982345872 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<ast.Constant object at 0x128f88a00> at 128f88130> -> __attr_value
                    __attr_value = 'Unlock'
                    __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append_4984153120_unlock_button((' value="%s"' % __attr_value))
                    __append_4984153120_unlock_button(' />')
                    __append_4982348080('${unlock_button}')
                    __stream_4984153120_unlock_button = ''.join(__stream_4984153120_unlock_button)
                    __append_4982348080('\n            the object. You will then be able to edit it.\n          ')
                    __msgid_4982348080 = __re_whitespace(''.join(__stream_4982348080)).strip()
                    if 'description_webdav_locked_steal':
                        __append(translate('description_webdav_locked_steal', mapping={'unlock_button': __stream_4984153120_unlock_button, }, default=__msgid_4982348080, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n        </form>')
                __append('\n      </dd>\n    </dl>\n  ')
            __append('\n</div>')
            __i18n_domain = __previous_i18n_domain_4982264336
            if (__backup_lock_details_4975052304 is __marker):
                del econtext['lock_details']
            else:
                econtext['lock_details'] = __backup_lock_details_4975052304
            if (__backup_stealable_4975063104 is __marker):
                del econtext['stealable']
            else:
                econtext['stealable'] = __backup_stealable_4975063104
            if (__backup_locked_4975055904 is __marker):
                del econtext['locked']
            else:
                econtext['locked'] = __backup_locked_4975055904
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }