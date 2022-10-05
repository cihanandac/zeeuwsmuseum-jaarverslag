# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/nextprevious/nextprevious.pt'

__tokens = {57: ('view/enabled|nothing', 2, 25), 110: (' view/isViewTemplate|nothin', 3, 31), 160: ('python:enabled and isViewTemplate', 4, 20), 254: ('view/site_url', 7, 32), 350: ('view/next', 10, 26), 390: (' view/previou', 11, 29), 430: ('python:previous is not None or next is not None', 12, 24), 576: ('previous', 14, 95), 721: ('previous/url', 17, 35), 925: ('previous/title', 21, 55), 1069: ('next', 25, 89), 1188: ('next/url', 27, 35), 1340: ('next/title', 30, 55)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4982439888 = {'class': 'arrow', }
_static_4982434224 = {'class': 'label', }
_static_4982437776 = {'class': 'btn btn-sm btn-outline-secondary align-self-end next', 'title': 'Go to next item', 'href': 'next/url', }
_static_4982025872 = {'class': 'label', }
_static_4982017664 = {'class': 'arrow', }
_static_4982027696 = {'class': 'btn btn-sm btn-outline-secondary align-self-start previous', 'title': 'Go to previous item', 'href': 'previous/url', }
_static_4982027024 = {'class': 'pagination justify-content-between', }
_static_4753720080 = {}
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4982021168 = {'id': 'section-next-prev', }

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

            # <Static value=<ast.Dict object at 0x128f39c30> name=None at 128f3af20> -> __attrs_4982020400
            __attrs_4982020400 = _static_4982021168
            __backup_enabled_4977853056 = get('enabled', __marker)

            # <Value 'view/enabled|nothing' (2:25)> -> __value
            __token = 57
            try:
                __zt_tmp = __attrs_4982020400
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/enabled|nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['enabled'] = __value
            __backup_isViewTemplate_4974675232 = get('isViewTemplate', __marker)

            # <Value 'view/isViewTemplate|nothing' (3:31)> -> __value
            __token = 110
            try:
                __zt_tmp = __attrs_4982020400
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'view/isViewTemplate|nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['isViewTemplate'] = __value

            # <Value 'python:enabled and isViewTemplate' (4:20)> -> __condition
            __token = 160
            try:
                __zt_tmp = __attrs_4982020400
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('python', 'enabled and isViewTemplate', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4982029424 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-next-prev">\n\n  ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982016224
                __attrs_4982016224 = _static_4753720080
                __backup_portal_url_4982043312 = get('portal_url', __marker)

                # <Value 'view/site_url' (7:32)> -> __value
                __token = 254
                try:
                    __zt_tmp = __attrs_4982016224
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('path', 'view/site_url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['portal_url'] = __value
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x128f3b310> name=None at 128f3bd00> -> __attrs_4982019920
                __attrs_4982019920 = _static_4982027024
                __backup_next_4982027936 = get('next', __marker)

                # <Value 'view/next' (10:26)> -> __value
                __token = 350
                try:
                    __zt_tmp = __attrs_4982019920
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('path', 'view/next', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['next'] = __value
                __backup_previous_4982028320 = get('previous', __marker)

                # <Value 'view/previous' (11:29)> -> __value
                __token = 390
                try:
                    __zt_tmp = __attrs_4982019920
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('path', 'view/previous', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['previous'] = __value

                # <Value 'python:previous is not None or next is not None' (12:24)> -> __condition
                __token = 430
                try:
                    __zt_tmp = __attrs_4982019920
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4754050160('python', 'previous is not None or next is not None', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                if __condition:

                    # <nav ... (0:0)
                    # --------------------------------------------------------
                    __append('<nav class="pagination justify-content-between">\n\n          ')

                    # <Static value=<ast.Dict object at 0x128f3b5b0> name=None at 128f3b130> -> __attrs_4982022272
                    __attrs_4982022272 = _static_4982027696

                    # <Value 'previous' (14:95)> -> __condition
                    __token = 576
                    try:
                        __zt_tmp = __attrs_4982022272
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4754050160('path', 'previous', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="btn btn-sm btn-outline-secondary align-self-start previous"')

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982015744
                        __default_4982015744 = _DEFAULT_MARKER

                        # <Translate msgid='title_previous_item' node=<ast.Constant object at 0x128f3b6d0> at 128f39090> -> __attr_title
                        __attr_title = 'Go to previous item'
                        __attr_title = translate('title_previous_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982029280
                        __default_4982029280 = _DEFAULT_MARKER

                        # <Substitution 'previous/url' (17:35)> -> __attr_href
                        __token = 721
                        try:
                            __zt_tmp = __attrs_4982022272
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4754050160('path', 'previous/url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>\n            ')

                        # <Static value=<ast.Dict object at 0x128f38e80> name=None at 128f38af0> -> __attrs_4982018432
                        __attrs_4982018432 = _static_4982017664

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="arrow"></span>\n            ')

                        # <Static value=<ast.Dict object at 0x128f3ae90> name=None at 128f380a0> -> __attrs_4982020352
                        __attrs_4982020352 = _static_4982025872

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="label">')
                        __stream_4982768576_itemtitle = ''
                        __stream_4982023904 = []
                        __append_4982023904 = __stream_4982023904.append
                        __append_4982023904('\n              Previous:\n              ')
                        __stream_4982768576_itemtitle = []
                        __append_4982768576_itemtitle = __stream_4982768576_itemtitle.append

                        # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982438880
                        __attrs_4982438880 = _static_4753720080

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982438400
                        __default_4982438400 = _DEFAULT_MARKER

                        # <Value 'previous/title' (21:55)> -> __cache_4982018816
                        __token = 925
                        try:
                            __zt_tmp = __attrs_4982438880
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4982018816 = _static_4754050160('path', 'previous/title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                        # <BinOp left=<Value 'previous/title' (21:55)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f38940> -> __condition
                        __expression = __cache_4982018816

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append_4982768576_itemtitle('<span />')
                        else:
                            __content = __cache_4982018816
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_4982768576_itemtitle(__content)
                        __append_4982023904('${itemtitle}')
                        __stream_4982768576_itemtitle = ''.join(__stream_4982768576_itemtitle)
                        __append_4982023904('\n            ')
                        __msgid_4982023904 = __re_whitespace(''.join(__stream_4982023904)).strip()
                        if 'label_previous_item':
                            __append(translate('label_previous_item', mapping={'itemtitle': __stream_4982768576_itemtitle, }, default=__msgid_4982023904, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n          </a>')
                    __append('\n\n          ')

                    # <Static value=<ast.Dict object at 0x128f9f790> name=None at 128f9cf70> -> __attrs_4982430384
                    __attrs_4982430384 = _static_4982437776

                    # <Value 'next' (25:89)> -> __condition
                    __token = 1069
                    try:
                        __zt_tmp = __attrs_4982430384
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4754050160('path', 'next', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="btn btn-sm btn-outline-secondary align-self-end next"')

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982433216
                        __default_4982433216 = _DEFAULT_MARKER

                        # <Translate msgid='title_next_item' node=<ast.Constant object at 0x128f9d150> at 128f9dae0> -> __attr_title
                        __attr_title = 'Go to next item'
                        __attr_title = translate('title_next_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982434512
                        __default_4982434512 = _DEFAULT_MARKER

                        # <Substitution 'next/url' (27:35)> -> __attr_href
                        __token = 1188
                        try:
                            __zt_tmp = __attrs_4982430384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4754050160('path', 'next/url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>\n            ')

                        # <Static value=<ast.Dict object at 0x128f9e9b0> name=None at 128f9df90> -> __attrs_4982425488
                        __attrs_4982425488 = _static_4982434224

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="label">')
                        __stream_4982769024_itemtitle = ''
                        __stream_4982425344 = []
                        __append_4982425344 = __stream_4982425344.append
                        __append_4982425344('\n              Next:\n              ')
                        __stream_4982769024_itemtitle = []
                        __append_4982769024_itemtitle = __stream_4982769024_itemtitle.append

                        # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982437584
                        __attrs_4982437584 = _static_4753720080

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982429376
                        __default_4982429376 = _DEFAULT_MARKER

                        # <Value 'next/title' (30:55)> -> __cache_4982425152
                        __token = 1340
                        try:
                            __zt_tmp = __attrs_4982437584
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4982425152 = _static_4754050160('path', 'next/title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                        # <BinOp left=<Value 'next/title' (30:55)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128f9c5e0> -> __condition
                        __expression = __cache_4982425152

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append_4982769024_itemtitle('<span />')
                        else:
                            __content = __cache_4982425152
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_4982769024_itemtitle(__content)
                        __append_4982425344('${itemtitle}')
                        __stream_4982769024_itemtitle = ''.join(__stream_4982769024_itemtitle)
                        __append_4982425344('\n            ')
                        __msgid_4982425344 = __re_whitespace(''.join(__stream_4982425344)).strip()
                        if 'label_next_item':
                            __append(translate('label_next_item', mapping={'itemtitle': __stream_4982769024_itemtitle, }, default=__msgid_4982425344, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n            ')

                        # <Static value=<ast.Dict object at 0x128f9ffd0> name=None at 128f9ffa0> -> __attrs_4982432208
                        __attrs_4982432208 = _static_4982439888

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="arrow"></span>\n          </a>')
                    __append('\n\n\n    </nav>')
                if (__backup_previous_4982028320 is __marker):
                    del econtext['previous']
                else:
                    econtext['previous'] = __backup_previous_4982028320
                if (__backup_next_4982027936 is __marker):
                    del econtext['next']
                else:
                    econtext['next'] = __backup_next_4982027936
                __append('\n\n  ')
                if (__backup_portal_url_4982043312 is __marker):
                    del econtext['portal_url']
                else:
                    econtext['portal_url'] = __backup_portal_url_4982043312
                __append('\n\n</section>')
                __i18n_domain = __previous_i18n_domain_4982029424
            if (__backup_isViewTemplate_4974675232 is __marker):
                del econtext['isViewTemplate']
            else:
                econtext['isViewTemplate'] = __backup_isViewTemplate_4974675232
            if (__backup_enabled_4977853056 is __marker):
                del econtext['enabled']
            else:
                econtext['enabled'] = __backup_enabled_4977853056
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }