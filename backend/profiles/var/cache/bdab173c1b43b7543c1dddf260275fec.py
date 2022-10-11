# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/Products/CMFPlone/controlpanel/browser/usergroups_usersoverview.pt'

__tokens = {413: ('string:@@usergroup-userprefs', 12, 28), 466: (" python:request.get('showAll', '') and not view.newSearch and 'y", 13, 23), 553: ("h python:modules['Products.CMFPlone'].Bat", 14, 20), 619: ("rt python:0 if showAll or view.newSearch else request.get('b_start'", 15, 21), 710: ('ize python:showAll and len(view.searchResults) o', 16, 19), 788: ('oles view/portal_', 17, 24), 833: ('l_url context/port', 18, 21), 1017: ('context/global_statusmessage/macros/portal_message', 27, 30), 1017: ('context/global_statusmessage/macros/portal_message', 27, 30), 1346: ("python:icons.tag('people', tag_alt='Inherited from Group')", 33, 92), 1601: ('view/show_users_listing_warning', 41, 26), 2229: ("python:'form.button.FindAll' in request.keys()", 54, 34), 2315: (' view/searchResult', 55, 38), 2366: ('h python:Batch(portal_users, b_size, int(b_start), orphan=', 56, 30), 2465: ("ys python:['searchstring','_authenticato", 57, 37), 2543: ('ers view/many_u', 58, 33), 2162: ('string:$portal_url/$template_id', 53, 37), 2780: ('{\n                "actionOptions": {\n                  "redirectOnResponse": true,\n                  "redirectToUrl": "${portal_url}/@@usergroup-userprefs"\n                }\n              }', 64, 35), 2901: ('portal_url', 67, 38), 3005: ('string:${portal_url}/@@new-user', 70, 34), 3494: ('view/searchString', 79, 40), 4135: ('not:many_users', 95, 33), 4352: ('portal_users', 99, 36), 4547: ('portal_roles', 102, 61), 4579: ('portal_role', 102, 93), 4973: ('batch', 108, 41), 5024: ('repeat/user/odd', 109, 43), 5083: (' user/useri', 110, 42), 5141: ('y python:view.makeQuery(userid=useri', 111, 44), 5228: ("python:oddrow and 'odd' or 'even'", 112, 46), 5423: ('string:$portal_url/@@user-information?${userquery}', 116, 52), 5527: (' useri', 117, 52), 5569: ('${user/fullname}', 118, 32), 5571: ('user/fullname', 118, 34), 5611: ('(${user/login})', 118, 74), 5614: ('user/login', 118, 77), 5762: ('userid', 120, 95), 5908: ('portal_roles', 124, 52), 5982: ("python:user['roles'][portal_role]['inherited']", 125, 59), 6087: (" python:user['roles'][portal_role]['explicit'", 126, 57), 6190: ("d python:user['roles'][portal_role]['canAssign", 127, 55), 6512: ('not:inherited', 132, 50), 6584: ('portal_role', 133, 57), 6643: (" python:'checked' if explicit else nothin", 134, 46), 6733: ("d python:default if enabled else 'disable", 135, 46), 6998: ('python:inherited', 139, 50), 7073: ('portal_role', 140, 57), 7142: ('inherited', 141, 53), 7176: ("python:icons.tag('people', tag_alt='Inherited from Group')", 141, 87), 7642: ('userid', 152, 55), 7704: (' string:Reset password of user ${user/fullname', 153, 54), 7809: ("d python:user['can_set_password'] and default or 'disable", 154, 56), 8257: ('userid', 162, 63), 8327: (' string:Remove user ${user/fullname', 163, 62), 8429: ("d python:user['can_delete'] and default or 'disable", 164, 64), 8610: ('not:batch', 168, 37), 8663: ('view/searchString', 169, 41), 8857: ('not:view/searchString', 172, 48), 8924: ('many_users', 173, 43), 9257: ('not:many_users', 179, 43), 9716: ('context/batch_macros/macros/navigation', 190, 32), 9716: ('context/batch_macros/macros/navigation', 190, 32), 9901: ("python:modules['ZTUtils'].make_query", 194, 30), 9970: (' batchformkeys|nothin', 195, 31), 10030: ('s python:keys and dict([(key, request.form[key]) for key in keys if key in request]) or request.fo', 196, 36), 10160: ('rl batch_base_url | string:${context/absolute_url}/${template_', 197, 28), 9834: ('python:batch.next or batch.previous', 193, 30), 10266: ("python: '%s?%s' % (url, mq( linkparams, {'showAll':'y'} ))", 198, 38), 10581: ('b_start', 205, 39), 10687: ('showAll', 208, 39), 10729: ('batch', 210, 30), 11096: ('context/@@authenticator/authenticator', 222, 40), 261: ('context/prefs_main_template/macros/master', 6, 23), 261: ('context/prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4900531328 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'form.button.Modify', 'value': 'Save', }
_static_4900524512 = {'class': 'btn-group', }
_static_4900534784 = {'type': 'hidden', 'value': '', 'name': 'showAll', }
_static_4900522544 = {'type': 'hidden', 'value': 'b_start', 'name': 'b_start', }
_static_4897681136 = {'href': "python: '%s?%s' % (url, mq( linkparams, {'showAll':'y'} ))", }
_static_4897678592 = {'class': 'showAllSearchResults', }
_static_4906186400 = 'navigation'
_static_4906176752 = {'class': 'discreet', 'style': 'text-align:center; font-size: 100%;', }
_static_4906172672 = {'class': 'discreet', 'style': 'text-align:center; font-size: 100%;', }
_static_4906184144 = {'style': 'text-align:center;', }
_static_4906181600 = {'type': 'checkbox', 'class': 'noborder notify', 'name': 'delete:list', 'value': '', 'title': 'string:Remove user ${user/fullname}', 'disabled': "python:user['can_delete'] and default or 'disabled'", }
_static_4906186640 = {'class': 'listingCheckbox table-danger', }
_static_4906182272 = {'type': 'checkbox', 'class': 'noborder', 'name': 'users.resetpassword:records', 'value': '', 'title': 'string:Reset password of user ${user/fullname}', 'disabled': "python:user['can_set_password'] and default or 'disabled'", }
_static_4906093344 = {'class': 'listingCheckbox table-warning', }
_static_4906091616 = {'type': 'hidden', 'name': 'users.roles:list:records', 'value': 'Manager', }
_static_4906092672 = {'type': 'checkbox', 'class': 'noborder', 'name': 'users.roles:list:records', 'value': 'Manager', 'checked': "python:'checked' if explicit else nothing", 'disabled': "python:default if enabled else 'disabled'", }
_static_4906104480 = {'class': 'listingCheckbox', }
_static_4906102368 = {'type': 'hidden', 'name': 'users.id:records', 'value': 'userid', }
_static_4906098960 = {'class': 'text-muted', }
_static_4905393104 = {'href': '@@user-i0nformation', 'title': 'userid', }
_static_4905392960 = {'class': 'text-start', }
_static_4905397856 = {'class': "python:oddrow and 'odd' or 'even'", }
_static_4907237728 = {'class': 'rotate table-danger', }
_static_4907237680 = {'class': 'rotate table-warning', }
_static_4907245696 = {'class': 'rotate', }
_static_4907243920 = {'class': 'text-start', }
_static_4907252704 = {'class': 'table table-responsive table-bordered table-striped text-center', 'summary': 'User Listing', }
_static_4907245984 = {'type': 'submit', 'class': 'searchButton btn btn-secondary', 'name': 'form.button.FindAll', 'value': 'Show all', }
_static_4905750816 = {'type': 'submit', 'class': 'searchButton btn btn-primary', 'name': 'form.button.Search', 'value': 'Search', }
_static_4905748560 = {'class': 'form-control quickSearch', 'id': 'quickSearch', 'aria-labelledby': 'quickSearchLabel', 'type': 'text', 'name': 'searchstring', 'value': '', }
_static_4905747696 = {'class': 'input-group-text', 'id': 'quickSearchLabel', }
_static_4905759312 = {'class': 'pat-plone-modal me-3 btn btn-success ', 'id': 'add-user', 'data-pat-plone-modal': '{\n                "actionOptions": {\n                  "redirectOnResponse": true,\n                  "redirectToUrl": "${portal_url}/@@usergroup-userprefs"\n                }\n              }', 'href': 'string:${portal_url}/@@new-user', }
_static_4905752112 = {'class': 'mb-3 input-group', }
_static_4905758496 = {'type': 'hidden', 'name': 'form.submitted', 'value': '1', }
_static_4906812512 = {'action': '', 'class': 'pat-formautofocus', 'name': 'users_search', 'method': 'post', }
_static_4906814720 = {'class': 'alert alert-warn', 'role': 'status', }
_static_4906819952 = {'class': 'autotabs', }
_static_4906818416 = {'id': 'content-core', }
_static_4906823216 = {'class': 'text-muted mt-2', }
_static_4906827584 = 'portal_message'
_static_4906824512 = {'class': 'documentFirstHeading', }
_static_4906824368 = {'id': 'content', }
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
_static_4907341696 = 'master'
_static_4428767312 = {}

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

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4907340592
            __attrs_4907340592 = _static_4428767312
            __previous_i18n_domain_4907341936 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4906666240 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x124801780> name=None at 1248018a0> -> __value
            __value = _static_4907341696
            econtext['macroname'] = __value

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4907350288
                __attrs_4907350288 = _static_4428767312
                __backup_template_id_4900964336 = get('template_id', __marker)

                # <Value 'string:@@usergroup-userprefs' (12:28)> -> __value
                __token = 413
                try:
                    __zt_tmp = __attrs_4907350288
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('string', '@@usergroup-userprefs', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['template_id'] = __value
                __backup_showAll_4900473104 = get('showAll', __marker)

                # <Value "python:request.get('showAll', '') and not view.newSearch and 'y'" (13:23)> -> __value
                __token = 466
                try:
                    __zt_tmp = __attrs_4907350288
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', "request.get('showAll', '') and not view.newSearch and 'y'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['showAll'] = __value
                __backup_Batch_4900474160 = get('Batch', __marker)

                # <Value "python:modules['Products.CMFPlone'].Batch" (14:20)> -> __value
                __token = 553
                try:
                    __zt_tmp = __attrs_4907350288
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', "modules['Products.CMFPlone'].Batch", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['Batch'] = __value
                __backup_b_start_4900481936 = get('b_start', __marker)

                # <Value "python:0 if showAll or view.newSearch else request.get('b_start',0)" (15:21)> -> __value
                __token = 619
                try:
                    __zt_tmp = __attrs_4907350288
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', "0 if showAll or view.newSearch else request.get('b_start',0)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['b_start'] = __value
                __backup_b_size_4900728944 = get('b_size', __marker)

                # <Value 'python:showAll and len(view.searchResults) or 20' (16:19)> -> __value
                __token = 710
                try:
                    __zt_tmp = __attrs_4907350288
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'showAll and len(view.searchResults) or 20', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['b_size'] = __value
                __backup_portal_roles_4900719872 = get('portal_roles', __marker)

                # <Value 'view/portal_roles' (17:24)> -> __value
                __token = 788
                try:
                    __zt_tmp = __attrs_4907350288
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'view/portal_roles', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['portal_roles'] = __value
                __backup_portal_url_4900719344 = get('portal_url', __marker)

                # <Value 'context/portal_url' (18:21)> -> __value
                __token = 833
                try:
                    __zt_tmp = __attrs_4907350288
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'context/portal_url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['portal_url'] = __value
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x1247832b0> name=None at 124782560> -> __attrs_4906819856
                __attrs_4906819856 = _static_4906824368

                # <article ... (0:0)
                # --------------------------------------------------------
                __append('<article id="content">\n\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4906818512
                __attrs_4906818512 = _static_4428767312

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n\n        ')

                # <Static value=<ast.Dict object at 0x124783340> name=None at 124780550> -> __attrs_4906826864
                __attrs_4906826864 = _static_4906824512

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">')
                __stream_4906824704 = []
                __append_4906824704 = __stream_4906824704.append
                __append_4906824704('Users')
                __msgid_4906824704 = __re_whitespace(''.join(__stream_4906824704)).strip()
                if __msgid_4906824704:
                    __append(translate(__msgid_4906824704, mapping=None, default=__msgid_4906824704, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n\n        ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4906827200
                __attrs_4906827200 = _static_4428767312
                __backup_macroname_4906205376 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x124783f40> name=None at 1247833a0> -> __value
                __value = _static_4906827584
                econtext['macroname'] = __value

                # <Value 'context/global_statusmessage/macros/portal_message' (27:30)> -> __macro
                __token = 1017
                try:
                    __zt_tmp = __attrs_4906827200
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_4427992992('path', 'context/global_statusmessage/macros/portal_message', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __token = 1017
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_4906205376 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_4906205376
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x124782e30> name=None at 124782770> -> __attrs_4906822976
                __attrs_4906822976 = _static_4906823216

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="text-muted mt-2">')
                __stream_4906733344_image_link_icon = ''
                __stream_4906827008 = []
                __append_4906827008 = __stream_4906827008.append
                __append_4906827008('\n              Note that roles set here apply directly to a user.\n              The symbol ')
                __stream_4906733344_image_link_icon = []
                __append_4906733344_image_link_icon = __stream_4906733344_image_link_icon.append

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4906822160
                __attrs_4906822160 = _static_4428767312

                # <span ... (0:0)
                # --------------------------------------------------------
                __append_4906733344_image_link_icon('<span>')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4906818128
                __attrs_4906818128 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906811792
                __default_4906811792 = _DEFAULT_MARKER

                # <Value "python:icons.tag('people', tag_alt='Inherited from Group')" (33:92)> -> __cache_4906816976
                __token = 1346
                try:
                    __zt_tmp = __attrs_4906818128
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4906816976 = _static_4427992992('python', "icons.tag('people', tag_alt='Inherited from Group')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('people', tag_alt='Inherited from Group')" (33:92)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1247802b0> -> __condition
                __expression = __cache_4906816976

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4906816976
                    __content = __convert(__content)
                    if (__content is not None):
                        __append_4906733344_image_link_icon(__content)
                __append_4906733344_image_link_icon('</span>')
                __append_4906827008('${image_link_icon}')
                __stream_4906733344_image_link_icon = ''.join(__stream_4906733344_image_link_icon)
                __append_4906827008('\n              indicates a role inherited from membership in a group.\n        ')
                __msgid_4906827008 = __re_whitespace(''.join(__stream_4906827008)).strip()
                if 'user_roles_note':
                    __append(translate('user_roles_note', mapping={'image_link_icon': __stream_4906733344_image_link_icon, }, default=__msgid_4906827008, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</div>\n      </header>\n\n    ')

                # <Static value=<ast.Dict object at 0x124781b70> name=None at 124782290> -> __attrs_4906822640
                __attrs_4906822640 = _static_4906818416

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n\n      ')

                # <Static value=<ast.Dict object at 0x124782170> name=None at 1247821d0> -> __attrs_4906820528
                __attrs_4906820528 = _static_4906819952

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="autotabs">\n        ')

                # <Static value=<ast.Dict object at 0x124780d00> name=None at 124781210> -> __attrs_4906814768
                __attrs_4906814768 = _static_4906814720

                # <Value 'view/show_users_listing_warning' (41:26)> -> __condition
                __token = 1601
                try:
                    __zt_tmp = __attrs_4906814768
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'view/show_users_listing_warning', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="alert alert-warn" role="status">\n          ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4906814192
                    __attrs_4906814192 = _static_4428767312

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_4906818224 = []
                    __append_4906818224 = __stream_4906818224.append
                    __append_4906818224('Note')
                    __msgid_4906818224 = __re_whitespace(''.join(__stream_4906818224)).strip()
                    if __msgid_4906818224:
                        __append(translate(__msgid_4906818224, mapping=None, default=__msgid_4906818224, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n          ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4906823984
                    __attrs_4906823984 = _static_4428767312

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_4906812848 = []
                    __append_4906812848 = __stream_4906812848.append
                    __append_4906812848('Some or all of your PAS user source\n          plugins do not allow listing of users, so you may not see\n          the users defined by those plugins unless doing a specific\n          search.')
                    __msgid_4906812848 = __re_whitespace(''.join(__stream_4906812848)).strip()
                    if 'description_pas_users_listing':
                        __append(translate('description_pas_users_listing', mapping=None, default=__msgid_4906812848, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n        </p>')
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x124780460> name=None at 1247804f0> -> __attrs_4905762240
                __attrs_4905762240 = _static_4906812512
                __backup_findAll_4900485872 = get('findAll', __marker)

                # <Value "python:'form.button.FindAll' in request.keys()" (54:34)> -> __value
                __token = 2229
                try:
                    __zt_tmp = __attrs_4905762240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', "'form.button.FindAll' in request.keys()", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['findAll'] = __value
                __backup_portal_users_4900484528 = get('portal_users', __marker)

                # <Value 'view/searchResults' (55:38)> -> __value
                __token = 2315
                try:
                    __zt_tmp = __attrs_4905762240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'view/searchResults', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['portal_users'] = __value
                __backup_batch_4900204464 = get('batch', __marker)

                # <Value 'python:Batch(portal_users, b_size, int(b_start), orphan=1)' (56:30)> -> __value
                __token = 2366
                try:
                    __zt_tmp = __attrs_4905762240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'Batch(portal_users, b_size, int(b_start), orphan=1)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['batch'] = __value
                __backup_batchformkeys_4900195344 = get('batchformkeys', __marker)

                # <Value "python:['searchstring','_authenticator']" (57:37)> -> __value
                __token = 2465
                try:
                    __zt_tmp = __attrs_4905762240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', "['searchstring','_authenticator']", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['batchformkeys'] = __value
                __backup_many_users_4900204176 = get('many_users', __marker)

                # <Value 'view/many_users' (58:33)> -> __value
                __token = 2543
                try:
                    __zt_tmp = __attrs_4905762240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'view/many_users', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['many_users'] = __value

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906824944
                __default_4906824944 = _DEFAULT_MARKER

                # <Substitution 'string:$portal_url/$template_id' (53:37)> -> __attr_action
                __token = 2162
                try:
                    __zt_tmp = __attrs_4905762240
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_action = _static_4427992992('string', '$portal_url/$template_id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                if (__attr_action is not None):
                    __append((' action="%s"' % __attr_action))
                __append(' class="pat-formautofocus" name="users_search" method="post">\n          ')

                # <Static value=<ast.Dict object at 0x12467ef20> name=None at 12467e2f0> -> __attrs_4905747936
                __attrs_4905747936 = _static_4905758496

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="form.submitted" value="1" />\n\n\n        ')

                # <Static value=<ast.Dict object at 0x12467d630> name=None at 12467e3b0> -> __attrs_4905757680
                __attrs_4905757680 = _static_4905752112

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="mb-3 input-group">\n          ')

                # <Static value=<ast.Dict object at 0x12467f250> name=None at 12467e0b0> -> __attrs_4905754752
                __attrs_4905754752 = _static_4905759312

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="pat-plone-modal me-3 btn btn-success " id="add-user"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4905747120
                __default_4905747120 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '{\n                "actionOptions": {\n                  "redirectOnResponse": true,\n                  "redirectToUrl": "${portal_url}/@@usergroup-userprefs"\n                }\n              }' (64:35)> braces_required=True translation=False default='"?"' default_marker='"?"' at 12467e380> -> __attr_data_pat_plone_modal
                __token = 2780
                __token = 2901
                try:
                    __zt_tmp = __attrs_4905754752
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_pat_plone_modal = _static_4427992992('path', 'portal_url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_data_pat_plone_modal = __quote(__attr_data_pat_plone_modal, "'", '&#39;', None, _DEFAULT_MARKER)
                __attr_data_pat_plone_modal = ('%s%s%s' % ('{\n                "actionOptions": {\n                  "redirectOnResponse": true,\n                  "redirectToUrl": "', (__attr_data_pat_plone_modal if (__attr_data_pat_plone_modal is not None) else ''), '/@@usergroup-userprefs"\n                }\n              }', ))
                if (__attr_data_pat_plone_modal is None):
                    pass
                else:
                    if (__attr_data_pat_plone_modal is _DEFAULT_MARKER):
                        __attr_data_pat_plone_modal = None
                    else:
                        __tt = type(__attr_data_pat_plone_modal)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __attr_data_pat_plone_modal = str(__attr_data_pat_plone_modal)
                        else:
                            if (__tt is bytes):
                                __attr_data_pat_plone_modal = decode(__attr_data_pat_plone_modal)
                            else:
                                if (__tt is not str):
                                    try:
                                        __attr_data_pat_plone_modal = __attr_data_pat_plone_modal.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__attr_data_pat_plone_modal)
                                        __attr_data_pat_plone_modal = (str(__attr_data_pat_plone_modal) if (__attr_data_pat_plone_modal is __converted) else __converted)
                                    else:
                                        __attr_data_pat_plone_modal = __attr_data_pat_plone_modal()
                if (__attr_data_pat_plone_modal is not None):
                    __append((" data-pat-plone-modal='%s'" % __attr_data_pat_plone_modal))

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4905751200
                __default_4905751200 = _DEFAULT_MARKER

                # <Substitution 'string:${portal_url}/@@new-user' (70:34)> -> __attr_href
                __token = 3005
                try:
                    __zt_tmp = __attrs_4905754752
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4427992992('string', '${portal_url}/@@new-user', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append('>')
                __stream_4905747984 = []
                __append_4905747984 = __stream_4905747984.append
                __append_4905747984('Add New User')
                __msgid_4905747984 = __re_whitespace(''.join(__stream_4905747984)).strip()
                if 'label_add_new_user':
                    __append(translate('label_add_new_user', mapping=None, default=__msgid_4905747984, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</a>\n          ')

                # <Static value=<ast.Dict object at 0x12467c4f0> name=None at 12467c070> -> __attrs_4905759696
                __attrs_4905759696 = _static_4905747696

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span class="input-group-text" id="quickSearchLabel">')
                __stream_4905760272 = []
                __append_4905760272 = __stream_4905760272.append
                __append_4905760272('User Search')
                __msgid_4905760272 = __re_whitespace(''.join(__stream_4905760272)).strip()
                if 'label_user_search':
                    __append(translate('label_user_search', mapping=None, default=__msgid_4905760272, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</span>\n          ')

                # <Static value=<ast.Dict object at 0x12467c850> name=None at 12467d450> -> __attrs_4905757632
                __attrs_4905757632 = _static_4905748560

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="form-control quickSearch" id="quickSearch" aria-labelledby="quickSearchLabel" type="text" name="searchstring"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4905753264
                __default_4905753264 = _DEFAULT_MARKER

                # <Substitution 'view/searchString' (79:40)> -> __attr_value
                __token = 3494
                try:
                    __zt_tmp = __attrs_4905757632
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'view/searchString', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n          ')

                # <Static value=<ast.Dict object at 0x12467d120> name=None at 12467e830> -> __attrs_4905748224
                __attrs_4905748224 = _static_4905750816

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button type="submit" class="searchButton btn btn-primary" name="form.button.Search"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4905753024
                __default_4905753024 = _DEFAULT_MARKER

                # <Translate msgid='label_search' node=<ast.Constant object at 0x12467c400> at 12467d690> -> __attr_value
                __attr_value = 'Search'
                __attr_value = translate('label_search', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' >')
                __stream_4905760848 = []
                __append_4905760848 = __stream_4905760848.append
                __append_4905760848('Search')
                __msgid_4905760848 = __re_whitespace(''.join(__stream_4905760848)).strip()
                if __msgid_4905760848:
                    __append(translate(__msgid_4905760848, mapping=None, default=__msgid_4905760848, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</button>\n\n          ')

                # <Static value=<ast.Dict object at 0x1247ea1a0> name=None at 12467fe20> -> __attrs_4907249776
                __attrs_4907249776 = _static_4907245984

                # <Value 'not:many_users' (95:33)> -> __condition
                __token = 4135
                try:
                    __zt_tmp = __attrs_4907249776
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('not', 'many_users', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button type="submit" class="searchButton btn btn-secondary" name="form.button.FindAll"')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4907248912
                    __default_4907248912 = _DEFAULT_MARKER

                    # <Translate msgid='label_showall' node=<ast.Constant object at 0x1247e8580> at 1247eb100> -> __attr_value
                    __attr_value = 'Show all'
                    __attr_value = translate('label_showall', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' >')
                    __stream_4905756672 = []
                    __append_4905756672 = __stream_4905756672.append
                    __append_4905756672('Show all')
                    __msgid_4905756672 = __re_whitespace(''.join(__stream_4905756672)).strip()
                    if 'label_showall':
                        __append(translate('label_showall', mapping=None, default=__msgid_4905756672, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>')
                __append('\n        </div>\n          ')

                # <Static value=<ast.Dict object at 0x1247ebbe0> name=None at 1247ebb50> -> __attrs_4907252992
                __attrs_4907252992 = _static_4907252704

                # <table ... (0:0)
                # --------------------------------------------------------
                __append('<table class="table table-responsive table-bordered table-striped text-center" summary="User Listing">\n              ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4907249872
                __attrs_4907249872 = _static_4428767312

                # <Value 'portal_users' (99:36)> -> __condition
                __token = 4352
                try:
                    __zt_tmp = __attrs_4907249872
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'portal_users', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <thead ... (0:0)
                    # --------------------------------------------------------
                    __append('<thead>\n                ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4907244736
                    __attrs_4907244736 = _static_4428767312

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr>\n                  ')

                    # <Static value=<ast.Dict object at 0x1247e9990> name=None at 1247ea950> -> __attrs_4907247664
                    __attrs_4907247664 = _static_4907243920

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th  class="text-start">')
                    __stream_4907246080 = []
                    __append_4907246080 = __stream_4907246080.append
                    __append_4907246080('User name')
                    __msgid_4907246080 = __re_whitespace(''.join(__stream_4907246080)).strip()
                    if 'listingheader_user_name':
                        __append(translate('listingheader_user_name', mapping=None, default=__msgid_4907246080, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</th>\n                  ')

                    # <Static value=<ast.Dict object at 0x1247ea080> name=None at 1247e8fd0> -> __attrs_4907248240
                    __attrs_4907248240 = _static_4907245696
                    __backup_portal_role_4905380512 = get('portal_role', __marker)

                    # <Value 'portal_roles' (102:61)> -> __iterator
                    __token = 4547
                    try:
                        __zt_tmp = __attrs_4907248240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_4427992992('path', 'portal_roles', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    (__iterator, ____index_4907245840, ) = getname('repeat')('portal_role', __iterator)
                    econtext['portal_role'] = None
                    for __item in __iterator:
                        econtext['portal_role'] = __item

                        # <th ... (0:0)
                        # --------------------------------------------------------
                        __append('<th class="rotate">')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4907243488
                        __attrs_4907243488 = _static_4428767312

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div>')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4907243152
                        __default_4907243152 = _DEFAULT_MARKER

                        # <Value 'portal_role' (102:93)> -> __cache_4907238880
                        __token = 4579
                        try:
                            __zt_tmp = __attrs_4907243488
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4907238880 = _static_4427992992('path', 'portal_role', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value 'portal_role' (102:93)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1247e8e80> -> __condition
                        __expression = __cache_4907238880

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Role')
                        else:
                            __content = __cache_4907238880
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</div></th>')
                        ____index_4907245840 -= 1
                        if (____index_4907245840 > 0):
                            __append('\n                  ')
                    if (__backup_portal_role_4905380512 is __marker):
                        del econtext['portal_role']
                    else:
                        econtext['portal_role'] = __backup_portal_role_4905380512
                    __append('\n                  ')

                    # <Static value=<ast.Dict object at 0x1247e8130> name=None at 1247e9630> -> __attrs_4907242432
                    __attrs_4907242432 = _static_4907237680

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th class="rotate table-warning">')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4907240704
                    __attrs_4907240704 = _static_4428767312

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div>')
                    __stream_4907242672 = []
                    __append_4907242672 = __stream_4907242672.append
                    __append_4907242672('Reset Password')
                    __msgid_4907242672 = __re_whitespace(''.join(__stream_4907242672)).strip()
                    if 'listingheader_reset_password':
                        __append(translate('listingheader_reset_password', mapping=None, default=__msgid_4907242672, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</div></th>\n                  ')

                    # <Static value=<ast.Dict object at 0x1247e8160> name=None at 1247e8a90> -> __attrs_4907238112
                    __attrs_4907238112 = _static_4907237728

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th class="rotate table-danger">')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4907237920
                    __attrs_4907237920 = _static_4428767312

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div>')
                    __stream_4907238928 = []
                    __append_4907238928 = __stream_4907238928.append
                    __append_4907238928('Remove')
                    __msgid_4907238928 = __re_whitespace(''.join(__stream_4907238928)).strip()
                    if 'listingheader_remove':
                        __append(translate('listingheader_remove', mapping=None, default=__msgid_4907238928, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</div></th>\n                </tr>\n              </thead>')
                __append('\n              ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4907241184
                __attrs_4907241184 = _static_4428767312

                # <tbody ... (0:0)
                # --------------------------------------------------------
                __append('<tbody>\n                  ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4907250304
                __attrs_4907250304 = _static_4428767312
                __backup_user_4900634192 = get('user', __marker)

                # <Value 'batch' (108:41)> -> __iterator
                __token = 4973
                try:
                    __zt_tmp = __attrs_4907250304
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4427992992('path', 'batch', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                (__iterator, ____index_4907250688, ) = getname('repeat')('user', __iterator)
                econtext['user'] = None
                for __item in __iterator:
                    econtext['user'] = __item
                    __append('\n                    ')

                    # <Static value=<ast.Dict object at 0x124626e60> name=None at 124627ca0> -> __attrs_4905390608
                    __attrs_4905390608 = _static_4905397856
                    __backup_oddrow_4900626944 = get('oddrow', __marker)

                    # <Value 'repeat/user/odd' (109:43)> -> __value
                    __token = 5024
                    try:
                        __zt_tmp = __attrs_4905390608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4427992992('path', 'repeat/user/odd', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    econtext['oddrow'] = __value
                    __backup_userid_4905380752 = get('userid', __marker)

                    # <Value 'user/userid' (110:42)> -> __value
                    __token = 5083
                    try:
                        __zt_tmp = __attrs_4905390608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4427992992('path', 'user/userid', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    econtext['userid'] = __value
                    __backup_userquery_4905372592 = get('userquery', __marker)

                    # <Value 'python:view.makeQuery(userid=userid)' (111:44)> -> __value
                    __token = 5141
                    try:
                        __zt_tmp = __attrs_4905390608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4427992992('python', 'view.makeQuery(userid=userid)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    econtext['userquery'] = __value

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4905397424
                    __default_4905397424 = _DEFAULT_MARKER

                    # <Substitution "python:oddrow and 'odd' or 'even'" (112:46)> -> __attr_class
                    __token = 5228
                    try:
                        __zt_tmp = __attrs_4905390608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4427992992('python', "oddrow and 'odd' or 'even'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n\n                        ')

                    # <Static value=<ast.Dict object at 0x124625b40> name=None at 1246265c0> -> __attrs_4905392336
                    __attrs_4905392336 = _static_4905392960

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td class="text-start">\n                            ')

                    # <Static value=<ast.Dict object at 0x124625bd0> name=None at 124625ed0> -> __attrs_4906094496
                    __attrs_4906094496 = _static_4905393104

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4905394064
                    __default_4905394064 = _DEFAULT_MARKER

                    # <Substitution 'string:$portal_url/@@user-information?${userquery}' (116:52)> -> __attr_href
                    __token = 5423
                    try:
                        __zt_tmp = __attrs_4906094496
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4427992992('string', '$portal_url/@@user-information?${userquery}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '@@user-i0nformation', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906102992
                    __default_4906102992 = _DEFAULT_MARKER

                    # <Substitution 'userid' (117:52)> -> __attr_title
                    __token = 5527
                    try:
                        __zt_tmp = __attrs_4906094496
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_4427992992('path', 'userid', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append('>')

                    # <Interpolation value=<Substitution '\n                                ${user/fullname} ' (117:61)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1246d21a0> -> __content_4353737008
                    __token = 5569
                    __token = 5571
                    try:
                        __zt_tmp = __attrs_4906094496
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_4353737008 = _static_4427992992('path', 'user/fullname', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __content_4353737008 = __quote(__content_4353737008, '\x00', '&#0;', None, None)
                    __content_4353737008 = ('%s%s%s' % ('\n                                ', (__content_4353737008 if (__content_4353737008 is not None) else ''), ' ', ))
                    if (__content_4353737008 is None):
                        pass
                    else:
                        if (__content_4353737008 is None):
                            __content_4353737008 = None
                        else:
                            __tt = type(__content_4353737008)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_4353737008 = str(__content_4353737008)
                            else:
                                if (__tt is bytes):
                                    __content_4353737008 = decode(__content_4353737008)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_4353737008 = __content_4353737008.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_4353737008)
                                            __content_4353737008 = (str(__content_4353737008) if (__content_4353737008 is __converted) else __converted)
                                        else:
                                            __content_4353737008 = __content_4353737008()
                    if (__content_4353737008 is not None):
                        __append(__content_4353737008)

                    # <Static value=<ast.Dict object at 0x1246d2110> name=None at 1246d3490> -> __attrs_4906091184
                    __attrs_4906091184 = _static_4906098960

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="text-muted">')

                    # <Interpolation value=<Substitution '(${user/login})' (118:74)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1246d0e80> -> __content_4353737008
                    __token = 5611
                    __token = 5614
                    try:
                        __zt_tmp = __attrs_4906091184
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_4353737008 = _static_4427992992('path', 'user/login', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __content_4353737008 = __quote(__content_4353737008, '\x00', '&#0;', None, None)
                    __content_4353737008 = ('%s%s%s' % ('(', (__content_4353737008 if (__content_4353737008 is not None) else ''), ')', ))
                    if (__content_4353737008 is None):
                        pass
                    else:
                        if (__content_4353737008 is None):
                            __content_4353737008 = None
                        else:
                            __tt = type(__content_4353737008)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_4353737008 = str(__content_4353737008)
                            else:
                                if (__tt is bytes):
                                    __content_4353737008 = decode(__content_4353737008)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_4353737008 = __content_4353737008.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_4353737008)
                                            __content_4353737008 = (str(__content_4353737008) if (__content_4353737008 is __converted) else __converted)
                                        else:
                                            __content_4353737008 = __content_4353737008()
                    if (__content_4353737008 is not None):
                        __append(__content_4353737008)
                    __append('</span>\n                            </a>\n                            ')

                    # <Static value=<ast.Dict object at 0x1246d2e60> name=None at 1246d3910> -> __attrs_4906099200
                    __attrs_4906099200 = _static_4906102368

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="hidden" name="users.id:records"')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906096368
                    __default_4906096368 = _DEFAULT_MARKER

                    # <Substitution 'userid' (120:95)> -> __attr_value
                    __token = 5762
                    try:
                        __zt_tmp = __attrs_4906099200
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_4427992992('path', 'userid', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n                        </td>\n\n                        ')

                    # <Static value=<ast.Dict object at 0x1246d36a0> name=None at 1246d3430> -> __attrs_4906097712
                    __attrs_4906097712 = _static_4906104480
                    __backup_portal_role_4900352208 = get('portal_role', __marker)

                    # <Value 'portal_roles' (124:52)> -> __iterator
                    __token = 5908
                    try:
                        __zt_tmp = __attrs_4906097712
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_4427992992('path', 'portal_roles', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    (__iterator, ____index_4906100112, ) = getname('repeat')('portal_role', __iterator)
                    econtext['portal_role'] = None
                    for __item in __iterator:
                        econtext['portal_role'] = __item

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="listingCheckbox">\n                          ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4906103904
                        __attrs_4906103904 = _static_4428767312
                        __backup_inherited_4900973312 = get('inherited', __marker)

                        # <Value "python:user['roles'][portal_role]['inherited']" (125:59)> -> __value
                        __token = 5982
                        try:
                            __zt_tmp = __attrs_4906103904
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4427992992('python', "user['roles'][portal_role]['inherited']", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        econtext['inherited'] = __value
                        __backup_explicit_4900965776 = get('explicit', __marker)

                        # <Value "python:user['roles'][portal_role]['explicit']" (126:57)> -> __value
                        __token = 6087
                        try:
                            __zt_tmp = __attrs_4906103904
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4427992992('python', "user['roles'][portal_role]['explicit']", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        econtext['explicit'] = __value
                        __backup_enabled_4900978304 = get('enabled', __marker)

                        # <Value "python:user['roles'][portal_role]['canAssign']" (127:55)> -> __value
                        __token = 6190
                        try:
                            __zt_tmp = __attrs_4906103904
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4427992992('python', "user['roles'][portal_role]['canAssign']", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        econtext['enabled'] = __value
                        __append('\n                            ')

                        # <Static value=<ast.Dict object at 0x1246d0880> name=None at 1246d1a80> -> __attrs_4906105920
                        __attrs_4906105920 = _static_4906092672

                        # <Value 'not:inherited' (132:50)> -> __condition
                        __token = 6512
                        try:
                            __zt_tmp = __attrs_4906105920
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4427992992('not', 'inherited', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        if __condition:

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input type="checkbox" class="noborder" name="users.roles:list:records"')

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906106688
                            __default_4906106688 = _DEFAULT_MARKER

                            # <Substitution 'portal_role' (133:57)> -> __attr_value
                            __token = 6584
                            try:
                                __zt_tmp = __attrs_4906105920
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_4427992992('path', 'portal_role', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', 'Manager', _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906090896
                            __default_4906090896 = _DEFAULT_MARKER

                            # <Boolean "python:'checked' if explicit else nothing" (134:46)> -> __attr_checked
                            __token = 6643
                            try:
                                __zt_tmp = __attrs_4906105920
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_checked = _static_4427992992('python', "'checked' if explicit else nothing", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                            if (__attr_checked is _DEFAULT_MARKER):
                                __attr_checked = None
                            else:
                                if __attr_checked:
                                    __attr_checked = 'checked'
                                else:
                                    __attr_checked = None
                            if (__attr_checked is not None):
                                __append((' checked="%s"' % __attr_checked))

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906100544
                            __default_4906100544 = _DEFAULT_MARKER

                            # <Boolean "python:default if enabled else 'disabled'" (135:46)> -> __attr_disabled
                            __token = 6733
                            try:
                                __zt_tmp = __attrs_4906105920
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_disabled = _static_4427992992('python', "default if enabled else 'disabled'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                            if (__attr_disabled is _DEFAULT_MARKER):
                                __attr_disabled = None
                            else:
                                if __attr_disabled:
                                    __attr_disabled = 'disabled'
                                else:
                                    __attr_disabled = None
                            if (__attr_disabled is not None):
                                __append((' disabled="%s"' % __attr_disabled))
                            __append(' />')
                        __append('\n                            ')

                        # <Static value=<ast.Dict object at 0x1246d0460> name=None at 1246d1a20> -> __attrs_4906098240
                        __attrs_4906098240 = _static_4906091616

                        # <Value 'python:inherited' (139:50)> -> __condition
                        __token = 6998
                        try:
                            __zt_tmp = __attrs_4906098240
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4427992992('python', 'inherited', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        if __condition:

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input type="hidden" name="users.roles:list:records"')

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906104336
                            __default_4906104336 = _DEFAULT_MARKER

                            # <Substitution 'portal_role' (140:57)> -> __attr_value
                            __token = 7073
                            try:
                                __zt_tmp = __attrs_4906098240
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_4427992992('path', 'portal_role', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', 'Manager', _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))
                            __append(' />')
                        __append('\n                            ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4906100976
                        __attrs_4906100976 = _static_4428767312

                        # <Value 'inherited' (141:53)> -> __condition
                        __token = 7142
                        try:
                            __zt_tmp = __attrs_4906100976
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4427992992('path', 'inherited', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        if __condition:

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906094976
                            __default_4906094976 = _DEFAULT_MARKER

                            # <Value "python:icons.tag('people', tag_alt='Inherited from Group')" (141:87)> -> __cache_4906106496
                            __token = 7176
                            try:
                                __zt_tmp = __attrs_4906100976
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4906106496 = _static_4427992992('python', "icons.tag('people', tag_alt='Inherited from Group')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                            # <BinOp left=<Value "python:icons.tag('people', tag_alt='Inherited from Group')" (141:87)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1246d0d00> -> __condition
                            __expression = __cache_4906106496

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_4906106496
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                        __append('\n\n                          ')
                        if (__backup_enabled_4900978304 is __marker):
                            del econtext['enabled']
                        else:
                            econtext['enabled'] = __backup_enabled_4900978304
                        if (__backup_explicit_4900965776 is __marker):
                            del econtext['explicit']
                        else:
                            econtext['explicit'] = __backup_explicit_4900965776
                        if (__backup_inherited_4900973312 is __marker):
                            del econtext['inherited']
                        else:
                            econtext['inherited'] = __backup_inherited_4900973312
                        __append('\n\n                        </td>')
                        ____index_4906100112 -= 1
                        if (____index_4906100112 > 0):
                            __append('\n                        ')
                    if (__backup_portal_role_4900352208 is __marker):
                        del econtext['portal_role']
                    else:
                        econtext['portal_role'] = __backup_portal_role_4900352208
                    __append('\n\n                        ')

                    # <Static value=<ast.Dict object at 0x1246d0b20> name=None at 1246d36d0> -> __attrs_4906099440
                    __attrs_4906099440 = _static_4906093344

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td class="listingCheckbox table-warning">\n                          ')

                    # <Static value=<ast.Dict object at 0x1246e6680> name=None at 1246d2410> -> __attrs_4906187168
                    __attrs_4906187168 = _static_4906182272

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="checkbox" class="noborder" name="users.resetpassword:records"')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906184624
                    __default_4906184624 = _DEFAULT_MARKER

                    # <Substitution 'userid' (152:55)> -> __attr_value
                    __token = 7642
                    try:
                        __zt_tmp = __attrs_4906187168
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_4427992992('path', 'userid', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906178672
                    __default_4906178672 = _DEFAULT_MARKER

                    # <Substitution 'string:Reset password of user ${user/fullname}' (153:54)> -> __attr_title
                    __token = 7704
                    try:
                        __zt_tmp = __attrs_4906187168
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_4427992992('string', 'Reset password of user ${user/fullname}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906179776
                    __default_4906179776 = _DEFAULT_MARKER

                    # <Boolean "python:user['can_set_password'] and default or 'disabled'" (154:56)> -> __attr_disabled
                    __token = 7809
                    try:
                        __zt_tmp = __attrs_4906187168
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_disabled = _static_4427992992('python', "user['can_set_password'] and default or 'disabled'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if (__attr_disabled is _DEFAULT_MARKER):
                        __attr_disabled = None
                    else:
                        if __attr_disabled:
                            __attr_disabled = 'disabled'
                        else:
                            __attr_disabled = None
                    if (__attr_disabled is not None):
                        __append((' disabled="%s"' % __attr_disabled))
                    __append(' />\n                        </td>\n\n                        ')

                    # <Static value=<ast.Dict object at 0x1246e7790> name=None at 1246e4ca0> -> __attrs_4906176464
                    __attrs_4906176464 = _static_4906186640

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td class="listingCheckbox table-danger">\n                          ')

                    # <Static value=<ast.Dict object at 0x1246e63e0> name=None at 1246e4220> -> __attrs_4906187408
                    __attrs_4906187408 = _static_4906181600

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="checkbox" class="noborder notify" name="delete:list"')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906175120
                    __default_4906175120 = _DEFAULT_MARKER

                    # <Substitution 'userid' (162:63)> -> __attr_value
                    __token = 8257
                    try:
                        __zt_tmp = __attrs_4906187408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_4427992992('path', 'userid', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906176368
                    __default_4906176368 = _DEFAULT_MARKER

                    # <Substitution 'string:Remove user ${user/fullname}' (163:62)> -> __attr_title
                    __token = 8327
                    try:
                        __zt_tmp = __attrs_4906187408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_4427992992('string', 'Remove user ${user/fullname}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4906188176
                    __default_4906188176 = _DEFAULT_MARKER

                    # <Boolean "python:user['can_delete'] and default or 'disabled'" (164:64)> -> __attr_disabled
                    __token = 8429
                    try:
                        __zt_tmp = __attrs_4906187408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_disabled = _static_4427992992('python', "user['can_delete'] and default or 'disabled'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if (__attr_disabled is _DEFAULT_MARKER):
                        __attr_disabled = None
                    else:
                        if __attr_disabled:
                            __attr_disabled = 'disabled'
                        else:
                            __attr_disabled = None
                    if (__attr_disabled is not None):
                        __append((' disabled="%s"' % __attr_disabled))
                    __append(' />\n                        </td>\n                    </tr>')
                    if (__backup_userquery_4905372592 is __marker):
                        del econtext['userquery']
                    else:
                        econtext['userquery'] = __backup_userquery_4905372592
                    if (__backup_userid_4905380752 is __marker):
                        del econtext['userid']
                    else:
                        econtext['userid'] = __backup_userid_4905380752
                    if (__backup_oddrow_4900626944 is __marker):
                        del econtext['oddrow']
                    else:
                        econtext['oddrow'] = __backup_oddrow_4900626944
                    __append('\n                  ')
                    ____index_4907250688 -= 1
                    if (____index_4907250688 > 0):
                        __append('')
                if (__backup_user_4900634192 is __marker):
                    del econtext['user']
                else:
                    econtext['user'] = __backup_user_4900634192
                __append('\n                  ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4906181696
                __attrs_4906181696 = _static_4428767312

                # <Value 'not:batch' (168:37)> -> __condition
                __token = 8610
                try:
                    __zt_tmp = __attrs_4906181696
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('not', 'batch', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr>\n                      ')

                    # <Static value=<ast.Dict object at 0x1246e6dd0> name=None at 1246e4820> -> __attrs_4906182368
                    __attrs_4906182368 = _static_4906184144

                    # <Value 'view/searchString' (169:41)> -> __condition
                    __token = 8663
                    try:
                        __zt_tmp = __attrs_4906182368
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('path', 'view/searchString', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td style="text-align:center;">')
                        __stream_4906182752 = []
                        __append_4906182752 = __stream_4906182752.append
                        __append_4906182752('No matches')
                        __msgid_4906182752 = __re_whitespace(''.join(__stream_4906182752)).strip()
                        if 'text_nomatches':
                            __append(translate('text_nomatches', mapping=None, default=__msgid_4906182752, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</td>')
                    __append('\n                      ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4906179920
                    __attrs_4906179920 = _static_4428767312

                    # <Value 'not:view/searchString' (172:48)> -> __condition
                    __token = 8857
                    try:
                        __zt_tmp = __attrs_4906179920
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('not', 'view/searchString', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:
                        __append('\n                        ')

                        # <Static value=<ast.Dict object at 0x1246e4100> name=None at 1246e4c70> -> __attrs_4906184192
                        __attrs_4906184192 = _static_4906172672

                        # <Value 'many_users' (173:43)> -> __condition
                        __token = 8924
                        try:
                            __zt_tmp = __attrs_4906184192
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4427992992('path', 'many_users', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        if __condition:

                            # <td ... (0:0)
                            # --------------------------------------------------------
                            __append('<td class="discreet" style="text-align:center; font-size: 100%;">')
                            __stream_4906181120 = []
                            __append_4906181120 = __stream_4906181120.append
                            __append_4906181120('\n                            Enter a username to search for\n                        ')
                            __msgid_4906181120 = __re_whitespace(''.join(__stream_4906181120)).strip()
                            if 'text_no_user_searchstring':
                                __append(translate('text_no_user_searchstring', mapping=None, default=__msgid_4906181120, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</td>')
                        __append('\n                        ')

                        # <Static value=<ast.Dict object at 0x1246e50f0> name=None at 1246e48b0> -> __attrs_4897677728
                        __attrs_4897677728 = _static_4906176752

                        # <Value 'not:many_users' (179:43)> -> __condition
                        __token = 9257
                        try:
                            __zt_tmp = __attrs_4897677728
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4427992992('not', 'many_users', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        if __condition:

                            # <td ... (0:0)
                            # --------------------------------------------------------
                            __append('<td class="discreet" style="text-align:center; font-size: 100%;">')
                            __stream_4906176272 = []
                            __append_4906176272 = __stream_4906176272.append
                            __append_4906176272("\n                            Enter a username to search for, or click 'Show All'\n                        ")
                            __msgid_4906176272 = __re_whitespace(''.join(__stream_4906176272)).strip()
                            if 'text_no_user_searchstring_largesite':
                                __append(translate('text_no_user_searchstring_largesite', mapping=None, default=__msgid_4906176272, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</td>')
                        __append('\n                      ')
                    __append('\n                  </tr>')
                __append('\n              </tbody>\n          </table>\n\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4897675136
                __attrs_4897675136 = _static_4428767312
                __backup_macroname_4907406912 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x1246e76a0> name=None at 1246e53c0> -> __value
                __value = _static_4906186400
                econtext['macroname'] = __value

                # <Value 'context/batch_macros/macros/navigation' (190:32)> -> __macro
                __token = 9716
                try:
                    __zt_tmp = __attrs_4897675136
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_4427992992('path', 'context/batch_macros/macros/navigation', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __token = 9716
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_4907406912 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_4907406912
                __append('\n\n          ')

                # <Static value=<ast.Dict object at 0x123eca500> name=None at 123ec9480> -> __attrs_4897677776
                __attrs_4897677776 = _static_4897678592
                __backup_mq_4905427600 = get('mq', __marker)

                # <Value "python:modules['ZTUtils'].make_query" (194:30)> -> __value
                __token = 9901
                try:
                    __zt_tmp = __attrs_4897677776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', "modules['ZTUtils'].make_query", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['mq'] = __value
                __backup_keys_4905429568 = get('keys', __marker)

                # <Value 'batchformkeys|nothing' (195:31)> -> __value
                __token = 9970
                try:
                    __zt_tmp = __attrs_4897677776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'batchformkeys|nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['keys'] = __value
                __backup_linkparams_4900123024 = get('linkparams', __marker)

                # <Value 'python:keys and dict([(key, request.form[key]) for key in keys if key in request]) or request.form' (196:36)> -> __value
                __token = 10030
                try:
                    __zt_tmp = __attrs_4897677776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'keys and dict([(key, request.form[key]) for key in keys if key in request]) or request.form', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['linkparams'] = __value
                __backup_url_4900629344 = get('url', __marker)

                # <Value 'batch_base_url | string:${context/absolute_url}/${template_id}' (197:28)> -> __value
                __token = 10160
                try:
                    __zt_tmp = __attrs_4897677776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'batch_base_url | string:${context/absolute_url}/${template_id}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['url'] = __value

                # <Value 'python:batch.next or batch.previous' (193:30)> -> __condition
                __token = 9834
                try:
                    __zt_tmp = __attrs_4897677776
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('python', 'batch.next or batch.previous', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="showAllSearchResults">\n              ')

                    # <Static value=<ast.Dict object at 0x123ecaef0> name=None at 123ec98a0> -> __attrs_4900644912
                    __attrs_4900644912 = _static_4897681136

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900640544
                    __default_4900640544 = _DEFAULT_MARKER

                    # <Substitution "python: '%s?%s' % (url, mq( linkparams, {'showAll':'y'} ))" (198:38)> -> __attr_href
                    __token = 10266
                    try:
                        __zt_tmp = __attrs_4900644912
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4427992992('python', " '%s?%s' % (url, mq( linkparams, {'showAll':'y'} ))", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append('>')
                    __stream_4897670000 = []
                    __append_4897670000 = __stream_4897670000.append
                    __append_4897670000('\n                  Show all search results\n              ')
                    __msgid_4897670000 = __re_whitespace(''.join(__stream_4897670000)).strip()
                    if 'description_pas_show_all_search_results':
                        __append(translate('description_pas_show_all_search_results', mapping=None, default=__msgid_4897670000, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</a>\n          </div>')
                if (__backup_url_4900629344 is __marker):
                    del econtext['url']
                else:
                    econtext['url'] = __backup_url_4900629344
                if (__backup_linkparams_4900123024 is __marker):
                    del econtext['linkparams']
                else:
                    econtext['linkparams'] = __backup_linkparams_4900123024
                if (__backup_keys_4905429568 is __marker):
                    del econtext['keys']
                else:
                    econtext['keys'] = __backup_keys_4905429568
                if (__backup_mq_4905427600 is __marker):
                    del econtext['mq']
                else:
                    econtext['mq'] = __backup_mq_4905427600
                __append('\n\n          ')

                # <Static value=<ast.Dict object at 0x124180a30> name=None at 124183670> -> __attrs_4900527152
                __attrs_4900527152 = _static_4900522544

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900520096
                __default_4900520096 = _DEFAULT_MARKER

                # <Substitution 'b_start' (205:39)> -> __attr_value
                __token = 10581
                try:
                    __zt_tmp = __attrs_4900527152
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'b_start', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', 'b_start', _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' name="b_start"/>\n\n          ')

                # <Static value=<ast.Dict object at 0x124183a00> name=None at 124180c10> -> __attrs_4900523744
                __attrs_4900523744 = _static_4900534784

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900532192
                __default_4900532192 = _DEFAULT_MARKER

                # <Substitution 'showAll' (208:39)> -> __attr_value
                __token = 10687
                try:
                    __zt_tmp = __attrs_4900523744
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'showAll', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' name="showAll"/>\n\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900520912
                __attrs_4900520912 = _static_4428767312

                # <Value 'batch' (210:30)> -> __condition
                __token = 10729
                try:
                    __zt_tmp = __attrs_4900520912
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'batch', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div>\n\n            ')

                    # <Static value=<ast.Dict object at 0x1241811e0> name=None at 124183070> -> __attrs_4900521632
                    __attrs_4900521632 = _static_4900524512

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="btn-group">\n              ')

                    # <Static value=<ast.Dict object at 0x124182c80> name=None at 1241801f0> -> __attrs_4900977152
                    __attrs_4900977152 = _static_4900531328

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="btn btn-primary" type="submit" name="form.button.Modify" value="Save" >')
                    __stream_4900528832 = []
                    __append_4900528832 = __stream_4900528832.append
                    __append_4900528832('Apply changes')
                    __msgid_4900528832 = __re_whitespace(''.join(__stream_4900528832)).strip()
                    if 'label_apply_changes':
                        __append(translate('label_apply_changes', mapping=None, default=__msgid_4900528832, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n            </div>\n          </div>')
                __append('\n\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900969664
                __attrs_4900969664 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900967648
                __default_4900967648 = _DEFAULT_MARKER

                # <Value 'context/@@authenticator/authenticator' (222:40)> -> __cache_4900970624
                __token = 11096
                try:
                    __zt_tmp = __attrs_4900969664
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4900970624 = _static_4427992992('path', 'context/@@authenticator/authenticator', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'context/@@authenticator/authenticator' (222:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1241ec670> -> __condition
                __expression = __cache_4900970624

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input />')
                else:
                    __content = __cache_4900970624
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n\n        </form>')
                if (__backup_many_users_4900204176 is __marker):
                    del econtext['many_users']
                else:
                    econtext['many_users'] = __backup_many_users_4900204176
                if (__backup_batchformkeys_4900195344 is __marker):
                    del econtext['batchformkeys']
                else:
                    econtext['batchformkeys'] = __backup_batchformkeys_4900195344
                if (__backup_batch_4900204464 is __marker):
                    del econtext['batch']
                else:
                    econtext['batch'] = __backup_batch_4900204464
                if (__backup_portal_users_4900484528 is __marker):
                    del econtext['portal_users']
                else:
                    econtext['portal_users'] = __backup_portal_users_4900484528
                if (__backup_findAll_4900485872 is __marker):
                    del econtext['findAll']
                else:
                    econtext['findAll'] = __backup_findAll_4900485872
                __append('\n      </div>\n    </div>\n\n  </article>\n\n')
                if (__backup_portal_url_4900719344 is __marker):
                    del econtext['portal_url']
                else:
                    econtext['portal_url'] = __backup_portal_url_4900719344
                if (__backup_portal_roles_4900719872 is __marker):
                    del econtext['portal_roles']
                else:
                    econtext['portal_roles'] = __backup_portal_roles_4900719872
                if (__backup_b_size_4900728944 is __marker):
                    del econtext['b_size']
                else:
                    econtext['b_size'] = __backup_b_size_4900728944
                if (__backup_b_start_4900481936 is __marker):
                    del econtext['b_start']
                else:
                    econtext['b_start'] = __backup_b_start_4900481936
                if (__backup_Batch_4900474160 is __marker):
                    del econtext['Batch']
                else:
                    econtext['Batch'] = __backup_Batch_4900474160
                if (__backup_showAll_4900473104 is __marker):
                    del econtext['showAll']
                else:
                    econtext['showAll'] = __backup_showAll_4900473104
                if (__backup_template_id_4900964336 is __marker):
                    del econtext['template_id']
                else:
                    econtext['template_id'] = __backup_template_id_4900964336
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'context/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_4907340592
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4427992992('path', 'context/prefs_main_template/macros/master', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4906666240 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4906666240
            __i18n_domain = __previous_i18n_domain_4907341936
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }