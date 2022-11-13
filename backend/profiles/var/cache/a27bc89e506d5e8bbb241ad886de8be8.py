# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/contenttypes/browser/templates/full_view_item.pt'

__tokens = {349: ('nocall:view/item_macros/content-core|nothing', 11, 30), 422: (' view/item_ur', 12, 27), 471: ('r python:', 13, 33), 519: ('provider:plone.abovecontenttitle', 15, 32), 644: ('item_url', 18, 78), 608: ('context/Title', 18, 42), 724: ('provider:plone.belowcontenttitle', 23, 32), 831: ('context/Description', 25, 69), 795: ('context/Description', 25, 33), 940: ('item_macro', 29, 59), 988: ('provider:plone.abovecontentbody', 31, 34), 1053: ('nocall:view/default_view', 33, 28), 1112: (' context/@@plon', 34, 33), 1157: ("s python:context.restrictedTraverse('@@iconresolver", 35, 27), 1245: ('te context/@@plone_portal_st', 36, 33), 1311: ('ate context/@@plone_context_s', 37, 33), 1377: ('yout context/@@plone_l', 38, 31), 1428: (' lang portal_state/la', 39, 22), 1479: (' dummy python: plone_layout.mark_vie', 40, 22), 1550: ('tal_url portal_state/po', 41, 26), 1613: ('rmission nocall: context/portal_membership/checkP', 42, 30), 1702: ('roperties context/portal_properties/site_', 43, 29), 1788: ('item_macro', 45, 30), 1788: ('item_macro', 45, 30), 1883: ('provider:plone.belowcontentbody', 51, 34), 1966: ('rendering_error', 55, 30), 2079: ('python:not(item_macro) or rendering_error', 59, 35), 2153: ('item_url', 60, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4886454736 = {'href': 'item_url', }
_static_4887410912 = {'class': 'more', }
_static_4887396464 = 'item_macro'
_static_4887410048 = {'id': 'section-item', 'class': 'mb-5', }
_static_4887399872 = {'class': 'lead', }
_static_4887409232 = {'class': 'summary url', 'href': 'item_url', }
_static_4439051040 = __C2ZContextWrapper
_static_4439058528 = __compile_zt_expr
_static_4901179008 = {'class': 'item', }
_static_4438893776 = {}
_static_4902159120 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'xml:lang': 'en', 'lang': 'en', }

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

            # <Static value=<ast.Dict object at 0x124310310> name=None at 1243110c0> -> __attrs_4840408592
            __attrs_4840408592 = _static_4902159120
            __previous_i18n_domain_4840414736 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901185536
            __attrs_4901185536 = _static_4438893776
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x124220e80> name=None at 1242213f0> -> __attrs_4901175600
            __attrs_4901175600 = _static_4901179008
            __backup_item_macro_4518775872 = get('item_macro', __marker)

            # <Value 'nocall:view/item_macros/content-core|nothing' (11:30)> -> __value
            __token = 349
            try:
                __zt_tmp = __attrs_4901175600
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('nocall', 'view/item_macros/content-core|nothing', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['item_macro'] = __value
            __backup_item_url_4879959232 = get('item_url', __marker)

            # <Value 'view/item_url' (12:27)> -> __value
            __token = 422
            try:
                __zt_tmp = __attrs_4901175600
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'view/item_url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['item_url'] = __value
            __backup_rendering_error_4605127040 = get('rendering_error', __marker)

            # <Value 'python:[]' (13:33)> -> __value
            __token = 471
            try:
                __zt_tmp = __attrs_4901175600
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('python', '[]', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['rendering_error'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="item">\n\n    ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901180688
            __attrs_4901180688 = _static_4438893776

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901185152
            __default_4901185152 = _DEFAULT_MARKER

            # <Value 'provider:plone.abovecontenttitle' (15:32)> -> __cache_4901188464
            __token = 519
            try:
                __zt_tmp = __attrs_4901180688
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4901188464 = _static_4439058528('provider', 'plone.abovecontenttitle', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.abovecontenttitle' (15:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1242229b0> -> __condition
            __expression = __cache_4901188464

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_4901188464
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901179200
            __attrs_4901179200 = _static_4438893776

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1>\n      ')

            # <Static value=<ast.Dict object at 0x1234ff250> name=None at 1234fdc90> -> __attrs_4887403328
            __attrs_4887403328 = _static_4887409232

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="summary url"')

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4887409952
            __default_4887409952 = _DEFAULT_MARKER

            # <Substitution 'item_url' (18:78)> -> __attr_href
            __token = 644
            try:
                __zt_tmp = __attrs_4887403328
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4439058528('path', 'item_url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append('>')

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4887409712
            __default_4887409712 = _DEFAULT_MARKER

            # <Value 'context/Title' (18:42)> -> __cache_4901187552
            __token = 608
            try:
                __zt_tmp = __attrs_4887403328
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4901187552 = _static_4439058528('path', 'context/Title', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/Title' (18:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 124222ec0> -> __condition
            __expression = __cache_4901187552

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('\n        Title\n      ')
            else:
                __content = __cache_4901187552
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</a>\n    </h1>\n\n    ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4887412640
            __attrs_4887412640 = _static_4438893776

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4887406784
            __default_4887406784 = _DEFAULT_MARKER

            # <Value 'provider:plone.belowcontenttitle' (23:32)> -> __cache_4887410624
            __token = 724
            try:
                __zt_tmp = __attrs_4887412640
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4887410624 = _static_4439058528('provider', 'plone.belowcontenttitle', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.belowcontenttitle' (23:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1234ffe80> -> __condition
            __expression = __cache_4887410624

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_4887410624
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x1234fcdc0> name=None at 1234fef20> -> __attrs_4887400592
            __attrs_4887400592 = _static_4887399872

            # <Value 'context/Description' (25:69)> -> __condition
            __token = 831
            try:
                __zt_tmp = __attrs_4887400592
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4439058528('path', 'context/Description', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            if __condition:

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="lead">')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4887401840
                __default_4887401840 = _DEFAULT_MARKER

                # <Value 'context/Description' (25:33)> -> __cache_4887411488
                __token = 795
                try:
                    __zt_tmp = __attrs_4887400592
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4887411488 = _static_4439058528('path', 'context/Description', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'context/Description' (25:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1234feda0> -> __condition
                __expression = __cache_4887411488

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n      Description\n    ')
                else:
                    __content = __cache_4887411488
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</p>')
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x1234ff580> name=None at 1234fc3d0> -> __attrs_4887398912
            __attrs_4887398912 = _static_4887410048

            # <Value 'item_macro' (29:59)> -> __condition
            __token = 940
            try:
                __zt_tmp = __attrs_4887398912
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4439058528('path', 'item_macro', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            if __condition:

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-item" class="mb-5">\n\n      ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4887400880
                __attrs_4887400880 = _static_4438893776

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4887397088
                __default_4887397088 = _DEFAULT_MARKER

                # <Value 'provider:plone.abovecontentbody' (31:34)> -> __cache_4887401360
                __token = 988
                try:
                    __zt_tmp = __attrs_4887400880
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4887401360 = _static_4439058528('provider', 'plone.abovecontentbody', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'provider:plone.abovecontentbody' (31:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1234fc160> -> __condition
                __expression = __cache_4887401360

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div />')
                else:
                    __content = __cache_4887401360
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4887399440
                __attrs_4887399440 = _static_4438893776
                __backup_view_4854208480 = get('view', __marker)

                # <Value 'nocall:view/default_view' (33:28)> -> __value
                __token = 1053
                try:
                    __zt_tmp = __attrs_4887399440
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('nocall', 'view/default_view', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['view'] = __value
                __backup_plone_view_4882665664 = get('plone_view', __marker)

                # <Value 'context/@@plone' (34:33)> -> __value
                __token = 1112
                try:
                    __zt_tmp = __attrs_4887399440
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'context/@@plone', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['plone_view'] = __value
                __backup_icons_4856670640 = get('icons', __marker)

                # <Value "python:context.restrictedTraverse('@@iconresolver')" (35:27)> -> __value
                __token = 1157
                try:
                    __zt_tmp = __attrs_4887399440
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['icons'] = __value
                __backup_portal_state_4882570912 = get('portal_state', __marker)

                # <Value 'context/@@plone_portal_state' (36:33)> -> __value
                __token = 1245
                try:
                    __zt_tmp = __attrs_4887399440
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'context/@@plone_portal_state', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['portal_state'] = __value
                __backup_context_state_4854909392 = get('context_state', __marker)

                # <Value 'context/@@plone_context_state' (37:33)> -> __value
                __token = 1311
                try:
                    __zt_tmp = __attrs_4887399440
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'context/@@plone_context_state', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['context_state'] = __value
                __backup_plone_layout_4609047520 = get('plone_layout', __marker)

                # <Value 'context/@@plone_layout' (38:31)> -> __value
                __token = 1377
                try:
                    __zt_tmp = __attrs_4887399440
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'context/@@plone_layout', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['plone_layout'] = __value
                __backup_lang_4617671424 = get('lang', __marker)

                # <Value 'portal_state/language' (39:22)> -> __value
                __token = 1428
                try:
                    __zt_tmp = __attrs_4887399440
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'portal_state/language', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['lang'] = __value
                __backup_dummy_4840415840 = get('dummy', __marker)

                # <Value 'python: plone_layout.mark_view(view)' (40:22)> -> __value
                __token = 1479
                try:
                    __zt_tmp = __attrs_4887399440
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', ' plone_layout.mark_view(view)', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['dummy'] = __value
                __backup_portal_url_4840408496 = get('portal_url', __marker)

                # <Value 'portal_state/portal_url' (41:26)> -> __value
                __token = 1550
                try:
                    __zt_tmp = __attrs_4887399440
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'portal_state/portal_url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['portal_url'] = __value
                __backup_checkPermission_4848241248 = get('checkPermission', __marker)

                # <Value 'nocall: context/portal_membership/checkPermission' (42:30)> -> __value
                __token = 1613
                try:
                    __zt_tmp = __attrs_4887399440
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('nocall', ' context/portal_membership/checkPermission', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['checkPermission'] = __value
                __backup_site_properties_4848239184 = get('site_properties', __marker)

                # <Value 'context/portal_properties/site_properties' (43:29)> -> __value
                __token = 1702
                try:
                    __zt_tmp = __attrs_4887399440
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'context/portal_properties/site_properties', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['site_properties'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n\n        ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4887406304
                __attrs_4887406304 = _static_4438893776
                __backup_macroname_4879558144 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x1234fc070> name=None at 1234fedd0> -> __value
                __value = _static_4887396464
                econtext['macroname'] = __value

                # <Value 'item_macro' (45:30)> -> __macro
                __token = 1788
                try:
                    __zt_tmp = __attrs_4887406304
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_4439058528('path', 'item_macro', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __token = 1788
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_4879558144 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_4879558144
                __append('\n\n      </div>')
                if (__backup_site_properties_4848239184 is __marker):
                    del econtext['site_properties']
                else:
                    econtext['site_properties'] = __backup_site_properties_4848239184
                if (__backup_checkPermission_4848241248 is __marker):
                    del econtext['checkPermission']
                else:
                    econtext['checkPermission'] = __backup_checkPermission_4848241248
                if (__backup_portal_url_4840408496 is __marker):
                    del econtext['portal_url']
                else:
                    econtext['portal_url'] = __backup_portal_url_4840408496
                if (__backup_dummy_4840415840 is __marker):
                    del econtext['dummy']
                else:
                    econtext['dummy'] = __backup_dummy_4840415840
                if (__backup_lang_4617671424 is __marker):
                    del econtext['lang']
                else:
                    econtext['lang'] = __backup_lang_4617671424
                if (__backup_plone_layout_4609047520 is __marker):
                    del econtext['plone_layout']
                else:
                    econtext['plone_layout'] = __backup_plone_layout_4609047520
                if (__backup_context_state_4854909392 is __marker):
                    del econtext['context_state']
                else:
                    econtext['context_state'] = __backup_context_state_4854909392
                if (__backup_portal_state_4882570912 is __marker):
                    del econtext['portal_state']
                else:
                    econtext['portal_state'] = __backup_portal_state_4882570912
                if (__backup_icons_4856670640 is __marker):
                    del econtext['icons']
                else:
                    econtext['icons'] = __backup_icons_4856670640
                if (__backup_plone_view_4882665664 is __marker):
                    del econtext['plone_view']
                else:
                    econtext['plone_view'] = __backup_plone_view_4882665664
                if (__backup_view_4854208480 is __marker):
                    del econtext['view']
                else:
                    econtext['view'] = __backup_view_4854208480
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4887404624
                __attrs_4887404624 = _static_4438893776

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4887400448
                __default_4887400448 = _DEFAULT_MARKER

                # <Value 'provider:plone.belowcontentbody' (51:34)> -> __cache_4887412112
                __token = 1883
                try:
                    __zt_tmp = __attrs_4887404624
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4887412112 = _static_4439058528('provider', 'plone.belowcontentbody', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'provider:plone.belowcontentbody' (51:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1234febf0> -> __condition
                __expression = __cache_4887412112

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div />')
                else:
                    __content = __cache_4887412112
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n\n    </section>')
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4887398960
            __attrs_4887398960 = _static_4438893776

            # <Value 'rendering_error' (55:30)> -> __condition
            __token = 1966
            try:
                __zt_tmp = __attrs_4887398960
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4439058528('path', 'rendering_error', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            if __condition:
                __append('\n      <!-- Error rendering item macro -->\n    ')
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x1234ff8e0> name=None at 1234fd6c0> -> __attrs_4887398576
            __attrs_4887398576 = _static_4887410912

            # <Value 'python:not(item_macro) or rendering_error' (59:35)> -> __condition
            __token = 2079
            try:
                __zt_tmp = __attrs_4887398576
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4439058528('python', 'not(item_macro) or rendering_error', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            if __condition:

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="more">\n      ')

                # <Static value=<ast.Dict object at 0x1234161d0> name=None at 123416170> -> __attrs_4886452192
                __attrs_4886452192 = _static_4886454736

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4886453728
                __default_4886453728 = _DEFAULT_MARKER

                # <Substitution 'item_url' (60:30)> -> __attr_href
                __token = 2153
                try:
                    __zt_tmp = __attrs_4886452192
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4439058528('path', 'item_url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append('>')
                __stream_4886453776 = []
                __append_4886453776 = __stream_4886453776.append
                __append_4886453776('\n        Read More&hellip;\n      ')
                __msgid_4886453776 = __re_whitespace(''.join(__stream_4886453776)).strip()
                if 'read_more':
                    __append(translate('read_more', mapping=None, default=__msgid_4886453776, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</a>\n    </p>')
            __append('\n\n  </div>')
            if (__backup_rendering_error_4605127040 is __marker):
                del econtext['rendering_error']
            else:
                econtext['rendering_error'] = __backup_rendering_error_4605127040
            if (__backup_item_url_4879959232 is __marker):
                del econtext['item_url']
            else:
                econtext['item_url'] = __backup_item_url_4879959232
            if (__backup_item_macro_4518775872 is __marker):
                del econtext['item_macro']
            else:
                econtext['item_macro'] = __backup_item_macro_4518775872
            __append('\n\n')
            __i18n_domain = __previous_i18n_domain_4840414736
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }