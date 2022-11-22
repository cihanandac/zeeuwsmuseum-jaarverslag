# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/customerize/registrations.pt'

__tokens = {27: ('context/manage_page_header', 1, 27), 85: ('context/manage_tabs', 2, 27), 1295: ('python:view.getTemplateViewRegistrations(mangle=False)', 33, 29), 1377: ('iface/name', 34, 25), 1428: ('iface/views', 36, 27), 1506: ('info/customized', 38, 26), 1555: ('string:${info/customized}/manage_main', 39, 32), 1619: ('info/viewname', 40, 24), 1693: ('not: info/customized', 43, 26), 1747: ('info/customize_url', 44, 32), 1799: (' info/zptfil', 45, 32), 1839: ('info/viewname', 46, 24), 1895: ('string:(${info/type})', 48, 27), 2013: ('context/manage_page_footer', 55, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4717518016 = {'class': 'type', }
_static_4717515808 = {'href': '', 'title': 'info/zptfile', }
_static_4717513120 = {'href': '', 'class': 'customized', }
_static_4717342112 = {'class': 'customized', }
_static_4717340288 = {'class': 'form-help', }
_static_4716531040 = {'class': 'alert alert-danger', 'role': 'alert', }
_static_4716532384 = {'type': 'text/css', }
_static_4716535504 = {'class': 'container-fluid', }
_static_4499344832 = __C2ZContextWrapper
_static_4499146784 = __compile_zt_expr
_static_4499034784 = {}

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

            # <Static value=<ast.Dict object at 0x10c29d2a0> name=None at 10c29f580> -> __attrs_4716763488
            __attrs_4716763488 = _static_4499034784

            # <Symbol value=<DEFAULT> at 10c29d480> -> __default_4716763296
            __default_4716763296 = _DEFAULT_MARKER

            # <Value 'context/manage_page_header' (1:27)> -> __cache_4716762096
            __token = 27
            try:
                __zt_tmp = __attrs_4716763488
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4716762096 = _static_4499146784('path', 'context/manage_page_header', econtext=econtext)(_static_4499344832(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/manage_page_header' (1:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 10c29d480> at 119242500> -> __condition
            __expression = __cache_4716762096

            # <Symbol value=<DEFAULT> at 10c29d480> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 />')
            else:
                __content = __cache_4716762096
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')

            # <Static value=<ast.Dict object at 0x10c29d2a0> name=None at 10c29f580> -> __attrs_4716759360
            __attrs_4716759360 = _static_4499034784

            # <Symbol value=<DEFAULT> at 10c29d480> -> __default_4716764304
            __default_4716764304 = _DEFAULT_MARKER

            # <Value 'context/manage_tabs' (2:27)> -> __cache_4716766560
            __token = 85
            try:
                __zt_tmp = __attrs_4716759360
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4716766560 = _static_4499146784('path', 'context/manage_tabs', econtext=econtext)(_static_4499344832(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/manage_tabs' (2:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 10c29d480> at 119240b50> -> __condition
            __expression = __cache_4716766560

            # <Symbol value=<DEFAULT> at 10c29d480> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 />')
            else:
                __content = __cache_4716766560
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x119209ed0> name=None at 119209de0> -> __attrs_4716529120
            __attrs_4716529120 = _static_4716535504

            # <main ... (0:0)
            # --------------------------------------------------------
            __append('<main class="container-fluid">\n\n  ')

            # <Static value=<ast.Dict object at 0x1192092a0> name=None at 119209480> -> __attrs_4716532576
            __attrs_4716532576 = _static_4716532384

            # <style ... (0:0)
            # --------------------------------------------------------
            __append('<style type="text/css">\n    dd span.type {\n      color: #999;\n    }\n    .customized {\n      background-color: yellow;\n    }\n  </style>\n\n')

            # <Static value=<ast.Dict object at 0x119208d60> name=None at 119208b50> -> __attrs_4715278640
            __attrs_4715278640 = _static_4716531040

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="alert alert-danger" role="alert">\n  ATTENTION: beware using this tool.\n  Errors (e.g. ')

            # <Static value=<ast.Dict object at 0x10c29d2a0> name=None at 10c29f580> -> __attrs_4715280560
            __attrs_4715280560 = _static_4499034784

            # <code ... (0:0)
            # --------------------------------------------------------
            __append('<code>TypeError</code>, ')

            # <Static value=<ast.Dict object at 0x10c29d2a0> name=None at 10c29f580> -> __attrs_4714743744
            __attrs_4714743744 = _static_4499034784

            # <code ... (0:0)
            # --------------------------------------------------------
            __append('<code>Unauthorized</code> etc) may popup if some kinds of\n  ')

            # <Static value=<ast.Dict object at 0x10c29d2a0> name=None at 10c29f580> -> __attrs_4717336688
            __attrs_4717336688 = _static_4499034784

            # <code ... (0:0)
            # --------------------------------------------------------
            __append('<code>python:</code> expressions are used in the template.\n  This makes it impossible to customize those here (try z3c.jbot or regular zcml overrides instead).\n  The reason is that browser view templates are Chameleon Pagetemplates while items in portal_view_customization are Zope 2 templates.\n  The different security models underlying the two implementations may break rendering of thesite.\n  If that happens just delete the custom copy using the Contents tab above.\n</div>\n\n  ')

            # <Static value=<ast.Dict object at 0x1192ce680> name=None at 1192ce620> -> __attrs_4717340144
            __attrs_4717340144 = _static_4717340288

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="form-help">\n    The following list shows all registered (template-based) views\n    sorted by interface. Click one of the links to see the contents\n    of the view template and possibly customize it. Views that already\n    have been customized are ')

            # <Static value=<ast.Dict object at 0x1192ceda0> name=None at 1192ced40> -> __attrs_4717342400
            __attrs_4717342400 = _static_4717342112

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span class="customized">highlighted like\n    this</span>.\n  </p>\n\n  ')

            # <Static value=<ast.Dict object at 0x10c29d2a0> name=None at 10c29f580> -> __attrs_4717343072
            __attrs_4717343072 = _static_4499034784
            __backup_iface_4717340480 = get('iface', __marker)

            # <Value 'python:view.getTemplateViewRegistrations(mangle=False)' (33:29)> -> __iterator
            __token = 1295
            try:
                __zt_tmp = __attrs_4717343072
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4499146784('python', 'view.getTemplateViewRegistrations(mangle=False)', econtext=econtext)(_static_4499344832(econtext, __zt_tmp))
            (__iterator, ____index_4717342640, ) = getname('repeat')('iface', __iterator)
            econtext['iface'] = None
            for __item in __iterator:
                econtext['iface'] = __item

                # <article ... (0:0)
                # --------------------------------------------------------
                __append('<article>\n    ')

                # <Static value=<ast.Dict object at 0x10c29d2a0> name=None at 10c29f580> -> __attrs_4717344848
                __attrs_4717344848 = _static_4499034784

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>')

                # <Symbol value=<DEFAULT> at 10c29d480> -> __default_4717344272
                __default_4717344272 = _DEFAULT_MARKER

                # <Value 'iface/name' (34:25)> -> __cache_4717343792
                __token = 1377
                try:
                    __zt_tmp = __attrs_4717344848
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4717343792 = _static_4499146784('path', 'iface/name', econtext=econtext)(_static_4499344832(econtext, __zt_tmp))

                # <BinOp left=<Value 'iface/name' (34:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 10c29d480> at 1192cf4f0> -> __condition
                __expression = __cache_4717343792

                # <Symbol value=<DEFAULT> at 10c29d480> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4717343792
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</header>\n    ')

                # <Static value=<ast.Dict object at 0x10c29d2a0> name=None at 10c29f580> -> __attrs_4717345616
                __attrs_4717345616 = _static_4499034784

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul>\n      ')

                # <Static value=<ast.Dict object at 0x10c29d2a0> name=None at 10c29f580> -> __attrs_4717346624
                __attrs_4717346624 = _static_4499034784
                __backup_info_4716543472 = get('info', __marker)

                # <Value 'iface/views' (36:27)> -> __iterator
                __token = 1428
                try:
                    __zt_tmp = __attrs_4717346624
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4499146784('path', 'iface/views', econtext=econtext)(_static_4499344832(econtext, __zt_tmp))
                (__iterator, ____index_4717510864, ) = getname('repeat')('info', __iterator)
                econtext['info'] = None
                for __item in __iterator:
                    econtext['info'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li>\n        ')

                    # <Static value=<ast.Dict object at 0x1192f89a0> name=None at 1192f8610> -> __attrs_4717513456
                    __attrs_4717513456 = _static_4717513120

                    # <Value 'info/customized' (38:26)> -> __condition
                    __token = 1506
                    try:
                        __zt_tmp = __attrs_4717513456
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4499146784('path', 'info/customized', econtext=econtext)(_static_4499344832(econtext, __zt_tmp))
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Symbol value=<DEFAULT> at 10c29d480> -> __default_4717512640
                        __default_4717512640 = _DEFAULT_MARKER

                        # <Substitution 'string:${info/customized}/manage_main' (39:32)> -> __attr_href
                        __token = 1555
                        try:
                            __zt_tmp = __attrs_4717513456
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4499146784('string', '${info/customized}/manage_main', econtext=econtext)(_static_4499344832(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' class="customized">')

                        # <Symbol value=<DEFAULT> at 10c29d480> -> __default_4717511920
                        __default_4717511920 = _DEFAULT_MARKER

                        # <Value 'info/viewname' (40:24)> -> __cache_4717511440
                        __token = 1619
                        try:
                            __zt_tmp = __attrs_4717513456
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4717511440 = _static_4499146784('path', 'info/viewname', econtext=econtext)(_static_4499344832(econtext, __zt_tmp))

                        # <BinOp left=<Value 'info/viewname' (40:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 10c29d480> at 1192f83d0> -> __condition
                        __expression = __cache_4717511440

                        # <Symbol value=<DEFAULT> at 10c29d480> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n        ')
                        else:
                            __content = __cache_4717511440
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</a>')
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x1192f9420> name=None at 1192f90c0> -> __attrs_4717516288
                    __attrs_4717516288 = _static_4717515808

                    # <Value 'not: info/customized' (43:26)> -> __condition
                    __token = 1693
                    try:
                        __zt_tmp = __attrs_4717516288
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4499146784('not', ' info/customized', econtext=econtext)(_static_4499344832(econtext, __zt_tmp))
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Symbol value=<DEFAULT> at 10c29d480> -> __default_4717515472
                        __default_4717515472 = _DEFAULT_MARKER

                        # <Substitution 'info/customize_url' (44:32)> -> __attr_href
                        __token = 1747
                        try:
                            __zt_tmp = __attrs_4717516288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4499146784('path', 'info/customize_url', econtext=econtext)(_static_4499344832(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))

                        # <Symbol value=<DEFAULT> at 10c29d480> -> __default_4717514848
                        __default_4717514848 = _DEFAULT_MARKER

                        # <Substitution 'info/zptfile' (45:32)> -> __attr_title
                        __token = 1799
                        try:
                            __zt_tmp = __attrs_4717516288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_4499146784('path', 'info/zptfile', econtext=econtext)(_static_4499344832(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))
                        __append('>')

                        # <Symbol value=<DEFAULT> at 10c29d480> -> __default_4717514656
                        __default_4717514656 = _DEFAULT_MARKER

                        # <Value 'info/viewname' (46:24)> -> __cache_4717514176
                        __token = 1839
                        try:
                            __zt_tmp = __attrs_4717516288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4717514176 = _static_4499146784('path', 'info/viewname', econtext=econtext)(_static_4499344832(econtext, __zt_tmp))

                        # <BinOp left=<Value 'info/viewname' (46:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 10c29d480> at 1192f8e80> -> __condition
                        __expression = __cache_4717514176

                        # <Symbol value=<DEFAULT> at 10c29d480> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n        ')
                        else:
                            __content = __cache_4717514176
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</a>')
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x1192f9cc0> name=None at 1192f9cf0> -> __attrs_4717518400
                    __attrs_4717518400 = _static_4717518016

                    # <code ... (0:0)
                    # --------------------------------------------------------
                    __append('<code class="type">')

                    # <Symbol value=<DEFAULT> at 10c29d480> -> __default_4717517440
                    __default_4717517440 = _DEFAULT_MARKER

                    # <Value 'string:(${info/type})' (48:27)> -> __cache_4717516960
                    __token = 1895
                    try:
                        __zt_tmp = __attrs_4717518400
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4717516960 = _static_4499146784('string', '(${info/type})', econtext=econtext)(_static_4499344832(econtext, __zt_tmp))

                    # <BinOp left=<Value 'string:(${info/type})' (48:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 10c29d480> at 1192f9960> -> __condition
                    __expression = __cache_4717516960

                    # <Symbol value=<DEFAULT> at 10c29d480> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4717516960
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</code> ')

                    # <Static value=<ast.Dict object at 0x10c29d2a0> name=None at 10c29f580> -> __attrs_4717519072
                    __attrs_4717519072 = _static_4499034784

                    # <br ... (0:0)
                    # --------------------------------------------------------
                    __append('<br />\n      </li>')
                    ____index_4717510864 -= 1
                    if (____index_4717510864 > 0):
                        __append('\n      ')
                if (__backup_info_4716543472 is __marker):
                    del econtext['info']
                else:
                    econtext['info'] = __backup_info_4716543472
                __append('\n    </ul>\n  </article>')
                ____index_4717342640 -= 1
                if (____index_4717342640 > 0):
                    __append('\n  ')
            if (__backup_iface_4717340480 is __marker):
                del econtext['iface']
            else:
                econtext['iface'] = __backup_iface_4717340480
            __append('\n\n</main>\n\n')

            # <Static value=<ast.Dict object at 0x10c29d2a0> name=None at 10c29f580> -> __attrs_4717520080
            __attrs_4717520080 = _static_4499034784

            # <Symbol value=<DEFAULT> at 10c29d480> -> __default_4717519888
            __default_4717519888 = _DEFAULT_MARKER

            # <Value 'context/manage_page_footer' (55:27)> -> __cache_4717519408
            __token = 2013
            try:
                __zt_tmp = __attrs_4717520080
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4717519408 = _static_4499146784('path', 'context/manage_page_footer', econtext=econtext)(_static_4499344832(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/manage_page_footer' (55:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 10c29d480> at 1192fa2f0> -> __condition
            __expression = __cache_4717519408

            # <Symbol value=<DEFAULT> at 10c29d480> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 />')
            else:
                __content = __cache_4717519408
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }