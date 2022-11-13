# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/contenttypes/browser/templates/listing_album.pt'

__tokens = {441: ('view/album_images', 11, 65), 466: (' view/album_folder', 11, 90), 589: ('view/text', 13, 100), 615: ('text', 13, 126), 643: ('view/text_class', 13, 154), 720: ('text', 14, 59), 815: ('context/@@plone_portal_state/portal', 17, 64), 863: (' portal/@@image_scal', 17, 112), 941: ('images', 21, 32), 1039: ("python:image_scale.tag(image, 'image', scale='mini')", 24, 31), 1108: ('scale', 24, 100), 1245: ('scale', 25, 38), 1348: ('image/Title', 28, 46), 1422: ('image/Description', 29, 44), 1524: ('string:${image/getURL}/view', 30, 67), 1558: (' image/Descriptio', 30, 101), 1703: ('albums', 36, 32), 1807: ("python:image_scale.tag(album, 'image', scale='mini') if getattr(album, 'image', None) else None", 39, 31), 1928: ('scale', 40, 24), 2065: ('scale', 41, 38), 2168: ('album/Title', 44, 46), 2242: ('album/Description', 45, 44), 2344: ('string:${album/getURL}/view', 46, 67), 2378: (' album/Descriptio', 46, 101), 2525: ('context/batch_macros/macros/navigation', 54, 24), 2525: ('context/batch_macros/macros/navigation', 54, 24), 2647: ('python: not images and not albums', 57, 22), 2695: ('view/no_items_message', 57, 70), 261: ('here/main_template/macros/master', 6, 23), 261: ('here/main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_4882409040 = 'master'
_static_4902370992 = 'navigation'
_static_4881066080 = {'class': 'card-link stretched-link', 'href': 'string:${album/getURL}/view', 'title': 'album/Description', }
_static_4901609840 = {'class': 'card-text', }
_static_4901615744 = {'class': 'card-title', }
_static_4903062208 = {'class': 'card-body', }
_static_4903360000 = {'class': 'card-image d-flex justify-content-center align-items-center', 'style': 'height: 14rem;', }
_static_4903366288 = {'class': 'card album h-100', }
_static_4903355488 = {'class': 'col mb-5', }
_static_4903362016 = {'class': 'card-link stretched-link', 'href': 'string:${image/getURL}/view', 'title': 'image/Description', }
_static_4903369024 = {'class': 'card-text', }
_static_4903361152 = {'class': 'card-title', }
_static_4903358992 = {'class': 'card-body', }
_static_4900940160 = {'class': 'card-image d-flex justify-content-center align-items-center', 'style': 'height: 14rem;', }
_static_4902362064 = {'class': 'card h-100', }
_static_4902358608 = {'class': 'col mb-5', }
_static_4902369264 = {'class': 'row', }
_static_4880488176 = {'id': 'parent-fieldname-text', 'class': 'stx', }
_static_4439051040 = __C2ZContextWrapper
_static_4439058528 = __compile_zt_expr
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4637603824
            __attrs_4637603824 = _static_4438893776
            __backup_images_4901610848 = get('images', __marker)

            # <Value 'view/album_images' (11:65)> -> __value
            __token = 441
            try:
                __zt_tmp = __attrs_4637603824
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'view/album_images', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['images'] = __value
            __backup_albums_4901614256 = get('albums', __marker)

            # <Value 'view/album_folders' (11:90)> -> __value
            __token = 466
            try:
                __zt_tmp = __attrs_4637603824
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'view/album_folders', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['albums'] = __value
            __append('\n\n  ')
            __token = None
            render_text_field_view(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n  ')
            __token = None
            render_listing(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n')
            if (__backup_albums_4901614256 is __marker):
                del econtext['albums']
            else:
                econtext['albums'] = __backup_albums_4901614256
            if (__backup_images_4901610848 is __marker):
                del econtext['images']
            else:
                econtext['images'] = __backup_images_4901610848
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

            # <Static value=<ast.Dict object at 0x122e656f0> name=None at 122e654e0> -> __attrs_4880494080
            __attrs_4880494080 = _static_4880488176
            __backup_text_4902172128 = get('text', __marker)

            # <Value 'view/text' (13:100)> -> __value
            __token = 589
            try:
                __zt_tmp = __attrs_4880494080
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'view/text', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['text'] = __value

            # <Value 'text' (13:126)> -> __condition
            __token = 615
            try:
                __zt_tmp = __attrs_4880494080
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4439058528('path', 'text', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="parent-fieldname-text"')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4880498544
                __default_4880498544 = _DEFAULT_MARKER

                # <Substitution 'view/text_class' (13:154)> -> __attr_class
                __token = 643
                try:
                    __zt_tmp = __attrs_4880494080
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_4439058528('path', 'view/text_class', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', 'stx', _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append('>\n    ')
                if (__slot_inside is None):

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4902364992
                    __attrs_4902364992 = _static_4438893776

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4902356352
                    __default_4902356352 = _DEFAULT_MARKER

                    # <Value 'text' (14:59)> -> __cache_4902370848
                    __token = 720
                    try:
                        __zt_tmp = __attrs_4902364992
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4902370848 = _static_4439058528('path', 'text', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value 'text' (14:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1243439d0> -> __condition
                    __expression = __cache_4902370848

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div>The body</div>')
                    else:
                        __content = __cache_4902370848
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                else:
                    __slot_inside(__stream, econtext.copy(), rcontext)
                __append('\n  </div>')
            if (__backup_text_4902172128 is __marker):
                del econtext['text']
            else:
                econtext['text'] = __backup_text_4902172128
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4902366864
            __attrs_4902366864 = _static_4438893776
            __backup_portal_4902172560 = get('portal', __marker)

            # <Value 'context/@@plone_portal_state/portal' (17:64)> -> __value
            __token = 815
            try:
                __zt_tmp = __attrs_4902366864
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'context/@@plone_portal_state/portal', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['portal'] = __value
            __backup_image_scale_4902161232 = get('image_scale', __marker)

            # <Value 'portal/@@image_scale' (17:112)> -> __value
            __token = 863
            try:
                __zt_tmp = __attrs_4902366864
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'portal/@@image_scale', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['image_scale'] = __value
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x1243437f0> name=None at 124341870> -> __attrs_4902360336
            __attrs_4902360336 = _static_4902369264

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="row">\n\n  ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4902359280
            __attrs_4902359280 = _static_4438893776
            __backup_image_4903008720 = get('image', __marker)

            # <Value 'images' (21:32)> -> __iterator
            __token = 941
            try:
                __zt_tmp = __attrs_4902359280
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4439058528('path', 'images', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            (__iterator, ____index_4902360192, ) = getname('repeat')('image', __iterator)
            econtext['image'] = None
            for __item in __iterator:
                econtext['image'] = __item
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x124340e50> name=None at 124343610> -> __attrs_4902356016
                __attrs_4902356016 = _static_4902358608

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="col mb-5">\n      ')

                # <Static value=<ast.Dict object at 0x124341bd0> name=None at 124343be0> -> __attrs_4902363648
                __attrs_4902363648 = _static_4902362064

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="card h-100">\n        ')

                # <Static value=<ast.Dict object at 0x1241e6980> name=None at 1241e7640> -> __attrs_4851668624
                __attrs_4851668624 = _static_4900940160
                __backup_scale_4882755936 = get('scale', __marker)

                # <Value "python:image_scale.tag(image, 'image', scale='mini')" (24:31)> -> __value
                __token = 1039
                try:
                    __zt_tmp = __attrs_4851668624
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', "image_scale.tag(image, 'image', scale='mini')", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['scale'] = __value

                # <Value 'scale' (24:100)> -> __condition
                __token = 1108
                try:
                    __zt_tmp = __attrs_4851668624
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('path', 'scale', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="card-image d-flex justify-content-center align-items-center" style="height: 14rem;">\n          ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903362544
                    __attrs_4903362544 = _static_4438893776

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4903354624
                    __default_4903354624 = _DEFAULT_MARKER

                    # <Value 'scale' (25:38)> -> __cache_4900171456
                    __token = 1245
                    try:
                        __zt_tmp = __attrs_4903362544
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4900171456 = _static_4439058528('path', 'scale', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value 'scale' (25:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 124434ca0> -> __condition
                    __expression = __cache_4900171456

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <img ... (0:0)
                        # --------------------------------------------------------
                        __append('<img />')
                    else:
                        __content = __cache_4900171456
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n        </div>')
                if (__backup_scale_4882755936 is __marker):
                    del econtext['scale']
                else:
                    econtext['scale'] = __backup_scale_4882755936
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x124435210> name=None at 124435870> -> __attrs_4903367056
                __attrs_4903367056 = _static_4903358992

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="card-body">\n          ')

                # <Static value=<ast.Dict object at 0x124435a80> name=None at 124435f90> -> __attrs_4903356832
                __attrs_4903356832 = _static_4903361152

                # <h5 ... (0:0)
                # --------------------------------------------------------
                __append('<h5 class="card-title">')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4903361776
                __default_4903361776 = _DEFAULT_MARKER

                # <Value 'image/Title' (28:46)> -> __cache_4903361488
                __token = 1348
                try:
                    __zt_tmp = __attrs_4903356832
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4903361488 = _static_4439058528('path', 'image/Title', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'image/Title' (28:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 124434700> -> __condition
                __expression = __cache_4903361488

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Image title')
                else:
                    __content = __cache_4903361488
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</h5>\n          ')

                # <Static value=<ast.Dict object at 0x124437940> name=None at 124435300> -> __attrs_4903360816
                __attrs_4903360816 = _static_4903369024

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="card-text">')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4903365520
                __default_4903365520 = _DEFAULT_MARKER

                # <Value 'image/Description' (29:44)> -> __cache_4903358512
                __token = 1422
                try:
                    __zt_tmp = __attrs_4903360816
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4903358512 = _static_4439058528('path', 'image/Description', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'image/Description' (29:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 124436530> -> __condition
                __expression = __cache_4903358512

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Description')
                else:
                    __content = __cache_4903358512
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</p>\n          ')

                # <Static value=<ast.Dict object at 0x124435de0> name=None at 1244377c0> -> __attrs_4903368304
                __attrs_4903368304 = _static_4903362016

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="card-link stretched-link"')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4903368160
                __default_4903368160 = _DEFAULT_MARKER

                # <Substitution 'string:${image/getURL}/view' (30:67)> -> __attr_href
                __token = 1524
                try:
                    __zt_tmp = __attrs_4903368304
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4439058528('string', '${image/getURL}/view', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4903367632
                __default_4903367632 = _DEFAULT_MARKER

                # <Substitution 'image/Description' (30:101)> -> __attr_title
                __token = 1558
                try:
                    __zt_tmp = __attrs_4903368304
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_title = _static_4439058528('path', 'image/Description', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_title is not None):
                    __append((' title="%s"' % __attr_title))
                __append('>')
                __stream_4903362256 = []
                __append_4903362256 = __stream_4903362256.append
                __append_4903362256('View')
                __msgid_4903362256 = __re_whitespace(''.join(__stream_4903362256)).strip()
                if 'label_view':
                    __append(translate('label_view', mapping=None, default=__msgid_4903362256, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</a>\n        </div>\n      </div>\n    </div>\n  ')
                ____index_4902360192 -= 1
                if (____index_4902360192 > 0):
                    __append('')
            if (__backup_image_4903008720 is __marker):
                del econtext['image']
            else:
                econtext['image'] = __backup_image_4903008720
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4902365520
            __attrs_4902365520 = _static_4438893776
            __backup_album_4902998928 = get('album', __marker)

            # <Value 'albums' (36:32)> -> __iterator
            __token = 1703
            try:
                __zt_tmp = __attrs_4902365520
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4439058528('path', 'albums', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            (__iterator, ____index_4903365760, ) = getname('repeat')('album', __iterator)
            econtext['album'] = None
            for __item in __iterator:
                econtext['album'] = __item
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x124434460> name=None at 124437d00> -> __attrs_4903370128
                __attrs_4903370128 = _static_4903355488

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="col mb-5">\n      ')

                # <Static value=<ast.Dict object at 0x124436e90> name=None at 1244374c0> -> __attrs_4903356064
                __attrs_4903356064 = _static_4903366288

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="card album h-100">\n        ')

                # <Static value=<ast.Dict object at 0x124435600> name=None at 124434e50> -> __attrs_4903370272
                __attrs_4903370272 = _static_4903360000
                __backup_scale_4882758000 = get('scale', __marker)

                # <Value "python:image_scale.tag(album, 'image', scale='mini') if getattr(album, 'image', None) else None" (39:31)> -> __value
                __token = 1807
                try:
                    __zt_tmp = __attrs_4903370272
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', "image_scale.tag(album, 'image', scale='mini') if getattr(album, 'image', None) else None", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['scale'] = __value

                # <Value 'scale' (40:24)> -> __condition
                __token = 1928
                try:
                    __zt_tmp = __attrs_4903370272
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('path', 'scale', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="card-image d-flex justify-content-center align-items-center" style="height: 14rem;">\n          ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903068832
                    __attrs_4903068832 = _static_4438893776

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4903074256
                    __default_4903074256 = _DEFAULT_MARKER

                    # <Value 'scale' (41:38)> -> __cache_4903071664
                    __token = 2065
                    try:
                        __zt_tmp = __attrs_4903068832
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4903071664 = _static_4439058528('path', 'scale', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value 'scale' (41:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1243ecbb0> -> __condition
                    __expression = __cache_4903071664

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <img ... (0:0)
                        # --------------------------------------------------------
                        __append('<img />')
                    else:
                        __content = __cache_4903071664
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n        </div>')
                if (__backup_scale_4882758000 is __marker):
                    del econtext['scale']
                else:
                    econtext['scale'] = __backup_scale_4882758000
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x1243ecac0> name=None at 1243ec5e0> -> __attrs_4903061968
                __attrs_4903061968 = _static_4903062208

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="card-body">\n          ')

                # <Static value=<ast.Dict object at 0x12428b880> name=None at 1242897b0> -> __attrs_4901603408
                __attrs_4901603408 = _static_4901615744

                # <h5 ... (0:0)
                # --------------------------------------------------------
                __append('<h5 class="card-title">')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901608112
                __default_4901608112 = _DEFAULT_MARKER

                # <Value 'album/Title' (44:46)> -> __cache_4903060048
                __token = 2168
                try:
                    __zt_tmp = __attrs_4901603408
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4903060048 = _static_4439058528('path', 'album/Title', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'album/Title' (44:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 124289000> -> __condition
                __expression = __cache_4903060048

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Image title')
                else:
                    __content = __cache_4903060048
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</h5>\n          ')

                # <Static value=<ast.Dict object at 0x12428a170> name=None at 124289570> -> __attrs_4901615984
                __attrs_4901615984 = _static_4901609840

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="card-text">')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901611472
                __default_4901611472 = _DEFAULT_MARKER

                # <Value 'album/Description' (45:44)> -> __cache_4901617376
                __token = 2242
                try:
                    __zt_tmp = __attrs_4901615984
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4901617376 = _static_4439058528('path', 'album/Description', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'album/Description' (45:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 12428b340> -> __condition
                __expression = __cache_4901617376

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Description')
                else:
                    __content = __cache_4901617376
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</p>\n          ')

                # <Static value=<ast.Dict object at 0x122ef2860> name=None at 122ef0550> -> __attrs_4881064160
                __attrs_4881064160 = _static_4881066080

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="card-link stretched-link"')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4881060992
                __default_4881060992 = _DEFAULT_MARKER

                # <Substitution 'string:${album/getURL}/view' (46:67)> -> __attr_href
                __token = 2344
                try:
                    __zt_tmp = __attrs_4881064160
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4439058528('string', '${album/getURL}/view', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4881069728
                __default_4881069728 = _DEFAULT_MARKER

                # <Substitution 'album/Description' (46:101)> -> __attr_title
                __token = 2378
                try:
                    __zt_tmp = __attrs_4881064160
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_title = _static_4439058528('path', 'album/Description', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_title is not None):
                    __append((' title="%s"' % __attr_title))
                __append('>')
                __stream_4881062864 = []
                __append_4881062864 = __stream_4881062864.append
                __append_4881062864('View')
                __msgid_4881062864 = __re_whitespace(''.join(__stream_4881062864)).strip()
                if 'label_view':
                    __append(translate('label_view', mapping=None, default=__msgid_4881062864, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</a>\n        </div>\n      </div>\n    </div>\n  ')
                ____index_4903365760 -= 1
                if (____index_4903365760 > 0):
                    __append('')
            if (__backup_album_4902998928 is __marker):
                del econtext['album']
            else:
                econtext['album'] = __backup_album_4902998928
            __append('\n\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903066576
            __attrs_4903066576 = _static_4438893776
            __backup_macroname_4617105856 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x124343eb0> name=None at 124435810> -> __value
            __value = _static_4902370992
            econtext['macroname'] = __value

            # <Value 'context/batch_macros/macros/navigation' (54:24)> -> __macro
            __token = 2525
            try:
                __zt_tmp = __attrs_4903066576
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4439058528('path', 'context/batch_macros/macros/navigation', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __token = 2525
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4617105856 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4617105856
            __append('\n\n  ')
            if (__slot_no_items_in_listing is None):

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4881066848
                __attrs_4881066848 = _static_4438893776
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900364800
                __attrs_4900364800 = _static_4438893776

                # <Value 'python: not images and not albums' (57:22)> -> __condition
                __token = 2647
                try:
                    __zt_tmp = __attrs_4900364800
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('python', ' not images and not albums', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p>')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900365184
                    __default_4900365184 = _DEFAULT_MARKER

                    # <Value 'view/no_items_message' (57:70)> -> __cache_4900364512
                    __token = 2695
                    try:
                        __zt_tmp = __attrs_4900364800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4900364512 = _static_4439058528('path', 'view/no_items_message', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/no_items_message' (57:70)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 12415b850> -> __condition
                    __expression = __cache_4900364512

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n      There are currently no items in this folder.\n    ')
                    else:
                        __content = __cache_4900364512
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</p>')
                __append('\n  ')
            else:
                __slot_no_items_in_listing(__stream, econtext.copy(), rcontext)
            __append('\n  ')
            if (__backup_image_scale_4902161232 is __marker):
                del econtext['image_scale']
            else:
                econtext['image_scale'] = __backup_image_scale_4902161232
            if (__backup_portal_4902172560 is __marker):
                del econtext['portal']
            else:
                econtext['portal'] = __backup_portal_4902172560
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4844384080
            __attrs_4844384080 = _static_4438893776
            __previous_i18n_domain_4844384752 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4516528384 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x12303a650> name=None at 123039300> -> __value
            __value = _static_4882409040
            econtext['macroname'] = __value

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4609077168
                __attrs_4609077168 = _static_4438893776
                __append('\n')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'here/main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_4844384080
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4439058528('path', 'here/main_template/macros/master', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4516528384 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4516528384
            __i18n_domain = __previous_i18n_domain_4844384752
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render_text_field_view': render_text_field_view, 'render_listing': render_listing, 'render': render, }