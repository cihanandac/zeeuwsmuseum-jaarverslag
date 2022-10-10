# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/batching/batchnavigation.pt'

__tokens = {55: ('view/batch|nothing', 2, 35), 90: ('batch', 3, 15), 227: ('batch/multiple_pages', 8, 21), 308: ('nothing', 12, 28), 422: ('batch/has_previous', 15, 52), 475: ('python:view.make_link(batch.previouspage)', 16, 32), 714: ('batch/pagesize', 19, 59), 833: ('nothing', 24, 28), 941: ('batch/show_link_to_first', 27, 49), 1000: ('python:view.make_link(1)', 28, 32), 1091: ('nothing', 31, 28), 1217: ('batch/second_page_not_in_navlist', 34, 52), 1318: ('nothing', 38, 28), 1458: ('batch/previous_pages', 41, 33), 1568: ('python:view.make_link(pagenumber)', 43, 33), 1523: ('pagenumber', 42, 24), 1664: ('nothing', 46, 28), 1794: ('batch/navlist', 49, 70), 1855: ('batch/pagenumber', 50, 45), 1982: ('nothing', 54, 28), 2118: ('batch/next_pages', 57, 33), 2224: ('python:view.make_link(pagenumber)', 59, 33), 2179: ('pagenumber', 58, 24), 2320: ('nothing', 62, 28), 2446: ('batch/before_last_page_not_in_navlist', 65, 52), 2570: ('nothing', 69, 28), 2676: ('batch/show_link_to_last', 72, 48), 2734: ('python:view.make_link(batch.lastpage)', 73, 32), 2797: ('batch/lastpage', 74, 24), 2875: ('nothing', 77, 28), 2981: ('batch/has_next', 80, 48), 3030: ('python:view.make_link(batch.nextpage)', 81, 32), 3238: ('batch/next_item_count', 84, 66)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4678298512 = {'aria-hidden': 'true', }
_static_4678303264 = {'class': 'label', }
_static_4678296304 = {'class': 'page-link', 'href': 'python:view.make_link(batch.nextpage)', }
_static_4684996064 = {'class': 'page-item next', }
_static_4685003984 = {'class': 'page-link', 'href': 'python:view.make_link(batch.lastpage)', }
_static_4685000192 = {'class': 'page-item last', }
_static_4684991216 = {'class': 'page-link', }
_static_4684997696 = {'class': 'page-item disabled', }
_static_4684989824 = {'class': 'page-link', 'href': 'python:view.make_link(pagenumber)', }
_static_4685000240 = {'class': 'page-item', }
_static_4672571808 = {'class': 'sr-only', }
_static_4672572768 = {'class': 'page-link', }
_static_4684944368 = {'class': 'page-item active', 'aria-current': 'page', }
_static_4684946288 = {'class': 'page-link', 'href': 'python:view.make_link(pagenumber)', }
_static_4684945424 = {'class': 'page-item', }
_static_4684953680 = {'class': 'page-item disabled', }
_static_4684951328 = {'class': 'page-link', 'href': 'python:view.make_link(1)', }
_static_4684942160 = {'class': 'first page-item', }
_static_4676678080 = {'class': 'label', }
_static_4680546096 = {'aria-hidden': 'true', }
_static_4680544464 = {'class': 'page-link', 'href': 'python:view.make_link(batch.previouspage)', }
_static_4680535584 = {'class': 'page-item previous', }
_static_4680544896 = {'class': 'pagination', }
_static_4680533232 = {'class': 'd-flex justify-content-center', }
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

    def render_navigation(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680544128
            __attrs_4680544128 = _static_4428767312
            __backup_batch_4684940672 = get('batch', __marker)

            # <Value 'view/batch|nothing' (2:35)> -> __value
            __token = 55
            try:
                __zt_tmp = __attrs_4680544128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'view/batch|nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['batch'] = __value

            # <Value 'batch' (3:15)> -> __condition
            __token = 90
            try:
                __zt_tmp = __attrs_4680544128
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'batch', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x116fb44f0> name=None at 116fb49d0> -> __attrs_4680538656
                __attrs_4680538656 = _static_4680533232

                # <Value 'batch/multiple_pages' (8:21)> -> __condition
                __token = 227
                try:
                    __zt_tmp = __attrs_4680538656
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'batch/multiple_pages', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:
                    __previous_i18n_domain_4680533856 = __i18n_domain
                    __i18n_domain = 'plone'

                    # <nav ... (0:0)
                    # --------------------------------------------------------
                    __append('<nav class="d-flex justify-content-center">\n\n    ')

                    # <Static value=<ast.Dict object at 0x116fb7280> name=None at 116fb4460> -> __attrs_4680547632
                    __attrs_4680547632 = _static_4680544896

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="pagination">\n\n      ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680544320
                    __attrs_4680544320 = _static_4428767312

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680539088
                    __default_4680539088 = _DEFAULT_MARKER

                    # <Value 'nothing' (12:28)> -> __cache_4680544704
                    __token = 308
                    try:
                        __zt_tmp = __attrs_4680544320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4680544704 = _static_4427992992('path', 'nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (12:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116fb5f00> -> __condition
                    __expression = __cache_4680544704

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Previous page -->\n      ')
                    else:
                        __content = __cache_4680544704
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x116fb4e20> name=None at 116fb4640> -> __attrs_4680544416
                    __attrs_4680544416 = _static_4680535584

                    # <Value 'batch/has_previous' (15:52)> -> __condition
                    __token = 422
                    try:
                        __zt_tmp = __attrs_4680544416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('path', 'batch/has_previous', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item previous">\n        ')

                        # <Static value=<ast.Dict object at 0x116fb70d0> name=None at 116fb4c70> -> __attrs_4680545904
                        __attrs_4680545904 = _static_4680544464

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="page-link"')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680546576
                        __default_4680546576 = _DEFAULT_MARKER

                        # <Substitution 'python:view.make_link(batch.previouspage)' (16:32)> -> __attr_href
                        __token = 475
                        try:
                            __zt_tmp = __attrs_4680545904
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4427992992('python', 'view.make_link(batch.previouspage)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>\n          ')

                        # <Static value=<ast.Dict object at 0x116fb7730> name=None at 116fb5540> -> __attrs_4680543840
                        __attrs_4680543840 = _static_4680546096

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span aria-hidden="true">&lt;</span>\n          ')

                        # <Static value=<ast.Dict object at 0x116c071c0> name=None at 116c046a0> -> __attrs_4684942208
                        __attrs_4684942208 = _static_4676678080

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="label">')
                        __stream_4678711808_number = ''
                        __stream_4680547680 = []
                        __append_4680547680 = __stream_4680547680.append
                        __append_4680547680('\n            Previous ')
                        __stream_4678711808_number = []
                        __append_4678711808_number = __stream_4678711808_number.append

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4684942592
                        __attrs_4684942592 = _static_4428767312

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684944224
                        __default_4684944224 = _DEFAULT_MARKER

                        # <Value 'batch/pagesize' (19:59)> -> __cache_4684945760
                        __token = 714
                        try:
                            __zt_tmp = __attrs_4684942592
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4684945760 = _static_4427992992('path', 'batch/pagesize', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value 'batch/pagesize' (19:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1173e8850> -> __condition
                        __expression = __cache_4684945760

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append_4678711808_number('n')
                        else:
                            __content = __cache_4684945760
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_4678711808_number(__content)
                        __append_4680547680('${number}')
                        __stream_4678711808_number = ''.join(__stream_4678711808_number)
                        __append_4680547680(' items\n          ')
                        __msgid_4680547680 = __re_whitespace(''.join(__stream_4680547680)).strip()
                        if 'batch_previous_x_items':
                            __append(translate('batch_previous_x_items', mapping={'number': __stream_4678711808_number, }, default=__msgid_4680547680, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n        </a>\n      </li>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4684947632
                    __attrs_4684947632 = _static_4428767312

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684948304
                    __default_4684948304 = _DEFAULT_MARKER

                    # <Value 'nothing' (24:28)> -> __cache_4684944848
                    __token = 833
                    try:
                        __zt_tmp = __attrs_4684947632
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4684944848 = _static_4427992992('path', 'nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (24:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1173e90f0> -> __condition
                    __expression = __cache_4684944848

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- First page -->\n      ')
                    else:
                        __content = __cache_4684944848
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x1173e8b50> name=None at 1173ea2f0> -> __attrs_4684944320
                    __attrs_4684944320 = _static_4684942160

                    # <Value 'batch/show_link_to_first' (27:49)> -> __condition
                    __token = 941
                    try:
                        __zt_tmp = __attrs_4684944320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('path', 'batch/show_link_to_first', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="first page-item">\n        ')

                        # <Static value=<ast.Dict object at 0x1173eaf20> name=None at 1173eb1c0> -> __attrs_4684946576
                        __attrs_4684946576 = _static_4684951328

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="page-link"')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684951376
                        __default_4684951376 = _DEFAULT_MARKER

                        # <Substitution 'python:view.make_link(1)' (28:32)> -> __attr_href
                        __token = 1000
                        try:
                            __zt_tmp = __attrs_4684946576
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4427992992('python', 'view.make_link(1)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>1</a>\n      </li>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4684953872
                    __attrs_4684953872 = _static_4428767312

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684953344
                    __default_4684953344 = _DEFAULT_MARKER

                    # <Value 'nothing' (31:28)> -> __cache_4684953008
                    __token = 1091
                    try:
                        __zt_tmp = __attrs_4684953872
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4684953008 = _static_4427992992('path', 'nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (31:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1173eb640> -> __condition
                    __expression = __cache_4684953008

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Ellipsis after first item -->\n      ')
                    else:
                        __content = __cache_4684953008
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x1173eb850> name=None at 1173eba60> -> __attrs_4684952816
                    __attrs_4684952816 = _static_4684953680

                    # <Value 'batch/second_page_not_in_navlist' (34:52)> -> __condition
                    __token = 1217
                    try:
                        __zt_tmp = __attrs_4684952816
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('path', 'batch/second_page_not_in_navlist', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item disabled">\n        ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4684950224
                        __attrs_4684950224 = _static_4428767312

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>...</span>\n      </li>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4684955120
                    __attrs_4684955120 = _static_4428767312

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684952336
                    __default_4684952336 = _DEFAULT_MARKER

                    # <Value 'nothing' (38:28)> -> __cache_4684947776
                    __token = 1318
                    try:
                        __zt_tmp = __attrs_4684955120
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4684947776 = _static_4427992992('path', 'nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (38:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1173e8b20> -> __condition
                    __expression = __cache_4684947776

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Pagelist with links to previous pages for quick navigation -->\n      ')
                    else:
                        __content = __cache_4684947776
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x1173e9810> name=None at 1173ebd30> -> __attrs_4684943696
                    __attrs_4684943696 = _static_4684945424
                    __backup_pagenumber_4680436704 = get('pagenumber', __marker)

                    # <Value 'batch/previous_pages' (41:33)> -> __iterator
                    __token = 1458
                    try:
                        __zt_tmp = __attrs_4684943696
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_4427992992('path', 'batch/previous_pages', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    (__iterator, ____index_4684943168, ) = getname('repeat')('pagenumber', __iterator)
                    econtext['pagenumber'] = None
                    for __item in __iterator:
                        econtext['pagenumber'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item">\n        ')

                        # <Static value=<ast.Dict object at 0x1173e9b70> name=None at 1173e9de0> -> __attrs_4684943072
                        __attrs_4684943072 = _static_4684946288

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="page-link"')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684950416
                        __default_4684950416 = _DEFAULT_MARKER

                        # <Substitution 'python:view.make_link(pagenumber)' (43:33)> -> __attr_href
                        __token = 1568
                        try:
                            __zt_tmp = __attrs_4684943072
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4427992992('python', 'view.make_link(pagenumber)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684949360
                        __default_4684949360 = _DEFAULT_MARKER

                        # <Value 'pagenumber' (42:24)> -> __cache_4684952480
                        __token = 1523
                        try:
                            __zt_tmp = __attrs_4684943072
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4684952480 = _static_4427992992('path', 'pagenumber', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value 'pagenumber' (42:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1173ebfd0> -> __condition
                        __expression = __cache_4684952480

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4684952480
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</a>\n      </li>')
                        ____index_4684943168 -= 1
                        if (____index_4684943168 > 0):
                            __append('\n      ')
                    if (__backup_pagenumber_4680436704 is __marker):
                        del econtext['pagenumber']
                    else:
                        econtext['pagenumber'] = __backup_pagenumber_4680436704
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4678223184
                    __attrs_4678223184 = _static_4428767312

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678227312
                    __default_4678227312 = _DEFAULT_MARKER

                    # <Value 'nothing' (46:28)> -> __cache_4684940288
                    __token = 1664
                    try:
                        __zt_tmp = __attrs_4678223184
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4684940288 = _static_4427992992('path', 'nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (46:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116d81ff0> -> __condition
                    __expression = __cache_4684940288

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Active page -->\n      ')
                    else:
                        __content = __cache_4684940288
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x1173e93f0> name=None at 1173e9420> -> __attrs_4678225440
                    __attrs_4678225440 = _static_4684944368

                    # <Value 'batch/navlist' (49:70)> -> __condition
                    __token = 1794
                    try:
                        __zt_tmp = __attrs_4678225440
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('path', 'batch/navlist', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item active" aria-current="page">\n        ')

                        # <Static value=<ast.Dict object at 0x11681cd60> name=None at 11681cdc0> -> __attrs_4672570512
                        __attrs_4672570512 = _static_4672572768

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="page-link">')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678232112
                        __default_4678232112 = _DEFAULT_MARKER

                        # <Value 'batch/pagenumber' (50:45)> -> __cache_4678222944
                        __token = 1855
                        try:
                            __zt_tmp = __attrs_4672570512
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4678222944 = _static_4427992992('path', 'batch/pagenumber', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value 'batch/pagenumber' (50:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116d820e0> -> __condition
                        __expression = __cache_4678222944

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4678222944
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>\n        ')

                        # <Static value=<ast.Dict object at 0x11681c9a0> name=None at 11681fa00> -> __attrs_4684993472
                        __attrs_4684993472 = _static_4672571808

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="sr-only">')
                        __stream_4672581552 = []
                        __append_4672581552 = __stream_4672581552.append
                        __msgid_4672581552 = __re_whitespace(''.join(__stream_4672581552)).strip()
                        if '(current)':
                            __append(translate('(current)', mapping=None, default=__msgid_4672581552, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n      </li>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4684992560
                    __attrs_4684992560 = _static_4428767312

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684990976
                    __default_4684990976 = _DEFAULT_MARKER

                    # <Value 'nothing' (54:28)> -> __cache_4684992272
                    __token = 1982
                    try:
                        __zt_tmp = __attrs_4684992560
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4684992272 = _static_4427992992('path', 'nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (54:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1173f41c0> -> __condition
                    __expression = __cache_4684992272

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Pagelist with links to next pages for quick navigation -->\n      ')
                    else:
                        __content = __cache_4684992272
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x1173f6e30> name=None at 1173f43a0> -> __attrs_4684992080
                    __attrs_4684992080 = _static_4685000240
                    __backup_pagenumber_4682903856 = get('pagenumber', __marker)

                    # <Value 'batch/next_pages' (57:33)> -> __iterator
                    __token = 2118
                    try:
                        __zt_tmp = __attrs_4684992080
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_4427992992('path', 'batch/next_pages', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    (__iterator, ____index_4684988816, ) = getname('repeat')('pagenumber', __iterator)
                    econtext['pagenumber'] = None
                    for __item in __iterator:
                        econtext['pagenumber'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item">\n        ')

                        # <Static value=<ast.Dict object at 0x1173f4580> name=None at 1173f4460> -> __attrs_4685003024
                        __attrs_4685003024 = _static_4684989824

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="page-link"')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684993376
                        __default_4684993376 = _DEFAULT_MARKER

                        # <Substitution 'python:view.make_link(pagenumber)' (59:33)> -> __attr_href
                        __token = 2224
                        try:
                            __zt_tmp = __attrs_4685003024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4427992992('python', 'view.make_link(pagenumber)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684996016
                        __default_4684996016 = _DEFAULT_MARKER

                        # <Value 'pagenumber' (58:24)> -> __cache_4684996400
                        __token = 2179
                        try:
                            __zt_tmp = __attrs_4685003024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4684996400 = _static_4427992992('path', 'pagenumber', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value 'pagenumber' (58:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1173f4ca0> -> __condition
                        __expression = __cache_4684996400

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4684996400
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</a>\n      </li>')
                        ____index_4684988816 -= 1
                        if (____index_4684988816 > 0):
                            __append('\n      ')
                    if (__backup_pagenumber_4682903856 is __marker):
                        del econtext['pagenumber']
                    else:
                        econtext['pagenumber'] = __backup_pagenumber_4682903856
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4685003696
                    __attrs_4685003696 = _static_4428767312

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685003120
                    __default_4685003120 = _DEFAULT_MARKER

                    # <Value 'nothing' (62:28)> -> __cache_4685001488
                    __token = 2320
                    try:
                        __zt_tmp = __attrs_4685003696
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4685001488 = _static_4427992992('path', 'nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (62:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1173f7f70> -> __condition
                    __expression = __cache_4685001488

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Ellipsis before last item -->\n      ')
                    else:
                        __content = __cache_4685001488
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x1173f6440> name=None at 1173f7430> -> __attrs_4685001056
                    __attrs_4685001056 = _static_4684997696

                    # <Value 'batch/before_last_page_not_in_navlist' (65:52)> -> __condition
                    __token = 2446
                    try:
                        __zt_tmp = __attrs_4685001056
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('path', 'batch/before_last_page_not_in_navlist', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item disabled">\n        ')

                        # <Static value=<ast.Dict object at 0x1173f4af0> name=None at 1173f7280> -> __attrs_4684994624
                        __attrs_4684994624 = _static_4684991216

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="page-link">...</span>\n      </li>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4684993952
                    __attrs_4684993952 = _static_4428767312

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685001008
                    __default_4685001008 = _DEFAULT_MARKER

                    # <Value 'nothing' (69:28)> -> __cache_4684991600
                    __token = 2570
                    try:
                        __zt_tmp = __attrs_4684993952
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4684991600 = _static_4427992992('path', 'nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (69:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1173f74c0> -> __condition
                    __expression = __cache_4684991600

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Last page -->\n      ')
                    else:
                        __content = __cache_4684991600
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x1173f6e00> name=None at 1173f6a70> -> __attrs_4684996880
                    __attrs_4684996880 = _static_4685000192

                    # <Value 'batch/show_link_to_last' (72:48)> -> __condition
                    __token = 2676
                    try:
                        __zt_tmp = __attrs_4684996880
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('path', 'batch/show_link_to_last', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item last">\n        ')

                        # <Static value=<ast.Dict object at 0x1173f7cd0> name=None at 1173f7eb0> -> __attrs_4685002256
                        __attrs_4685002256 = _static_4685003984

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="page-link"')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685003648
                        __default_4685003648 = _DEFAULT_MARKER

                        # <Substitution 'python:view.make_link(batch.lastpage)' (73:32)> -> __attr_href
                        __token = 2734
                        try:
                            __zt_tmp = __attrs_4685002256
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4427992992('python', 'view.make_link(batch.lastpage)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685004752
                        __default_4685004752 = _DEFAULT_MARKER

                        # <Value 'batch/lastpage' (74:24)> -> __cache_4684999328
                        __token = 2797
                        try:
                            __zt_tmp = __attrs_4685002256
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4684999328 = _static_4427992992('path', 'batch/lastpage', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value 'batch/lastpage' (74:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1173f5120> -> __condition
                        __expression = __cache_4684999328

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4684999328
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</a>\n      </li>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4685000960
                    __attrs_4685000960 = _static_4428767312

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684998224
                    __default_4684998224 = _DEFAULT_MARKER

                    # <Value 'nothing' (77:28)> -> __cache_4685000144
                    __token = 2875
                    try:
                        __zt_tmp = __attrs_4685000960
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4685000144 = _static_4427992992('path', 'nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (77:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1173f5660> -> __condition
                    __expression = __cache_4685000144

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Next page -->\n      ')
                    else:
                        __content = __cache_4685000144
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x1173f5de0> name=None at 1173f4c40> -> __attrs_4678289008
                    __attrs_4678289008 = _static_4684996064

                    # <Value 'batch/has_next' (80:48)> -> __condition
                    __token = 2981
                    try:
                        __zt_tmp = __attrs_4678289008
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('path', 'batch/has_next', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item next">\n        ')

                        # <Static value=<ast.Dict object at 0x116d922f0> name=None at 116d93d00> -> __attrs_4678291216
                        __attrs_4678291216 = _static_4678296304

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="page-link"')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678301248
                        __default_4678301248 = _DEFAULT_MARKER

                        # <Substitution 'python:view.make_link(batch.nextpage)' (81:32)> -> __attr_href
                        __token = 3030
                        try:
                            __zt_tmp = __attrs_4678291216
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4427992992('python', 'view.make_link(batch.nextpage)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>\n          ')

                        # <Static value=<ast.Dict object at 0x116d93e20> name=None at 116d90ee0> -> __attrs_4678296256
                        __attrs_4678296256 = _static_4678303264

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="label">')
                        __stream_4678706432_number = ''
                        __stream_4678295680 = []
                        __append_4678295680 = __stream_4678295680.append
                        __append_4678295680('\n            Next\n            ')
                        __stream_4678706432_number = []
                        __append_4678706432_number = __stream_4678706432_number.append

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4678301632
                        __attrs_4678301632 = _static_4428767312

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678299568
                        __default_4678299568 = _DEFAULT_MARKER

                        # <Value 'batch/next_item_count' (84:66)> -> __cache_4678288576
                        __token = 3238
                        try:
                            __zt_tmp = __attrs_4678301632
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4678288576 = _static_4427992992('path', 'batch/next_item_count', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value 'batch/next_item_count' (84:66)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116d93850> -> __condition
                        __expression = __cache_4678288576

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append_4678706432_number('n')
                        else:
                            __content = __cache_4678288576
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_4678706432_number(__content)
                        __append_4678295680('${number}')
                        __stream_4678706432_number = ''.join(__stream_4678706432_number)
                        __append_4678295680('\n            items\n          ')
                        __msgid_4678295680 = __re_whitespace(''.join(__stream_4678295680)).strip()
                        if 'batch_next_x_items':
                            __append(translate('batch_next_x_items', mapping={'number': __stream_4678706432_number, }, default=__msgid_4678295680, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n          ')

                        # <Static value=<ast.Dict object at 0x116d92b90> name=None at 116d91e40> -> __attrs_4678287568
                        __attrs_4678287568 = _static_4678298512

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span aria-hidden="true">&gt;</span>\n        </a>\n      </li>')
                    __append('\n    </ul>\n\n  </nav>')
                    __i18n_domain = __previous_i18n_domain_4680533856
                __append('\n\n')
            if (__backup_batch_4684940672 is __marker):
                del econtext['batch']
            else:
                econtext['batch'] = __backup_batch_4684940672
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
            __append('<!-- Navigation -->\n')
            __token = None
            render_navigation(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_navigation': render_navigation, 'render': render, }