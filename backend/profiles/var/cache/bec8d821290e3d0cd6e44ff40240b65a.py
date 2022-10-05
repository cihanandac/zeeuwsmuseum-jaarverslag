# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/Products/CMFPlone/browser/templates/plone-addsite.pt'

__tokens = {481: ('${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}', 12, 14), 483: ('string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css', 12, 16), 627: ('${string:${context/absolute_url}/++resource++plone-admin-ui.css}', 15, 14), 629: ('string:${context/absolute_url}/++resource++plone-admin-ui.css', 15, 16), 726: ('string:${context/absolute_url}/++resource++jstz-1.0.4.min.js', 16, 30), 831: ('string:${context/absolute_url}/++resource++plone-admin-ui.js', 18, 30), 1117: ('string:${context/absolute_url}/++resource++plone-logo.svg', 28, 35), 1405: ('view/profiles', 35, 25), 1449: (' profiles/bas', 36, 29), 1495: ('e profiles/defau', 37, 30), 1547: ('es profiles/extensi', 38, 32), 1592: ('ced request/advanced|not', 39, 21), 1332: ('string:${context/absolute_url}/@@plone-addsite', 34, 27), 2255: ('request/site_id|nothing', 55, 40), 3261: ('view/browser_language', 78, 49), 3333: (' python:view.grouped_languages(browser_language', 79, 49), 3426: ('grouped_languages', 80, 42), 3491: ('group/label', 81, 46), 3582: ('group/languages', 84, 41), 3645: ("python:lang['langcode']", 85, 46), 3718: (" python:lang['langcode'] == browser_languag", 86, 48), 3801: ("python: lang['label']", 87, 37), 4403: ('view/timezones', 108, 40), 4462: ('tz_list', 109, 42), 4517: ('group', 110, 46), 4576: ('python:tz_list[group]', 111, 51), 4621: ('tz/value', 111, 96), 4662: ('tz/label', 112, 31), 5112: ('advanced', 124, 30), 5742: ('not:advanced', 140, 32), 5897: ('python: len(base_profiles) > 1', 144, 30), 6069: ('base_profiles', 148, 36), 6388: (' info/i', 155, 43), 6336: ('info/id', 154, 41), 6442: ("d python: default_profile==info['id'] and 'checked' or nothi", 156, 44), 6577: ('info/id', 157, 68), 6586: ('${info/title}', 157, 77), 6588: ('info/title', 157, 79), 6660: ('info/description', 158, 52), 6678: ('${info/description}', 158, 70), 6680: ('info/description', 158, 72), 7046: ("python:[p for p in extension_profiles if p.get('selected', None)]", 170, 40), 7143: ('python: extension_profiles or advanced', 171, 30), 7212: ('python: has_selected and not advanced', 172, 29), 7286: ('python: advanced', 173, 34), 7692: ('extension_profiles', 183, 39), 7757: ('info/selected|nothing', 184, 44), 7824: ('python: not selected or advanced', 185, 43), 7943: ('python: advanced', 187, 37), 8090: ('${info/id}', 190, 33), 8092: ('info/id', 190, 35), 8132: ('${info/id}', 191, 30), 8134: ('info/id', 191, 32), 8245: ('info/selected|nothing', 193, 50), 8329: ('${info/id}', 194, 57), 8331: ('info/id', 194, 59), 8342: ('${info/title}', 194, 70), 8344: ('info/title', 194, 72), 8446: ("python: advanced and info['description']", 196, 39), 8511: ('${info/description}', 197, 22), 8513: ('info/description', 197, 24), 8656: ('python: selected and not advanced', 201, 43), 8812: ('${info/id}', 204, 31), 8814: ('info/id', 204, 33)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4778979728 = {'class': 'btn btn-success mt-3', 'type': 'submit', 'name': 'submit', }
_static_4831186080 = {'type': 'hidden', 'name': 'form.submitted:boolean', 'value': 'True', }
_static_4799908592 = {'class': 'col-md-12 mt-3', }
_static_4779178640 = {'type': 'hidden', 'name': 'extension_ids:list', 'value': '${info/id}', }
_static_4754251328 = {'class': 'form-text', }
_static_4777430560 = {'class': 'form-check-label', 'for': '${info/id}', }
_static_4776784608 = {'type': 'checkbox', 'name': 'extension_ids:list', 'value': '${info/id}', 'id': '${info/id}', 'class': 'form-check-input', 'checked': 'info/selected|nothing', }
_static_4772860624 = {'class': 'form-check mb-3', }
_static_4799911280 = {'class': 'lead', }
_static_4799912000 = {'class': 'col-md-12 mt-3', }
_static_4799919344 = {'class': 'form-text', }
_static_4799920496 = {'class': 'form-text', }
_static_4799918720 = {'class': 'form-check-label', 'for': 'info/id', }
_static_4974770064 = {'type': 'radio', 'name': 'profile_id:string', 'value': 'profile', 'class': 'form-check-input', 'id': 'info/id', 'checked': "python: default_profile==info['id'] and 'checked' or nothing", }
_static_4974770976 = {'class': 'form-check mb-3', }
_static_4974770448 = {'class': 'lead', }
_static_4974758400 = {'class': 'mb-3', }
_static_4974764880 = {'class': 'col-md-12', }
_static_4974765936 = {'type': 'hidden', 'name': 'setup_content:boolean', 'value': 'true', }
_static_4974764112 = {'class': 'form-text', }
_static_4974761712 = {'class': 'form-check-label', 'for': 'example-content', }
_static_4974759744 = {'class': 'form-check-input', 'id': 'example-content', 'type': 'checkbox', 'name': 'setup_content:boolean', 'checked': 'checked', }
_static_4773682032 = {'class': 'form-check', }
_static_4773677520 = {'class': 'col-md-12 mb-3', }
_static_4773677952 = {'class': 'form-text', }
_static_4773680256 = {'value': 'UTC', }
_static_4773686976 = {'label': 'group', }
_static_4773685104 = {'id': 'portal_timezone', 'name': 'portal_timezone', 'class': 'form-select', }
_static_4773690384 = {'for': 'portal_timezone', 'class': 'form-label', }
_static_4773690528 = {'class': 'col-md-12 mb-3 tzx', }
_static_4773683280 = {'class': 'form-text', }
_static_4773679392 = {'value': 'en', 'selected': "python:lang['langcode'] == browser_language", }
_static_4773973104 = {'label': 'group/label', }
_static_4773976560 = {'name': 'default_language', 'class': 'form-select', }
_static_4773973776 = {'for': 'default_language', 'class': 'form-label', }
_static_4773978144 = {'class': 'col-md-12 mb-3', }
_static_4773984960 = {'class': 'form-text', }
_static_4773984192 = {'type': 'text', 'name': 'title', 'size': '30', 'value': 'Site', 'class': 'form-control', }
_static_4773976896 = {'for': 'title', 'class': 'form-label', }
_static_4773981648 = {'class': 'col-md-12 mb-3', }
_static_4773977760 = {'class': 'form-text', }
_static_4362534144 = {'type': 'text', 'name': 'site_id', 'size': '20', 'id': 'site_id', 'class': 'form-control', 'value': 'request/site_id|nothing', }
_static_4698552112 = {'for': 'site_id', 'class': 'form-label', }
_static_4827965872 = {'class': 'col-md-12 mb-3 mb-3', }
_static_4827668752 = {'class': 'lead', }
_static_4803869088 = {'class': 'col-md-12', }
_static_4750793392 = {'class': 'row', }
_static_4974860352 = {'action': '#', 'method': 'post', }
_static_4974855168 = {'src': '/++resource++plone-logo.svg', 'width': '215', 'height': '56', 'alt': 'Plone logo', }
_static_4974855456 = {'class': 'row', }
_static_4974863424 = {'class': 'container admin mt-5 mb-5 p-4 ', }
_static_4974857232 = {'src': 'string:${context/absolute_url}/++resource++plone-admin-ui.js', }
_static_4974865920 = {'src': 'string:${context/absolute_url}/++resource++jstz-1.0.4.min.js', }
_static_4974866256 = {'rel': 'stylesheet', 'type': 'text/css', 'href': '${string:${context/absolute_url}/++resource++plone-admin-ui.css}', }
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4974868896 = {'rel': 'stylesheet', 'type': 'text/css', 'href': '${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}', }
_static_4974854880 = {'name': 'viewport', 'content': 'width=device-width, initial-scale=1', }
_static_4974706400 = {'charset': 'utf-8', }
_static_4753720080 = {}
_static_4974701360 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'xml:lang': 'en', 'lang': 'en', }

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
            __append('<!DOCTYPE html>\n')

            # <Static value=<ast.Dict object at 0x12883eb30> name=None at 12883ceb0> -> __attrs_4974700736
            __attrs_4974700736 = _static_4974701360
            __previous_i18n_domain_4974694496 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n\n')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4974704624
            __attrs_4974704624 = _static_4753720080

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n  ')

            # <Static value=<ast.Dict object at 0x12883fee0> name=None at 12883db40> -> __attrs_4974870240
            __attrs_4974870240 = _static_4974706400

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta charset="utf-8" />\n  ')

            # <Static value=<ast.Dict object at 0x1288642e0> name=None at 1288654e0> -> __attrs_4974854448
            __attrs_4974854448 = _static_4974854880

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta name="viewport" content="width=device-width, initial-scale=1" />\n  ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4974857472
            __attrs_4974857472 = _static_4753720080

            # <title ... (0:0)
            # --------------------------------------------------------
            __append('<title>')
            __stream_4974861936 = []
            __append_4974861936 = __stream_4974861936.append
            __append_4974861936('Create a Plone site')
            __msgid_4974861936 = __re_whitespace(''.join(__stream_4974861936)).strip()
            if __msgid_4974861936:
                __append(translate(__msgid_4974861936, mapping=None, default=__msgid_4974861936, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</title>\n  ')

            # <Static value=<ast.Dict object at 0x1288679a0> name=None at 1288676d0> -> __attrs_4974869424
            __attrs_4974869424 = _static_4974868896

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4974868272
            __default_4974868272 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}' (12:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 128867190> -> __attr_href
            __token = 481
            __token = 483
            try:
                __zt_tmp = __attrs_4974869424
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4754050160('string', '${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
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
            __append(' />\n  ')

            # <Static value=<ast.Dict object at 0x128866f50> name=None at 128866ce0> -> __attrs_4974864000
            __attrs_4974864000 = _static_4974866256

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4974866352
            __default_4974866352 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${string:${context/absolute_url}/++resource++plone-admin-ui.css}' (15:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 128867610> -> __attr_href
            __token = 627
            __token = 629
            try:
                __zt_tmp = __attrs_4974864000
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4754050160('string', '${context/absolute_url}/++resource++plone-admin-ui.css', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
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
            __append(' />\n  ')

            # <Static value=<ast.Dict object at 0x128866e00> name=None at 128866e60> -> __attrs_4974864720
            __attrs_4974864720 = _static_4974865920

            # <script ... (0:0)
            # --------------------------------------------------------
            __append('<script')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4974865152
            __default_4974865152 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/++resource++jstz-1.0.4.min.js' (16:30)> -> __attr_src
            __token = 726
            try:
                __zt_tmp = __attrs_4974864720
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_4754050160('string', '${context/absolute_url}/++resource++jstz-1.0.4.min.js', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((' src="%s"' % __attr_src))
            __append('>\n  </script>\n  ')

            # <Static value=<ast.Dict object at 0x128864c10> name=None at 128864190> -> __attrs_4974855888
            __attrs_4974855888 = _static_4974857232

            # <script ... (0:0)
            # --------------------------------------------------------
            __append('<script')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4974854736
            __default_4974854736 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/++resource++plone-admin-ui.js' (18:30)> -> __attr_src
            __token = 831
            try:
                __zt_tmp = __attrs_4974855888
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_4754050160('string', '${context/absolute_url}/++resource++plone-admin-ui.js', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((' src="%s"' % __attr_src))
            __append('>\n  </script>\n</head>\n\n')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4974862416
            __attrs_4974862416 = _static_4753720080

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n\n  ')

            # <Static value=<ast.Dict object at 0x128866440> name=None at 128866170> -> __attrs_4974855792
            __attrs_4974855792 = _static_4974863424

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="container admin mt-5 mb-5 p-4 ">\n    ')

            # <Static value=<ast.Dict object at 0x128864520> name=None at 128865150> -> __attrs_4974860832
            __attrs_4974860832 = _static_4974855456

            # <header ... (0:0)
            # --------------------------------------------------------
            __append('<header class="row">\n      ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4974859680
            __attrs_4974859680 = _static_4753720080

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')

            # <Static value=<ast.Dict object at 0x128864400> name=None at 1288645b0> -> __attrs_4362432240
            __attrs_4362432240 = _static_4974855168

            # <img ... (0:0)
            # --------------------------------------------------------
            __append('<img')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4974854592
            __default_4974854592 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/++resource++plone-logo.svg' (28:35)> -> __attr_src
            __token = 1117
            try:
                __zt_tmp = __attrs_4362432240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_4754050160('string', '${context/absolute_url}/++resource++plone-logo.svg', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', '/++resource++plone-logo.svg', _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((' src="%s"' % __attr_src))
            __append(' width="215" height="56"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4974861216
            __default_4974861216 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x128865e10> at 128865e40> -> __attr_alt
            __attr_alt = 'Plone logo'
            __attr_alt = translate(__attr_alt, default=__attr_alt, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_alt is not None):
                __append((' alt="%s"' % __attr_alt))
            __append(' /></p>\n    </header>\n    ')

            # <Static value=<ast.Dict object at 0x128865840> name=None at 128865690> -> __attrs_4405206976
            __attrs_4405206976 = _static_4974860352
            __backup_profiles_4974701984 = get('profiles', __marker)

            # <Value 'view/profiles' (35:25)> -> __value
            __token = 1405
            try:
                __zt_tmp = __attrs_4405206976
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/profiles', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['profiles'] = __value
            __backup_base_profiles_4974702224 = get('base_profiles', __marker)

            # <Value 'profiles/base' (36:29)> -> __value
            __token = 1449
            try:
                __zt_tmp = __attrs_4405206976
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'profiles/base', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['base_profiles'] = __value
            __backup_default_profile_4974868512 = get('default_profile', __marker)

            # <Value 'profiles/default' (37:30)> -> __value
            __token = 1495
            try:
                __zt_tmp = __attrs_4405206976
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'profiles/default', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['default_profile'] = __value
            __backup_extension_profiles_4974859008 = get('extension_profiles', __marker)

            # <Value 'profiles/extensions' (38:32)> -> __value
            __token = 1547
            try:
                __zt_tmp = __attrs_4405206976
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'profiles/extensions', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['extension_profiles'] = __value
            __backup_advanced_4974854688 = get('advanced', __marker)

            # <Value 'request/advanced|nothing' (39:21)> -> __value
            __token = 1592
            try:
                __zt_tmp = __attrs_4405206976
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'request/advanced|nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['advanced'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4362422352
            __default_4362422352 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/@@plone-addsite' (34:27)> -> __attr_action
            __token = 1332
            try:
                __zt_tmp = __attrs_4405206976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_4754050160('string', '${context/absolute_url}/@@plone-addsite', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', '#', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append(' method="post">\n      ')

            # <Static value=<ast.Dict object at 0x11b2b5ab0> name=None at 11b2b6890> -> __attrs_4751608992
            __attrs_4751608992 = _static_4750793392

            # <article ... (0:0)
            # --------------------------------------------------------
            __append('<article class="row">\n        ')

            # <Static value=<ast.Dict object at 0x11e5539a0> name=None at 11e553970> -> __attrs_4801641056
            __attrs_4801641056 = _static_4803869088

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12">\n          ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4804550208
            __attrs_4804550208 = _static_4753720080

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1>')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4827661792
            __attrs_4827661792 = _static_4753720080

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span>')
            __stream_4804551168 = []
            __append_4804551168 = __stream_4804551168.append
            __append_4804551168('Create a Plone site')
            __msgid_4804551168 = __re_whitespace(''.join(__stream_4804551168)).strip()
            if __msgid_4804551168:
                __append(translate(__msgid_4804551168, mapping=None, default=__msgid_4804551168, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span></h1>\n          ')

            # <Static value=<ast.Dict object at 0x11fc06110> name=None at 11fc06c80> -> __attrs_4827959056
            __attrs_4827959056 = _static_4827668752

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="lead">')
            __stream_4827673936 = []
            __append_4827673936 = __stream_4827673936.append
            __append_4827673936('Adds a new Plone content management system site to the underlying application server.')
            __msgid_4827673936 = __re_whitespace(''.join(__stream_4827673936)).strip()
            if __msgid_4827673936:
                __append(translate(__msgid_4827673936, mapping=None, default=__msgid_4827673936, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n        </div>\n\n          ')

            # <Static value=<ast.Dict object at 0x11fc4e9b0> name=None at 11fc4f6a0> -> __attrs_4827964432
            __attrs_4827964432 = _static_4827965872

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12 mb-3 mb-3">\n            ')

            # <Static value=<ast.Dict object at 0x1180e3730> name=None at 1180e3700> -> __attrs_4828194816
            __attrs_4828194816 = _static_4698552112

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="site_id" class="form-label">')
            __stream_4827962656 = []
            __append_4827962656 = __stream_4827962656.append
            __append_4827962656('\n              Path identifier\n            ')
            __msgid_4827962656 = __re_whitespace(''.join(__stream_4827962656)).strip()
            if __msgid_4827962656:
                __append(translate(__msgid_4827962656, mapping=None, default=__msgid_4827962656, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n\n            ')

            # <Static value=<ast.Dict object at 0x10406fd00> name=None at 106962800> -> __attrs_4773970560
            __attrs_4773970560 = _static_4362534144

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="text" name="site_id" size="20" id="site_id" class="form-control"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4773976752
            __default_4773976752 = _DEFAULT_MARKER

            # <Substitution 'request/site_id|nothing' (55:40)> -> __attr_value
            __token = 2255
            try:
                __zt_tmp = __attrs_4773970560
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_4754050160('path', 'request/site_id|nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' />\n\n            ')

            # <Static value=<ast.Dict object at 0x11c8d1ea0> name=None at 11c8d28c0> -> __attrs_4773981360
            __attrs_4773981360 = _static_4773977760

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-text">')
            __stream_4773972192 = []
            __append_4773972192 = __stream_4773972192.append
            __append_4773972192('\n              The ID of the site. No special characters or spaces are allowed. This ends up as part of the URL unless hidden by an upstream web server.\n            ')
            __msgid_4773972192 = __re_whitespace(''.join(__stream_4773972192)).strip()
            if __msgid_4773972192:
                __append(translate(__msgid_4773972192, mapping=None, default=__msgid_4773972192, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n          </div>\n\n          ')

            # <Static value=<ast.Dict object at 0x11c8d2dd0> name=None at 11c8d2d10> -> __attrs_4773978288
            __attrs_4773978288 = _static_4773981648

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12 mb-3">\n            ')

            # <Static value=<ast.Dict object at 0x11c8d1b40> name=None at 11c8d2d40> -> __attrs_4773982176
            __attrs_4773982176 = _static_4773976896

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="title" class="form-label">')
            __stream_4773985728 = []
            __append_4773985728 = __stream_4773985728.append
            __append_4773985728('Title')
            __msgid_4773985728 = __re_whitespace(''.join(__stream_4773985728)).strip()
            if 'label_title':
                __append(translate('label_title', mapping=None, default=__msgid_4773985728, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n\n            ')

            # <Static value=<ast.Dict object at 0x11c8d37c0> name=None at 11c8d3820> -> __attrs_4773985056
            __attrs_4773985056 = _static_4773984192

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="text" name="title" size="30"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4773983664
            __default_4773983664 = _DEFAULT_MARKER

            # <Translate msgid='text_default_site_title' node=<ast.Constant object at 0x11c8d36a0> at 11c8d3640> -> __attr_value
            __attr_value = 'Site'
            __attr_value = translate('text_default_site_title', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' class="form-control" />\n\n            ')

            # <Static value=<ast.Dict object at 0x11c8d3ac0> name=None at 11c8d3b80> -> __attrs_4773980880
            __attrs_4773980880 = _static_4773984960

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-text">')
            __stream_4773980784 = []
            __append_4773980784 = __stream_4773980784.append
            __append_4773980784('\n              A short title for the site. This will be shown as part of the title of the browser window on each page.\n            ')
            __msgid_4773980784 = __re_whitespace(''.join(__stream_4773980784)).strip()
            if __msgid_4773980784:
                __append(translate(__msgid_4773980784, mapping=None, default=__msgid_4773980784, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n          </div>\n\n          ')

            # <Static value=<ast.Dict object at 0x11c8d2020> name=None at 11c8d2740> -> __attrs_4773980256
            __attrs_4773980256 = _static_4773978144

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12 mb-3">\n            ')

            # <Static value=<ast.Dict object at 0x11c8d0f10> name=None at 11c8d1c30> -> __attrs_4773972384
            __attrs_4773972384 = _static_4773973776

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="default_language" class="form-label">')
            __stream_4773978912 = []
            __append_4773978912 = __stream_4773978912.append
            __append_4773978912('Language')
            __msgid_4773978912 = __re_whitespace(''.join(__stream_4773978912)).strip()
            if __msgid_4773978912:
                __append(translate(__msgid_4773978912, mapping=None, default=__msgid_4773978912, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n\n            ')

            # <Static value=<ast.Dict object at 0x11c8d19f0> name=None at 11c8d1750> -> __attrs_4773976224
            __attrs_4773976224 = _static_4773976560
            __backup_browser_language_4750793296 = get('browser_language', __marker)

            # <Value 'view/browser_language' (78:49)> -> __value
            __token = 3261
            try:
                __zt_tmp = __attrs_4773976224
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/browser_language', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['browser_language'] = __value
            __backup_grouped_languages_4802069312 = get('grouped_languages', __marker)

            # <Value 'python:view.grouped_languages(browser_language)' (79:49)> -> __value
            __token = 3333
            try:
                __zt_tmp = __attrs_4773976224
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', 'view.grouped_languages(browser_language)', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['grouped_languages'] = __value

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select name="default_language" class="form-select">\n              ')

            # <Static value=<ast.Dict object at 0x11c8d0c70> name=None at 11c8d0c10> -> __attrs_4773970752
            __attrs_4773970752 = _static_4773973104
            __backup_group_4827676096 = get('group', __marker)

            # <Value 'grouped_languages' (80:42)> -> __iterator
            __token = 3426
            try:
                __zt_tmp = __attrs_4773970752
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4754050160('path', 'grouped_languages', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            (__iterator, ____index_4773971328, ) = getname('repeat')('group', __iterator)
            econtext['group'] = None
            for __item in __iterator:
                econtext['group'] = __item

                # <optgroup ... (0:0)
                # --------------------------------------------------------
                __append('<optgroup')

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4773970800
                __default_4773970800 = _DEFAULT_MARKER

                # <Substitution 'group/label' (81:46)> -> __attr_label
                __token = 3491
                try:
                    __zt_tmp = __attrs_4773970752
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_label = _static_4754050160('path', 'group/label', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                __attr_label = __quote(__attr_label, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_label is not None):
                    __append((' label="%s"' % __attr_label))
                __append('>\n\n                ')

                # <Static value=<ast.Dict object at 0x11c889120> name=None at 11c889150> -> __attrs_4773676848
                __attrs_4773676848 = _static_4773679392
                __backup_lang_4773971040 = get('lang', __marker)

                # <Value 'group/languages' (84:41)> -> __iterator
                __token = 3582
                try:
                    __zt_tmp = __attrs_4773676848
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4754050160('path', 'group/languages', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                (__iterator, ____index_4773689280, ) = getname('repeat')('lang', __iterator)
                econtext['lang'] = None
                for __item in __iterator:
                    econtext['lang'] = __item

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append('<option')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4773680352
                    __default_4773680352 = _DEFAULT_MARKER

                    # <Substitution "python:lang['langcode']" (85:46)> -> __attr_value
                    __token = 3645
                    try:
                        __zt_tmp = __attrs_4773676848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_4754050160('python', "lang['langcode']", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', 'en', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4773679728
                    __default_4773679728 = _DEFAULT_MARKER

                    # <Boolean "python:lang['langcode'] == browser_language" (86:48)> -> __attr_selected
                    __token = 3718
                    try:
                        __zt_tmp = __attrs_4773676848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_selected = _static_4754050160('python', "lang['langcode'] == browser_language", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    if (__attr_selected is _DEFAULT_MARKER):
                        __attr_selected = None
                    else:
                        if __attr_selected:
                            __attr_selected = 'selected'
                        else:
                            __attr_selected = None
                    if (__attr_selected is not None):
                        __append((' selected="%s"' % __attr_selected))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4773683424
                    __default_4773683424 = _DEFAULT_MARKER

                    # <Value "python: lang['label']" (87:37)> -> __cache_4773971904
                    __token = 3801
                    try:
                        __zt_tmp = __attrs_4773676848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4773971904 = _static_4754050160('python', " lang['label']", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value "python: lang['label']" (87:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 11c8d0160> -> __condition
                    __expression = __cache_4773971904

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                  English\n                ')
                    else:
                        __content = __cache_4773971904
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</option>')
                    ____index_4773689280 -= 1
                    if (____index_4773689280 > 0):
                        __append('\n                ')
                if (__backup_lang_4773971040 is __marker):
                    del econtext['lang']
                else:
                    econtext['lang'] = __backup_lang_4773971040
                __append('\n\n              </optgroup>')
                ____index_4773971328 -= 1
                if (____index_4773971328 > 0):
                    __append('\n              ')
            if (__backup_group_4827676096 is __marker):
                del econtext['group']
            else:
                econtext['group'] = __backup_group_4827676096
            __append('\n            </select>')
            if (__backup_grouped_languages_4802069312 is __marker):
                del econtext['grouped_languages']
            else:
                econtext['grouped_languages'] = __backup_grouped_languages_4802069312
            if (__backup_browser_language_4750793296 is __marker):
                del econtext['browser_language']
            else:
                econtext['browser_language'] = __backup_browser_language_4750793296
            __append('\n\n            ')

            # <Static value=<ast.Dict object at 0x11c88a050> name=None at 11c88b310> -> __attrs_4773683376
            __attrs_4773683376 = _static_4773683280

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-text">')
            __stream_4773684240 = []
            __append_4773684240 = __stream_4773684240.append
            __append_4773684240('\n              The main language of the site.\n            ')
            __msgid_4773684240 = __re_whitespace(''.join(__stream_4773684240)).strip()
            if __msgid_4773684240:
                __append(translate(__msgid_4773684240, mapping=None, default=__msgid_4773684240, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n          </div>\n\n          ')

            # <Static value=<ast.Dict object at 0x11c88bca0> name=None at 11c88bd30> -> __attrs_4773676944
            __attrs_4773676944 = _static_4773690528

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12 mb-3 tzx">\n            ')

            # <Static value=<ast.Dict object at 0x11c88bc10> name=None at 11c88b970> -> __attrs_4773689856
            __attrs_4773689856 = _static_4773690384

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="portal_timezone" class="form-label">')
            __stream_4773690912 = []
            __append_4773690912 = __stream_4773690912.append
            __append_4773690912('\n              Default timezone\n            ')
            __msgid_4773690912 = __re_whitespace(''.join(__stream_4773690912)).strip()
            if __msgid_4773690912:
                __append(translate(__msgid_4773690912, mapping=None, default=__msgid_4773690912, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n\n            ')

            # <Static value=<ast.Dict object at 0x11c88a770> name=None at 11c88ad40> -> __attrs_4773686784
            __attrs_4773686784 = _static_4773685104
            __backup_tz_list_4804204656 = get('tz_list', __marker)

            # <Value 'view/timezones' (108:40)> -> __value
            __token = 4403
            try:
                __zt_tmp = __attrs_4773686784
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/timezones', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['tz_list'] = __value

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select id="portal_timezone" name="portal_timezone" class="form-select">\n              ')

            # <Static value=<ast.Dict object at 0x11c88aec0> name=None at 11c88af20> -> __attrs_4773683568
            __attrs_4773683568 = _static_4773686976
            __backup_group_4773970896 = get('group', __marker)

            # <Value 'tz_list' (109:42)> -> __iterator
            __token = 4462
            try:
                __zt_tmp = __attrs_4773683568
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4754050160('path', 'tz_list', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            (__iterator, ____index_4773687696, ) = getname('repeat')('group', __iterator)
            econtext['group'] = None
            for __item in __iterator:
                econtext['group'] = __item

                # <optgroup ... (0:0)
                # --------------------------------------------------------
                __append('<optgroup')

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4773687216
                __default_4773687216 = _DEFAULT_MARKER

                # <Substitution 'group' (110:46)> -> __attr_label
                __token = 4517
                try:
                    __zt_tmp = __attrs_4773683568
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_label = _static_4754050160('path', 'group', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                __attr_label = __quote(__attr_label, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_label is not None):
                    __append((' label="%s"' % __attr_label))
                __append('>\n                ')

                # <Static value=<ast.Dict object at 0x11c889480> name=None at 11c8887c0> -> __attrs_4773678432
                __attrs_4773678432 = _static_4773680256
                __backup_tz_4773682464 = get('tz', __marker)

                # <Value 'python:tz_list[group]' (111:51)> -> __iterator
                __token = 4576
                try:
                    __zt_tmp = __attrs_4773678432
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4754050160('python', 'tz_list[group]', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                (__iterator, ____index_4773681984, ) = getname('repeat')('tz', __iterator)
                econtext['tz'] = None
                for __item in __iterator:
                    econtext['tz'] = __item

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append('<option')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4773675504
                    __default_4773675504 = _DEFAULT_MARKER

                    # <Substitution 'tz/value' (111:96)> -> __attr_value
                    __token = 4621
                    try:
                        __zt_tmp = __attrs_4773678432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_4754050160('path', 'tz/value', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', 'UTC', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4773680160
                    __default_4773680160 = _DEFAULT_MARKER

                    # <Value 'tz/label' (112:31)> -> __cache_4773683712
                    __token = 4662
                    try:
                        __zt_tmp = __attrs_4773678432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4773683712 = _static_4754050160('path', 'tz/label', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'tz/label' (112:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 11c889ea0> -> __condition
                    __expression = __cache_4773683712

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                  UTC\n                ')
                    else:
                        __content = __cache_4773683712
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</option>')
                    ____index_4773681984 -= 1
                    if (____index_4773681984 > 0):
                        __append('\n                ')
                if (__backup_tz_4773682464 is __marker):
                    del econtext['tz']
                else:
                    econtext['tz'] = __backup_tz_4773682464
                __append('\n              </optgroup>')
                ____index_4773687696 -= 1
                if (____index_4773687696 > 0):
                    __append('\n              ')
            if (__backup_group_4773970896 is __marker):
                del econtext['group']
            else:
                econtext['group'] = __backup_group_4773970896
            __append('\n            </select>')
            if (__backup_tz_list_4804204656 is __marker):
                del econtext['tz_list']
            else:
                econtext['tz_list'] = __backup_tz_list_4804204656
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x11c888b80> name=None at 11c888ac0> -> __attrs_4773677280
            __attrs_4773677280 = _static_4773677952

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-text">')
            __stream_4773675216 = []
            __append_4773675216 = __stream_4773675216.append
            __append_4773675216('\n              The default timezone setting of the portal.\n              Users will be able to set their own timezone, if available timezones are defined in the date and time settings.\n            ')
            __msgid_4773675216 = __re_whitespace(''.join(__stream_4773675216)).strip()
            if __msgid_4773675216:
                __append(translate(__msgid_4773675216, mapping=None, default=__msgid_4773675216, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n          </div>\n\n          ')

            # <Static value=<ast.Dict object at 0x11c8889d0> name=None at 11c888a00> -> __attrs_4773678960
            __attrs_4773678960 = _static_4773677520

            # <Value 'advanced' (124:30)> -> __condition
            __token = 5112
            try:
                __zt_tmp = __attrs_4773678960
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('path', 'advanced', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="col-md-12 mb-3">\n            ')

                # <Static value=<ast.Dict object at 0x11c889b70> name=None at 11c888400> -> __attrs_4974757776
                __attrs_4974757776 = _static_4773682032

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-check">\n              ')

                # <Static value=<ast.Dict object at 0x12884cf40> name=None at 12884ce80> -> __attrs_4974758832
                __attrs_4974758832 = _static_4974759744

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="form-check-input" id="example-content" type="checkbox" name="setup_content:boolean" checked="checked" />\n              ')

                # <Static value=<ast.Dict object at 0x12884d6f0> name=None at 12884d6c0> -> __attrs_4974760560
                __attrs_4974760560 = _static_4974761712

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="form-check-label" for="example-content">')
                __stream_4974760944 = []
                __append_4974760944 = __stream_4974760944.append
                __append_4974760944('Example content')
                __msgid_4974760944 = __re_whitespace(''.join(__stream_4974760944)).strip()
                if __msgid_4974760944:
                    __append(translate(__msgid_4974760944, mapping=None, default=__msgid_4974760944, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>\n              ')

                # <Static value=<ast.Dict object at 0x12884e050> name=None at 12884db70> -> __attrs_4974766368
                __attrs_4974766368 = _static_4974764112

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-text">')
                __stream_4974762240 = []
                __append_4974762240 = __stream_4974762240.append
                __append_4974762240('\n                Should the default example content be added to the site?\n              ')
                __msgid_4974762240 = __re_whitespace(''.join(__stream_4974762240)).strip()
                if __msgid_4974762240:
                    __append(translate(__msgid_4974762240, mapping=None, default=__msgid_4974762240, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</div>\n            </div>\n          </div>')
            __append('\n\n          ')

            # <Static value=<ast.Dict object at 0x12884e770> name=None at 12884e740> -> __attrs_4974766080
            __attrs_4974766080 = _static_4974765936

            # <Value 'not:advanced' (140:32)> -> __condition
            __token = 5742
            try:
                __zt_tmp = __attrs_4974766080
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('not', 'advanced', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="setup_content:boolean" value="true" />')
            __append('\n\n          ')

            # <Static value=<ast.Dict object at 0x12884e350> name=None at 12884e0e0> -> __attrs_4974770160
            __attrs_4974770160 = _static_4974764880

            # <Value 'python: len(base_profiles) > 1' (144:30)> -> __condition
            __token = 5897
            try:
                __zt_tmp = __attrs_4974770160
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('python', ' len(base_profiles) > 1', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="col-md-12">\n            ')

                # <Static value=<ast.Dict object at 0x12884ca00> name=None at 12884c7c0> -> __attrs_4974757488
                __attrs_4974757488 = _static_4974758400

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="mb-3">\n              ')

                # <Static value=<ast.Dict object at 0x12884f910> name=None at 12884fbe0> -> __attrs_4974770592
                __attrs_4974770592 = _static_4974770448

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="lead">')
                __stream_4974767376 = []
                __append_4974767376 = __stream_4974767376.append
                __append_4974767376('Base configuration')
                __msgid_4974767376 = __re_whitespace(''.join(__stream_4974767376)).strip()
                if __msgid_4974767376:
                    __append(translate(__msgid_4974767376, mapping=None, default=__msgid_4974767376, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n\n              ')

                # <Static value=<ast.Dict object at 0x12884fb20> name=None at 12884fd30> -> __attrs_4974771984
                __attrs_4974771984 = _static_4974770976
                __backup_info_4773684672 = get('info', __marker)

                # <Value 'base_profiles' (148:36)> -> __iterator
                __token = 6069
                try:
                    __zt_tmp = __attrs_4974771984
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4754050160('path', 'base_profiles', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                (__iterator, ____index_4974771648, ) = getname('repeat')('info', __iterator)
                econtext['info'] = None
                for __item in __iterator:
                    econtext['info'] = __item

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-check mb-3">\n                ')

                    # <Static value=<ast.Dict object at 0x12884f790> name=None at 12884e140> -> __attrs_4799909024
                    __attrs_4799909024 = _static_4974770064

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="radio" name="profile_id:string"')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4974769104
                    __default_4974769104 = _DEFAULT_MARKER

                    # <Substitution 'info/id' (155:43)> -> __attr_value
                    __token = 6388
                    try:
                        __zt_tmp = __attrs_4799909024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_4754050160('path', 'info/id', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', 'profile', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' class="form-check-input"')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4974762672
                    __default_4974762672 = _DEFAULT_MARKER

                    # <Substitution 'info/id' (154:41)> -> __attr_id
                    __token = 6336
                    try:
                        __zt_tmp = __attrs_4799909024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_4754050160('path', 'info/id', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4799917712
                    __default_4799917712 = _DEFAULT_MARKER

                    # <Boolean "python: default_profile==info['id'] and 'checked' or nothing" (156:44)> -> __attr_checked
                    __token = 6442
                    try:
                        __zt_tmp = __attrs_4799909024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_checked = _static_4754050160('python', " default_profile==info['id'] and 'checked' or nothing", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    if (__attr_checked is _DEFAULT_MARKER):
                        __attr_checked = None
                    else:
                        if __attr_checked:
                            __attr_checked = 'checked'
                        else:
                            __attr_checked = None
                    if (__attr_checked is not None):
                        __append((' checked="%s"' % __attr_checked))
                    __append(' />\n                ')

                    # <Static value=<ast.Dict object at 0x11e18f280> name=None at 11e18d150> -> __attrs_4799914256
                    __attrs_4799914256 = _static_4799918720

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append('<label class="form-check-label"')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4799906768
                    __default_4799906768 = _DEFAULT_MARKER

                    # <Substitution 'info/id' (157:68)> -> __attr_for
                    __token = 6577
                    try:
                        __zt_tmp = __attrs_4799914256
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_for = _static_4754050160('path', 'info/id', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_for is not None):
                        __append((' for="%s"' % __attr_for))
                    __append('>')

                    # <Interpolation value=<Substitution '${info/title}' (157:77)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11e18f0d0> -> __content_4355604080
                    __token = 6586
                    __token = 6588
                    try:
                        __zt_tmp = __attrs_4799914256
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_4355604080 = _static_4754050160('path', 'info/title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
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
                    __append('</label>\n                ')

                    # <Static value=<ast.Dict object at 0x11e18f970> name=None at 11e18ea10> -> __attrs_4799917760
                    __attrs_4799917760 = _static_4799920496

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-text">')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4799915840
                    __default_4799915840 = _DEFAULT_MARKER

                    # <Value 'info/description' (158:52)> -> __cache_4799909648
                    __token = 6660
                    try:
                        __zt_tmp = __attrs_4799917760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4799909648 = _static_4754050160('path', 'info/description', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'info/description' (158:52)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 11e18f760> -> __condition
                    __expression = __cache_4799909648

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <Interpolation value=<Substitution '${info/description}' (158:70)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11e18e980> -> __content_4355604080
                        __token = 6678
                        __token = 6680
                        try:
                            __zt_tmp = __attrs_4799917760
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_4355604080 = _static_4754050160('path', 'info/description', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
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
                    else:
                        __content = __cache_4799909648
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n              </div>')
                    ____index_4974771648 -= 1
                    if (____index_4974771648 > 0):
                        __append('\n              ')
                if (__backup_info_4773684672 is __marker):
                    del econtext['info']
                else:
                    econtext['info'] = __backup_info_4773684672
                __append('\n\n              ')

                # <Static value=<ast.Dict object at 0x11e18f4f0> name=None at 11e18d390> -> __attrs_4799912288
                __attrs_4799912288 = _static_4799919344

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-text">')
                __stream_4799918000 = []
                __append_4799918000 = __stream_4799918000.append
                __append_4799918000("\n                You normally don't need to change anything here unless you have specific reasons and know what you are doing.\n              ")
                __msgid_4799918000 = __re_whitespace(''.join(__stream_4799918000)).strip()
                if __msgid_4799918000:
                    __append(translate(__msgid_4799918000, mapping=None, default=__msgid_4799918000, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</div>\n\n            </div>\n          </div>')
            __append('\n\n\n          ')

            # <Static value=<ast.Dict object at 0x11e18d840> name=None at 11e18e590> -> __attrs_4799913248
            __attrs_4799913248 = _static_4799912000
            __backup_has_selected_4804549488 = get('has_selected', __marker)

            # <Value "python:[p for p in extension_profiles if p.get('selected', None)]" (170:40)> -> __value
            __token = 7046
            try:
                __zt_tmp = __attrs_4799913248
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', "[p for p in extension_profiles if p.get('selected', None)]", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['has_selected'] = __value

            # <Value 'python: extension_profiles or advanced' (171:30)> -> __condition
            __token = 7143
            try:
                __zt_tmp = __attrs_4799913248
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('python', ' extension_profiles or advanced', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:

                # <Negate value=<Value 'python: has_selected and not advanced' (172:29)> at 11e18d9c0> -> __cache_4799912384

                # <Value 'python: has_selected and not advanced' (172:29)> -> __cache_4799912384
                __token = 7212
                try:
                    __zt_tmp = __attrs_4799913248
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4799912384 = _static_4754050160('python', ' has_selected and not advanced', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                __cache_4799912384 = not __cache_4799912384
                __condition = __cache_4799912384
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="col-md-12 mt-3">')
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4799919824
                __attrs_4799919824 = _static_4753720080

                # <Value 'python: advanced' (173:34)> -> __condition
                __token = 7286
                try:
                    __zt_tmp = __attrs_4799919824
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4754050160('python', ' advanced', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                if __condition:
                    __append('\n              ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4799920976
                    __attrs_4799920976 = _static_4753720080

                    # <h2 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h2>')
                    __stream_4799920352 = []
                    __append_4799920352 = __stream_4799920352.append
                    __append_4799920352('Add-ons')
                    __msgid_4799920352 = __re_whitespace(''.join(__stream_4799920352)).strip()
                    if __msgid_4799920352:
                        __append(translate(__msgid_4799920352, mapping=None, default=__msgid_4799920352, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</h2>\n\n              ')

                    # <Static value=<ast.Dict object at 0x11e18d570> name=None at 11e18f2e0> -> __attrs_4799922128
                    __attrs_4799922128 = _static_4799911280

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="lead" >')
                    __stream_4799919200 = []
                    __append_4799919200 = __stream_4799919200.append
                    __append_4799919200('\n                Select any add-ons you want to activate immediately.\n                You can also activate add-ons after the site has been created using the Add-ons control panel.\n              ')
                    __msgid_4799919200 = __re_whitespace(''.join(__stream_4799919200)).strip()
                    if __msgid_4799919200:
                        __append(translate(__msgid_4799919200, mapping=None, default=__msgid_4799919200, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</div>\n            ')
                __append('\n\n            ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4799908784
                __attrs_4799908784 = _static_4753720080
                __backup_info_4773684576 = get('info', __marker)

                # <Value 'extension_profiles' (183:39)> -> __iterator
                __token = 7692
                try:
                    __zt_tmp = __attrs_4799908784
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4754050160('path', 'extension_profiles', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                (__iterator, ____index_4799919056, ) = getname('repeat')('info', __iterator)
                econtext['info'] = None
                for __item in __iterator:
                    econtext['info'] = __item
                    __append('\n              ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4799915120
                    __attrs_4799915120 = _static_4753720080
                    __backup_selected_4773678624 = get('selected', __marker)

                    # <Value 'info/selected|nothing' (184:44)> -> __value
                    __token = 7757
                    try:
                        __zt_tmp = __attrs_4799915120
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('path', 'info/selected|nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['selected'] = __value
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4799911568
                    __attrs_4799911568 = _static_4753720080

                    # <Value 'python: not selected or advanced' (185:43)> -> __condition
                    __token = 7824
                    try:
                        __zt_tmp = __attrs_4799911568
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4754050160('python', ' not selected or advanced', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    if __condition:
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x11c7c12d0> name=None at 11c7c10f0> -> __attrs_4767185024
                        __attrs_4767185024 = _static_4772860624

                        # <Value 'python: advanced' (187:37)> -> __condition
                        __token = 7943
                        try:
                            __zt_tmp = __attrs_4767185024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4754050160('python', ' advanced', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="form-check mb-3">\n                    ')

                            # <Static value=<ast.Dict object at 0x11cb7f2e0> name=None at 11cb7cfd0> -> __attrs_4777432912
                            __attrs_4777432912 = _static_4776784608

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input type="checkbox" name="extension_ids:list"')

                            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4777038928
                            __default_4777038928 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${info/id}' (190:33)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11cb15120> -> __attr_value
                            __token = 8090
                            __token = 8092
                            try:
                                __zt_tmp = __attrs_4777432912
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_4754050160('path', 'info/id', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_value = __attr_value
                            if (__attr_value is None):
                                pass
                            else:
                                if (__attr_value is _DEFAULT_MARKER):
                                    __attr_value = None
                                else:
                                    __tt = type(__attr_value)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __attr_value = str(__attr_value)
                                    else:
                                        if (__tt is bytes):
                                            __attr_value = decode(__attr_value)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __attr_value = __attr_value.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__attr_value)
                                                    __attr_value = (str(__attr_value) if (__attr_value is __converted) else __converted)
                                                else:
                                                    __attr_value = __attr_value()
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))

                            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4777035280
                            __default_4777035280 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${info/id}' (191:30)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11cbbcb50> -> __attr_id
                            __token = 8132
                            __token = 8134
                            try:
                                __zt_tmp = __attrs_4777432912
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_id = _static_4754050160('path', 'info/id', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_id = __attr_id
                            if (__attr_id is None):
                                pass
                            else:
                                if (__attr_id is _DEFAULT_MARKER):
                                    __attr_id = None
                                else:
                                    __tt = type(__attr_id)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __attr_id = str(__attr_id)
                                    else:
                                        if (__tt is bytes):
                                            __attr_id = decode(__attr_id)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __attr_id = __attr_id.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__attr_id)
                                                    __attr_id = (str(__attr_id) if (__attr_id is __converted) else __converted)
                                                else:
                                                    __attr_id = __attr_id()
                            if (__attr_id is not None):
                                __append((' id="%s"' % __attr_id))
                            __append(' class="form-check-input"')

                            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4777428496
                            __default_4777428496 = _DEFAULT_MARKER

                            # <Boolean 'info/selected|nothing' (193:50)> -> __attr_checked
                            __token = 8245
                            try:
                                __zt_tmp = __attrs_4777432912
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_checked = _static_4754050160('path', 'info/selected|nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                            if (__attr_checked is _DEFAULT_MARKER):
                                __attr_checked = None
                            else:
                                if __attr_checked:
                                    __attr_checked = 'checked'
                                else:
                                    __attr_checked = None
                            if (__attr_checked is not None):
                                __append((' checked="%s"' % __attr_checked))
                            __append(' />\n                    ')

                            # <Static value=<ast.Dict object at 0x11cc1ce20> name=None at 11cc1cee0> -> __attrs_4778055216
                            __attrs_4778055216 = _static_4777430560

                            # <label ... (0:0)
                            # --------------------------------------------------------
                            __append('<label class="form-check-label"')

                            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4777810752
                            __default_4777810752 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${info/id}' (194:57)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11cc79780> -> __attr_for
                            __token = 8329
                            __token = 8331
                            try:
                                __zt_tmp = __attrs_4778055216
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_for = _static_4754050160('path', 'info/id', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                            __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_for = __attr_for
                            if (__attr_for is None):
                                pass
                            else:
                                if (__attr_for is _DEFAULT_MARKER):
                                    __attr_for = None
                                else:
                                    __tt = type(__attr_for)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __attr_for = str(__attr_for)
                                    else:
                                        if (__tt is bytes):
                                            __attr_for = decode(__attr_for)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __attr_for = __attr_for.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__attr_for)
                                                    __attr_for = (str(__attr_for) if (__attr_for is __converted) else __converted)
                                                else:
                                                    __attr_for = __attr_for()
                            if (__attr_for is not None):
                                __append((' for="%s"' % __attr_for))
                            __append(' >')

                            # <Interpolation value=<Substitution '${info/title}' (194:70)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11ccb56f0> -> __content_4355604080
                            __token = 8342
                            __token = 8344
                            try:
                                __zt_tmp = __attrs_4778055216
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __content_4355604080 = _static_4754050160('path', 'info/title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
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
                            __append('</label>\n                    ')

                            # <Static value=<ast.Dict object at 0x11b601e40> name=None at 11ccb69b0> -> __attrs_4778665552
                            __attrs_4778665552 = _static_4754251328

                            # <Value "python: advanced and info['description']" (196:39)> -> __condition
                            __token = 8446
                            try:
                                __zt_tmp = __attrs_4778665552
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4754050160('python', " advanced and info['description']", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="form-text">')

                                # <Interpolation value=<Substitution '\n                      ${info/description}\n                    ' (196:81)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11e119c90> -> __content_4355604080
                                __token = 8511
                                __token = 8513
                                try:
                                    __zt_tmp = __attrs_4778665552
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __content_4355604080 = _static_4754050160('path', 'info/description', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                                __content_4355604080 = __quote(__content_4355604080, '\x00', '&#0;', None, None)
                                __content_4355604080 = ('%s%s%s' % ('\n                      ', (__content_4355604080 if (__content_4355604080 is not None) else ''), '\n                    ', ))
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
                                __append('</div>')
                            __append('\n                  </div>')
                        __append('\n                ')
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4799445312
                    __attrs_4799445312 = _static_4753720080

                    # <Value 'python: selected and not advanced' (201:43)> -> __condition
                    __token = 8656
                    try:
                        __zt_tmp = __attrs_4799445312
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4754050160('python', ' selected and not advanced', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    if __condition:
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x11cdc7a90> name=None at 11cdc4fa0> -> __attrs_4831185024
                        __attrs_4831185024 = _static_4779178640

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="hidden" name="extension_ids:list"')

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4831184544
                        __default_4831184544 = _DEFAULT_MARKER

                        # <Interpolation value=<Substitution '${info/id}' (204:31)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11ff608e0> -> __attr_value
                        __token = 8812
                        __token = 8814
                        try:
                            __zt_tmp = __attrs_4831185024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_4754050160('path', 'info/id', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        __attr_value = __attr_value
                        if (__attr_value is None):
                            pass
                        else:
                            if (__attr_value is _DEFAULT_MARKER):
                                __attr_value = None
                            else:
                                __tt = type(__attr_value)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __attr_value = str(__attr_value)
                                else:
                                    if (__tt is bytes):
                                        __attr_value = decode(__attr_value)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __attr_value = __attr_value.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__attr_value)
                                                __attr_value = (str(__attr_value) if (__attr_value is __converted) else __converted)
                                            else:
                                                __attr_value = __attr_value()
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' />\n                ')
                    __append('\n              ')
                    if (__backup_selected_4773678624 is __marker):
                        del econtext['selected']
                    else:
                        econtext['selected'] = __backup_selected_4773678624
                    __append('\n            ')
                    ____index_4799919056 -= 1
                    if (____index_4799919056 > 0):
                        __append('')
                if (__backup_info_4773684576 is __marker):
                    del econtext['info']
                else:
                    econtext['info'] = __backup_info_4773684576
                __append('\n          ')
                __condition = __cache_4799912384
                if __condition:
                    __append('</div>')
            if (__backup_has_selected_4804549488 is __marker):
                del econtext['has_selected']
            else:
                econtext['has_selected'] = __backup_has_selected_4804549488
            __append('\n          ')

            # <Static value=<ast.Dict object at 0x11e18caf0> name=None at 11e18c550> -> __attrs_4799909792
            __attrs_4799909792 = _static_4799908592

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12 mt-3">\n            ')

            # <Static value=<ast.Dict object at 0x11ff60ca0> name=None at 11ff60640> -> __attrs_4798877840
            __attrs_4798877840 = _static_4831186080

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" name="form.submitted:boolean" value="True" />\n            ')

            # <Static value=<ast.Dict object at 0x11cd97190> name=None at 11cd941f0> -> __attrs_4974621504
            __attrs_4974621504 = _static_4778979728

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button class="btn btn-success mt-3" type="submit" name="submit">')
            __stream_4778978720 = []
            __append_4778978720 = __stream_4778978720.append
            __append_4778978720('Create Plone Site')
            __msgid_4778978720 = __re_whitespace(''.join(__stream_4778978720)).strip()
            if __msgid_4778978720:
                __append(translate(__msgid_4778978720, mapping=None, default=__msgid_4778978720, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</button>\n          </div>\n      </article>\n    </form>')
            if (__backup_advanced_4974854688 is __marker):
                del econtext['advanced']
            else:
                econtext['advanced'] = __backup_advanced_4974854688
            if (__backup_extension_profiles_4974859008 is __marker):
                del econtext['extension_profiles']
            else:
                econtext['extension_profiles'] = __backup_extension_profiles_4974859008
            if (__backup_default_profile_4974868512 is __marker):
                del econtext['default_profile']
            else:
                econtext['default_profile'] = __backup_default_profile_4974868512
            if (__backup_base_profiles_4974702224 is __marker):
                del econtext['base_profiles']
            else:
                econtext['base_profiles'] = __backup_base_profiles_4974702224
            if (__backup_profiles_4974701984 is __marker):
                del econtext['profiles']
            else:
                econtext['profiles'] = __backup_profiles_4974701984
            __append('\n  </div>\n</body>\n\n</html>')
            __i18n_domain = __previous_i18n_domain_4974694496
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }