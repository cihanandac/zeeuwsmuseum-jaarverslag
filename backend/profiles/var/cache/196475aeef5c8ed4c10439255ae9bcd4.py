# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/content/browser/contents/templates/workflow.pt'

__tokens = {}

from sys import exc_info as _exc_info

_static_4476935120 = {'class': 'form-text', }
_static_4476929504 = {'class': 'form-check-label', 'for': 'fcWorkflowRecurse', }
_static_4476929264 = {'class': 'form-check-input', 'type': 'checkbox', 'name': 'recurse', 'value': 'yes', 'id': 'fcWorkflowRecurse', }
_static_4477174400 = {'class': 'form-check', }
_static_4477175024 = {'class': 'form-text', }
_static_4477179536 = {'value': '<%= transition.id %>', }
_static_4477179008 = {'class': 'form-select', 'name': 'transition', }
_static_4477183232 = {'class': 'form-label', }
_static_4477185728 = {'class': 'mb-2', }
_static_4477181936 = {'class': 'form-control', 'rows': '2', 'name': 'comments', }
_static_4477185248 = {'class': 'form-label', }
_static_4477183952 = {'class': 'mb-2', }
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

            # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4477180688
            __attrs_4477180688 = _static_4418309904
            __previous_i18n_domain_4477182368 = __i18n_domain
            __i18n_domain = 'plone'

            # <fieldset ... (0:0)
            # --------------------------------------------------------
            __append('<fieldset>\n  ')

            # <Static value=<ast.Dict object at 0x10adc67d0> name=None at 10adc6800> -> __attrs_4477184384
            __attrs_4477184384 = _static_4477183952

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x10adc6ce0> name=None at 10adc6290> -> __attrs_4477188032
            __attrs_4477188032 = _static_4477185248

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4477179920 = []
            __append_4477179920 = __stream_4477179920.append
            __append_4477179920('Comments')
            __msgid_4477179920 = __re_whitespace(''.join(__stream_4477179920)).strip()
            if 'label_comments':
                __append(translate('label_comments', mapping=None, default=__msgid_4477179920, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x10adc5ff0> name=None at 10adc6fe0> -> __attrs_4477177280
            __attrs_4477177280 = _static_4477181936

            # <textarea ... (0:0)
            # --------------------------------------------------------
            __append('<textarea class="form-control" rows="2" name="comments"></textarea>\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x10adc6ec0> name=None at 10adc6e60> -> __attrs_4477188464
            __attrs_4477188464 = _static_4477185728

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x10adc6500> name=None at 10adc6320> -> __attrs_4477176848
            __attrs_4477176848 = _static_4477183232

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4477180448 = []
            __append_4477180448 = __stream_4477180448.append
            __append_4477180448('Change State')
            __msgid_4477180448 = __re_whitespace(''.join(__stream_4477180448)).strip()
            if 'label_change_status':
                __append(translate('label_change_status', mapping=None, default=__msgid_4477180448, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x10adc5480> name=None at 10adc53f0> -> __attrs_4477178000
            __attrs_4477178000 = _static_4477179008

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select class="form-select" name="transition">\n      <% if(data.transitions){\n        _.each(data.transitions, function(transition){\n          %>')

            # <Static value=<ast.Dict object at 0x10adc5690> name=None at 10adc4d60> -> __attrs_4477178624
            __attrs_4477178624 = _static_4477179536

            # <option ... (0:0)
            # --------------------------------------------------------
            __append('<option value="<%= transition.id %>"><%= transition.title %></option>\n          <%\n        });\n      } %>\n    </select>\n    ')

            # <Static value=<ast.Dict object at 0x10adc44f0> name=None at 10adc7640> -> __attrs_4477186976
            __attrs_4477186976 = _static_4477175024

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="form-text">')
            __stream_4477189280 = []
            __append_4477189280 = __stream_4477189280.append
            __append_4477189280('Select the transition to be used for modifying the items state.')
            __msgid_4477189280 = __re_whitespace(''.join(__stream_4477189280)).strip()
            if 'help_change_status_action':
                __append(translate('help_change_status_action', mapping=None, default=__msgid_4477189280, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n  </div>\n  ')

            # <Static value=<ast.Dict object at 0x10adc4280> name=None at 10adc7b50> -> __attrs_4476930656
            __attrs_4476930656 = _static_4477174400

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-check">\n    ')

            # <Static value=<ast.Dict object at 0x10ad884f0> name=None at 10ad888e0> -> __attrs_4476929648
            __attrs_4476929648 = _static_4476929264

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-check-input" type="checkbox" name="recurse" value="yes" id="fcWorkflowRecurse" />\n    ')

            # <Static value=<ast.Dict object at 0x10ad885e0> name=None at 10ad88a00> -> __attrs_4476930128
            __attrs_4476930128 = _static_4476929504

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-check-label" for="fcWorkflowRecurse">')
            __stream_4476935840 = []
            __append_4476935840 = __stream_4476935840.append
            __append_4476935840('Include contained items')
            __msgid_4476935840 = __re_whitespace(''.join(__stream_4476935840)).strip()
            if 'label_include_contained_objects':
                __append(translate('label_include_contained_objects', mapping=None, default=__msgid_4476935840, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x10ad89bd0> name=None at 10ad8beb0> -> __attrs_4476932720
            __attrs_4476932720 = _static_4476935120

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="form-text">')
            __stream_4476931616 = []
            __append_4476931616 = __stream_4476931616.append
            __append_4476931616('\n    If checked, this will attempt to modify the status of all content in any selected folders and their subfolders.\n    ')
            __msgid_4476931616 = __re_whitespace(''.join(__stream_4476931616)).strip()
            if 'help_include_contained_objects':
                __append(translate('help_include_contained_objects', mapping=None, default=__msgid_4476931616, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n  </div>\n</fieldset>')
            __i18n_domain = __previous_i18n_domain_4477182368
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }