# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/z3cform/templates/widget.pt'

__tokens = {89: ('nocall:context', 4, 22), 125: (' python:widget.erro', 5, 20), 172: ("s python:error and ' error' or ", 6, 25), 232: ("es python: (None, '', [], ('', '', '', '00', '00', ''), ('', '', '", 7, 25), 326: ("ass python: (widget.value in empty_values) and ' empty' o", 8, 23), 413: ('formfield-${python:widget.id}', 10, 7), 425: ('python:widget.id', 10, 19), 454: ("mb-3 field fieldname-${python:widget.name} widget-mode-${python:widget.mode}${error_class}${empty_class} ${python:getattr(widget, 'wrapper_css_class', False) or False}", 11, 10), 477: ('python:widget.name', 11, 33), 511: ('python:widget.mode', 11, 67), 532: ('error_class', 11, 88), 546: ('empty_class', 11, 102), 561: ("python:getattr(widget, 'wrapper_css_class', False) or False", 11, 117), 642: ('${widget/name}', 12, 19), 644: ('widget/name', 12, 21), 752: ("python: widget.mode == 'input' and widget.label", 15, 26), 675: ('${python:widget.id}', 13, 16), 677: ('python:widget.id', 13, 18), 847: ('python:widget.label', 16, 45), 959: ('python:widget.required', 19, 29), 1130: ("python: widget.mode == 'display' and widget.label", 23, 25), 1227: ('python:widget.label', 24, 45), 1317: ('python:widget.render()', 27, 46), 1416: ("python: getattr(widget, 'description', widget.field.description)", 30, 33), 1584: ("python:description and widget.mode == 'input'", 33, 26), 1545: ('description', 32, 34), 1713: ('error', 38, 24), 1752: ('python:error.render() or False', 39, 32)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4710338320 = {'class': 'form-text', }
_static_4708948704 = {'type': 'text', }
_static_4708956960 = {'class': 'widget-label form-label d-block', }
_static_4708954080 = {'class': 'required', 'title': 'Required', }
_static_4459104240 = {}
_static_4708951392 = {'for': '${python:widget.id}', 'class': 'form-label', }
_static_4459175296 = __C2ZContextWrapper
_static_4459168576 = __compile_zt_expr
_static_4708943904 = {'id': 'formfield-${python:widget.id}', 'class': "mb-3 field fieldname-${python:widget.name} widget-mode-${python:widget.mode}${error_class}${empty_class} ${python:getattr(widget, 'wrapper_css_class', False) or False}", 'data-fieldname': '${widget/name}', }

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

    def render_widget_wrapper(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_widget = econtext['__slot_widget'].pop()
        except:
            __slot_widget = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x118acc820> name=None at 118acc880> -> __attrs_4708946736
            __attrs_4708946736 = _static_4708943904
            __backup_widget_4708727920 = get('widget', __marker)

            # <Value 'nocall:context' (4:22)> -> __value
            __token = 89
            try:
                __zt_tmp = __attrs_4708946736
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('nocall', 'context', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['widget'] = __value
            __backup_error_4708728784 = get('error', __marker)

            # <Value 'python:widget.error' (5:20)> -> __value
            __token = 125
            try:
                __zt_tmp = __attrs_4708946736
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('python', 'widget.error', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['error'] = __value
            __backup_error_class_4708644368 = get('error_class', __marker)

            # <Value "python:error and ' error' or ''" (6:25)> -> __value
            __token = 172
            try:
                __zt_tmp = __attrs_4708946736
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('python', "error and ' error' or ''", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['error_class'] = __value
            __backup_empty_values_4708636448 = get('empty_values', __marker)

            # <Value "python: (None, '', [], ('', '', '', '00', '00', ''), ('', '', ''))" (7:25)> -> __value
            __token = 232
            try:
                __zt_tmp = __attrs_4708946736
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('python', " (None, '', [], ('', '', '', '00', '00', ''), ('', '', ''))", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['empty_values'] = __value
            __backup_empty_class_4708674352 = get('empty_class', __marker)

            # <Value "python: (widget.value in empty_values) and ' empty' or ''" (8:23)> -> __value
            __token = 326
            try:
                __zt_tmp = __attrs_4708946736
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('python', " (widget.value in empty_values) and ' empty' or ''", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['empty_class'] = __value
            __previous_i18n_domain_4708948368 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div')

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708945680
            __default_4708945680 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution 'formfield-${python:widget.id}' (10:7)> braces_required=True translation=False default='"?"' default_marker='"?"' at 118acccd0> -> __attr_id
            __token = 413
            __token = 425
            try:
                __zt_tmp = __attrs_4708946736
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_4459168576('python', 'widget.id', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_id = ('%s%s' % ('formfield-', (__attr_id if (__attr_id is not None) else ''), ))
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

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708944720
            __default_4708944720 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "mb-3 field fieldname-${python:widget.name} widget-mode-${python:widget.mode}${error_class}${empty_class} ${python:getattr(widget, 'wrapper_css_class', False) or False}" (11:10)> braces_required=True translation=False default='"?"' default_marker='"?"' at 118acc520> -> __attr_class
            __token = 454
            __token = 477
            try:
                __zt_tmp = __attrs_4708946736
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4459168576('python', 'widget.name', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 511
            try:
                __zt_tmp = __attrs_4708946736
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class_509 = _static_4459168576('python', 'widget.mode', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_class_509 = __quote(__attr_class_509, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 532
            try:
                __zt_tmp = __attrs_4708946736
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class_530 = _static_4459168576('path', 'error_class', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_class_530 = __quote(__attr_class_530, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 546
            try:
                __zt_tmp = __attrs_4708946736
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class_544 = _static_4459168576('path', 'empty_class', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_class_544 = __quote(__attr_class_544, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 561
            try:
                __zt_tmp = __attrs_4708946736
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class_559 = _static_4459168576('python', "getattr(widget, 'wrapper_css_class', False) or False", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_class_559 = __quote(__attr_class_559, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_class = ('%s%s%s%s%s%s%s%s' % ('mb-3 field fieldname-', (__attr_class if (__attr_class is not None) else ''), ' widget-mode-', (__attr_class_509 if (__attr_class_509 is not None) else ''), (__attr_class_530 if (__attr_class_530 is not None) else ''), (__attr_class_544 if (__attr_class_544 is not None) else ''), ' ', (__attr_class_559 if (__attr_class_559 is not None) else ''), ))
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

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708942032
            __default_4708942032 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${widget/name}' (12:19)> braces_required=True translation=False default='"?"' default_marker='"?"' at 118acc340> -> __attr_data_fieldname
            __token = 642
            __token = 644
            try:
                __zt_tmp = __attrs_4708946736
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_fieldname = _static_4459168576('path', 'widget/name', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_data_fieldname = __quote(__attr_data_fieldname, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_data_fieldname = __attr_data_fieldname
            if (__attr_data_fieldname is None):
                pass
            else:
                if (__attr_data_fieldname is _DEFAULT_MARKER):
                    __attr_data_fieldname = None
                else:
                    __tt = type(__attr_data_fieldname)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_data_fieldname = str(__attr_data_fieldname)
                    else:
                        if (__tt is bytes):
                            __attr_data_fieldname = decode(__attr_data_fieldname)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_data_fieldname = __attr_data_fieldname.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_data_fieldname)
                                    __attr_data_fieldname = (str(__attr_data_fieldname) if (__attr_data_fieldname is __converted) else __converted)
                                else:
                                    __attr_data_fieldname = __attr_data_fieldname()
            if (__attr_data_fieldname is not None):
                __append((' data-fieldname="%s"' % __attr_data_fieldname))
            __append('>\n    ')

            # <Static value=<ast.Dict object at 0x118ace560> name=None at 118ace5f0> -> __attrs_4708950288
            __attrs_4708950288 = _static_4708951392

            # <Value "python: widget.mode == 'input' and widget.label" (15:26)> -> __condition
            __token = 752
            try:
                __zt_tmp = __attrs_4708950288
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4459168576('python', " widget.mode == 'input' and widget.label", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            if __condition:

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label')

                # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708947168
                __default_4708947168 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${python:widget.id}' (13:16)> braces_required=True translation=False default='"?"' default_marker='"?"' at 118ace530> -> __attr_for
                __token = 675
                __token = 677
                try:
                    __zt_tmp = __attrs_4708950288
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_for = _static_4459168576('python', 'widget.id', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
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
                __append(' class="form-label">\n        ')

                # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708947072
                __attrs_4708947072 = _static_4459104240

                # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708950912
                __default_4708950912 = _DEFAULT_MARKER

                # <Value 'python:widget.label' (16:45)> -> __cache_4708948752
                __token = 847
                try:
                    __zt_tmp = __attrs_4708947072
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4708948752 = _static_4459168576('python', 'widget.label', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:widget.label' (16:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118acda50> -> __condition
                __expression = __cache_4708948752

                # <Symbol value=<DEFAULT> at 109c89f90> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>label</span>')
                else:
                    __content = __cache_4708948752
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x118acefe0> name=None at 118acebf0> -> __attrs_4708957728
                __attrs_4708957728 = _static_4708954080

                # <Value 'python:widget.required' (19:29)> -> __condition
                __token = 959
                try:
                    __zt_tmp = __attrs_4708957728
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4459168576('python', 'widget.required', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="required"')

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708943856
                    __default_4708943856 = _DEFAULT_MARKER

                    # <Translate msgid='title_required' node=<ast.Constant object at 0x118acc8e0> at 118acddb0> -> __attr_title
                    __attr_title = 'Required'
                    __attr_title = translate('title_required', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append('></span>')
                __append('\n    </label>')
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x118acfb20> name=None at 118acef50> -> __attrs_4708957248
            __attrs_4708957248 = _static_4708956960

            # <Value "python: widget.mode == 'display' and widget.label" (23:25)> -> __condition
            __token = 1130
            try:
                __zt_tmp = __attrs_4708957248
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4459168576('python', " widget.mode == 'display' and widget.label", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            if __condition:

                # <b ... (0:0)
                # --------------------------------------------------------
                __append('<b class="widget-label form-label d-block">\n        ')

                # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708955664
                __attrs_4708955664 = _static_4459104240

                # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708955280
                __default_4708955280 = _DEFAULT_MARKER

                # <Value 'python:widget.label' (24:45)> -> __cache_4708954416
                __token = 1227
                try:
                    __zt_tmp = __attrs_4708955664
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4708954416 = _static_4459168576('python', 'widget.label', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:widget.label' (24:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118acf3d0> -> __condition
                __expression = __cache_4708954416

                # <Symbol value=<DEFAULT> at 109c89f90> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>label</span>')
                else:
                    __content = __cache_4708954416
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('\n    </b>')
            __append('\n\n    ')
            if (__slot_widget is None):

                # <Static value=<ast.Dict object at 0x118acdae0> name=None at 118acdde0> -> __attrs_4710334768
                __attrs_4710334768 = _static_4708948704

                # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708951056
                __default_4708951056 = _DEFAULT_MARKER

                # <Value 'python:widget.render()' (27:46)> -> __cache_4708954992
                __token = 1317
                try:
                    __zt_tmp = __attrs_4710334768
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4708954992 = _static_4459168576('python', 'widget.render()', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:widget.render()' (27:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118ace9b0> -> __condition
                __expression = __cache_4708954992

                # <Symbol value=<DEFAULT> at 109c89f90> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="text" />')
                else:
                    __content = __cache_4708954992
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
            else:
                __slot_widget(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x118c20f10> name=None at 118c20ee0> -> __attrs_4710339136
            __attrs_4710339136 = _static_4710338320
            __backup_description_4708769920 = get('description', __marker)

            # <Value "python: getattr(widget, 'description', widget.field.description)" (30:33)> -> __value
            __token = 1416
            try:
                __zt_tmp = __attrs_4710339136
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('python', " getattr(widget, 'description', widget.field.description)", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['description'] = __value

            # <Value "python:description and widget.mode == 'input'" (33:26)> -> __condition
            __token = 1584
            try:
                __zt_tmp = __attrs_4710339136
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4459168576('python', "description and widget.mode == 'input'", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-text">')

                # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710335056
                __default_4710335056 = _DEFAULT_MARKER

                # <Value 'description' (32:34)> -> __cache_4710338848
                __token = 1545
                try:
                    __zt_tmp = __attrs_4710339136
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4710338848 = _static_4459168576('path', 'description', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

                # <BinOp left=<Value 'description' (32:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118c20d90> -> __condition
                __expression = __cache_4710338848

                # <Symbol value=<DEFAULT> at 109c89f90> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n      help text\n    ')
                else:
                    __content = __cache_4710338848
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('</div>')
            if (__backup_description_4708769920 is __marker):
                del econtext['description']
            else:
                econtext['description'] = __backup_description_4708769920
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4710341680
            __attrs_4710341680 = _static_4459104240

            # <Value 'error' (38:24)> -> __condition
            __token = 1713
            try:
                __zt_tmp = __attrs_4710341680
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4459168576('path', 'error', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            if __condition:

                # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4710342976
                __default_4710342976 = _DEFAULT_MARKER

                # <Value 'python:error.render() or False' (39:32)> -> __cache_4710337600
                __token = 1752
                try:
                    __zt_tmp = __attrs_4710341680
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4710337600 = _static_4459168576('python', 'error.render() or False', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:error.render() or False' (39:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118c21810> -> __condition
                __expression = __cache_4710337600

                # <Symbol value=<DEFAULT> at 109c89f90> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div>\n        Error\n    </div>')
                else:
                    __content = __cache_4710337600
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
            __append('\n\n</div>')
            __i18n_domain = __previous_i18n_domain_4708948368
            if (__backup_empty_class_4708674352 is __marker):
                del econtext['empty_class']
            else:
                econtext['empty_class'] = __backup_empty_class_4708674352
            if (__backup_empty_values_4708636448 is __marker):
                del econtext['empty_values']
            else:
                econtext['empty_values'] = __backup_empty_values_4708636448
            if (__backup_error_class_4708644368 is __marker):
                del econtext['error_class']
            else:
                econtext['error_class'] = __backup_error_class_4708644368
            if (__backup_error_4708728784 is __marker):
                del econtext['error']
            else:
                econtext['error'] = __backup_error_4708728784
            if (__backup_widget_4708727920 is __marker):
                del econtext['widget']
            else:
                econtext['widget'] = __backup_widget_4708727920
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
            __token = None
            render_widget_wrapper(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_widget_wrapper': render_widget_wrapper, 'render': render, }