# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/contenttypes/behaviors/leadimage.pt'

__tokens = {56: ('view/available', 2, 24), 129: ('context/@@images', 3, 56), 182: ("python: images.tag('image', scale='large', css_class='figure-img img-fluid')", 4, 34), 319: ("python: getattr(context, 'image_caption', None)", 5, 56), 381: ('python: context.image_caption', 5, 118)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4881435424 = {'class': 'figure-caption', }
_static_4438893776 = {}
_static_4882750080 = {'class': 'newsImageContainer', }
_static_4439051040 = __C2ZContextWrapper
_static_4439058528 = __compile_zt_expr
_static_4882754448 = {'id': 'section-leadimage', }

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

            # <Static value=<ast.Dict object at 0x12308eb90> name=None at 12308eb30> -> __attrs_4882743456
            __attrs_4882743456 = _static_4882754448

            # <Value 'view/available' (2:24)> -> __condition
            __token = 56
            try:
                __zt_tmp = __attrs_4882743456
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4439058528('path', 'view/available', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            if __condition:

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-leadimage">\n  ')

                # <Static value=<ast.Dict object at 0x12308da80> name=None at 12308da20> -> __attrs_4881445408
                __attrs_4881445408 = _static_4882750080
                __backup_images_4851666704 = get('images', __marker)

                # <Value 'context/@@images' (3:56)> -> __value
                __token = 129
                try:
                    __zt_tmp = __attrs_4881445408
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'context/@@images', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['images'] = __value

                # <figure ... (0:0)
                # --------------------------------------------------------
                __append('<figure class="newsImageContainer">\n      ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4881434560
                __attrs_4881434560 = _static_4438893776

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4881432736
                __default_4881432736 = _DEFAULT_MARKER

                # <Value "python: images.tag('image', scale='large', css_class='figure-img img-fluid')" (4:34)> -> __cache_4881444352
                __token = 182
                try:
                    __zt_tmp = __attrs_4881434560
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4881444352 = _static_4439058528('python', " images.tag('image', scale='large', css_class='figure-img img-fluid')", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value "python: images.tag('image', scale='large', css_class='figure-img img-fluid')" (4:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 122f4e6e0> -> __condition
                __expression = __cache_4881444352

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <img ... (0:0)
                    # --------------------------------------------------------
                    __append('<img />')
                else:
                    __content = __cache_4881444352
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x122f4cb20> name=None at 122f4db70> -> __attrs_4881447088
                __attrs_4881447088 = _static_4881435424

                # <Value "python: getattr(context, 'image_caption', None)" (5:56)> -> __condition
                __token = 319
                try:
                    __zt_tmp = __attrs_4881447088
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('python', " getattr(context, 'image_caption', None)", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:

                    # <figcaption ... (0:0)
                    # --------------------------------------------------------
                    __append('<figcaption class="figure-caption">')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4881446800
                    __default_4881446800 = _DEFAULT_MARKER

                    # <Value 'python: context.image_caption' (5:118)> -> __cache_4881445168
                    __token = 381
                    try:
                        __zt_tmp = __attrs_4881447088
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4881445168 = _static_4439058528('python', ' context.image_caption', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value 'python: context.image_caption' (5:118)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 122f4dd50> -> __condition
                    __expression = __cache_4881445168

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        Image caption\n      ')
                    else:
                        __content = __cache_4881445168
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</figcaption>')
                __append('\n  </figure>')
                if (__backup_images_4851666704 is __marker):
                    del econtext['images']
                else:
                    econtext['images'] = __backup_images_4851666704
                __append('\n</section>')
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }