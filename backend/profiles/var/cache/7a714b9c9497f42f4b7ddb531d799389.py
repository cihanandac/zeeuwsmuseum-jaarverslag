# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/i18n/locales/browser/languageselector.pt'

__tokens = {29: ('view/available', 1, 29), 115: ('view/showFlags', 4, 28), 156: (' view/language', 5, 25), 196: ('l context/@@plone_context_state/view_u', 6, 23), 262: ('rl view/portal_', 7, 24), 300: ("ons python:context.restrictedTraverse('@@iconresolv", 8, 18), 390: ('languages', 9, 31), 439: ('lang/code', 11, 27), 478: (' lang/selecte', 12, 28), 522: ('s string:language-${cod', 13, 28), 574: ("nt python: selected and 'currentLanguage ' or", 14, 25), 657: ('string:${current}${codeclass}', 15, 32), 749: ('lang/flag|nothing', 18, 29), 795: (' lang/native|lang/nam', 19, 27), 849: ('g python:showFlags and fl', 20, 30), 912: ('string:${here_url}?set_language=${code}', 21, 33), 985: (' nam', 22, 32), 1024: ('showflag', 23, 31), 1075: ("python:icons.tag(flag, tag_class='plone-icon-flag')", 24, 40), 1201: ('not: showflag', 27, 25), 1239: ('name', 28, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4983931376 = {'href': '', 'title': 'name', }
_static_4983945008 = {'class': 'string:${current}${codeclass}', }
_static_4975317472 = {'id': 'portal-languageselector', }
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

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975321552
            __attrs_4975321552 = _static_4753720080

            # <Value 'view/available' (1:29)> -> __condition
            __token = 29
            try:
                __zt_tmp = __attrs_4975321552
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('path', 'view/available', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x1288d51e0> name=None at 1288d61a0> -> __attrs_4975319152
                __attrs_4975319152 = _static_4975317472
                __backup_showFlags_4977863040 = get('showFlags', __marker)

                # <Value 'view/showFlags' (4:28)> -> __value
                __token = 115
                try:
                    __zt_tmp = __attrs_4975319152
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('path', 'view/showFlags', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['showFlags'] = __value
                __backup_languages_4975064160 = get('languages', __marker)

                # <Value 'view/languages' (5:25)> -> __value
                __token = 156
                try:
                    __zt_tmp = __attrs_4975319152
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('path', 'view/languages', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['languages'] = __value
                __backup_here_url_4975062288 = get('here_url', __marker)

                # <Value 'context/@@plone_context_state/view_url' (6:23)> -> __value
                __token = 196
                try:
                    __zt_tmp = __attrs_4975319152
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('path', 'context/@@plone_context_state/view_url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['here_url'] = __value
                __backup_portal_url_4975064880 = get('portal_url', __marker)

                # <Value 'view/portal_url' (7:24)> -> __value
                __token = 262
                try:
                    __zt_tmp = __attrs_4975319152
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('path', 'view/portal_url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['portal_url'] = __value
                __backup_icons_4975066464 = get('icons', __marker)

                # <Value "python:context.restrictedTraverse('@@iconresolver')" (8:18)> -> __value
                __token = 300
                try:
                    __zt_tmp = __attrs_4975319152
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['icons'] = __value

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul id="portal-languageselector">\n    ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4983936848
                __attrs_4983936848 = _static_4753720080
                __backup_lang_4975057872 = get('lang', __marker)

                # <Value 'languages' (9:31)> -> __iterator
                __token = 390
                try:
                    __zt_tmp = __attrs_4983936848
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4754050160('path', 'languages', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                (__iterator, ____index_4983939728, ) = getname('repeat')('lang', __iterator)
                econtext['lang'] = None
                for __item in __iterator:
                    econtext['lang'] = __item
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x12910f730> name=None at 12910c040> -> __attrs_4983943280
                    __attrs_4983943280 = _static_4983945008
                    __backup_code_4975059216 = get('code', __marker)

                    # <Value 'lang/code' (11:27)> -> __value
                    __token = 439
                    try:
                        __zt_tmp = __attrs_4983943280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('path', 'lang/code', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['code'] = __value
                    __backup_selected_4975058400 = get('selected', __marker)

                    # <Value 'lang/selected' (12:28)> -> __value
                    __token = 478
                    try:
                        __zt_tmp = __attrs_4983943280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('path', 'lang/selected', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['selected'] = __value
                    __backup_codeclass_4975055856 = get('codeclass', __marker)

                    # <Value 'string:language-${code}' (13:28)> -> __value
                    __token = 522
                    try:
                        __zt_tmp = __attrs_4983943280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('string', 'language-${code}', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['codeclass'] = __value
                    __backup_current_4975059984 = get('current', __marker)

                    # <Value "python: selected and 'currentLanguage ' or ''" (14:25)> -> __value
                    __token = 574
                    try:
                        __zt_tmp = __attrs_4983943280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('python', " selected and 'currentLanguage ' or ''", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['current'] = __value

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4983934112
                    __default_4983934112 = _DEFAULT_MARKER

                    # <Substitution 'string:${current}${codeclass}' (15:32)> -> __attr_class
                    __token = 657
                    try:
                        __zt_tmp = __attrs_4983943280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4754050160('string', '${current}${codeclass}', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n        ')

                    # <Static value=<ast.Dict object at 0x12910c1f0> name=None at 12910e8c0> -> __attrs_4983939248
                    __attrs_4983939248 = _static_4983931376
                    __backup_flag_4975056816 = get('flag', __marker)

                    # <Value 'lang/flag|nothing' (18:29)> -> __value
                    __token = 749
                    try:
                        __zt_tmp = __attrs_4983939248
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('path', 'lang/flag|nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['flag'] = __value
                    __backup_name_4975055040 = get('name', __marker)

                    # <Value 'lang/native|lang/name' (19:27)> -> __value
                    __token = 795
                    try:
                        __zt_tmp = __attrs_4983939248
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('path', 'lang/native|lang/name', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['name'] = __value
                    __backup_showflag_4975058352 = get('showflag', __marker)

                    # <Value 'python:showFlags and flag' (20:30)> -> __value
                    __token = 849
                    try:
                        __zt_tmp = __attrs_4983939248
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('python', 'showFlags and flag', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['showflag'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4983942128
                    __default_4983942128 = _DEFAULT_MARKER

                    # <Substitution 'string:${here_url}?set_language=${code}' (21:33)> -> __attr_href
                    __token = 912
                    try:
                        __zt_tmp = __attrs_4983939248
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4754050160('string', '${here_url}?set_language=${code}', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4983937568
                    __default_4983937568 = _DEFAULT_MARKER

                    # <Substitution 'name' (22:32)> -> __attr_title
                    __token = 985
                    try:
                        __zt_tmp = __attrs_4983939248
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_4754050160('path', 'name', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append('>\n          ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4983934064
                    __attrs_4983934064 = _static_4753720080

                    # <Value 'showflag' (23:31)> -> __condition
                    __token = 1024
                    try:
                        __zt_tmp = __attrs_4983934064
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4754050160('path', 'showflag', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    if __condition:
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4983934016
                        __attrs_4983934016 = _static_4753720080

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4983944816
                        __default_4983944816 = _DEFAULT_MARKER

                        # <Value "python:icons.tag(flag, tag_class='plone-icon-flag')" (24:40)> -> __cache_4983933104
                        __token = 1075
                        try:
                            __zt_tmp = __attrs_4983934016
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4983933104 = _static_4754050160('python', "icons.tag(flag, tag_class='plone-icon-flag')", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:icons.tag(flag, tag_class='plone-icon-flag')" (24:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 12910d060> -> __condition
                        __expression = __cache_4983933104

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <img ... (0:0)
                            # --------------------------------------------------------
                            __append('<img />')
                        else:
                            __content = __cache_4983933104
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n          ')
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4983934736
                    __attrs_4983934736 = _static_4753720080

                    # <Value 'not: showflag' (27:25)> -> __condition
                    __token = 1201
                    try:
                        __zt_tmp = __attrs_4983934736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4754050160('not', ' showflag', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4983938432
                        __default_4983938432 = _DEFAULT_MARKER

                        # <Value 'name' (28:23)> -> __cache_4983935552
                        __token = 1239
                        try:
                            __zt_tmp = __attrs_4983934736
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4983935552 = _static_4754050160('path', 'name', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                        # <BinOp left=<Value 'name' (28:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 12910d720> -> __condition
                        __expression = __cache_4983935552

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('language name')
                        else:
                            __content = __cache_4983935552
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    __append('\n        </a>')
                    if (__backup_showflag_4975058352 is __marker):
                        del econtext['showflag']
                    else:
                        econtext['showflag'] = __backup_showflag_4975058352
                    if (__backup_name_4975055040 is __marker):
                        del econtext['name']
                    else:
                        econtext['name'] = __backup_name_4975055040
                    if (__backup_flag_4975056816 is __marker):
                        del econtext['flag']
                    else:
                        econtext['flag'] = __backup_flag_4975056816
                    __append('\n      </li>')
                    if (__backup_current_4975059984 is __marker):
                        del econtext['current']
                    else:
                        econtext['current'] = __backup_current_4975059984
                    if (__backup_codeclass_4975055856 is __marker):
                        del econtext['codeclass']
                    else:
                        econtext['codeclass'] = __backup_codeclass_4975055856
                    if (__backup_selected_4975058400 is __marker):
                        del econtext['selected']
                    else:
                        econtext['selected'] = __backup_selected_4975058400
                    if (__backup_code_4975059216 is __marker):
                        del econtext['code']
                    else:
                        econtext['code'] = __backup_code_4975059216
                    __append('\n    ')
                    ____index_4983939728 -= 1
                    if (____index_4983939728 > 0):
                        __append('')
                if (__backup_lang_4975057872 is __marker):
                    del econtext['lang']
                else:
                    econtext['lang'] = __backup_lang_4975057872
                __append('\n  </ul>')
                if (__backup_icons_4975066464 is __marker):
                    del econtext['icons']
                else:
                    econtext['icons'] = __backup_icons_4975066464
                if (__backup_portal_url_4975064880 is __marker):
                    del econtext['portal_url']
                else:
                    econtext['portal_url'] = __backup_portal_url_4975064880
                if (__backup_here_url_4975062288 is __marker):
                    del econtext['here_url']
                else:
                    econtext['here_url'] = __backup_here_url_4975062288
                if (__backup_languages_4975064160 is __marker):
                    del econtext['languages']
                else:
                    econtext['languages'] = __backup_languages_4975064160
                if (__backup_showFlags_4977863040 is __marker):
                    del econtext['showFlags']
                else:
                    econtext['showFlags'] = __backup_showFlags_4977863040
                __append('\n')
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }