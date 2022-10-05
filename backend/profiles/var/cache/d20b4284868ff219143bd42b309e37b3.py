# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/contenttypes/browser/templates/document.pt'

__tokens = {453: ("python:  getattr(context, 'table_of_contents', False)", 12, 36), 648: ("python:getattr(context, 'text', None)", 16, 24), 584: ("${python: toc and 'pat-autotoc' or ''}", 15, 43), 586: ("python: toc and 'pat-autotoc' or ''", 15, 45), 719: ('python:context.text.output_relative_to(view.context)', 17, 32), 251: ('context/@@main_template/macros/master', 6, 21), 251: ('context/@@main_template/macros/master', 6, 21)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4803161888 = 'master'
_static_4803151952 = {'id': 'parent-fieldname-text', 'class': "${python: toc and 'pat-autotoc' or ''}", }
_static_4803152192 = {'id': 'section-text', }
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

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4803160592
            __attrs_4803160592 = _static_4753720080
            __backup_toc_4974779968 = get('toc', __marker)

            # <Value "python:  getattr(context, 'table_of_contents', False)" (12:36)> -> __value
            __token = 453
            try:
                __zt_tmp = __attrs_4803160592
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', "  getattr(context, 'table_of_contents', False)", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['toc'] = __value
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x11e4a4940> name=None at 128e6aef0> -> __attrs_4981280384
            __attrs_4981280384 = _static_4803152192

            # <section ... (0:0)
            # --------------------------------------------------------
            __append('<section id="section-text">\n    ')

            # <Static value=<ast.Dict object at 0x11e4a4850> name=None at 11e4a7c10> -> __attrs_4803159776
            __attrs_4803159776 = _static_4803151952

            # <Value "python:getattr(context, 'text', None)" (16:24)> -> __condition
            __token = 648
            try:
                __zt_tmp = __attrs_4803159776
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('python', "getattr(context, 'text', None)", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="parent-fieldname-text"')

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4803163184
                __default_4803163184 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution "${python: toc and 'pat-autotoc' or ''}" (15:43)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11e4a4520> -> __attr_class
                __token = 584
                __token = 586
                try:
                    __zt_tmp = __attrs_4803159776
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_4754050160('python', " toc and 'pat-autotoc' or ''", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_class = __attr_class
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
                __append('>')

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4803151520
                __default_4803151520 = _DEFAULT_MARKER

                # <Value 'python:context.text.output_relative_to(view.context)' (17:32)> -> __cache_4981585184
                __token = 719
                try:
                    __zt_tmp = __attrs_4803159776
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4981585184 = _static_4754050160('python', 'context.text.output_relative_to(view.context)', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:context.text.output_relative_to(view.context)' (17:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128ecfc10> -> __condition
                __expression = __cache_4981585184

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n      Text\n    ')
                else:
                    __content = __cache_4981585184
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('</div>')
            __append('\n  </section>\n\n')
            if (__backup_toc_4974779968 is __marker):
                del econtext['toc']
            else:
                econtext['toc'] = __backup_toc_4974779968
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

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4803164288
            __attrs_4803164288 = _static_4753720080
            __previous_i18n_domain_4803163616 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4360823040 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x11e4a6f20> name=None at 11e4a6b30> -> __value
            __value = _static_4803161888
            econtext['macroname'] = __value

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4803163424
                __attrs_4803163424 = _static_4753720080
                __append('\n')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/@@main_template/macros/master' (6:21)> -> __macro
            __token = 251
            try:
                __zt_tmp = __attrs_4803164288
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4754050160('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __token = 251
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4360823040 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4360823040
            __i18n_domain = __previous_i18n_domain_4803163616
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render': render, }