# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/Products/CMFPlone/browser/templates/footer.pt'

__tokens = {860: ('nocall:modules/DateTime.DateTime', 20, 30), 921: (' python:DateTime(', 21, 27), 963: ('python:myTime.year()', 22, 22)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4975071808 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'xml:lang': 'en', 'lang': 'en', }
_static_4982345872 = {'href': 'http://creativecommons.org/licenses/GPL/2.0/', }
_static_4975171792 = {'href': 'http://plone.org/foundation', }
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4975173520 = {'title': 'Copyright', }
_static_4975179856 = {'href': 'http://plone.org', }
_static_4753720080 = {}
_static_4975179280 = {'class': 'card-body', }
_static_4975074016 = {'class': 'card card-classic', 'id': 'portal-footer-signature', }

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

    def render_portlet(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x128899ae0> name=None at 12889a110> -> __attrs_4975174576
            __attrs_4975174576 = _static_4975074016

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card card-classic" id="portal-footer-signature">\n\n    ')

            # <Static value=<ast.Dict object at 0x1288b3610> name=None at 1288b2290> -> __attrs_4975177024
            __attrs_4975177024 = _static_4975179280

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card-body">\n      ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975169200
            __attrs_4975169200 = _static_4753720080
            __stream_4982819968_plonefoundation = ''
            __stream_4982819968_plonecms = ''
            __stream_4982819968_copyright = ''
            __stream_4982819968_current_year = ''
            __stream_4975172704 = []
            __append_4975172704 = __stream_4975172704.append
            __append_4975172704('\n      The\n      ')
            __stream_4982819968_plonecms = []
            __append_4982819968_plonecms = __stream_4982819968_plonecms.append

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975177888
            __attrs_4975177888 = _static_4753720080
            __append_4982819968_plonecms('\n           ')

            # <Static value=<ast.Dict object at 0x1288b3850> name=None at 1288b1de0> -> __attrs_4975170256
            __attrs_4975170256 = _static_4975179856

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_4982819968_plonecms('<a href="http://plone.org">')
            __stream_4975176304 = []
            __append_4975176304 = __stream_4975176304.append
            __append_4975176304('Plone')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975168336
            __attrs_4975168336 = _static_4753720080

            # <sup ... (0:0)
            # --------------------------------------------------------
            __append_4975176304('<sup>&reg;</sup> Open Source CMS/WCM')
            __msgid_4975176304 = __re_whitespace(''.join(__stream_4975176304)).strip()
            if 'label_plone_cms':
                __append_4982819968_plonecms(translate('label_plone_cms', mapping=None, default=__msgid_4975176304, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_4982819968_plonecms('</a>\n      ')
            __append_4975172704('${plonecms}')
            __stream_4982819968_plonecms = ''.join(__stream_4982819968_plonecms)
            __append_4975172704('\n      is\n      ')
            __stream_4982819968_copyright = []
            __append_4982819968_copyright = __stream_4982819968_copyright.append

            # <Static value=<ast.Dict object at 0x1288b1f90> name=None at 1288b1060> -> __attrs_4975168624
            __attrs_4975168624 = _static_4975173520

            # <abbr ... (0:0)
            # --------------------------------------------------------
            __append_4982819968_copyright('<abbr')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975176736
            __default_4975176736 = _DEFAULT_MARKER

            # <Translate msgid='title_copyright' node=<ast.Constant object at 0x1288b1960> at 1288b37c0> -> __attr_title
            __attr_title = 'Copyright'
            __attr_title = translate('title_copyright', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append_4982819968_copyright((' title="%s"' % __attr_title))
            __append_4982819968_copyright('>&copy;</abbr>')
            __append_4975172704('${copyright}')
            __stream_4982819968_copyright = ''.join(__stream_4982819968_copyright)
            __append_4975172704('\n      2000-')
            __stream_4982819968_current_year = []
            __append_4982819968_current_year = __stream_4982819968_current_year.append

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975166320
            __attrs_4975166320 = _static_4753720080
            __backup_DateTime_4981795344 = get('DateTime', __marker)

            # <Value 'nocall:modules/DateTime.DateTime' (20:30)> -> __value
            __token = 860
            try:
                __zt_tmp = __attrs_4975166320
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('nocall', 'modules/DateTime.DateTime', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['DateTime'] = __value
            __backup_myTime_4982393104 = get('myTime', __marker)

            # <Value 'python:DateTime()' (21:27)> -> __value
            __token = 921
            try:
                __zt_tmp = __attrs_4975166320
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', 'DateTime()', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['myTime'] = __value

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975170784
            __default_4975170784 = _DEFAULT_MARKER

            # <Value 'python:myTime.year()' (22:22)> -> __cache_4975170688
            __token = 963
            try:
                __zt_tmp = __attrs_4975166320
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4975170688 = _static_4754050160('python', 'myTime.year()', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

            # <BinOp left=<Value 'python:myTime.year()' (22:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 1288b2530> -> __condition
            __expression = __cache_4975170688

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4975170688
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append_4982819968_current_year(__content)
            if (__backup_myTime_4982393104 is __marker):
                del econtext['myTime']
            else:
                econtext['myTime'] = __backup_myTime_4982393104
            if (__backup_DateTime_4981795344 is __marker):
                del econtext['DateTime']
            else:
                econtext['DateTime'] = __backup_DateTime_4981795344
            __append_4975172704('${current_year}')
            __stream_4982819968_current_year = ''.join(__stream_4982819968_current_year)
            __append_4975172704('\n      by the\n      ')
            __stream_4982819968_plonefoundation = []
            __append_4982819968_plonefoundation = __stream_4982819968_plonefoundation.append

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975179664
            __attrs_4975179664 = _static_4753720080
            __append_4982819968_plonefoundation('\n           ')

            # <Static value=<ast.Dict object at 0x1288b18d0> name=None at 1288b3f70> -> __attrs_4982356960
            __attrs_4982356960 = _static_4975171792

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_4982819968_plonefoundation('<a href="http://plone.org/foundation">')
            __stream_4975176496 = []
            __append_4975176496 = __stream_4975176496.append
            __append_4975176496('Plone Foundation')
            __msgid_4975176496 = __re_whitespace(''.join(__stream_4975176496)).strip()
            if 'label_plone_foundation':
                __append_4982819968_plonefoundation(translate('label_plone_foundation', mapping=None, default=__msgid_4975176496, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_4982819968_plonefoundation('</a>')
            __append_4975172704('${plonefoundation}')
            __stream_4982819968_plonefoundation = ''.join(__stream_4982819968_plonefoundation)
            __append_4975172704('\n      and friends.\n      ')
            __msgid_4975172704 = __re_whitespace(''.join(__stream_4975172704)).strip()
            if 'description_copyright':
                __append(translate('description_copyright', mapping={'current_year': __stream_4982819968_current_year, 'copyright': __stream_4982819968_copyright, 'plonecms': __stream_4982819968_plonecms, 'plonefoundation': __stream_4982819968_plonefoundation, }, default=__msgid_4975172704, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n\n      ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975174816
            __attrs_4975174816 = _static_4753720080
            __stream_4982819744_license = ''
            __stream_4975170736 = []
            __append_4975170736 = __stream_4975170736.append
            __append_4975170736('\n      Distributed under the\n           ')
            __stream_4982819744_license = []
            __append_4982819744_license = __stream_4982819744_license.append

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982352112
            __attrs_4982352112 = _static_4753720080
            __append_4982819744_license('\n                ')

            # <Static value=<ast.Dict object at 0x128f89090> name=None at 128f8a560> -> __attrs_4982344240
            __attrs_4982344240 = _static_4982345872

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_4982819744_license('<a href="http://creativecommons.org/licenses/GPL/2.0/">')
            __stream_4982356336 = []
            __append_4982356336 = __stream_4982356336.append
            __append_4982356336('GNU GPL license')
            __msgid_4982356336 = __re_whitespace(''.join(__stream_4982356336)).strip()
            if 'label_gnu_gpl_licence':
                __append_4982819744_license(translate('label_gnu_gpl_licence', mapping=None, default=__msgid_4982356336, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_4982819744_license('</a>')
            __append_4975170736('${license}')
            __stream_4982819744_license = ''.join(__stream_4982819744_license)
            __append_4975170736('.\n      ')
            __msgid_4975170736 = __re_whitespace(''.join(__stream_4975170736)).strip()
            if 'description_license':
                __append(translate('description_license', mapping={'license': __stream_4982819744_license, }, default=__msgid_4975170736, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n    </div>\n\n  </div>')
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

            # <Static value=<ast.Dict object at 0x128899240> name=None at 12889b490> -> __attrs_4975081456
            __attrs_4975081456 = _static_4975071808
            __previous_i18n_domain_4975081936 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n\n  ')
            __token = None
            render_portlet(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n')
            __i18n_domain = __previous_i18n_domain_4975081936
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_portlet': render_portlet, 'render': render, }