# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/viewlets/path_bar.pt'

__tokens = {133: ('python:view.breadcrumbs', 2, 132), 283: ('${python:view.navigation_root_url}', 5, 70), 285: ('python:view.navigation_root_url', 5, 72), 367: ('breadcrumbs', 6, 34), 406: ('not: repeat/crumb/end', 7, 25), 463: ("${python:crumb['absolute_url']}", 7, 82), 465: ("python:crumb['absolute_url']", 7, 84), 496: ("${python:crumb['Title']}", 7, 115), 498: ("python:crumb['Title']", 7, 117), 555: ('repeat/crumb/end', 8, 25), 624: ("${python:crumb['Title']}", 8, 94), 626: ("python:crumb['Title']", 8, 96)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4975321648 = {'class': 'breadcrumb-item active', 'aria-current': 'page', }
_static_4982180016 = {'href': "${python:crumb['absolute_url']}", }
_static_4982498128 = {'class': 'breadcrumb-item', }
_static_4753720080 = {}
_static_4982505040 = {'href': '${python:view.navigation_root_url}', }
_static_4982505232 = {'class': 'breadcrumb-item', }
_static_4982502496 = {'class': 'breadcrumb', }
_static_4982503360 = {'class': 'container', }
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4982500864 = {'id': 'portal-breadcrumbs', 'aria-label': 'breadcrumb', 'label_breadcrumb': 'label_breadcrumb', }

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
            __append('\n')

            # <Static value=<ast.Dict object at 0x128faee00> name=None at 128fad900> -> __attrs_4982494480
            __attrs_4982494480 = _static_4982500864
            __backup_breadcrumbs_4975052400 = get('breadcrumbs', __marker)

            # <Value 'python:view.breadcrumbs' (2:132)> -> __value
            __token = 133
            try:
                __zt_tmp = __attrs_4982494480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', 'view.breadcrumbs', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['breadcrumbs'] = __value
            __previous_i18n_domain_4982504992 = __i18n_domain
            __i18n_domain = 'plone'

            # <nav ... (0:0)
            # --------------------------------------------------------
            __append('<nav id="portal-breadcrumbs" aria-label="breadcrumb"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982502208
            __default_4982502208 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x128fad9f0> at 128faf3a0> -> __attr_label_breadcrumb
            __attr_label_breadcrumb = 'label_breadcrumb'
            __attr_label_breadcrumb = translate(__attr_label_breadcrumb, default=__attr_label_breadcrumb, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_label_breadcrumb is not None):
                __append((' label_breadcrumb="%s"' % __attr_label_breadcrumb))
            __append('>\n  ')

            # <Static value=<ast.Dict object at 0x128faf7c0> name=None at 128faf070> -> __attrs_4982497024
            __attrs_4982497024 = _static_4982503360

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="container">\n    ')

            # <Static value=<ast.Dict object at 0x128faf460> name=None at 128fad1b0> -> __attrs_4982496784
            __attrs_4982496784 = _static_4982502496

            # <ol ... (0:0)
            # --------------------------------------------------------
            __append('<ol class="breadcrumb">\n      ')

            # <Static value=<ast.Dict object at 0x128faff10> name=None at 128fac2e0> -> __attrs_4982501728
            __attrs_4982501728 = _static_4982505232

            # <li ... (0:0)
            # --------------------------------------------------------
            __append('<li class="breadcrumb-item">')

            # <Static value=<ast.Dict object at 0x128fafe50> name=None at 128fad960> -> __attrs_4982492368
            __attrs_4982492368 = _static_4982505040

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982503744
            __default_4982503744 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${python:view.navigation_root_url}' (5:70)> braces_required=True translation=False default='"?"' default_marker='"?"' at 128fae980> -> __attr_href
            __token = 283
            __token = 285
            try:
                __zt_tmp = __attrs_4982492368
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4754050160('python', 'view.navigation_root_url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = __attr_href
            if (__attr_href is None):
                pass
            else:
                if (__attr_href is _DEFAULT_MARKER):
                    __attr_href = None
                else:
                    __tt = type(__attr_href)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_href = str(__attr_href)
                    else:
                        if (__tt is bytes):
                            __attr_href = decode(__attr_href)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_href = __attr_href.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_href)
                                    __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                else:
                                    __attr_href = __attr_href()
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append('>')
            __stream_4982491552 = []
            __append_4982491552 = __stream_4982491552.append
            __append_4982491552('Home')
            __msgid_4982491552 = __re_whitespace(''.join(__stream_4982491552)).strip()
            if 'tabs_home':
                __append(translate('tabs_home', mapping=None, default=__msgid_4982491552, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a></li>\n      ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982504320
            __attrs_4982504320 = _static_4753720080
            __backup_crumb_4975051920 = get('crumb', __marker)

            # <Value 'breadcrumbs' (6:34)> -> __iterator
            __token = 367
            try:
                __zt_tmp = __attrs_4982504320
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4754050160('path', 'breadcrumbs', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            (__iterator, ____index_4982499952, ) = getname('repeat')('crumb', __iterator)
            econtext['crumb'] = None
            for __item in __iterator:
                econtext['crumb'] = __item
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x128fae350> name=None at 128fadae0> -> __attrs_4982490496
                __attrs_4982490496 = _static_4982498128

                # <Value 'not: repeat/crumb/end' (7:25)> -> __condition
                __token = 406
                try:
                    __zt_tmp = __attrs_4982490496
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4754050160('not', ' repeat/crumb/end', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                if __condition:

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="breadcrumb-item" >')

                    # <Static value=<ast.Dict object at 0x128f608b0> name=None at 128f62410> -> __attrs_4975319104
                    __attrs_4975319104 = _static_4982180016

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982188272
                    __default_4982188272 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "${python:crumb['absolute_url']}" (7:82)> braces_required=True translation=False default='"?"' default_marker='"?"' at 128f63130> -> __attr_href
                    __token = 463
                    __token = 465
                    try:
                        __zt_tmp = __attrs_4975319104
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4754050160('python', "crumb['absolute_url']", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_href = __attr_href
                    if (__attr_href is None):
                        pass
                    else:
                        if (__attr_href is _DEFAULT_MARKER):
                            __attr_href = None
                        else:
                            __tt = type(__attr_href)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_href = str(__attr_href)
                            else:
                                if (__tt is bytes):
                                    __attr_href = decode(__attr_href)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_href = __attr_href.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_href)
                                            __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                        else:
                                            __attr_href = __attr_href()
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append('>')

                    # <Interpolation value=<Substitution "${python:crumb['Title']}" (7:115)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1288d5d80> -> __content_4355604080
                    __token = 496
                    __token = 498
                    try:
                        __zt_tmp = __attrs_4975319104
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_4355604080 = _static_4754050160('python', "crumb['Title']", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
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
                    __append('</a></li>')
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x1288d6230> name=None at 1288d60b0> -> __attrs_4975321600
                __attrs_4975321600 = _static_4975321648

                # <Value 'repeat/crumb/end' (8:25)> -> __condition
                __token = 555
                try:
                    __zt_tmp = __attrs_4975321600
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4754050160('path', 'repeat/crumb/end', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                if __condition:

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="breadcrumb-item active" aria-current="page">')

                    # <Interpolation value=<Substitution "${python:crumb['Title']}" (8:94)> braces_required=True translation=False default='"?"' default_marker='"?"' at 12910e6b0> -> __content_4355604080
                    __token = 624
                    __token = 626
                    try:
                        __zt_tmp = __attrs_4975321600
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_4355604080 = _static_4754050160('python', "crumb['Title']", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
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
                    __append('</li>')
                __append('\n      ')
                ____index_4982499952 -= 1
                if (____index_4982499952 > 0):
                    __append('')
            if (__backup_crumb_4975051920 is __marker):
                del econtext['crumb']
            else:
                econtext['crumb'] = __backup_crumb_4975051920
            __append('\n    </ol>\n  </div>\n</nav>')
            __i18n_domain = __previous_i18n_domain_4982504992
            if (__backup_breadcrumbs_4975052400 is __marker):
                del econtext['breadcrumbs']
            else:
                econtext['breadcrumbs'] = __backup_breadcrumbs_4975052400
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }