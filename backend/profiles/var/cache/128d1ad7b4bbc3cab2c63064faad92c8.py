# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/dexterity/browser/overview.pt'

__tokens = {221: ('view/widgets/title/@@ploneform-render-widget', 5, 36), 306: ('view/widgets/description/@@ploneform-render-widget', 6, 36), 389: ("python:'filter_content_types' in view.fields", 8, 27), 547: ('nocall:view/widgets/filter_content_types', 10, 35), 621: (' context/valu', 11, 32), 868: ('context/name', 16, 36), 920: (" python:'checked' if 'none' in value else Non", 17, 38), 1179: ('context/name', 22, 38), 1231: (" python:'checked' if 'all' in value else Non", 23, 38), 1492: ('context/name', 28, 38), 1544: (" python:'checked' if 'some' in value else Non", 29, 38), 1733: ('view/widgets/allowed_content_types/render', 31, 44), 679: ('context/@@ploneform-render-widget/widget-wrapper', 12, 41), 679: ('context/@@ploneform-render-widget/widget-wrapper', 12, 41), 27: ('context/@@ploneform-macros/titlelessform', 1, 27), 27: ('context/@@ploneform-macros/titlelessform', 1, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4664799392 = {'type': 'radio', 'value': 'some', 'name': 'context/name', 'checked': "python:'checked' if 'some' in value else None", }
_static_4681904816 = {'type': 'radio', 'value': 'all', 'name': 'context/name', 'checked': "python:'checked' if 'all' in value else None", }
_static_4681896464 = {'type': 'radio', 'value': 'none', 'name': 'context/name', 'checked': "python:'checked' if 'none' in value else None", }
_static_4681901600 = 'widget-wrapper'
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
_static_4682700912 = 'titlelessform'
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

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682705088
            __attrs_4682705088 = _static_4428767312
            __previous_i18n_domain_4682700576 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4686219712 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x1171c5870> name=None at 1171c7730> -> __value
            __value = _static_4682700912
            econtext['macroname'] = __value

            def __fill_fields(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682696496
                __attrs_4682696496 = _static_4428767312
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682696160
                __attrs_4682696160 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682701632
                __default_4682701632 = _DEFAULT_MARKER

                # <Value 'view/widgets/title/@@ploneform-render-widget' (5:36)> -> __cache_4682704176
                __token = 221
                try:
                    __zt_tmp = __attrs_4682696160
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4682704176 = _static_4427992992('path', 'view/widgets/title/@@ploneform-render-widget', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/widgets/title/@@ploneform-render-widget' (5:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1171c6aa0> -> __condition
                __expression = __cache_4682704176

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4682704176
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682698272
                __attrs_4682698272 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682694768
                __default_4682694768 = _DEFAULT_MARKER

                # <Value 'view/widgets/description/@@ploneform-render-widget' (6:36)> -> __cache_4682695584
                __token = 306
                try:
                    __zt_tmp = __attrs_4682698272
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4682695584 = _static_4427992992('path', 'view/widgets/description/@@ploneform-render-widget', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/widgets/description/@@ploneform-render-widget' (6:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1171c5bd0> -> __condition
                __expression = __cache_4682695584

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4682695584
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682710176
                __attrs_4682710176 = _static_4428767312

                # <Value "python:'filter_content_types' in view.fields" (8:27)> -> __condition
                __token = 389
                try:
                    __zt_tmp = __attrs_4682710176
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('python', "'filter_content_types' in view.fields", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <fieldset ... (0:0)
                    # --------------------------------------------------------
                    __append('<fieldset>\n    ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682695968
                    __attrs_4682695968 = _static_4428767312

                    # <legend ... (0:0)
                    # --------------------------------------------------------
                    __append('<legend>')
                    __stream_4682704752 = []
                    __append_4682704752 = __stream_4682704752.append
                    __append_4682704752('Contained items')
                    __msgid_4682704752 = __re_whitespace(''.join(__stream_4682704752)).strip()
                    if 'label_contained_items':
                        __append(translate('label_contained_items', mapping=None, default=__msgid_4682704752, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</legend>\n    ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682698608
                    __attrs_4682698608 = _static_4428767312
                    __backup_context_4680440064 = get('context', __marker)

                    # <Value 'nocall:view/widgets/filter_content_types' (10:35)> -> __value
                    __token = 547
                    try:
                        __zt_tmp = __attrs_4682698608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4427992992('nocall', 'view/widgets/filter_content_types', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    econtext['context'] = __value
                    __backup_value_4680534576 = get('value', __marker)

                    # <Value 'context/value' (11:32)> -> __value
                    __token = 621
                    try:
                        __zt_tmp = __attrs_4682698608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4427992992('path', 'context/value', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    econtext['value'] = __value
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4681893440
                    __attrs_4681893440 = _static_4428767312
                    __backup_macroname_4687066176 = get('macroname', __marker)

                    # <Static value=<ast.Constant object at 0x117102620> name=None at 1171004c0> -> __value
                    __value = _static_4681901600
                    econtext['macroname'] = __value

                    def __fill_widget(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                        getname = econtext.get_name
                        get = econtext.get

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4681894496
                        __attrs_4681894496 = _static_4428767312
                        __append('\n        ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4681901840
                        __attrs_4681901840 = _static_4428767312

                        # <label ... (0:0)
                        # --------------------------------------------------------
                        __append('<label>\n          ')

                        # <Static value=<ast.Dict object at 0x117101210> name=None at 117100880> -> __attrs_4681897376
                        __attrs_4681897376 = _static_4681896464

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="radio" value="none"')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4681894064
                        __default_4681894064 = _DEFAULT_MARKER

                        # <Substitution 'context/name' (16:36)> -> __attr_name
                        __token = 868
                        try:
                            __zt_tmp = __attrs_4681897376
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_4427992992('path', 'context/name', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4681902464
                        __default_4681902464 = _DEFAULT_MARKER

                        # <Boolean "python:'checked' if 'none' in value else None" (17:38)> -> __attr_checked
                        __token = 920
                        try:
                            __zt_tmp = __attrs_4681897376
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_checked = _static_4427992992('python', "'checked' if 'none' in value else None", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        if (__attr_checked is _DEFAULT_MARKER):
                            __attr_checked = None
                        else:
                            if __attr_checked:
                                __attr_checked = 'checked'
                            else:
                                __attr_checked = None
                        if (__attr_checked is not None):
                            __append((' checked="%s"' % __attr_checked))
                        __append('/>\n          ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4681893008
                        __attrs_4681893008 = _static_4428767312
                        __stream_4681892720 = []
                        __append_4681892720 = __stream_4681892720.append
                        __append_4681892720('No content types')
                        __msgid_4681892720 = __re_whitespace(''.join(__stream_4681892720)).strip()
                        if 'label_no_content_types':
                            __append(translate('label_no_content_types', mapping=None, default=__msgid_4681892720, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('\n        </label>')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4681899152
                        __attrs_4681899152 = _static_4428767312

                        # <br ... (0:0)
                        # --------------------------------------------------------
                        __append('<br />\n        ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4681900064
                        __attrs_4681900064 = _static_4428767312

                        # <label ... (0:0)
                        # --------------------------------------------------------
                        __append('<label>\n          ')

                        # <Static value=<ast.Dict object at 0x1171032b0> name=None at 117100bb0> -> __attrs_4681907264
                        __attrs_4681907264 = _static_4681904816

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="radio" value="all"')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4681901744
                        __default_4681901744 = _DEFAULT_MARKER

                        # <Substitution 'context/name' (22:38)> -> __attr_name
                        __token = 1179
                        try:
                            __zt_tmp = __attrs_4681907264
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_4427992992('path', 'context/name', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4681895408
                        __default_4681895408 = _DEFAULT_MARKER

                        # <Boolean "python:'checked' if 'all' in value else None" (23:38)> -> __attr_checked
                        __token = 1231
                        try:
                            __zt_tmp = __attrs_4681907264
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_checked = _static_4427992992('python', "'checked' if 'all' in value else None", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        if (__attr_checked is _DEFAULT_MARKER):
                            __attr_checked = None
                        else:
                            if __attr_checked:
                                __attr_checked = 'checked'
                            else:
                                __attr_checked = None
                        if (__attr_checked is not None):
                            __append((' checked="%s"' % __attr_checked))
                        __append('/>\n          ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4681901456
                        __attrs_4681901456 = _static_4428767312
                        __stream_4681902656 = []
                        __append_4681902656 = __stream_4681902656.append
                        __append_4681902656('All content types')
                        __msgid_4681902656 = __re_whitespace(''.join(__stream_4681902656)).strip()
                        if 'label_all_content_types':
                            __append(translate('label_all_content_types', mapping=None, default=__msgid_4681902656, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('\n        </label>')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4681898000
                        __attrs_4681898000 = _static_4428767312

                        # <br ... (0:0)
                        # --------------------------------------------------------
                        __append('<br />\n        ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4681900544
                        __attrs_4681900544 = _static_4428767312

                        # <label ... (0:0)
                        # --------------------------------------------------------
                        __append('<label>\n          ')

                        # <Static value=<ast.Dict object at 0x1160b30a0> name=None at 1160b36a0> -> __attrs_4685689328
                        __attrs_4685689328 = _static_4664799392

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="radio" value="some"')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685687264
                        __default_4685687264 = _DEFAULT_MARKER

                        # <Substitution 'context/name' (28:38)> -> __attr_name
                        __token = 1492
                        try:
                            __zt_tmp = __attrs_4685689328
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_4427992992('path', 'context/name', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685688800
                        __default_4685688800 = _DEFAULT_MARKER

                        # <Boolean "python:'checked' if 'some' in value else None" (29:38)> -> __attr_checked
                        __token = 1544
                        try:
                            __zt_tmp = __attrs_4685689328
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_checked = _static_4427992992('python', "'checked' if 'some' in value else None", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        if (__attr_checked is _DEFAULT_MARKER):
                            __attr_checked = None
                        else:
                            if __attr_checked:
                                __attr_checked = 'checked'
                            else:
                                __attr_checked = None
                        if (__attr_checked is not None):
                            __append((' checked="%s"' % __attr_checked))
                        __append('/>\n          ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4685676800
                        __attrs_4685676800 = _static_4428767312
                        __stream_4685677760 = []
                        __append_4685677760 = __stream_4685677760.append
                        __append_4685677760('Some content types:')
                        __msgid_4685677760 = __re_whitespace(''.join(__stream_4685677760)).strip()
                        if 'label_some_content_types':
                            __append(translate('label_some_content_types', mapping=None, default=__msgid_4685677760, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('\n          ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4685685056
                        __attrs_4685685056 = _static_4428767312

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4685692592
                        __default_4685692592 = _DEFAULT_MARKER

                        # <Value 'view/widgets/allowed_content_types/render' (31:44)> -> __cache_4685692640
                        __token = 1733
                        try:
                            __zt_tmp = __attrs_4685685056
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4685692640 = _static_4427992992('path', 'view/widgets/allowed_content_types/render', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value 'view/widgets/allowed_content_types/render' (31:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 11749fbb0> -> __condition
                        __expression = __cache_4685692640

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4685692640
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n        </label>\n      ')
                    _slots = econtext['__slot_widget'] = _deque((__fill_widget, ))

                    # <Value 'context/@@ploneform-render-widget/widget-wrapper' (12:41)> -> __macro
                    __token = 679
                    try:
                        __zt_tmp = __attrs_4681893440
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __macro = _static_4427992992('path', 'context/@@ploneform-render-widget/widget-wrapper', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __token = 679
                    __m = __macro.include
                    __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    if (__backup_macroname_4687066176 is __marker):
                        del econtext['macroname']
                    else:
                        econtext['macroname'] = __backup_macroname_4687066176
                    __append('\n    ')
                    if (__backup_value_4680534576 is __marker):
                        del econtext['value']
                    else:
                        econtext['value'] = __backup_value_4680534576
                    if (__backup_context_4680440064 is __marker):
                        del econtext['context']
                    else:
                        econtext['context'] = __backup_context_4680440064
                    __append('\n  </fieldset>')
                __append('\n\n')
            _slots = econtext['__slot_fields'] = _deque((__fill_fields, ))

            # <Value 'context/@@ploneform-macros/titlelessform' (1:27)> -> __macro
            __token = 27
            try:
                __zt_tmp = __attrs_4682705088
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4427992992('path', 'context/@@ploneform-macros/titlelessform', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __token = 27
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4686219712 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4686219712
            __i18n_domain = __previous_i18n_domain_4682700576
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }