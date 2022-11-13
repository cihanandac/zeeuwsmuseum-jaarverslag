# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/contenttypes/browser/templates/listing_tabular.pt'

__tokens = {512: ('python:view.text', 13, 100), 545: ('python:text', 13, 133), 580: ('python:view.text_class', 13, 168), 664: ('python:text', 14, 59), 777: ('python:view.batch()', 18, 29), 827: ('python:batch', 19, 28), 871: ('context/batch_macros/macros/navigation', 21, 28), 871: ('context/batch_macros/macros/navigation', 21, 28), 1023: ('view/tabular_fields', 25, 70), 1061: (' python:view.get_thumb_scale_table(', 25, 108), 1107: ("s python:'thumb-%s float-end' % thumb_scale_tab", 25, 154), 1166: ('s  python:view.show_icon', 25, 213), 1410: ('tabular_fields', 30, 56), 1439: ('python:view.tabular_field_label(field)', 30, 85), 1571: ('python:thumb_scale_table', 31, 76), 1682: ('python:portal_state.portal()', 35, 36), 1723: (' portal/@@image_scal', 35, 77), 1789: ('python:batch', 36, 42), 1850: ('python:item.getURL()', 37, 46), 1917: (' python:item.getId(', 38, 45), 1986: ('e python:item.Title', 39, 47), 2055: ('le python:item_title or item', 40, 46), 2132: ('ype python:item.PortalTy', 41, 44), 2211: ("lass python:'contenttype/' + view.normalizeString(item_type) if showicons el", 42, 49), 2340: ('state python:item.review_s', 43, 46), 2425: ("_class python:'state-' + view.normalizeString(item_wf", 44, 51), 2530: ('creator python:item.C', 45, 43), 2605: ('as_image python:ite', 46, 44), 2673: ("item_link python:item_type in view.use_view_action and item_url+'/view' o", 47, 38), 2800: ('_mime_type python:ite', 48, 42), 2880: ("e_type_icon python: 'mimetype-' + it", 49, 46), 4960: ('context/batch_macros/macros/navigation', 94, 28), 4960: ('context/batch_macros/macros/navigation', 94, 28), 5104: ('python: not batch', 99, 22), 5136: ('python: view.no_items_message', 99, 54), 3092: ("python: item_type == 'File'", 55, 45), 3144: ('python:icons.tag(item_mime_type_icon)', 55, 97), 3231: ("python: item_type != 'File'", 56, 45), 3283: ('python:icons.tag(item_type_class)', 56, 97), 3393: ('python:tabular_fields', 59, 47), 3551: ('python:view.tabular_fielddata(item, field)', 61, 133), 3475: ("python:field not in ['Title', 'Creator', 'getIcon']", 61, 57), 3640: ("python: field_data.get('value')", 62, 44), 3758: ("python:field == 'Title'", 65, 57), 3828: ('python:item_link', 66, 44), 3851: (' string:$item_type_class $item_wf_state_class ur', 66, 67), 3906: ('e python:item_ty', 66, 122), 3939: ('python: item_title', 66, 155), 4146: ('python:view.pas_member.info(item_creator)', 71, 103), 4193: (" python:author['fullname'] or author['username'", 71, 150), 4100: ("python:field == 'Creator'", 71, 57), 4282: ('python: author', 72, 38), 4304: ('${view/navigation_root_url}/author/${item_creator}', 72, 60), 4306: ('view/navigation_root_url', 72, 62), 4341: ('item_creator', 72, 97), 4379: ('${name}', 73, 22), 4381: ('name', 73, 24), 4530: ('python:item_has_image and thumb_scale_table', 80, 38), 4666: ("python:image_scale.tag(item, 'image', scale=thumb_scale_table, css_class=img_class)", 81, 90), 4624: ('python: item_link', 81, 48), 251: ('context/@@main_template/macros/master', 6, 21), 251: ('context/@@main_template/macros/master', 6, 21)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_4901038704 = 'master'
_static_4900792272 = {'href': 'python: item_link', }
_static_4880492448 = {'href': '${view/navigation_root_url}/author/${item_creator}', }
_static_4856158752 = {'class': 'text-nowrap', }
_static_4901615984 = {'href': 'python:item_link', 'class': 'string:$item_type_class $item_wf_state_class url', 'title': 'python:item_type', }
_static_4880312656 = {'class': 'text-nowrap', }
_static_4903009440 = {'class': 'text-nowrap', }
_static_4903370512 = 'navigation'
_static_4903360720 = {'class': 'text-nowrap', }
_static_4903360096 = {'class': 'text-nowrap', }
_static_4903366624 = {'class': 'text-nowrap', }
_static_4903068016 = {'class': 'table table-striped', 'summary': 'Content listing', }
_static_4903061728 = {'class': 'table-responsive', }
_static_4900347360 = 'navigation'
_static_4439051040 = __C2ZContextWrapper
_static_4439058528 = __compile_zt_expr
_static_4900727792 = {'id': 'parent-fieldname-text', 'class': 'stx', }
_static_4438893776 = {}

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

    def render_content_core(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900716656
            __attrs_4900716656 = _static_4438893776
            __append('\n\n  ')
            __token = None
            render_text_field_view(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n  ')
            __token = None
            render_listing(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_text_field_view(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_inside = econtext['__slot_inside'].pop()
        except:
            __slot_inside = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x1241b2bf0> name=None at 1241b0d00> -> __attrs_4900354896
            __attrs_4900354896 = _static_4900727792
            __backup_text_4582930176 = get('text', __marker)

            # <Value 'python:view.text' (13:100)> -> __value
            __token = 512
            try:
                __zt_tmp = __attrs_4900354896
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('python', 'view.text', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['text'] = __value

            # <Value 'python:text' (13:133)> -> __condition
            __token = 545
            try:
                __zt_tmp = __attrs_4900354896
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4439058528('python', 'text', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="parent-fieldname-text"')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900342992
                __default_4900342992 = _DEFAULT_MARKER

                # <Substitution 'python:view.text_class' (13:168)> -> __attr_class
                __token = 580
                try:
                    __zt_tmp = __attrs_4900354896
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_4439058528('python', 'view.text_class', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', 'stx', _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append('>\n    ')
                if (__slot_inside is None):

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900344768
                    __attrs_4900344768 = _static_4438893776

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900347024
                    __default_4900347024 = _DEFAULT_MARKER

                    # <Value 'python:text' (14:59)> -> __cache_4900345632
                    __token = 664
                    try:
                        __zt_tmp = __attrs_4900344768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4900345632 = _static_4439058528('python', 'text', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value 'python:text' (14:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1241575b0> -> __condition
                    __expression = __cache_4900345632

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div>The body</div>')
                    else:
                        __content = __cache_4900345632
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                else:
                    __slot_inside(__stream, econtext.copy(), rcontext)
                __append('\n  </div>')
            if (__backup_text_4582930176 is __marker):
                del econtext['text']
            else:
                econtext['text'] = __backup_text_4582930176
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_listing(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_no_items_in_listing = econtext['__slot_no_items_in_listing'].pop()
        except:
            __slot_no_items_in_listing = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900340208
            __attrs_4900340208 = _static_4438893776
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900347072
            __attrs_4900347072 = _static_4438893776
            __backup_batch_4582917600 = get('batch', __marker)

            # <Value 'python:view.batch()' (18:29)> -> __value
            __token = 777
            try:
                __zt_tmp = __attrs_4900347072
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('python', 'view.batch()', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['batch'] = __value
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900350384
            __attrs_4900350384 = _static_4438893776

            # <Value 'python:batch' (19:28)> -> __condition
            __token = 827
            try:
                __zt_tmp = __attrs_4900350384
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4439058528('python', 'batch', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            if __condition:
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903066768
                __attrs_4903066768 = _static_4438893776
                __backup_macroname_4682470912 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x124155de0> name=None at 124155360> -> __value
                __value = _static_4900347360
                econtext['macroname'] = __value

                # <Value 'context/batch_macros/macros/navigation' (21:28)> -> __macro
                __token = 871
                try:
                    __zt_tmp = __attrs_4903066768
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_4439058528('path', 'context/batch_macros/macros/navigation', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __token = 871
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_4682470912 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_4682470912
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x1243ec8e0> name=None at 1243ed240> -> __attrs_4903063600
                __attrs_4903063600 = _static_4903061728

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="table-responsive">\n\n        ')

                # <Static value=<ast.Dict object at 0x1243ee170> name=None at 1243efd90> -> __attrs_4882408800
                __attrs_4882408800 = _static_4903068016
                __backup_tabular_fields_4692271760 = get('tabular_fields', __marker)

                # <Value 'view/tabular_fields' (25:70)> -> __value
                __token = 1023
                try:
                    __zt_tmp = __attrs_4882408800
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'view/tabular_fields', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['tabular_fields'] = __value
                __backup_thumb_scale_table_4853269888 = get('thumb_scale_table', __marker)

                # <Value 'python:view.get_thumb_scale_table()' (25:108)> -> __value
                __token = 1061
                try:
                    __zt_tmp = __attrs_4882408800
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', 'view.get_thumb_scale_table()', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['thumb_scale_table'] = __value
                __backup_img_class_4853279584 = get('img_class', __marker)

                # <Value "python:'thumb-%s float-end' % thumb_scale_table" (25:154)> -> __value
                __token = 1107
                try:
                    __zt_tmp = __attrs_4882408800
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', "'thumb-%s float-end' % thumb_scale_table", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['img_class'] = __value
                __backup_showicons_4853279776 = get('showicons', __marker)

                # <Value 'python:view.show_icons()' (25:213)> -> __value
                __token = 1166
                try:
                    __zt_tmp = __attrs_4882408800
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', 'view.show_icons()', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['showicons'] = __value

                # <table ... (0:0)
                # --------------------------------------------------------
                __append('<table class="table table-striped"')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4903059616
                __default_4903059616 = _DEFAULT_MARKER

                # <Translate msgid='summary_content_listing' node=<ast.Constant object at 0x1243ef250> at 1243ee230> -> __attr_summary
                __attr_summary = 'Content listing'
                __attr_summary = translate('summary_content_listing', default=__attr_summary, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_summary is not None):
                    __append((' summary="%s"' % __attr_summary))
                __append('>\n\n          ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903357840
                __attrs_4903357840 = _static_4438893776

                # <thead ... (0:0)
                # --------------------------------------------------------
                __append('<thead>\n            ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903358512
                __attrs_4903358512 = _static_4438893776

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n              ')

                # <Static value=<ast.Dict object at 0x124436fe0> name=None at 1244347f0> -> __attrs_4903364320
                __attrs_4903364320 = _static_4903366624

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th class="text-nowrap"></th>\n              ')

                # <Static value=<ast.Dict object at 0x124435660> name=None at 124436d70> -> __attrs_4903354480
                __attrs_4903354480 = _static_4903360096
                __backup_field_4617681552 = get('field', __marker)

                # <Value 'tabular_fields' (30:56)> -> __iterator
                __token = 1410
                try:
                    __zt_tmp = __attrs_4903354480
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4439058528('path', 'tabular_fields', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                (__iterator, ____index_4903361392, ) = getname('repeat')('field', __iterator)
                econtext['field'] = None
                for __item in __iterator:
                    econtext['field'] = __item

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th class="text-nowrap">')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4903365232
                    __default_4903365232 = _DEFAULT_MARKER

                    # <Value 'python:view.tabular_field_label(field)' (30:85)> -> __cache_4903359280
                    __token = 1439
                    try:
                        __zt_tmp = __attrs_4903354480
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4903359280 = _static_4439058528('python', 'view.tabular_field_label(field)', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value 'python:view.tabular_field_label(field)' (30:85)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1244353f0> -> __condition
                    __expression = __cache_4903359280

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Field name')
                    else:
                        __content = __cache_4903359280
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</th>')
                    ____index_4903361392 -= 1
                    if (____index_4903361392 > 0):
                        __append('\n              ')
                if (__backup_field_4617681552 is __marker):
                    del econtext['field']
                else:
                    econtext['field'] = __backup_field_4617681552
                __append('\n              ')

                # <Static value=<ast.Dict object at 0x1244358d0> name=None at 1244367d0> -> __attrs_4903358560
                __attrs_4903358560 = _static_4903360720

                # <Value 'python:thumb_scale_table' (31:76)> -> __condition
                __token = 1571
                try:
                    __zt_tmp = __attrs_4903358560
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('python', 'thumb_scale_table', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th class="text-nowrap">')
                    __stream_4903356832 = []
                    __append_4903356832 = __stream_4903356832.append
                    __append_4903356832('Image')
                    __msgid_4903356832 = __re_whitespace(''.join(__stream_4903356832)).strip()
                    if 'image':
                        __append(translate('image', mapping=None, default=__msgid_4903356832, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</th>')
                __append('\n            </tr>\n          </thead>\n\n          ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903370128
                __attrs_4903370128 = _static_4438893776
                __backup_portal_4852580896 = get('portal', __marker)

                # <Value 'python:portal_state.portal()' (35:36)> -> __value
                __token = 1682
                try:
                    __zt_tmp = __attrs_4903370128
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', 'portal_state.portal()', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['portal'] = __value
                __backup_image_scale_4851672224 = get('image_scale', __marker)

                # <Value 'portal/@@image_scale' (35:77)> -> __value
                __token = 1723
                try:
                    __zt_tmp = __attrs_4903370128
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'portal/@@image_scale', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['image_scale'] = __value

                # <tbody ... (0:0)
                # --------------------------------------------------------
                __append('<tbody>\n            ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903368064
                __attrs_4903368064 = _static_4438893776
                __backup_item_4848243024 = get('item', __marker)

                # <Value 'python:batch' (36:42)> -> __iterator
                __token = 1789
                try:
                    __zt_tmp = __attrs_4903368064
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4439058528('python', 'batch', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                (__iterator, ____index_4903367584, ) = getname('repeat')('item', __iterator)
                econtext['item'] = None
                for __item in __iterator:
                    econtext['item'] = __item
                    __append('\n              ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903366048
                    __attrs_4903366048 = _static_4438893776
                    __backup_item_url_4848248304 = get('item_url', __marker)

                    # <Value 'python:item.getURL()' (37:46)> -> __value
                    __token = 1850
                    try:
                        __zt_tmp = __attrs_4903366048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('python', 'item.getURL()', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['item_url'] = __value
                    __backup_item_id_4848239712 = get('item_id', __marker)

                    # <Value 'python:item.getId()' (38:45)> -> __value
                    __token = 1917
                    try:
                        __zt_tmp = __attrs_4903366048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('python', 'item.getId()', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['item_id'] = __value
                    __backup_item_title_4607241872 = get('item_title', __marker)

                    # <Value 'python:item.Title()' (39:47)> -> __value
                    __token = 1986
                    try:
                        __zt_tmp = __attrs_4903366048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('python', 'item.Title()', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['item_title'] = __value
                    __backup_item_title_4604468896 = get('item_title', __marker)

                    # <Value 'python:item_title or item_id' (40:46)> -> __value
                    __token = 2055
                    try:
                        __zt_tmp = __attrs_4903366048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('python', 'item_title or item_id', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['item_title'] = __value
                    __backup_item_type_4874875184 = get('item_type', __marker)

                    # <Value 'python:item.PortalType()' (41:44)> -> __value
                    __token = 2132
                    try:
                        __zt_tmp = __attrs_4903366048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('python', 'item.PortalType()', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['item_type'] = __value
                    __backup_item_type_class_4551203408 = get('item_type_class', __marker)

                    # <Value "python:'contenttype/' + view.normalizeString(item_type) if showicons else ''" (42:49)> -> __value
                    __token = 2211
                    try:
                        __zt_tmp = __attrs_4903366048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('python', "'contenttype/' + view.normalizeString(item_type) if showicons else ''", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['item_type_class'] = __value
                    __backup_item_wf_state_4840407440 = get('item_wf_state', __marker)

                    # <Value 'python:item.review_state()' (43:46)> -> __value
                    __token = 2340
                    try:
                        __zt_tmp = __attrs_4903366048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('python', 'item.review_state()', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['item_wf_state'] = __value
                    __backup_item_wf_state_class_4840411184 = get('item_wf_state_class', __marker)

                    # <Value "python:'state-' + view.normalizeString(item_wf_state)" (44:51)> -> __value
                    __token = 2425
                    try:
                        __zt_tmp = __attrs_4903366048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('python', "'state-' + view.normalizeString(item_wf_state)", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['item_wf_state_class'] = __value
                    __backup_item_creator_4879774192 = get('item_creator', __marker)

                    # <Value 'python:item.Creator()' (45:43)> -> __value
                    __token = 2530
                    try:
                        __zt_tmp = __attrs_4903366048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('python', 'item.Creator()', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['item_creator'] = __value
                    __backup_item_has_image_4840410560 = get('item_has_image', __marker)

                    # <Value 'python:item.getIcon' (46:44)> -> __value
                    __token = 2605
                    try:
                        __zt_tmp = __attrs_4903366048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('python', 'item.getIcon', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['item_has_image'] = __value
                    __backup_item_link_4637476992 = get('item_link', __marker)

                    # <Value "python:item_type in view.use_view_action and item_url+'/view' or item_url" (47:38)> -> __value
                    __token = 2673
                    try:
                        __zt_tmp = __attrs_4903366048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('python', "item_type in view.use_view_action and item_url+'/view' or item_url", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['item_link'] = __value
                    __backup_item_mime_type_4637488416 = get('item_mime_type', __marker)

                    # <Value 'python:item.mime_type' (48:42)> -> __value
                    __token = 2800
                    try:
                        __zt_tmp = __attrs_4903366048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('python', 'item.mime_type', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['item_mime_type'] = __value
                    __backup_item_mime_type_icon_4881131952 = get('item_mime_type_icon', __marker)

                    # <Value "python: 'mimetype-' + item_mime_type" (49:46)> -> __value
                    __token = 2880
                    try:
                        __zt_tmp = __attrs_4903366048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('python', " 'mimetype-' + item_mime_type", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['item_mime_type_icon'] = __value
                    __append('\n\n                ')
                    __token = None
                    render_listitem(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    __append('\n\n              ')
                    if (__backup_item_mime_type_icon_4881131952 is __marker):
                        del econtext['item_mime_type_icon']
                    else:
                        econtext['item_mime_type_icon'] = __backup_item_mime_type_icon_4881131952
                    if (__backup_item_mime_type_4637488416 is __marker):
                        del econtext['item_mime_type']
                    else:
                        econtext['item_mime_type'] = __backup_item_mime_type_4637488416
                    if (__backup_item_link_4637476992 is __marker):
                        del econtext['item_link']
                    else:
                        econtext['item_link'] = __backup_item_link_4637476992
                    if (__backup_item_has_image_4840410560 is __marker):
                        del econtext['item_has_image']
                    else:
                        econtext['item_has_image'] = __backup_item_has_image_4840410560
                    if (__backup_item_creator_4879774192 is __marker):
                        del econtext['item_creator']
                    else:
                        econtext['item_creator'] = __backup_item_creator_4879774192
                    if (__backup_item_wf_state_class_4840411184 is __marker):
                        del econtext['item_wf_state_class']
                    else:
                        econtext['item_wf_state_class'] = __backup_item_wf_state_class_4840411184
                    if (__backup_item_wf_state_4840407440 is __marker):
                        del econtext['item_wf_state']
                    else:
                        econtext['item_wf_state'] = __backup_item_wf_state_4840407440
                    if (__backup_item_type_class_4551203408 is __marker):
                        del econtext['item_type_class']
                    else:
                        econtext['item_type_class'] = __backup_item_type_class_4551203408
                    if (__backup_item_type_4874875184 is __marker):
                        del econtext['item_type']
                    else:
                        econtext['item_type'] = __backup_item_type_4874875184
                    if (__backup_item_title_4604468896 is __marker):
                        del econtext['item_title']
                    else:
                        econtext['item_title'] = __backup_item_title_4604468896
                    if (__backup_item_title_4607241872 is __marker):
                        del econtext['item_title']
                    else:
                        econtext['item_title'] = __backup_item_title_4607241872
                    if (__backup_item_id_4848239712 is __marker):
                        del econtext['item_id']
                    else:
                        econtext['item_id'] = __backup_item_id_4848239712
                    if (__backup_item_url_4848248304 is __marker):
                        del econtext['item_url']
                    else:
                        econtext['item_url'] = __backup_item_url_4848248304
                    __append('\n            ')
                    ____index_4903367584 -= 1
                    if (____index_4903367584 > 0):
                        __append('')
                if (__backup_item_4848243024 is __marker):
                    del econtext['item']
                else:
                    econtext['item'] = __backup_item_4848243024
                __append('\n          </tbody>')
                if (__backup_image_scale_4851672224 is __marker):
                    del econtext['image_scale']
                else:
                    econtext['image_scale'] = __backup_image_scale_4851672224
                if (__backup_portal_4852580896 is __marker):
                    del econtext['portal']
                else:
                    econtext['portal'] = __backup_portal_4852580896
                __append('\n        </table>')
                if (__backup_showicons_4853279776 is __marker):
                    del econtext['showicons']
                else:
                    econtext['showicons'] = __backup_showicons_4853279776
                if (__backup_img_class_4853279584 is __marker):
                    del econtext['img_class']
                else:
                    econtext['img_class'] = __backup_img_class_4853279584
                if (__backup_thumb_scale_table_4853269888 is __marker):
                    del econtext['thumb_scale_table']
                else:
                    econtext['thumb_scale_table'] = __backup_thumb_scale_table_4853269888
                if (__backup_tabular_fields_4692271760 is __marker):
                    del econtext['tabular_fields']
                else:
                    econtext['tabular_fields'] = __backup_tabular_fields_4692271760
                __append('\n\n      </div>\n\n      ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903359616
                __attrs_4903359616 = _static_4438893776
                __backup_macroname_4692365760 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x124437f10> name=None at 124435cf0> -> __value
                __value = _static_4903370512
                econtext['macroname'] = __value

                # <Value 'context/batch_macros/macros/navigation' (94:28)> -> __macro
                __token = 4960
                try:
                    __zt_tmp = __attrs_4903359616
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_4439058528('path', 'context/batch_macros/macros/navigation', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __token = 4960
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_4692365760 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_4692365760
                __append('\n\n    ')
            __append('\n\n    ')
            if (__slot_no_items_in_listing is None):

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903363744
                __attrs_4903363744 = _static_4438893776
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900791648
                __attrs_4900791648 = _static_4438893776

                # <Value 'python: not batch' (99:22)> -> __condition
                __token = 5104
                try:
                    __zt_tmp = __attrs_4900791648
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('python', ' not batch', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p>')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900794624
                    __default_4900794624 = _DEFAULT_MARKER

                    # <Value 'python: view.no_items_message' (99:54)> -> __cache_4900790832
                    __token = 5136
                    try:
                        __zt_tmp = __attrs_4900791648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4900790832 = _static_4439058528('python', ' view.no_items_message', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value 'python: view.no_items_message' (99:54)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1241c05b0> -> __condition
                    __expression = __cache_4900790832

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n      There are currently no items in this folder.\n    ')
                    else:
                        __content = __cache_4900790832
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</p>')
                __append('\n    ')
            else:
                __slot_no_items_in_listing(__stream, econtext.copy(), rcontext)
            __append('\n\n  ')
            if (__backup_batch_4582917600 is __marker):
                del econtext['batch']
            else:
                econtext['batch'] = __backup_batch_4582917600
            __append('\n  ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_listitem(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903002192
            __attrs_4903002192 = _static_4438893776

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append('<tr>\n\n                  ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903005888
            __attrs_4903005888 = _static_4438893776

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>\n                    ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4902999504
            __attrs_4902999504 = _static_4438893776

            # <Value "python: item_type == 'File'" (55:45)> -> __condition
            __token = 3092
            try:
                __zt_tmp = __attrs_4902999504
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4439058528('python', " item_type == 'File'", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            if __condition:

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4902996912
                __default_4902996912 = _DEFAULT_MARKER

                # <Value 'python:icons.tag(item_mime_type_icon)' (55:97)> -> __cache_4903000704
                __token = 3144
                try:
                    __zt_tmp = __attrs_4902999504
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4903000704 = _static_4439058528('python', 'icons.tag(item_mime_type_icon)', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:icons.tag(item_mime_type_icon)' (55:97)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1243dc7c0> -> __condition
                __expression = __cache_4903000704

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4903000704
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
            __append('\n                    ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903007664
            __attrs_4903007664 = _static_4438893776

            # <Value "python: item_type != 'File'" (56:45)> -> __condition
            __token = 3231
            try:
                __zt_tmp = __attrs_4903007664
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4439058528('python', " item_type != 'File'", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            if __condition:

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4902997920
                __default_4902997920 = _DEFAULT_MARKER

                # <Value 'python:icons.tag(item_type_class)' (56:97)> -> __cache_4903001856
                __token = 3283
                try:
                    __zt_tmp = __attrs_4903007664
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4903001856 = _static_4439058528('python', 'icons.tag(item_type_class)', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:icons.tag(item_type_class)' (56:97)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1243dcc70> -> __condition
                __expression = __cache_4903001856

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4903001856
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
            __append('\n                  </td>\n\n                  ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903001328
            __attrs_4903001328 = _static_4438893776
            __backup_field_4882368064 = get('field', __marker)

            # <Value 'python:tabular_fields' (59:47)> -> __iterator
            __token = 3393
            try:
                __zt_tmp = __attrs_4903001328
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4439058528('python', 'tabular_fields', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            (__iterator, ____index_4902999696, ) = getname('repeat')('field', __iterator)
            econtext['field'] = None
            for __item in __iterator:
                econtext['field'] = __item
                __append('\n\n                  ')

                # <Static value=<ast.Dict object at 0x1243dfca0> name=None at 1243df730> -> __attrs_4903006272
                __attrs_4903006272 = _static_4903009440
                __backup_field_data_4882662208 = get('field_data', __marker)

                # <Value 'python:view.tabular_fielddata(item, field)' (61:133)> -> __value
                __token = 3551
                try:
                    __zt_tmp = __attrs_4903006272
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', 'view.tabular_fielddata(item, field)', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['field_data'] = __value

                # <Value "python:field not in ['Title', 'Creator', 'getIcon']" (61:57)> -> __condition
                __token = 3475
                try:
                    __zt_tmp = __attrs_4903006272
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('python', "field not in ['Title', 'Creator', 'getIcon']", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td class="text-nowrap">\n                    ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4880313856
                    __attrs_4880313856 = _static_4438893776

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4880312224
                    __default_4880312224 = _DEFAULT_MARKER

                    # <Value "python: field_data.get('value')" (62:44)> -> __cache_4903001616
                    __token = 3640
                    try:
                        __zt_tmp = __attrs_4880313856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4903001616 = _static_4439058528('python', " field_data.get('value')", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value "python: field_data.get('value')" (62:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1243de320> -> __condition
                    __expression = __cache_4903001616

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4903001616
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n                  </td>')
                if (__backup_field_data_4882662208 is __marker):
                    del econtext['field_data']
                else:
                    econtext['field_data'] = __backup_field_data_4882662208
                __append('\n\n                  ')

                # <Static value=<ast.Dict object at 0x122e3a950> name=None at 122e38d60> -> __attrs_4697392512
                __attrs_4697392512 = _static_4880312656

                # <Value "python:field == 'Title'" (65:57)> -> __condition
                __token = 3758
                try:
                    __zt_tmp = __attrs_4697392512
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('python', "field == 'Title'", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td class="text-nowrap">\n                    ')

                    # <Static value=<ast.Dict object at 0x12428b970> name=None at 124288820> -> __attrs_4504779600
                    __attrs_4504779600 = _static_4901615984

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901611856
                    __default_4901611856 = _DEFAULT_MARKER

                    # <Substitution 'python:item_link' (66:44)> -> __attr_href
                    __token = 3828
                    try:
                        __zt_tmp = __attrs_4504779600
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4439058528('python', 'item_link', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901609264
                    __default_4901609264 = _DEFAULT_MARKER

                    # <Substitution 'string:$item_type_class $item_wf_state_class url' (66:67)> -> __attr_class
                    __token = 3851
                    try:
                        __zt_tmp = __attrs_4504779600
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4439058528('string', '$item_type_class $item_wf_state_class url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901607248
                    __default_4901607248 = _DEFAULT_MARKER

                    # <Substitution 'python:item_type' (66:122)> -> __attr_title
                    __token = 3906
                    try:
                        __zt_tmp = __attrs_4504779600
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_4439058528('python', 'item_type', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901607392
                    __default_4901607392 = _DEFAULT_MARKER

                    # <Value 'python: item_title' (66:155)> -> __cache_4901609744
                    __token = 3939
                    try:
                        __zt_tmp = __attrs_4504779600
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4901609744 = _static_4439058528('python', ' item_title', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value 'python: item_title' (66:155)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 12428b310> -> __condition
                    __expression = __cache_4901609744

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                      Item Title\n                    ')
                    else:
                        __content = __cache_4901609744
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</a>\n                  </td>')
                __append('\n\n                  ')

                # <Static value=<ast.Dict object at 0x121731a20> name=None at 121730730> -> __attrs_4854911696
                __attrs_4854911696 = _static_4856158752
                __backup_author_4850907744 = get('author', __marker)

                # <Value 'python:view.pas_member.info(item_creator)' (71:103)> -> __value
                __token = 4146
                try:
                    __zt_tmp = __attrs_4854911696
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', 'view.pas_member.info(item_creator)', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['author'] = __value
                __backup_name_4850905104 = get('name', __marker)

                # <Value "python:author['fullname'] or author['username']" (71:150)> -> __value
                __token = 4193
                try:
                    __zt_tmp = __attrs_4854911696
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', "author['fullname'] or author['username']", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['name'] = __value

                # <Value "python:field == 'Creator'" (71:57)> -> __condition
                __token = 4100
                try:
                    __zt_tmp = __attrs_4854911696
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('python', "field == 'Creator'", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td class="text-nowrap">\n                    ')

                    # <Static value=<ast.Dict object at 0x122e667a0> name=None at 122e658a0> -> __attrs_4880485824
                    __attrs_4880485824 = _static_4880492448

                    # <Value 'python: author' (72:38)> -> __condition
                    __token = 4282
                    try:
                        __zt_tmp = __attrs_4880485824
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4439058528('python', ' author', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4880492496
                        __default_4880492496 = _DEFAULT_MARKER

                        # <Interpolation value=<Substitution '${view/navigation_root_url}/author/${item_creator}' (72:60)> braces_required=True translation=False default='"?"' default_marker='"?"' at 122e66d40> -> __attr_href
                        __token = 4304
                        __token = 4306
                        try:
                            __zt_tmp = __attrs_4880485824
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4439058528('path', 'view/navigation_root_url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        __token = 4341
                        try:
                            __zt_tmp = __attrs_4880485824
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href_4339 = _static_4439058528('path', 'item_creator', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        __attr_href_4339 = __quote(__attr_href_4339, '"', '&quot;', None, _DEFAULT_MARKER)
                        __attr_href = ('%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/author/', (__attr_href_4339 if (__attr_href_4339 is not None) else ''), ))
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

                        # <Interpolation value=<Substitution '\n                      ${name}\n                    ' (72:112)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1241c1ea0> -> __content_4340547312
                        __token = 4379
                        __token = 4381
                        try:
                            __zt_tmp = __attrs_4880485824
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_4340547312 = _static_4439058528('path', 'name', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        __content_4340547312 = __quote(__content_4340547312, '\x00', '&#0;', None, None)
                        __content_4340547312 = ('%s%s%s' % ('\n                      ', (__content_4340547312 if (__content_4340547312 is not None) else ''), '\n                    ', ))
                        if (__content_4340547312 is None):
                            pass
                        else:
                            if (__content_4340547312 is None):
                                __content_4340547312 = None
                            else:
                                __tt = type(__content_4340547312)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __content_4340547312 = str(__content_4340547312)
                                else:
                                    if (__tt is bytes):
                                        __content_4340547312 = decode(__content_4340547312)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __content_4340547312 = __content_4340547312.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__content_4340547312)
                                                __content_4340547312 = (str(__content_4340547312) if (__content_4340547312 is __converted) else __converted)
                                            else:
                                                __content_4340547312 = __content_4340547312()
                        if (__content_4340547312 is not None):
                            __append(__content_4340547312)
                        __append('</a>')
                    __append('\n                  </td>')
                if (__backup_name_4850905104 is __marker):
                    del econtext['name']
                else:
                    econtext['name'] = __backup_name_4850905104
                if (__backup_author_4850907744 is __marker):
                    del econtext['author']
                else:
                    econtext['author'] = __backup_author_4850907744
                __append('\n\n                  ')
                ____index_4902999696 -= 1
                if (____index_4902999696 > 0):
                    __append('')
            if (__backup_field_4882368064 is __marker):
                del econtext['field']
            else:
                econtext['field'] = __backup_field_4882368064
            __append('\n\n                  ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900785504
            __attrs_4900785504 = _static_4438893776

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>\n                    ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900796160
            __attrs_4900796160 = _static_4438893776

            # <Value 'python:item_has_image and thumb_scale_table' (80:38)> -> __condition
            __token = 4530
            try:
                __zt_tmp = __attrs_4900796160
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4439058528('python', 'item_has_image and thumb_scale_table', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            if __condition:

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a>\n                      ')

                # <Static value=<ast.Dict object at 0x1241c27d0> name=None at 1241c3e80> -> __attrs_4900784640
                __attrs_4900784640 = _static_4900792272

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900789632
                __default_4900789632 = _DEFAULT_MARKER

                # <Value "python:image_scale.tag(item, 'image', scale=thumb_scale_table, css_class=img_class)" (81:90)> -> __cache_4900786176
                __token = 4666
                try:
                    __zt_tmp = __attrs_4900784640
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4900786176 = _static_4439058528('python', "image_scale.tag(item, 'image', scale=thumb_scale_table, css_class=img_class)", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value "python:image_scale.tag(item, 'image', scale=thumb_scale_table, css_class=img_class)" (81:90)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1241c3c10> -> __condition
                __expression = __cache_4900786176

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <img ... (0:0)
                    # --------------------------------------------------------
                    __append('<img')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900785600
                    __default_4900785600 = _DEFAULT_MARKER

                    # <Substitution 'python: item_link' (81:48)> -> __attr_href
                    __token = 4624
                    try:
                        __zt_tmp = __attrs_4900784640
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4439058528('python', ' item_link', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' />')
                else:
                    __content = __cache_4900786176
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n                    </a>')
            __append('\n                  </td>\n\n                </tr>')
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900370896
            __attrs_4900370896 = _static_4438893776
            __previous_i18n_domain_4900361056 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4479561344 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x1241fea70> name=None at 12415b970> -> __value
            __value = _static_4901038704
            econtext['macroname'] = __value

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4881134880
                __attrs_4881134880 = _static_4438893776
                __append('\n')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/@@main_template/macros/master' (6:21)> -> __macro
            __token = 251
            try:
                __zt_tmp = __attrs_4900370896
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4439058528('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __token = 251
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4479561344 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4479561344
            __i18n_domain = __previous_i18n_domain_4900361056
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render_text_field_view': render_text_field_view, 'render_listing': render_listing, 'render_listitem': render_listitem, 'render': render, }