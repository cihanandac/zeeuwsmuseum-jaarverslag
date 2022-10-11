# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/Products/CMFPlone/controlpanel/browser/actions.pt'

__tokens = {1011: ('view/actions', 29, 51), 1071: ('category/title', 30, 27), 1219: ('category/actions', 33, 33), 1378: ('repeat/action/number', 35, 37), 1423: ('action/title', 35, 82), 1540: ('plone-action-${action/id} flex-shrink-0', 37, 25), 1555: ('action/id', 37, 40), 1703: ('action/id', 40, 38), 1806: ('category/id', 42, 38), 1859: ('not:action/visible', 43, 37), 2069: ("python:icons.tag('square', tag_alt='Toggle to show')", 46, 49), 2238: ('action/visible', 48, 37), 2445: ("python:icons.tag('check-square', tag_alt='Toggle to hide')", 51, 49), 2695: ('string:${action/url}/@@action-form', 54, 37), 2781: ("python:icons.tag('plone-edit', tag_alt='Edit')", 55, 50), 3248: ("python:icons.tag('plone-delete', tag_alt='Delete')", 61, 49), 261: ('context/prefs_main_template/macros/master', 6, 23), 261: ('context/prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4906630880 = {'class': 'ms-2', }
_static_4906630544 = {'type': 'submit', 'class': 'btn btn-sm btn-danger destructive', 'name': 'delete', 'value': 'Delete', 'confirm-message': 'Delete the action?', 'onclick': "return confirm(this.getAttribute('confirm-message'));", }
_static_4906623344 = {'class': 'ms-2', }
_static_4906620368 = {'class': 'pat-plone-modal btn btn-sm btn-primary standalone', 'href': 'string:${action/url}/@@action-form', }
_static_4906620512 = {'class': 'ms-2', }
_static_4900375472 = {'type': 'submit', 'class': 'btn  btn-sm btn-link standalone me-5', 'name': 'hide', 'value': 'Hide', }
_static_4900630736 = {'class': 'ms-2', }
_static_4906626896 = {'type': 'submit', 'class': 'btn btn-sm btn-link standalone me-5', 'name': 'show', 'value': 'Show', }
_static_4900204512 = {'type': 'hidden', 'name': 'category', 'value': 'category/id', }
_static_4900090016 = {'type': 'hidden', 'name': 'actionid', 'value': 'action/id', }
_static_4900124560 = {'action': '@@actions-controlpanel', 'class': 'plone-action-${action/id} flex-shrink-0', 'method': 'POST', }
_static_4900341648 = {'class': 'list-group-item bg-transparent d-flex align-items-center justify-content-between', }
_static_4900723856 = {'class': 'configlets list-group list-group-flush', }
_static_4900732304 = {'class': 'card-header', }
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
_static_4905775936 = {'class': 'card mb-4', }
_static_4905773920 = {'href': '@@new-action', 'class': 'context pat-plone-modal btn btn-success', }
_static_4905777664 = {'class': 'addAction', }
_static_4905777040 = {'id': 'content-core', }
_static_4905767296 = {'class': 'text-muted', }
_static_4905778624 = {'class': 'documentFirstHeading', }
_static_4900633808 = 'master'
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

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900625984
            __attrs_4900625984 = _static_4428767312
            __backup_macroname_4905000192 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x12419bcd0> name=None at 12419a7a0> -> __value
            __value = _static_4900633808
            econtext['macroname'] = __value

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4905772624
                __attrs_4905772624 = _static_4428767312
                __previous_i18n_domain_4905778240 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4905775600
                __attrs_4905775600 = _static_4428767312

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n\n    ')

                # <Static value=<ast.Dict object at 0x124683dc0> name=None at 124682800> -> __attrs_4905766960
                __attrs_4905766960 = _static_4905778624

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">')
                __stream_4905762928 = []
                __append_4905762928 = __stream_4905762928.append
                __append_4905762928('Portal actions')
                __msgid_4905762928 = __re_whitespace(''.join(__stream_4905762928)).strip()
                if 'portal_actions_controlpanel_header':
                    __append(translate('portal_actions_controlpanel_header', mapping=None, default=__msgid_4905762928, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n\n    ')

                # <Static value=<ast.Dict object at 0x124681180> name=None at 124681e10> -> __attrs_4905764320
                __attrs_4905764320 = _static_4905767296

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="text-muted">')
                __stream_4905775360 = []
                __append_4905775360 = __stream_4905775360.append
                __append_4905775360('\n        This is the portal actions configuration section, you can manage the\n        actions contained in the different action categories.\n    ')
                __msgid_4905775360 = __re_whitespace(''.join(__stream_4905775360)).strip()
                if 'portal_actions_controlpanel_description':
                    __append(translate('portal_actions_controlpanel_description', mapping=None, default=__msgid_4905775360, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</div>\n  </header>\n  ')

                # <Static value=<ast.Dict object at 0x124683790> name=None at 1246814b0> -> __attrs_4905777808
                __attrs_4905777808 = _static_4905777040

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n    ')

                # <Static value=<ast.Dict object at 0x124683a00> name=None at 124682770> -> __attrs_4905778768
                __attrs_4905778768 = _static_4905777664

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="addAction">\n      ')

                # <Static value=<ast.Dict object at 0x124682b60> name=None at 124683700> -> __attrs_4905772576
                __attrs_4905772576 = _static_4905773920

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a href="@@new-action" class="context pat-plone-modal btn btn-success">')
                __stream_4905777424 = []
                __append_4905777424 = __stream_4905777424.append
                __append_4905777424('Add new action')
                __msgid_4905777424 = __re_whitespace(''.join(__stream_4905777424)).strip()
                if __msgid_4905777424:
                    __append(translate(__msgid_4905777424, mapping=None, default=__msgid_4905777424, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</a>\n    </p>\n    ')

                # <Static value=<ast.Dict object at 0x124683340> name=None at 1246831c0> -> __attrs_4900730000
                __attrs_4900730000 = _static_4905775936
                __backup_category_4906623728 = get('category', __marker)

                # <Value 'view/actions' (29:51)> -> __iterator
                __token = 1011
                try:
                    __zt_tmp = __attrs_4900730000
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4427992992('path', 'view/actions', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                (__iterator, ____index_4900721072, ) = getname('repeat')('category', __iterator)
                econtext['category'] = None
                for __item in __iterator:
                    econtext['category'] = __item

                    # <section ... (0:0)
                    # --------------------------------------------------------
                    __append('<section class="category" class="card mb-4">\n      ')

                    # <Static value=<ast.Dict object at 0x1241b3d90> name=None at 1241b1b40> -> __attrs_4900728704
                    __attrs_4900728704 = _static_4900732304

                    # <header ... (0:0)
                    # --------------------------------------------------------
                    __append('<header class="card-header">')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900732688
                    __default_4900732688 = _DEFAULT_MARKER

                    # <Value 'category/title' (30:27)> -> __cache_4900722656
                    __token = 1071
                    try:
                        __zt_tmp = __attrs_4900728704
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4900722656 = _static_4427992992('path', 'category/title', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'category/title' (30:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1241b1c00> -> __condition
                    __expression = __cache_4900722656

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4900722656
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</header>\n      ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900723472
                    __attrs_4900723472 = _static_4428767312

                    # <section ... (0:0)
                    # --------------------------------------------------------
                    __append('<section>\n        ')

                    # <Static value=<ast.Dict object at 0x1241b1c90> name=None at 1241b0d60> -> __attrs_4899344528
                    __attrs_4899344528 = _static_4900723856

                    # <ol ... (0:0)
                    # --------------------------------------------------------
                    __append('<ol class="configlets list-group list-group-flush">\n          ')

                    # <Static value=<ast.Dict object at 0x124154790> name=None at 124155420> -> __attrs_4900340784
                    __attrs_4900340784 = _static_4900341648
                    __backup_action_4900196112 = get('action', __marker)

                    # <Value 'category/actions' (33:33)> -> __iterator
                    __token = 1219
                    try:
                        __zt_tmp = __attrs_4900340784
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_4427992992('path', 'category/actions', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    (__iterator, ____index_4900353792, ) = getname('repeat')('action', __iterator)
                    econtext['action'] = None
                    for __item in __iterator:
                        econtext['action'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="list-group-item bg-transparent d-flex align-items-center justify-content-between">\n            ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900352016
                        __attrs_4900352016 = _static_4428767312

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900350912
                        __attrs_4900350912 = _static_4428767312

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900340448
                        __default_4900340448 = _DEFAULT_MARKER

                        # <Value 'repeat/action/number' (35:37)> -> __cache_4900353408
                        __token = 1378
                        try:
                            __zt_tmp = __attrs_4900350912
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4900353408 = _static_4427992992('path', 'repeat/action/number', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value 'repeat/action/number' (35:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 124155060> -> __condition
                        __expression = __cache_4900353408

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span />')
                        else:
                            __content = __cache_4900353408
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('. ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900113376
                        __attrs_4900113376 = _static_4428767312

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4897895520
                        __default_4897895520 = _DEFAULT_MARKER

                        # <Value 'action/title' (35:82)> -> __cache_4897896144
                        __token = 1423
                        try:
                            __zt_tmp = __attrs_4900113376
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4897896144 = _static_4427992992('path', 'action/title', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value 'action/title' (35:82)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 123efc760> -> __condition
                        __expression = __cache_4897896144

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span />')
                        else:
                            __content = __cache_4897896144
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>\n            ')

                        # <Static value=<ast.Dict object at 0x12411f790> name=None at 12411c0d0> -> __attrs_4900087760
                        __attrs_4900087760 = _static_4900124560

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append('<form action="@@actions-controlpanel"')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900124608
                        __default_4900124608 = _DEFAULT_MARKER

                        # <Interpolation value=<Substitution 'plone-action-${action/id} flex-shrink-0' (37:25)> braces_required=True translation=False default='"?"' default_marker='"?"' at 12411ea40> -> __attr_class
                        __token = 1540
                        __token = 1555
                        try:
                            __zt_tmp = __attrs_4900087760
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_4427992992('path', 'action/id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        __attr_class = ('%s%s%s' % ('plone-action-', (__attr_class if (__attr_class is not None) else ''), ' flex-shrink-0', ))
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
                        __append(' method="POST">\n              ')

                        # <Static value=<ast.Dict object at 0x1241170a0> name=None at 124115b70> -> __attrs_4900200576
                        __attrs_4900200576 = _static_4900090016

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="hidden" name="actionid"')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900192656
                        __default_4900192656 = _DEFAULT_MARKER

                        # <Substitution 'action/id' (40:38)> -> __attr_value
                        __token = 1703
                        try:
                            __zt_tmp = __attrs_4900200576
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_4427992992('path', 'action/id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' />\n              ')

                        # <Static value=<ast.Dict object at 0x124132fe0> name=None at 124130ac0> -> __attrs_4900192896
                        __attrs_4900192896 = _static_4900204512

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="hidden" name="category"')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900201440
                        __default_4900201440 = _DEFAULT_MARKER

                        # <Substitution 'category/id' (42:38)> -> __attr_value
                        __token = 1806
                        try:
                            __zt_tmp = __attrs_4900192896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_4427992992('path', 'category/id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' />\n              ')

                        # <Static value=<ast.Dict object at 0x124752f50> name=None at 124751840> -> __attrs_4906624016
                        __attrs_4906624016 = _static_4906626896

                        # <Value 'not:action/visible' (43:37)> -> __condition
                        __token = 1859
                        try:
                            __zt_tmp = __attrs_4906624016
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4427992992('not', 'action/visible', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        if __condition:

                            # <button ... (0:0)
                            # --------------------------------------------------------
                            __append('<button type="submit" class="btn btn-sm btn-link standalone me-5" name="show"')

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906615040
                            __default_4906615040 = _DEFAULT_MARKER

                            # <Translate msgid=None node=<ast.Constant object at 0x124752020> at 124750070> -> __attr_value
                            __attr_value = 'Show'
                            __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))
                            __append(' >\n                ')

                            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4905771664
                            __attrs_4905771664 = _static_4428767312

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4905763456
                            __default_4905763456 = _DEFAULT_MARKER

                            # <Value "python:icons.tag('square', tag_alt='Toggle to show')" (46:49)> -> __cache_4905766624
                            __token = 2069
                            try:
                                __zt_tmp = __attrs_4905771664
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4905766624 = _static_4427992992('python', "icons.tag('square', tag_alt='Toggle to show')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                            # <BinOp left=<Value "python:icons.tag('square', tag_alt='Toggle to show')" (46:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 124682fe0> -> __condition
                            __expression = __cache_4905766624

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_4905766624
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)

                            # <Static value=<ast.Dict object at 0x12419b0d0> name=None at 12419afe0> -> __attrs_4900633040
                            __attrs_4900633040 = _static_4900630736

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span class="ms-2">')
                            __stream_4900618976 = []
                            __append_4900618976 = __stream_4900618976.append
                            __append_4900618976('visible')
                            __msgid_4900618976 = __re_whitespace(''.join(__stream_4900618976)).strip()
                            if __msgid_4900618976:
                                __append(translate(__msgid_4900618976, mapping=None, default=__msgid_4900618976, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</span>\n              </button>')
                        __append('\n              ')

                        # <Static value=<ast.Dict object at 0x12415cbb0> name=None at 12415dd80> -> __attrs_4906627088
                        __attrs_4906627088 = _static_4900375472

                        # <Value 'action/visible' (48:37)> -> __condition
                        __token = 2238
                        try:
                            __zt_tmp = __attrs_4906627088
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4427992992('path', 'action/visible', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        if __condition:

                            # <button ... (0:0)
                            # --------------------------------------------------------
                            __append('<button type="submit" class="btn  btn-sm btn-link standalone me-5" name="hide"')

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906628432
                            __default_4906628432 = _DEFAULT_MARKER

                            # <Translate msgid=None node=<ast.Constant object at 0x124750220> at 1247501f0> -> __attr_value
                            __attr_value = 'Hide'
                            __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))
                            __append(' >\n                ')

                            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4906627280
                            __attrs_4906627280 = _static_4428767312

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906616336
                            __default_4906616336 = _DEFAULT_MARKER

                            # <Value "python:icons.tag('check-square', tag_alt='Toggle to hide')" (51:49)> -> __cache_4906616000
                            __token = 2445
                            try:
                                __zt_tmp = __attrs_4906627280
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4906616000 = _static_4427992992('python', "icons.tag('check-square', tag_alt='Toggle to hide')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                            # <BinOp left=<Value "python:icons.tag('check-square', tag_alt='Toggle to hide')" (51:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 124750520> -> __condition
                            __expression = __cache_4906616000

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_4906616000
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)

                            # <Static value=<ast.Dict object at 0x124751660> name=None at 124751690> -> __attrs_4906619072
                            __attrs_4906619072 = _static_4906620512

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span class="ms-2">')
                            __stream_4906618016 = []
                            __append_4906618016 = __stream_4906618016.append
                            __append_4906618016('visible')
                            __msgid_4906618016 = __re_whitespace(''.join(__stream_4906618016)).strip()
                            if __msgid_4906618016:
                                __append(translate(__msgid_4906618016, mapping=None, default=__msgid_4906618016, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</span>\n              </button>')
                        __append('\n              ')

                        # <Static value=<ast.Dict object at 0x1247515d0> name=None at 124751c60> -> __attrs_4906628960
                        __attrs_4906628960 = _static_4906620368

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="pat-plone-modal btn btn-sm btn-primary standalone"')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906628048
                        __default_4906628048 = _DEFAULT_MARKER

                        # <Substitution 'string:${action/url}/@@action-form' (54:37)> -> __attr_href
                        __token = 2695
                        try:
                            __zt_tmp = __attrs_4906628960
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4427992992('string', '${action/url}/@@action-form', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4906623392
                        __attrs_4906623392 = _static_4428767312

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906625024
                        __default_4906625024 = _DEFAULT_MARKER

                        # <Value "python:icons.tag('plone-edit', tag_alt='Edit')" (55:50)> -> __cache_4906627808
                        __token = 2781
                        try:
                            __zt_tmp = __attrs_4906623392
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4906627808 = _static_4427992992('python', "icons.tag('plone-edit', tag_alt='Edit')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:icons.tag('plone-edit', tag_alt='Edit')" (55:50)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1247531f0> -> __condition
                        __expression = __cache_4906627808

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4906627808
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)

                        # <Static value=<ast.Dict object at 0x124752170> name=None at 124751750> -> __attrs_4906615856
                        __attrs_4906615856 = _static_4906623344

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="ms-2">')
                        __stream_4906617392 = []
                        __append_4906617392 = __stream_4906617392.append
                        __append_4906617392('Edit')
                        __msgid_4906617392 = __re_whitespace(''.join(__stream_4906617392)).strip()
                        if __msgid_4906617392:
                            __append(translate(__msgid_4906617392, mapping=None, default=__msgid_4906617392, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span></a>\n              ')

                        # <Static value=<ast.Dict object at 0x124753d90> name=None at 124751210> -> __attrs_4906624832
                        __attrs_4906624832 = _static_4906630544

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" class="btn btn-sm btn-danger destructive" name="delete"')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906629680
                        __default_4906629680 = _DEFAULT_MARKER

                        # <Translate msgid=None node=<ast.Constant object at 0x124752a10> at 124753a60> -> __attr_value
                        __attr_value = 'Delete'
                        __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906630256
                        __default_4906630256 = _DEFAULT_MARKER

                        # <Translate msgid=None node=<ast.Constant object at 0x1247525c0> at 1247524d0> -> __attr_confirm_message
                        __attr_confirm_message = 'Delete the action?'
                        __attr_confirm_message = translate(__attr_confirm_message, default=__attr_confirm_message, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_confirm_message is not None):
                            __append((' confirm-message="%s"' % __attr_confirm_message))
                        __append(' onclick="return confirm(this.getAttribute(\'confirm-message\'));" >\n                ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4906630448
                        __attrs_4906630448 = _static_4428767312

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906630928
                        __default_4906630928 = _DEFAULT_MARKER

                        # <Value "python:icons.tag('plone-delete', tag_alt='Delete')" (61:49)> -> __cache_4906628720
                        __token = 3248
                        try:
                            __zt_tmp = __attrs_4906630448
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4906628720 = _static_4427992992('python', "icons.tag('plone-delete', tag_alt='Delete')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:icons.tag('plone-delete', tag_alt='Delete')" (61:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 124753880> -> __condition
                        __expression = __cache_4906628720

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4906628720
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)

                        # <Static value=<ast.Dict object at 0x124753ee0> name=None at 124753df0> -> __attrs_4905400496
                        __attrs_4905400496 = _static_4906630880

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="ms-2">')
                        __stream_4906618112 = []
                        __append_4906618112 = __stream_4906618112.append
                        __append_4906618112('Delete')
                        __msgid_4906618112 = __re_whitespace(''.join(__stream_4906618112)).strip()
                        if __msgid_4906618112:
                            __append(translate(__msgid_4906618112, mapping=None, default=__msgid_4906618112, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n              </button>\n            </form>\n          </li>')
                        ____index_4900353792 -= 1
                        if (____index_4900353792 > 0):
                            __append('\n          ')
                    if (__backup_action_4900196112 is __marker):
                        del econtext['action']
                    else:
                        econtext['action'] = __backup_action_4900196112
                    __append('\n        </ol>\n      </section>\n    </section>')
                    ____index_4900721072 -= 1
                    if (____index_4900721072 > 0):
                        __append('\n    ')
                if (__backup_category_4906623728 is __marker):
                    del econtext['category']
                else:
                    econtext['category'] = __backup_category_4906623728
                __append('\n  </div>\n')
                __i18n_domain = __previous_i18n_domain_4905778240
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'context/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_4900625984
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4427992992('path', 'context/prefs_main_template/macros/master', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4905000192 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4905000192
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }