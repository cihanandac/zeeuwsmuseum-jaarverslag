# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/z3cform/crud/crud-table.pt'

__tokens = {229: ('view/subforms', 6, 21), 267: ('view/label | nothing', 8, 21), 308: ('view/label', 9, 19), 384: ('view/status', 11, 47), 423: ('view/status', 12, 25), 510: ('view/getURL', 15, 56), 563: ('view/render_batch_navigation', 17, 38), 668: ('view/subforms', 19, 71), 716: ('python:len(rows) and rows[0] or None', 20, 32), 784: ('python:row1 is not None', 21, 30), 870: ('row1/getTitleWidgets', 23, 45), 930: (' row1/getNiceTitle', 24, 38), 986: ('widgetsForTitles', 25, 35), 1042: ('repeat/widget/index', 27, 36), 1163: ('widget/field/description', 29, 42), 1230: (" python: 'header-' + niceTitles[idx", 30, 41), 1096: ('python: niceTitles[idx]', 28, 33), 1391: ("python:widget.required and widget.mode == 'input'", 35, 35), 1583: ('view/subforms', 42, 33), 1638: ('row/render', 43, 39), 1791: ('view/actions/values', 50, 44), 1863: ('action/render', 51, 50)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4682800368 = {'type': 'submit', }
_static_4682793504 = {'class': 'action', }
_static_4682807088 = {'class': 'fieldRequired', }
_static_4682804544 = {'title': 'widget/field/description', 'class': "python: 'header-' + niceTitles[idx]", }
_static_4683044256 = {'class': 'table table-striped table-bordered', }
_static_4683043728 = {'action': '.', 'method': 'post', }
_static_4683052128 = {'class': 'alert alert-info', }
_static_4428767312 = {}
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
_static_4683044592 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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
            __append(' ')

            # <Static value=<ast.Dict object at 0x1172196f0> name=None at 11721a1d0> -> __attrs_4683052752
            __attrs_4683052752 = _static_4683044592

            # <Value 'view/subforms' (6:21)> -> __condition
            __token = 229
            try:
                __zt_tmp = __attrs_4683052752
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'view/subforms', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4683047808 = __i18n_domain
                __i18n_domain = 'plone.z3cform'
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4683053136
                __attrs_4683053136 = _static_4428767312

                # <Value 'view/label | nothing' (8:21)> -> __condition
                __token = 267
                try:
                    __zt_tmp = __attrs_4683053136
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'view/label | nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <h2 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h2>')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4683043248
                    __default_4683043248 = _DEFAULT_MARKER

                    # <Value 'view/label' (9:19)> -> __cache_4683054816
                    __token = 308
                    try:
                        __zt_tmp = __attrs_4683053136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4683054816 = _static_4427992992('path', 'view/label', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/label' (9:19)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 117219f30> -> __condition
                    __expression = __cache_4683054816

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Form title')
                    else:
                        __content = __cache_4683054816
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</h2>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x11721b460> name=None at 117219270> -> __attrs_4683049680
                __attrs_4683049680 = _static_4683052128

                # <Value 'view/status' (11:47)> -> __condition
                __token = 384
                try:
                    __zt_tmp = __attrs_4683049680
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'view/status', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-info">\n      ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4683050976
                    __attrs_4683050976 = _static_4428767312

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4683044544
                    __default_4683044544 = _DEFAULT_MARKER

                    # <Value 'view/status' (12:25)> -> __cache_4683045504
                    __token = 423
                    try:
                        __zt_tmp = __attrs_4683050976
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4683045504 = _static_4427992992('path', 'view/status', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/status' (12:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 11721b9d0> -> __condition
                    __expression = __cache_4683045504

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4683045504
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n  </div>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x117219390> name=None at 1172194e0> -> __attrs_4683038880
                __attrs_4683038880 = _static_4683043728

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4683045360
                __default_4683045360 = _DEFAULT_MARKER

                # <Substitution 'view/getURL' (15:56)> -> __attr_action
                __token = 510
                try:
                    __zt_tmp = __attrs_4683038880
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_action = _static_4427992992('path', 'view/getURL', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_action = __quote(__attr_action, '"', '&quot;', '.', _DEFAULT_MARKER)
                if (__attr_action is not None):
                    __append((' action="%s"' % __attr_action))
                __append(' method="post">\n\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4683041808
                __attrs_4683041808 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4683044976
                __default_4683044976 = _DEFAULT_MARKER

                # <Value 'view/render_batch_navigation' (17:38)> -> __cache_4683048000
                __token = 563
                try:
                    __zt_tmp = __attrs_4683041808
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4683048000 = _static_4427992992('path', 'view/render_batch_navigation', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/render_batch_navigation' (17:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 117218580> -> __condition
                __expression = __cache_4683048000

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4683048000
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x1172195a0> name=None at 11721a170> -> __attrs_4683053760
                __attrs_4683053760 = _static_4683044256
                __backup_rows_4676511408 = get('rows', __marker)

                # <Value 'view/subforms' (19:71)> -> __value
                __token = 668
                try:
                    __zt_tmp = __attrs_4683053760
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'view/subforms', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['rows'] = __value

                # <table ... (0:0)
                # --------------------------------------------------------
                __append('<table class="table table-striped table-bordered">\n        ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4683052368
                __attrs_4683052368 = _static_4428767312
                __backup_row1_4682892576 = get('row1', __marker)

                # <Value 'python:len(rows) and rows[0] or None' (20:32)> -> __value
                __token = 716
                try:
                    __zt_tmp = __attrs_4683052368
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'len(rows) and rows[0] or None', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['row1'] = __value

                # <Value 'python:row1 is not None' (21:30)> -> __condition
                __token = 784
                try:
                    __zt_tmp = __attrs_4683052368
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('python', 'row1 is not None', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <thead ... (0:0)
                    # --------------------------------------------------------
                    __append('<thead>\n          ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682806368
                    __attrs_4682806368 = _static_4428767312

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr>\n            ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682799648
                    __attrs_4682799648 = _static_4428767312
                    __backup_widgetsForTitles_4682901744 = get('widgetsForTitles', __marker)

                    # <Value 'row1/getTitleWidgets' (23:45)> -> __value
                    __token = 870
                    try:
                        __zt_tmp = __attrs_4682799648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4427992992('path', 'row1/getTitleWidgets', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    econtext['widgetsForTitles'] = __value
                    __backup_niceTitles_4682894592 = get('niceTitles', __marker)

                    # <Value 'row1/getNiceTitles' (24:38)> -> __value
                    __token = 930
                    try:
                        __zt_tmp = __attrs_4682799648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4427992992('path', 'row1/getNiceTitles', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    econtext['niceTitles'] = __value
                    __backup_widget_4682794704 = get('widget', __marker)

                    # <Value 'widgetsForTitles' (25:35)> -> __iterator
                    __token = 986
                    try:
                        __zt_tmp = __attrs_4682799648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_4427992992('path', 'widgetsForTitles', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    (__iterator, ____index_4682794944, ) = getname('repeat')('widget', __iterator)
                    econtext['widget'] = None
                    for __item in __iterator:
                        econtext['widget'] = __item

                        # <th ... (0:0)
                        # --------------------------------------------------------
                        __append('<th>\n\n              ')

                        # <Static value=<ast.Dict object at 0x1171ded40> name=None at 1171dec20> -> __attrs_4682799216
                        __attrs_4682799216 = _static_4682804544
                        __backup_idx_4680547728 = get('idx', __marker)

                        # <Value 'repeat/widget/index' (27:36)> -> __value
                        __token = 1042
                        try:
                            __zt_tmp = __attrs_4682799216
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4427992992('path', 'repeat/widget/index', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        econtext['idx'] = __value

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682800224
                        __default_4682800224 = _DEFAULT_MARKER

                        # <Substitution 'widget/field/description' (29:42)> -> __attr_title
                        __token = 1163
                        try:
                            __zt_tmp = __attrs_4682799216
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_4427992992('path', 'widget/field/description', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682805168
                        __default_4682805168 = _DEFAULT_MARKER

                        # <Substitution "python: 'header-' + niceTitles[idx]" (30:41)> -> __attr_class
                        __token = 1230
                        try:
                            __zt_tmp = __attrs_4682799216
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_4427992992('python', " 'header-' + niceTitles[idx]", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))
                        __append('>')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682796576
                        __default_4682796576 = _DEFAULT_MARKER

                        # <Value 'python: niceTitles[idx]' (28:33)> -> __cache_4682800608
                        __token = 1096
                        try:
                            __zt_tmp = __attrs_4682799216
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4682800608 = _static_4427992992('python', ' niceTitles[idx]', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value 'python: niceTitles[idx]' (28:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1171dcf70> -> __condition
                        __expression = __cache_4682800608

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n                Field\n              ')
                        else:
                            __content = __cache_4682800608
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>')
                        if (__backup_idx_4680547728 is __marker):
                            del econtext['idx']
                        else:
                            econtext['idx'] = __backup_idx_4680547728
                        __append('\n\n              ')

                        # <Static value=<ast.Dict object at 0x1171df730> name=None at 1171de8f0> -> __attrs_4682803104
                        __attrs_4682803104 = _static_4682807088

                        # <Value "python:widget.required and widget.mode == 'input'" (35:35)> -> __condition
                        __token = 1391
                        try:
                            __zt_tmp = __attrs_4682803104
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4427992992('python', "widget.required and widget.mode == 'input'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span class="fieldRequired">\n                *\n              </span>')
                        __append('\n            </th>')
                        ____index_4682794944 -= 1
                        if (____index_4682794944 > 0):
                            __append('\n            ')
                    if (__backup_widget_4682794704 is __marker):
                        del econtext['widget']
                    else:
                        econtext['widget'] = __backup_widget_4682794704
                    if (__backup_niceTitles_4682894592 is __marker):
                        del econtext['niceTitles']
                    else:
                        econtext['niceTitles'] = __backup_niceTitles_4682894592
                    if (__backup_widgetsForTitles_4682901744 is __marker):
                        del econtext['widgetsForTitles']
                    else:
                        econtext['widgetsForTitles'] = __backup_widgetsForTitles_4682901744
                    __append('\n          </tr>\n        </thead>')
                if (__backup_row1_4682892576 is __marker):
                    del econtext['row1']
                else:
                    econtext['row1'] = __backup_row1_4682892576
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682801856
                __attrs_4682801856 = _static_4428767312

                # <tbody ... (0:0)
                # --------------------------------------------------------
                __append('<tbody>\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682805264
                __attrs_4682805264 = _static_4428767312
                __backup_row_4682894976 = get('row', __marker)

                # <Value 'view/subforms' (42:33)> -> __iterator
                __token = 1583
                try:
                    __zt_tmp = __attrs_4682805264
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4427992992('path', 'view/subforms', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                (__iterator, ____index_4682797968, ) = getname('repeat')('row', __iterator)
                econtext['row'] = None
                for __item in __iterator:
                    econtext['row'] = __item
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682793216
                    __attrs_4682793216 = _static_4428767312

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr>')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682798208
                    __default_4682798208 = _DEFAULT_MARKER

                    # <Value 'row/render' (43:39)> -> __cache_4682796672
                    __token = 1638
                    try:
                        __zt_tmp = __attrs_4682793216
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4682796672 = _static_4427992992('path', 'row/render', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'row/render' (43:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1171dd420> -> __condition
                    __expression = __cache_4682796672

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n              ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682802720
                        __attrs_4682802720 = _static_4428767312

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td></td>\n            ')
                    else:
                        __content = __cache_4682796672
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</tr>\n          ')
                    ____index_4682797968 -= 1
                    if (____index_4682797968 > 0):
                        __append('')
                if (__backup_row_4682894976 is __marker):
                    del econtext['row']
                else:
                    econtext['row'] = __backup_row_4682894976
                __append('\n        </tbody>\n    </table>')
                if (__backup_rows_4676511408 is __marker):
                    del econtext['rows']
                else:
                    econtext['rows'] = __backup_rows_4676511408
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x1171dc220> name=None at 1171dcd30> -> __attrs_4682800032
                __attrs_4682800032 = _static_4682793504
                __backup_action_4682906208 = get('action', __marker)

                # <Value 'view/actions/values' (50:44)> -> __iterator
                __token = 1791
                try:
                    __zt_tmp = __attrs_4682800032
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4427992992('path', 'view/actions/values', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                (__iterator, ____index_4682797920, ) = getname('repeat')('action', __iterator)
                econtext['action'] = None
                for __item in __iterator:
                    econtext['action'] = __item

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="action">\n      ')

                    # <Static value=<ast.Dict object at 0x1171ddcf0> name=None at 1171dd900> -> __attrs_4682805888
                    __attrs_4682805888 = _static_4682800368

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682800320
                    __default_4682800320 = _DEFAULT_MARKER

                    # <Value 'action/render' (51:50)> -> __cache_4682807280
                    __token = 1863
                    try:
                        __zt_tmp = __attrs_4682805888
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4682807280 = _static_4427992992('path', 'action/render', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'action/render' (51:50)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1171de2f0> -> __condition
                    __expression = __cache_4682807280

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="submit" />')
                    else:
                        __content = __cache_4682807280
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n    </span>')
                    ____index_4682797920 -= 1
                    if (____index_4682797920 > 0):
                        __append('\n    ')
                if (__backup_action_4682906208 is __marker):
                    del econtext['action']
                else:
                    econtext['action'] = __backup_action_4682906208
                __append('\n\n  </form>\n\n')
                __i18n_domain = __previous_i18n_domain_4683047808
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }