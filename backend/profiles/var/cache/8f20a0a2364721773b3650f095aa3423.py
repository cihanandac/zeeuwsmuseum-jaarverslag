# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/Products/CMFPlone/browser/login/templates/login.pt'

__tokens = {586: ('view/label | nothing', 18, 29), 1108: ('context/@@ploneform-macros/titlelessform', 31, 37), 1108: ('context/@@ploneform-macros/titlelessform', 31, 37), 1236: ('context/@@plone_portal_state', 34, 43), 1306: (' portal_state/portal_ur', 35, 40), 1520: ('string:${portal_url}/@@login-help', 38, 62), 1672: ('python:view.self_registration_enabled()', 40, 36), 1871: ('string:${portal_url}/@@register', 42, 60), 287: ('here/main_template/macros/master', 7, 23), 287: ('here/main_template/macros/master', 7, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4708203968 = 'master'
_static_4708522720 = {'href': '@@register', 'class': 'emph', }
_static_4708518784 = {'href': '@@login-help', }
_static_4708449584 = {'class': 'footer mt-4', }
_static_4708448000 = 'titlelessform'
_static_4708445984 = {'class': 'alert alert-danger pat-cookietrigger', 'style': 'display:none', }
_static_4708444160 = {'id': 'login-form', }
_static_4459175296 = __C2ZContextWrapper
_static_4459168576 = __compile_zt_expr
_static_4708443008 = {'class': 'card-title h5', }
_static_4708440944 = {'class': 'card-body', }
_static_4708439552 = {'class': 'card', }
_static_4708438496 = {'id': 'content', 'class': 'login-wrapper', }
_static_4459104240 = {}

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

    def render_main(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708436816
            __attrs_4708436816 = _static_4459104240
            __append('\n\n      ')

            # <Static value=<ast.Dict object at 0x118a511e0> name=None at 118a50e20> -> __attrs_4708438544
            __attrs_4708438544 = _static_4708438496

            # <article ... (0:0)
            # --------------------------------------------------------
            __append('<article id="content" class="login-wrapper">\n\n        ')

            # <Static value=<ast.Dict object at 0x118a51600> name=None at 118a51630> -> __attrs_4708439936
            __attrs_4708439936 = _static_4708439552

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card">\n          ')

            # <Static value=<ast.Dict object at 0x118a51b70> name=None at 118a51ba0> -> __attrs_4708441328
            __attrs_4708441328 = _static_4708440944

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card-body">\n            ')

            # <Static value=<ast.Dict object at 0x118a52380> name=None at 118a523b0> -> __attrs_4708443392
            __attrs_4708443392 = _static_4708443008

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1 class="card-title h5">')

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708442432
            __default_4708442432 = _DEFAULT_MARKER

            # <Value 'view/label | nothing' (18:29)> -> __cache_4708441952
            __token = 586
            try:
                __zt_tmp = __attrs_4708443392
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4708441952 = _static_4459168576('path', 'view/label | nothing', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/label | nothing' (18:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118a52020> -> __condition
            __expression = __cache_4708441952

            # <Symbol value=<DEFAULT> at 109c89f90> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4708441952
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</h1>\n\n            ')

            # <Static value=<ast.Dict object at 0x118a52800> name=None at 118a52830> -> __attrs_4708444544
            __attrs_4708444544 = _static_4708444160

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="login-form">\n\n              ')

            # <Static value=<ast.Dict object at 0x118a52f20> name=None at 118a52f50> -> __attrs_4708446176
            __attrs_4708446176 = _static_4708445984

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="alert alert-danger pat-cookietrigger" style="display:none">\n                ')

            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708447280
            __attrs_4708447280 = _static_4459104240

            # <strong ... (0:0)
            # --------------------------------------------------------
            __append('<strong>')
            __stream_4708446800 = []
            __append_4708446800 = __stream_4708446800.append
            __append_4708446800('\n                  Error\n                ')
            __msgid_4708446800 = __re_whitespace(''.join(__stream_4708446800)).strip()
            if __msgid_4708446800:
                __append(translate(__msgid_4708446800, mapping=None, default=__msgid_4708446800, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</strong>\n                ')

            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708448240
            __attrs_4708448240 = _static_4459104240
            __stream_4708447856 = []
            __append_4708447856 = __stream_4708447856.append
            __append_4708447856('\n                  Cookies are not enabled. You must enable cookies before you can log in.\n                ')
            __msgid_4708447856 = __re_whitespace(''.join(__stream_4708447856)).strip()
            if 'enable_cookies_message_before_login':
                __append(translate('enable_cookies_message_before_login', mapping=None, default=__msgid_4708447856, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n              </div>\n              ')

            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708448816
            __attrs_4708448816 = _static_4459104240
            __backup_macroname_4556161344 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x118a53700> name=None at 118a53850> -> __value
            __value = _static_4708448000
            econtext['macroname'] = __value

            # <Value 'context/@@ploneform-macros/titlelessform' (31:37)> -> __macro
            __token = 1108
            try:
                __zt_tmp = __attrs_4708448816
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4459168576('path', 'context/@@ploneform-macros/titlelessform', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __token = 1108
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4556161344 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4556161344
            __append('\n\n              ')

            # <Static value=<ast.Dict object at 0x118a53d30> name=None at 118a53d60> -> __attrs_4708449968
            __attrs_4708449968 = _static_4708449584
            __backup_portal_state_4708440272 = get('portal_state', __marker)

            # <Value 'context/@@plone_portal_state' (34:43)> -> __value
            __token = 1236
            try:
                __zt_tmp = __attrs_4708449968
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'context/@@plone_portal_state', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['portal_state'] = __value
            __backup_portal_url_4708441664 = get('portal_url', __marker)

            # <Value 'portal_state/portal_url' (35:40)> -> __value
            __token = 1306
            try:
                __zt_tmp = __attrs_4708449968
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'portal_state/portal_url', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['portal_url'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="footer mt-4">\n                ')

            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708516960
            __attrs_4708516960 = _static_4459104240

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div>\n                  ')

            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708517968
            __attrs_4708517968 = _static_4459104240
            __stream_4708517584 = []
            __append_4708517584 = __stream_4708517584.append
            __append_4708517584('Trouble logging in?')
            __msgid_4708517584 = __re_whitespace(''.join(__stream_4708517584)).strip()
            if 'trouble_logging_in':
                __append(translate('trouble_logging_in', mapping=None, default=__msgid_4708517584, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n                  ')

            # <Static value=<ast.Dict object at 0x118a64b80> name=None at 118a64bb0> -> __attrs_4708519456
            __attrs_4708519456 = _static_4708518784

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708518928
            __default_4708518928 = _DEFAULT_MARKER

            # <Substitution 'string:${portal_url}/@@login-help' (38:62)> -> __attr_href
            __token = 1520
            try:
                __zt_tmp = __attrs_4708519456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4459168576('string', '${portal_url}/@@login-help', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', '@@login-help', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append('>')
            __stream_4708517728 = []
            __append_4708517728 = __stream_4708517728.append
            __append_4708517728('Get help')
            __msgid_4708517728 = __re_whitespace(''.join(__stream_4708517728)).strip()
            if 'footer_login_link_get_help':
                __append(translate('footer_login_link_get_help', mapping=None, default=__msgid_4708517728, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>.\n                </div>\n                ')

            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708520224
            __attrs_4708520224 = _static_4459104240

            # <Value 'python:view.self_registration_enabled()' (40:36)> -> __condition
            __token = 1672
            try:
                __zt_tmp = __attrs_4708520224
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4459168576('python', 'view.self_registration_enabled()', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n                  ')

                # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708521376
                __attrs_4708521376 = _static_4459104240
                __stream_4708520992 = []
                __append_4708520992 = __stream_4708520992.append
                __append_4708520992('Need an account?')
                __msgid_4708520992 = __re_whitespace(''.join(__stream_4708520992)).strip()
                if 'need_an_account':
                    __append(translate('need_an_account', mapping=None, default=__msgid_4708520992, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n                  ')

                # <Static value=<ast.Dict object at 0x118a65ae0> name=None at 118a657b0> -> __attrs_4708523008
                __attrs_4708523008 = _static_4708522720

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708522384
                __default_4708522384 = _DEFAULT_MARKER

                # <Substitution 'string:${portal_url}/@@register' (42:60)> -> __attr_href
                __token = 1871
                try:
                    __zt_tmp = __attrs_4708523008
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4459168576('string', '${portal_url}/@@register', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '@@register', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' class="emph">')
                __stream_4708521136 = []
                __append_4708521136 = __stream_4708521136.append
                __append_4708521136('Sign up here')
                __msgid_4708521136 = __re_whitespace(''.join(__stream_4708521136)).strip()
                if 'footer_login_link_signup':
                    __append(translate('footer_login_link_signup', mapping=None, default=__msgid_4708521136, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</a>.\n                </div>')
            __append('\n              </div>')
            if (__backup_portal_url_4708441664 is __marker):
                del econtext['portal_url']
            else:
                econtext['portal_url'] = __backup_portal_url_4708441664
            if (__backup_portal_state_4708440272 is __marker):
                del econtext['portal_state']
            else:
                econtext['portal_state'] = __backup_portal_state_4708440272
            __append('\n\n            </div>\n\n          </div>\n        </div>\n\n      </article>\n\n    ')
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

            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708204304
            __attrs_4708204304 = _static_4459104240
            __previous_i18n_domain_4708204448 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4491700800 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x118a17dc0> name=None at 118a17df0> -> __value
            __value = _static_4708203968
            econtext['macroname'] = __value

            def __fill_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708435808
                __attrs_4708435808 = _static_4459104240
                __append('\n    ')
                __token = None
                render_main(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n  ')
            _slots = econtext['__slot_main'] = _deque((__fill_main, ))

            # <Value 'here/main_template/macros/master' (7:23)> -> __macro
            __token = 287
            try:
                __zt_tmp = __attrs_4708204304
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4459168576('path', 'here/main_template/macros/master', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __token = 287
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4491700800 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4491700800
            __i18n_domain = __previous_i18n_domain_4708204448
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_main': render_main, 'render': render, }