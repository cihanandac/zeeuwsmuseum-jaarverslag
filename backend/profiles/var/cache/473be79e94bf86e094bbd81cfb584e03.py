# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/content/browser/contents/templates/tags.pt'

__tokens = {721: ("multiple: true; vocabularyUrl: ${python: options['vocabulary_url']}", 21, 29), 754: ("python: options['vocabulary_url']", 21, 62)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4417565216 = __C2ZContextWrapper
_static_4417553984 = __compile_zt_expr
_static_4477226864 = {'class': 'toadd pat-select2', 'name': 'toadd', 'style': 'width:100%', 'data-pat-select2': "multiple: true; vocabularyUrl: ${python: options['vocabulary_url']}", }
_static_4477228448 = {'class': 'form-label', }
_static_4477231712 = {'value': '<%= tag %>', }
_static_4477232576 = {'multiple': '', 'class': 'toremove pat-select2', 'name': 'toremove', 'style': 'width:100%', }
_static_4477235216 = {'class': 'form-label', }
_static_4477236656 = {'class': 'mb-2', }
_static_4418309904 = {}

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

            # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4477237712
            __attrs_4477237712 = _static_4418309904
            __previous_i18n_domain_4477237568 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div>\n  ')

            # <Static value=<ast.Dict object at 0x10add35b0> name=None at 10add3580> -> __attrs_4477236272
            __attrs_4477236272 = _static_4477236656

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x10add3010> name=None at 10add2fe0> -> __attrs_4477234832
            __attrs_4477234832 = _static_4477235216

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4477235696 = []
            __append_4477235696 = __stream_4477235696.append
            __append_4477235696('Tags to remove')
            __msgid_4477235696 = __re_whitespace(''.join(__stream_4477235696)).strip()
            if 'tags_to_remove':
                __append(translate('tags_to_remove', mapping=None, default=__msgid_4477235696, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x10add25c0> name=None at 10add2590> -> __attrs_4477233920
            __attrs_4477233920 = _static_4477232576

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select multiple class="toremove pat-select2" name="toremove" style="width:100%">\n      <% var tags = [];\n      _.each(items, function(item, index) {\n        _.each(item.Subject, function(tag) {\n          if(tags.indexOf(tag) === -1){\n            tags.push(tag);\n            %>')

            # <Static value=<ast.Dict object at 0x10add2260> name=None at 10add2230> -> __attrs_4477231328
            __attrs_4477231328 = _static_4477231712

            # <option ... (0:0)
            # --------------------------------------------------------
            __append('<option value="<%= tag %>"><%= tag %></option>\n            <%\n          }\n        });\n      }); %>\n    </select>\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4477223840
            __attrs_4477223840 = _static_4418309904

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div>\n    ')

            # <Static value=<ast.Dict object at 0x10add15a0> name=None at 10add1510> -> __attrs_4477229120
            __attrs_4477229120 = _static_4477228448

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4477224512 = []
            __append_4477224512 = __stream_4477224512.append
            __append_4477224512('Tags to add')
            __msgid_4477224512 = __re_whitespace(''.join(__stream_4477224512)).strip()
            if 'tags_to_add':
                __append(translate('tags_to_add', mapping=None, default=__msgid_4477224512, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x10add0f70> name=None at 10add0760> -> __attrs_4477229840
            __attrs_4477229840 = _static_4477226864

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="toadd pat-select2" name="toadd" style="width:100%"')

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4477230176
            __default_4477230176 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "multiple: true; vocabularyUrl: ${python: options['vocabulary_url']}" (21:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10add0850> -> __attr_data_pat_select2
            __token = 721
            __token = 754
            try:
                __zt_tmp = __attrs_4477229840
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_pat_select2 = _static_4417553984('python', " options['vocabulary_url']", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_data_pat_select2 = __quote(__attr_data_pat_select2, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_data_pat_select2 = ('%s%s' % ('multiple: true; vocabularyUrl: ', (__attr_data_pat_select2 if (__attr_data_pat_select2 is not None) else ''), ))
            if (__attr_data_pat_select2 is None):
                pass
            else:
                if (__attr_data_pat_select2 is _DEFAULT_MARKER):
                    __attr_data_pat_select2 = None
                else:
                    __tt = type(__attr_data_pat_select2)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_data_pat_select2 = str(__attr_data_pat_select2)
                    else:
                        if (__tt is bytes):
                            __attr_data_pat_select2 = decode(__attr_data_pat_select2)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_data_pat_select2 = __attr_data_pat_select2.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_data_pat_select2)
                                    __attr_data_pat_select2 = (str(__attr_data_pat_select2) if (__attr_data_pat_select2 is __converted) else __converted)
                                else:
                                    __attr_data_pat_select2 = __attr_data_pat_select2()
            if (__attr_data_pat_select2 is not None):
                __append((' data-pat-select2="%s"' % __attr_data_pat_select2))
            __append('/>\n\n  </div>\n</div>')
            __i18n_domain = __previous_i18n_domain_4477237568
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }