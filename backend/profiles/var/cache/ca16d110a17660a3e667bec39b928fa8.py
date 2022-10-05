# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/viewlets/sections.pt'

__tokens = {182: ('python:view.navtree', 4, 17), 309: ('python:view.render_globalnav()', 7, 36)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4982403952 = {'class': 'navbar-toggler-icon', }
_static_4982398048 = {'class': 'navbar-toggler', 'type': 'button', 'aria-label': 'Toggle navigation', }
_static_4982398288 = {'class': 'navbar-nav', 'id': 'portal-globalnav', }
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

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982403184
            __attrs_4982403184 = _static_4753720080

            # <Value 'python:view.navtree' (4:17)> -> __condition
            __token = 182
            try:
                __zt_tmp = __attrs_4982403184
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('python', 'view.navtree', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4982399824 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x128f95d50> name=None at 128f96290> -> __attrs_4982391232
                __attrs_4982391232 = _static_4982398288

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="navbar-nav" id="portal-globalnav">\n    ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982406112
                __attrs_4982406112 = _static_4753720080

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982404672
                __default_4982404672 = _DEFAULT_MARKER

                # <Value 'python:view.render_globalnav()' (7:36)> -> __cache_4982396560
                __token = 309
                try:
                    __zt_tmp = __attrs_4982406112
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4982396560 = _static_4754050160('python', 'view.render_globalnav()', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:view.render_globalnav()' (7:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f95c00> -> __condition
                __expression = __cache_4982396560

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <navtree ... (0:0)
                    # --------------------------------------------------------
                    __append('<navtree />')
                else:
                    __content = __cache_4982396560
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n  </ul>\n\n  ')

                # <Static value=<ast.Dict object at 0x128f95c60> name=None at 128f94dc0> -> __attrs_4982401744
                __attrs_4982401744 = _static_4982398048

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="navbar-toggler" type="button"')

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982403808
                __default_4982403808 = _DEFAULT_MARKER

                # <Translate msgid='label_toggle_navigation' node=<ast.Constant object at 0x128f97df0> at 128f967a0> -> __attr_aria_label
                __attr_aria_label = 'Toggle navigation'
                __attr_aria_label = translate('label_toggle_navigation', default=__attr_aria_label, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_aria_label is not None):
                    __append((' aria-label="%s"' % __attr_aria_label))
                __append('>\n    ')

                # <Static value=<ast.Dict object at 0x128f97370> name=None at 128f96b30> -> __attrs_4982397232
                __attrs_4982397232 = _static_4982403952

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span class="navbar-toggler-icon"></span>\n  </button>\n\n')
                __i18n_domain = __previous_i18n_domain_4982399824
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }