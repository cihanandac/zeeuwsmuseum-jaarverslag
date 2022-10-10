# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/dexterity/browser/types_listing.pt'

__tokens = {103: ('view/status', 5, 22), 140: ('view/status', 6, 23), 260: ('view/description', 12, 21), 307: ('view/description', 13, 29), 402: ('${context/absolute_url}/@@add-type', 17, 14), 404: ('context/absolute_url', 17, 16), 588: ('${context/absolute_url}/@@import-types', 22, 14), 590: ('context/absolute_url', 22, 16), 793: ('view/subforms', 28, 23), 837: ('form/render', 29, 29), 902: ('view/actions/values', 32, 41), 972: ('action/render', 33, 48)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4684990208 = {'type': 'submit', }
_static_4684943696 = {'class': 'action', }
_static_4684951040 = {'class': 'crud-form', }
_static_4684953968 = {'class': 'btn btn-primary', }
_static_4684952960 = {'class': 'pat-plone-modal', 'href': '${context/absolute_url}/@@import-types', }
_static_4684952048 = {'class': 'btn btn-primary', }
_static_4684945472 = {'class': 'pat-plone-modal', 'href': '${context/absolute_url}/@@add-type', }
_static_4684947776 = {'class': 'mb-4', }
_static_4684948832 = {'class': 'crud-description documentDescription', }
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
_static_4676671504 = {'class': 'alert alert-info', 'role': 'alert', }
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

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4664610864
            __attrs_4664610864 = _static_4428767312
            __previous_i18n_domain_4664617008 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x116c05810> name=None at 116c071c0> -> __attrs_4684940000
            __attrs_4684940000 = _static_4676671504

            # <Value 'view/status' (5:22)> -> __condition
            __token = 103
            try:
                __zt_tmp = __attrs_4684940000
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'view/status', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="alert alert-info" role="alert">\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4684943024
                __attrs_4684943024 = _static_4428767312

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684945232
                __default_4684945232 = _DEFAULT_MARKER

                # <Value 'view/status' (6:23)> -> __cache_4684944416
                __token = 140
                try:
                    __zt_tmp = __attrs_4684943024
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4684944416 = _static_4427992992('path', 'view/status', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/status' (6:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1173e9450> -> __condition
                __expression = __cache_4684944416

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n      Status\n    ')
                else:
                    __content = __cache_4684944416
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</span>\n  </div>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x1173ea560> name=None at 1173ea410> -> __attrs_4684948112
            __attrs_4684948112 = _static_4684948832

            # <Value 'view/description' (12:21)> -> __condition
            __token = 260
            try:
                __zt_tmp = __attrs_4684948112
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'view/description', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="crud-description documentDescription">')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684942640
                __default_4684942640 = _DEFAULT_MARKER

                # <Value 'view/description' (13:29)> -> __cache_4684939424
                __token = 307
                try:
                    __zt_tmp = __attrs_4684948112
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4684939424 = _static_4427992992('path', 'view/description', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/description' (13:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1173ea4a0> -> __condition
                __expression = __cache_4684939424

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n  ')
                else:
                    __content = __cache_4684939424
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('</p>')
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x1173ea140> name=None at 1173ea0e0> -> __attrs_4684946864
            __attrs_4684946864 = _static_4684947776

            # <header ... (0:0)
            # --------------------------------------------------------
            __append('<header class="mb-4">\n    ')

            # <Static value=<ast.Dict object at 0x1173e9840> name=None at 1173e97b0> -> __attrs_4684943456
            __attrs_4684943456 = _static_4684945472

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="pat-plone-modal"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684947344
            __default_4684947344 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${context/absolute_url}/@@add-type' (17:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1173e8be0> -> __attr_href
            __token = 402
            __token = 404
            try:
                __zt_tmp = __attrs_4684943456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4427992992('path', 'context/absolute_url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = ('%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/@@add-type', ))
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
            __append('>\n      ')

            # <Static value=<ast.Dict object at 0x1173eb1f0> name=None at 1173eae60> -> __attrs_4684946144
            __attrs_4684946144 = _static_4684952048

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button class="btn btn-primary">')
            __stream_4684951520 = []
            __append_4684951520 = __stream_4684951520.append
            __append_4684951520('Add New Content Type&hellip;')
            __msgid_4684951520 = __re_whitespace(''.join(__stream_4684951520)).strip()
            if __msgid_4684951520:
                __append(translate(__msgid_4684951520, mapping=None, default=__msgid_4684951520, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</button>\n    </a>\n\n    ')

            # <Static value=<ast.Dict object at 0x1173eb580> name=None at 1173eb550> -> __attrs_4684952528
            __attrs_4684952528 = _static_4684952960

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="pat-plone-modal"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684949936
            __default_4684949936 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${context/absolute_url}/@@import-types' (22:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1173e81c0> -> __attr_href
            __token = 588
            __token = 590
            try:
                __zt_tmp = __attrs_4684952528
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4427992992('path', 'context/absolute_url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = ('%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/@@import-types', ))
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
            __append('>\n      ')

            # <Static value=<ast.Dict object at 0x1173eb970> name=None at 1173eb940> -> __attrs_4684954112
            __attrs_4684954112 = _static_4684953968

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button class="btn btn-primary">')
            __stream_4684953344 = []
            __append_4684953344 = __stream_4684953344.append
            __append_4684953344('Import Type Profiles&hellip;')
            __msgid_4684953344 = __re_whitespace(''.join(__stream_4684953344)).strip()
            if __msgid_4684953344:
                __append(translate(__msgid_4684953344, mapping=None, default=__msgid_4684953344, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</button>\n    </a>\n  </header>\n\n  ')

            # <Static value=<ast.Dict object at 0x1173eae00> name=None at 1173eb6d0> -> __attrs_4684952480
            __attrs_4684952480 = _static_4684951040
            __backup_form_4682781440 = get('form', __marker)

            # <Value 'view/subforms' (28:23)> -> __iterator
            __token = 793
            try:
                __zt_tmp = __attrs_4684952480
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4427992992('path', 'view/subforms', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            (__iterator, ____index_4684943840, ) = getname('repeat')('form', __iterator)
            econtext['form'] = None
            for __item in __iterator:
                econtext['form'] = __item

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="crud-form">')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684954400
                __default_4684954400 = _DEFAULT_MARKER

                # <Value 'form/render' (29:29)> -> __cache_4684954496
                __token = 837
                try:
                    __zt_tmp = __attrs_4684952480
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4684954496 = _static_4427992992('path', 'form/render', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'form/render' (29:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1173ebe20> -> __condition
                __expression = __cache_4684954496

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n  ')
                else:
                    __content = __cache_4684954496
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('</div>')
                ____index_4684943840 -= 1
                if (____index_4684943840 > 0):
                    __append('\n  ')
            if (__backup_form_4682781440 is __marker):
                del econtext['form']
            else:
                econtext['form'] = __backup_form_4682781440
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x1173e9150> name=None at 1173ea650> -> __attrs_4684993280
            __attrs_4684993280 = _static_4684943696
            __backup_action_4680815696 = get('action', __marker)

            # <Value 'view/actions/values' (32:41)> -> __iterator
            __token = 902
            try:
                __zt_tmp = __attrs_4684993280
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4427992992('path', 'view/actions/values', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            (__iterator, ____index_4684988768, ) = getname('repeat')('action', __iterator)
            econtext['action'] = None
            for __item in __iterator:
                econtext['action'] = __item

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="action">\n    ')

                # <Static value=<ast.Dict object at 0x1173f4700> name=None at 1173f4730> -> __attrs_4684992704
                __attrs_4684992704 = _static_4684990208

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4684992560
                __default_4684992560 = _DEFAULT_MARKER

                # <Value 'action/render' (33:48)> -> __cache_4684990640
                __token = 972
                try:
                    __zt_tmp = __attrs_4684992704
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4684990640 = _static_4427992992('path', 'action/render', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'action/render' (33:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1173f4b20> -> __condition
                __expression = __cache_4684990640

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="submit" />')
                else:
                    __content = __cache_4684990640
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n  </div>')
                ____index_4684988768 -= 1
                if (____index_4684988768 > 0):
                    __append('\n  ')
            if (__backup_action_4680815696 is __marker):
                del econtext['action']
            else:
                econtext['action'] = __backup_action_4680815696
            __append('\n')
            __i18n_domain = __previous_i18n_domain_4664617008
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }