# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/z3cform/templates/macros.pt'

__tokens = {386: ('view/label | nothing', 12, 33), 421: ('view/label', 12, 68), 619: ('view/status', 18, 47), 681: (" python:view.widgets.errors or status == getattr(view, 'formErrorsMessage', None", 19, 49), 809: ('s view/widgets/erro', 20, 45), 875: ('ns nocall: context/@@iconresol', 21, 43), 953: ('python: status', 22, 43), 1010: ('python:not (has_error or errors)', 23, 40), 1237: ("python:icons.tag('plone-statusmessage-info', tag_alt='Info', tag_class='statusmessage-icon mb-1 me-2')", 26, 57), 1464: ('status | nothing', 28, 53), 1685: ('python:has_error or errors', 33, 40), 1909: ("python:icons.tag('plone-statusmessage-error', tag_alt='Error', tag_class='statusmessage-icon mb-1 me-2')", 36, 57), 2138: ('status | nothing', 38, 53), 2362: ("python:[e for e in errors if not getattr(e, 'widget', None)]", 42, 69), 2518: ('errors', 44, 60), 2582: ('not:nocall:error/widget', 45, 55), 2670: ('error/render', 46, 63), 3164: ('view/groups | nothing', 58, 41), 3230: (' view/form_name | nothin', 59, 43), 3300: ('s view/css_class | strin', 60, 43), 3382: ('el view/default_fieldset_label | form_n', 61, 54), 3476: ('ing view/enable_form_tabbing | python:', 62, 50), 3574: ('tion view/enable_unload_protection|python', 63, 54), 3668: ("ction python:enable_unload_protection and 'pat-formunload", 64, 46), 3777: ('ofocus view/enable_autofocus|pyth', 65, 44), 3855: ("tofocus python:enable_autofocus and 'pat-formau", 66, 36), 3948: ("lidation python:'pat-validation' if Tru", 67, 36), 4033: ('as_groups python:bo', 68, 35), 4100: ("rm_tabbing python:(has_groups and enable_form_tabbing) and 'enableFormTabbing pat-aut", 69, 36), 4239: ('fault_label python:has_groups and default_fieldset_label and len(v', 70, 41), 4359: ('iew_name_raw python:view.__name__ or request.getURL().s', 71, 40), 4464: ("orm_view_name python:'-'.join(['view', 'name'] + [x for x in form_view_name_raw.spli", 72, 35), 4775: ('s string:rowlike $unload_protection $autofocus $validation $form_tabbing $form_class $form_view_name_raw $form_view_na', 76, 42), 4645: ('view/action|request/getURL', 74, 45), 5041: ('thod view/method|string', 79, 40), 4718: (' view/enctyp', 75, 45), 4935: ('id view', 77, 38), 4986: ('ame form_', 78, 39), 5333: ('request/fieldset | python:None', 86, 55), 5406: ('python:has_groups and enable_form_tabbing and current_fieldset is not None', 87, 41), 5530: ('current_fieldset', 88, 48), 10179: ('view/enableCSRFProtection|nothing', 169, 46), 10259: ('context/@@authenticator/authenticator', 170, 45), 5767: ('show_default_label|nothing', 94, 57), 5843: (' has_groups|nothin', 95, 48), 5938: ('not:show_default_label', 97, 72), 6017: ('show_default_label', 99, 53), 6094: ('string:fieldsetlegend-default', 100, 57), 6176: ('default_fieldset_label', 101, 51), 7039: ('has_groups', 115, 74), 7020: ('groups', 115, 55), 7154: ('nocall:context/@@plone/normalizeString', 117, 62), 7254: (' group/labe', 118, 60), 7326: ("e python:getattr(group, '__name__', False) or getattr(group.label, 'default', False) or fieldset_lab", 119, 58), 7487: ('me python:normalizeString(fieldset_na', 120, 57), 7583: ('string:fieldset-${fieldset_name}', 121, 53), 7672: (' string:kssattr-fieldset-${fieldset_name', 122, 55), 7777: ('t fieldset_na', 123, 62), 7960: ('fieldset_label', 127, 57), 8037: ('string:fieldsetlegend-${fieldset_name}', 128, 61), 8132: ('fieldset_label', 129, 55), 8298: ('group/description|nothing', 132, 71), 8381: ('group_description', 133, 56), 8464: ('group_description', 134, 64), 8650: ('group/widgets/errors', 138, 68), 8736: ('errors', 139, 64), 8811: ('errors', 140, 67), 8948: ('not:nocall:error/widget', 142, 61), 9042: ('error/render', 143, 69), 9219: ('nocall:group', 147, 62), 9300: ('context/@@ploneform-macros/widget_rendering', 148, 66), 9300: ('context/@@ploneform-macros/widget_rendering', 148, 66), 6359: ('python:view.widgets.values()', 104, 62), 6625: ('widget/@@ploneform-render-widget', 107, 81), 9808: ('view/actions/values|nothing', 161, 65), 9890: ('view/actions/values', 162, 52), 9970: ('action/render', 163, 58)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4708767568 = {'xmlns': 'http://www.w3.org/1999/xhtml', }
_static_4708669792 = {'class': 'formControls', }
_static_4708663552 = 'widget_rendering'
_static_4708673536 = {'class': 'field error', }
_static_4708677088 = {'id': 'string:fieldsetlegend-${fieldset_name}', }
_static_4708639136 = {'id': 'string:fieldset-${fieldset_name}', 'class': 'string:kssattr-fieldset-${fieldset_name}', 'data-fieldset': 'fieldset_name', }
_static_4708646768 = {'id': 'string:fieldsetlegend-default', }
_static_4708634432 = {'id': 'fieldset-default', }
_static_4708712704 = {'type': 'hidden', 'name': 'fieldset', 'value': 'current_fieldset', }
_static_4708785440 = {'data-pat-autotoc': 'levels: legend; section: fieldset; className: autotabs', 'class': 'rowlike enableUnloadProtection', 'action': '.', 'method': 'post', 'enctype': 'view/enctype', 'id': 'view/id', 'name': 'form_name', }
_static_4708728688 = {'class': 'mt-2 field error', }
_static_4708791440 = {'class': 'content', }
_static_4708791632 = {'alt': 'alt', }
_static_4708788992 = {'class': 'portalMessage statusmessage statusmessage-error alert alert-danger', 'role': 'alert', }
_static_4708794128 = {'class': 'content', }
_static_4708793936 = {'alt': 'alt', }
_static_4708785920 = {'class': 'portalMessage statusmessage statusmessage-info alert alert-info', 'role': 'alert', }
_static_4459175296 = __C2ZContextWrapper
_static_4459168576 = __compile_zt_expr
_static_4459104240 = {}
_static_4708763152 = {'class': 'form', }

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

    def render_form(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_title = econtext['__slot_title'].pop()
        except:
            __slot_title = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x118aa0610> name=None at 118aa00d0> -> __attrs_4708784480
            __attrs_4708784480 = _static_4708763152

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form">\n\n            ')
            if (__slot_title is None):

                # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708779344
                __attrs_4708779344 = _static_4459104240
                __append('\n              ')

                # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708780112
                __attrs_4708780112 = _static_4459104240

                # <Value 'view/label | nothing' (12:33)> -> __condition
                __token = 386
                try:
                    __zt_tmp = __attrs_4708780112
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4459168576('path', 'view/label | nothing', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                if __condition:

                    # <h3 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h3>')

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708779584
                    __default_4708779584 = _DEFAULT_MARKER

                    # <Value 'view/label' (12:68)> -> __cache_4708781312
                    __token = 421
                    try:
                        __zt_tmp = __attrs_4708780112
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4708781312 = _static_4459168576('path', 'view/label', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/label' (12:68)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118aa4f70> -> __condition
                    __expression = __cache_4708781312

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4708781312
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</h3>')
                __append('\n            ')
            else:
                __slot_title(__stream, econtext.copy(), rcontext)
            __append('\n\n            ')
            __token = None
            render_titlelessform(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n        </div>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_titlelessform(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_formtop = econtext['__slot_formtop'].pop()
        except:
            __slot_formtop = None

        try:
            __slot_fields = econtext['__slot_fields'].pop()
        except:
            __slot_fields = None

        try:
            __slot_actions = econtext['__slot_actions'].pop()
        except:
            __slot_actions = None

        try:
            __slot_formbottom = econtext['__slot_formbottom'].pop()
        except:
            __slot_formbottom = None

        try:
            __slot_belowfields = econtext['__slot_belowfields'].pop()
        except:
            __slot_belowfields = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708780736
            __attrs_4708780736 = _static_4459104240
            __previous_i18n_domain_4708781840 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n\n                ')

            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708782800
            __attrs_4708782800 = _static_4459104240
            __backup_status_4708779296 = get('status', __marker)

            # <Value 'view/status' (18:47)> -> __value
            __token = 619
            try:
                __zt_tmp = __attrs_4708782800
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'view/status', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['status'] = __value
            __backup_has_error_4708786784 = get('has_error', __marker)

            # <Value "python:view.widgets.errors or status == getattr(view, 'formErrorsMessage', None)" (19:49)> -> __value
            __token = 681
            try:
                __zt_tmp = __attrs_4708782800
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('python', "view.widgets.errors or status == getattr(view, 'formErrorsMessage', None)", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['has_error'] = __value
            __backup_errors_4708778288 = get('errors', __marker)

            # <Value 'view/widgets/errors' (20:45)> -> __value
            __token = 809
            try:
                __zt_tmp = __attrs_4708782800
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'view/widgets/errors', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['errors'] = __value
            __backup_icons_4708780256 = get('icons', __marker)

            # <Value 'nocall: context/@@iconresolver' (21:43)> -> __value
            __token = 875
            try:
                __zt_tmp = __attrs_4708782800
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('nocall', ' context/@@iconresolver', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['icons'] = __value

            # <Value 'python: status' (22:43)> -> __condition
            __token = 953
            try:
                __zt_tmp = __attrs_4708782800
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4459168576('python', ' status', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            if __condition:
                __append('\n                    ')

                # <Static value=<ast.Dict object at 0x118aa5f00> name=None at 118aa5f30> -> __attrs_4708785488
                __attrs_4708785488 = _static_4708785920

                # <Value 'python:not (has_error or errors)' (23:40)> -> __condition
                __token = 1010
                try:
                    __zt_tmp = __attrs_4708785488
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4459168576('python', 'not (has_error or errors)', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="portalMessage statusmessage statusmessage-info alert alert-info" role="alert">\n                        ')

                    # <Static value=<ast.Dict object at 0x118aa7e50> name=None at 118aa7e80> -> __attrs_4708792352
                    __attrs_4708792352 = _static_4708793936

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708783904
                    __default_4708783904 = _DEFAULT_MARKER

                    # <Value "python:icons.tag('plone-statusmessage-info', tag_alt='Info', tag_class='statusmessage-icon mb-1 me-2')" (26:57)> -> __cache_4708792496
                    __token = 1237
                    try:
                        __zt_tmp = __attrs_4708792352
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4708792496 = _static_4459168576('python', "icons.tag('plone-statusmessage-info', tag_alt='Info', tag_class='statusmessage-icon mb-1 me-2')", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag('plone-statusmessage-info', tag_alt='Info', tag_class='statusmessage-icon mb-1 me-2')" (26:57)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118aa79a0> -> __condition
                    __expression = __cache_4708792496

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4708792496
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n                        ')

                    # <Static value=<ast.Dict object at 0x118aa7f10> name=None at 118aa7010> -> __attrs_4708787360
                    __attrs_4708787360 = _static_4708794128

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708787744
                    __default_4708787744 = _DEFAULT_MARKER

                    # <Value 'status | nothing' (28:53)> -> __cache_4708790144
                    __token = 1464
                    try:
                        __zt_tmp = __attrs_4708787360
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4708790144 = _static_4459168576('path', 'status | nothing', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

                    # <BinOp left=<Value 'status | nothing' (28:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118aa6e30> -> __condition
                    __expression = __cache_4708790144

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="content">\n                              The info status message.\n                        </span>')
                    else:
                        __content = __cache_4708790144
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n                    </div>')
                __append('\n                    ')

                # <Static value=<ast.Dict object at 0x118aa6b00> name=None at 118aa6cb0> -> __attrs_4708789280
                __attrs_4708789280 = _static_4708788992

                # <Value 'python:has_error or errors' (33:40)> -> __condition
                __token = 1685
                try:
                    __zt_tmp = __attrs_4708789280
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4459168576('python', 'has_error or errors', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="portalMessage statusmessage statusmessage-error alert alert-danger" role="alert">\n                        ')

                    # <Static value=<ast.Dict object at 0x118aa7550> name=None at 118aa75b0> -> __attrs_4708790480
                    __attrs_4708790480 = _static_4708791632

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708791104
                    __default_4708791104 = _DEFAULT_MARKER

                    # <Value "python:icons.tag('plone-statusmessage-error', tag_alt='Error', tag_class='statusmessage-icon mb-1 me-2')" (36:57)> -> __cache_4708784672
                    __token = 1909
                    try:
                        __zt_tmp = __attrs_4708790480
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4708784672 = _static_4459168576('python', "icons.tag('plone-statusmessage-error', tag_alt='Error', tag_class='statusmessage-icon mb-1 me-2')", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag('plone-statusmessage-error', tag_alt='Error', tag_class='statusmessage-icon mb-1 me-2')" (36:57)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118aa71f0> -> __condition
                    __expression = __cache_4708784672

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4708784672
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n                        ')

                    # <Static value=<ast.Dict object at 0x118aa7490> name=None at 118aa70a0> -> __attrs_4708793648
                    __attrs_4708793648 = _static_4708791440

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708793744
                    __default_4708793744 = _DEFAULT_MARKER

                    # <Value 'status | nothing' (38:53)> -> __cache_4708793024
                    __token = 2138
                    try:
                        __zt_tmp = __attrs_4708793648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4708793024 = _static_4459168576('path', 'status | nothing', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

                    # <BinOp left=<Value 'status | nothing' (38:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118aa7c40> -> __condition
                    __expression = __cache_4708793024

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="content">\n                              The error status message.\n                        </span>')
                    else:
                        __content = __cache_4708793024
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n                        ')

                    # <Static value=<ast.Dict object at 0x118a97f70> name=None at 118a96470> -> __attrs_4708723744
                    __attrs_4708723744 = _static_4708728688

                    # <Value "python:[e for e in errors if not getattr(e, 'widget', None)]" (42:69)> -> __condition
                    __token = 2362
                    try:
                        __zt_tmp = __attrs_4708723744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4459168576('python', "[e for e in errors if not getattr(e, 'widget', None)]", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="mt-2 field error">\n                            ')

                        # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708727632
                        __attrs_4708727632 = _static_4459104240

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append('<ul>\n                                ')

                        # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708713568
                        __attrs_4708713568 = _static_4459104240
                        __backup_error_4708727920 = get('error', __marker)

                        # <Value 'errors' (44:60)> -> __iterator
                        __token = 2518
                        try:
                            __zt_tmp = __attrs_4708713568
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_4459168576('path', 'errors', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                        (__iterator, ____index_4708726480, ) = getname('repeat')('error', __iterator)
                        econtext['error'] = None
                        for __item in __iterator:
                            econtext['error'] = __item
                            __append('\n                                    ')

                            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708724848
                            __attrs_4708724848 = _static_4459104240

                            # <Value 'not:nocall:error/widget' (45:55)> -> __condition
                            __token = 2582
                            try:
                                __zt_tmp = __attrs_4708724848
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4459168576('not', 'nocall:error/widget', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                            if __condition:

                                # <li ... (0:0)
                                # --------------------------------------------------------
                                __append('<li>')

                                # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708723504
                                __default_4708723504 = _DEFAULT_MARKER

                                # <Value 'error/render' (46:63)> -> __cache_4708724992
                                __token = 2670
                                try:
                                    __zt_tmp = __attrs_4708724848
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_4708724992 = _static_4459168576('path', 'error/render', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

                                # <BinOp left=<Value 'error/render' (46:63)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118a96b00> -> __condition
                                __expression = __cache_4708724992

                                # <Symbol value=<DEFAULT> at 109c89f90> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append('\n                                        Error\n                                    ')
                                else:
                                    __content = __cache_4708724992
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append('</li>')
                            __append('\n                                ')
                            ____index_4708726480 -= 1
                            if (____index_4708726480 > 0):
                                __append('')
                        if (__backup_error_4708727920 is __marker):
                            del econtext['error']
                        else:
                            econtext['error'] = __backup_error_4708727920
                        __append('\n                            </ul>\n                        </div>')
                    __append('\n                    </div>')
                __append('\n                ')
            if (__backup_icons_4708780256 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_4708780256
            if (__backup_errors_4708778288 is __marker):
                del econtext['errors']
            else:
                econtext['errors'] = __backup_errors_4708778288
            if (__backup_has_error_4708786784 is __marker):
                del econtext['has_error']
            else:
                econtext['has_error'] = __backup_has_error_4708786784
            if (__backup_status_4708779296 is __marker):
                del econtext['status']
            else:
                econtext['status'] = __backup_status_4708779296
            __append('\n\n\n                ')

            # <Static value=<ast.Dict object at 0x118aa5d20> name=None at 118aa6b60> -> __attrs_4708718656
            __attrs_4708718656 = _static_4708785440
            __backup_groups_4708783040 = get('groups', __marker)

            # <Value 'view/groups | nothing' (58:41)> -> __value
            __token = 3164
            try:
                __zt_tmp = __attrs_4708718656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'view/groups | nothing', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['groups'] = __value
            __backup_form_name_4708782704 = get('form_name', __marker)

            # <Value 'view/form_name | nothing' (59:43)> -> __value
            __token = 3230
            try:
                __zt_tmp = __attrs_4708718656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'view/form_name | nothing', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['form_name'] = __value
            __backup_form_class_4708786688 = get('form_class', __marker)

            # <Value 'view/css_class | string:' (60:43)> -> __value
            __token = 3300
            try:
                __zt_tmp = __attrs_4708718656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'view/css_class | string:', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['form_class'] = __value
            __backup_default_fieldset_label_4708786832 = get('default_fieldset_label', __marker)

            # <Value 'view/default_fieldset_label | form_name' (61:54)> -> __value
            __token = 3382
            try:
                __zt_tmp = __attrs_4708718656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'view/default_fieldset_label | form_name', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['default_fieldset_label'] = __value
            __backup_enable_form_tabbing_4708785536 = get('enable_form_tabbing', __marker)

            # <Value 'view/enable_form_tabbing | python:True' (62:50)> -> __value
            __token = 3476
            try:
                __zt_tmp = __attrs_4708718656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'view/enable_form_tabbing | python:True', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['enable_form_tabbing'] = __value
            __backup_enable_unload_protection_4708785824 = get('enable_unload_protection', __marker)

            # <Value 'view/enable_unload_protection|python:True' (63:54)> -> __value
            __token = 3574
            try:
                __zt_tmp = __attrs_4708718656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'view/enable_unload_protection|python:True', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['enable_unload_protection'] = __value
            __backup_unload_protection_4708785152 = get('unload_protection', __marker)

            # <Value "python:enable_unload_protection and 'pat-formunloadalert'" (64:46)> -> __value
            __token = 3668
            try:
                __zt_tmp = __attrs_4708718656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('python', "enable_unload_protection and 'pat-formunloadalert'", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['unload_protection'] = __value
            __backup_enable_autofocus_4708788416 = get('enable_autofocus', __marker)

            # <Value 'view/enable_autofocus|python:True' (65:44)> -> __value
            __token = 3777
            try:
                __zt_tmp = __attrs_4708718656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'view/enable_autofocus|python:True', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['enable_autofocus'] = __value
            __backup_autofocus_4708726864 = get('autofocus', __marker)

            # <Value "python:enable_autofocus and 'pat-formautofocus'" (66:36)> -> __value
            __token = 3855
            try:
                __zt_tmp = __attrs_4708718656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('python', "enable_autofocus and 'pat-formautofocus'", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['autofocus'] = __value
            __backup_validation_4708728064 = get('validation', __marker)

            # <Value "python:'pat-validation' if True else ''" (67:36)> -> __value
            __token = 3948
            try:
                __zt_tmp = __attrs_4708718656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('python', "'pat-validation' if True else ''", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['validation'] = __value
            __backup_has_groups_4708727008 = get('has_groups', __marker)

            # <Value 'python:bool(groups)' (68:35)> -> __value
            __token = 4033
            try:
                __zt_tmp = __attrs_4708718656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('python', 'bool(groups)', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['has_groups'] = __value
            __backup_form_tabbing_4708725088 = get('form_tabbing', __marker)

            # <Value "python:(has_groups and enable_form_tabbing) and 'enableFormTabbing pat-autotoc' or ''" (69:36)> -> __value
            __token = 4100
            try:
                __zt_tmp = __attrs_4708718656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('python', "(has_groups and enable_form_tabbing) and 'enableFormTabbing pat-autotoc' or ''", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['form_tabbing'] = __value
            __backup_show_default_label_4708725712 = get('show_default_label', __marker)

            # <Value 'python:has_groups and default_fieldset_label and len(view.widgets)' (70:41)> -> __value
            __token = 4239
            try:
                __zt_tmp = __attrs_4708718656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('python', 'has_groups and default_fieldset_label and len(view.widgets)', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['show_default_label'] = __value
            __backup_form_view_name_raw_4708720672 = get('form_view_name_raw', __marker)

            # <Value "python:view.__name__ or request.getURL().split('/')[-1]" (71:40)> -> __value
            __token = 4359
            try:
                __zt_tmp = __attrs_4708718656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('python', "view.__name__ or request.getURL().split('/')[-1]", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['form_view_name_raw'] = __value
            __backup_form_view_name_4708718848 = get('form_view_name', __marker)

            # <Value "python:'-'.join(['view', 'name'] + [x for x in form_view_name_raw.split('++') if x])" (72:35)> -> __value
            __token = 4464
            try:
                __zt_tmp = __attrs_4708718656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('python', "'-'.join(['view', 'name'] + [x for x in form_view_name_raw.split('++') if x])", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['form_view_name'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form data-pat-autotoc="levels: legend; section: fieldset; className: autotabs"')

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708724464
            __default_4708724464 = _DEFAULT_MARKER

            # <Substitution 'string:rowlike $unload_protection $autofocus $validation $form_tabbing $form_class $form_view_name_raw $form_view_name' (76:42)> -> __attr_class
            __token = 4775
            try:
                __zt_tmp = __attrs_4708718656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4459168576('string', 'rowlike $unload_protection $autofocus $validation $form_tabbing $form_class $form_view_name_raw $form_view_name', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', 'rowlike enableUnloadProtection', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708726768
            __default_4708726768 = _DEFAULT_MARKER

            # <Substitution 'view/action|request/getURL' (74:45)> -> __attr_action
            __token = 4645
            try:
                __zt_tmp = __attrs_4708718656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_4459168576('path', 'view/action|request/getURL', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', '.', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708728736
            __default_4708728736 = _DEFAULT_MARKER

            # <Substitution 'view/method|string:post' (79:40)> -> __attr_method
            __token = 5041
            try:
                __zt_tmp = __attrs_4708718656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_method = _static_4459168576('path', 'view/method|string:post', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_method = __quote(__attr_method, '"', '&quot;', 'post', _DEFAULT_MARKER)
            if (__attr_method is not None):
                __append((' method="%s"' % __attr_method))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708726432
            __default_4708726432 = _DEFAULT_MARKER

            # <Substitution 'view/enctype' (75:45)> -> __attr_enctype
            __token = 4718
            try:
                __zt_tmp = __attrs_4708718656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_enctype = _static_4459168576('path', 'view/enctype', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_enctype = __quote(__attr_enctype, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_enctype is not None):
                __append((' enctype="%s"' % __attr_enctype))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708720864
            __default_4708720864 = _DEFAULT_MARKER

            # <Substitution 'view/id' (77:38)> -> __attr_id
            __token = 4935
            try:
                __zt_tmp = __attrs_4708718656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_4459168576('path', 'view/id', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708719904
            __default_4708719904 = _DEFAULT_MARKER

            # <Substitution 'form_name' (78:39)> -> __attr_name
            __token = 4986
            try:
                __zt_tmp = __attrs_4708718656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_4459168576('path', 'form_name', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))
            __append('>\n\n                    ')
            if (__slot_formtop is None):

                # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708713520
                __attrs_4708713520 = _static_4459104240
            else:
                __slot_formtop(__stream, econtext.copy(), rcontext)
            __append('\n\n                    ')
            if (__slot_fields is None):

                # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708717888
                __attrs_4708717888 = _static_4459104240
                __append('\n                      ')

                # <Static value=<ast.Dict object at 0x118a94100> name=None at 118a94310> -> __attrs_4708714096
                __attrs_4708714096 = _static_4708712704
                __backup_current_fieldset_4708717504 = get('current_fieldset', __marker)

                # <Value 'request/fieldset | python:None' (86:55)> -> __value
                __token = 5333
                try:
                    __zt_tmp = __attrs_4708714096
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4459168576('path', 'request/fieldset | python:None', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                econtext['current_fieldset'] = __value

                # <Value 'python:has_groups and enable_form_tabbing and current_fieldset is not None' (87:41)> -> __condition
                __token = 5406
                try:
                    __zt_tmp = __attrs_4708714096
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4459168576('python', 'has_groups and enable_form_tabbing and current_fieldset is not None', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="hidden" name="fieldset"')

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708713760
                    __default_4708713760 = _DEFAULT_MARKER

                    # <Substitution 'current_fieldset' (88:48)> -> __attr_value
                    __token = 5530
                    try:
                        __zt_tmp = __attrs_4708714096
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_4459168576('path', 'current_fieldset', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />')
                if (__backup_current_fieldset_4708717504 is __marker):
                    del econtext['current_fieldset']
                else:
                    econtext['current_fieldset'] = __backup_current_fieldset_4708717504
                __append('\n\n                      <!-- Default fieldset -->\n                      ')
                __token = None
                render_fields(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n                    ')
            else:
                __slot_fields(__stream, econtext.copy(), rcontext)
            __append('\n\n                    ')
            if (__slot_belowfields is None):

                # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708630688
                __attrs_4708630688 = _static_4459104240
            else:
                __slot_belowfields(__stream, econtext.copy(), rcontext)
            __append('\n\n                    ')
            if (__slot_actions is None):

                # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708642016
                __attrs_4708642016 = _static_4459104240
                __append('\n                      ')
                __token = None
                render_actions(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n                    ')
            else:
                __slot_actions(__stream, econtext.copy(), rcontext)
            __append('\n\n                    ')

            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708666192
            __attrs_4708666192 = _static_4459104240

            # <Value 'view/enableCSRFProtection|nothing' (169:46)> -> __condition
            __token = 10179
            try:
                __zt_tmp = __attrs_4708666192
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4459168576('path', 'view/enableCSRFProtection|nothing', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            if __condition:

                # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708665472
                __default_4708665472 = _DEFAULT_MARKER

                # <Value 'context/@@authenticator/authenticator' (170:45)> -> __cache_4708666720
                __token = 10259
                try:
                    __zt_tmp = __attrs_4708666192
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4708666720 = _static_4459168576('path', 'context/@@authenticator/authenticator', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

                # <BinOp left=<Value 'context/@@authenticator/authenticator' (170:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118a884c0> -> __condition
                __expression = __cache_4708666720

                # <Symbol value=<DEFAULT> at 109c89f90> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4708666720
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
            __append('\n                    ')
            if (__slot_formbottom is None):

                # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708521520
                __attrs_4708521520 = _static_4459104240
            else:
                __slot_formbottom(__stream, econtext.copy(), rcontext)
            __append('\n\n                </form>')
            if (__backup_form_view_name_4708718848 is __marker):
                del econtext['form_view_name']
            else:
                econtext['form_view_name'] = __backup_form_view_name_4708718848
            if (__backup_form_view_name_raw_4708720672 is __marker):
                del econtext['form_view_name_raw']
            else:
                econtext['form_view_name_raw'] = __backup_form_view_name_raw_4708720672
            if (__backup_show_default_label_4708725712 is __marker):
                del econtext['show_default_label']
            else:
                econtext['show_default_label'] = __backup_show_default_label_4708725712
            if (__backup_form_tabbing_4708725088 is __marker):
                del econtext['form_tabbing']
            else:
                econtext['form_tabbing'] = __backup_form_tabbing_4708725088
            if (__backup_has_groups_4708727008 is __marker):
                del econtext['has_groups']
            else:
                econtext['has_groups'] = __backup_has_groups_4708727008
            if (__backup_validation_4708728064 is __marker):
                del econtext['validation']
            else:
                econtext['validation'] = __backup_validation_4708728064
            if (__backup_autofocus_4708726864 is __marker):
                del econtext['autofocus']
            else:
                econtext['autofocus'] = __backup_autofocus_4708726864
            if (__backup_enable_autofocus_4708788416 is __marker):
                del econtext['enable_autofocus']
            else:
                econtext['enable_autofocus'] = __backup_enable_autofocus_4708788416
            if (__backup_unload_protection_4708785152 is __marker):
                del econtext['unload_protection']
            else:
                econtext['unload_protection'] = __backup_unload_protection_4708785152
            if (__backup_enable_unload_protection_4708785824 is __marker):
                del econtext['enable_unload_protection']
            else:
                econtext['enable_unload_protection'] = __backup_enable_unload_protection_4708785824
            if (__backup_enable_form_tabbing_4708785536 is __marker):
                del econtext['enable_form_tabbing']
            else:
                econtext['enable_form_tabbing'] = __backup_enable_form_tabbing_4708785536
            if (__backup_default_fieldset_label_4708786832 is __marker):
                del econtext['default_fieldset_label']
            else:
                econtext['default_fieldset_label'] = __backup_default_fieldset_label_4708786832
            if (__backup_form_class_4708786688 is __marker):
                del econtext['form_class']
            else:
                econtext['form_class'] = __backup_form_class_4708786688
            if (__backup_form_name_4708782704 is __marker):
                del econtext['form_name']
            else:
                econtext['form_name'] = __backup_form_name_4708782704
            if (__backup_groups_4708783040 is __marker):
                del econtext['groups']
            else:
                econtext['groups'] = __backup_groups_4708783040
            __append('\n            ')
            __i18n_domain = __previous_i18n_domain_4708781840
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_fields(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708632848
            __attrs_4708632848 = _static_4459104240
            __backup_show_default_label_4708728784 = get('show_default_label', __marker)

            # <Value 'show_default_label|nothing' (94:57)> -> __value
            __token = 5767
            try:
                __zt_tmp = __attrs_4708632848
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'show_default_label|nothing', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['show_default_label'] = __value
            __backup_has_groups_4708712848 = get('has_groups', __marker)

            # <Value 'has_groups|nothing' (95:48)> -> __value
            __token = 5843
            try:
                __zt_tmp = __attrs_4708632848
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'has_groups|nothing', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['has_groups'] = __value
            __append('\n\n                          ')

            # <Static value=<ast.Dict object at 0x118a80f40> name=None at 118a81690> -> __attrs_4708635296
            __attrs_4708635296 = _static_4708634432

            # <Negate value=<Value 'not:show_default_label' (97:72)> at 118a80be0> -> __cache_4708633568

            # <Value 'not:show_default_label' (97:72)> -> __cache_4708633568
            __token = 5938
            try:
                __zt_tmp = __attrs_4708635296
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4708633568 = _static_4459168576('not', 'show_default_label', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            __cache_4708633568 = not __cache_4708633568
            __condition = __cache_4708633568
            if __condition:

                # <fieldset ... (0:0)
                # --------------------------------------------------------
                __append('<fieldset id="fieldset-default">')
            __append('\n\n                              ')

            # <Static value=<ast.Dict object at 0x118a83f70> name=None at 118a83700> -> __attrs_4708641632
            __attrs_4708641632 = _static_4708646768

            # <Value 'show_default_label' (99:53)> -> __condition
            __token = 6017
            try:
                __zt_tmp = __attrs_4708641632
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4459168576('path', 'show_default_label', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            if __condition:

                # <legend ... (0:0)
                # --------------------------------------------------------
                __append('<legend')

                # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708646096
                __default_4708646096 = _DEFAULT_MARKER

                # <Substitution 'string:fieldsetlegend-default' (100:57)> -> __attr_id
                __token = 6094
                try:
                    __zt_tmp = __attrs_4708641632
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_4459168576('string', 'fieldsetlegend-default', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))
                __append('>')

                # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708646672
                __default_4708646672 = _DEFAULT_MARKER

                # <Value 'default_fieldset_label' (101:51)> -> __cache_4708641152
                __token = 6176
                try:
                    __zt_tmp = __attrs_4708641632
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4708641152 = _static_4459168576('path', 'default_fieldset_label', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

                # <BinOp left=<Value 'default_fieldset_label' (101:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118a83fa0> -> __condition
                __expression = __cache_4708641152

                # <Symbol value=<DEFAULT> at 109c89f90> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Form name')
                else:
                    __content = __cache_4708641152
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</legend>')
            __append('\n\n                              ')
            __token = None
            render_widget_rendering(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n                          ')
            __condition = __cache_4708633568
            if __condition:
                __append('</fieldset>')
            __append('\n\n                          <!-- Secondary fieldsets -->\n                          ')

            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708642304
            __attrs_4708642304 = _static_4459104240

            # <Value 'has_groups' (115:74)> -> __condition
            __token = 7039
            try:
                __zt_tmp = __attrs_4708642304
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4459168576('path', 'has_groups', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            if __condition:
                __backup_group_4708633136 = get('group', __marker)

                # <Value 'groups' (115:55)> -> __iterator
                __token = 7020
                try:
                    __zt_tmp = __attrs_4708642304
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4459168576('path', 'groups', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                (__iterator, ____index_4708643600, ) = getname('repeat')('group', __iterator)
                econtext['group'] = None
                for __item in __iterator:
                    econtext['group'] = __item
                    __append('\n                              ')

                    # <Static value=<ast.Dict object at 0x118a821a0> name=None at 118a820e0> -> __attrs_4708636736
                    __attrs_4708636736 = _static_4708639136
                    __backup_normalizeString_4708645520 = get('normalizeString', __marker)

                    # <Value 'nocall:context/@@plone/normalizeString' (117:62)> -> __value
                    __token = 7154
                    try:
                        __zt_tmp = __attrs_4708636736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4459168576('nocall', 'context/@@plone/normalizeString', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                    econtext['normalizeString'] = __value
                    __backup_fieldset_label_4708636448 = get('fieldset_label', __marker)

                    # <Value 'group/label' (118:60)> -> __value
                    __token = 7254
                    try:
                        __zt_tmp = __attrs_4708636736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4459168576('path', 'group/label', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                    econtext['fieldset_label'] = __value
                    __backup_fieldset_name_4708631840 = get('fieldset_name', __marker)

                    # <Value "python:getattr(group, '__name__', False) or getattr(group.label, 'default', False) or fieldset_label" (119:58)> -> __value
                    __token = 7326
                    try:
                        __zt_tmp = __attrs_4708636736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4459168576('python', "getattr(group, '__name__', False) or getattr(group.label, 'default', False) or fieldset_label", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                    econtext['fieldset_name'] = __value
                    __backup_fieldset_name_4708644368 = get('fieldset_name', __marker)

                    # <Value 'python:normalizeString(fieldset_name)' (120:57)> -> __value
                    __token = 7487
                    try:
                        __zt_tmp = __attrs_4708636736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4459168576('python', 'normalizeString(fieldset_name)', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                    econtext['fieldset_name'] = __value

                    # <fieldset ... (0:0)
                    # --------------------------------------------------------
                    __append('<fieldset')

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708639808
                    __default_4708639808 = _DEFAULT_MARKER

                    # <Substitution 'string:fieldset-${fieldset_name}' (121:53)> -> __attr_id
                    __token = 7583
                    try:
                        __zt_tmp = __attrs_4708636736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_4459168576('string', 'fieldset-${fieldset_name}', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708638752
                    __default_4708638752 = _DEFAULT_MARKER

                    # <Substitution 'string:kssattr-fieldset-${fieldset_name}' (122:55)> -> __attr_class
                    __token = 7672
                    try:
                        __zt_tmp = __attrs_4708636736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4459168576('string', 'kssattr-fieldset-${fieldset_name}', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708634288
                    __default_4708634288 = _DEFAULT_MARKER

                    # <Substitution 'fieldset_name' (123:62)> -> __attr_data_fieldset
                    __token = 7777
                    try:
                        __zt_tmp = __attrs_4708636736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_data_fieldset = _static_4459168576('path', 'fieldset_name', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                    __attr_data_fieldset = __quote(__attr_data_fieldset, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_data_fieldset is not None):
                        __append((' data-fieldset="%s"' % __attr_data_fieldset))
                    __append('>\n\n                                      ')

                    # <Static value=<ast.Dict object at 0x118a8b5e0> name=None at 118a8b850> -> __attrs_4708675792
                    __attrs_4708675792 = _static_4708677088

                    # <Value 'fieldset_label' (127:57)> -> __condition
                    __token = 7960
                    try:
                        __zt_tmp = __attrs_4708675792
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4459168576('path', 'fieldset_label', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                    if __condition:

                        # <legend ... (0:0)
                        # --------------------------------------------------------
                        __append('<legend')

                        # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708675744
                        __default_4708675744 = _DEFAULT_MARKER

                        # <Substitution 'string:fieldsetlegend-${fieldset_name}' (128:61)> -> __attr_id
                        __token = 8037
                        try:
                            __zt_tmp = __attrs_4708675792
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_4459168576('string', 'fieldsetlegend-${fieldset_name}', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((' id="%s"' % __attr_id))
                        __append('>')

                        # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708678384
                        __default_4708678384 = _DEFAULT_MARKER

                        # <Value 'fieldset_label' (129:55)> -> __cache_4708677856
                        __token = 8132
                        try:
                            __zt_tmp = __attrs_4708675792
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4708677856 = _static_4459168576('path', 'fieldset_label', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

                        # <BinOp left=<Value 'fieldset_label' (129:55)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118a8b9a0> -> __condition
                        __expression = __cache_4708677856

                        # <Symbol value=<DEFAULT> at 109c89f90> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Form name')
                        else:
                            __content = __cache_4708677856
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</legend>')
                    __append('\n\n                                      ')

                    # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708672048
                    __attrs_4708672048 = _static_4459104240
                    __backup_group_description_4708631792 = get('group_description', __marker)

                    # <Value 'group/description|nothing' (132:71)> -> __value
                    __token = 8298
                    try:
                        __zt_tmp = __attrs_4708672048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4459168576('path', 'group/description|nothing', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                    econtext['group_description'] = __value

                    # <Value 'group_description' (133:56)> -> __condition
                    __token = 8381
                    try:
                        __zt_tmp = __attrs_4708672048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4459168576('path', 'group_description', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                    if __condition:

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append('<p>')

                        # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708679200
                        __default_4708679200 = _DEFAULT_MARKER

                        # <Value 'group_description' (134:64)> -> __cache_4708675264
                        __token = 8464
                        try:
                            __zt_tmp = __attrs_4708672048
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4708675264 = _static_4459168576('path', 'group_description', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

                        # <BinOp left=<Value 'group_description' (134:64)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118a8a380> -> __condition
                        __expression = __cache_4708675264

                        # <Symbol value=<DEFAULT> at 109c89f90> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n                                          Description\n                                      ')
                        else:
                            __content = __cache_4708675264
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('</p>')
                    if (__backup_group_description_4708631792 is __marker):
                        del econtext['group_description']
                    else:
                        econtext['group_description'] = __backup_group_description_4708631792
                    __append('\n\n                                      ')

                    # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708677472
                    __attrs_4708677472 = _static_4459104240
                    __backup_errors_4708674064 = get('errors', __marker)

                    # <Value 'group/widgets/errors' (138:68)> -> __value
                    __token = 8650
                    try:
                        __zt_tmp = __attrs_4708677472
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4459168576('path', 'group/widgets/errors', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                    econtext['errors'] = __value

                    # <Value 'errors' (139:64)> -> __condition
                    __token = 8736
                    try:
                        __zt_tmp = __attrs_4708677472
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4459168576('path', 'errors', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                    if __condition:
                        __backup_error_4708677040 = get('error', __marker)

                        # <Value 'errors' (140:67)> -> __iterator
                        __token = 8811
                        try:
                            __zt_tmp = __attrs_4708677472
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_4459168576('path', 'errors', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                        (__iterator, ____index_4708677808, ) = getname('repeat')('error', __iterator)
                        econtext['error'] = None
                        for __item in __iterator:
                            econtext['error'] = __item
                            __append('\n                                          ')

                            # <Static value=<ast.Dict object at 0x118a8a800> name=None at 118a8a470> -> __attrs_4708672960
                            __attrs_4708672960 = _static_4708673536

                            # <Value 'not:nocall:error/widget' (142:61)> -> __condition
                            __token = 8948
                            try:
                                __zt_tmp = __attrs_4708672960
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4459168576('not', 'nocall:error/widget', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="field error">')

                                # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708672864
                                __default_4708672864 = _DEFAULT_MARKER

                                # <Value 'error/render' (143:69)> -> __cache_4708667920
                                __token = 9042
                                try:
                                    __zt_tmp = __attrs_4708672960
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_4708667920 = _static_4459168576('path', 'error/render', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

                                # <BinOp left=<Value 'error/render' (143:69)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118a89d50> -> __condition
                                __expression = __cache_4708667920

                                # <Symbol value=<DEFAULT> at 109c89f90> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_4708667920
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append('</div>')
                            __append('\n                                      ')
                            ____index_4708677808 -= 1
                            if (____index_4708677808 > 0):
                                __append('')
                        if (__backup_error_4708677040 is __marker):
                            del econtext['error']
                        else:
                            econtext['error'] = __backup_error_4708677040
                    if (__backup_errors_4708674064 is __marker):
                        del econtext['errors']
                    else:
                        econtext['errors'] = __backup_errors_4708674064
                    __append('\n\n                                      ')

                    # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708671568
                    __attrs_4708671568 = _static_4459104240
                    __backup_view_4708674352 = get('view', __marker)

                    # <Value 'nocall:group' (147:62)> -> __value
                    __token = 9219
                    try:
                        __zt_tmp = __attrs_4708671568
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4459168576('nocall', 'group', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                    econtext['view'] = __value
                    __append('\n                                          ')

                    # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708667536
                    __attrs_4708667536 = _static_4459104240
                    __backup_macroname_4557297408 = get('macroname', __marker)

                    # <Static value=<ast.Constant object at 0x118a88100> name=None at 118a880d0> -> __value
                    __value = _static_4708663552
                    econtext['macroname'] = __value

                    # <Value 'context/@@ploneform-macros/widget_rendering' (148:66)> -> __macro
                    __token = 9300
                    try:
                        __zt_tmp = __attrs_4708667536
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __macro = _static_4459168576('path', 'context/@@ploneform-macros/widget_rendering', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                    __token = 9300
                    __m = __macro.include
                    __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    if (__backup_macroname_4557297408 is __marker):
                        del econtext['macroname']
                    else:
                        econtext['macroname'] = __backup_macroname_4557297408
                    __append('\n                                      ')
                    if (__backup_view_4708674352 is __marker):
                        del econtext['view']
                    else:
                        econtext['view'] = __backup_view_4708674352
                    __append('\n\n                              </fieldset>')
                    if (__backup_fieldset_name_4708644368 is __marker):
                        del econtext['fieldset_name']
                    else:
                        econtext['fieldset_name'] = __backup_fieldset_name_4708644368
                    if (__backup_fieldset_name_4708631840 is __marker):
                        del econtext['fieldset_name']
                    else:
                        econtext['fieldset_name'] = __backup_fieldset_name_4708631840
                    if (__backup_fieldset_label_4708636448 is __marker):
                        del econtext['fieldset_label']
                    else:
                        econtext['fieldset_label'] = __backup_fieldset_label_4708636448
                    if (__backup_normalizeString_4708645520 is __marker):
                        del econtext['normalizeString']
                    else:
                        econtext['normalizeString'] = __backup_normalizeString_4708645520
                    __append('\n                          ')
                    ____index_4708643600 -= 1
                    if (____index_4708643600 > 0):
                        __append('')
                if (__backup_group_4708633136 is __marker):
                    del econtext['group']
                else:
                    econtext['group'] = __backup_group_4708633136
            __append('\n\n                      ')
            if (__backup_has_groups_4708712848 is __marker):
                del econtext['has_groups']
            else:
                econtext['has_groups'] = __backup_has_groups_4708712848
            if (__backup_show_default_label_4708728784 is __marker):
                del econtext['show_default_label']
            else:
                econtext['show_default_label'] = __backup_show_default_label_4708728784
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_widget_rendering(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_field = econtext['__slot_field'].pop()
        except:
            __slot_field = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708644896
            __attrs_4708644896 = _static_4459104240
            __append('\n                                  ')

            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708641872
            __attrs_4708641872 = _static_4459104240
            __backup_widget_4708639520 = get('widget', __marker)

            # <Value 'python:view.widgets.values()' (104:62)> -> __iterator
            __token = 6359
            try:
                __zt_tmp = __attrs_4708641872
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4459168576('python', 'view.widgets.values()', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            (__iterator, ____index_4708643264, ) = getname('repeat')('widget', __iterator)
            econtext['widget'] = None
            for __item in __iterator:
                econtext['widget'] = __item
                __append('\n                                      ')
                if (__slot_field is None):

                    # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708644416
                    __attrs_4708644416 = _static_4459104240
                    __append('\n                                          ')
                    __token = None
                    render_field(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    __append('\n                                      ')
                else:
                    __slot_field(__stream, econtext.copy(), rcontext)
                __append('\n                                  ')
                ____index_4708643264 -= 1
                if (____index_4708643264 > 0):
                    __append('')
            if (__backup_widget_4708639520 is __marker):
                del econtext['widget']
            else:
                econtext['widget'] = __backup_widget_4708639520
            __append('\n                              ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_field(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708641920
            __attrs_4708641920 = _static_4459104240
            __append('\n                                              ')

            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708637120
            __attrs_4708637120 = _static_4459104240

            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708631888
            __default_4708631888 = _DEFAULT_MARKER

            # <Value 'widget/@@ploneform-render-widget' (107:81)> -> __cache_4708634384
            __token = 6625
            try:
                __zt_tmp = __attrs_4708637120
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4708634384 = _static_4459168576('path', 'widget/@@ploneform-render-widget', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

            # <BinOp left=<Value 'widget/@@ploneform-render-widget' (107:81)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118a816f0> -> __condition
            __expression = __cache_4708634384

            # <Symbol value=<DEFAULT> at 109c89f90> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4708634384
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n                                          ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_actions(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708665424
            __attrs_4708665424 = _static_4459104240
            __append('\n                        ')

            # <Static value=<ast.Dict object at 0x118a89960> name=None at 118a88520> -> __attrs_4708665712
            __attrs_4708665712 = _static_4708669792

            # <Value 'view/actions/values|nothing' (161:65)> -> __condition
            __token = 9808
            try:
                __zt_tmp = __attrs_4708665712
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4459168576('path', 'view/actions/values|nothing', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="formControls">\n                          ')

                # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708665136
                __attrs_4708665136 = _static_4459104240
                __backup_action_4708640864 = get('action', __marker)

                # <Value 'view/actions/values' (162:52)> -> __iterator
                __token = 9890
                try:
                    __zt_tmp = __attrs_4708665136
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4459168576('path', 'view/actions/values', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                (__iterator, ____index_4708664656, ) = getname('repeat')('action', __iterator)
                econtext['action'] = None
                for __item in __iterator:
                    econtext['action'] = __item
                    __append('\n                            ')

                    # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708679632
                    __attrs_4708679632 = _static_4459104240

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708667344
                    __default_4708667344 = _DEFAULT_MARKER

                    # <Value 'action/render' (163:58)> -> __cache_4708664992
                    __token = 9970
                    try:
                        __zt_tmp = __attrs_4708679632
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4708664992 = _static_4459168576('path', 'action/render', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

                    # <BinOp left=<Value 'action/render' (163:58)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118a882b0> -> __condition
                    __expression = __cache_4708664992

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input />')
                    else:
                        __content = __cache_4708664992
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n                          ')
                    ____index_4708664656 -= 1
                    if (____index_4708664656 > 0):
                        __append('')
                if (__backup_action_4708640864 is __marker):
                    del econtext['action']
                else:
                    econtext['action'] = __backup_action_4708640864
                __append('\n                       </div>')
            __append('\n                      ')
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

            # <Static value=<ast.Dict object at 0x118aa1750> name=None at 118aa1bd0> -> __attrs_4708769008
            __attrs_4708769008 = _static_4708767568
            __previous_i18n_domain_4708767376 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml">\n\n    ')

            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708764064
            __attrs_4708764064 = _static_4459104240

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n\n        ')
            __token = None
            render_form(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n    </body>\n</html>')
            __i18n_domain = __previous_i18n_domain_4708767376
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_form': render_form, 'render_titlelessform': render_titlelessform, 'render_fields': render_fields, 'render_widget_rendering': render_widget_rendering, 'render_field': render_field, 'render_actions': render_actions, 'render': render, }