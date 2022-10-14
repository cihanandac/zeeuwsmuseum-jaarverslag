# -*- coding: utf-8 -*-
__filename = 'manage_activateInterfacesForm'

__tokens = {27: ('here/manage_page_header', 1, 27), 91: ('here/manage_tabs', 2, 27), 229: ('here/meta_type', 8, 21), 481: ('here/listInterfaces', 15, 30), 526: ('here/plugins/listPluginTypeInfo', 16, 23), 643: ('nocall:info/interface', 18, 30), 692: (" python:info['methods'][0", 19, 26), 753: ('e info/', 20, 33), 787: ('le info/ti', 21, 23), 826: ('ves python:here.plugins.listPlugins(interf', 22, 24), 897: ('_ids python:[x[0] for x in act', 23, 23), 952: ('  pau string:${here/plugins/absolute_url}/manage_p', 24, 18), 1033: ('python:here.testImplements(interface)', 25, 23), 1169: ('interface_name', 27, 33), 1207: (" python:here.getId() in act_ids and 'checked' or '", 28, 22), 1328: ('string:${pau}?plugin_type=${info/id}', 31, 32), 1396: ('title/title', 32, 29), 1446: ('method', 33, 31), 1665: ('here/manage_page_footer', 47, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_5109697648 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'submit', 'value': ' Update ', }
_static_4961623952 = {'href': '', }
_static_4961626016 = {'type': 'checkbox', 'name': 'interfaces:list', 'value': '', 'checked': "python:here.getId() in act_ids and 'checked' or ''", }
_static_4961619584 = {'align': 'left', 'valign': 'top', 'class': 'form-label', }
_static_4961630240 = {'cellspacing': '0', 'cellpadding': '2', 'border': '0', }
_static_5109672608 = {'type': 'hidden', 'name': 'interfaces:default', 'value': '', }
_static_5109661808 = {'action': 'manage_activateInterfaces', 'method': 'post', }
_static_5109676688 = {'class': 'form-help', }
_static_5109670448 = {'class': 'container-fluid', }
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
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

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109670400
            __attrs_5109670400 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109666416
            __default_5109666416 = _DEFAULT_MARKER

            # <Value 'here/manage_page_header' (1:27)> -> __cache_5109667520
            __token = 27
            try:
                __zt_tmp = __attrs_5109670400
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_5109667520 = _static_4427992992('path', 'here/manage_page_header', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_page_header' (1:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1308f5930> -> __condition
            __expression = __cache_5109667520

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>Header</h1>')
            else:
                __content = __cache_5109667520
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109672848
            __attrs_5109672848 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109672656
            __default_5109672656 = _DEFAULT_MARKER

            # <Value 'here/manage_tabs' (2:27)> -> __cache_5109673520
            __token = 91
            try:
                __zt_tmp = __attrs_5109672848
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_5109673520 = _static_4427992992('path', 'here/manage_tabs', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_tabs' (2:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1308f6590> -> __condition
            __expression = __cache_5109673520

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2> TABS </h2>')
            else:
                __content = __cache_5109673520
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x1308f6230> name=None at 1308f5c90> -> __attrs_5109674192
            __attrs_5109674192 = _static_5109670448

            # <main ... (0:0)
            # --------------------------------------------------------
            __append('<main class="container-fluid">\n\n')

            # <Static value=<ast.Dict object at 0x1308f7a90> name=None at 1308f7940> -> __attrs_5109676016
            __attrs_5109676016 = _static_5109676688

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="form-help">\n  Choose the functionality this\n  ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109677984
            __attrs_5109677984 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109671120
            __default_5109671120 = _DEFAULT_MARKER

            # <Value 'here/meta_type' (8:21)> -> __cache_5109670640
            __token = 229
            try:
                __zt_tmp = __attrs_5109677984
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_5109670640 = _static_4427992992('path', 'here/meta_type', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/meta_type' (8:21)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1308f7550> -> __condition
            __expression = __cache_5109670640

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span> Foo Plugin </span>')
            else:
                __content = __cache_5109670640
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('\n  will perform.\n</p>\n\n')

            # <Static value=<ast.Dict object at 0x1308f4070> name=None at 1308f7cd0> -> __attrs_5109671264
            __attrs_5109671264 = _static_5109661808

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form action="manage_activateInterfaces" method="post">\n')

            # <Static value=<ast.Dict object at 0x1308f6aa0> name=None at 1308f7ee0> -> __attrs_5109674384
            __attrs_5109674384 = _static_5109672608

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" name="interfaces:default" value=""/>\n')

            # <Static value=<ast.Dict object at 0x127bc7820> name=None at 127bc4550> -> __attrs_4961628752
            __attrs_4961628752 = _static_4961630240
            __backup_interfaces_4961552992 = get('interfaces', __marker)

            # <Value 'here/listInterfaces' (15:30)> -> __value
            __token = 481
            try:
                __zt_tmp = __attrs_4961628752
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'here/listInterfaces', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['interfaces'] = __value

            # <table ... (0:0)
            # --------------------------------------------------------
            __append('<table cellspacing="0" cellpadding="2" border="0">\n  ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961625440
            __attrs_4961625440 = _static_4428767312
            __backup_info_4960596848 = get('info', __marker)

            # <Value 'here/plugins/listPluginTypeInfo' (16:23)> -> __iterator
            __token = 526
            try:
                __zt_tmp = __attrs_4961625440
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4427992992('path', 'here/plugins/listPluginTypeInfo', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            (__iterator, ____index_4961628128, ) = getname('repeat')('info', __iterator)
            econtext['info'] = None
            for __item in __iterator:
                econtext['info'] = __item

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n    ')

                # <Static value=<ast.Dict object at 0x127bc4e80> name=None at 127bc7760> -> __attrs_4961620880
                __attrs_4961620880 = _static_4961619584
                __backup_interface_4961045616 = get('interface', __marker)

                # <Value 'nocall:info/interface' (18:30)> -> __value
                __token = 643
                try:
                    __zt_tmp = __attrs_4961620880
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('nocall', 'info/interface', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['interface'] = __value
                __backup_method_4960368960 = get('method', __marker)

                # <Value "python:info['methods'][0]" (19:26)> -> __value
                __token = 692
                try:
                    __zt_tmp = __attrs_4961620880
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', "info['methods'][0]", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['method'] = __value
                __backup_interface_name_4961557216 = get('interface_name', __marker)

                # <Value 'info/id' (20:33)> -> __value
                __token = 753
                try:
                    __zt_tmp = __attrs_4961620880
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'info/id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['interface_name'] = __value
                __backup_title_4927089744 = get('title', __marker)

                # <Value 'info/title' (21:23)> -> __value
                __token = 787
                try:
                    __zt_tmp = __attrs_4961620880
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'info/title', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['title'] = __value
                __backup_actives_4961541840 = get('actives', __marker)

                # <Value 'python:here.plugins.listPlugins(interface)' (22:24)> -> __value
                __token = 826
                try:
                    __zt_tmp = __attrs_4961620880
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'here.plugins.listPlugins(interface)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['actives'] = __value
                __backup_act_ids_4960118976 = get('act_ids', __marker)

                # <Value 'python:[x[0] for x in actives]' (23:23)> -> __value
                __token = 897
                try:
                    __zt_tmp = __attrs_4961620880
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', '[x[0] for x in actives]', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['act_ids'] = __value
                __backup_pau_4961553520 = get('pau', __marker)

                # <Value 'string:${here/plugins/absolute_url}/manage_plugins' (24:18)> -> __value
                __token = 952
                try:
                    __zt_tmp = __attrs_4961620880
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('string', '${here/plugins/absolute_url}/manage_plugins', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['pau'] = __value

                # <Value 'python:here.testImplements(interface)' (25:23)> -> __condition
                __token = 1033
                try:
                    __zt_tmp = __attrs_4961620880
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('python', 'here.testImplements(interface)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td align="left" valign="top" class="form-label">\n        ')

                    # <Static value=<ast.Dict object at 0x127bc67a0> name=None at 127bc6aa0> -> __attrs_4961629376
                    __attrs_4961629376 = _static_4961626016

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="checkbox" name="interfaces:list"')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961621552
                    __default_4961621552 = _DEFAULT_MARKER

                    # <Substitution 'interface_name' (27:33)> -> __attr_value
                    __token = 1169
                    try:
                        __zt_tmp = __attrs_4961629376
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_4427992992('path', 'interface_name', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961623424
                    __default_4961623424 = _DEFAULT_MARKER

                    # <Boolean "python:here.getId() in act_ids and 'checked' or ''" (28:22)> -> __attr_checked
                    __token = 1207
                    try:
                        __zt_tmp = __attrs_4961629376
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_checked = _static_4427992992('python', "here.getId() in act_ids and 'checked' or ''", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if (__attr_checked is _DEFAULT_MARKER):
                        __attr_checked = None
                    else:
                        if __attr_checked:
                            __attr_checked = 'checked'
                        else:
                            __attr_checked = None
                    if (__attr_checked is not None):
                        __append((' checked="%s"' % __attr_checked))
                    __append(' />&nbsp;\n        ')

                    # <Static value=<ast.Dict object at 0x127bc5f90> name=None at 127bc5f30> -> __attrs_4961622512
                    __attrs_4961622512 = _static_4961623952

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961624096
                    __default_4961624096 = _DEFAULT_MARKER

                    # <Substitution 'string:${pau}?plugin_type=${info/id}' (31:32)> -> __attr_href
                    __token = 1328
                    try:
                        __zt_tmp = __attrs_4961622512
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4427992992('string', '${pau}?plugin_type=${info/id}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append('>\n          ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961621888
                    __attrs_4961621888 = _static_4428767312

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961621840
                    __default_4961621840 = _DEFAULT_MARKER

                    # <Value 'title/title' (32:29)> -> __cache_4961625968
                    __token = 1396
                    try:
                        __zt_tmp = __attrs_4961621888
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4961625968 = _static_4427992992('path', 'title/title', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'title/title' (32:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 127bc58a0> -> __condition
                    __expression = __cache_4961625968

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span/>')
                    else:
                        __content = __cache_4961625968
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</a>\n        ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961628032
                    __attrs_4961628032 = _static_4428767312

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i>(')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109706000
                    __attrs_5109706000 = _static_4428767312

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109705472
                    __default_5109705472 = _DEFAULT_MARKER

                    # <Value 'method' (33:31)> -> __cache_4961618960
                    __token = 1446
                    try:
                        __zt_tmp = __attrs_5109706000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4961618960 = _static_4427992992('path', 'method', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'method' (33:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 127bc4250> -> __condition
                    __expression = __cache_4961618960

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span/>')
                    else:
                        __content = __cache_4961618960
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(')</i>\n    </td>')
                if (__backup_pau_4961553520 is __marker):
                    del econtext['pau']
                else:
                    econtext['pau'] = __backup_pau_4961553520
                if (__backup_act_ids_4960118976 is __marker):
                    del econtext['act_ids']
                else:
                    econtext['act_ids'] = __backup_act_ids_4960118976
                if (__backup_actives_4961541840 is __marker):
                    del econtext['actives']
                else:
                    econtext['actives'] = __backup_actives_4961541840
                if (__backup_title_4927089744 is __marker):
                    del econtext['title']
                else:
                    econtext['title'] = __backup_title_4927089744
                if (__backup_interface_name_4961557216 is __marker):
                    del econtext['interface_name']
                else:
                    econtext['interface_name'] = __backup_interface_name_4961557216
                if (__backup_method_4960368960 is __marker):
                    del econtext['method']
                else:
                    econtext['method'] = __backup_method_4960368960
                if (__backup_interface_4961045616 is __marker):
                    del econtext['interface']
                else:
                    econtext['interface'] = __backup_interface_4961045616
                __append('\n  </tr>')
                ____index_4961628128 -= 1
                if (____index_4961628128 > 0):
                    __append('\n  ')
            if (__backup_info_4960596848 is __marker):
                del econtext['info']
            else:
                econtext['info'] = __backup_info_4960596848
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109708592
            __attrs_5109708592 = _static_4428767312

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append('<tr>\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109700240
            __attrs_5109700240 = _static_4428767312

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>\n      ')

            # <Static value=<ast.Dict object at 0x1308fcc70> name=None at 1308fcc10> -> __attrs_5109697456
            __attrs_5109697456 = _static_5109697648

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="btn btn-primary" type="submit" name="submit" value=" Update " />\n    </td>\n  </tr>\n</table>')
            if (__backup_interfaces_4961552992 is __marker):
                del econtext['interfaces']
            else:
                econtext['interfaces'] = __backup_interfaces_4961552992
            __append('\n</form>\n\n</main>\n\n')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109698992
            __attrs_5109698992 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109697984
            __default_5109697984 = _DEFAULT_MARKER

            # <Value 'here/manage_page_footer' (47:27)> -> __cache_5109695680
            __token = 1665
            try:
                __zt_tmp = __attrs_5109698992
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_5109695680 = _static_4427992992('path', 'here/manage_page_footer', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_page_footer' (47:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1308fcd90> -> __condition
            __expression = __cache_5109695680

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>Footer</h1>')
            else:
                __content = __cache_5109695680
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }