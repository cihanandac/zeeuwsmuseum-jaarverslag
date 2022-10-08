# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/content/browser/contents/templates/rename.pt'

__tokens = {}

from sys import exc_info as _exc_info

_static_4472196112 = {'class': 'thumb-thumb', 'src': '<%= item.getURL %>/@@images/image/thumb', }
_static_4476345488 = {'class': 'form-control', 'name': 'newid_<%= index %>', 'value': '<%= item.id %>', }
_static_4476350624 = {'class': 'form-label', }
_static_4476351872 = {'class': 'mb-2', }
_static_4476943520 = {'class': 'form-control', 'name': 'newtitle_<%= index %>', 'value': '<%= item.Title %>', }
_static_4476931616 = {'class': 'form-label', }
_static_4476935120 = {'class': 'mb-2', }
_static_4476937376 = {'name': 'UID_<%= index %>', 'type': 'hidden', 'value': '<%- item.UID %>', }
_static_4476936752 = {'class': 'mb-3 pb-3 <% if (items.length > 1){%>border-bottom<% } %>', }
_static_4476939488 = {'class': 'itemstoremove row row-cols-1', }

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

            # <Static value=<ast.Dict object at 0x10ad8ace0> name=None at 10ad8ad10> -> __attrs_4476943712
            __attrs_4476943712 = _static_4476939488
            __previous_i18n_domain_4476936848 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="itemstoremove row row-cols-1">\n<% _.each(items, function(item, index) { %>\n  ')

            # <Static value=<ast.Dict object at 0x10ad8a230> name=None at 10ad88760> -> __attrs_4476933680
            __attrs_4476933680 = _static_4476936752

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-3 pb-3 <% if (items.length > 1){%>border-bottom<% } %>">\n    ')

            # <Static value=<ast.Dict object at 0x10ad8a4a0> name=None at 10ad892a0> -> __attrs_4476934448
            __attrs_4476934448 = _static_4476937376

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input name="UID_<%= index %>" type="hidden" value="<%- item.UID %>" />\n\n    ')

            # <Static value=<ast.Dict object at 0x10ad89bd0> name=None at 10ad89000> -> __attrs_4476934592
            __attrs_4476934592 = _static_4476935120

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n      ')

            # <Static value=<ast.Dict object at 0x10ad88e20> name=None at 10ad88280> -> __attrs_4476943376
            __attrs_4476943376 = _static_4476931616

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4476932720 = []
            __append_4476932720 = __stream_4476932720.append
            __append_4476932720('Title')
            __msgid_4476932720 = __re_whitespace(''.join(__stream_4476932720)).strip()
            if 'label_title':
                __append(translate('label_title', mapping=None, default=__msgid_4476932720, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n      ')

            # <Static value=<ast.Dict object at 0x10ad8bca0> name=None at 10ad89e70> -> __attrs_4476268656
            __attrs_4476268656 = _static_4476943520

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-control" name="newtitle_<%= index %>" value="<%= item.Title %>" />\n    </div>\n\n    ')

            # <Static value=<ast.Dict object at 0x10acfb580> name=None at 10acfb010> -> __attrs_4476351632
            __attrs_4476351632 = _static_4476351872

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n      ')

            # <Static value=<ast.Dict object at 0x10acfb0a0> name=None at 10acfb040> -> __attrs_4476352256
            __attrs_4476352256 = _static_4476350624

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4476347936 = []
            __append_4476347936 = __stream_4476347936.append
            __append_4476347936('Short name')
            __msgid_4476347936 = __re_whitespace(''.join(__stream_4476347936)).strip()
            if 'label_short_name':
                __append(translate('label_short_name', mapping=None, default=__msgid_4476347936, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n      ')

            # <Static value=<ast.Dict object at 0x10acf9c90> name=None at 10acfbfd0> -> __attrs_4476343760
            __attrs_4476343760 = _static_4476345488

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-control" name="newid_<%= index %>" value="<%= item.id %>" />\n    </div>\n\n    <% if(item.getIcon ){ %>')

            # <Static value=<ast.Dict object at 0x10a904c10> name=None at 10a905ff0> -> __attrs_4477076864
            __attrs_4477076864 = _static_4472196112

            # <img ... (0:0)
            # --------------------------------------------------------
            __append('<img class="thumb-thumb" src="<%= item.getURL %>/@@images/image/thumb"><% } %>\n\n  </div>\n<% }) %>\n</div>')
            __i18n_domain = __previous_i18n_domain_4476936848
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }