# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/viewlets/keywords.pt'

__tokens = {74: ('context/Subject|nothing', 1, 74), 108: (' nocall:modules/Products.PythonScripts.standard/url_quot', 1, 108), 182: ('categories', 1, 182), 402: ('categories', 9, 37), 513: ('python:url_quote(category)', 11, 28), 568: ('string:${context/@@plone_portal_state/navigation_root_url}/@@search?Subject%3Alist=${quotedCat}', 12, 27), 691: ('category', 13, 25)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4975255584 = {'href': '#', 'rel': 'nofollow', 'class': 'btn btn-sm btn-outline-primary', }
_static_4753720080 = {}
_static_4975255344 = {'class': 'card-title section-heading d-none', }
_static_4981584608 = {'class': 'viewlet keywords-viewlet', }
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4975268560 = {'id': 'section-category', }

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

            # <Static value=<ast.Dict object at 0x1288c92d0> name=None at 1288c95a0> -> __attrs_4975267840
            __attrs_4975267840 = _static_4975268560
            __backup_categories_4981901392 = get('categories', __marker)

            # <Value 'context/Subject|nothing' (1:74)> -> __value
            __token = 74
            try:
                __zt_tmp = __attrs_4975267840
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'context/Subject|nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['categories'] = __value
            __backup_url_quote_4974679984 = get('url_quote', __marker)

            # <Value 'nocall:modules/Products.PythonScripts.standard/url_quote' (1:108)> -> __value
            __token = 108
            try:
                __zt_tmp = __attrs_4975267840
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('nocall', 'modules/Products.PythonScripts.standard/url_quote', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['url_quote'] = __value

            # <Value 'categories' (1:182)> -> __condition
            __token = 182
            try:
                __zt_tmp = __attrs_4975267840
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('path', 'categories', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4981580336 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-category">\n\n  ')

                # <Static value=<ast.Dict object at 0x128ecf2e0> name=None at 107f67790> -> __attrs_4975261344
                __attrs_4975261344 = _static_4981584608

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="viewlet keywords-viewlet">\n\n    ')

                # <Static value=<ast.Dict object at 0x1288c5f30> name=None at 1288c4070> -> __attrs_4975254720
                __attrs_4975254720 = _static_4975255344

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="card-title section-heading d-none">')
                __stream_4975259760 = []
                __append_4975259760 = __stream_4975259760.append
                __append_4975259760('\n      Keywords\n    ')
                __msgid_4975259760 = __re_whitespace(''.join(__stream_4975259760)).strip()
                if 'section_keywords_heading':
                    __append(translate('section_keywords_heading', mapping=None, default=__msgid_4975259760, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n\n    ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975251888
                __attrs_4975251888 = _static_4753720080
                __backup_category_4975309056 = get('category', __marker)

                # <Value 'categories' (9:37)> -> __iterator
                __token = 402
                try:
                    __zt_tmp = __attrs_4975251888
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4754050160('path', 'categories', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                (__iterator, ____index_4975250640, ) = getname('repeat')('category', __iterator)
                econtext['category'] = None
                for __item in __iterator:
                    econtext['category'] = __item
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x1288c6020> name=None at 1288c4d60> -> __attrs_4975248384
                    __attrs_4975248384 = _static_4975255584
                    __backup_quotedCat_4974678256 = get('quotedCat', __marker)

                    # <Value 'python:url_quote(category)' (11:28)> -> __value
                    __token = 513
                    try:
                        __zt_tmp = __attrs_4975248384
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('python', 'url_quote(category)', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['quotedCat'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975258752
                    __default_4975258752 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/@@plone_portal_state/navigation_root_url}/@@search?Subject%3Alist=${quotedCat}' (12:27)> -> __attr_href
                    __token = 568
                    try:
                        __zt_tmp = __attrs_4975248384
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4754050160('string', '${context/@@plone_portal_state/navigation_root_url}/@@search?Subject%3Alist=${quotedCat}', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' rel="nofollow" class="btn btn-sm btn-outline-primary">\n      ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975254768
                    __attrs_4975254768 = _static_4753720080

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975250976
                    __default_4975250976 = _DEFAULT_MARKER

                    # <Value 'category' (13:25)> -> __cache_4975256448
                    __token = 691
                    try:
                        __zt_tmp = __attrs_4975254768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4975256448 = _static_4754050160('path', 'category', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'category' (13:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 1288c5a20> -> __condition
                    __expression = __cache_4975256448

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4975256448
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n    </a>')
                    if (__backup_quotedCat_4974678256 is __marker):
                        del econtext['quotedCat']
                    else:
                        econtext['quotedCat'] = __backup_quotedCat_4974678256
                    __append('\n    ')
                    ____index_4975250640 -= 1
                    if (____index_4975250640 > 0):
                        __append('')
                if (__backup_category_4975309056 is __marker):
                    del econtext['category']
                else:
                    econtext['category'] = __backup_category_4975309056
                __append('\n\n  </div>\n\n</section>')
                __i18n_domain = __previous_i18n_domain_4981580336
            if (__backup_url_quote_4974679984 is __marker):
                del econtext['url_quote']
            else:
                econtext['url_quote'] = __backup_url_quote_4974679984
            if (__backup_categories_4981901392 is __marker):
                del econtext['categories']
            else:
                econtext['categories'] = __backup_categories_4981901392
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }