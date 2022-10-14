# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/Products/CMFPlone/browser/templates/basic_error_message.pt'

__tokens = {293: ('python:view.is_manager()', 8, 27), 352: ('not:isManager', 11, 24), 423: ('isManager', 12, 24), 434: ('${options/error_type}', 12, 35), 436: ('options/error_type', 12, 37), 694: ('isManager', 23, 21), 705: ('${options/error_type}', 23, 32), 707: ('options/error_type', 23, 34), 755: ('isManager', 25, 22), 786: ('options/error_tb', 26, 20), 834: ('not:isManager', 28, 26)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_5109099168 = {'class': 'documentFirstHeading', }
_static_5109100416 = {'class': 'documentFirstHeading', }
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
_static_4428767312 = {}
_static_5108951184 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'xml:lang': 'en', 'lang': 'en', }

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

            # <Static value=<ast.Dict object at 0x130846890> name=None at 130845330> -> __attrs_5108956896
            __attrs_5108956896 = _static_5108951184
            __previous_i18n_domain_5108950992 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n\n')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5108953872
            __attrs_5108953872 = _static_4428767312
            __backup_isManager_4960597568 = get('isManager', __marker)

            # <Value 'python:view.is_manager()' (8:27)> -> __value
            __token = 293
            try:
                __zt_tmp = __attrs_5108953872
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', 'view.is_manager()', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['isManager'] = __value
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5108953632
            __attrs_5108953632 = _static_4428767312

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n  ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109103632
            __attrs_5109103632 = _static_4428767312

            # <Value 'not:isManager' (11:24)> -> __condition
            __token = 352
            try:
                __zt_tmp = __attrs_5109103632
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('not', 'isManager', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <title ... (0:0)
                # --------------------------------------------------------
                __append('<title>')
                __stream_5109104112 = []
                __append_5109104112 = __stream_5109104112.append
                __append_5109104112('Error')
                __msgid_5109104112 = __re_whitespace(''.join(__stream_5109104112)).strip()
                if __msgid_5109104112:
                    __append(translate(__msgid_5109104112, mapping=None, default=__msgid_5109104112, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</title>')
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109102576
            __attrs_5109102576 = _static_4428767312

            # <Value 'isManager' (12:24)> -> __condition
            __token = 423
            try:
                __zt_tmp = __attrs_5109102576
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'isManager', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <title ... (0:0)
                # --------------------------------------------------------
                __append('<title>')

                # <Interpolation value=<Substitution '${options/error_type}' (12:35)> braces_required=True translation=False default='"?"' default_marker='"?"' at 13086b5e0> -> __content_4353737008
                __token = 434
                __token = 436
                try:
                    __zt_tmp = __attrs_5109102576
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_4353737008 = _static_4427992992('path', 'options/error_type', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __content_4353737008 = __quote(__content_4353737008, '\x00', '&#0;', None, None)
                __content_4353737008 = __content_4353737008
                if (__content_4353737008 is None):
                    pass
                else:
                    if (__content_4353737008 is None):
                        __content_4353737008 = None
                    else:
                        __tt = type(__content_4353737008)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_4353737008 = str(__content_4353737008)
                        else:
                            if (__tt is bytes):
                                __content_4353737008 = decode(__content_4353737008)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_4353737008 = __content_4353737008.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_4353737008)
                                        __content_4353737008 = (str(__content_4353737008) if (__content_4353737008 is __converted) else __converted)
                                    else:
                                        __content_4353737008 = __content_4353737008()
                if (__content_4353737008 is not None):
                    __append(__content_4353737008)
                __append('</title>')
            __append('\n</head>\n\n')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109101520
            __attrs_5109101520 = _static_4428767312

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n\n  ')

            # <Static value=<ast.Dict object at 0x13086af80> name=None at 13086b100> -> __attrs_5109100080
            __attrs_5109100080 = _static_5109100416

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1 class="documentFirstHeading">')
            __stream_5109100944 = []
            __append_5109100944 = __stream_5109100944.append
            __append_5109100944('\n      We&#8217;re sorry, but there seems to be an error&hellip;\n  ')
            __msgid_5109100944 = __re_whitespace(''.join(__stream_5109100944)).strip()
            if 'heading_site_error_sorry':
                __append(translate('heading_site_error_sorry', mapping=None, default=__msgid_5109100944, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h1>\n\n  ')

            # <Static value=<ast.Dict object at 0x13086aaa0> name=None at 13086ac20> -> __attrs_5109098832
            __attrs_5109098832 = _static_5109099168

            # <Value 'isManager' (23:21)> -> __condition
            __token = 694
            try:
                __zt_tmp = __attrs_5109098832
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'isManager', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2 class="documentFirstHeading">')

                # <Interpolation value=<Substitution '${options/error_type}' (23:32)> braces_required=True translation=False default='"?"' default_marker='"?"' at 13086a740> -> __content_4353737008
                __token = 705
                __token = 707
                try:
                    __zt_tmp = __attrs_5109098832
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_4353737008 = _static_4427992992('path', 'options/error_type', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __content_4353737008 = __quote(__content_4353737008, '\x00', '&#0;', None, None)
                __content_4353737008 = __content_4353737008
                if (__content_4353737008 is None):
                    pass
                else:
                    if (__content_4353737008 is None):
                        __content_4353737008 = None
                    else:
                        __tt = type(__content_4353737008)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_4353737008 = str(__content_4353737008)
                        else:
                            if (__tt is bytes):
                                __content_4353737008 = decode(__content_4353737008)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_4353737008 = __content_4353737008.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_4353737008)
                                        __content_4353737008 = (str(__content_4353737008) if (__content_4353737008 is __converted) else __converted)
                                    else:
                                        __content_4353737008 = __content_4353737008()
                if (__content_4353737008 is not None):
                    __append(__content_4353737008)
                __append('</h2>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109097008
            __attrs_5109097008 = _static_4428767312

            # <Value 'isManager' (25:22)> -> __condition
            __token = 755
            try:
                __zt_tmp = __attrs_5109097008
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'isManager', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <pre ... (0:0)
                # --------------------------------------------------------
                __append('<pre>')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109097584
                __default_5109097584 = _DEFAULT_MARKER

                # <Value 'options/error_tb' (26:20)> -> __cache_5109098064
                __token = 786
                try:
                    __zt_tmp = __attrs_5109097008
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_5109098064 = _static_4427992992('path', 'options/error_tb', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'options/error_tb' (26:20)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 13086a590> -> __condition
                __expression = __cache_5109098064

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_5109098064
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</pre>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109096144
            __attrs_5109096144 = _static_4428767312

            # <Value 'not:isManager' (28:26)> -> __condition
            __token = 834
            try:
                __zt_tmp = __attrs_5109096144
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('not', 'isManager', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109094896
                __attrs_5109094896 = _static_4428767312

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p>')
                __stream_4938163008_site_admin = ''
                __stream_5109095376 = []
                __append_5109095376 = __stream_5109095376.append
                __append_5109095376('\n      If you are certain you have the correct web address but are encountering an error, please\n      contact the ')
                __stream_4938163008_site_admin = []
                __append_4938163008_site_admin = __stream_4938163008_site_admin.append

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109093840
                __attrs_5109093840 = _static_4428767312

                # <span ... (0:0)
                # --------------------------------------------------------
                __append_4938163008_site_admin('<span>')
                __stream_5109094320 = []
                __append_5109094320 = __stream_5109094320.append
                __append_5109094320('site administration')
                __msgid_5109094320 = __re_whitespace(''.join(__stream_5109094320)).strip()
                if 'label_site_admin':
                    __append_4938163008_site_admin(translate('label_site_admin', mapping=None, default=__msgid_5109094320, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append_4938163008_site_admin('</span>')
                __append_5109095376('${site_admin}')
                __stream_4938163008_site_admin = ''.join(__stream_4938163008_site_admin)
                __append_5109095376('.\n      ')
                __msgid_5109095376 = __re_whitespace(''.join(__stream_5109095376)).strip()
                if 'description_site_error_mail_site_admin':
                    __append(translate('description_site_error_mail_site_admin', mapping={'site_admin': __stream_4938163008_site_admin, }, default=__msgid_5109095376, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n  ')
            __append('\n\n</body>\n')
            if (__backup_isManager_4960597568 is __marker):
                del econtext['isManager']
            else:
                econtext['isManager'] = __backup_isManager_4960597568
            __append('\n</html>')
            __i18n_domain = __previous_i18n_domain_5108950992
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }