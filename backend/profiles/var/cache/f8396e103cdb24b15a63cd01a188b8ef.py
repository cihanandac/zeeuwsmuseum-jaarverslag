# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/Products/Five/utilities/browser/edit_markers.pt'

__tokens = {803: ('request/ACTUAL_URL', 22, 33), 991: ('view/getInterfaceNames', 27, 34), 1141: ('interface/name', 30, 27), 1226: ('view/getDirectlyProvidedNames', 33, 34), 1416: ('interface/name', 36, 38), 1472: (' interface/nam', 37, 40), 1570: ('interface/name', 40, 27), 1648: ('view/getDirectlyProvidedNames', 43, 27), 2151: ('view/getAvailableInterfaceNames', 57, 34), 2340: ('interface/name', 60, 38), 2396: (' interface/nam', 61, 40), 2494: ('interface/name', 64, 27), 2629: ('view/getAvailableInterfaceNames', 67, 70), 23: ('context/@@standard_macros/page', 1, 23), 23: ('context/@@standard_macros/page', 1, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_4900346448 = 'page'
_static_4903358224 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'SAVE', 'value': 'Add', }
_static_4903359088 = {'class': 'zmi-controls form-group form-inline', }
_static_4903368496 = {'class': 'zmi-object-id', }
_static_4900796256 = {'type': 'checkbox', 'id': 'INTERFACE', 'name': 'add:list', 'value': 'interface/name', }
_static_4900795104 = {'class': 'zmi-object-check text-right', }
_static_4900795056 = {'class': 'table table-striped table-hover table-sm', }
_static_4900798128 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'SAVE', 'value': 'Remove', }
_static_4900786800 = {'class': 'zmi-controls', }
_static_4902087712 = {'class': 'zmi-object-check text-right', }
_static_4902083968 = {'class': 'zmi-object-id', }
_static_4902084256 = {'type': 'checkbox', 'id': 'INTERFACE', 'name': 'remove:list', 'value': 'interface/name', }
_static_4902092368 = {'class': 'zmi-object-check text-right', }
_static_4902085312 = {'class': 'zmi-object-id', }
_static_4902077392 = {'class': 'zmi-object-check text-right', }
_static_4900347072 = {'class': 'table table-striped table-hover table-sm', }
_static_4439051040 = __C2ZContextWrapper
_static_4439058528 = __compile_zt_expr
_static_4900346784 = {'action': '.', 'method': 'post', }
_static_4900342944 = {'class': 'form-help formHelp', }
_static_4438893776 = {}

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

    def render_heading(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900343232
            __attrs_4900343232 = _static_4438893776
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900355328
            __attrs_4900355328 = _static_4438893776

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1>')
            __stream_4900353744 = []
            __append_4900353744 = __stream_4900353744.append
            __append_4900353744('Assign Marker Interfaces')
            __msgid_4900353744 = __re_whitespace(''.join(__stream_4900353744)).strip()
            if 'heading_edit_marker':
                __append(translate('heading_edit_marker', mapping=None, default=__msgid_4900353744, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h1>\n  ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_main(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900355952
            __attrs_4900355952 = _static_4438893776
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x124154ca0> name=None at 124154e20> -> __attrs_4900340160
            __attrs_4900340160 = _static_4900342944

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="form-help formHelp">')
            __stream_4900355280 = []
            __append_4900355280 = __stream_4900355280.append
            __append_4900355280('\n      Change the behavior of this object by adding or removing marker\n      interfaces. You can choose one or more interfaces to be added to the\n      list of provided interfaces for this object.\n      ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900351920
            __attrs_4900351920 = _static_4438893776

            # <br ... (0:0)
            # --------------------------------------------------------
            __append_4900355280('<br />\n      A marker interface is used to identify an instance of a piece of\n      content. This allows you to enable and disable views based on marker\n      interfaces for example.\n    ')
            __msgid_4900355280 = __re_whitespace(''.join(__stream_4900355280)).strip()
            if __msgid_4900355280:
                __append(translate(__msgid_4900355280, mapping=None, default=__msgid_4900355280, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n    \n    ')

            # <Static value=<ast.Dict object at 0x124155ba0> name=None at 124155570> -> __attrs_4900342656
            __attrs_4900342656 = _static_4900346784

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form')

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900341984
            __default_4900341984 = _DEFAULT_MARKER

            # <Substitution 'request/ACTUAL_URL' (22:33)> -> __attr_action
            __token = 803
            try:
                __zt_tmp = __attrs_4900342656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_4439058528('path', 'request/ACTUAL_URL', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', '.', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append(' method="post">\n\n      ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900354848
            __attrs_4900354848 = _static_4438893776

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3>')
            __stream_4900353264 = []
            __append_4900353264 = __stream_4900353264.append
            __append_4900353264('Provided interfaces')
            __msgid_4900353264 = __re_whitespace(''.join(__stream_4900353264)).strip()
            if 'legend_provided':
                __append(translate('legend_provided', mapping=None, default=__msgid_4900353264, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h3>\n\n      ')

            # <Static value=<ast.Dict object at 0x124155cc0> name=None at 124155180> -> __attrs_4902084976
            __attrs_4902084976 = _static_4900347072

            # <table ... (0:0)
            # --------------------------------------------------------
            __append('<table class="table table-striped table-hover table-sm">\n        ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4902077632
            __attrs_4902077632 = _static_4438893776
            __backup_interface_4840695280 = get('interface', __marker)

            # <Value 'view/getInterfaceNames' (27:34)> -> __iterator
            __token = 991
            try:
                __zt_tmp = __attrs_4902077632
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4439058528('path', 'view/getInterfaceNames', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            (__iterator, ____index_4902082288, ) = getname('repeat')('interface', __iterator)
            econtext['interface'] = None
            for __item in __iterator:
                econtext['interface'] = __item

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n          ')

                # <Static value=<ast.Dict object at 0x1242fc3d0> name=None at 1242ff3d0> -> __attrs_4902087616
                __attrs_4902087616 = _static_4902077392

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-check text-right">&nbsp;</td>\n          ')

                # <Static value=<ast.Dict object at 0x1242fe2c0> name=None at 1242fecb0> -> __attrs_4902089968
                __attrs_4902089968 = _static_4902085312

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-id">')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4902081856
                __default_4902081856 = _DEFAULT_MARKER

                # <Value 'interface/name' (30:27)> -> __cache_4902084640
                __token = 1141
                try:
                    __zt_tmp = __attrs_4902089968
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4902084640 = _static_4439058528('path', 'interface/name', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'interface/name' (30:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1242ff040> -> __condition
                __expression = __cache_4902084640

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Interface Name')
                else:
                    __content = __cache_4902084640
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</td>\n        </tr>')
                ____index_4902082288 -= 1
                if (____index_4902082288 > 0):
                    __append('\n        ')
            if (__backup_interface_4840695280 is __marker):
                del econtext['interface']
            else:
                econtext['interface'] = __backup_interface_4840695280
            __append('\n\n        ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4902082768
            __attrs_4902082768 = _static_4438893776
            __backup_interface_4840688896 = get('interface', __marker)

            # <Value 'view/getDirectlyProvidedNames' (33:34)> -> __iterator
            __token = 1226
            try:
                __zt_tmp = __attrs_4902082768
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4439058528('path', 'view/getDirectlyProvidedNames', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            (__iterator, ____index_4902090160, ) = getname('repeat')('interface', __iterator)
            econtext['interface'] = None
            for __item in __iterator:
                econtext['interface'] = __item

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n          ')

                # <Static value=<ast.Dict object at 0x1242ffe50> name=None at 1242fe9e0> -> __attrs_4902080848
                __attrs_4902080848 = _static_4902092368

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-check text-right">\n            ')

                # <Static value=<ast.Dict object at 0x1242fdea0> name=None at 1242ff730> -> __attrs_4902083440
                __attrs_4902083440 = _static_4902084256

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="checkbox"')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4902092224
                __default_4902092224 = _DEFAULT_MARKER

                # <Substitution 'interface/name' (36:38)> -> __attr_id
                __token = 1416
                try:
                    __zt_tmp = __attrs_4902083440
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_4439058528('path', 'interface/name', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', 'INTERFACE', _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))
                __append(' name="remove:list"')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4902081760
                __default_4902081760 = _DEFAULT_MARKER

                # <Substitution 'interface/name' (37:40)> -> __attr_value
                __token = 1472
                try:
                    __zt_tmp = __attrs_4902083440
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4439058528('path', 'interface/name', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append('/>\n          </td>\n          ')

                # <Static value=<ast.Dict object at 0x1242fdd80> name=None at 1242fe740> -> __attrs_4902079936
                __attrs_4902079936 = _static_4902083968

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-id">')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4902078640
                __default_4902078640 = _DEFAULT_MARKER

                # <Value 'interface/name' (40:27)> -> __cache_4902078064
                __token = 1570
                try:
                    __zt_tmp = __attrs_4902079936
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4902078064 = _static_4439058528('path', 'interface/name', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'interface/name' (40:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1242fe110> -> __condition
                __expression = __cache_4902078064

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Interface Name')
                else:
                    __content = __cache_4902078064
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</td>\n        </tr>')
                ____index_4902090160 -= 1
                if (____index_4902090160 > 0):
                    __append('\n        ')
            if (__backup_interface_4840688896 is __marker):
                del econtext['interface']
            else:
                econtext['interface'] = __backup_interface_4840688896
            __append('\n\n        ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4902083488
            __attrs_4902083488 = _static_4438893776

            # <Value 'view/getDirectlyProvidedNames' (43:27)> -> __condition
            __token = 1648
            try:
                __zt_tmp = __attrs_4902083488
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4439058528('path', 'view/getDirectlyProvidedNames', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            if __condition:

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n          ')

                # <Static value=<ast.Dict object at 0x1242fec20> name=None at 1242ff490> -> __attrs_4902087664
                __attrs_4902087664 = _static_4902087712

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-check text-right">&nbsp;</td>\n          ')

                # <Static value=<ast.Dict object at 0x1241c1270> name=None at 1241c3d60> -> __attrs_4900791792
                __attrs_4900791792 = _static_4900786800

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-controls">\n            ')

                # <Static value=<ast.Dict object at 0x1241c3eb0> name=None at 1241c03a0> -> __attrs_4900787664
                __attrs_4900787664 = _static_4900798128

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="btn btn-primary" type="submit" name="SAVE"')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900789776
                __default_4900789776 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x1241c2d70> at 1241c0430> -> __attr_value
                __attr_value = 'Remove'
                __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append('/>\n          </td>\n        </tr>')
            __append('\n      </table>\n\n      ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900786608
            __attrs_4900786608 = _static_4438893776

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3>')
            __stream_4900782960 = []
            __append_4900782960 = __stream_4900782960.append
            __append_4900782960('\n        Available Marker Interfaces\n      ')
            __msgid_4900782960 = __re_whitespace(''.join(__stream_4900782960)).strip()
            if 'legend_available_marker':
                __append(translate('legend_available_marker', mapping=None, default=__msgid_4900782960, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h3>\n\n      ')

            # <Static value=<ast.Dict object at 0x1241c32b0> name=None at 1241c31c0> -> __attrs_4900789296
            __attrs_4900789296 = _static_4900795056

            # <table ... (0:0)
            # --------------------------------------------------------
            __append('<table class="table table-striped table-hover table-sm">\n        ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900796688
            __attrs_4900796688 = _static_4438893776
            __backup_interface_4638269472 = get('interface', __marker)

            # <Value 'view/getAvailableInterfaceNames' (57:34)> -> __iterator
            __token = 2151
            try:
                __zt_tmp = __attrs_4900796688
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4439058528('path', 'view/getAvailableInterfaceNames', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            (__iterator, ____index_4900796592, ) = getname('repeat')('interface', __iterator)
            econtext['interface'] = None
            for __item in __iterator:
                econtext['interface'] = __item

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n          ')

                # <Static value=<ast.Dict object at 0x1241c32e0> name=None at 1241c2a70> -> __attrs_4900785264
                __attrs_4900785264 = _static_4900795104

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-check text-right">\n            ')

                # <Static value=<ast.Dict object at 0x1241c3760> name=None at 1241c36d0> -> __attrs_4903354480
                __attrs_4903354480 = _static_4900796256

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="checkbox"')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900791168
                __default_4900791168 = _DEFAULT_MARKER

                # <Substitution 'interface/name' (60:38)> -> __attr_id
                __token = 2340
                try:
                    __zt_tmp = __attrs_4903354480
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_4439058528('path', 'interface/name', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', 'INTERFACE', _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))
                __append(' name="add:list"')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900785120
                __default_4900785120 = _DEFAULT_MARKER

                # <Substitution 'interface/name' (61:40)> -> __attr_value
                __token = 2396
                try:
                    __zt_tmp = __attrs_4903354480
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4439058528('path', 'interface/name', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append('/>\n          </td>\n          ')

                # <Static value=<ast.Dict object at 0x124437730> name=None at 124434c70> -> __attrs_4903359904
                __attrs_4903359904 = _static_4903368496

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-id">')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4903365328
                __default_4903365328 = _DEFAULT_MARKER

                # <Value 'interface/name' (64:27)> -> __cache_4903367680
                __token = 2494
                try:
                    __zt_tmp = __attrs_4903359904
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4903367680 = _static_4439058528('path', 'interface/name', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'interface/name' (64:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1244376a0> -> __condition
                __expression = __cache_4903367680

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Interface Name')
                else:
                    __content = __cache_4903367680
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</td>\n        </tr>')
                ____index_4900796592 -= 1
                if (____index_4900796592 > 0):
                    __append('\n        ')
            if (__backup_interface_4638269472 is __marker):
                del econtext['interface']
            else:
                econtext['interface'] = __backup_interface_4638269472
            __append('\n      </table>\n      ')

            # <Static value=<ast.Dict object at 0x124435270> name=None at 124435300> -> __attrs_4903361344
            __attrs_4903361344 = _static_4903359088

            # <Value 'view/getAvailableInterfaceNames' (67:70)> -> __condition
            __token = 2629
            try:
                __zt_tmp = __attrs_4903361344
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4439058528('path', 'view/getAvailableInterfaceNames', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="zmi-controls form-group form-inline">\n            ')

                # <Static value=<ast.Dict object at 0x124434f10> name=None at 124434d90> -> __attrs_4903361728
                __attrs_4903361728 = _static_4903358224

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="btn btn-primary" type="submit" name="SAVE"')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4903357216
                __default_4903357216 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x124437490> at 124436680> -> __attr_value
                __attr_value = 'Add'
                __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append('/>\n      </div>')
            __append('\n    </form>\n  ')
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900355760
            __attrs_4900355760 = _static_4438893776
            __backup_macroname_4903636288 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x124155a50> name=None at 124154100> -> __value
            __value = _static_4900346448
            econtext['macroname'] = __value

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900355184
                __attrs_4900355184 = _static_4438893776
                __append('\n\n  ')
                __token = None
                render_heading(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n  \n  ')
                __token = None
                render_main(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n')
            _slots = econtext['__slot_body'] = _deque((__fill_body, ))

            # <Value 'context/@@standard_macros/page' (1:23)> -> __macro
            __token = 23
            try:
                __zt_tmp = __attrs_4900355760
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4439058528('path', 'context/@@standard_macros/page', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __token = 23
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4903636288 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4903636288
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_heading': render_heading, 'render_main': render_main, 'render': render, }