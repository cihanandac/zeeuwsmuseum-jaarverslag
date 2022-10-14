# -*- coding: utf-8 -*-
__filename = 'manage_editProtocolMappingForm'

__tokens = {27: ('here/manage_page_header', 1, 27), 108: ('request/manage_tabs_message | nothing', 3, 43), 165: (' string:Challenge Protocol Mappin', 4, 18), 228: ('here/manage_tabs', 5, 27), 319: ('options/info', 9, 28), 671: ('info', 22, 28), 738: ('entry/label', 25, 25), 945: ('string:mapping.${entry/label}:list:record', 32, 35), 1116: ('entry/settings', 36, 40), 1227: ('protocol/selected', 38, 43), 1277: (' protocol/valu', 39, 31), 1168: ('protocol/label', 37, 35), 1643: ('here/manage_page_footer', 61, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_5110214336 = {'type': 'submit', 'class': 'btn btn-primary', 'value': ' Update Mapping ', }
_static_5110216112 = {'colspan': '2', }
_static_5110217888 = {'selected': 'protocol/selected', 'value': 'protocol/value', }
_static_5110168448 = {'name': 'mapping.name:record:list', 'class': 'form-control', 'type': 'multiple', 'multiple': 'multiple', 'size': '3', }
_static_5110163168 = {'class': 'zmi-object-id', }
_static_5110160336 = {'class': 'zmi-object-id', }
_static_5110159664 = {'scope': 'col', 'class': 'zmi-object-id', }
_static_5110158032 = {'scope': 'col', 'class': 'zmi-object-id', }
_static_5110153424 = {'class': 'table table-striped table-hover table-sm', }
_static_5110157168 = {'action': 'manage_updateProtocolMapping', 'method': 'POST', }
_static_4961559520 = {'class': 'container-fluid', }
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

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961556256
            __attrs_4961556256 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961557504
            __default_4961557504 = _DEFAULT_MARKER

            # <Value 'here/manage_page_header' (1:27)> -> __cache_4932533840
            __token = 27
            try:
                __zt_tmp = __attrs_4961556256
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4932533840 = _static_4427992992('path', 'here/manage_page_header', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_page_header' (1:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 127bb6050> -> __condition
            __expression = __cache_4932533840

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>Header</h1>')
            else:
                __content = __cache_4932533840
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961556208
            __attrs_4961556208 = _static_4428767312

            # <Value 'request/manage_tabs_message | nothing' (3:43)> -> __value
            __token = 108
            try:
                __zt_tmp = __attrs_4961556208
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'request/manage_tabs_message | nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['manage_tabs_message'] = __value
            rcontext['manage_tabs_message'] = __value
            __backup_form_title_4961591088 = get('form_title', __marker)

            # <Value 'string:Challenge Protocol Mapping' (4:18)> -> __value
            __token = 165
            try:
                __zt_tmp = __attrs_4961556208
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('string', 'Challenge Protocol Mapping', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['form_title'] = __value

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961552512
            __default_4961552512 = _DEFAULT_MARKER

            # <Value 'here/manage_tabs' (5:27)> -> __cache_4961564128
            __token = 228
            try:
                __zt_tmp = __attrs_4961556208
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4961564128 = _static_4427992992('path', 'here/manage_tabs', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_tabs' (5:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 127bb7dc0> -> __condition
            __expression = __cache_4961564128

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2> TABS </h2>')
            else:
                __content = __cache_4961564128
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            if (__backup_form_title_4961591088 is __marker):
                del econtext['form_title']
            else:
                econtext['form_title'] = __backup_form_title_4961591088
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x127bb63e0> name=None at 127bb4c40> -> __attrs_4961552704
            __attrs_4961552704 = _static_4961559520

            # <main ... (0:0)
            # --------------------------------------------------------
            __append('<main class="container-fluid">\n\n')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961559664
            __attrs_4961559664 = _static_4428767312
            __backup_info_4961538288 = get('info', __marker)

            # <Value 'options/info' (9:28)> -> __value
            __token = 319
            try:
                __zt_tmp = __attrs_4961559664
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'options/info', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['info'] = __value
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961556736
            __attrs_4961556736 = _static_4428767312

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3> Protocol Mapping </h3>\n\n  ')

            # <Static value=<ast.Dict object at 0x13096cf70> name=None at 13096c040> -> __attrs_5110156784
            __attrs_5110156784 = _static_5110157168

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form action="manage_updateProtocolMapping" method="POST">\n\n    ')

            # <Static value=<ast.Dict object at 0x13096c0d0> name=None at 13096c940> -> __attrs_5110154288
            __attrs_5110154288 = _static_5110153424

            # <table ... (0:0)
            # --------------------------------------------------------
            __append('<table class="table table-striped table-hover table-sm">\n\n      ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5110153664
            __attrs_5110153664 = _static_4428767312

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append('<tr>\n        ')

            # <Static value=<ast.Dict object at 0x13096d2d0> name=None at 13096c670> -> __attrs_5110161728
            __attrs_5110161728 = _static_5110158032

            # <th ... (0:0)
            # --------------------------------------------------------
            __append('<th scope="col" class="zmi-object-id"> Request Type </th>\n        ')

            # <Static value=<ast.Dict object at 0x13096d930> name=None at 13096df00> -> __attrs_5110159568
            __attrs_5110159568 = _static_5110159664

            # <th ... (0:0)
            # --------------------------------------------------------
            __append('<th scope="col" class="zmi-object-id"> Protocols </th>\n      </tr>\n\n      ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5110163552
            __attrs_5110163552 = _static_4428767312
            __backup_entry_4960598048 = get('entry', __marker)

            # <Value 'info' (22:28)> -> __iterator
            __token = 671
            try:
                __zt_tmp = __attrs_5110163552
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4427992992('path', 'info', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            (__iterator, ____index_5110160528, ) = getname('repeat')('entry', __iterator)
            econtext['entry'] = None
            for __item in __iterator:
                econtext['entry'] = __item

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n\n        ')

                # <Static value=<ast.Dict object at 0x13096dbd0> name=None at 13096e590> -> __attrs_5110163696
                __attrs_5110163696 = _static_5110160336

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-id">')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5110159376
                __default_5110159376 = _DEFAULT_MARKER

                # <Value 'entry/label' (25:25)> -> __cache_5110164272
                __token = 738
                try:
                    __zt_tmp = __attrs_5110163696
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_5110164272 = _static_4427992992('path', 'entry/label', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'entry/label' (25:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 13096ec50> -> __condition
                __expression = __cache_5110164272

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n          Request Type\n        ')
                else:
                    __content = __cache_5110164272
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</td>\n\n        ')

                # <Static value=<ast.Dict object at 0x13096e6e0> name=None at 13096e710> -> __attrs_5110154144
                __attrs_5110154144 = _static_5110163168

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-id">\n          ')

                # <Static value=<ast.Dict object at 0x13096fb80> name=None at 13096ff70> -> __attrs_5110168880
                __attrs_5110168880 = _static_5110168448

                # <select ... (0:0)
                # --------------------------------------------------------
                __append('<select')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5110168400
                __default_5110168400 = _DEFAULT_MARKER

                # <Substitution 'string:mapping.${entry/label}:list:record' (32:35)> -> __attr_name
                __token = 945
                try:
                    __zt_tmp = __attrs_5110168880
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_4427992992('string', 'mapping.${entry/label}:list:record', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', 'mapping.name:record:list', _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((' name="%s"' % __attr_name))
                __append(' class="form-control" type="multiple" multiple="multiple" size="3">\n            ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5110162400
                __attrs_5110162400 = _static_4428767312
                __backup_protocol_4961053248 = get('protocol', __marker)

                # <Value 'entry/settings' (36:40)> -> __iterator
                __token = 1116
                try:
                    __zt_tmp = __attrs_5110162400
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4427992992('path', 'entry/settings', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                (__iterator, ____index_5110162304, ) = getname('repeat')('protocol', __iterator)
                econtext['protocol'] = None
                for __item in __iterator:
                    econtext['protocol'] = __item
                    __append('\n              ')

                    # <Static value=<ast.Dict object at 0x13097bca0> name=None at 13097bc70> -> __attrs_5110217264
                    __attrs_5110217264 = _static_5110217888

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append('<option')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5110218320
                    __default_5110218320 = _DEFAULT_MARKER

                    # <Boolean 'protocol/selected' (38:43)> -> __attr_selected
                    __token = 1227
                    try:
                        __zt_tmp = __attrs_5110217264
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_selected = _static_4427992992('path', 'protocol/selected', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if (__attr_selected is _DEFAULT_MARKER):
                        __attr_selected = None
                    else:
                        if __attr_selected:
                            __attr_selected = 'selected'
                        else:
                            __attr_selected = None
                    if (__attr_selected is not None):
                        __append((' selected="%s"' % __attr_selected))

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5110217792
                    __default_5110217792 = _DEFAULT_MARKER

                    # <Substitution 'protocol/value' (39:31)> -> __attr_value
                    __token = 1277
                    try:
                        __zt_tmp = __attrs_5110217264
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_4427992992('path', 'protocol/value', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5110166864
                    __default_5110166864 = _DEFAULT_MARKER

                    # <Value 'protocol/label' (37:35)> -> __cache_5110169552
                    __token = 1168
                    try:
                        __zt_tmp = __attrs_5110217264
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_5110169552 = _static_4427992992('path', 'protocol/label', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'protocol/label' (37:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 13096d570> -> __condition
                    __expression = __cache_5110169552

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                Protocol\n              ')
                    else:
                        __content = __cache_5110169552
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</option>\n            ')
                    ____index_5110162304 -= 1
                    if (____index_5110162304 > 0):
                        __append('')
                if (__backup_protocol_4961053248 is __marker):
                    del econtext['protocol']
                else:
                    econtext['protocol'] = __backup_protocol_4961053248
                __append('\n          </select>\n        </td>\n     </tr>')
                ____index_5110160528 -= 1
                if (____index_5110160528 > 0):
                    __append('\n      ')
            if (__backup_entry_4960598048 is __marker):
                del econtext['entry']
            else:
                econtext['entry'] = __backup_entry_4960598048
            __append('\n\n     ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5110154960
            __attrs_5110154960 = _static_4428767312

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append('<tr>\n       ')

            # <Static value=<ast.Dict object at 0x13097b5b0> name=None at 13097b580> -> __attrs_5110215728
            __attrs_5110215728 = _static_5110216112

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td colspan="2">\n         ')

            # <Static value=<ast.Dict object at 0x13097aec0> name=None at 13097ae90> -> __attrs_5110214000
            __attrs_5110214000 = _static_5110214336

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="submit" class="btn btn-primary" value=" Update Mapping " />\n       </td>\n      </tr>\n\n    </table>\n  </form>\n\n')
            if (__backup_info_4961538288 is __marker):
                del econtext['info']
            else:
                econtext['info'] = __backup_info_4961538288
            __append('\n\n</main>\n\n')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5110213376
            __attrs_5110213376 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5110213568
            __default_5110213568 = _DEFAULT_MARKER

            # <Value 'here/manage_page_footer' (61:27)> -> __cache_5110158224
            __token = 1643
            try:
                __zt_tmp = __attrs_5110213376
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_5110158224 = _static_4427992992('path', 'here/manage_page_footer', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_page_footer' (61:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 13097b2e0> -> __condition
            __expression = __cache_5110158224

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>Footer</h1>')
            else:
                __content = __cache_5110158224
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }