# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/content/browser/contents/templates/properties.pt'

__tokens = {795: ("multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}", 22, 29), 857: ("python: options['vocabulary_url']", 23, 46), 1119: ("multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}", 30, 29), 1181: ("python: options['vocabulary_url']", 31, 46)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4481059376 = {'class': 'form-text', }
_static_4481058176 = {'class': 'form-check-label', 'for': 'fcCheckRecurse', }
_static_4481023904 = {'class': 'form-check-input', 'type': 'checkbox', 'name': 'recurse', 'value': 'yes', 'id': 'fcCheckRecurse', }
_static_4481021408 = {'class': 'form-check', }
_static_4481019824 = {'value': '<%= lang.value %>', }
_static_4481018672 = {'class': 'form-select', 'name': 'language', }
_static_4481016848 = {'class': 'form-label', }
_static_4481015408 = {'class': 'mb-2', }
_static_4481014304 = {'class': 'form-check-label', 'for': 'fcSwitchExcludeFromNavNo', }
_static_4481013008 = {'class': 'form-check-input', 'type': 'radio', 'name': 'exclude-from-nav', 'id': 'fcSwitchExcludeFromNavNo', 'value': 'no', }
_static_4481010368 = {'class': 'form-check', }
_static_4481009360 = {'class': 'form-check-label', 'for': 'fcSwitchExcludeFromNavYes', }
_static_4480974752 = {'class': 'form-check-input', 'type': 'radio', 'name': 'exclude-from-nav', 'id': 'fcSwitchExcludeFromNavYes', 'value': 'yes', }
_static_4480972592 = {'class': 'form-check', }
_static_4480971536 = {'class': 'form-label', 'for': 'fcSwitchExcludeFromNav', }
_static_4480969664 = {'class': 'mb-2', }
_static_4480968272 = {'name': 'contributors', 'class': 'pat-select2', 'data-pat-select2': "multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}", }
_static_4480966544 = {'class': 'form-label', }
_static_4480965104 = {'class': 'mb-2', }
_static_4417565216 = __C2ZContextWrapper
_static_4417553984 = __compile_zt_expr
_static_4480963712 = {'name': 'creators', 'class': 'pat-select2', 'data-pat-select2': "multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}", }
_static_4480961984 = {'class': 'form-label', }
_static_4480960544 = {'class': 'mb-2', }
_static_4480959824 = {'class': 'form-control', 'name': 'copyright', }
_static_4477183328 = {'class': 'form-label', }
_static_4477188512 = {'class': 'mb-2', }
_static_4477177280 = {'class': 'form-control', 'name': 'expirationDate', 'type': 'datetime-local', }
_static_4477180592 = {'class': 'form-label', }
_static_4477176464 = {'class': 'mb-2', }
_static_4477186592 = {'class': 'form-control', 'name': 'effectiveDate', 'type': 'datetime-local', }
_static_4477187456 = {'class': 'form-label', }
_static_4477185728 = {'class': 'mb-2', }
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

            # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4477177712
            __attrs_4477177712 = _static_4418309904
            __previous_i18n_domain_4477174352 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div>\n\n  ')

            # <Static value=<ast.Dict object at 0x10adc6ec0> name=None at 10adc7e80> -> __attrs_4477180640
            __attrs_4477180640 = _static_4477185728

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x10adc7580> name=None at 10adc7c70> -> __attrs_4477187216
            __attrs_4477187216 = _static_4477187456

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4477187648 = []
            __append_4477187648 = __stream_4477187648.append
            __append_4477187648('Publication Date')
            __msgid_4477187648 = __re_whitespace(''.join(__stream_4477187648)).strip()
            if 'publiciation_date':
                __append(translate('publiciation_date', mapping=None, default=__msgid_4477187648, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x10adc7220> name=None at 10adc55d0> -> __attrs_4477177088
            __attrs_4477177088 = _static_4477186592

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-control" name="effectiveDate" type="datetime-local" />\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x10adc4a90> name=None at 10adc4b80> -> __attrs_4477174736
            __attrs_4477174736 = _static_4477176464

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x10adc5ab0> name=None at 10adc5a20> -> __attrs_4477180352
            __attrs_4477180352 = _static_4477180592

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4477181312 = []
            __append_4477181312 = __stream_4477181312.append
            __append_4477181312('Expiration Date')
            __msgid_4477181312 = __re_whitespace(''.join(__stream_4477181312)).strip()
            if 'expiration_date':
                __append(translate('expiration_date', mapping=None, default=__msgid_4477181312, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x10adc4dc0> name=None at 10adc5c30> -> __attrs_4477189904
            __attrs_4477189904 = _static_4477177280

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-control" name="expirationDate" type="datetime-local" />\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x10adc79a0> name=None at 10adc4c40> -> __attrs_4477174832
            __attrs_4477174832 = _static_4477188512

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x10adc6560> name=None at 10adc5600> -> __attrs_4477183136
            __attrs_4477183136 = _static_4477183328

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4477179440 = []
            __append_4477179440 = __stream_4477179440.append
            __append_4477179440('Copyright')
            __msgid_4477179440 = __re_whitespace(''.join(__stream_4477179440)).strip()
            if 'copyright':
                __append(translate('copyright', mapping=None, default=__msgid_4477179440, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x10b160550> name=None at 10b160190> -> __attrs_4480959872
            __attrs_4480959872 = _static_4480959824

            # <textarea ... (0:0)
            # --------------------------------------------------------
            __append('<textarea class="form-control" name="copyright"></textarea>\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x10b160820> name=None at 10b160850> -> __attrs_4480960928
            __attrs_4480960928 = _static_4480960544

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x10b160dc0> name=None at 10b160df0> -> __attrs_4480962368
            __attrs_4480962368 = _static_4480961984

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4480961504 = []
            __append_4480961504 = __stream_4480961504.append
            __append_4480961504('Creators')
            __msgid_4480961504 = __re_whitespace(''.join(__stream_4480961504)).strip()
            if 'creators':
                __append(translate('creators', mapping=None, default=__msgid_4480961504, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x10b161480> name=None at 10b1614b0> -> __attrs_4480964432
            __attrs_4480964432 = _static_4480963712

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input name="creators" class="form-control" class="pat-select2"')

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4480964000
            __default_4480964000 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}" (22:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10b161510> -> __attr_data_pat_select2
            __token = 795
            __token = 857
            try:
                __zt_tmp = __attrs_4480964432
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_pat_select2 = _static_4417553984('python', " options['vocabulary_url']", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_data_pat_select2 = __quote(__attr_data_pat_select2, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_data_pat_select2 = ('%s%s' % ('multiple: true;\n                             vocabularyUrl: ', (__attr_data_pat_select2 if (__attr_data_pat_select2 is not None) else ''), ))
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
            __append('/>\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x10b1619f0> name=None at 10b161a20> -> __attrs_4480965488
            __attrs_4480965488 = _static_4480965104

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x10b161f90> name=None at 10b161fc0> -> __attrs_4480966928
            __attrs_4480966928 = _static_4480966544

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4480966064 = []
            __append_4480966064 = __stream_4480966064.append
            __append_4480966064('Contributors')
            __msgid_4480966064 = __re_whitespace(''.join(__stream_4480966064)).strip()
            if 'contributors':
                __append(translate('contributors', mapping=None, default=__msgid_4480966064, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x10b162650> name=None at 10b162680> -> __attrs_4480968992
            __attrs_4480968992 = _static_4480968272

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input name="contributors" class="form-control" class="pat-select2"')

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4480968560
            __default_4480968560 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}" (30:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10b1626e0> -> __attr_data_pat_select2
            __token = 1119
            __token = 1181
            try:
                __zt_tmp = __attrs_4480968992
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_pat_select2 = _static_4417553984('python', " options['vocabulary_url']", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_data_pat_select2 = __quote(__attr_data_pat_select2, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_data_pat_select2 = ('%s%s' % ('multiple: true;\n                             vocabularyUrl: ', (__attr_data_pat_select2 if (__attr_data_pat_select2 is not None) else ''), ))
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
            __append('/>\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x10b162bc0> name=None at 10b162bf0> -> __attrs_4480970048
            __attrs_4480970048 = _static_4480969664

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x10b163310> name=None at 10b163340> -> __attrs_4480971728
            __attrs_4480971728 = _static_4480971536

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label" for="fcSwitchExcludeFromNav">')
            __stream_4480970624 = []
            __append_4480970624 = __stream_4480970624.append
            __append_4480970624('Exclude from navigation')
            __msgid_4480970624 = __re_whitespace(''.join(__stream_4480970624)).strip()
            if 'exclude_from_nav':
                __append(translate('exclude_from_nav', mapping=None, default=__msgid_4480970624, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x10b163730> name=None at 10b163760> -> __attrs_4480972976
            __attrs_4480972976 = _static_4480972592

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-check">\n      ')

            # <Static value=<ast.Dict object at 0x10b163fa0> name=None at 10b163fd0> -> __attrs_4481007776
            __attrs_4481007776 = _static_4480974752

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-check-input" type="radio" name="exclude-from-nav" id="fcSwitchExcludeFromNavYes" value="yes">\n      ')

            # <Static value=<ast.Dict object at 0x10b16c6d0> name=None at 10b16c700> -> __attrs_4481009600
            __attrs_4481009600 = _static_4481009360

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-check-label" for="fcSwitchExcludeFromNavYes">')
            __stream_4481008496 = []
            __append_4481008496 = __stream_4481008496.append
            __append_4481008496('Yes')
            __msgid_4481008496 = __re_whitespace(''.join(__stream_4481008496)).strip()
            if 'yes':
                __append(translate('yes', mapping=None, default=__msgid_4481008496, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    </div>\n    ')

            # <Static value=<ast.Dict object at 0x10b16cac0> name=None at 10b16caf0> -> __attrs_4481010752
            __attrs_4481010752 = _static_4481010368

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-check">\n      ')

            # <Static value=<ast.Dict object at 0x10b16d510> name=None at 10b16d540> -> __attrs_4481011472
            __attrs_4481011472 = _static_4481013008

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-check-input" type="radio" name="exclude-from-nav" id="fcSwitchExcludeFromNavNo" value="no">\n      ')

            # <Static value=<ast.Dict object at 0x10b16da20> name=None at 10b16da50> -> __attrs_4481014544
            __attrs_4481014544 = _static_4481014304

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-check-label" for="fcSwitchExcludeFromNavNo">')
            __stream_4481013440 = []
            __append_4481013440 = __stream_4481013440.append
            __append_4481013440('No')
            __msgid_4481013440 = __re_whitespace(''.join(__stream_4481013440)).strip()
            if 'no':
                __append(translate('no', mapping=None, default=__msgid_4481013440, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    </div>\n  </div>\n\n  <% if (data.languages) { %>\n  ')

            # <Static value=<ast.Dict object at 0x10b16de70> name=None at 10b16dea0> -> __attrs_4481015792
            __attrs_4481015792 = _static_4481015408

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x10b16e410> name=None at 10b16e440> -> __attrs_4481017232
            __attrs_4481017232 = _static_4481016848

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4481016368 = []
            __append_4481016368 = __stream_4481016368.append
            __append_4481016368('Language')
            __msgid_4481016368 = __re_whitespace(''.join(__stream_4481016368)).strip()
            if 'label_language':
                __append(translate('label_language', mapping=None, default=__msgid_4481016368, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x10b16eb30> name=None at 10b16e770> -> __attrs_4481018720
            __attrs_4481018720 = _static_4481018672

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select class="form-select" name="language">\n      <% _.each(data.languages, function (lang) { %>\n        ')

            # <Static value=<ast.Dict object at 0x10b16efb0> name=None at 10b16efe0> -> __attrs_4481020256
            __attrs_4481020256 = _static_4481019824

            # <option ... (0:0)
            # --------------------------------------------------------
            __append('<option value="<%= lang.value %>"><%= lang.title %></option>\n      <% }); %>\n    </select>\n  </div>\n  <% } %>\n\n  ')

            # <Static value=<ast.Dict object at 0x10b16f5e0> name=None at 10b16f610> -> __attrs_4481021792
            __attrs_4481021792 = _static_4481021408

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-check">\n    ')

            # <Static value=<ast.Dict object at 0x10b16ffa0> name=None at 10b16ffd0> -> __attrs_4481056928
            __attrs_4481056928 = _static_4481023904

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-check-input" type="checkbox" name="recurse" value="yes" id="fcCheckRecurse" />\n    ')

            # <Static value=<ast.Dict object at 0x10b178580> name=None at 10b1785b0> -> __attrs_4481058416
            __attrs_4481058416 = _static_4481058176

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-check-label" for="fcCheckRecurse">')
            __stream_4481057312 = []
            __append_4481057312 = __stream_4481057312.append
            __append_4481057312('Include contained items')
            __msgid_4481057312 = __re_whitespace(''.join(__stream_4481057312)).strip()
            if 'label_include_contained_objects':
                __append(translate('label_include_contained_objects', mapping=None, default=__msgid_4481057312, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x10b178a30> name=None at 10b178a60> -> __attrs_4481059760
            __attrs_4481059760 = _static_4481059376

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="form-text">')
            __stream_4481058896 = []
            __append_4481058896 = __stream_4481058896.append
            __append_4481058896('\n    If checked, this will attempt to modify the status of all content in any selected folders and their subfolders.\n    ')
            __msgid_4481058896 = __re_whitespace(''.join(__stream_4481058896)).strip()
            if 'help_include_contained_objects':
                __append(translate('help_include_contained_objects', mapping=None, default=__msgid_4481058896, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n  </div>\n\n</div>')
            __i18n_domain = __previous_i18n_domain_4477174352
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }