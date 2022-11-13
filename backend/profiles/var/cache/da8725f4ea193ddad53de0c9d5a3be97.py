# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/contenttypes/browser/templates/listing_summary.pt'

__tokens = {606: ('context/@@plone_portal_state/portal', 16, 86), 654: (' portal/@@image_scal', 16, 134), 1060: ('context/@@listing_view/macros/document_byline', 31, 34), 1060: ('context/@@listing_view/macros/document_byline', 31, 34), 1175: ('item_description', 34, 43), 1245: ('item_description', 35, 51), 1393: ('item_link', 41, 36), 1576: ('python: item_has_image and thumb_scale_summary', 49, 30), 1661: ('item_link', 50, 36), 1715: ("python:image_scale.tag(item, 'image', scale=thumb_scale_summary, css_class='image-responsive thumb-' + thumb_scale_summary)", 51, 42), 548: ('context/@@listing_view/macros/entries', 16, 28), 548: ('context/@@listing_view/macros/entries', 16, 28), 436: ('context/@@listing_view/macros/content-core', 13, 24), 436: ('context/@@listing_view/macros/content-core', 13, 24), 884: ('item_link', 25, 56), 900: (' item_typ', 25, 72), 925: ('item_title', 25, 97), 251: ('context/@@main_template/macros/master', 6, 21), 251: ('context/@@main_template/macros/master', 6, 21)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4899042832 = 'master'
_static_4886615264 = {'class': 'summary url', 'href': 'item_link', 'title': 'item_type', }
_static_4886779584 = {'href': 'item_link', }
_static_4886774304 = {'class': 'col-3', }
_static_4886778768 = {'href': 'item_link', }
_static_4886777520 = {'class': 'mb-1', }
_static_4886781552 = {'class': 'description', }
_static_4886625824 = {'class': 'mb-1', }
_static_4886625392 = 'document_byline'
_static_4886622512 = {'class': 'mb-3', }
_static_4886616080 = {'class': 'col', }
_static_4886617520 = {'class': 'row mb-3', }
_static_4886610512 = 'entries'
_static_4439051040 = __C2ZContextWrapper
_static_4439058528 = __compile_zt_expr
_static_4880697520 = 'content-core'
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4880703616
            __attrs_4880703616 = _static_4438893776
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4880702656
            __attrs_4880702656 = _static_4438893776
            __backup_macroname_4852136896 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x122e988b0> name=None at 122e9b6d0> -> __value
            __value = _static_4880697520
            econtext['macroname'] = __value

            def __fill_entries(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4886613440
                __attrs_4886613440 = _static_4438893776
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4886613872
                __attrs_4886613872 = _static_4438893776
                __backup_portal_4697401776 = get('portal', __marker)

                # <Value 'context/@@plone_portal_state/portal' (16:86)> -> __value
                __token = 606
                try:
                    __zt_tmp = __attrs_4886613872
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'context/@@plone_portal_state/portal', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['portal'] = __value
                __backup_image_scale_4840417088 = get('image_scale', __marker)

                # <Value 'portal/@@image_scale' (16:134)> -> __value
                __token = 654
                try:
                    __zt_tmp = __attrs_4886613872
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'portal/@@image_scale', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['image_scale'] = __value
                __backup_macroname_4617621184 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x12343c250> name=None at 12343c3a0> -> __value
                __value = _static_4886610512
                econtext['macroname'] = __value

                def __fill_entry(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                    getname = econtext.get_name
                    get = econtext.get

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4886618240
                    __attrs_4886618240 = _static_4438893776
                    __append('\n\n        ')

                    # <Static value=<ast.Dict object at 0x12343ddb0> name=None at 12343de10> -> __attrs_4886610752
                    __attrs_4886610752 = _static_4886617520

                    # <article ... (0:0)
                    # --------------------------------------------------------
                    __append('<article class="row mb-3">\n\n          ')

                    # <Static value=<ast.Dict object at 0x12343d810> name=None at 12343e380> -> __attrs_4886620016
                    __attrs_4886620016 = _static_4886616080

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="col">\n\n          ')
                    __token = None
                    render_listitem(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    __append('\n\n          ')

                    # <Static value=<ast.Dict object at 0x12343f130> name=None at 12343f550> -> __attrs_4886623856
                    __attrs_4886623856 = _static_4886622512

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="mb-3">\n            ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4886624960
                    __attrs_4886624960 = _static_4438893776
                    __backup_macroname_4843874496 = get('macroname', __marker)

                    # <Static value=<ast.Constant object at 0x12343fc70> name=None at 12343fa60> -> __value
                    __value = _static_4886625392
                    econtext['macroname'] = __value

                    # <Value 'context/@@listing_view/macros/document_byline' (31:34)> -> __macro
                    __token = 1060
                    try:
                        __zt_tmp = __attrs_4886624960
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __macro = _static_4439058528('path', 'context/@@listing_view/macros/document_byline', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    __token = 1060
                    __m = __macro.include
                    __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    if (__backup_macroname_4843874496 is __marker):
                        del econtext['macroname']
                    else:
                        econtext['macroname'] = __backup_macroname_4843874496
                    __append('\n          </div>\n\n          ')

                    # <Static value=<ast.Dict object at 0x12343fe20> name=None at 12343fdf0> -> __attrs_4886624192
                    __attrs_4886624192 = _static_4886625824

                    # <Value 'item_description' (34:43)> -> __condition
                    __token = 1175
                    try:
                        __zt_tmp = __attrs_4886624192
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4439058528('path', 'item_description', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="mb-1">\n            ')

                        # <Static value=<ast.Dict object at 0x123465e70> name=None at 123465e40> -> __attrs_4886781744
                        __attrs_4886781744 = _static_4886781552

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="description">')

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4886781024
                        __default_4886781024 = _DEFAULT_MARKER

                        # <Value 'item_description' (35:51)> -> __cache_4886617088
                        __token = 1245
                        try:
                            __zt_tmp = __attrs_4886781744
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4886617088 = _static_4439058528('path', 'item_description', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                        # <BinOp left=<Value 'item_description' (35:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 123465f90> -> __condition
                        __expression = __cache_4886617088

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n              description\n            ')
                        else:
                            __content = __cache_4886617088
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>\n          </div>')
                    __append('\n\n          ')

                    # <Static value=<ast.Dict object at 0x123464eb0> name=None at 123465cc0> -> __attrs_4886781984
                    __attrs_4886781984 = _static_4886777520

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="mb-1">\n            ')

                    # <Static value=<ast.Dict object at 0x123465390> name=None at 123465330> -> __attrs_4886778912
                    __attrs_4886778912 = _static_4886778768

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4886774976
                    __default_4886774976 = _DEFAULT_MARKER

                    # <Substitution 'item_link' (41:36)> -> __attr_href
                    __token = 1393
                    try:
                        __zt_tmp = __attrs_4886778912
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4439058528('path', 'item_link', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append('>')
                    __stream_4886774736 = []
                    __append_4886774736 = __stream_4886774736.append
                    __append_4886774736('\n              Read More&hellip;\n            ')
                    __msgid_4886774736 = __re_whitespace(''.join(__stream_4886774736)).strip()
                    if 'read_more':
                        __append(translate('read_more', mapping=None, default=__msgid_4886774736, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</a>\n          </div>\n\n          </div>\n\n          ')

                    # <Static value=<ast.Dict object at 0x123464220> name=None at 1234651e0> -> __attrs_4886774400
                    __attrs_4886774400 = _static_4886774304

                    # <Value 'python: item_has_image and thumb_scale_summary' (49:30)> -> __condition
                    __token = 1576
                    try:
                        __zt_tmp = __attrs_4886774400
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4439058528('python', ' item_has_image and thumb_scale_summary', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="col-3">\n            ')

                        # <Static value=<ast.Dict object at 0x1234656c0> name=None at 123465660> -> __attrs_4886780160
                        __attrs_4886780160 = _static_4886779584

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4886778000
                        __default_4886778000 = _DEFAULT_MARKER

                        # <Substitution 'item_link' (50:36)> -> __attr_href
                        __token = 1661
                        try:
                            __zt_tmp = __attrs_4886780160
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4439058528('path', 'item_link', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>\n              ')

                        # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4886784864
                        __attrs_4886784864 = _static_4438893776

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4886785536
                        __default_4886785536 = _DEFAULT_MARKER

                        # <Value "python:image_scale.tag(item, 'image', scale=thumb_scale_summary, css_class='image-responsive thumb-' + thumb_scale_summary)" (51:42)> -> __cache_4886784240
                        __token = 1715
                        try:
                            __zt_tmp = __attrs_4886784864
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4886784240 = _static_4439058528('python', "image_scale.tag(item, 'image', scale=thumb_scale_summary, css_class='image-responsive thumb-' + thumb_scale_summary)", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:image_scale.tag(item, 'image', scale=thumb_scale_summary, css_class='image-responsive thumb-' + thumb_scale_summary)" (51:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 123465a20> -> __condition
                        __expression = __cache_4886784240

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <img ... (0:0)
                            # --------------------------------------------------------
                            __append('<img />')
                        else:
                            __content = __cache_4886784240
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n            </a>\n          </div>')
                    __append('\n\n        </article>\n\n      ')
                _slots = econtext['__slot_entry'] = _deque((__fill_entry, ))

                # <Value 'context/@@listing_view/macros/entries' (16:28)> -> __macro
                __token = 548
                try:
                    __zt_tmp = __attrs_4886613872
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_4439058528('path', 'context/@@listing_view/macros/entries', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __token = 548
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_4617621184 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_4617621184
                if (__backup_image_scale_4840417088 is __marker):
                    del econtext['image_scale']
                else:
                    econtext['image_scale'] = __backup_image_scale_4840417088
                if (__backup_portal_4697401776 is __marker):
                    del econtext['portal']
                else:
                    econtext['portal'] = __backup_portal_4697401776
                __append('\n  ')
            _slots = econtext['__slot_entries'] = _deque((__fill_entries, ))

            # <Value 'context/@@listing_view/macros/content-core' (13:24)> -> __macro
            __token = 436
            try:
                __zt_tmp = __attrs_4880702656
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4439058528('path', 'context/@@listing_view/macros/content-core', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __token = 436
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4852136896 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4852136896
            __append('\n\n')
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4886621024
            __attrs_4886621024 = _static_4438893776

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append('<h2>\n            ')

            # <Static value=<ast.Dict object at 0x12343d4e0> name=None at 12343d540> -> __attrs_4886623040
            __attrs_4886623040 = _static_4886615264

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="summary url"')

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4886619200
            __default_4886619200 = _DEFAULT_MARKER

            # <Substitution 'item_link' (25:56)> -> __attr_href
            __token = 884
            try:
                __zt_tmp = __attrs_4886623040
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4439058528('path', 'item_link', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4886622656
            __default_4886622656 = _DEFAULT_MARKER

            # <Substitution 'item_type' (25:72)> -> __attr_title
            __token = 900
            try:
                __zt_tmp = __attrs_4886623040
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_4439058528('path', 'item_type', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append('>')

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4886620160
            __default_4886620160 = _DEFAULT_MARKER

            # <Value 'item_title' (25:97)> -> __cache_4886619728
            __token = 925
            try:
                __zt_tmp = __attrs_4886623040
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4886619728 = _static_4439058528('path', 'item_title', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

            # <BinOp left=<Value 'item_title' (25:97)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 12343dc60> -> __condition
            __expression = __cache_4886619728

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('\n              Item Title\n            ')
            else:
                __content = __cache_4886619728
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</a>\n          </h2>')
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4899045136
            __attrs_4899045136 = _static_4438893776
            __previous_i18n_domain_4902162624 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4636835328 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x124017610> name=None at 1240167d0> -> __value
            __value = _static_4899042832
            econtext['macroname'] = __value

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900366000
                __attrs_4900366000 = _static_4438893776
                __append('\n')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/@@main_template/macros/master' (6:21)> -> __macro
            __token = 251
            try:
                __zt_tmp = __attrs_4899045136
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4439058528('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __token = 251
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4636835328 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4636835328
            __i18n_domain = __previous_i18n_domain_4902162624
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render_listitem': render_listitem, 'render': render, }