# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/contenttypes/browser/templates/listing.pt'

__tokens = {524: ('python:view.text', 15, 23), 563: ('python:text', 16, 21), 604: ('python:view.text_class', 17, 28), 688: ('text', 18, 59), 797: ('python:view.batch()', 23, 31), 859: (' python:view.get_thumb_scale_list(', 24, 41), 937: ('e python:view.get_thumb_scale_table', 25, 41), 1018: ('ry python:view.get_thumb_scale_summar', 26, 42), 1091: ("ass python:'thumb-{} image-responsive'.format(thumb_scale_l", 27, 31), 1186: ('cons python:view.show_ic', 28, 30), 1248: ('python:batch', 29, 30), 1351: ('python:portal_state.portal()', 31, 31), 1416: (' portal/@@image_scal', 32, 35), 6459: ('context/batch_macros/macros/navigation', 129, 30), 6459: ('context/batch_macros/macros/navigation', 129, 30), 6640: ('python: not batch', 135, 27), 6684: ('python: view.no_items_message', 136, 25), 1476: ('python:batch', 34, 35), 1559: ('python:item.getObject()', 35, 39), 1608: (' python:item.getURL(', 36, 24), 1653: ('d python:item.getId', 37, 22), 1700: ('le python:item.Titl', 38, 24), 1747: ('tle python:item_title or ite', 39, 23), 1809: ('tion python:item.Descript', 40, 28), 1861: ('_type python:item.Portal', 41, 20), 1916: ('dified python:item.Modificatio', 42, 23), 1976: ('created python:item.Creati', 43, 21), 2033: ('wf_state python:item.revie', 44, 21), 2096: ("ate_class python:'state-' + view.normalizeString(item", 45, 26), 2179: ('em_creator python:ite', 46, 18), 2227: ("  item_link python:item_type in view.use_view_action and item_url+'/view'", 47, 14), 2331: ('tem_is_event python:view.', 48, 17), 2388: ('tem_has_image pytho', 49, 17), 2440: ("tem_type_class python:('contenttype-' + view.normalizeString(item_type)) if sh", 50, 17), 6011: ('python:item_has_image and thumb_scale_list', 117, 61), 6100: ('python:item_link', 118, 44), 6170: ("python:image_scale.tag(item, 'image', scale=thumb_scale_list, css_class=img_class)", 119, 50), 2804: ('python:item_link', 59, 48), 2827: (' string:$item_type_class $item_wf_state_class ur', 59, 71), 2882: ('e item_ty', 59, 126), 2908: ('python:item_title', 59, 152), 5797: ('python:item_description', 112, 53), 5835: ('python:item_description', 112, 91), 3185: ('python:item_is_event', 67, 46), 3267: ('python:view.formatted_date(obj)', 68, 59), 3349: ('python:obj.location', 69, 47), 3499: ('python:obj.location', 71, 47), 3723: ('python:view.show_about', 76, 47), 3869: ('python:view.pas_member.info(item_creator)', 78, 49), 3972: (" python:author.get('username'", 79, 60), 4062: ('m string:?author=$${python:author.usernam', 80, 58), 4164: ("id python:'/' in creator_short_f", 81, 57), 4250: ('_id python:(creator_short_form, creator_long_form)[creator_is_ope', 82, 49), 3799: ('python:item_creator', 77, 51), 4656: ('python: not author', 87, 46), 4472: ('string:${view/navigation_root_url}/author/${item_creator}', 85, 52), 4576: ("python: author.get('name_or_id')", 86, 45), 4928: ("python:item_type != 'Event'", 94, 51), 5137: ('python:view.toLocalizedTime(item_modified,long_format=1)', 97, 47), 5460: ('nothing', 103, 50), 251: ('context/@@main_template/macros/master', 6, 21), 251: ('context/@@main_template/macros/master', 6, 21)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_5115188688 = 'master'
_static_5114979728 = {'href': 'string:${view/navigation_root_url}/author/${item_creator}', }
_static_5114982800 = {'class': 'location', }
_static_5115063184 = {'class': 'mb-1', }
_static_5114978816 = {'class': 'me-3', }
_static_5115059248 = {'href': 'python:item_link', 'class': 'string:$item_type_class $item_wf_state_class url', 'title': 'item_type', }
_static_5115060304 = {'class': 'mb-1', }
_static_5115055024 = {'class': 'col', }
_static_5114974016 = {'href': 'python:item_link', }
_static_5114972288 = {'class': 'col-3 text-end', }
_static_5115061456 = {'class': 'mb-3 row', }
_static_4960785584 = {'class': 'discreet', }
_static_5108905344 = 'navigation'
_static_5115196224 = {'class': 'entries', }
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
_static_5115195312 = {'id': 'parent-fieldname-text', 'class': 'stx', }
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

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5115189696
            __attrs_5115189696 = _static_4428767312
            __append('\n\n  ')
            __token = None
            render_text_field_view(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n  ')
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

            # <Static value=<ast.Dict object at 0x130e3afb0> name=None at 130e3a350> -> __attrs_5115194640
            __attrs_5115194640 = _static_5115195312
            __backup_text_5110155248 = get('text', __marker)

            # <Value 'python:view.text' (15:23)> -> __value
            __token = 524
            try:
                __zt_tmp = __attrs_5115194640
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', 'view.text', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['text'] = __value

            # <Value 'python:text' (16:21)> -> __condition
            __token = 563
            try:
                __zt_tmp = __attrs_5115194640
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('python', 'text', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="parent-fieldname-text"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5115192384
                __default_5115192384 = _DEFAULT_MARKER

                # <Substitution 'python:view.text_class' (17:28)> -> __attr_class
                __token = 604
                try:
                    __zt_tmp = __attrs_5115194640
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_4427992992('python', 'view.text_class', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', 'stx', _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append('>\n    ')
                if (__slot_inside is None):

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5115192480
                    __attrs_5115192480 = _static_4428767312

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5115186192
                    __default_5115186192 = _DEFAULT_MARKER

                    # <Value 'text' (18:59)> -> __cache_5115185280
                    __token = 688
                    try:
                        __zt_tmp = __attrs_5115192480
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_5115185280 = _static_4427992992('path', 'text', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'text' (18:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 130e3a4d0> -> __condition
                    __expression = __cache_5115185280

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div>The body</div>')
                    else:
                        __content = __cache_5115185280
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                else:
                    __slot_inside(__stream, econtext.copy(), rcontext)
                __append('\n  </div>')
            if (__backup_text_5110155248 is __marker):
                del econtext['text']
            else:
                econtext['text'] = __backup_text_5110155248
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
            __slot_entries = econtext['__slot_entries'].pop()
        except:
            __slot_entries = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5115198384
            __attrs_5115198384 = _static_4428767312
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5115191712
            __attrs_5115191712 = _static_4428767312
            __backup_batch_4961050656 = get('batch', __marker)

            # <Value 'python:view.batch()' (23:31)> -> __value
            __token = 797
            try:
                __zt_tmp = __attrs_5115191712
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', 'view.batch()', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['batch'] = __value
            __backup_thumb_scale_list_5109674720 = get('thumb_scale_list', __marker)

            # <Value 'python:view.get_thumb_scale_list()' (24:41)> -> __value
            __token = 859
            try:
                __zt_tmp = __attrs_5115191712
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', 'view.get_thumb_scale_list()', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['thumb_scale_list'] = __value
            __backup_thumb_scale_table_5109677600 = get('thumb_scale_table', __marker)

            # <Value 'python:view.get_thumb_scale_table()' (25:41)> -> __value
            __token = 937
            try:
                __zt_tmp = __attrs_5115191712
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', 'view.get_thumb_scale_table()', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['thumb_scale_table'] = __value
            __backup_thumb_scale_summary_5110167488 = get('thumb_scale_summary', __marker)

            # <Value 'python:view.get_thumb_scale_summary()' (26:42)> -> __value
            __token = 1018
            try:
                __zt_tmp = __attrs_5115191712
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', 'view.get_thumb_scale_summary()', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['thumb_scale_summary'] = __value
            __backup_img_class_5108718976 = get('img_class', __marker)

            # <Value "python:'thumb-{} image-responsive'.format(thumb_scale_list)" (27:31)> -> __value
            __token = 1091
            try:
                __zt_tmp = __attrs_5115191712
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', "'thumb-{} image-responsive'.format(thumb_scale_list)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['img_class'] = __value
            __backup_showicons_5109666128 = get('showicons', __marker)

            # <Value 'python:view.show_icons()' (28:30)> -> __value
            __token = 1186
            try:
                __zt_tmp = __attrs_5115191712
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', 'view.show_icons()', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['showicons'] = __value
            __append('\n      ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5115186432
            __attrs_5115186432 = _static_4428767312

            # <Value 'python:batch' (29:30)> -> __condition
            __token = 1248
            try:
                __zt_tmp = __attrs_5115186432
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('python', 'batch', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:
                __append('\n        ')
                if (__slot_entries is None):

                    # <Static value=<ast.Dict object at 0x130e3b340> name=None at 130e3b250> -> __attrs_5108907504
                    __attrs_5108907504 = _static_5115196224
                    __backup_portal_4961817056 = get('portal', __marker)

                    # <Value 'python:portal_state.portal()' (31:31)> -> __value
                    __token = 1351
                    try:
                        __zt_tmp = __attrs_5108907504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4427992992('python', 'portal_state.portal()', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    econtext['portal'] = __value
                    __backup_image_scale_5108859760 = get('image_scale', __marker)

                    # <Value 'portal/@@image_scale' (32:35)> -> __value
                    __token = 1416
                    try:
                        __zt_tmp = __attrs_5108907504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4427992992('path', 'portal/@@image_scale', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    econtext['image_scale'] = __value

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="entries">\n\n          ')
                    __token = None
                    render_entries(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    __append('\n        </div>')
                    if (__backup_image_scale_5108859760 is __marker):
                        del econtext['image_scale']
                    else:
                        econtext['image_scale'] = __backup_image_scale_5108859760
                    if (__backup_portal_4961817056 is __marker):
                        del econtext['portal']
                    else:
                        econtext['portal'] = __backup_portal_4961817056
                else:
                    __slot_entries(__stream, econtext.copy(), rcontext)
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5108900160
                __attrs_5108900160 = _static_4428767312
                __backup_macroname_5115343232 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x13083b580> name=None at 1308382e0> -> __value
                __value = _static_5108905344
                econtext['macroname'] = __value

                # <Value 'context/batch_macros/macros/navigation' (129:30)> -> __macro
                __token = 6459
                try:
                    __zt_tmp = __attrs_5108900160
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_4427992992('path', 'context/batch_macros/macros/navigation', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __token = 6459
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_5115343232 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_5115343232
                __append('\n\n      ')
            __append('\n\n      ')
            if (__slot_no_items_in_listing is None):

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5115052672
                __attrs_5115052672 = _static_4428767312
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x127af94b0> name=None at 127afb040> -> __attrs_4960785392
                __attrs_4960785392 = _static_4960785584

                # <Value 'python: not batch' (135:27)> -> __condition
                __token = 6640
                try:
                    __zt_tmp = __attrs_4960785392
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('python', ' not batch', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="discreet">')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4960793984
                    __default_4960793984 = _DEFAULT_MARKER

                    # <Value 'python: view.no_items_message' (136:25)> -> __cache_4960795328
                    __token = 6684
                    try:
                        __zt_tmp = __attrs_4960785392
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4960795328 = _static_4427992992('python', ' view.no_items_message', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'python: view.no_items_message' (136:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 127af89a0> -> __condition
                    __expression = __cache_4960795328

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n          There are currently no items in this folder.\n        ')
                    else:
                        __content = __cache_4960795328
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</p>')
                __append('\n      ')
            else:
                __slot_no_items_in_listing(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')
            if (__backup_showicons_5109666128 is __marker):
                del econtext['showicons']
            else:
                econtext['showicons'] = __backup_showicons_5109666128
            if (__backup_img_class_5108718976 is __marker):
                del econtext['img_class']
            else:
                econtext['img_class'] = __backup_img_class_5108718976
            if (__backup_thumb_scale_summary_5110167488 is __marker):
                del econtext['thumb_scale_summary']
            else:
                econtext['thumb_scale_summary'] = __backup_thumb_scale_summary_5110167488
            if (__backup_thumb_scale_table_5109677600 is __marker):
                del econtext['thumb_scale_table']
            else:
                econtext['thumb_scale_table'] = __backup_thumb_scale_table_5109677600
            if (__backup_thumb_scale_list_5109674720 is __marker):
                del econtext['thumb_scale_list']
            else:
                econtext['thumb_scale_list'] = __backup_thumb_scale_list_5109674720
            if (__backup_batch_4961050656 is __marker):
                del econtext['batch']
            else:
                econtext['batch'] = __backup_batch_4961050656
            __append('\n  ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_entries(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_entry = econtext['__slot_entry'].pop()
        except:
            __slot_entry = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5108904192
            __attrs_5108904192 = _static_4428767312
            __backup_item_4932410368 = get('item', __marker)

            # <Value 'python:batch' (34:35)> -> __iterator
            __token = 1476
            try:
                __zt_tmp = __attrs_5108904192
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4427992992('python', 'batch', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            (__iterator, ____index_5108895312, ) = getname('repeat')('item', __iterator)
            econtext['item'] = None
            for __item in __iterator:
                econtext['item'] = __item
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5108899776
                __attrs_5108899776 = _static_4428767312
                __backup_obj_5109669632 = get('obj', __marker)

                # <Value 'python:item.getObject()' (35:39)> -> __value
                __token = 1559
                try:
                    __zt_tmp = __attrs_5108899776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'item.getObject()', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['obj'] = __value
                __backup_item_url_4961824592 = get('item_url', __marker)

                # <Value 'python:item.getURL()' (36:24)> -> __value
                __token = 1608
                try:
                    __zt_tmp = __attrs_5108899776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'item.getURL()', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['item_url'] = __value
                __backup_item_id_4932415120 = get('item_id', __marker)

                # <Value 'python:item.getId()' (37:22)> -> __value
                __token = 1653
                try:
                    __zt_tmp = __attrs_5108899776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'item.getId()', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['item_id'] = __value
                __backup_item_title_5108821840 = get('item_title', __marker)

                # <Value 'python:item.Title()' (38:24)> -> __value
                __token = 1700
                try:
                    __zt_tmp = __attrs_5108899776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'item.Title()', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['item_title'] = __value
                __backup_item_title_4961630336 = get('item_title', __marker)

                # <Value 'python:item_title or item_id' (39:23)> -> __value
                __token = 1747
                try:
                    __zt_tmp = __attrs_5108899776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'item_title or item_id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['item_title'] = __value
                __backup_item_description_5110208240 = get('item_description', __marker)

                # <Value 'python:item.Description()' (40:28)> -> __value
                __token = 1809
                try:
                    __zt_tmp = __attrs_5108899776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'item.Description()', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['item_description'] = __value
                __backup_item_type_5108863696 = get('item_type', __marker)

                # <Value 'python:item.PortalType()' (41:20)> -> __value
                __token = 1861
                try:
                    __zt_tmp = __attrs_5108899776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'item.PortalType()', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['item_type'] = __value
                __backup_item_modified_4961820368 = get('item_modified', __marker)

                # <Value 'python:item.ModificationDate()' (42:23)> -> __value
                __token = 1916
                try:
                    __zt_tmp = __attrs_5108899776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'item.ModificationDate()', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['item_modified'] = __value
                __backup_item_created_4961046096 = get('item_created', __marker)

                # <Value 'python:item.CreationDate()' (43:21)> -> __value
                __token = 1976
                try:
                    __zt_tmp = __attrs_5108899776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'item.CreationDate()', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['item_created'] = __value
                __backup_item_wf_state_5110203632 = get('item_wf_state', __marker)

                # <Value 'python:item.review_state()' (44:21)> -> __value
                __token = 2033
                try:
                    __zt_tmp = __attrs_5108899776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'item.review_state()', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['item_wf_state'] = __value
                __backup_item_wf_state_class_5108791472 = get('item_wf_state_class', __marker)

                # <Value "python:'state-' + view.normalizeString(item_wf_state)" (45:26)> -> __value
                __token = 2096
                try:
                    __zt_tmp = __attrs_5108899776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', "'state-' + view.normalizeString(item_wf_state)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['item_wf_state_class'] = __value
                __backup_item_creator_4932418384 = get('item_creator', __marker)

                # <Value 'python:item.Creator()' (46:18)> -> __value
                __token = 2179
                try:
                    __zt_tmp = __attrs_5108899776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'item.Creator()', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['item_creator'] = __value
                __backup_item_link_5110204928 = get('item_link', __marker)

                # <Value "python:item_type in view.use_view_action and item_url+'/view' or item_url" (47:14)> -> __value
                __token = 2227
                try:
                    __zt_tmp = __attrs_5108899776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', "item_type in view.use_view_action and item_url+'/view' or item_url", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['item_link'] = __value
                __backup_item_is_event_5109779856 = get('item_is_event', __marker)

                # <Value 'python:view.is_event(obj)' (48:17)> -> __value
                __token = 2331
                try:
                    __zt_tmp = __attrs_5108899776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'view.is_event(obj)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['item_is_event'] = __value
                __backup_item_has_image_5109783072 = get('item_has_image', __marker)

                # <Value 'python:item.getIcon' (49:17)> -> __value
                __token = 2388
                try:
                    __zt_tmp = __attrs_5108899776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'item.getIcon', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['item_has_image'] = __value
                __backup_item_type_class_4932417184 = get('item_type_class', __marker)

                # <Value "python:('contenttype-' + view.normalizeString(item_type)) if showicons else '' " (50:17)> -> __value
                __token = 2440
                try:
                    __zt_tmp = __attrs_5108899776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', "('contenttype-' + view.normalizeString(item_type)) if showicons else '' ", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['item_type_class'] = __value
                __append('\n              ')
                if (__slot_entry is None):

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5115052960
                    __attrs_5115052960 = _static_4428767312
                    __append('\n\n                ')

                    # <Static value=<ast.Dict object at 0x130e1a4d0> name=None at 130e19b40> -> __attrs_5115063616
                    __attrs_5115063616 = _static_5115061456

                    # <article ... (0:0)
                    # --------------------------------------------------------
                    __append('<article class="mb-3 row">\n\n                  ')
                    __token = None
                    render_listitem(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    __append('\n\n                  ')

                    # <Static value=<ast.Dict object at 0x130e04880> name=None at 130e04850> -> __attrs_5114973296
                    __attrs_5114973296 = _static_5114972288

                    # <Value 'python:item_has_image and thumb_scale_list' (117:61)> -> __condition
                    __token = 6011
                    try:
                        __zt_tmp = __attrs_5114973296
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('python', 'item_has_image and thumb_scale_list', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="col-3 text-end">\n                    ')

                        # <Static value=<ast.Dict object at 0x130e04f40> name=None at 130e04dc0> -> __attrs_4960780592
                        __attrs_4960780592 = _static_5114974016

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5114972960
                        __default_5114972960 = _DEFAULT_MARKER

                        # <Substitution 'python:item_link' (118:44)> -> __attr_href
                        __token = 6100
                        try:
                            __zt_tmp = __attrs_4960780592
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4427992992('python', 'item_link', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>\n                      ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4960785488
                        __attrs_4960785488 = _static_4428767312

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4960794896
                        __default_4960794896 = _DEFAULT_MARKER

                        # <Value "python:image_scale.tag(item, 'image', scale=thumb_scale_list, css_class=img_class)" (119:50)> -> __cache_4960784576
                        __token = 6170
                        try:
                            __zt_tmp = __attrs_4960785488
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4960784576 = _static_4427992992('python', "image_scale.tag(item, 'image', scale=thumb_scale_list, css_class=img_class)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:image_scale.tag(item, 'image', scale=thumb_scale_list, css_class=img_class)" (119:50)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 127af9d20> -> __condition
                        __expression = __cache_4960784576

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <img ... (0:0)
                            # --------------------------------------------------------
                            __append('<img />')
                        else:
                            __content = __cache_4960784576
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n                    </a>\n                  </div>')
                    __append('\n                </article>\n\n              ')
                else:
                    __slot_entry(__stream, econtext.copy(), rcontext)
                __append('\n            ')
                if (__backup_item_type_class_4932417184 is __marker):
                    del econtext['item_type_class']
                else:
                    econtext['item_type_class'] = __backup_item_type_class_4932417184
                if (__backup_item_has_image_5109783072 is __marker):
                    del econtext['item_has_image']
                else:
                    econtext['item_has_image'] = __backup_item_has_image_5109783072
                if (__backup_item_is_event_5109779856 is __marker):
                    del econtext['item_is_event']
                else:
                    econtext['item_is_event'] = __backup_item_is_event_5109779856
                if (__backup_item_link_5110204928 is __marker):
                    del econtext['item_link']
                else:
                    econtext['item_link'] = __backup_item_link_5110204928
                if (__backup_item_creator_4932418384 is __marker):
                    del econtext['item_creator']
                else:
                    econtext['item_creator'] = __backup_item_creator_4932418384
                if (__backup_item_wf_state_class_5108791472 is __marker):
                    del econtext['item_wf_state_class']
                else:
                    econtext['item_wf_state_class'] = __backup_item_wf_state_class_5108791472
                if (__backup_item_wf_state_5110203632 is __marker):
                    del econtext['item_wf_state']
                else:
                    econtext['item_wf_state'] = __backup_item_wf_state_5110203632
                if (__backup_item_created_4961046096 is __marker):
                    del econtext['item_created']
                else:
                    econtext['item_created'] = __backup_item_created_4961046096
                if (__backup_item_modified_4961820368 is __marker):
                    del econtext['item_modified']
                else:
                    econtext['item_modified'] = __backup_item_modified_4961820368
                if (__backup_item_type_5108863696 is __marker):
                    del econtext['item_type']
                else:
                    econtext['item_type'] = __backup_item_type_5108863696
                if (__backup_item_description_5110208240 is __marker):
                    del econtext['item_description']
                else:
                    econtext['item_description'] = __backup_item_description_5110208240
                if (__backup_item_title_4961630336 is __marker):
                    del econtext['item_title']
                else:
                    econtext['item_title'] = __backup_item_title_4961630336
                if (__backup_item_title_5108821840 is __marker):
                    del econtext['item_title']
                else:
                    econtext['item_title'] = __backup_item_title_5108821840
                if (__backup_item_id_4932415120 is __marker):
                    del econtext['item_id']
                else:
                    econtext['item_id'] = __backup_item_id_4932415120
                if (__backup_item_url_4961824592 is __marker):
                    del econtext['item_url']
                else:
                    econtext['item_url'] = __backup_item_url_4961824592
                if (__backup_obj_5109669632 is __marker):
                    del econtext['obj']
                else:
                    econtext['obj'] = __backup_obj_5109669632
                __append('\n          ')
                ____index_5108895312 -= 1
                if (____index_5108895312 > 0):
                    __append('')
            if (__backup_item_4932410368 is __marker):
                del econtext['item']
            else:
                econtext['item'] = __backup_item_4932410368
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

            # <Static value=<ast.Dict object at 0x130e18bb0> name=None at 130e19420> -> __attrs_5115055936
            __attrs_5115055936 = _static_5115055024

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col">\n\n                      ')

            # <Static value=<ast.Dict object at 0x130e1a050> name=None at 130e1a1d0> -> __attrs_5115060592
            __attrs_5115060592 = _static_5115060304

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-1">\n                        ')

            # <Static value=<ast.Dict object at 0x130e19c30> name=None at 130e19ae0> -> __attrs_5115066064
            __attrs_5115066064 = _static_5115059248

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5115056224
            __default_5115056224 = _DEFAULT_MARKER

            # <Substitution 'python:item_link' (59:48)> -> __attr_href
            __token = 2804
            try:
                __zt_tmp = __attrs_5115066064
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4427992992('python', 'item_link', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5115063520
            __default_5115063520 = _DEFAULT_MARKER

            # <Substitution 'string:$item_type_class $item_wf_state_class url' (59:71)> -> __attr_class
            __token = 2827
            try:
                __zt_tmp = __attrs_5115066064
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4427992992('string', '$item_type_class $item_wf_state_class url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5115065824
            __default_5115065824 = _DEFAULT_MARKER

            # <Substitution 'item_type' (59:126)> -> __attr_title
            __token = 2882
            try:
                __zt_tmp = __attrs_5115066064
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_4427992992('path', 'item_type', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append('>')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5115058576
            __default_5115058576 = _DEFAULT_MARKER

            # <Value 'python:item_title' (59:152)> -> __cache_5115060016
            __token = 2908
            try:
                __zt_tmp = __attrs_5115066064
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_5115060016 = _static_4427992992('python', 'item_title', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'python:item_title' (59:152)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 130e19a50> -> __condition
            __expression = __cache_5115060016

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('\n                          Item Title\n                        ')
            else:
                __content = __cache_5115060016
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</a>\n                      </div>\n\n                      ')
            __token = None
            render_document_byline(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n                      ')

            # <Static value=<ast.Dict object at 0x130e06200> name=None at 130e06920> -> __attrs_5114972432
            __attrs_5114972432 = _static_5114978816

            # <Value 'python:item_description' (112:53)> -> __condition
            __token = 5797
            try:
                __zt_tmp = __attrs_5114972432
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('python', 'item_description', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="me-3">')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5115062800
                __default_5115062800 = _DEFAULT_MARKER

                # <Value 'python:item_description' (112:91)> -> __cache_5115065344
                __token = 5835
                try:
                    __zt_tmp = __attrs_5114972432
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_5115065344 = _static_4427992992('python', 'item_description', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:item_description' (112:91)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 130e1ab60> -> __condition
                __expression = __cache_5115065344

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n                        description\n                      ')
                else:
                    __content = __cache_5115065344
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</p>')
            __append('\n                  </div>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_document_byline(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_description_slot = econtext['__slot_description_slot'].pop()
        except:
            __slot_description_slot = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5115065392
            __attrs_5115065392 = _static_4428767312
            __append('\n                      ')

            # <Static value=<ast.Dict object at 0x130e1ab90> name=None at 130e1b070> -> __attrs_5115061264
            __attrs_5115061264 = _static_5115063184

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-1">\n\n                        ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5115066976
            __attrs_5115066976 = _static_4428767312

            # <Value 'python:item_is_event' (67:46)> -> __condition
            __token = 3185
            try:
                __zt_tmp = __attrs_5115066976
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('python', 'item_is_event', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:
                __append('\n                          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5115067408
                __attrs_5115067408 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5115064768
                __default_5115064768 = _DEFAULT_MARKER

                # <Value 'python:view.formatted_date(obj)' (68:59)> -> __cache_5115067264
                __token = 3267
                try:
                    __zt_tmp = __attrs_5115067408
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_5115067264 = _static_4427992992('python', 'view.formatted_date(obj)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:view.formatted_date(obj)' (68:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 130e1bf70> -> __condition
                __expression = __cache_5115067264

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_5115067264
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n                          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5115058720
                __attrs_5115058720 = _static_4428767312

                # <Value 'python:obj.location' (69:47)> -> __condition
                __token = 3349
                try:
                    __zt_tmp = __attrs_5115058720
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('python', 'obj.location', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_5114231744_location = ''
                    __stream_5115062272 = []
                    __append_5115062272 = __stream_5115062272.append
                    __append_5115062272('\n                            &mdash;\n                            ')
                    __stream_5114231744_location = []
                    __append_5114231744_location = __stream_5114231744_location.append

                    # <Static value=<ast.Dict object at 0x130e07190> name=None at 130e07730> -> __attrs_5114983904
                    __attrs_5114983904 = _static_5114982800

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_5114231744_location('<span class="location">')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5114983232
                    __default_5114983232 = _DEFAULT_MARKER

                    # <Value 'python:obj.location' (71:47)> -> __cache_5114971376
                    __token = 3499
                    try:
                        __zt_tmp = __attrs_5114983904
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_5114971376 = _static_4427992992('python', 'obj.location', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'python:obj.location' (71:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 130e07dc0> -> __condition
                    __expression = __cache_5114971376

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append_5114231744_location('Oslo')
                    else:
                        __content = __cache_5114971376
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_5114231744_location(__content)
                    __append_5114231744_location('</span>')
                    __append_5115062272('${location}')
                    __stream_5114231744_location = ''.join(__stream_5114231744_location)
                    __append_5115062272('\n                          ')
                    __msgid_5115062272 = __re_whitespace(''.join(__stream_5115062272)).strip()
                    if 'label_event_byline_location':
                        __append(translate('label_event_byline_location', mapping={'location': __stream_5114231744_location, }, default=__msgid_5115062272, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>')
                __append('\n                          &mdash;\n                        ')
            __append('\n\n                        ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5114983184
            __attrs_5114983184 = _static_4428767312

            # <Value 'python:view.show_about' (76:47)> -> __condition
            __token = 3723
            try:
                __zt_tmp = __attrs_5114983184
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('python', 'view.show_about', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:
                __append('\n                          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5114984432
                __attrs_5114984432 = _static_4428767312
                __backup_author_5108717584 = get('author', __marker)

                # <Value 'python:view.pas_member.info(item_creator)' (78:49)> -> __value
                __token = 3869
                try:
                    __zt_tmp = __attrs_5114984432
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'view.pas_member.info(item_creator)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['author'] = __value
                __backup_creator_short_form_5109668336 = get('creator_short_form', __marker)

                # <Value "python:author.get('username')" (79:60)> -> __value
                __token = 3972
                try:
                    __zt_tmp = __attrs_5114984432
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', "author.get('username')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['creator_short_form'] = __value
                __backup_creator_long_form_5110215632 = get('creator_long_form', __marker)

                # <Value 'string:?author=$${python:author.username}' (80:58)> -> __value
                __token = 4062
                try:
                    __zt_tmp = __attrs_5114984432
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('string', '?author=$${python:author.username}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['creator_long_form'] = __value
                __backup_creator_is_openid_5109790944 = get('creator_is_openid', __marker)

                # <Value "python:'/' in creator_short_form" (81:57)> -> __value
                __token = 4164
                try:
                    __zt_tmp = __attrs_5114984432
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', "'/' in creator_short_form", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['creator_is_openid'] = __value
                __backup_creator_id_4960590512 = get('creator_id', __marker)

                # <Value 'python:(creator_short_form, creator_long_form)[creator_is_openid]' (82:49)> -> __value
                __token = 4250
                try:
                    __zt_tmp = __attrs_5114984432
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', '(creator_short_form, creator_long_form)[creator_is_openid]', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['creator_id'] = __value

                # <Value 'python:item_creator' (77:51)> -> __condition
                __token = 3799
                try:
                    __zt_tmp = __attrs_5114984432
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('python', 'item_creator', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:
                    __append('\n                          ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5114976032
                    __attrs_5114976032 = _static_4428767312

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_5114231520_author = ''
                    __stream_5114984960 = []
                    __append_5114984960 = __stream_5114984960.append
                    __append_5114984960('\n                            by\n                            ')
                    __stream_5114231520_author = []
                    __append_5114231520_author = __stream_5114231520_author.append

                    # <Static value=<ast.Dict object at 0x130e06590> name=None at 130e055a0> -> __attrs_5114981312
                    __attrs_5114981312 = _static_5114979728

                    # <Negate value=<Value 'python: not author' (87:46)> at 130e063b0> -> __cache_5114979248

                    # <Value 'python: not author' (87:46)> -> __cache_5114979248
                    __token = 4656
                    try:
                        __zt_tmp = __attrs_5114981312
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_5114979248 = _static_4427992992('python', ' not author', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __cache_5114979248 = not __cache_5114979248
                    __condition = __cache_5114979248
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append_5114231520_author('<a')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5114979680
                        __default_5114979680 = _DEFAULT_MARKER

                        # <Substitution 'string:${view/navigation_root_url}/author/${item_creator}' (85:52)> -> __attr_href
                        __token = 4472
                        try:
                            __zt_tmp = __attrs_5114981312
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4427992992('string', '${view/navigation_root_url}/author/${item_creator}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append_5114231520_author((' href="%s"' % __attr_href))
                        __append_5114231520_author('>')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5114980976
                    __default_5114980976 = _DEFAULT_MARKER

                    # <Value "python: author.get('name_or_id')" (86:45)> -> __cache_5114980304
                    __token = 4576
                    try:
                        __zt_tmp = __attrs_5114981312
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_5114980304 = _static_4427992992('python', " author.get('name_or_id')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value "python: author.get('name_or_id')" (86:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 130e047f0> -> __condition
                    __expression = __cache_5114980304

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append_5114231520_author('\n                              Bob Dobalina\n                            ')
                    else:
                        __content = __cache_5114980304
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_5114231520_author(__content)
                    __condition = __cache_5114979248
                    if __condition:
                        __append_5114231520_author('</a>')
                    __append_5114984960('${author}')
                    __stream_5114231520_author = ''.join(__stream_5114231520_author)
                    __append_5114984960('\n                          ')
                    __msgid_5114984960 = __re_whitespace(''.join(__stream_5114984960)).strip()
                    if 'label_by_author':
                        __append(translate('label_by_author', mapping={'author': __stream_5114231520_author, }, default=__msgid_5114984960, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n                          ')
                if (__backup_creator_id_4960590512 is __marker):
                    del econtext['creator_id']
                else:
                    econtext['creator_id'] = __backup_creator_id_4960590512
                if (__backup_creator_is_openid_5109790944 is __marker):
                    del econtext['creator_is_openid']
                else:
                    econtext['creator_is_openid'] = __backup_creator_is_openid_5109790944
                if (__backup_creator_long_form_5110215632 is __marker):
                    del econtext['creator_long_form']
                else:
                    econtext['creator_long_form'] = __backup_creator_long_form_5110215632
                if (__backup_creator_short_form_5109668336 is __marker):
                    del econtext['creator_short_form']
                else:
                    econtext['creator_short_form'] = __backup_creator_short_form_5109668336
                if (__backup_author_5108717584 is __marker):
                    del econtext['author']
                else:
                    econtext['author'] = __backup_author_5108717584
                __append('\n\n                          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5114982656
                __attrs_5114982656 = _static_4428767312

                # <Value "python:item_type != 'Event'" (94:51)> -> __condition
                __token = 4928
                try:
                    __zt_tmp = __attrs_5114982656
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('python', "item_type != 'Event'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:
                    __append('\n                            &mdash;\n                            ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5114977856
                    __attrs_5114977856 = _static_4428767312
                    __stream_5114970752 = []
                    __append_5114970752 = __stream_5114970752.append
                    __append_5114970752('last modified')
                    __msgid_5114970752 = __re_whitespace(''.join(__stream_5114970752)).strip()
                    if 'box_last_modified':
                        __append(translate('box_last_modified', mapping=None, default=__msgid_5114970752, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n                            ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5114978240
                    __attrs_5114978240 = _static_4428767312

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5114978288
                    __default_5114978288 = _DEFAULT_MARKER

                    # <Value 'python:view.toLocalizedTime(item_modified,long_format=1)' (97:47)> -> __cache_5114976320
                    __token = 5137
                    try:
                        __zt_tmp = __attrs_5114978240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_5114976320 = _static_4427992992('python', 'view.toLocalizedTime(item_modified,long_format=1)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'python:view.toLocalizedTime(item_modified,long_format=1)' (97:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 130e059c0> -> __condition
                    __expression = __cache_5114976320

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>\n                              August 16, 2001 at 23:35:59\n                            </span>')
                    else:
                        __content = __cache_5114976320
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n                          ')
                __append('\n\n                          ')
                if (__slot_description_slot is None):

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5114978912
                    __attrs_5114978912 = _static_4428767312
                    __append('\n                            ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5114977184
                    __attrs_5114977184 = _static_4428767312

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5114977568
                    __default_5114977568 = _DEFAULT_MARKER

                    # <Value 'nothing' (103:50)> -> __cache_5114976416
                    __token = 5460
                    try:
                        __zt_tmp = __attrs_5114977184
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_5114976416 = _static_4427992992('path', 'nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (103:50)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 130e05bd0> -> __condition
                    __expression = __cache_5114976416

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                              Place custom listing info for custom types here\n                            ')
                    else:
                        __content = __cache_5114976416
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n                          ')
                else:
                    __slot_description_slot(__stream, econtext.copy(), rcontext)
                __append('\n\n                        ')
            __append('\n                      </div>\n                      ')
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

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5115192816
            __attrs_5115192816 = _static_4428767312
            __previous_i18n_domain_5115188304 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_5115270336 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x130e395d0> name=None at 130e38640> -> __value
            __value = _static_5115188688
            econtext['macroname'] = __value

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5115194592
                __attrs_5115194592 = _static_4428767312
                __append('\n')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/@@main_template/macros/master' (6:21)> -> __macro
            __token = 251
            try:
                __zt_tmp = __attrs_5115192816
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4427992992('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __token = 251
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_5115270336 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_5115270336
            __i18n_domain = __previous_i18n_domain_5115188304
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render_text_field_view': render_text_field_view, 'render_listing': render_listing, 'render_entries': render_entries, 'render_listitem': render_listitem, 'render_document_byline': render_document_byline, 'render': render, }