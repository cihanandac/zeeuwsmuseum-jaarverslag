# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/dexterity/browser/tabbed_forms.pt'

__tokens = {418: ('context/global_statusmessage/macros/portal_message', 12, 26), 418: ('context/global_statusmessage/macros/portal_message', 12, 26), 572: ('context/Title', 16, 61), 614: ('python:context.__name__', 16, 103), 722: ('view/tabs', 19, 43), 874: (" python: 'nav-link ' + ('active' if tab[0] == view.label else ''", 22, 33), 795: ("python:context.absolute_url() + '/' + tab[1]", 21, 33), 966: ('python:tab[0]', 23, 25), 1084: ('view/contents|view/render', 28, 40), 231: ('here/prefs_main_template/macros/master', 5, 23), 231: ('here/prefs_main_template/macros/master', 5, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4685504112 = {'id': 'content-core', }
_static_4685512656 = {'class': 'nav-link', 'href': "python:context.absolute_url() + '/' + tab[1]", }
_static_4685508816 = {'class': 'nav-item', }
_static_4685510016 = {'class': 'nav nav-tabs', }
_static_4685506368 = {'class': 'documentFirstHeading', }
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
_static_4685497056 = 'portal_message'
_static_4685510976 = {'class': 'mb-4', }
_static_4676511984 = 'master'
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

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4685496912
            __attrs_4685496912 = _static_4428767312
            __previous_i18n_domain_4685499360 = __i18n_domain
            __i18n_domain = 'plone.z3cform'
            __backup_macroname_4686666880 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x116bde8f0> name=None at 116bdfb20> -> __value
            __value = _static_4676511984
            econtext['macroname'] = __value

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4685496864
                __attrs_4685496864 = _static_4428767312
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x117473940> name=None at 1174737f0> -> __attrs_4685505120
                __attrs_4685505120 = _static_4685510976

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="mb-4"> \n\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4685509584
                __attrs_4685509584 = _static_4428767312
                __backup_macroname_4677680256 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x1174702e0> name=None at 117472080> -> __value
                __value = _static_4685497056
                econtext['macroname'] = __value

                # <Value 'context/global_statusmessage/macros/portal_message' (12:26)> -> __macro
                __token = 418
                try:
                    __zt_tmp = __attrs_4685509584
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_4427992992('path', 'context/global_statusmessage/macros/portal_message', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __token = 418
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_4677680256 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_4677680256
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x117472740> name=None at 117473310> -> __attrs_4685509200
                __attrs_4685509200 = _static_4685506368

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4685503968
                __attrs_4685503968 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685505024
                __default_4685505024 = _DEFAULT_MARKER

                # <Value 'context/Title' (16:61)> -> __cache_4685509056
                __token = 572
                try:
                    __zt_tmp = __attrs_4685503968
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4685509056 = _static_4427992992('path', 'context/Title', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'context/Title' (16:61)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1174739d0> -> __condition
                __expression = __cache_4685509056

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4685509056
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(' (')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4685511648
                __attrs_4685511648 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4672918800
                __default_4672918800 = _DEFAULT_MARKER

                # <Value 'python:context.__name__' (16:103)> -> __cache_4685508576
                __token = 614
                try:
                    __zt_tmp = __attrs_4685511648
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4685508576 = _static_4427992992('python', 'context.__name__', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:context.__name__' (16:103)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116873d00> -> __condition
                __expression = __cache_4685508576

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4685508576
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(')</h1>\n\n    ')

                # <Static value=<ast.Dict object at 0x117473580> name=None at 117473a90> -> __attrs_4685510784
                __attrs_4685510784 = _static_4685510016

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="nav nav-tabs">\n      ')

                # <Static value=<ast.Dict object at 0x1174730d0> name=None at 117472c80> -> __attrs_4685506128
                __attrs_4685506128 = _static_4685508816
                __backup_tab_4685497344 = get('tab', __marker)

                # <Value 'view/tabs' (19:43)> -> __iterator
                __token = 722
                try:
                    __zt_tmp = __attrs_4685506128
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4427992992('path', 'view/tabs', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                (__iterator, ____index_4685510064, ) = getname('repeat')('tab', __iterator)
                econtext['tab'] = None
                for __item in __iterator:
                    econtext['tab'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="nav-item">\n        ')

                    # <Static value=<ast.Dict object at 0x117473fd0> name=None at 117470340> -> __attrs_4685502096
                    __attrs_4685502096 = _static_4685512656

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685511840
                    __default_4685511840 = _DEFAULT_MARKER

                    # <Substitution "python: 'nav-link ' + ('active' if tab[0] == view.label else '')" (22:33)> -> __attr_class
                    __token = 874
                    try:
                        __zt_tmp = __attrs_4685502096
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4427992992('python', " 'nav-link ' + ('active' if tab[0] == view.label else '')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', 'nav-link', _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685497824
                    __default_4685497824 = _DEFAULT_MARKER

                    # <Substitution "python:context.absolute_url() + '/' + tab[1]" (21:33)> -> __attr_href
                    __token = 795
                    try:
                        __zt_tmp = __attrs_4685502096
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4427992992('python', "context.absolute_url() + '/' + tab[1]", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685511792
                    __default_4685511792 = _DEFAULT_MARKER

                    # <Value 'python:tab[0]' (23:25)> -> __cache_4685510352
                    __token = 966
                    try:
                        __zt_tmp = __attrs_4685502096
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4685510352 = _static_4427992992('python', 'tab[0]', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'python:tab[0]' (23:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 117471b70> -> __condition
                    __expression = __cache_4685510352

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4685510352
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</a>\n      </li>')
                    ____index_4685510064 -= 1
                    if (____index_4685510064 > 0):
                        __append('\n      ')
                if (__backup_tab_4685497344 is __marker):
                    del econtext['tab']
                else:
                    econtext['tab'] = __backup_tab_4685497344
                __append('\n    </ul>\n  </header>\n  ')

                # <Static value=<ast.Dict object at 0x117471e70> name=None at 1174702b0> -> __attrs_4685511264
                __attrs_4685511264 = _static_4685504112

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n      ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682929808
                __attrs_4682929808 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682937488
                __default_4682937488 = _DEFAULT_MARKER

                # <Value 'view/contents|view/render' (28:40)> -> __cache_4685498352
                __token = 1084
                try:
                    __zt_tmp = __attrs_4682929808
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4685498352 = _static_4427992992('path', 'view/contents|view/render', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/contents|view/render' (28:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1171fc580> -> __condition
                __expression = __cache_4685498352

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4685498352
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n  </div>\n\n')
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'here/prefs_main_template/macros/master' (5:23)> -> __macro
            __token = 231
            try:
                __zt_tmp = __attrs_4685496912
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4427992992('path', 'here/prefs_main_template/macros/master', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __token = 231
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4686666880 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4686666880
            __i18n_domain = __previous_i18n_domain_4685499360
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }