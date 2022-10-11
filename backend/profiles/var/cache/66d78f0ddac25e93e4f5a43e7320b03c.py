# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/registry/browser/templates/exportxml.pt'

__tokens = {671: ('python:view.interfaces()', 14, 35), 722: ('${python:prefix[1]}', 14, 86), 724: ('python:prefix[1]', 14, 88), 743: ('${python:prefix[0]}', 14, 107), 745: ('python:prefix[0]', 14, 109), 1025: ('python:view.prefixes()', 21, 35), 1074: ('${python:prefix[1]}', 21, 84), 1076: ('python:prefix[1]', 21, 86), 1095: ('${python:prefix[0]}', 21, 105), 1097: ('python:prefix[0]', 21, 107)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4900728752 = {'target': '_blank', 'href': '${python:prefix[1]}', }
_static_4900723856 = {'id': 'h3-prefixes', }
_static_4900724864 = {'class': 'exporttab', 'id': 'export-section-prefixes', }
_static_4900723760 = {'target': '_blank', 'href': '${python:prefix[1]}', }
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
_static_4900726832 = {'class': 'collapse_interfaces', }
_static_4900730624 = {'id': 'h3-interfaces', }
_static_4900342176 = {'class': 'exporttab', 'id': 'export-section-interfaces', }
_static_4900349808 = {'class': 'pat-autotoc autotabs', 'data-pat-autotoc': 'levels: h3; section: div.exporttab; className: autotabs', }
_static_4428767312 = {}

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

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900344912
            __attrs_4900344912 = _static_4428767312

            # <tal ... (0:0)
            # --------------------------------------------------------
            __append('<tal>\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900353504
            __attrs_4900353504 = _static_4428767312

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3>')
            __stream_4900353312 = []
            __append_4900353312 = __stream_4900353312.append
            __append_4900353312('Export parts')
            __msgid_4900353312 = __re_whitespace(''.join(__stream_4900353312)).strip()
            if 'registry_export_parts_heading':
                __append(translate('registry_export_parts_heading', mapping=None, default=__msgid_4900353312, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h3>\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900343328
            __attrs_4900343328 = _static_4428767312

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')
            __stream_4900343808 = []
            __append_4900343808 = __stream_4900343808.append
            __append_4900343808('\n      Download of a XML-file optimized to be used in a GenericSetup profile of an add-on or policy profile.\n      It contains only the selected parts.\n    ')
            __msgid_4900343808 = __re_whitespace(''.join(__stream_4900343808)).strip()
            if 'registry_export_parts_text':
                __append(translate('registry_export_parts_text', mapping=None, default=__msgid_4900343808, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n\n    ')

            # <Static value=<ast.Dict object at 0x124156770> name=None at 1241574f0> -> __attrs_4900353744
            __attrs_4900353744 = _static_4900349808

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="pat-autotoc autotabs" data-pat-autotoc="levels: h3; section: div.exporttab; className: autotabs">\n        ')

            # <Static value=<ast.Dict object at 0x1241549a0> name=None at 1241553f0> -> __attrs_4900731776
            __attrs_4900731776 = _static_4900342176

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="exporttab" id="export-section-interfaces">\n          ')

            # <Static value=<ast.Dict object at 0x1241b3700> name=None at 1241b3c70> -> __attrs_4900723088
            __attrs_4900723088 = _static_4900730624

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3 id="h3-interfaces">')
            __stream_4900720064 = []
            __append_4900720064 = __stream_4900720064.append
            __append_4900720064('by Interface')
            __msgid_4900720064 = __re_whitespace(''.join(__stream_4900720064)).strip()
            if 'registry_export_parts_label_iface':
                __append(translate('registry_export_parts_label_iface', mapping=None, default=__msgid_4900720064, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h3>\n          ')

            # <Static value=<ast.Dict object at 0x1241b2830> name=None at 1241b0e20> -> __attrs_4900721936
            __attrs_4900721936 = _static_4900726832

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append('<ul class="collapse_interfaces">\n            ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900731440
            __attrs_4900731440 = _static_4428767312
            __backup_prefix_4909528688 = get('prefix', __marker)

            # <Value 'python:view.interfaces()' (14:35)> -> __iterator
            __token = 671
            try:
                __zt_tmp = __attrs_4900731440
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4427992992('python', 'view.interfaces()', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            (__iterator, ____index_4900723904, ) = getname('repeat')('prefix', __iterator)
            econtext['prefix'] = None
            for __item in __iterator:
                econtext['prefix'] = __item

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li>')

                # <Static value=<ast.Dict object at 0x1241b1c30> name=None at 1241b3df0> -> __attrs_4900728560
                __attrs_4900728560 = _static_4900723760

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a target="_blank"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900724384
                __default_4900724384 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${python:prefix[1]}' (14:86)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1241b2680> -> __attr_href
                __token = 722
                __token = 724
                try:
                    __zt_tmp = __attrs_4900728560
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4427992992('python', 'prefix[1]', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
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
                __append('>')

                # <Interpolation value=<Substitution '${python:prefix[0]}' (14:107)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1241b3280> -> __content_4353737008
                __token = 743
                __token = 745
                try:
                    __zt_tmp = __attrs_4900728560
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_4353737008 = _static_4427992992('python', 'prefix[0]', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
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
                __append('</a></li>')
                ____index_4900723904 -= 1
                if (____index_4900723904 > 0):
                    __append('\n            ')
            if (__backup_prefix_4909528688 is __marker):
                del econtext['prefix']
            else:
                econtext['prefix'] = __backup_prefix_4909528688
            __append('\n          </ul>\n        </div>\n        ')

            # <Static value=<ast.Dict object at 0x1241b2080> name=None at 1241b1c00> -> __attrs_4900730000
            __attrs_4900730000 = _static_4900724864

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="exporttab" id="export-section-prefixes">\n          ')

            # <Static value=<ast.Dict object at 0x1241b1c90> name=None at 1241b19c0> -> __attrs_4900730864
            __attrs_4900730864 = _static_4900723856

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3 id="h3-prefixes">')
            __stream_4900729664 = []
            __append_4900729664 = __stream_4900729664.append
            __append_4900729664('by Prefix')
            __msgid_4900729664 = __re_whitespace(''.join(__stream_4900729664)).strip()
            if 'registry_export_parts_label_prefix':
                __append(translate('registry_export_parts_label_prefix', mapping=None, default=__msgid_4900729664, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h3>\n          ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900727552
            __attrs_4900727552 = _static_4428767312

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append('<ul>\n            ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900719248
            __attrs_4900719248 = _static_4428767312
            __backup_prefix_4899637136 = get('prefix', __marker)

            # <Value 'python:view.prefixes()' (21:35)> -> __iterator
            __token = 1025
            try:
                __zt_tmp = __attrs_4900719248
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4427992992('python', 'view.prefixes()', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            (__iterator, ____index_4900722464, ) = getname('repeat')('prefix', __iterator)
            econtext['prefix'] = None
            for __item in __iterator:
                econtext['prefix'] = __item

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li>')

                # <Static value=<ast.Dict object at 0x1241b2fb0> name=None at 1241b2c20> -> __attrs_4907671248
                __attrs_4907671248 = _static_4900728752

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a target="_blank"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4907669424
                __default_4907669424 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${python:prefix[1]}' (21:84)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1248506d0> -> __attr_href
                __token = 1074
                __token = 1076
                try:
                    __zt_tmp = __attrs_4907671248
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4427992992('python', 'prefix[1]', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
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
                __append('>')

                # <Interpolation value=<Substitution '${python:prefix[0]}' (21:105)> braces_required=True translation=False default='"?"' default_marker='"?"' at 124851fc0> -> __content_4353737008
                __token = 1095
                __token = 1097
                try:
                    __zt_tmp = __attrs_4907671248
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_4353737008 = _static_4427992992('python', 'prefix[0]', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
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
                __append('</a></li>')
                ____index_4900722464 -= 1
                if (____index_4900722464 > 0):
                    __append('\n            ')
            if (__backup_prefix_4899637136 is __marker):
                del econtext['prefix']
            else:
                econtext['prefix'] = __backup_prefix_4899637136
            __append('\n          </ul>\n        </div>\n    </div>\n</tal>\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }