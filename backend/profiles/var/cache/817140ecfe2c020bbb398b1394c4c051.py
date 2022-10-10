# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/dexterity/browser/behaviors.pt'

__tokens = {53: ('view/status', 2, 42), 79: ('view/status', 2, 68), 154: ('request/getURL', 4, 54), 177: (' view/enctyp', 4, 77), 221: ('view/widgets/values|nothing', 5, 28), 298: ('widget/error', 8, 25), 337: (" python:widget.mode == 'hidden", 9, 25), 399: ("python:'mb-3 field' + (error and 'alert alert-warning' or '')", 10, 29), 538: ('python:widget.required and not hidden', 13, 25), 724: ('error', 19, 24), 754: ('error/render', 19, 54), 866: ('widget/render', 24, 48), 945: ('widget/field/description', 26, 32), 1054: ('python:description and not hidden', 29, 23), 1018: ('description', 28, 21), 1197: ('context/@@ploneform-macros/actions', 36, 32), 1197: ('context/@@ploneform-macros/actions', 36, 32)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4685211504 = 'actions'
_static_4685243744 = {'class': 'form-text', }
_static_4685245424 = {'type': 'text', }
_static_4685248640 = {'class': 'widget', }
_static_4685243792 = {'class': 'fieldRequired', 'title': 'Required', }
_static_4685205840 = {'class': 'field', }
_static_4685217216 = {'action': '.', 'method': 'post', 'enctype': 'view/enctype', }
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
_static_4685214336 = {'class': 'portalMessage', }
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

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4683053520
            __attrs_4683053520 = _static_4428767312
            __append('\n')

            # <Static value=<ast.Dict object at 0x11742b280> name=None at 11742b2b0> -> __attrs_4685213952
            __attrs_4685213952 = _static_4685214336

            # <Value 'view/status' (2:42)> -> __condition
            __token = 53
            try:
                __zt_tmp = __attrs_4685213952
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'view/status', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="portalMessage">')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685216736
                __default_4685216736 = _DEFAULT_MARKER

                # <Value 'view/status' (2:68)> -> __cache_4685212176
                __token = 79
                try:
                    __zt_tmp = __attrs_4685213952
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4685212176 = _static_4427992992('path', 'view/status', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/status' (2:68)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 11742b2e0> -> __condition
                __expression = __cache_4685212176

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4685212176
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</div>')
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x11742bdc0> name=None at 11742ba30> -> __attrs_4685215344
            __attrs_4685215344 = _static_4685217216

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685212224
            __default_4685212224 = _DEFAULT_MARKER

            # <Substitution 'request/getURL' (4:54)> -> __attr_action
            __token = 154
            try:
                __zt_tmp = __attrs_4685215344
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_4427992992('path', 'request/getURL', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', '.', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append(' method="post"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685212512
            __default_4685212512 = _DEFAULT_MARKER

            # <Substitution 'view/enctype' (4:77)> -> __attr_enctype
            __token = 177
            try:
                __zt_tmp = __attrs_4685215344
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_enctype = _static_4427992992('path', 'view/enctype', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_enctype = __quote(__attr_enctype, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_enctype is not None):
                __append((' enctype="%s"' % __attr_enctype))
            __append('>\n')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4685215440
            __attrs_4685215440 = _static_4428767312
            __backup_widget_4682708976 = get('widget', __marker)

            # <Value 'view/widgets/values|nothing' (5:28)> -> __iterator
            __token = 221
            try:
                __zt_tmp = __attrs_4685215440
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4427992992('path', 'view/widgets/values|nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            (__iterator, ____index_4685215920, ) = getname('repeat')('widget', __iterator)
            econtext['widget'] = None
            for __item in __iterator:
                econtext['widget'] = __item
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x117429150> name=None at 117429210> -> __attrs_4685206560
                __attrs_4685206560 = _static_4685205840
                __backup_error_4680546864 = get('error', __marker)

                # <Value 'widget/error' (8:25)> -> __value
                __token = 298
                try:
                    __zt_tmp = __attrs_4685206560
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'widget/error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['error'] = __value
                __backup_hidden_4685212704 = get('hidden', __marker)

                # <Value "python:widget.mode == 'hidden'" (9:25)> -> __value
                __token = 337
                try:
                    __zt_tmp = __attrs_4685206560
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', "widget.mode == 'hidden'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['hidden'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685205696
                __default_4685205696 = _DEFAULT_MARKER

                # <Substitution "python:'mb-3 field' + (error and 'alert alert-warning' or '')" (10:29)> -> __attr_class
                __token = 399
                try:
                    __zt_tmp = __attrs_4685206560
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_4427992992('python', "'mb-3 field' + (error and 'alert alert-warning' or '')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', 'field', _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append('>\n\n    ')

                # <Static value=<ast.Dict object at 0x117432590> name=None at 117428790> -> __attrs_4685235344
                __attrs_4685235344 = _static_4685243792

                # <Value 'python:widget.required and not hidden' (13:25)> -> __condition
                __token = 538
                try:
                    __zt_tmp = __attrs_4685235344
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('python', 'widget.required and not hidden', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="fieldRequired"')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685245040
                    __default_4685245040 = _DEFAULT_MARKER

                    # <Translate msgid='title_required' node=<ast.Constant object at 0x117433790> at 117432ec0> -> __attr_title
                    __attr_title = 'Required'
                    __attr_title = translate('title_required', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append('>')
                    __stream_4685201520 = []
                    __append_4685201520 = __stream_4685201520.append
                    __append_4685201520('\n      (Required)\n    ')
                    __msgid_4685201520 = __re_whitespace(''.join(__stream_4685201520)).strip()
                    if 'label_required':
                        __append(translate('label_required', mapping=None, default=__msgid_4685201520, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>')
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4685249648
                __attrs_4685249648 = _static_4428767312

                # <Value 'error' (19:24)> -> __condition
                __token = 724
                try:
                    __zt_tmp = __attrs_4685249648
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div>')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685249600
                    __default_4685249600 = _DEFAULT_MARKER

                    # <Value 'error/render' (19:54)> -> __cache_4685249792
                    __token = 754
                    try:
                        __zt_tmp = __attrs_4685249648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4685249792 = _static_4427992992('path', 'error/render', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'error/render' (19:54)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 117433970> -> __condition
                    __expression = __cache_4685249792

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n      Error\n    ')
                    else:
                        __content = __cache_4685249792
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>')
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x117433880> name=None at 117432a40> -> __attrs_4685248016
                __attrs_4685248016 = _static_4685248640

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="widget">\n      ')

                # <Static value=<ast.Dict object at 0x117432bf0> name=None at 117432b30> -> __attrs_4685247200
                __attrs_4685247200 = _static_4685245424

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685246912
                __default_4685246912 = _DEFAULT_MARKER

                # <Value 'widget/render' (24:48)> -> __cache_4685246624
                __token = 866
                try:
                    __zt_tmp = __attrs_4685247200
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4685246624 = _static_4427992992('path', 'widget/render', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'widget/render' (24:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 117433100> -> __condition
                __expression = __cache_4685246624

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="text" />')
                else:
                    __content = __cache_4685246624
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x117432560> name=None at 1174302e0> -> __attrs_4685243024
                __attrs_4685243024 = _static_4685243744
                __backup_description_4685211696 = get('description', __marker)

                # <Value 'widget/field/description' (26:32)> -> __value
                __token = 945
                try:
                    __zt_tmp = __attrs_4685243024
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'widget/field/description', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['description'] = __value

                # <Value 'python:description and not hidden' (29:23)> -> __condition
                __token = 1054
                try:
                    __zt_tmp = __attrs_4685243024
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('python', 'description and not hidden', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-text" >')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685244272
                    __default_4685244272 = _DEFAULT_MARKER

                    # <Value 'description' (28:21)> -> __cache_4685245664
                    __token = 1018
                    try:
                        __zt_tmp = __attrs_4685243024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4685245664 = _static_4427992992('path', 'description', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'description' (28:21)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 117432e30> -> __condition
                    __expression = __cache_4685245664

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('field description\n      ')
                    else:
                        __content = __cache_4685245664
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>')
                if (__backup_description_4685211696 is __marker):
                    del econtext['description']
                else:
                    econtext['description'] = __backup_description_4685211696
                __append('\n    </div>\n  </div>')
                if (__backup_hidden_4685212704 is __marker):
                    del econtext['hidden']
                else:
                    econtext['hidden'] = __backup_hidden_4685212704
                if (__backup_error_4680546864 is __marker):
                    del econtext['error']
                else:
                    econtext['error'] = __backup_error_4680546864
                __append('\n\n')
                ____index_4685215920 -= 1
                if (____index_4685215920 > 0):
                    __append('')
            if (__backup_widget_4682708976 is __marker):
                del econtext['widget']
            else:
                econtext['widget'] = __backup_widget_4682708976
            __append('\n')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4685243600
            __attrs_4685243600 = _static_4428767312
            __backup_macroname_4686972992 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x11742a770> name=None at 117429330> -> __value
            __value = _static_4685211504
            econtext['macroname'] = __value

            # <Value 'context/@@ploneform-macros/actions' (36:32)> -> __macro
            __token = 1197
            try:
                __zt_tmp = __attrs_4685243600
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4427992992('path', 'context/@@ploneform-macros/actions', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __token = 1197
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4686972992 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4686972992
            __append('\n</form>\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }