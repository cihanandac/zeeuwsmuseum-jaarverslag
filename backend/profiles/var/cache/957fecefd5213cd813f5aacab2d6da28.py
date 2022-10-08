# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/Products/CMFPlone/browser/templates/error_message.pt'

__tokens = {390: ('options/error_type|nothing', 11, 26), 441: (' options/error_tb|nothin', 12, 23), 494: ('d options/error_log_id|nothi', 13, 26), 567: ("python:err_type == 'NotFound'", 15, 39), 651: ('nocall:view/@@plone_redirector_view', 17, 51), 1699: ('string:${context/portal_url}/contact-info', 35, 48), 2055: ('redirection_view/find_first_parent', 43, 58), 2149: (' redirection_view/search_for_simila', 44, 58), 2241: ('w context/@@plo', 45, 54), 2311: ('ry context/portal_regis', 46, 51), 2396: ("ion python:registry['plone.types_use_view_action_in_listin", 47, 57), 2512: ("ngth python:registry['plone.search_results_description_len", 48, 52), 2632: ('tring nocall:plone_view/normalize', 49, 55), 2722: ('python:first_parent is not None or similar_items', 50, 48), 3031: ('first_parent/absolute_url | nothing', 56, 52), 3124: ('first_parent/absolute_url', 57, 55), 3206: (" python:hasattr(first_parent, 'getTypeInfo') and first_parent.getTypeInfo().getId(", 58, 55), 3337: ("l python:result_url + '/view' if result_type in use_view_action else result_u", 59, 46), 3466: ('result_type', 60, 47), 3596: ("python:' state-' + context.portal_workflow.getInfoFor(first_parent, 'review_state', '')", 62, 67), 3521: ('${url}', 61, 41), 3523: ('url', 61, 43), 3743: ("python:'contenttype-' + normalizeString(result_type) + item_wf_state_class", 63, 57), 3819: ('${first_parent/Title}', 63, 133), 3821: ('first_parent/Title', 63, 135), 3896: ('python:plone_view.cropText(first_parent.Description(), desc_length)', 64, 51), 4134: ('similar_items', 68, 53), 4205: ('similar/getURL', 69, 55), 4276: (' similar/portal_typ', 70, 55), 4344: ("l python:result_url + '/view' if result_type in use_view_action else result_u", 71, 46), 4543: ('string: state-${similar/review_state}', 73, 67), 4468: ('${url}', 72, 41), 4470: ('url', 72, 43), 4640: ("python:'contenttype-' + normalizeString(result_type) + item_wf_state_class", 74, 57), 4716: ('${similar/pretty_title_or_id}', 74, 133), 4718: ('similar/pretty_title_or_id', 74, 135), 4801: ("python:plone_view.cropText(similar.Description or '', desc_length)", 75, 51), 5269: ('view/is_manager', 89, 35), 5202: ("python: err_type != 'NotFound'", 88, 41), 5557: ('isManager', 97, 36), 5756: ('err_tb', 102, 37), 5830: ('not:isManager', 105, 40), 6231: ('string:${context/portal_url}/contact-info', 111, 44), 261: ('context/@@main_template/macros/master', 6, 23), 261: ('context/@@main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4480087856 = {'href': '#', }
_static_4485570688 = {'id': 'content-core', }
_static_4482931040 = {'class': 'documentFirstHeading', }
_static_4485567232 = {'class': 'discreet', }
_static_4485565744 = {'href': '${url}', 'class': "python:'contenttype-' + normalizeString(result_type) + item_wf_state_class", }
_static_4482930032 = {'class': 'discreet', }
_static_4482925664 = {'href': '${url}', 'class': "python:'contenttype-' + normalizeString(result_type) + item_wf_state_class", }
_static_4482934400 = {'id': 'page-not-found-list', }
_static_4480407472 = {'href': '#', }
_static_4480408480 = {'class': 'discreet', }
_static_4480411264 = {'class': 'description', }
_static_4480415824 = {'id': 'content-core', }
_static_4480406176 = {'class': 'documentFirstHeading', }
_static_4417565216 = __C2ZContextWrapper
_static_4417553984 = __compile_zt_expr
_static_4480343568 = 'master'
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

            # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4480344816
            __attrs_4480344816 = _static_4418309904
            __previous_i18n_domain_4480339392 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4484835968 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x10b0c9e10> name=None at 10b0c8c40> -> __value
            __value = _static_4480343568
            econtext['macroname'] = __value

            def __fill_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4480405264
                __attrs_4480405264 = _static_4418309904
                __backup_err_type_4480349952 = get('err_type', __marker)

                # <Value 'options/error_type|nothing' (11:26)> -> __value
                __token = 390
                try:
                    __zt_tmp = __attrs_4480405264
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4417553984('path', 'options/error_type|nothing', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                econtext['err_type'] = __value
                __backup_err_tb_4480350720 = get('err_tb', __marker)

                # <Value 'options/error_tb|nothing' (12:23)> -> __value
                __token = 441
                try:
                    __zt_tmp = __attrs_4480405264
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4417553984('path', 'options/error_tb|nothing', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                econtext['err_tb'] = __value
                __backup_err_log_id_4480132256 = get('err_log_id', __marker)

                # <Value 'options/error_log_id|nothing' (13:26)> -> __value
                __token = 494
                try:
                    __zt_tmp = __attrs_4480405264
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4417553984('path', 'options/error_log_id|nothing', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                econtext['err_log_id'] = __value
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4480416064
                __attrs_4480416064 = _static_4418309904

                # <Value "python:err_type == 'NotFound'" (15:39)> -> __condition
                __token = 567
                try:
                    __zt_tmp = __attrs_4480416064
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4417553984('python', "err_type == 'NotFound'", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                if __condition:
                    __append('\n\n            ')

                    # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4480412128
                    __attrs_4480412128 = _static_4418309904
                    __backup_redirection_view_4480412656 = get('redirection_view', __marker)

                    # <Value 'nocall:view/@@plone_redirector_view' (17:51)> -> __value
                    __token = 651
                    try:
                        __zt_tmp = __attrs_4480412128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4417553984('nocall', 'view/@@plone_redirector_view', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    econtext['redirection_view'] = __value
                    __append('\n\n                ')

                    # <Static value=<ast.Dict object at 0x10b0d92a0> name=None at 10b0d9c30> -> __attrs_4480415680
                    __attrs_4480415680 = _static_4480406176

                    # <h1 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h1 class="documentFirstHeading">')
                    __stream_4480417504 = []
                    __append_4480417504 = __stream_4480417504.append
                    __append_4480417504('\n                    This page does not seem to exist&hellip;\n                ')
                    __msgid_4480417504 = __re_whitespace(''.join(__stream_4480417504)).strip()
                    if 'heading_site_there_seems_to_be_an_error':
                        __append(translate('heading_site_there_seems_to_be_an_error', mapping=None, default=__msgid_4480417504, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</h1>\n\n                ')

                    # <Static value=<ast.Dict object at 0x10b0db850> name=None at 10b0dbcd0> -> __attrs_4480404352
                    __attrs_4480404352 = _static_4480415824

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="content-core">\n                    ')

                    # <Static value=<ast.Dict object at 0x10b0da680> name=None at 10b0d8670> -> __attrs_4480406416
                    __attrs_4480406416 = _static_4480411264

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="description">')
                    __stream_4480412080 = []
                    __append_4480412080 = __stream_4480412080.append
                    __append_4480412080('\n \t                    We apologize for the inconvenience, but the page you were trying to access is not at this address.\n                        You can use the links below to help you find what you are looking for.\n                     ')
                    __msgid_4480412080 = __re_whitespace(''.join(__stream_4480412080)).strip()
                    if 'description_site_error':
                        __append(translate('description_site_error', mapping=None, default=__msgid_4480412080, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>\n\n                    ')

                    # <Static value=<ast.Dict object at 0x10b0d9ba0> name=None at 10b096170> -> __attrs_4480402432
                    __attrs_4480402432 = _static_4480408480

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="discreet">')
                    __stream_4469634240_site_admin = ''
                    __stream_4480412560 = []
                    __append_4480412560 = __stream_4480412560.append
                    __append_4480412560('\n                        If you are certain you have the correct web address but are encountering an error, please\n                        contact the ')
                    __stream_4469634240_site_admin = []
                    __append_4469634240_site_admin = __stream_4469634240_site_admin.append

                    # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4480411552
                    __attrs_4480411552 = _static_4418309904

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_4469634240_site_admin('<span>\n                        ')

                    # <Static value=<ast.Dict object at 0x10b0d97b0> name=None at 10b0d90c0> -> __attrs_4482939392
                    __attrs_4482939392 = _static_4480407472

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_4469634240_site_admin('<a')

                    # <Symbol value=<DEFAULT> at 107619600> -> __default_4480417120
                    __default_4480417120 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/portal_url}/contact-info' (35:48)> -> __attr_href
                    __token = 1699
                    try:
                        __zt_tmp = __attrs_4482939392
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4417553984('string', '${context/portal_url}/contact-info', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_4469634240_site_admin((' href="%s"' % __attr_href))
                    __append_4469634240_site_admin('>')
                    __stream_4480413088 = []
                    __append_4480413088 = __stream_4480413088.append
                    __append_4480413088('site administration')
                    __msgid_4480413088 = __re_whitespace(''.join(__stream_4480413088)).strip()
                    if 'label_site_administration':
                        __append_4469634240_site_admin(translate('label_site_administration', mapping=None, default=__msgid_4480413088, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_4469634240_site_admin('</a></span>')
                    __append_4480412560('${site_admin}')
                    __stream_4469634240_site_admin = ''.join(__stream_4469634240_site_admin)
                    __append_4480412560('.\n                    ')
                    __msgid_4480412560 = __re_whitespace(''.join(__stream_4480412560)).strip()
                    if 'description_site_error_mail_site_admin':
                        __append(translate('description_site_error_mail_site_admin', mapping={'site_admin': __stream_4469634240_site_admin, }, default=__msgid_4480412560, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>\n\n                    ')

                    # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4482929552
                    __attrs_4482929552 = _static_4418309904

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p>')
                    __stream_4480409392 = []
                    __append_4480409392 = __stream_4480409392.append
                    __append_4480409392('\n                    Thank you.\n                    ')
                    __msgid_4480409392 = __re_whitespace(''.join(__stream_4480409392)).strip()
                    if 'description_site_error_thank_you':
                        __append(translate('description_site_error_thank_you', mapping=None, default=__msgid_4480409392, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>\n\n                    <!-- Offer search results for suggestions -->\n                    ')

                    # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4482936848
                    __attrs_4482936848 = _static_4418309904
                    __backup_first_parent_4480570928 = get('first_parent', __marker)

                    # <Value 'redirection_view/find_first_parent' (43:58)> -> __value
                    __token = 2055
                    try:
                        __zt_tmp = __attrs_4482936848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4417553984('path', 'redirection_view/find_first_parent', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    econtext['first_parent'] = __value
                    __backup_similar_items_4480377584 = get('similar_items', __marker)

                    # <Value 'redirection_view/search_for_similar' (44:58)> -> __value
                    __token = 2149
                    try:
                        __zt_tmp = __attrs_4482936848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4417553984('path', 'redirection_view/search_for_similar', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    econtext['similar_items'] = __value
                    __backup_plone_view_4482863776 = get('plone_view', __marker)

                    # <Value 'context/@@plone' (45:54)> -> __value
                    __token = 2241
                    try:
                        __zt_tmp = __attrs_4482936848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4417553984('path', 'context/@@plone', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    econtext['plone_view'] = __value
                    __backup_registry_4480574528 = get('registry', __marker)

                    # <Value 'context/portal_registry' (46:51)> -> __value
                    __token = 2311
                    try:
                        __zt_tmp = __attrs_4482936848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4417553984('path', 'context/portal_registry', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    econtext['registry'] = __value
                    __backup_use_view_action_4480578704 = get('use_view_action', __marker)

                    # <Value "python:registry['plone.types_use_view_action_in_listings']" (47:57)> -> __value
                    __token = 2396
                    try:
                        __zt_tmp = __attrs_4482936848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4417553984('python', "registry['plone.types_use_view_action_in_listings']", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    econtext['use_view_action'] = __value
                    __backup_desc_length_4483069168 = get('desc_length', __marker)

                    # <Value "python:registry['plone.search_results_description_length']" (48:52)> -> __value
                    __token = 2512
                    try:
                        __zt_tmp = __attrs_4482936848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4417553984('python', "registry['plone.search_results_description_length']", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    econtext['desc_length'] = __value
                    __backup_normalizeString_4483056496 = get('normalizeString', __marker)

                    # <Value 'nocall:plone_view/normalizeString' (49:55)> -> __value
                    __token = 2632
                    try:
                        __zt_tmp = __attrs_4482936848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4417553984('nocall', 'plone_view/normalizeString', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    econtext['normalizeString'] = __value

                    # <Value 'python:first_parent is not None or similar_items' (50:48)> -> __condition
                    __token = 2722
                    try:
                        __zt_tmp = __attrs_4482936848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4417553984('python', 'first_parent is not None or similar_items', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    if __condition:
                        __append('\n\n                        ')

                        # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4482934880
                        __attrs_4482934880 = _static_4418309904

                        # <h2 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h2>')
                        __stream_4482925856 = []
                        __append_4482925856 = __stream_4482925856.append
                        __append_4482925856('You might have been looking for&hellip;')
                        __msgid_4482925856 = __re_whitespace(''.join(__stream_4482925856)).strip()
                        if 'heading_not_found_suggestions':
                            __append(translate('heading_not_found_suggestions', mapping=None, default=__msgid_4482925856, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</h2>\n                        ')

                        # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4482934160
                        __attrs_4482934160 = _static_4418309904

                        # <nav ... (0:0)
                        # --------------------------------------------------------
                        __append('<nav>\n                        ')

                        # <Static value=<ast.Dict object at 0x10b342680> name=None at 10b341d50> -> __attrs_4482935264
                        __attrs_4482935264 = _static_4482934400

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append('<ul id="page-not-found-list">\n\n                        ')

                        # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4482925616
                        __attrs_4482925616 = _static_4418309904

                        # <Value 'first_parent/absolute_url | nothing' (56:52)> -> __condition
                        __token = 3031
                        try:
                            __zt_tmp = __attrs_4482925616
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4417553984('path', 'first_parent/absolute_url | nothing', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        if __condition:
                            __append('\n                            ')

                            # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4482934928
                            __attrs_4482934928 = _static_4418309904
                            __backup_result_url_4480074848 = get('result_url', __marker)

                            # <Value 'first_parent/absolute_url' (57:55)> -> __value
                            __token = 3124
                            try:
                                __zt_tmp = __attrs_4482934928
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4417553984('path', 'first_parent/absolute_url', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                            econtext['result_url'] = __value
                            __backup_result_type_4480085696 = get('result_type', __marker)

                            # <Value "python:hasattr(first_parent, 'getTypeInfo') and first_parent.getTypeInfo().getId()" (58:55)> -> __value
                            __token = 3206
                            try:
                                __zt_tmp = __attrs_4482934928
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4417553984('python', "hasattr(first_parent, 'getTypeInfo') and first_parent.getTypeInfo().getId()", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                            econtext['result_type'] = __value
                            __backup_url_4480415296 = get('url', __marker)

                            # <Value "python:result_url + '/view' if result_type in use_view_action else result_url" (59:46)> -> __value
                            __token = 3337
                            try:
                                __zt_tmp = __attrs_4482934928
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4417553984('python', "result_url + '/view' if result_type in use_view_action else result_url", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                            econtext['url'] = __value

                            # <Value 'result_type' (60:47)> -> __condition
                            __token = 3466
                            try:
                                __zt_tmp = __attrs_4482934928
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4417553984('path', 'result_type', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                            if __condition:

                                # <li ... (0:0)
                                # --------------------------------------------------------
                                __append('<li>\n                                ')

                                # <Static value=<ast.Dict object at 0x10b340460> name=None at 10b340700> -> __attrs_4482930224
                                __attrs_4482930224 = _static_4482925664
                                __backup_item_wf_state_class_4480407856 = get('item_wf_state_class', __marker)

                                # <Value "python:' state-' + context.portal_workflow.getInfoFor(first_parent, 'review_state', '')" (62:67)> -> __value
                                __token = 3596
                                try:
                                    __zt_tmp = __attrs_4482930224
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __value = _static_4417553984('python', "' state-' + context.portal_workflow.getInfoFor(first_parent, 'review_state', '')", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                                econtext['item_wf_state_class'] = __value

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append('<a')

                                # <Symbol value=<DEFAULT> at 107619600> -> __default_4482929072
                                __default_4482929072 = _DEFAULT_MARKER

                                # <Interpolation value=<Substitution '${url}' (61:41)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10b340af0> -> __attr_href
                                __token = 3521
                                __token = 3523
                                try:
                                    __zt_tmp = __attrs_4482930224
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_4417553984('path', 'url', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
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

                                # <Symbol value=<DEFAULT> at 107619600> -> __default_4482932768
                                __default_4482932768 = _DEFAULT_MARKER

                                # <Substitution "python:'contenttype-' + normalizeString(result_type) + item_wf_state_class" (63:57)> -> __attr_class
                                __token = 3743
                                try:
                                    __zt_tmp = __attrs_4482930224
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_class = _static_4417553984('python', "'contenttype-' + normalizeString(result_type) + item_wf_state_class", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_class is not None):
                                    __append((' class="%s"' % __attr_class))
                                __append('>')

                                # <Interpolation value=<Substitution '${first_parent/Title}' (63:133)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10b343160> -> __content_4320017904
                                __token = 3819
                                __token = 3821
                                try:
                                    __zt_tmp = __attrs_4482930224
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __content_4320017904 = _static_4417553984('path', 'first_parent/Title', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                                __content_4320017904 = __quote(__content_4320017904, '\x00', '&#0;', None, None)
                                __content_4320017904 = __content_4320017904
                                if (__content_4320017904 is None):
                                    pass
                                else:
                                    if (__content_4320017904 is None):
                                        __content_4320017904 = None
                                    else:
                                        __tt = type(__content_4320017904)
                                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                                            __content_4320017904 = str(__content_4320017904)
                                        else:
                                            if (__tt is bytes):
                                                __content_4320017904 = decode(__content_4320017904)
                                            else:
                                                if (__tt is not str):
                                                    try:
                                                        __content_4320017904 = __content_4320017904.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__content_4320017904)
                                                        __content_4320017904 = (str(__content_4320017904) if (__content_4320017904 is __converted) else __converted)
                                                    else:
                                                        __content_4320017904 = __content_4320017904()
                                if (__content_4320017904 is not None):
                                    __append(__content_4320017904)
                                __append('</a>')
                                if (__backup_item_wf_state_class_4480407856 is __marker):
                                    del econtext['item_wf_state_class']
                                else:
                                    econtext['item_wf_state_class'] = __backup_item_wf_state_class_4480407856
                                __append('\n                                ')

                                # <Static value=<ast.Dict object at 0x10b341570> name=None at 10b340eb0> -> __attrs_4485568672
                                __attrs_4485568672 = _static_4482930032

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span class="discreet">')

                                # <Symbol value=<DEFAULT> at 107619600> -> __default_4482934640
                                __default_4482934640 = _DEFAULT_MARKER

                                # <Value 'python:plone_view.cropText(first_parent.Description(), desc_length)' (64:51)> -> __cache_4482934736
                                __token = 3896
                                try:
                                    __zt_tmp = __attrs_4485568672
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_4482934736 = _static_4417553984('python', 'plone_view.cropText(first_parent.Description(), desc_length)', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))

                                # <BinOp left=<Value 'python:plone_view.cropText(first_parent.Description(), desc_length)' (64:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107619600> at 10b342d70> -> __condition
                                __expression = __cache_4482934736

                                # <Symbol value=<DEFAULT> at 107619600> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append(' Description ')
                                else:
                                    __content = __cache_4482934736
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                                __append('</span>\n                            </li>')
                            if (__backup_url_4480415296 is __marker):
                                del econtext['url']
                            else:
                                econtext['url'] = __backup_url_4480415296
                            if (__backup_result_type_4480085696 is __marker):
                                del econtext['result_type']
                            else:
                                econtext['result_type'] = __backup_result_type_4480085696
                            if (__backup_result_url_4480074848 is __marker):
                                del econtext['result_url']
                            else:
                                econtext['result_url'] = __backup_result_url_4480074848
                            __append('\n                        ')
                        __append('\n\n                        ')

                        # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4485577888
                        __attrs_4485577888 = _static_4418309904
                        __backup_similar_4480336896 = get('similar', __marker)

                        # <Value 'similar_items' (68:53)> -> __iterator
                        __token = 4134
                        try:
                            __zt_tmp = __attrs_4485577888
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_4417553984('path', 'similar_items', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        (__iterator, ____index_4485577360, ) = getname('repeat')('similar', __iterator)
                        econtext['similar'] = None
                        for __item in __iterator:
                            econtext['similar'] = __item
                            __append('\n                            ')

                            # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4485563920
                            __attrs_4485563920 = _static_4418309904
                            __backup_result_url_4480413472 = get('result_url', __marker)

                            # <Value 'similar/getURL' (69:55)> -> __value
                            __token = 4205
                            try:
                                __zt_tmp = __attrs_4485563920
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4417553984('path', 'similar/getURL', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                            econtext['result_url'] = __value
                            __backup_result_type_4480417264 = get('result_type', __marker)

                            # <Value 'similar/portal_type' (70:55)> -> __value
                            __token = 4276
                            try:
                                __zt_tmp = __attrs_4485563920
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4417553984('path', 'similar/portal_type', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                            econtext['result_type'] = __value
                            __backup_url_4482938096 = get('url', __marker)

                            # <Value "python:result_url + '/view' if result_type in use_view_action else result_url" (71:46)> -> __value
                            __token = 4344
                            try:
                                __zt_tmp = __attrs_4485563920
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4417553984('python', "result_url + '/view' if result_type in use_view_action else result_url", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                            econtext['url'] = __value

                            # <li ... (0:0)
                            # --------------------------------------------------------
                            __append('<li>\n                                ')

                            # <Static value=<ast.Dict object at 0x10b5c4d30> name=None at 10b5c40d0> -> __attrs_4485572752
                            __attrs_4485572752 = _static_4485565744
                            __backup_item_wf_state_class_4482925040 = get('item_wf_state_class', __marker)

                            # <Value 'string: state-${similar/review_state}' (73:67)> -> __value
                            __token = 4543
                            try:
                                __zt_tmp = __attrs_4485572752
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4417553984('string', ' state-${similar/review_state}', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                            econtext['item_wf_state_class'] = __value

                            # <a ... (0:0)
                            # --------------------------------------------------------
                            __append('<a')

                            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485574192
                            __default_4485574192 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${url}' (72:41)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10b5c5b40> -> __attr_href
                            __token = 4468
                            __token = 4470
                            try:
                                __zt_tmp = __attrs_4485572752
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href = _static_4417553984('path', 'url', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
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

                            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485572128
                            __default_4485572128 = _DEFAULT_MARKER

                            # <Substitution "python:'contenttype-' + normalizeString(result_type) + item_wf_state_class" (74:57)> -> __attr_class
                            __token = 4640
                            try:
                                __zt_tmp = __attrs_4485572752
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_4417553984('python', "'contenttype-' + normalizeString(result_type) + item_wf_state_class", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((' class="%s"' % __attr_class))
                            __append('>')

                            # <Interpolation value=<Substitution '${similar/pretty_title_or_id}' (74:133)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10b5c4a00> -> __content_4320017904
                            __token = 4716
                            __token = 4718
                            try:
                                __zt_tmp = __attrs_4485572752
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __content_4320017904 = _static_4417553984('path', 'similar/pretty_title_or_id', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                            __content_4320017904 = __quote(__content_4320017904, '\x00', '&#0;', None, None)
                            __content_4320017904 = __content_4320017904
                            if (__content_4320017904 is None):
                                pass
                            else:
                                if (__content_4320017904 is None):
                                    __content_4320017904 = None
                                else:
                                    __tt = type(__content_4320017904)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __content_4320017904 = str(__content_4320017904)
                                    else:
                                        if (__tt is bytes):
                                            __content_4320017904 = decode(__content_4320017904)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __content_4320017904 = __content_4320017904.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__content_4320017904)
                                                    __content_4320017904 = (str(__content_4320017904) if (__content_4320017904 is __converted) else __converted)
                                                else:
                                                    __content_4320017904 = __content_4320017904()
                            if (__content_4320017904 is not None):
                                __append(__content_4320017904)
                            __append('</a>')
                            if (__backup_item_wf_state_class_4482925040 is __marker):
                                del econtext['item_wf_state_class']
                            else:
                                econtext['item_wf_state_class'] = __backup_item_wf_state_class_4482925040
                            __append('\n                                ')

                            # <Static value=<ast.Dict object at 0x10b5c5300> name=None at 10b5c4f70> -> __attrs_4485565792
                            __attrs_4485565792 = _static_4485567232

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span class="discreet">')

                            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485575056
                            __default_4485575056 = _DEFAULT_MARKER

                            # <Value "python:plone_view.cropText(similar.Description or '', desc_length)" (75:51)> -> __cache_4485574576
                            __token = 4801
                            try:
                                __zt_tmp = __attrs_4485565792
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4485574576 = _static_4417553984('python', "plone_view.cropText(similar.Description or '', desc_length)", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))

                            # <BinOp left=<Value "python:plone_view.cropText(similar.Description or '', desc_length)" (75:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107619600> at 10b5c46d0> -> __condition
                            __expression = __cache_4485574576

                            # <Symbol value=<DEFAULT> at 107619600> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(' Description ')
                            else:
                                __content = __cache_4485574576
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('</span>\n                            </li>')
                            if (__backup_url_4482938096 is __marker):
                                del econtext['url']
                            else:
                                econtext['url'] = __backup_url_4482938096
                            if (__backup_result_type_4480417264 is __marker):
                                del econtext['result_type']
                            else:
                                econtext['result_type'] = __backup_result_type_4480417264
                            if (__backup_result_url_4480413472 is __marker):
                                del econtext['result_url']
                            else:
                                econtext['result_url'] = __backup_result_url_4480413472
                            __append('\n                        ')
                            ____index_4485577360 -= 1
                            if (____index_4485577360 > 0):
                                __append('')
                        if (__backup_similar_4480336896 is __marker):
                            del econtext['similar']
                        else:
                            econtext['similar'] = __backup_similar_4480336896
                        __append('\n\n                        </ul>\n                        </nav>\n\n                    ')
                    if (__backup_normalizeString_4483056496 is __marker):
                        del econtext['normalizeString']
                    else:
                        econtext['normalizeString'] = __backup_normalizeString_4483056496
                    if (__backup_desc_length_4483069168 is __marker):
                        del econtext['desc_length']
                    else:
                        econtext['desc_length'] = __backup_desc_length_4483069168
                    if (__backup_use_view_action_4480578704 is __marker):
                        del econtext['use_view_action']
                    else:
                        econtext['use_view_action'] = __backup_use_view_action_4480578704
                    if (__backup_registry_4480574528 is __marker):
                        del econtext['registry']
                    else:
                        econtext['registry'] = __backup_registry_4480574528
                    if (__backup_plone_view_4482863776 is __marker):
                        del econtext['plone_view']
                    else:
                        econtext['plone_view'] = __backup_plone_view_4482863776
                    if (__backup_similar_items_4480377584 is __marker):
                        del econtext['similar_items']
                    else:
                        econtext['similar_items'] = __backup_similar_items_4480377584
                    if (__backup_first_parent_4480570928 is __marker):
                        del econtext['first_parent']
                    else:
                        econtext['first_parent'] = __backup_first_parent_4480570928
                    __append('\n                </div>\n            ')
                    if (__backup_redirection_view_4480412656 is __marker):
                        del econtext['redirection_view']
                    else:
                        econtext['redirection_view'] = __backup_redirection_view_4480412656
                    __append('\n\n        ')
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4480415632
                __attrs_4480415632 = _static_4418309904
                __backup_isManager_4480406224 = get('isManager', __marker)

                # <Value 'view/is_manager' (89:35)> -> __value
                __token = 5269
                try:
                    __zt_tmp = __attrs_4480415632
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4417553984('path', 'view/is_manager', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                econtext['isManager'] = __value

                # <Value "python: err_type != 'NotFound'" (88:41)> -> __condition
                __token = 5202
                try:
                    __zt_tmp = __attrs_4480415632
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4417553984('python', " err_type != 'NotFound'", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                if __condition:
                    __append('\n\n            ')

                    # <Static value=<ast.Dict object at 0x10b341960> name=None at 10b340a60> -> __attrs_4485565168
                    __attrs_4485565168 = _static_4482931040

                    # <h1 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h1 class="documentFirstHeading">')
                    __stream_4482931904 = []
                    __append_4482931904 = __stream_4482931904.append
                    __append_4482931904('\n                We&#8217;re sorry, but there seems to be an error&hellip;\n            ')
                    __msgid_4482931904 = __re_whitespace(''.join(__stream_4482931904)).strip()
                    if 'heading_site_error_sorry':
                        __append(translate('heading_site_error_sorry', mapping=None, default=__msgid_4482931904, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</h1>\n\n            ')

                    # <Static value=<ast.Dict object at 0x10b5c6080> name=None at 10b5c7130> -> __attrs_4485576352
                    __attrs_4485576352 = _static_4485570688

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="content-core">\n                ')

                    # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4485575872
                    __attrs_4485575872 = _static_4418309904

                    # <Value 'isManager' (97:36)> -> __condition
                    __token = 5557
                    try:
                        __zt_tmp = __attrs_4485575872
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4417553984('path', 'isManager', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div>\n                   ')

                        # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4485564256
                        __attrs_4485564256 = _static_4418309904

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append('<p>')
                        __stream_4485564400 = []
                        __append_4485564400 = __stream_4485564400.append
                        __append_4485564400('\n                   Here is the full error message:\n                   ')
                        __msgid_4485564400 = __re_whitespace(''.join(__stream_4485564400)).strip()
                        if 'description_site_admin_full_error':
                            __append(translate('description_site_admin_full_error', mapping=None, default=__msgid_4485564400, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</p>\n\n                   ')

                        # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4485573328
                        __attrs_4485573328 = _static_4418309904

                        # <pre ... (0:0)
                        # --------------------------------------------------------
                        __append('<pre>')

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4485575824
                        __default_4485575824 = _DEFAULT_MARKER

                        # <Value 'err_tb' (102:37)> -> __cache_4485569728
                        __token = 5756
                        try:
                            __zt_tmp = __attrs_4485573328
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4485569728 = _static_4417553984('path', 'err_tb', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))

                        # <BinOp left=<Value 'err_tb' (102:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107619600> at 10b5c55d0> -> __condition
                        __expression = __cache_4485569728

                        # <Symbol value=<DEFAULT> at 107619600> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4485569728
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</pre>\n                </div>')
                    __append('\n\n                ')

                    # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4485567520
                    __attrs_4485567520 = _static_4418309904

                    # <Value 'not:isManager' (105:40)> -> __condition
                    __token = 5830
                    try:
                        __zt_tmp = __attrs_4485567520
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4417553984('not', 'isManager', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    if __condition:
                        __append('\n                    ')

                        # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4485571504
                        __attrs_4485571504 = _static_4418309904

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append('<p>')
                        __stream_4469625504_site_admin = ''
                        __stream_4485570832 = []
                        __append_4485570832 = __stream_4485570832.append
                        __append_4485570832('\n                    If you are certain you have the correct web address but are encountering an error, please\n                    contact the ')
                        __stream_4469625504_site_admin = []
                        __append_4469625504_site_admin = __stream_4469625504_site_admin.append

                        # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4480087808
                        __attrs_4480087808 = _static_4418309904

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append_4469625504_site_admin('<span>\n                    ')

                        # <Static value=<ast.Dict object at 0x10b08b730> name=None at 10b08b8b0> -> __attrs_4480077584
                        __attrs_4480077584 = _static_4480087856

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append_4469625504_site_admin('<a')

                        # <Symbol value=<DEFAULT> at 107619600> -> __default_4480086032
                        __default_4480086032 = _DEFAULT_MARKER

                        # <Substitution 'string:${context/portal_url}/contact-info' (111:44)> -> __attr_href
                        __token = 6231
                        try:
                            __zt_tmp = __attrs_4480077584
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4417553984('string', '${context/portal_url}/contact-info', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append_4469625504_site_admin((' href="%s"' % __attr_href))
                        __append_4469625504_site_admin('>')
                        __stream_4480073840 = []
                        __append_4480073840 = __stream_4480073840.append
                        __append_4480073840('site administration')
                        __msgid_4480073840 = __re_whitespace(''.join(__stream_4480073840)).strip()
                        if 'label_site_admin':
                            __append_4469625504_site_admin(translate('label_site_admin', mapping=None, default=__msgid_4480073840, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append_4469625504_site_admin('</a></span>')
                        __append_4485570832('${site_admin}')
                        __stream_4469625504_site_admin = ''.join(__stream_4469625504_site_admin)
                        __append_4485570832('.\n                    ')
                        __msgid_4485570832 = __re_whitespace(''.join(__stream_4485570832)).strip()
                        if 'description_site_error_mail_site_admin':
                            __append(translate('description_site_error_mail_site_admin', mapping={'site_admin': __stream_4469625504_site_admin, }, default=__msgid_4485570832, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</p>\n                ')
                    __append('\n            </div>\n\n        ')
                if (__backup_isManager_4480406224 is __marker):
                    del econtext['isManager']
                else:
                    econtext['isManager'] = __backup_isManager_4480406224
                __append('\n\n')
                if (__backup_err_log_id_4480132256 is __marker):
                    del econtext['err_log_id']
                else:
                    econtext['err_log_id'] = __backup_err_log_id_4480132256
                if (__backup_err_tb_4480350720 is __marker):
                    del econtext['err_tb']
                else:
                    econtext['err_tb'] = __backup_err_tb_4480350720
                if (__backup_err_type_4480349952 is __marker):
                    del econtext['err_type']
                else:
                    econtext['err_type'] = __backup_err_type_4480349952
            _slots = econtext['__slot_main'] = _deque((__fill_main, ))

            # <Value 'context/@@main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_4480344816
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4417553984('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4484835968 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4484835968
            __i18n_domain = __previous_i18n_domain_4480339392
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }