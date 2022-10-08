# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/content/browser/contents/templates/folder_contents.pt'

__tokens = {861: ('context/@@authenticator/authenticator', 20, 37), 982: ('view/options', 22, 45), 449: ("python:request.set('enable_border', 1)", 11, 32), 533: (" python:request.set('disable_plone.leftcolumn', 1", 12, 44), 628: ("o python:request.set('disable_plone.rightcolumn', ", 13, 43), 408: ('nothing', 10, 33), 261: ('context/main_template/macros/master', 6, 23), 261: ('context/main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4481429280 = 'master'
_static_4481430816 = {'class': 'pat-structure', 'data-pat-structure': 'view/options', }
_static_4417565216 = __C2ZContextWrapper
_static_4417553984 = __compile_zt_expr
_static_4418309904 = {}

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

            # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4481431296
            __attrs_4481431296 = _static_4418309904
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4481419680
            __attrs_4481419680 = _static_4418309904

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4481420352
            __default_4481420352 = _DEFAULT_MARKER

            # <Value 'context/@@authenticator/authenticator' (20:37)> -> __cache_4481419824
            __token = 861
            try:
                __zt_tmp = __attrs_4481419680
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4481419824 = _static_4417553984('path', 'context/@@authenticator/authenticator', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/@@authenticator/authenticator' (20:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107619600> at 10b1d0f40> -> __condition
            __expression = __cache_4481419824

            # <Symbol value=<DEFAULT> at 107619600> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span/>')
            else:
                __content = __cache_4481419824
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x10b1d3520> name=None at 10b1d3610> -> __attrs_4481430432
            __attrs_4481430432 = _static_4481430816

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="pat-structure"')

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4481419440
            __default_4481419440 = _DEFAULT_MARKER

            # <Substitution 'view/options' (22:45)> -> __attr_data_pat_structure
            __token = 982
            try:
                __zt_tmp = __attrs_4481430432
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_pat_structure = _static_4417553984('path', 'view/options', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_data_pat_structure = __quote(__attr_data_pat_structure, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_pat_structure is not None):
                __append((' data-pat-structure="%s"' % __attr_data_pat_structure))
            __append(' />\n    ')
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

            # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4481428272
            __attrs_4481428272 = _static_4418309904
            __previous_i18n_domain_4481427984 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4481382528 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x10b1d2f20> name=None at 10b1d2f80> -> __value
            __value = _static_4481429280
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4481425344
                __attrs_4481425344 = _static_4418309904
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4481423472
                __attrs_4481423472 = _static_4418309904
                __backup_dummy_4477229360 = get('dummy', __marker)

                # <Value "python:request.set('enable_border', 1)" (11:32)> -> __value
                __token = 449
                try:
                    __zt_tmp = __attrs_4481423472
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4417553984('python', "request.set('enable_border', 1)", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                econtext['dummy'] = __value
                __backup_disable_column_one_4476352880 = get('disable_column_one', __marker)

                # <Value "python:request.set('disable_plone.leftcolumn', 1)" (12:44)> -> __value
                __token = 533
                try:
                    __zt_tmp = __attrs_4481423472
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4417553984('python', "request.set('disable_plone.leftcolumn', 1)", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                econtext['disable_column_one'] = __value
                __backup_disable_column_two_4477077488 = get('disable_column_two', __marker)

                # <Value "python:request.set('disable_plone.rightcolumn', 1)" (13:43)> -> __value
                __token = 628
                try:
                    __zt_tmp = __attrs_4481423472
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4417553984('python', "request.set('disable_plone.rightcolumn', 1)", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                econtext['disable_column_two'] = __value

                # <Symbol value=<DEFAULT> at 107619600> -> __default_4481419008
                __default_4481419008 = _DEFAULT_MARKER

                # <Value 'nothing' (10:33)> -> __cache_4481425776
                __token = 408
                try:
                    __zt_tmp = __attrs_4481423472
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4481425776 = _static_4417553984('path', 'nothing', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))

                # <BinOp left=<Value 'nothing' (10:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107619600> at 10b1d1f00> -> __condition
                __expression = __cache_4481425776

                # <Symbol value=<DEFAULT> at 107619600> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4481425776
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                if (__backup_disable_column_two_4477077488 is __marker):
                    del econtext['disable_column_two']
                else:
                    econtext['disable_column_two'] = __backup_disable_column_two_4477077488
                if (__backup_disable_column_one_4476352880 is __marker):
                    del econtext['disable_column_one']
                else:
                    econtext['disable_column_one'] = __backup_disable_column_one_4476352880
                if (__backup_dummy_4477229360 is __marker):
                    del econtext['dummy']
                else:
                    econtext['dummy'] = __backup_dummy_4477229360
                __append('\n      ')
            _slots = econtext['__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4481422272
                __attrs_4481422272 = _static_4418309904
                __append('\n    ')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_4481428272
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4417553984('path', 'context/main_template/macros/master', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4481382528 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4481382528
            __i18n_domain = __previous_i18n_domain_4481427984
            __append('\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render': render, }