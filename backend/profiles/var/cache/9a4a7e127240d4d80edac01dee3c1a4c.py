# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/viewlets/searchbox.pt'

__tokens = {128: ('view/navigation_root_url', 3, 34), 369: ('string:${navigation_root_url}/@@search', 9, 27), 239: ("d-flex ${python: view.livesearch and 'pat-livesearch'} ${python: view.show_images and 'show_images'}", 8, 11), 248: ("python: view.livesearch and 'pat-livesearch'", 8, 20), 296: ("python: view.show_images and 'show_images'", 8, 68), 448: (' string:ajaxUrl:${navigation_root_url}/@@ajax-searc', 10, 39), 916: ('request/form/SearchableText|nothing', 25, 28), 1263: ('string:${navigation_root_url}/@@search', 37, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4977857088 = {'href': '#', }
_static_4977868128 = {'id': 'portal-advanced-search', 'class': 'hiddenStructure', }
_static_4977854208 = {'class': 'searchButton btn btn-outline-light', 'type': 'submit', }
_static_4977856416 = {'name': 'SearchableText', 'type': 'text', 'size': '18', 'value': '', 'id': 'searchGadget', 'title': 'Search Site', 'placeholder': 'Search Site', 'class': 'searchField form-control me-2', }
_static_4977857904 = {'class': 'hiddenStructure', 'for': 'searchGadget', }
_static_4975078000 = {'id': 'searchGadget_form', 'action': '@@search', 'role': 'search', 'class': "d-flex ${python: view.livesearch and 'pat-livesearch'} ${python: view.show_images and 'show_images'} ", 'data-pat-livesearch': 'string:ajaxUrl:${navigation_root_url}/@@ajax-search', }
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4975072000 = {'id': 'portal-searchbox', 'class': 'd-flex flex-column position-relative', }

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

            # <Static value=<ast.Dict object at 0x128899300> name=None at 12889bc40> -> __attrs_4975075696
            __attrs_4975075696 = _static_4975072000
            __backup_navigation_root_url_4975064160 = get('navigation_root_url', __marker)

            # <Value 'view/navigation_root_url' (3:34)> -> __value
            __token = 128
            try:
                __zt_tmp = __attrs_4975075696
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/navigation_root_url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['navigation_root_url'] = __value
            __previous_i18n_domain_4975083472 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="portal-searchbox" class="d-flex flex-column position-relative">\n\n  ')

            # <Static value=<ast.Dict object at 0x12889aa70> name=None at 12889ab00> -> __attrs_4977866496
            __attrs_4977866496 = _static_4975078000

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form id="searchGadget_form"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975081264
            __default_4975081264 = _DEFAULT_MARKER

            # <Substitution 'string:${navigation_root_url}/@@search' (9:27)> -> __attr_action
            __token = 369
            try:
                __zt_tmp = __attrs_4977866496
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_4754050160('string', '${navigation_root_url}/@@search', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', '@@search', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append(' role="search"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975080736
            __default_4975080736 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "d-flex ${python: view.livesearch and 'pat-livesearch'} ${python: view.show_images and 'show_images'} " (8:11)> braces_required=True translation=False default='"?"' default_marker='"?"' at 12889a0b0> -> __attr_class
            __token = 239
            __token = 248
            try:
                __zt_tmp = __attrs_4977866496
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4754050160('python', " view.livesearch and 'pat-livesearch'", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 296
            try:
                __zt_tmp = __attrs_4977866496
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class_294 = _static_4754050160('python', " view.show_images and 'show_images'", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_class_294 = __quote(__attr_class_294, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_class = ('%s%s%s%s%s' % ('d-flex ', (__attr_class if (__attr_class is not None) else ''), ' ', (__attr_class_294 if (__attr_class_294 is not None) else ''), ' ', ))
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

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4974660432
            __default_4974660432 = _DEFAULT_MARKER

            # <Substitution 'string:ajaxUrl:${navigation_root_url}/@@ajax-search' (10:39)> -> __attr_data_pat_livesearch
            __token = 448
            try:
                __zt_tmp = __attrs_4977866496
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_pat_livesearch = _static_4754050160('string', 'ajaxUrl:${navigation_root_url}/@@ajax-search', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_data_pat_livesearch = __quote(__attr_data_pat_livesearch, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_pat_livesearch is not None):
                __append((' data-pat-livesearch="%s"' % __attr_data_pat_livesearch))
            __append('>\n\n    ')

            # <Static value=<ast.Dict object at 0x128b41570> name=None at 128b43130> -> __attrs_4977864240
            __attrs_4977864240 = _static_4977857904

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="hiddenStructure" for="searchGadget">')
            __stream_4977863952 = []
            __append_4977863952 = __stream_4977863952.append
            __append_4977863952('Search Site')
            __msgid_4977863952 = __re_whitespace(''.join(__stream_4977863952)).strip()
            if 'text_search':
                __append(translate('text_search', mapping=None, default=__msgid_4977863952, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n\n    ')

            # <Static value=<ast.Dict object at 0x128b40fa0> name=None at 128b423e0> -> __attrs_4977866304
            __attrs_4977866304 = _static_4977856416

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input name="SearchableText" type="text" size="18"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4977858336
            __default_4977858336 = _DEFAULT_MARKER

            # <Substitution 'request/form/SearchableText|nothing' (25:28)> -> __attr_value
            __token = 916
            try:
                __zt_tmp = __attrs_4977866304
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_4754050160('path', 'request/form/SearchableText|nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' id="searchGadget"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4977867312
            __default_4977867312 = _DEFAULT_MARKER

            # <Translate msgid='title_search_site' node=<ast.Constant object at 0x128b41d50> at 128b40880> -> __attr_title
            __attr_title = 'Search Site'
            __attr_title = translate('title_search_site', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4977863616
            __default_4977863616 = _DEFAULT_MARKER

            # <Translate msgid='title_search_site' node=<ast.Constant object at 0x128b43460> at 128b43100> -> __attr_placeholder
            __attr_placeholder = 'Search Site'
            __attr_placeholder = translate('title_search_site', default=__attr_placeholder, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_placeholder is not None):
                __append((' placeholder="%s"' % __attr_placeholder))
            __append(' class="searchField form-control me-2" />\n\n    ')

            # <Static value=<ast.Dict object at 0x128b40700> name=None at 128b41990> -> __attrs_4977863712
            __attrs_4977863712 = _static_4977854208

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button class="searchButton btn btn-outline-light" type="submit">')
            __stream_4977857424 = []
            __append_4977857424 = __stream_4977857424.append
            __append_4977857424('\n      Search\n    ')
            __msgid_4977857424 = __re_whitespace(''.join(__stream_4977857424)).strip()
            if 'label_search':
                __append(translate('label_search', mapping=None, default=__msgid_4977857424, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</button>\n\n    ')

            # <Static value=<ast.Dict object at 0x128b43d60> name=None at 128b43370> -> __attrs_4977865536
            __attrs_4977865536 = _static_4977868128

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="portal-advanced-search" class="hiddenStructure">\n      ')

            # <Static value=<ast.Dict object at 0x128b41240> name=None at 128b404c0> -> __attrs_4977861120
            __attrs_4977861120 = _static_4977857088

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4977858240
            __default_4977858240 = _DEFAULT_MARKER

            # <Substitution 'string:${navigation_root_url}/@@search' (37:31)> -> __attr_href
            __token = 1263
            try:
                __zt_tmp = __attrs_4977861120
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4754050160('string', '${navigation_root_url}/@@search', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append('>')
            __stream_4977855600 = []
            __append_4977855600 = __stream_4977855600.append
            __append_4977855600('\n          Advanced Search&hellip;\n      ')
            __msgid_4977855600 = __re_whitespace(''.join(__stream_4977855600)).strip()
            if 'label_advanced_search':
                __append(translate('label_advanced_search', mapping=None, default=__msgid_4977855600, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n    </div>\n\n  </form>\n\n</div>')
            __i18n_domain = __previous_i18n_domain_4975083472
            if (__backup_navigation_root_url_4975064160 is __marker):
                del econtext['navigation_root_url']
            else:
                econtext['navigation_root_url'] = __backup_navigation_root_url_4975064160
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }