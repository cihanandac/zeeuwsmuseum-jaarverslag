# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/contenttypes/browser/templates/image.pt'

__tokens = {448: ('python: context.image.contentType', 12, 38), 512: (' context/image/getSiz', 13, 29), 575: ('n context/image/getImageSi', 14, 39), 634: ('MB python: size > 1024*1', 15, 29), 694: ("ion python: str(image_dimension[0])+'x'+str(image_dimension", 16, 31), 788: ('name python: context.image.fil', 17, 29), 858: ("_icon python: 'mimetype-' + conten", 18, 33), 931: ("ad_url python: '{}/@@download/image/{}'.format(context.absolute_url(), fi", 19, 31), 1269: ('context/@@images', 25, 27), 1294: (" python:scale.tag('image', scale='large', css_class='figure-img img-fluid'", 25, 52), 1168: ('string:${context/@@plone_context_state/object_url}/image_view_fullscreen', 24, 30), 1466: ('img_tag', 27, 36), 1394: ('string: Image cannot be displayed', 26, 23), 1545: ('${python:download_url}', 32, 15), 1547: ('python:download_url', 32, 17), 1582: ('python: filename', 32, 52), 1764: ("python:icons.tag(mimetype_icon, tag_class='icon-inline', tag_alt=content_type)", 36, 41), 1949: ('python: content_type', 38, 27), 2068: ("python:icons.tag('aspect-ratio', tag_class='icon-inline', tag_alt='Dimension')", 41, 41), 2263: ('python: dimension', 43, 27), 2376: ("python:icons.tag('file-binary', tag_class='icon-inline', tag_alt='Size')", 46, 41), 2560: ('use_MB', 48, 27), 2568: ('${python:round(size/1024/1024, 1)} MB', 48, 35), 2570: ('python:round(size/1024/1024, 1)', 48, 37), 2642: ('not: use_MB', 49, 27), 2655: ('${python:round(size/1024, 1)} KB', 49, 40), 2657: ('python:round(size/1024, 1)', 49, 42), 2826: ('${python:download_url}', 56, 46), 2828: ('python:download_url', 56, 48), 2929: ('${context/@@plone_context_state/object_url}/image_view_fullscreen', 57, 48), 2931: ('context/@@plone_context_state/object_url', 57, 50), 251: ('context/@@main_template/macros/master', 6, 21), 251: ('context/@@main_template/macros/master', 6, 21)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tal import ErrorInfo as _ErrorInfo
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4495708832 = 'master'
_static_4495929168 = {'class': 'btn btn-primary fullscreen', 'href': '${context/@@plone_context_state/object_url}/image_view_fullscreen', }
_static_4495927392 = {'class': 'btn btn-primary download', 'href': '${python:download_url}', }
_static_4495925616 = {'class': 'section section-actions', }
_static_4495923072 = {'class': 'd-none', }
_static_4495920576 = {'class': 'px-2', }
_static_4495917888 = {'class': 'd-none', }
_static_4495882560 = {'class': 'px-2', }
_static_4495879872 = {'class': 'd-none', }
_static_4495877376 = {'class': 'px-2', }
_static_4495875984 = {'class': 'metadata d-flex justify-content-center text-muted small', }
_static_4495874640 = {'href': '${python:download_url}', }
_static_4495872576 = {'class': 'h5 mb-2', }
_static_4495868832 = {'href': 'string:${context/@@plone_context_state/object_url}/image_view_fullscreen', }
_static_4495211008 = {'class': 'figure', }
_static_4495200304 = {'class': 'section section-main', }
_static_4438741184 = __C2ZContextWrapper
_static_4438540496 = __compile_zt_expr
_static_4438430896 = {}

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

            # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4495560896
            __attrs_4495560896 = _static_4438430896
            __backup_content_type_4495715744 = get('content_type', __marker)

            # <Value 'python: context.image.contentType' (12:38)> -> __value
            __token = 448
            try:
                __zt_tmp = __attrs_4495560896
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('python', ' context.image.contentType', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['content_type'] = __value
            __backup_size_4495715216 = get('size', __marker)

            # <Value 'context/image/getSize' (13:29)> -> __value
            __token = 512
            try:
                __zt_tmp = __attrs_4495560896
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('path', 'context/image/getSize', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['size'] = __value
            __backup_image_dimension_4495715312 = get('image_dimension', __marker)

            # <Value 'context/image/getImageSize' (14:39)> -> __value
            __token = 575
            try:
                __zt_tmp = __attrs_4495560896
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('path', 'context/image/getImageSize', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['image_dimension'] = __value
            __backup_use_MB_4495715408 = get('use_MB', __marker)

            # <Value 'python: size > 1024*1024' (15:29)> -> __value
            __token = 634
            try:
                __zt_tmp = __attrs_4495560896
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('python', ' size > 1024*1024', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['use_MB'] = __value
            __backup_dimension_4495715504 = get('dimension', __marker)

            # <Value "python: str(image_dimension[0])+'x'+str(image_dimension[1])" (16:31)> -> __value
            __token = 694
            try:
                __zt_tmp = __attrs_4495560896
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('python', " str(image_dimension[0])+'x'+str(image_dimension[1])", econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['dimension'] = __value
            __backup_filename_4495715072 = get('filename', __marker)

            # <Value 'python: context.image.filename' (17:29)> -> __value
            __token = 788
            try:
                __zt_tmp = __attrs_4495560896
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('python', ' context.image.filename', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['filename'] = __value
            __backup_mimetype_icon_4495714976 = get('mimetype_icon', __marker)

            # <Value "python: 'mimetype-' + content_type" (18:33)> -> __value
            __token = 858
            try:
                __zt_tmp = __attrs_4495560896
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('python', " 'mimetype-' + content_type", econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['mimetype_icon'] = __value
            __backup_download_url_4495715168 = get('download_url', __marker)

            # <Value "python: '{}/@@download/image/{}'.format(context.absolute_url(), filename)\n                                                     " (19:31)> -> __value
            __token = 931
            try:
                __zt_tmp = __attrs_4495560896
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('python', " '{}/@@download/image/{}'.format(context.absolute_url(), filename)\n                                                     ", econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['download_url'] = __value
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x10bef5030> name=None at 10bef4eb0> -> __attrs_4495200544
            __attrs_4495200544 = _static_4495200304

            # <section ... (0:0)
            # --------------------------------------------------------
            __append('<section class="section section-main">\n    ')

            # <Static value=<ast.Dict object at 0x10bef7a00> name=None at 10bef75e0> -> __attrs_4495210816
            __attrs_4495210816 = _static_4495211008

            # <figure ... (0:0)
            # --------------------------------------------------------
            __append('<figure class="figure">\n      ')
            ____fallback_4440750832 = len(__stream)
            try:

                # <Static value=<ast.Dict object at 0x10bf983a0> name=None at 10bf983d0> -> __attrs_4495869456
                __attrs_4495869456 = _static_4495868832
                __backup_scale_4495714736 = get('scale', __marker)

                # <Value 'context/@@images' (25:27)> -> __value
                __token = 1269
                try:
                    __zt_tmp = __attrs_4495869456
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4438540496('path', 'context/@@images', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                econtext['scale'] = __value
                __backup_img_tag_4495715024 = get('img_tag', __marker)

                # <Value "python:scale.tag('image', scale='large', css_class='figure-img img-fluid')" (25:52)> -> __value
                __token = 1294
                try:
                    __zt_tmp = __attrs_4495869456
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4438540496('python', "scale.tag('image', scale='large', css_class='figure-img img-fluid')", econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                econtext['img_tag'] = __value

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4495868928
                __default_4495868928 = _DEFAULT_MARKER

                # <Substitution 'string:${context/@@plone_context_state/object_url}/image_view_fullscreen' (24:30)> -> __attr_href
                __token = 1168
                try:
                    __zt_tmp = __attrs_4495869456
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4438540496('string', '${context/@@plone_context_state/object_url}/image_view_fullscreen', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append('>\n        ')

                # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4495871904
                __attrs_4495871904 = _static_4438430896

                # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4495871712
                __default_4495871712 = _DEFAULT_MARKER

                # <Value 'img_tag' (27:36)> -> __cache_4495871232
                __token = 1466
                try:
                    __zt_tmp = __attrs_4495871904
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4495871232 = _static_4438540496('path', 'img_tag', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))

                # <BinOp left=<Value 'img_tag' (27:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088d2740> at 10bf98dc0> -> __condition
                __expression = __cache_4495871232

                # <Symbol value=<DEFAULT> at 1088d2740> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <img ... (0:0)
                    # --------------------------------------------------------
                    __append('<img />')
                else:
                    __content = __cache_4495871232
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      </a>')
                if (__backup_img_tag_4495715024 is __marker):
                    del econtext['img_tag']
                else:
                    econtext['img_tag'] = __backup_img_tag_4495715024
                if (__backup_scale_4495714736 is __marker):
                    del econtext['scale']
                else:
                    econtext['scale'] = __backup_scale_4495714736
            except (Exception, ) as __exc:
                econtext['error'] = _ErrorInfo(__exc, __tokens[__token][1:3])
                if (on_error_handler is not None):
                    on_error_handler(__exc)
                del __stream[____fallback_4440750832:]

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a>')

                # <Value 'string: Image cannot be displayed' (26:23)> -> __content
                __token = 1394
                try:
                    __zt_tmp = __attrs_4495210816
                except get('NameError', NameError):
                    __zt_tmp = None

                __content = _static_4438540496('string', ' Image cannot be displayed', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
                __append('</a>')

            __append('\n    </figure>\n\n    ')

            # <Static value=<ast.Dict object at 0x10bf99240> name=None at 10bf99270> -> __attrs_4495872960
            __attrs_4495872960 = _static_4495872576

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="h5 mb-2">\n      ')

            # <Static value=<ast.Dict object at 0x10bf99a50> name=None at 10bf998d0> -> __attrs_4495875264
            __attrs_4495875264 = _static_4495874640

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4495874736
            __default_4495874736 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${python:download_url}' (32:15)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10bf99900> -> __attr_href
            __token = 1545
            __token = 1547
            try:
                __zt_tmp = __attrs_4495875264
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4438540496('python', 'download_url', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = __attr_href
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

            # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4495874016
            __default_4495874016 = _DEFAULT_MARKER

            # <Value 'python: filename' (32:52)> -> __cache_4495873536
            __token = 1582
            try:
                __zt_tmp = __attrs_4495875264
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4495873536 = _static_4438540496('python', ' filename', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))

            # <BinOp left=<Value 'python: filename' (32:52)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088d2740> at 10bf996c0> -> __condition
            __expression = __cache_4495873536

            # <Symbol value=<DEFAULT> at 1088d2740> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('Filename')
            else:
                __content = __cache_4495873536
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</a>\n    </div>\n    ')

            # <Static value=<ast.Dict object at 0x10bf99f90> name=None at 10bf99fc0> -> __attrs_4495876416
            __attrs_4495876416 = _static_4495875984

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="metadata d-flex justify-content-center text-muted small">\n      ')

            # <Static value=<ast.Dict object at 0x10bf9a500> name=None at 10bf9a530> -> __attrs_4495877760
            __attrs_4495877760 = _static_4495877376

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="px-2">\n        ')

            # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4495879200
            __attrs_4495879200 = _static_4438430896

            # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4495879008
            __default_4495879008 = _DEFAULT_MARKER

            # <Value "python:icons.tag(mimetype_icon, tag_class='icon-inline', tag_alt=content_type)" (36:41)> -> __cache_4495878528
            __token = 1764
            try:
                __zt_tmp = __attrs_4495879200
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4495878528 = _static_4438540496('python', "icons.tag(mimetype_icon, tag_class='icon-inline', tag_alt=content_type)", econtext=econtext)(_static_4438741184(econtext, __zt_tmp))

            # <BinOp left=<Value "python:icons.tag(mimetype_icon, tag_class='icon-inline', tag_alt=content_type)" (36:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088d2740> at 10bf9aa40> -> __condition
            __expression = __cache_4495878528

            # <Symbol value=<DEFAULT> at 1088d2740> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4495878528
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x10bf9aec0> name=None at 10bf9aef0> -> __attrs_4495880256
            __attrs_4495880256 = _static_4495879872

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span class="d-none">')
            __stream_4495879296 = []
            __append_4495879296 = __stream_4495879296.append
            __append_4495879296('Type')
            __msgid_4495879296 = __re_whitespace(''.join(__stream_4495879296)).strip()
            if 'image_kind_label':
                __append(translate('image_kind_label', mapping=None, default=__msgid_4495879296, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span>\n        ')

            # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4495881792
            __attrs_4495881792 = _static_4438430896

            # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4495881600
            __default_4495881600 = _DEFAULT_MARKER

            # <Value 'python: content_type' (38:27)> -> __cache_4495881120
            __token = 1949
            try:
                __zt_tmp = __attrs_4495881792
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4495881120 = _static_4438540496('python', ' content_type', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))

            # <BinOp left=<Value 'python: content_type' (38:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088d2740> at 10bf9b460> -> __condition
            __expression = __cache_4495881120

            # <Symbol value=<DEFAULT> at 1088d2740> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>image/jpeg</span>')
            else:
                __content = __cache_4495881120
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('\n      </div>\n      ')

            # <Static value=<ast.Dict object at 0x10bf9b940> name=None at 10bf9b970> -> __attrs_4495882944
            __attrs_4495882944 = _static_4495882560

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="px-2">\n        ')

            # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4495917216
            __attrs_4495917216 = _static_4438430896

            # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4495884192
            __default_4495884192 = _DEFAULT_MARKER

            # <Value "python:icons.tag('aspect-ratio', tag_class='icon-inline', tag_alt='Dimension')" (41:41)> -> __cache_4495883712
            __token = 2068
            try:
                __zt_tmp = __attrs_4495917216
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4495883712 = _static_4438540496('python', "icons.tag('aspect-ratio', tag_class='icon-inline', tag_alt='Dimension')", econtext=econtext)(_static_4438741184(econtext, __zt_tmp))

            # <BinOp left=<Value "python:icons.tag('aspect-ratio', tag_class='icon-inline', tag_alt='Dimension')" (41:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088d2740> at 10bf9be80> -> __condition
            __expression = __cache_4495883712

            # <Symbol value=<DEFAULT> at 1088d2740> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4495883712
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x10bfa4340> name=None at 10bfa4370> -> __attrs_4495918272
            __attrs_4495918272 = _static_4495917888

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span class="d-none">')
            __stream_4495917312 = []
            __append_4495917312 = __stream_4495917312.append
            __append_4495917312('Dimension')
            __msgid_4495917312 = __re_whitespace(''.join(__stream_4495917312)).strip()
            if 'image_dimension_label':
                __append(translate('image_dimension_label', mapping=None, default=__msgid_4495917312, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span>\n        ')

            # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4495919808
            __attrs_4495919808 = _static_4438430896

            # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4495919616
            __default_4495919616 = _DEFAULT_MARKER

            # <Value 'python: dimension' (43:27)> -> __cache_4495919136
            __token = 2263
            try:
                __zt_tmp = __attrs_4495919808
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4495919136 = _static_4438540496('python', ' dimension', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))

            # <BinOp left=<Value 'python: dimension' (43:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088d2740> at 10bfa48e0> -> __condition
            __expression = __cache_4495919136

            # <Symbol value=<DEFAULT> at 1088d2740> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>400x300</span>')
            else:
                __content = __cache_4495919136
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('\n      </div>\n      ')

            # <Static value=<ast.Dict object at 0x10bfa4dc0> name=None at 10bfa4df0> -> __attrs_4495920960
            __attrs_4495920960 = _static_4495920576

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="px-2">\n        ')

            # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4495922400
            __attrs_4495922400 = _static_4438430896

            # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4495922208
            __default_4495922208 = _DEFAULT_MARKER

            # <Value "python:icons.tag('file-binary', tag_class='icon-inline', tag_alt='Size')" (46:41)> -> __cache_4495921728
            __token = 2376
            try:
                __zt_tmp = __attrs_4495922400
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4495921728 = _static_4438540496('python', "icons.tag('file-binary', tag_class='icon-inline', tag_alt='Size')", econtext=econtext)(_static_4438741184(econtext, __zt_tmp))

            # <BinOp left=<Value "python:icons.tag('file-binary', tag_class='icon-inline', tag_alt='Size')" (46:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088d2740> at 10bfa5300> -> __condition
            __expression = __cache_4495921728

            # <Symbol value=<DEFAULT> at 1088d2740> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4495921728
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x10bfa5780> name=None at 10bfa57b0> -> __attrs_4495923456
            __attrs_4495923456 = _static_4495923072

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span class="d-none">')
            __stream_4495922496 = []
            __append_4495922496 = __stream_4495922496.append
            __append_4495922496('File size')
            __msgid_4495922496 = __re_whitespace(''.join(__stream_4495922496)).strip()
            if 'image_size_label':
                __append(translate('image_size_label', mapping=None, default=__msgid_4495922496, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span>\n        ')

            # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4495924224
            __attrs_4495924224 = _static_4438430896

            # <Value 'use_MB' (48:27)> -> __condition
            __token = 2560
            try:
                __zt_tmp = __attrs_4495924224
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4438540496('path', 'use_MB', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            if __condition:

                # <Interpolation value=<Substitution '${python:round(size/1024/1024, 1)} MB' (48:35)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10bfa5e10> -> __content_4340137456
                __token = 2568
                __token = 2570
                try:
                    __zt_tmp = __attrs_4495924224
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_4340137456 = _static_4438540496('python', 'round(size/1024/1024, 1)', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                __content_4340137456 = __quote(__content_4340137456, '\x00', '&#0;', None, None)
                __content_4340137456 = ('%s%s' % ((__content_4340137456 if (__content_4340137456 is not None) else ''), ' MB', ))
                if (__content_4340137456 is None):
                    pass
                else:
                    if (__content_4340137456 is None):
                        __content_4340137456 = None
                    else:
                        __tt = type(__content_4340137456)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_4340137456 = str(__content_4340137456)
                        else:
                            if (__tt is bytes):
                                __content_4340137456 = decode(__content_4340137456)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_4340137456 = __content_4340137456.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_4340137456)
                                        __content_4340137456 = (str(__content_4340137456) if (__content_4340137456 is __converted) else __converted)
                                    else:
                                        __content_4340137456 = __content_4340137456()
                if (__content_4340137456 is not None):
                    __append(__content_4340137456)
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4495924992
            __attrs_4495924992 = _static_4438430896

            # <Value 'not: use_MB' (49:27)> -> __condition
            __token = 2642
            try:
                __zt_tmp = __attrs_4495924992
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4438540496('not', ' use_MB', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            if __condition:

                # <Interpolation value=<Substitution '${python:round(size/1024, 1)} KB' (49:40)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10bfa6110> -> __content_4340137456
                __token = 2655
                __token = 2657
                try:
                    __zt_tmp = __attrs_4495924992
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_4340137456 = _static_4438540496('python', 'round(size/1024, 1)', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                __content_4340137456 = __quote(__content_4340137456, '\x00', '&#0;', None, None)
                __content_4340137456 = ('%s%s' % ((__content_4340137456 if (__content_4340137456 is not None) else ''), ' KB', ))
                if (__content_4340137456 is None):
                    pass
                else:
                    if (__content_4340137456 is None):
                        __content_4340137456 = None
                    else:
                        __tt = type(__content_4340137456)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_4340137456 = str(__content_4340137456)
                        else:
                            if (__tt is bytes):
                                __content_4340137456 = decode(__content_4340137456)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_4340137456 = __content_4340137456.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_4340137456)
                                        __content_4340137456 = (str(__content_4340137456) if (__content_4340137456 is __converted) else __converted)
                                    else:
                                        __content_4340137456 = __content_4340137456()
                if (__content_4340137456 is not None):
                    __append(__content_4340137456)
            __append('\n      </div>\n    </div>\n\n  </section>\n\n  ')

            # <Static value=<ast.Dict object at 0x10bfa6170> name=None at 10bfa4fa0> -> __attrs_4495925952
            __attrs_4495925952 = _static_4495925616

            # <section ... (0:0)
            # --------------------------------------------------------
            __append('<section class="section section-actions">\n    ')

            # <Static value=<ast.Dict object at 0x10bfa6860> name=None at 10bfa6890> -> __attrs_4495927920
            __attrs_4495927920 = _static_4495927392

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="btn btn-primary download"')

            # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4495926672
            __default_4495926672 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${python:download_url}' (56:46)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10bfa6650> -> __attr_href
            __token = 2826
            __token = 2828
            try:
                __zt_tmp = __attrs_4495927920
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4438540496('python', 'download_url', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = __attr_href
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
            __stream_4495926528 = []
            __append_4495926528 = __stream_4495926528.append
            __append_4495926528('Download')
            __msgid_4495926528 = __re_whitespace(''.join(__stream_4495926528)).strip()
            if __msgid_4495926528:
                __append(translate(__msgid_4495926528, mapping=None, default=__msgid_4495926528, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n    ')

            # <Static value=<ast.Dict object at 0x10bfa6f50> name=None at 10bfa6f80> -> __attrs_4495929696
            __attrs_4495929696 = _static_4495929168

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="btn btn-primary fullscreen"')

            # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4495928448
            __default_4495928448 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${context/@@plone_context_state/object_url}/image_view_fullscreen' (57:48)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10bfa6d40> -> __attr_href
            __token = 2929
            __token = 2931
            try:
                __zt_tmp = __attrs_4495929696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4438540496('path', 'context/@@plone_context_state/object_url', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = ('%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/image_view_fullscreen', ))
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

            # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4495930656
            __attrs_4495930656 = _static_4438430896

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span>')
            __stream_4495930176 = []
            __append_4495930176 = __stream_4495930176.append
            __append_4495930176('View full-size image')
            __msgid_4495930176 = __re_whitespace(''.join(__stream_4495930176)).strip()
            if 'label_click_to_view_full_image':
                __append(translate('label_click_to_view_full_image', mapping=None, default=__msgid_4495930176, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span></a>\n  </section>\n\n\n')
            if (__backup_download_url_4495715168 is __marker):
                del econtext['download_url']
            else:
                econtext['download_url'] = __backup_download_url_4495715168
            if (__backup_mimetype_icon_4495714976 is __marker):
                del econtext['mimetype_icon']
            else:
                econtext['mimetype_icon'] = __backup_mimetype_icon_4495714976
            if (__backup_filename_4495715072 is __marker):
                del econtext['filename']
            else:
                econtext['filename'] = __backup_filename_4495715072
            if (__backup_dimension_4495715504 is __marker):
                del econtext['dimension']
            else:
                econtext['dimension'] = __backup_dimension_4495715504
            if (__backup_use_MB_4495715408 is __marker):
                del econtext['use_MB']
            else:
                econtext['use_MB'] = __backup_use_MB_4495715408
            if (__backup_image_dimension_4495715312 is __marker):
                del econtext['image_dimension']
            else:
                econtext['image_dimension'] = __backup_image_dimension_4495715312
            if (__backup_size_4495715216 is __marker):
                del econtext['size']
            else:
                econtext['size'] = __backup_size_4495715216
            if (__backup_content_type_4495715744 is __marker):
                del econtext['content_type']
            else:
                econtext['content_type'] = __backup_content_type_4495715744
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

            # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4495566464
            __attrs_4495566464 = _static_4438430896
            __previous_i18n_domain_4495562048 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4485243648 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x10bf712a0> name=None at 10bf71630> -> __value
            __value = _static_4495708832
            econtext['macroname'] = __value

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4495570016
                __attrs_4495570016 = _static_4438430896
                __append('\n')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/@@main_template/macros/master' (6:21)> -> __macro
            __token = 251
            try:
                __zt_tmp = __attrs_4495566464
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4438540496('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            __token = 251
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4485243648 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4485243648
            __i18n_domain = __previous_i18n_domain_4495562048
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render': render, }