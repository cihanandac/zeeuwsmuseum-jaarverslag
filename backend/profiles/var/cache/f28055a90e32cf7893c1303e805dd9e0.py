# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/Products/CMFPlone/browser/templates/plone-overview.pt'

__tokens = {581: ('${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}', 16, 14), 583: ('string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css', 16, 16), 727: ('${string:${context/absolute_url}/++resource++plone-admin-ui.css}', 19, 14), 729: ('string:${context/absolute_url}/++resource++plone-admin-ui.css', 19, 16), 830: ('view/sites', 23, 24), 864: (' python:len(sites) > ', 24, 22), 1087: ('string:${context/absolute_url}/++resource++plone-logo.svg', 29, 36), 1755: ('sites', 44, 28), 1802: ('sites', 45, 39), 1852: ('python: view.outdated(site)', 46, 42), 1910: ("mb-3 ${python: 'p-3 alert-warning' if outdated else ''}", 47, 28), 1917: ("python: 'p-3 alert-warning' if outdated else ''", 47, 35), 2006: ('outdated', 48, 38), 2279: ('site/absolute_url', 50, 45), 2160: ("btn btn-primary ${python:'btn-lg' if not many and not outdated  else ''}", 49, 60), 2178: ("python:'btn-lg' if not many and not outdated  else ''", 49, 78), 2444: ('not: many', 53, 44), 2549: ('many', 54, 45), 2555: ('${python:site.title}', 54, 51), 2557: ('python:site.title', 54, 53), 2583: ('(${python:"/".join(site.getPhysicalPath())})', 54, 79), 2586: ('python:"/".join(site.getPhysicalPath())', 54, 82), 2845: ('outdated', 59, 43), 2906: ('python:view.upgrade_url(site)', 60, 51), 2984: ('not:view/can_manage', 61, 46), 3122: ('python:view.upgrade_url(site, can_manage=True)', 63, 54), 3614: ('sites', 74, 30), 3764: ('not:sites', 78, 30), 4005: ("python: '' if not sites else len(sites) + 1", 84, 44), 4088: (' string:${context/absolute_url}/@@plone-addsit', 85, 38), 4165: ('${action}', 86, 28), 4167: ('action', 86, 30), 4236: ('Plone${site_number}', 87, 59), 4243: ('site_number', 87, 66), 4329: ("btn btn-${python:'success' if sites else 'primary'}", 89, 31), 4339: ("python:'success' if sites else 'primary'", 89, 41), 4497: ('nothing', 91, 40), 4816: ('view/has_volto', 97, 35), 4858: ('${action}?site_id=Plone${site_number}&amp;classic=1', 98, 26), 4860: ('action', 98, 28), 4883: ('site_number', 98, 51), 5071: ('${action}?site_id=Plone${site_number}&amp;advanced=1', 102, 26), 5073: ('action', 102, 28), 5096: ('site_number', 102, 51), 5290: ('string:${context/absolute_url}/manage_main', 111, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4799917328 = {'href': '#', 'title': 'Go to the ZMI', }
_static_4771675200 = {'class': 'row', }
_static_4771670688 = {'class': 'btn btn-secondary', 'href': '${action}?site_id=Plone${site_number}&amp;advanced=1', }
_static_4771674576 = {'class': 'btn btn-info', 'href': '${action}?site_id=Plone${site_number}&amp;classic=1', }
_static_4771668288 = {'type': 'submit', 'class': "btn btn-${python:'success' if sites else 'primary'}", }
_static_4771667040 = {'type': 'hidden', 'name': 'site_id', 'value': 'Plone${site_number}', }
_static_4771661472 = {'id': 'add-plone-site', 'method': 'get', 'action': '${action}', }
_static_4771670304 = {'class': 'alert-warning p-1', }
_static_4760156624 = {'class': 'col-md-12', }
_static_4760142032 = {'type': 'submit', 'class': 'btn btn-warning me-3', }
_static_4760153072 = {'type': 'hidden', 'name': 'came_from', 'value': 'python:view.upgrade_url(site, can_manage=True)', }
_static_4760144528 = {'action': '', 'style': 'display: inline;', 'method': 'get', }
_static_4760146688 = {'href': '#', 'id': 'go-to-site-link', 'class': "btn btn-primary ${python:'btn-lg' if not many and not outdated  else ''}", 'title': 'Go to your instance', }
_static_4760148416 = {'class': "mb-3 ${python: 'p-3 alert-warning' if outdated else ''}", }
_static_4778358576 = {'class': 'col-md-12 mb-4', }
_static_4778355120 = {'class': 'row mb-5', }
_static_4778346912 = {'href': 'http://plone.org', 'title': 'Plone Community Home', }
_static_4778344896 = {'class': 'lead', }
_static_4778350752 = {'src': '/++resource++plone-logo.svg', 'width': '215', 'height': '56', 'alt': 'Plone logo', }
_static_4778352768 = {'class': 'row', }
_static_4778353200 = {'class': 'container admin mt-5 mb-5 p-4', }
_static_4778359968 = {'rel': 'stylesheet', 'type': 'text/css', 'href': '${string:${context/absolute_url}/++resource++plone-admin-ui.css}', }
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4803150560 = {'rel': 'stylesheet', 'type': 'text/css', 'href': '${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}', }
_static_4803161216 = {'name': 'viewport', 'content': 'width=device-width, initial-scale=1', }
_static_4803162704 = {'charset': 'utf-8', }
_static_4753720080 = {}
_static_4803165152 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'xml:lang': 'en', 'lang': 'en', }

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
            __append('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n')

            # <Static value=<ast.Dict object at 0x11e4a7be0> name=None at 11e4a7bb0> -> __attrs_4803164720
            __attrs_4803164720 = _static_4803165152
            __previous_i18n_domain_4803164576 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n\n')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4803163664
            __attrs_4803163664 = _static_4753720080

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n  ')

            # <Static value=<ast.Dict object at 0x11e4a7250> name=None at 11e4a7220> -> __attrs_4803162416
            __attrs_4803162416 = _static_4803162704

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta charset="utf-8"/>\n  ')

            # <Static value=<ast.Dict object at 0x11e4a6c80> name=None at 11e4a4af0> -> __attrs_4803152576
            __attrs_4803152576 = _static_4803161216

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta name="viewport" content="width=device-width, initial-scale=1"/>\n  ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4803151808
            __attrs_4803151808 = _static_4753720080

            # <title ... (0:0)
            # --------------------------------------------------------
            __append('<title>Plone</title>\n  ')

            # <Static value=<ast.Dict object at 0x11e4a42e0> name=None at 11e4a40a0> -> __attrs_4778360784
            __attrs_4778360784 = _static_4803150560

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4803150176
            __default_4803150176 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}' (16:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11e4a4550> -> __attr_href
            __token = 581
            __token = 583
            try:
                __zt_tmp = __attrs_4778360784
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

            # <Static value=<ast.Dict object at 0x11ccffca0> name=None at 11ccffb50> -> __attrs_4778358960
            __attrs_4778358960 = _static_4778359968

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4778356800
            __default_4778356800 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${string:${context/absolute_url}/++resource++plone-admin-ui.css}' (19:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11ccffac0> -> __attr_href
            __token = 727
            __token = 729
            try:
                __zt_tmp = __attrs_4778358960
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
            __append(' />\n</head>\n\n\n')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4778345856
            __attrs_4778345856 = _static_4753720080
            __backup_sites_4772601744 = get('sites', __marker)

            # <Value 'view/sites' (23:24)> -> __value
            __token = 830
            try:
                __zt_tmp = __attrs_4778345856
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/sites', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['sites'] = __value
            __backup_many_4772602080 = get('many', __marker)

            # <Value 'python:len(sites) > 1' (24:22)> -> __value
            __token = 864
            try:
                __zt_tmp = __attrs_4778345856
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', 'len(sites) > 1', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['many'] = __value

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n  ')

            # <Static value=<ast.Dict object at 0x11ccfe230> name=None at 11ccff0a0> -> __attrs_4778352672
            __attrs_4778352672 = _static_4778353200

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="container admin mt-5 mb-5 p-4">\n    ')

            # <Static value=<ast.Dict object at 0x11ccfe080> name=None at 11ccfdea0> -> __attrs_4778352144
            __attrs_4778352144 = _static_4778352768

            # <header ... (0:0)
            # --------------------------------------------------------
            __append('<header class="row">\n        ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4778354640
            __attrs_4778354640 = _static_4753720080

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')

            # <Static value=<ast.Dict object at 0x11ccfd8a0> name=None at 11ccfd7b0> -> __attrs_4778345472
            __attrs_4778345472 = _static_4778350752

            # <img ... (0:0)
            # --------------------------------------------------------
            __append('<img')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4778344848
            __default_4778344848 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/++resource++plone-logo.svg' (29:36)> -> __attr_src
            __token = 1087
            try:
                __zt_tmp = __attrs_4778345472
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_4754050160('string', '${context/absolute_url}/++resource++plone-logo.svg', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', '/++resource++plone-logo.svg', _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((' src="%s"' % __attr_src))
            __append(' width="215" height="56"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4778352048
            __default_4778352048 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x11ccfdc30> at 11ccfdbd0> -> __attr_alt
            __attr_alt = 'Plone logo'
            __attr_alt = translate(__attr_alt, default=__attr_alt, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_alt is not None):
                __append((' alt="%s"' % __attr_alt))
            __append(' /></p>\n        ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4778344704
            __attrs_4778344704 = _static_4753720080

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1>')
            __stream_4778350560 = []
            __append_4778350560 = __stream_4778350560.append
            __append_4778350560('Plone is up and running.')
            __msgid_4778350560 = __re_whitespace(''.join(__stream_4778350560)).strip()
            if __msgid_4778350560:
                __append(translate(__msgid_4778350560, mapping=None, default=__msgid_4778350560, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h1>\n        ')

            # <Static value=<ast.Dict object at 0x11ccfc1c0> name=None at 11ccfcd60> -> __attrs_4778348688
            __attrs_4778348688 = _static_4778344896

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="lead">\n            ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4778346096
            __attrs_4778346096 = _static_4753720080

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span>')
            __stream_4778348832 = []
            __append_4778348832 = __stream_4778348832.append
            __append_4778348832(' For an introduction to Plone, documentation, demos, add-ons, support, and community, visit')
            __msgid_4778348832 = __re_whitespace(''.join(__stream_4778348832)).strip()
            if 'label_plone_org_description':
                __append(translate('label_plone_org_description', mapping=None, default=__msgid_4778348832, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span>\n            ')

            # <Static value=<ast.Dict object at 0x11ccfc9a0> name=None at 11ccfc940> -> __attrs_4778346672
            __attrs_4778346672 = _static_4778346912

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a href="http://plone.org"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4778349408
            __default_4778349408 = _DEFAULT_MARKER

            # <Translate msgid='label_plone_org_title' node=<ast.Constant object at 0x11ccfca90> at 11ccfd4b0> -> __attr_title
            __attr_title = 'Plone Community Home'
            __attr_title = translate('label_plone_org_title', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append('>plone.org</a>.\n          </p>\n\n    </header>\n\n    ')

            # <Static value=<ast.Dict object at 0x11ccfe9b0> name=None at 11ccff310> -> __attrs_4778356608
            __attrs_4778356608 = _static_4778355120

            # <article ... (0:0)
            # --------------------------------------------------------
            __append('<article class="row mb-5">\n        ')

            # <Static value=<ast.Dict object at 0x11ccff730> name=None at 11ccfe770> -> __attrs_4760144768
            __attrs_4760144768 = _static_4778358576

            # <Value 'sites' (44:28)> -> __condition
            __token = 1755
            try:
                __zt_tmp = __attrs_4760144768
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('path', 'sites', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="col-md-12 mb-4">\n            ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4760147696
                __attrs_4760147696 = _static_4753720080
                __backup_site_4772859712 = get('site', __marker)

                # <Value 'sites' (45:39)> -> __iterator
                __token = 1802
                try:
                    __zt_tmp = __attrs_4760147696
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4754050160('path', 'sites', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                (__iterator, ____index_4760146400, ) = getname('repeat')('site', __iterator)
                econtext['site'] = None
                for __item in __iterator:
                    econtext['site'] = __item
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x11bba19c0> name=None at 11bba1b10> -> __attrs_4760149664
                    __attrs_4760149664 = _static_4760148416
                    __backup_outdated_4772860288 = get('outdated', __marker)

                    # <Value 'python: view.outdated(site)' (46:42)> -> __value
                    __token = 1852
                    try:
                        __zt_tmp = __attrs_4760149664
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4754050160('python', ' view.outdated(site)', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    econtext['outdated'] = __value

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4760148608
                    __default_4760148608 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "mb-3 ${python: 'p-3 alert-warning' if outdated else ''}" (47:28)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11bba18d0> -> __attr_class
                    __token = 1910
                    __token = 1917
                    try:
                        __zt_tmp = __attrs_4760149664
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4754050160('python', " 'p-3 alert-warning' if outdated else ''", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s' % ('mb-3 ', (__attr_class if (__attr_class is not None) else ''), ))
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
                    __append('>\n                    ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4760158016
                    __attrs_4760158016 = _static_4753720080

                    # <Value 'outdated' (48:38)> -> __condition
                    __token = 2006
                    try:
                        __zt_tmp = __attrs_4760158016
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4754050160('path', 'outdated', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    if __condition:

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append('<p>')
                        __stream_4760146208 = []
                        __append_4760146208 = __stream_4760146208.append
                        __append_4760146208('This site configuration is outdated and needs to be upgraded:')
                        __msgid_4760146208 = __re_whitespace(''.join(__stream_4760146208)).strip()
                        if __msgid_4760146208:
                            __append(translate(__msgid_4760146208, mapping=None, default=__msgid_4760146208, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</p>')
                    __append('\n                    ')

                    # <Static value=<ast.Dict object at 0x11bba1300> name=None at 11bba0c70> -> __attrs_4760142992
                    __attrs_4760142992 = _static_4760146688

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4760150816
                    __default_4760150816 = _DEFAULT_MARKER

                    # <Substitution 'site/absolute_url' (50:45)> -> __attr_href
                    __token = 2279
                    try:
                        __zt_tmp = __attrs_4760142992
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4754050160('path', 'site/absolute_url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' id="go-to-site-link"')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4760154752
                    __default_4760154752 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "btn btn-primary ${python:'btn-lg' if not many and not outdated  else ''}" (49:60)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11bba3f10> -> __attr_class
                    __token = 2160
                    __token = 2178
                    try:
                        __zt_tmp = __attrs_4760142992
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4754050160('python', "'btn-lg' if not many and not outdated  else ''", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s' % ('btn btn-primary ', (__attr_class if (__attr_class is not None) else ''), ))
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

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4760155568
                    __default_4760155568 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<ast.Constant object at 0x11bba33a0> at 11bba07c0> -> __attr_title
                    __attr_title = 'Go to your instance'
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append('>\n                        ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4760151296
                    __attrs_4760151296 = _static_4753720080

                    # <Value 'not: many' (53:44)> -> __condition
                    __token = 2444
                    try:
                        __zt_tmp = __attrs_4760151296
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4754050160('not', ' many', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    if __condition:
                        __stream_4760153648 = []
                        __append_4760153648 = __stream_4760153648.append
                        __append_4760153648('View your Plone site')
                        __msgid_4760153648 = __re_whitespace(''.join(__stream_4760153648)).strip()
                        if __msgid_4760153648:
                            __append(translate(__msgid_4760153648, mapping=None, default=__msgid_4760153648, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n                        ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4760145968
                    __attrs_4760145968 = _static_4753720080

                    # <Value 'many' (54:45)> -> __condition
                    __token = 2549
                    try:
                        __zt_tmp = __attrs_4760145968
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4754050160('path', 'many', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    if __condition:

                        # <Interpolation value=<Substitution '${python:site.title} ' (54:51)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11bba0f40> -> __content_4355604080
                        __token = 2555
                        __token = 2557
                        try:
                            __zt_tmp = __attrs_4760145968
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_4355604080 = _static_4754050160('python', 'site.title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                        __content_4355604080 = __quote(__content_4355604080, '\x00', '&#0;', None, None)
                        __content_4355604080 = ('%s%s' % ((__content_4355604080 if (__content_4355604080 is not None) else ''), ' ', ))
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

                        # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4760152640
                        __attrs_4760152640 = _static_4753720080

                        # <small ... (0:0)
                        # --------------------------------------------------------
                        __append('<small>')

                        # <Interpolation value=<Substitution '(${python:"/".join(site.getPhysicalPath())})' (54:79)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11bba2710> -> __content_4355604080
                        __token = 2583
                        __token = 2586
                        try:
                            __zt_tmp = __attrs_4760152640
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_4355604080 = _static_4754050160('python', '"/".join(site.getPhysicalPath())', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                        __content_4355604080 = __quote(__content_4355604080, '\x00', '&#0;', None, None)
                        __content_4355604080 = ('%s%s%s' % ('(', (__content_4355604080 if (__content_4355604080 is not None) else ''), ')', ))
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
                        __append('</small>')
                    __append('\n                    </a>\n                    ')

                    # <Static value=<ast.Dict object at 0x11bba0a90> name=None at 11bba0130> -> __attrs_4760152400
                    __attrs_4760152400 = _static_4760144528

                    # <Value 'outdated' (59:43)> -> __condition
                    __token = 2845
                    try:
                        __zt_tmp = __attrs_4760152400
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4754050160('path', 'outdated', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    if __condition:

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append('<form')

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4760152256
                        __default_4760152256 = _DEFAULT_MARKER

                        # <Substitution 'python:view.upgrade_url(site)' (60:51)> -> __attr_action
                        __token = 2906
                        try:
                            __zt_tmp = __attrs_4760152400
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_action = _static_4754050160('python', 'view.upgrade_url(site)', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                        __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_action is not None):
                            __append((' action="%s"' % __attr_action))
                        __append(' style="display: inline;" method="get">\n                        ')

                        # <Static value=<ast.Dict object at 0x11bba2bf0> name=None at 11bba02e0> -> __attrs_4760155424
                        __attrs_4760155424 = _static_4760153072

                        # <Value 'not:view/can_manage' (61:46)> -> __condition
                        __token = 2984
                        try:
                            __zt_tmp = __attrs_4760155424
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4754050160('not', 'view/can_manage', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                        if __condition:

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input type="hidden" name="came_from"')

                            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4760153408
                            __default_4760153408 = _DEFAULT_MARKER

                            # <Substitution 'python:view.upgrade_url(site, can_manage=True)' (63:54)> -> __attr_value
                            __token = 3122
                            try:
                                __zt_tmp = __attrs_4760155424
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_4754050160('python', 'view.upgrade_url(site, can_manage=True)', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))
                            __append('/>')
                        __append('\n                        ')

                        # <Static value=<ast.Dict object at 0x11bba00d0> name=None at 11bba0100> -> __attrs_4760142464
                        __attrs_4760142464 = _static_4760142032

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" class="btn btn-warning me-3">')
                        __stream_4760144096 = []
                        __append_4760144096 = __stream_4760144096.append
                        __append_4760144096('Upgrade&hellip;')
                        __msgid_4760144096 = __re_whitespace(''.join(__stream_4760144096)).strip()
                        if 'label_upgrade_hellip':
                            __append(translate('label_upgrade_hellip', mapping=None, default=__msgid_4760144096, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</button>\n                    </form>')
                    __append('\n                </div>')
                    if (__backup_outdated_4772860288 is __marker):
                        del econtext['outdated']
                    else:
                        econtext['outdated'] = __backup_outdated_4772860288
                    __append('\n            ')
                    ____index_4760146400 -= 1
                    if (____index_4760146400 > 0):
                        __append('')
                if (__backup_site_4772859712 is __marker):
                    del econtext['site']
                else:
                    econtext['site'] = __backup_site_4772859712
                __append('\n        </div>')
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x11bba39d0> name=None at 11bba0df0> -> __attrs_4771667664
            __attrs_4771667664 = _static_4760156624

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12">\n            ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4771673280
            __attrs_4771673280 = _static_4753720080

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append('<h2 >')
            __stream_4771673232 = []
            __append_4771673232 = __stream_4771673232.append
            __append_4771673232('Add Plone site')
            __msgid_4771673232 = __re_whitespace(''.join(__stream_4771673232)).strip()
            if __msgid_4771673232:
                __append(translate(__msgid_4771673232, mapping=None, default=__msgid_4771673232, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h2>\n            ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4771671504
            __attrs_4771671504 = _static_4753720080

            # <Value 'sites' (74:30)> -> __condition
            __token = 3614
            try:
                __zt_tmp = __attrs_4771671504
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('path', 'sites', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p>')
                __stream_4771673952 = []
                __append_4771673952 = __stream_4771673952.append
                __append_4771673952('\n                You can add another Plone site to the server.\n            ')
                __msgid_4771673952 = __re_whitespace(''.join(__stream_4771673952)).strip()
                if __msgid_4771673952:
                    __append(translate(__msgid_4771673952, mapping=None, default=__msgid_4771673952, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>')
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x11c69e920> name=None at 11c69c940> -> __attrs_4771667760
            __attrs_4771667760 = _static_4771670304

            # <Value 'not:sites' (78:30)> -> __condition
            __token = 3764
            try:
                __zt_tmp = __attrs_4771667760
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('not', 'sites', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="alert-warning p-1">')
                __stream_4771670928 = []
                __append_4771670928 = __stream_4771670928.append
                __append_4771670928('\n                Your Plone site has not been added yet.\n            ')
                __msgid_4771670928 = __re_whitespace(''.join(__stream_4771670928)).strip()
                if __msgid_4771670928:
                    __append(translate(__msgid_4771670928, mapping=None, default=__msgid_4771670928, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>')
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x11c69c6a0> name=None at 11c69e470> -> __attrs_4771660656
            __attrs_4771660656 = _static_4771661472
            __backup_site_number_4772456976 = get('site_number', __marker)

            # <Value "python: '' if not sites else len(sites) + 1" (84:44)> -> __value
            __token = 4005
            try:
                __zt_tmp = __attrs_4771660656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', " '' if not sites else len(sites) + 1", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['site_number'] = __value
            __backup_action_4772604528 = get('action', __marker)

            # <Value 'string:${context/absolute_url}/@@plone-addsite' (85:38)> -> __value
            __token = 4088
            try:
                __zt_tmp = __attrs_4771660656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('string', '${context/absolute_url}/@@plone-addsite', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['action'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form id="add-plone-site" method="get"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4771660848
            __default_4771660848 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${action}' (86:28)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11c69c910> -> __attr_action
            __token = 4165
            __token = 4167
            try:
                __zt_tmp = __attrs_4771660656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_4754050160('path', 'action', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_action = __attr_action
            if (__attr_action is None):
                pass
            else:
                if (__attr_action is _DEFAULT_MARKER):
                    __attr_action = None
                else:
                    __tt = type(__attr_action)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_action = str(__attr_action)
                    else:
                        if (__tt is bytes):
                            __attr_action = decode(__attr_action)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_action = __attr_action.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_action)
                                    __attr_action = (str(__attr_action) if (__attr_action is __converted) else __converted)
                                else:
                                    __attr_action = __attr_action()
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append('>\n                ')

            # <Static value=<ast.Dict object at 0x11c69dc60> name=None at 11c69dc90> -> __attrs_4771667904
            __attrs_4771667904 = _static_4771667040

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" name="site_id"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4771663824
            __default_4771663824 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution 'Plone${site_number}' (87:59)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11c69dc30> -> __attr_value
            __token = 4236
            __token = 4243
            try:
                __zt_tmp = __attrs_4771667904
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_4754050160('path', 'site_number', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_value = ('%s%s' % ('Plone', (__attr_value if (__attr_value is not None) else ''), ))
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

            # <Static value=<ast.Dict object at 0x11c69e140> name=None at 11c69dae0> -> __attrs_4771666272
            __attrs_4771666272 = _static_4771668288

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button type="submit"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4771668720
            __default_4771668720 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "btn btn-${python:'success' if sites else 'primary'}" (89:31)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11c69e410> -> __attr_class
            __token = 4329
            __token = 4339
            try:
                __zt_tmp = __attrs_4771666272
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4754050160('python', "'success' if sites else 'primary'", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_class = ('%s%s' % ('btn btn-', (__attr_class if (__attr_class is not None) else ''), ))
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
            __stream_4771668672 = []
            __append_4771668672 = __stream_4771668672.append
            __append_4771668672('Create a new Plone site')
            __msgid_4771668672 = __re_whitespace(''.join(__stream_4771668672)).strip()
            if __msgid_4771668672:
                __append(translate(__msgid_4771668672, mapping=None, default=__msgid_4771668672, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</button>\n                ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4771665408
            __attrs_4771665408 = _static_4753720080

            # <Value 'nothing' (91:40)> -> __condition
            __token = 4497
            try:
                __zt_tmp = __attrs_4771665408
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('path', 'nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:
                __append('\n                  When we have Volto, the button above will create a Volto site,\n                  and we need an extra button below to create a Classic Plone site.\n                ')
            __append('\n                ')

            # <Static value=<ast.Dict object at 0x11c69f9d0> name=None at 11c69fa30> -> __attrs_4771672560
            __attrs_4771672560 = _static_4771674576

            # <Value 'view/has_volto' (97:35)> -> __condition
            __token = 4816
            try:
                __zt_tmp = __attrs_4771672560
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('path', 'view/has_volto', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="btn btn-info"')

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4771675968
                __default_4771675968 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${action}?site_id=Plone${site_number}&amp;classic=1' (98:26)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11c69e5f0> -> __attr_href
                __token = 4858
                __token = 4860
                try:
                    __zt_tmp = __attrs_4771672560
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4754050160('path', 'action', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                __token = 4883
                try:
                    __zt_tmp = __attrs_4771672560
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href_4881 = _static_4754050160('path', 'site_number', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                __attr_href_4881 = __quote(__attr_href_4881, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_href = ('%s%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '?site_id=Plone', (__attr_href_4881 if (__attr_href_4881 is not None) else ''), '&amp;classic=1', ))
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
                __append(' >')
                __stream_4771665216 = []
                __append_4771665216 = __stream_4771665216.append
                __append_4771665216('Create Classic Plone site')
                __msgid_4771665216 = __re_whitespace(''.join(__stream_4771665216)).strip()
                if __msgid_4771665216:
                    __append(translate(__msgid_4771665216, mapping=None, default=__msgid_4771665216, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</a>')
            __append('\n                ')

            # <Static value=<ast.Dict object at 0x11c69eaa0> name=None at 11c69e9e0> -> __attrs_4771672848
            __attrs_4771672848 = _static_4771670688

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="btn btn-secondary"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4771669968
            __default_4771669968 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${action}?site_id=Plone${site_number}&amp;advanced=1' (102:26)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11c69e890> -> __attr_href
            __token = 5071
            __token = 5073
            try:
                __zt_tmp = __attrs_4771672848
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4754050160('path', 'action', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 5096
            try:
                __zt_tmp = __attrs_4771672848
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href_5094 = _static_4754050160('path', 'site_number', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_href_5094 = __quote(__attr_href_5094, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = ('%s%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '?site_id=Plone', (__attr_href_5094 if (__attr_href_5094 is not None) else ''), '&amp;advanced=1', ))
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
            __append(' >')
            __stream_4771671840 = []
            __append_4771671840 = __stream_4771671840.append
            __append_4771671840('Advanced')
            __msgid_4771671840 = __re_whitespace(''.join(__stream_4771671840)).strip()
            if __msgid_4771671840:
                __append(translate(__msgid_4771671840, mapping=None, default=__msgid_4771671840, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n            </form>')
            if (__backup_action_4772604528 is __marker):
                del econtext['action']
            else:
                econtext['action'] = __backup_action_4772604528
            if (__backup_site_number_4772456976 is __marker):
                del econtext['site_number']
            else:
                econtext['site_number'] = __backup_site_number_4772456976
            __append('\n        </div>\n    </article>\n\n    ')

            # <Static value=<ast.Dict object at 0x11c69fc40> name=None at 11c69fca0> -> __attrs_4771675584
            __attrs_4771675584 = _static_4771675200

            # <footer ... (0:0)
            # --------------------------------------------------------
            __append('<footer class="row">\n    ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4799915168
            __attrs_4799915168 = _static_4753720080

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>\n      ')

            # <Static value=<ast.Dict object at 0x11e18ed10> name=None at 11e18d450> -> __attrs_4799919056
            __attrs_4799919056 = _static_4799917328

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4799913344
            __default_4799913344 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/manage_main' (111:29)> -> __attr_href
            __token = 5290
            try:
                __zt_tmp = __attrs_4799919056
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4754050160('string', '${context/absolute_url}/manage_main', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4799914112
            __default_4799914112 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x11e18cdf0> at 11e18d4b0> -> __attr_title
            __attr_title = 'Go to the ZMI'
            __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append('>')
            __stream_4799909888 = []
            __append_4799909888 = __stream_4799909888.append
            __append_4799909888('Management Interface')
            __msgid_4799909888 = __re_whitespace(''.join(__stream_4799909888)).strip()
            if 'label_zmi_link':
                __append(translate('label_zmi_link', mapping=None, default=__msgid_4799909888, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n      ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4799919296
            __attrs_4799919296 = _static_4753720080

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span>')
            __stream_4799917904 = []
            __append_4799917904 = __stream_4799917904.append
            __append_4799917904(' &#151; low-level technical configuration.')
            __msgid_4799917904 = __re_whitespace(''.join(__stream_4799917904)).strip()
            if 'label_zmi_link_description':
                __append(translate('label_zmi_link_description', mapping=None, default=__msgid_4799917904, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span>\n    </p>\n  </footer>\n</div>\n</body>')
            if (__backup_many_4772602080 is __marker):
                del econtext['many']
            else:
                econtext['many'] = __backup_many_4772602080
            if (__backup_sites_4772601744 is __marker):
                del econtext['sites']
            else:
                econtext['sites'] = __backup_sites_4772601744
            __append('\n</html>')
            __i18n_domain = __previous_i18n_domain_4803164576
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }