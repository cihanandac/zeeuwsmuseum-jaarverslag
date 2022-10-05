# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/viewlets/social_tags_body.pt'

__tokens = {128: ('view/body_tags', 3, 24), 177: ('tag/itemprop|nothing', 4, 33), 220: ('tag/content|nothing', 5, 21)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4982502640 = {'itemprop': 'tag/itemprop|nothing', }
_static_4982497984 = {'id': 'social-tags-body', 'style': 'display: none', 'itemscope': '', 'itemtype': 'http://schema.org/WebPage', }

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

            # <Static value=<ast.Dict object at 0x128fae2c0> name=None at 128fad8a0> -> __attrs_4982495632
            __attrs_4982495632 = _static_4982497984

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span id="social-tags-body" style="display: none" itemscope itemtype="http://schema.org/WebPage">\n  ')

            # <Static value=<ast.Dict object at 0x128faf4f0> name=None at 128fad960> -> __attrs_4982499232
            __attrs_4982499232 = _static_4982502640
            __backup_tag_4975057536 = get('tag', __marker)

            # <Value 'view/body_tags' (3:24)> -> __iterator
            __token = 128
            try:
                __zt_tmp = __attrs_4982499232
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4754050160('path', 'view/body_tags', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            (__iterator, ____index_4982493856, ) = getname('repeat')('tag', __iterator)
            econtext['tag'] = None
            for __item in __iterator:
                econtext['tag'] = __item

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span')

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982489584
                __default_4982489584 = _DEFAULT_MARKER

                # <Substitution 'tag/itemprop|nothing' (4:33)> -> __attr_itemprop
                __token = 177
                try:
                    __zt_tmp = __attrs_4982499232
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_itemprop = _static_4754050160('path', 'tag/itemprop|nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                __attr_itemprop = __quote(__attr_itemprop, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_itemprop is not None):
                    __append((' itemprop="%s"' % __attr_itemprop))
                __append('>')

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982505376
                __default_4982505376 = _DEFAULT_MARKER

                # <Value 'tag/content|nothing' (5:21)> -> __cache_4982504992
                __token = 220
                try:
                    __zt_tmp = __attrs_4982499232
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4982504992 = _static_4754050160('path', 'tag/content|nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                # <BinOp left=<Value 'tag/content|nothing' (5:21)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128faf610> -> __condition
                __expression = __cache_4982504992

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4982504992
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</span>')
                ____index_4982493856 -= 1
                if (____index_4982493856 > 0):
                    __append('\n  ')
            if (__backup_tag_4975057536 is __marker):
                del econtext['tag']
            else:
                econtext['tag'] = __backup_tag_4975057536
            __append('\n</span>\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }