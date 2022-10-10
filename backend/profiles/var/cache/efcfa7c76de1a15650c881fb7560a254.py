# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/schemaeditor/browser/schema/schema_listing.pt'

__tokens = {306: ('${context/absolute_url}/@@add-field', 7, 11), 308: ('context/absolute_url', 7, 13), 512: ('context/enableFieldsets', 12, 90), 548: ('${context/absolute_url}/@@add-fieldset', 13, 11), 550: ('context/absolute_url', 13, 13), 817: ('context/@@authenticator/authenticator', 20, 36), 1896: ('python:[view] + list(view.groups)', 76, 35), 1976: ('repeat/group/index', 77, 44), 2036: (' python:view.can_delete_fieldset(group', 78, 40), 2115: ('string:fieldset-${fieldset_name}', 79, 37), 2188: (' string:kssattr-fieldset-${fieldset_name', 80, 39), 2283: ("s python:(repeat['group'].start or can_delete) and 'true' or 'fals", 81, 52), 2396: ('python:group.label or view.default_fieldset_label', 83, 41), 2478: ('group_name', 84, 31), 2610: ('python:context.enableFieldsets and can_delete', 86, 96), 2531: ('delete-fieldset-${fieldset_name}', 86, 17), 2549: ('fieldset_name', 86, 35), 2676: ('${context/absolute_url}/@@delete-fieldset?name=${python:group.__name__}&_authenticator=${context/@@authenticator/token}', 87, 19), 2678: ('context/absolute_url', 87, 21), 2725: ('python:group.__name__', 87, 68), 2765: ('context/@@authenticator/token', 87, 108), 2927: ('group/widgets/errors', 91, 40), 2985: ('errors', 92, 36), 3032: ('errors', 93, 39), 3113: ('not:nocall:error/widget', 95, 33), 3179: ('error/render', 96, 41), 3276: ('group/widgets/values', 100, 38), 3374: ('widget/disabled|nothing', 103, 25), 3424: (' python:view.protected_field(widget.field', 104, 25), 3505: ('python:disabled or protected', 106, 34), 3662: ('disabled', 108, 46), 3771: ("python:widget.__name__.split('.')[0]", 109, 72), 3874: ('widget/field/__name__', 110, 41), 3952: ('python:view.field_type(widget.field)', 111, 44), 4065: ('widget/@@ploneform-render-widget', 113, 50), 4217: ('python:not(disabled or protected)', 117, 34), 4332: ('widget/field/__name__', 118, 80), 4439: ('widget/field/__name__', 121, 41), 4517: ('python:view.field_type(widget.field)', 122, 44), 4755: ('python:view.edit_url(widget.field)', 127, 44), 4829: ('edit_url', 128, 38), 4924: ('edit_url', 130, 44), 5280: ('python:view.delete_url(widget.field)', 135, 46), 5356: ('delete_url', 136, 38), 5412: ('delete_url', 137, 44), 5553: ('widget/@@ploneform-render-widget', 141, 52), 700: ('context/@@ploneform-macros/form', 18, 31), 700: ('context/@@ploneform-macros/form', 18, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4684186624 = {'style': 'width: 80%', }
_static_4684187440 = {'class': 'schemaeditor-delete-field btn btn-sm btn-danger ms-1', 'title': 'Delete field', 'data-confirm_msg': 'Are you sure you want to delete this field?', 'href': 'delete_url', }
_static_4684189168 = {'class': 'fieldSettings pat-plone-modal btn btn-sm btn-secondary', 'href': 'edit_url', }
_static_4684189312 = {'class': 'fieldControls', }
_static_4685681024 = {'class': 'fieldLabel', }
_static_4685680016 = {'class': 'fieldPreview orderable', 'data-field_id': 'widget/field/__name__', }
_static_4685687888 = {'class': 'disabled-field-overlay', }
_static_4685683760 = {'class': 'fieldLabel', }
_static_4685690864 = {'class': 'fieldPreview fieldFromBehavior', }
_static_4685677808 = {'class': 'field error', }
_static_4682973776 = {'id': 'delete-fieldset-${fieldset_name}', 'class': 'btn btn-sm btn-danger', 'href': '${context/absolute_url}/@@delete-fieldset?name=${python:group.__name__}&_authenticator=${context/@@authenticator/token}', }
_static_4682985584 = {'id': 'string:fieldset-${fieldset_name}', 'class': 'string:kssattr-fieldset-${fieldset_name}', 'data-can-add-fields': "python:(repeat['group'].start or can_delete) and 'true' or 'false'", }
_static_4682978192 = {'type': 'text/css', }
_static_4682544080 = 'form'
_static_4428767312 = {}
_static_4682538896 = {'id': 'add-fieldset', 'class': 'pat-plone-modal btn btn-secondary float-end', 'href': '${context/absolute_url}/@@add-fieldset', }
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
_static_4682544656 = {'id': 'add-field', 'class': 'pat-plone-modal btn btn-secondary float-end ms-3', 'href': '${context/absolute_url}/@@add-field', }
_static_4682706576 = {'class': 'pat-schemaeditor', }

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

            # <Static value=<ast.Dict object at 0x1171c6e90> name=None at 1171c6110> -> __attrs_4682697264
            __attrs_4682697264 = _static_4682706576
            __previous_i18n_domain_4682699520 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="pat-schemaeditor">\n  ')

            # <Static value=<ast.Dict object at 0x11719f610> name=None at 11719c5e0> -> __attrs_4682542880
            __attrs_4682542880 = _static_4682544656

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a id="add-field" class="pat-plone-modal btn btn-secondary float-end ms-3"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682542928
            __default_4682542928 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${context/absolute_url}/@@add-field' (7:11)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11719d0f0> -> __attr_href
            __token = 306
            __token = 308
            try:
                __zt_tmp = __attrs_4682542880
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4427992992('path', 'context/absolute_url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = ('%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/@@add-field', ))
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
            __stream_4682541536 = []
            __append_4682541536 = __stream_4682541536.append
            __append_4682541536('\n     Add new field&hellip;\n  ')
            __msgid_4682541536 = __re_whitespace(''.join(__stream_4682541536)).strip()
            if 'add_new_field_hellip':
                __append(translate('add_new_field_hellip', mapping=None, default=__msgid_4682541536, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n\n  ')

            # <Static value=<ast.Dict object at 0x11719df90> name=None at 11719cca0> -> __attrs_4682530976
            __attrs_4682530976 = _static_4682538896

            # <Value 'context/enableFieldsets' (12:90)> -> __condition
            __token = 512
            try:
                __zt_tmp = __attrs_4682530976
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'context/enableFieldsets', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a id="add-fieldset" class="pat-plone-modal btn btn-secondary float-end"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682540864
                __default_4682540864 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${context/absolute_url}/@@add-fieldset' (13:11)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11719e1a0> -> __attr_href
                __token = 548
                __token = 550
                try:
                    __zt_tmp = __attrs_4682530976
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4427992992('path', 'context/absolute_url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_href = ('%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/@@add-fieldset', ))
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
                __stream_4682532944 = []
                __append_4682532944 = __stream_4682532944.append
                __append_4682532944('\n     Add new fieldset&hellip;\n  ')
                __msgid_4682532944 = __re_whitespace(''.join(__stream_4682532944)).strip()
                if 'add_fieldset_hellip':
                    __append(translate('add_fieldset_hellip', mapping=None, default=__msgid_4682532944, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</a>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682543552
            __attrs_4682543552 = _static_4428767312
            __backup_macroname_4687157312 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x11719f3d0> name=None at 11719c0d0> -> __value
            __value = _static_4682544080
            econtext['macroname'] = __value

            def __fill_formtop(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682978000
                __attrs_4682978000 = _static_4428767312
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682976128
                __attrs_4682976128 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682986400
                __default_4682986400 = _DEFAULT_MARKER

                # <Value 'context/@@authenticator/authenticator' (20:36)> -> __cache_4682987552
                __token = 817
                try:
                    __zt_tmp = __attrs_4682976128
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4682987552 = _static_4427992992('path', 'context/@@authenticator/authenticator', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'context/@@authenticator/authenticator' (20:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1172080d0> -> __condition
                __expression = __cache_4682987552

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input />')
                else:
                    __content = __cache_4682987552
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x117209390> name=None at 11720b790> -> __attrs_4682975408
                __attrs_4682975408 = _static_4682978192

                # <style ... (0:0)
                # --------------------------------------------------------
                __append('<style type="text/css">\n  .fieldPreview {\n    background: #eee;\n    padding: 1em 1em 1px 1em;\n    margin: 0.5em 0;\n    -moz-border-radius: 0.5em;\n    position: relative;\n    border: solid 2px #ccc;\n  }\n  .field {\n    clear: left;\n  }\n\n  .fieldFromBehavior {\n    border: dashed 2px #ccc;\n  }\n\n  .fieldFromBehavior .disabled-field-overlay {\n    position: absolute;\n    top: 0;\n    left: 0;\n    height: 100%;\n    width: 100%;\n    z-index: 2;\n    background: #fff;\n    opacity: 0.6;\n  }\n\n  .fieldLabel {\n    float: left;\n    background: #ddd;\n    border-right: solid 1px #fff;\n    border-bottom: solid 1px #fff;\n    -moz-border-radius-bottomright: 0.5em;\n    margin: -1em -1em 0;\n    padding: 0 0.5em;\n    position: relative;\n    z-index: 3;\n  }\n\n  .fieldFromBehavior .fieldLabel {\n    outline-width-top: 0;\n    outline-left: none;\n  }\n\n  .fieldControls {\n    position: absolute;\n    top: 0;\n    right: 1em;\n  }\n      </style>\n    ')
            _slots = econtext['__slot_formtop'] = _deque((__fill_formtop, ))

            def __fill_fields(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682981600
                __attrs_4682981600 = _static_4428767312
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682986112
                __attrs_4682986112 = _static_4428767312
                __backup_group_4682535824 = get('group', __marker)

                # <Value 'python:[view] + list(view.groups)' (76:35)> -> __iterator
                __token = 1896
                try:
                    __zt_tmp = __attrs_4682986112
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4427992992('python', '[view] + list(view.groups)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                (__iterator, ____index_4682973440, ) = getname('repeat')('group', __iterator)
                econtext['group'] = None
                for __item in __iterator:
                    econtext['group'] = __item
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x11720b070> name=None at 11720bd00> -> __attrs_4682974976
                    __attrs_4682974976 = _static_4682985584
                    __backup_fieldset_name_4682546048 = get('fieldset_name', __marker)

                    # <Value 'repeat/group/index' (77:44)> -> __value
                    __token = 1976
                    try:
                        __zt_tmp = __attrs_4682974976
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4427992992('path', 'repeat/group/index', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    econtext['fieldset_name'] = __value
                    __backup_can_delete_4682980400 = get('can_delete', __marker)

                    # <Value 'python:view.can_delete_fieldset(group)' (78:40)> -> __value
                    __token = 2036
                    try:
                        __zt_tmp = __attrs_4682974976
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4427992992('python', 'view.can_delete_fieldset(group)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    econtext['can_delete'] = __value

                    # <fieldset ... (0:0)
                    # --------------------------------------------------------
                    __append('<fieldset')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682989232
                    __default_4682989232 = _DEFAULT_MARKER

                    # <Substitution 'string:fieldset-${fieldset_name}' (79:37)> -> __attr_id
                    __token = 2115
                    try:
                        __zt_tmp = __attrs_4682974976
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_4427992992('string', 'fieldset-${fieldset_name}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682985680
                    __default_4682985680 = _DEFAULT_MARKER

                    # <Substitution 'string:kssattr-fieldset-${fieldset_name}' (80:39)> -> __attr_class
                    __token = 2188
                    try:
                        __zt_tmp = __attrs_4682974976
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4427992992('string', 'kssattr-fieldset-${fieldset_name}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682986976
                    __default_4682986976 = _DEFAULT_MARKER

                    # <Substitution "python:(repeat['group'].start or can_delete) and 'true' or 'false'" (81:52)> -> __attr_data_can_add_fields
                    __token = 2283
                    try:
                        __zt_tmp = __attrs_4682974976
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_data_can_add_fields = _static_4427992992('python', "(repeat['group'].start or can_delete) and 'true' or 'false'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_data_can_add_fields = __quote(__attr_data_can_add_fields, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_data_can_add_fields is not None):
                        __append((' data-can-add-fields="%s"' % __attr_data_can_add_fields))
                    __append('>\n\n          ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682976368
                    __attrs_4682976368 = _static_4428767312
                    __backup_group_name_4682980352 = get('group_name', __marker)

                    # <Value 'python:group.label or view.default_fieldset_label' (83:41)> -> __value
                    __token = 2396
                    try:
                        __zt_tmp = __attrs_4682976368
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4427992992('python', 'group.label or view.default_fieldset_label', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    econtext['group_name'] = __value

                    # <legend ... (0:0)
                    # --------------------------------------------------------
                    __append('<legend>')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682980640
                    __default_4682980640 = _DEFAULT_MARKER

                    # <Value 'group_name' (84:31)> -> __cache_4682985008
                    __token = 2478
                    try:
                        __zt_tmp = __attrs_4682976368
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4682985008 = _static_4427992992('path', 'group_name', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'group_name' (84:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 117209cc0> -> __condition
                    __expression = __cache_4682985008

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Fieldset name')
                    else:
                        __content = __cache_4682985008
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</legend>')
                    if (__backup_group_name_4682980352 is __marker):
                        del econtext['group_name']
                    else:
                        econtext['group_name'] = __backup_group_name_4682980352
                    __append('\n\n          ')

                    # <Static value=<ast.Dict object at 0x117208250> name=None at 11720ba00> -> __attrs_4682983136
                    __attrs_4682983136 = _static_4682973776

                    # <Value 'python:context.enableFieldsets and can_delete' (86:96)> -> __condition
                    __token = 2610
                    try:
                        __zt_tmp = __attrs_4682983136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('python', 'context.enableFieldsets and can_delete', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682987312
                        __default_4682987312 = _DEFAULT_MARKER

                        # <Interpolation value=<Substitution 'delete-fieldset-${fieldset_name}' (86:17)> braces_required=True translation=False default='"?"' default_marker='"?"' at 117208520> -> __attr_id
                        __token = 2531
                        __token = 2549
                        try:
                            __zt_tmp = __attrs_4682983136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_4427992992('path', 'fieldset_name', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        __attr_id = ('%s%s' % ('delete-fieldset-', (__attr_id if (__attr_id is not None) else ''), ))
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
                        __append(' class="btn btn-sm btn-danger"')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682989520
                        __default_4682989520 = _DEFAULT_MARKER

                        # <Interpolation value=<Substitution '${context/absolute_url}/@@delete-fieldset?name=${python:group.__name__}&_authenticator=${context/@@authenticator/token}' (87:19)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11720a9e0> -> __attr_href
                        __token = 2676
                        __token = 2678
                        try:
                            __zt_tmp = __attrs_4682983136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4427992992('path', 'context/absolute_url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        __token = 2725
                        try:
                            __zt_tmp = __attrs_4682983136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href_2723 = _static_4427992992('python', 'group.__name__', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_href_2723 = __quote(__attr_href_2723, '"', '&quot;', None, _DEFAULT_MARKER)
                        __token = 2765
                        try:
                            __zt_tmp = __attrs_4682983136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href_2763 = _static_4427992992('path', 'context/@@authenticator/token', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_href_2763 = __quote(__attr_href_2763, '"', '&quot;', None, _DEFAULT_MARKER)
                        __attr_href = ('%s%s%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/@@delete-fieldset?name=', (__attr_href_2723 if (__attr_href_2723 is not None) else ''), '&_authenticator=', (__attr_href_2763 if (__attr_href_2763 is not None) else ''), ))
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
                        __stream_4682977376 = []
                        __append_4682977376 = __stream_4682977376.append
                        __append_4682977376('Delete fieldset\n          ')
                        __msgid_4682977376 = __re_whitespace(''.join(__stream_4682977376)).strip()
                        if 'delete_fieldset_hellip':
                            __append(translate('delete_fieldset_hellip', mapping=None, default=__msgid_4682977376, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</a>')
                    __append('\n\n          ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4676572240
                    __attrs_4676572240 = _static_4428767312
                    __backup_errors_4682981840 = get('errors', __marker)

                    # <Value 'group/widgets/errors' (91:40)> -> __value
                    __token = 2927
                    try:
                        __zt_tmp = __attrs_4676572240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4427992992('path', 'group/widgets/errors', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    econtext['errors'] = __value

                    # <Value 'errors' (92:36)> -> __condition
                    __token = 2985
                    try:
                        __zt_tmp = __attrs_4676572240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('path', 'errors', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:
                        __backup_error_4682978768 = get('error', __marker)

                        # <Value 'errors' (93:39)> -> __iterator
                        __token = 3032
                        try:
                            __zt_tmp = __attrs_4676572240
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_4427992992('path', 'errors', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        (__iterator, ____index_4676576272, ) = getname('repeat')('error', __iterator)
                        econtext['error'] = None
                        for __item in __iterator:
                            econtext['error'] = __item
                            __append('\n              ')

                            # <Static value=<ast.Dict object at 0x11749c4f0> name=None at 11749e920> -> __attrs_4685682080
                            __attrs_4685682080 = _static_4685677808

                            # <Value 'not:nocall:error/widget' (95:33)> -> __condition
                            __token = 3113
                            try:
                                __zt_tmp = __attrs_4685682080
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4427992992('not', 'nocall:error/widget', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="field error">')

                                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685692688
                                __default_4685692688 = _DEFAULT_MARKER

                                # <Value 'error/render' (96:41)> -> __cache_4664498336
                                __token = 3179
                                try:
                                    __zt_tmp = __attrs_4685682080
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_4664498336 = _static_4427992992('path', 'error/render', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                                # <BinOp left=<Value 'error/render' (96:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116068d90> -> __condition
                                __expression = __cache_4664498336

                                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_4664498336
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append('</div>')
                            __append('\n          ')
                            ____index_4676576272 -= 1
                            if (____index_4676576272 > 0):
                                __append('')
                        if (__backup_error_4682978768 is __marker):
                            del econtext['error']
                        else:
                            econtext['error'] = __backup_error_4682978768
                    if (__backup_errors_4682981840 is __marker):
                        del econtext['errors']
                    else:
                        econtext['errors'] = __backup_errors_4682981840
                    __append('\n\n          ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4685686640
                    __attrs_4685686640 = _static_4428767312
                    __backup_widget_4682980160 = get('widget', __marker)

                    # <Value 'group/widgets/values' (100:38)> -> __iterator
                    __token = 3276
                    try:
                        __zt_tmp = __attrs_4685686640
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_4427992992('path', 'group/widgets/values', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    (__iterator, ____index_4685688944, ) = getname('repeat')('widget', __iterator)
                    econtext['widget'] = None
                    for __item in __iterator:
                        econtext['widget'] = __item
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4685692352
                        __attrs_4685692352 = _static_4428767312
                        __backup_disabled_4676574544 = get('disabled', __marker)

                        # <Value 'widget/disabled|nothing' (103:25)> -> __value
                        __token = 3374
                        try:
                            __zt_tmp = __attrs_4685692352
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4427992992('path', 'widget/disabled|nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        econtext['disabled'] = __value
                        __backup_protected_4676581312 = get('protected', __marker)

                        # <Value 'python:view.protected_field(widget.field)' (104:25)> -> __value
                        __token = 3424
                        try:
                            __zt_tmp = __attrs_4685692352
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4427992992('python', 'view.protected_field(widget.field)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        econtext['protected'] = __value
                        __append('\n\n              ')

                        # <Static value=<ast.Dict object at 0x11749f7f0> name=None at 11749f280> -> __attrs_4685684960
                        __attrs_4685684960 = _static_4685690864

                        # <Value 'python:disabled or protected' (106:34)> -> __condition
                        __token = 3505
                        try:
                            __zt_tmp = __attrs_4685684960
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4427992992('python', 'disabled or protected', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="fieldPreview fieldFromBehavior">\n                ')

                            # <Static value=<ast.Dict object at 0x11749dc30> name=None at 11749e3e0> -> __attrs_4685684192
                            __attrs_4685684192 = _static_4685683760

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="fieldLabel">\n                    ')

                            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4685683856
                            __attrs_4685683856 = _static_4428767312

                            # <Value 'disabled' (108:46)> -> __condition
                            __token = 3662
                            try:
                                __zt_tmp = __attrs_4685683856
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4427992992('path', 'disabled', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                            if __condition:
                                __stream_4670264416_behavior_name = ''
                                __stream_4685682896 = []
                                __append_4685682896 = __stream_4685682896.append
                                __append_4685682896('From the\n                      ')
                                __stream_4670264416_behavior_name = []
                                __append_4670264416_behavior_name = __stream_4670264416_behavior_name.append

                                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4685679344
                                __attrs_4685679344 = _static_4428767312

                                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685688176
                                __default_4685688176 = _DEFAULT_MARKER

                                # <Value "python:widget.__name__.split('.')[0]" (109:72)> -> __cache_4685679392
                                __token = 3771
                                try:
                                    __zt_tmp = __attrs_4685679344
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_4685679392 = _static_4427992992('python', "widget.__name__.split('.')[0]", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                                # <BinOp left=<Value "python:widget.__name__.split('.')[0]" (109:72)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 11749ccd0> -> __condition
                                __expression = __cache_4685679392

                                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_4685679392
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append_4670264416_behavior_name(__content)
                                __append_4685682896('${behavior_name}')
                                __stream_4670264416_behavior_name = ''.join(__stream_4670264416_behavior_name)
                                __append_4685682896(' behavior:')
                                __msgid_4685682896 = __re_whitespace(''.join(__stream_4685682896)).strip()
                                if __msgid_4685682896:
                                    __append(translate(__msgid_4685682896, mapping={'behavior_name': __stream_4670264416_behavior_name, }, default=__msgid_4685682896, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('\n                    ')

                            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4685688416
                            __attrs_4685688416 = _static_4428767312

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append('<strong>')

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685685200
                            __default_4685685200 = _DEFAULT_MARKER

                            # <Value 'widget/field/__name__' (110:41)> -> __cache_4685683376
                            __token = 3874
                            try:
                                __zt_tmp = __attrs_4685688416
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4685683376 = _static_4427992992('path', 'widget/field/__name__', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                            # <BinOp left=<Value 'widget/field/__name__' (110:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 11749cfa0> -> __condition
                            __expression = __cache_4685683376

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_4685683376
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('</strong> &ndash;\n                    ')

                            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4685680448
                            __attrs_4685680448 = _static_4428767312

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685688224
                            __default_4685688224 = _DEFAULT_MARKER

                            # <Value 'python:view.field_type(widget.field)' (111:44)> -> __cache_4685687936
                            __token = 3952
                            try:
                                __zt_tmp = __attrs_4685680448
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4685687936 = _static_4427992992('python', 'view.field_type(widget.field)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                            # <BinOp left=<Value 'python:view.field_type(widget.field)' (111:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 11749ead0> -> __condition
                            __expression = __cache_4685687936

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_4685687936
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('\n                </div>\n                ')

                            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4685683136
                            __attrs_4685683136 = _static_4428767312

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685691488
                            __default_4685691488 = _DEFAULT_MARKER

                            # <Value 'widget/@@ploneform-render-widget' (113:50)> -> __cache_4685680688
                            __token = 4065
                            try:
                                __zt_tmp = __attrs_4685683136
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4685680688 = _static_4427992992('path', 'widget/@@ploneform-render-widget', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                            # <BinOp left=<Value 'widget/@@ploneform-render-widget' (113:50)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 11749d270> -> __condition
                            __expression = __cache_4685680688

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_4685680688
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append('\n                ')

                            # <Static value=<ast.Dict object at 0x11749ec50> name=None at 11749cc10> -> __attrs_4685685248
                            __attrs_4685685248 = _static_4685687888

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="disabled-field-overlay"></div>\n              </div>')
                        __append('\n\n              ')

                        # <Static value=<ast.Dict object at 0x11749cd90> name=None at 11749fa30> -> __attrs_4685687216
                        __attrs_4685687216 = _static_4685680016

                        # <Value 'python:not(disabled or protected)' (117:34)> -> __condition
                        __token = 4217
                        try:
                            __zt_tmp = __attrs_4685687216
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4427992992('python', 'not(disabled or protected)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="fieldPreview orderable"')

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685681744
                            __default_4685681744 = _DEFAULT_MARKER

                            # <Substitution 'widget/field/__name__' (118:80)> -> __attr_data_field_id
                            __token = 4332
                            try:
                                __zt_tmp = __attrs_4685687216
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_data_field_id = _static_4427992992('path', 'widget/field/__name__', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                            __attr_data_field_id = __quote(__attr_data_field_id, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_data_field_id is not None):
                                __append((' data-field_id="%s"' % __attr_data_field_id))
                            __append('>\n\n                ')

                            # <Static value=<ast.Dict object at 0x11749d180> name=None at 11749ec20> -> __attrs_4684192480
                            __attrs_4684192480 = _static_4685681024

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="fieldLabel">\n                    ')

                            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4684199200
                            __attrs_4684199200 = _static_4428767312

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append('<strong>')

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684194544
                            __default_4684194544 = _DEFAULT_MARKER

                            # <Value 'widget/field/__name__' (121:41)> -> __cache_4684199056
                            __token = 4439
                            try:
                                __zt_tmp = __attrs_4684199200
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4684199056 = _static_4427992992('path', 'widget/field/__name__', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                            # <BinOp left=<Value 'widget/field/__name__' (121:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1173333a0> -> __condition
                            __expression = __cache_4684199056

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_4684199056
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('</strong> &ndash;\n                    ')

                            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4684201840
                            __attrs_4684201840 = _static_4428767312

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684190704
                            __default_4684190704 = _DEFAULT_MARKER

                            # <Value 'python:view.field_type(widget.field)' (122:44)> -> __cache_4684196560
                            __token = 4517
                            try:
                                __zt_tmp = __attrs_4684201840
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4684196560 = _static_4427992992('python', 'view.field_type(widget.field)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                            # <BinOp left=<Value 'python:view.field_type(widget.field)' (122:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 117332710> -> __condition
                            __expression = __cache_4684196560

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_4684196560
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('\n                </div>\n\n                ')

                            # <Static value=<ast.Dict object at 0x117330e80> name=None at 1173301f0> -> __attrs_4684186432
                            __attrs_4684186432 = _static_4684189312

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="fieldControls">\n                    ')

                            # <Static value=<ast.Dict object at 0x117330df0> name=None at 117333e20> -> __attrs_4684186576
                            __attrs_4684186576 = _static_4684189168
                            __backup_edit_url_4685677520 = get('edit_url', __marker)

                            # <Value 'python:view.edit_url(widget.field)' (127:44)> -> __value
                            __token = 4755
                            try:
                                __zt_tmp = __attrs_4684186576
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4427992992('python', 'view.edit_url(widget.field)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                            econtext['edit_url'] = __value

                            # <Value 'edit_url' (128:38)> -> __condition
                            __token = 4829
                            try:
                                __zt_tmp = __attrs_4684186576
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4427992992('path', 'edit_url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                            if __condition:

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append('<a class="fieldSettings pat-plone-modal btn btn-sm btn-secondary"')

                                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684190320
                                __default_4684190320 = _DEFAULT_MARKER

                                # <Substitution 'edit_url' (130:44)> -> __attr_href
                                __token = 4924
                                try:
                                    __zt_tmp = __attrs_4684186576
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_4427992992('path', 'edit_url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_href is not None):
                                    __append((' href="%s"' % __attr_href))
                                __append('>')
                                __stream_4684196464 = []
                                __append_4684196464 = __stream_4684196464.append
                                __append_4684196464('Settings&hellip;')
                                __msgid_4684196464 = __re_whitespace(''.join(__stream_4684196464)).strip()
                                if __msgid_4684196464:
                                    __append(translate(__msgid_4684196464, mapping=None, default=__msgid_4684196464, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                __append('</a>')
                            if (__backup_edit_url_4685677520 is __marker):
                                del econtext['edit_url']
                            else:
                                econtext['edit_url'] = __backup_edit_url_4685677520
                            __append('\n                    ')

                            # <Static value=<ast.Dict object at 0x117330730> name=None at 1173304f0> -> __attrs_4684195648
                            __attrs_4684195648 = _static_4684187440
                            __backup_delete_url_4685678672 = get('delete_url', __marker)

                            # <Value 'python:view.delete_url(widget.field)' (135:46)> -> __value
                            __token = 5280
                            try:
                                __zt_tmp = __attrs_4684195648
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4427992992('python', 'view.delete_url(widget.field)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                            econtext['delete_url'] = __value

                            # <Value 'delete_url' (136:38)> -> __condition
                            __token = 5356
                            try:
                                __zt_tmp = __attrs_4684195648
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4427992992('path', 'delete_url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                            if __condition:

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append('<a class="schemaeditor-delete-field btn btn-sm btn-danger ms-1"')

                                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684201216
                                __default_4684201216 = _DEFAULT_MARKER

                                # <Translate msgid=None node=<ast.Constant object at 0x117333d60> at 117333be0> -> __attr_title
                                __attr_title = 'Delete field'
                                __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                if (__attr_title is not None):
                                    __append((' title="%s"' % __attr_title))

                                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684200736
                                __default_4684200736 = _DEFAULT_MARKER

                                # <Translate msgid=None node=<ast.Constant object at 0x117333700> at 117330820> -> __attr_data_confirm_msg
                                __attr_data_confirm_msg = 'Are you sure you want to delete this field?'
                                __attr_data_confirm_msg = translate(__attr_data_confirm_msg, default=__attr_data_confirm_msg, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                if (__attr_data_confirm_msg is not None):
                                    __append((' data-confirm_msg="%s"' % __attr_data_confirm_msg))

                                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684195456
                                __default_4684195456 = _DEFAULT_MARKER

                                # <Substitution 'delete_url' (137:44)> -> __attr_href
                                __token = 5412
                                try:
                                    __zt_tmp = __attrs_4684195648
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_4427992992('path', 'delete_url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_href is not None):
                                    __append((' href="%s"' % __attr_href))
                                __append('>&times;</a>')
                            if (__backup_delete_url_4685678672 is __marker):
                                del econtext['delete_url']
                            else:
                                econtext['delete_url'] = __backup_delete_url_4685678672
                            __append('\n                </div>\n\n                ')

                            # <Static value=<ast.Dict object at 0x117330400> name=None at 117333bb0> -> __attrs_4684197040
                            __attrs_4684197040 = _static_4684186624

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div style="width: 80%">\n                  ')

                            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4684198144
                            __attrs_4684198144 = _static_4428767312

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684190896
                            __default_4684190896 = _DEFAULT_MARKER

                            # <Value 'widget/@@ploneform-render-widget' (141:52)> -> __cache_4684194400
                            __token = 5553
                            try:
                                __zt_tmp = __attrs_4684198144
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4684194400 = _static_4427992992('path', 'widget/@@ploneform-render-widget', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                            # <BinOp left=<Value 'widget/@@ploneform-render-widget' (141:52)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 117331120> -> __condition
                            __expression = __cache_4684194400

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_4684194400
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append('\n                </div>\n\n              </div>')
                        __append('\n            ')
                        if (__backup_protected_4676581312 is __marker):
                            del econtext['protected']
                        else:
                            econtext['protected'] = __backup_protected_4676581312
                        if (__backup_disabled_4676574544 is __marker):
                            del econtext['disabled']
                        else:
                            econtext['disabled'] = __backup_disabled_4676574544
                        __append('\n\n          ')
                        ____index_4685688944 -= 1
                        if (____index_4685688944 > 0):
                            __append('')
                    if (__backup_widget_4682980160 is __marker):
                        del econtext['widget']
                    else:
                        econtext['widget'] = __backup_widget_4682980160
                    __append('\n\n        </fieldset>')
                    if (__backup_can_delete_4682980400 is __marker):
                        del econtext['can_delete']
                    else:
                        econtext['can_delete'] = __backup_can_delete_4682980400
                    if (__backup_fieldset_name_4682546048 is __marker):
                        del econtext['fieldset_name']
                    else:
                        econtext['fieldset_name'] = __backup_fieldset_name_4682546048
                    __append('\n      ')
                    ____index_4682973440 -= 1
                    if (____index_4682973440 > 0):
                        __append('')
                if (__backup_group_4682535824 is __marker):
                    del econtext['group']
                else:
                    econtext['group'] = __backup_group_4682535824
                __append('\n    ')
            _slots = econtext['__slot_fields'] = _deque((__fill_fields, ))

            # <Value 'context/@@ploneform-macros/form' (18:31)> -> __macro
            __token = 700
            try:
                __zt_tmp = __attrs_4682543552
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4427992992('path', 'context/@@ploneform-macros/form', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __token = 700
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4687157312 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4687157312
            __append('\n</div>')
            __i18n_domain = __previous_i18n_domain_4682699520
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }