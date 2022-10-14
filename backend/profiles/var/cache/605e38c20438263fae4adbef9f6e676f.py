# -*- coding: utf-8 -*-
__filename = 'manage_roles'

__tokens = {27: ('here/manage_page_header', 1, 27), 92: ('string:ZODB Roles', 3, 27), 136: ('here/manage_tabs', 4, 25), 218: ('request/adding | nothing', 7, 21), 257: (" python:not adding and request.get('assign'", 8, 13), 314: ("g python:not assigning and request.get('role_id", 9, 11), 375: ('ng python:(not assigning and not adding and not updati', 10, 10), 801: ('context/@@csrf_token/token', 21, 28), 1171: ('here/listRoleInfo', 32, 29), 1327: ('info/id', 35, 36), 1440: ('string:?role_id=${info/id}', 39, 35), 1495: ('info/id', 40, 27), 1562: ('info/title', 42, 33), 1601: ('string:(${info/title})', 43, 27), 1686: ('info/description', 45, 27), 1824: ('string:?role_id=${info/id}&amp;assi', 48, 35), 1968: ("python:','.join(\n                [x[1] for x in here.listAssignedPrincipals(info['id'])] )", 51, 27), 2441: ('adding', 66, 22), 2498: ("request/role_id | python:''", 67, 29), 2543: (" request/login_name | python:'", 68, 16), 2586: ('s request/roles | python:', 69, 10), 2775: ('context/@@csrf_token/token', 73, 32), 3828: ('updating', 100, 22), 3890: ('request/role_id', 101, 29), 3917: (' python:here.getRoleInfo(role_id', 102, 10), 3962: ('e info/tit', 103, 10), 3991: ('on info/descript', 104, 15), 4089: ('role_id', 106, 27), 4201: ('here/absolute_url', 108, 28), 4236: (' string:role_id=${role_id}&amp;ass', 109, 16), 4311: ('string:${url}/manage_roles?${qs}', 110, 33), 4512: ('context/@@csrf_token/token', 115, 32), 4635: ('role_id', 117, 32), 4912: ('role_id', 121, 94), 5209: ('title', 127, 87), 5533: ('description', 134, 27), 5777: ('assigning', 144, 22), 5840: ('request/role_id', 145, 29), 5872: (' request/search_id | nothin', 146, 15), 5979: ('role_id', 148, 27), 6078: ('here/absolute_url', 150, 28), 6130: ('string:${url}/manage_roles?role_id=${role_id}', 151, 33), 6286: ('string:${here/absolute_url}/manage_roles', 155, 31), 6408: ('context/@@csrf_token/token', 157, 32), 6515: ('role_id', 159, 32), 6863: ('search_id', 166, 36), 7083: ('python:here.listAvailablePrincipals(role_id, search_id)', 173, 29), 7159: (' string:principal_id', 174, 19), 7200: ('t matchi', 175, 18), 7230: ('me string:principal_', 176, 18), 7272: ('ist python:here.listAssignedPrincipals(role', 177, 17), 7340: ('ight string:manage_assignRoleToPrinc', 178, 19), 7401: ('_left string:manage_removeRoleFromPrin', 179, 18), 7467: ('rdered p', 180, 20), 7565: ('context/@@csrf_token/token', 182, 32), 7763: ('role_id', 186, 34), 7627: ('here/manage_twoLists/macros/two_lists', 184, 30), 7627: ('here/manage_twoLists/macros/two_lists', 184, 30), 7903: ('here/manage_page_footer', 195, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_5108898864 = {'type': 'hidden', 'name': 'role_id', 'value': 'ROLE_ID', }
_static_5108903568 = 'two_lists'
_static_5108891808 = {'type': 'hidden', 'name': 'csrf_token', 'value': 'context/@@csrf_token/token', }
_static_5108893056 = {'action': '.', 'method': 'POST', }
_static_5108897184 = {'type': 'submit', 'class': 'col-2 btn btn-primary zmi-patch', 'value': ' Search ', }
_static_5108900016 = {'class': 'col-10 form-control', 'placeholder': 'Enter Principal ID', 'type': 'text', 'name': 'search_id', 'value': '', }
_static_5108895792 = {'class': 'input-group', }
_static_5108900160 = {'class': 'form-row align-items-center py-4 px-2', }
_static_5109033248 = {'type': 'hidden', 'name': 'assign', 'value': '1', }
_static_5109039008 = {'type': 'hidden', 'name': 'role_id', 'value': 'role_id', }
_static_5109038240 = {'type': 'hidden', 'name': 'csrf_token', 'value': 'context/@@csrf_token/token', }
_static_5109029600 = {'action': 'HERE', 'method': 'POST', }
_static_5109032672 = {'href': 'manage_roles?role_id=role_id', }
_static_5109024800 = {'class': 'text-muted py-2', }
_static_4961534544 = {'title': 'Assign a Role', }
_static_4961546352 = {'type': 'submit', 'value': ' Update Role ', 'class': 'btn btn-primary', }
_static_4961540160 = {'class': 'zmi-controls', }
_static_4961539152 = {'type': 'text', 'name': 'description', 'rows': '5', 'class': 'form-control', }
_static_4961545728 = {'class': 'col-sm-9 col-md-10', }
_static_4961534160 = {'for': 'title', 'class': 'form-label col-sm-3 col-md-2', 'label': '', }
_static_4961542320 = {'class': 'form-group row', }
_static_4959654224 = {'type': 'text', 'name': 'title', 'class': 'form-control', 'value': 'title', }
_static_4959656240 = {'class': 'col-sm-9 col-md-10', }
_static_4959664784 = {'for': 'title', 'class': 'form-label col-sm-3 col-md-2', 'label': '', }
_static_4959449296 = {'class': 'form-group row', }
_static_4932436704 = {'type': 'text', 'disabled': 'disabled', 'class': 'form-control', 'value': 'role_id', }
_static_4959443920 = {'class': 'col-sm-9 col-md-10', }
_static_4905729664 = {'for': 'group_id', 'class': 'form-label col-sm-3 col-md-2', 'label': '', }
_static_4960112784 = {'class': 'form-group row', }
_static_4960114176 = {'type': 'hidden', 'name': 'role_id', 'value': 'ROLE_ID', }
_static_4685863984 = {'type': 'hidden', 'name': 'csrf_token', 'value': 'context/@@csrf_token/token', }
_static_4894580048 = {'action': 'manage_updateRole', 'method': 'POST', }
_static_4960359024 = {'href': 'manage_roles?role_id=role_id&amp;assign=1', }
_static_4960357728 = {'class': 'text-muted py-3', }
_static_4960584608 = {'title': 'Update a Role', }
_static_4960594640 = {'type': 'submit', 'value': ' Add Role ', 'class': 'btn btn-primary', }
_static_4960599776 = {'class': 'zmi-controls', }
_static_4960589360 = {'type': 'text', 'name': 'description', 'rows': '5', 'class': 'form-control', }
_static_4960599632 = {'class': 'col-sm-9 col-md-10', }
_static_4960593056 = {'for': 'title', 'class': 'form-label col-sm-3 col-md-2', 'label': '', }
_static_5109097296 = {'class': 'form-group row', }
_static_5109097536 = {'type': 'text', 'name': 'title', 'class': 'form-control', }
_static_5109096720 = {'class': 'col-sm-9 col-md-10', }
_static_5109097776 = {'for': 'title', 'class': 'form-label col-sm-3 col-md-2', 'label': '', }
_static_5109098640 = {'class': 'form-group row', }
_static_5109095856 = {'type': 'text', 'name': 'role_id', 'class': 'form-control', }
_static_5109093552 = {'class': 'col-sm-9 col-md-10', }
_static_5109088608 = {'for': 'role_id', 'class': 'form-label col-sm-3 col-md-2', 'label': '', }
_static_5109088704 = {'class': 'form-group row', }
_static_5109094800 = {'type': 'hidden', 'name': 'csrf_token', 'value': 'context/@@csrf_token/token', }
_static_4916882032 = {'action': 'manage_addRole', 'method': 'POST', }
_static_4959936256 = {'title': 'Add a Role', }
_static_5108953008 = {'type': 'submit', 'name': 'manage_removeRoles:method', 'class': 'btn btn-primary', 'value': ' Remove Roles ', }
_static_5108949216 = {'type': 'hidden', 'name': 'role_ids:list:default', 'value': '', }
_static_4961598720 = {'class': 'form-group form-inline zmi-controls', }
_static_5108954544 = {'class': 'far fa-edit text-primary', }
_static_4960789376 = {'href': '?role_id=foo&amp;assign=1', }
_static_4961590080 = {'href': '?role_id=foo', }
_static_4961590128 = {'type': 'checkbox', 'name': 'role_ids:list', 'value': 'ROLE_ID', }
_static_4961593632 = {'class': 'pl-4', }
_static_4961586816 = {'scope': 'col', }
_static_4961592432 = {'scope': 'col', }
_static_4961598192 = {'scope': 'col', }
_static_4909718144 = {'scope': 'col', 'style': 'width:4rem', }
_static_4907803568 = {'class': 'table table-sm table-striped table-hover', }
_static_4932303120 = {'type': 'hidden', 'name': 'csrf_token', 'value': 'context/@@csrf_token/token', }
_static_4932722144 = {'action': '.', 'method': 'POST', }
_static_4961564128 = {'href': '?adding=1', }
_static_4961552704 = {'class': 'container-fluid', }
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
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

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961558032
            __attrs_4961558032 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961557264
            __default_4961557264 = _DEFAULT_MARKER

            # <Value 'here/manage_page_header' (1:27)> -> __cache_4961554336
            __token = 27
            try:
                __zt_tmp = __attrs_4961558032
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4961554336 = _static_4427992992('path', 'here/manage_page_header', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_page_header' (1:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 127bb4250> -> __condition
            __expression = __cache_4961554336

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>Header</h1>')
            else:
                __content = __cache_4961554336
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961552800
            __attrs_4961552800 = _static_4428767312
            __backup_form_title_4960584704 = get('form_title', __marker)

            # <Value 'string:ZODB Roles' (3:27)> -> __value
            __token = 92
            try:
                __zt_tmp = __attrs_4961552800
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('string', 'ZODB Roles', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['form_title'] = __value

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961557936
            __default_4961557936 = _DEFAULT_MARKER

            # <Value 'here/manage_tabs' (4:25)> -> __cache_4961550448
            __token = 136
            try:
                __zt_tmp = __attrs_4961552800
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4961550448 = _static_4427992992('path', 'here/manage_tabs', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_tabs' (4:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 127bb7250> -> __condition
            __expression = __cache_4961550448

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2> TABS </h2>')
            else:
                __content = __cache_4961550448
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            if (__backup_form_title_4960584704 is __marker):
                del econtext['form_title']
            else:
                econtext['form_title'] = __backup_form_title_4960584704
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x127bb4940> name=None at 127bb4820> -> __attrs_4961550688
            __attrs_4961550688 = _static_4961552704
            __backup_adding_4921478400 = get('adding', __marker)

            # <Value 'request/adding | nothing' (7:21)> -> __value
            __token = 218
            try:
                __zt_tmp = __attrs_4961550688
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'request/adding | nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['adding'] = __value
            __backup_assigning_4960595840 = get('assigning', __marker)

            # <Value "python:not adding and request.get('assign')" (8:13)> -> __value
            __token = 257
            try:
                __zt_tmp = __attrs_4961550688
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', "not adding and request.get('assign')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['assigning'] = __value
            __backup_updating_4961565664 = get('updating', __marker)

            # <Value "python:not assigning and request.get('role_id')" (9:11)> -> __value
            __token = 314
            try:
                __zt_tmp = __attrs_4961550688
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', "not assigning and request.get('role_id')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['updating'] = __value
            __backup_browsing_4961565808 = get('browsing', __marker)

            # <Value 'python:(not assigning and not adding and not updating)' (10:10)> -> __value
            __token = 375
            try:
                __zt_tmp = __attrs_4961550688
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', '(not assigning and not adding and not updating)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['browsing'] = __value

            # <main ... (0:0)
            # --------------------------------------------------------
            __append('<main class="container-fluid">\n\n  ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961556448
            __attrs_4961556448 = _static_4428767312

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3>Current Roles ')

            # <Static value=<ast.Dict object at 0x127bb75e0> name=None at 127bb62f0> -> __attrs_4961561632
            __attrs_4961561632 = _static_4961564128

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a href="?adding=1">(Add a role)</a></h3>\n  ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961556112
            __attrs_4961556112 = _static_4428767312

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>\n    Note that adding or removing a role here does not have much effect\n    if you do not do the same in the root of the site (at the bottom of\n    the Security tab at manage_access).\n  </p>\n\n  ')

            # <Static value=<ast.Dict object at 0x126035de0> name=None at 126034f10> -> __attrs_4921351936
            __attrs_4921351936 = _static_4932722144

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form action="." method="POST">\n    ')

            # <Static value=<ast.Dict object at 0x125fcf910> name=None at 125fcc790> -> __attrs_4909549312
            __attrs_4909549312 = _static_4932303120

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" name="csrf_token"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4909550896
            __default_4909550896 = _DEFAULT_MARKER

            # <Substitution 'context/@@csrf_token/token' (21:28)> -> __attr_value
            __token = 801
            try:
                __zt_tmp = __attrs_4909549312
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_4427992992('path', 'context/@@csrf_token/token', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' />\n    ')

            # <Static value=<ast.Dict object at 0x1248723b0> name=None at 124871780> -> __attrs_4932656128
            __attrs_4932656128 = _static_4907803568

            # <table ... (0:0)
            # --------------------------------------------------------
            __append('<table class="table table-sm table-striped table-hover">\n      ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4909713152
            __attrs_4909713152 = _static_4428767312

            # <thead ... (0:0)
            # --------------------------------------------------------
            __append('<thead>\n        ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4909727408
            __attrs_4909727408 = _static_4428767312

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append('<tr>\n          ')

            # <Static value=<ast.Dict object at 0x124a45a80> name=None at 124a44190> -> __attrs_4961587488
            __attrs_4961587488 = _static_4909718144

            # <th ... (0:0)
            # --------------------------------------------------------
            __append('<th scope="col" style="width:4rem">&nbsp;</th>\n          ')

            # <Static value=<ast.Dict object at 0x127bbfaf0> name=None at 127bbe050> -> __attrs_4961597904
            __attrs_4961597904 = _static_4961598192

            # <th ... (0:0)
            # --------------------------------------------------------
            __append('<th scope="col">Role</th>\n          ')

            # <Static value=<ast.Dict object at 0x127bbe470> name=None at 127bbf730> -> __attrs_4961595216
            __attrs_4961595216 = _static_4961592432

            # <th ... (0:0)
            # --------------------------------------------------------
            __append('<th scope="col">Description</th>\n          ')

            # <Static value=<ast.Dict object at 0x127bbce80> name=None at 127bbcbb0> -> __attrs_4961585232
            __attrs_4961585232 = _static_4961586816

            # <th ... (0:0)
            # --------------------------------------------------------
            __append('<th scope="col">Assignments</th>\n        </tr>\n      </thead>\n      ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961583264
            __attrs_4961583264 = _static_4428767312

            # <tbody ... (0:0)
            # --------------------------------------------------------
            __append('<tbody>\n        ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961589168
            __attrs_4961589168 = _static_4428767312
            __backup_info_4961052192 = get('info', __marker)

            # <Value 'here/listRoleInfo' (32:29)> -> __iterator
            __token = 1171
            try:
                __zt_tmp = __attrs_4961589168
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4427992992('path', 'here/listRoleInfo', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            (__iterator, ____index_4961591712, ) = getname('repeat')('info', __iterator)
            econtext['info'] = None
            for __item in __iterator:
                econtext['info'] = __item

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n          ')

                # <Static value=<ast.Dict object at 0x127bbe920> name=None at 127bbf940> -> __attrs_4961586048
                __attrs_4961586048 = _static_4961593632

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="pl-4">\n            ')

                # <Static value=<ast.Dict object at 0x127bbdb70> name=None at 127bbc9a0> -> __attrs_4961583888
                __attrs_4961583888 = _static_4961590128

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="checkbox" name="role_ids:list"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961584560
                __default_4961584560 = _DEFAULT_MARKER

                # <Substitution 'info/id' (35:36)> -> __attr_value
                __token = 1327
                try:
                    __zt_tmp = __attrs_4961583888
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'info/id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', 'ROLE_ID', _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n          </td>\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961590272
                __attrs_4961590272 = _static_4428767312

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td>\n            ')

                # <Static value=<ast.Dict object at 0x127bbdb40> name=None at 127bbf430> -> __attrs_4921385952
                __attrs_4921385952 = _static_4961590080

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4921382544
                __default_4921382544 = _DEFAULT_MARKER

                # <Substitution 'string:?role_id=${info/id}' (39:35)> -> __attr_href
                __token = 1440
                try:
                    __zt_tmp = __attrs_4921385952
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4427992992('string', '?role_id=${info/id}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '?role_id=foo', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' >')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961596608
                __default_4961596608 = _DEFAULT_MARKER

                # <Value 'info/id' (40:27)> -> __cache_4961589408
                __token = 1495
                try:
                    __zt_tmp = __attrs_4921385952
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4961589408 = _static_4427992992('path', 'info/id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'info/id' (40:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 127bbe8c0> -> __condition
                __expression = __cache_4961589408

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('ROLE_ID')
                else:
                    __content = __cache_4961589408
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</a>\n            ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4960792976
                __attrs_4960792976 = _static_4428767312

                # <Value 'info/title' (42:33)> -> __condition
                __token = 1562
                try:
                    __zt_tmp = __attrs_4960792976
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'info/title', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4960784768
                    __default_4960784768 = _DEFAULT_MARKER

                    # <Value 'string:(${info/title})' (43:27)> -> __cache_4921382064
                    __token = 1601
                    try:
                        __zt_tmp = __attrs_4960792976
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4921382064 = _static_4427992992('string', '(${info/title})', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'string:(${info/title})' (43:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 125566740> -> __condition
                    __expression = __cache_4921382064

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('ROLE_TITLE')
                    else:
                        __content = __cache_4921382064
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>')
                __append('\n          </td>\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4960782752
                __attrs_4960782752 = _static_4428767312

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td>')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4960783952
                __default_4960783952 = _DEFAULT_MARKER

                # <Value 'info/description' (45:27)> -> __cache_4960794560
                __token = 1686
                try:
                    __zt_tmp = __attrs_4960782752
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4960794560 = _static_4427992992('path', 'info/description', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'info/description' (45:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 127af8730> -> __condition
                __expression = __cache_4960794560

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('ROLE DESCRIPTION')
                else:
                    __content = __cache_4960794560
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</td>\n          ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4960788992
                __attrs_4960788992 = _static_4428767312

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td>\n            ')

                # <Static value=<ast.Dict object at 0x127afa380> name=None at 127afac80> -> __attrs_5108950560
                __attrs_5108950560 = _static_4960789376

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108950464
                __default_5108950464 = _DEFAULT_MARKER

                # <Substitution 'string:?role_id=${info/id}&assign=1' (48:35)> -> __attr_href
                __token = 1824
                try:
                    __zt_tmp = __attrs_5108950560
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4427992992('string', '?role_id=${info/id}&assign=1', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '?role_id=foo&amp;assign=1', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' >')

                # <Static value=<ast.Dict object at 0x1308475b0> name=None at 130845ff0> -> __attrs_5108952624
                __attrs_5108952624 = _static_5108954544

                # <i ... (0:0)
                # --------------------------------------------------------
                __append('<i class="far fa-edit text-primary"></i></a>\n            ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5108949696
                __attrs_5108949696 = _static_4428767312

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span >')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108948688
                __default_5108948688 = _DEFAULT_MARKER

                # <Value "python:','.join(\n                [x[1] for x in here.listAssignedPrincipals(info['id'])] )" (51:27)> -> __cache_5108941488
                __token = 1968
                try:
                    __zt_tmp = __attrs_5108949696
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_5108941488 = _static_4427992992('python', "','.join(\n                [x[1] for x in here.listAssignedPrincipals(info['id'])] )", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value "python:','.join(\n                [x[1] for x in here.listAssignedPrincipals(info['id'])] )" (51:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1308467d0> -> __condition
                __expression = __cache_5108941488

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('ROLE ASSIGNMENTS')
                else:
                    __content = __cache_5108941488
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</span>\n          </td>\n        </tr>')
                ____index_4961591712 -= 1
                if (____index_4961591712 > 0):
                    __append('\n        ')
            if (__backup_info_4961052192 is __marker):
                del econtext['info']
            else:
                econtext['info'] = __backup_info_4961052192
            __append('\n      </tbody>\n    </table>\n\n    ')

            # <Static value=<ast.Dict object at 0x127bbfd00> name=None at 127af9060> -> __attrs_5108952240
            __attrs_5108952240 = _static_4961598720

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-group form-inline zmi-controls">\n      ')

            # <Static value=<ast.Dict object at 0x1308460e0> name=None at 130846d10> -> __attrs_5108953728
            __attrs_5108953728 = _static_5108949216

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" name="role_ids:list:default" value="" />\n      ')

            # <Static value=<ast.Dict object at 0x130846fb0> name=None at 130847010> -> __attrs_4959943984
            __attrs_4959943984 = _static_5108953008

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="submit" name="manage_removeRoles:method"         class="btn btn-primary" value=" Remove Roles " />\n    </div>\n  </form>\n\n  ')

            # <Static value=<ast.Dict object at 0x127a29f00> name=None at 127a28700> -> __attrs_4959931744
            __attrs_4959931744 = _static_4959936256

            # <Value 'adding' (66:22)> -> __condition
            __token = 2441
            try:
                __zt_tmp = __attrs_4959931744
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'adding', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div title="Add a Role">\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4959934288
                __attrs_4959934288 = _static_4428767312
                __backup_role_id_4961051952 = get('role_id', __marker)

                # <Value "request/role_id | python:''" (67:29)> -> __value
                __token = 2498
                try:
                    __zt_tmp = __attrs_4959934288
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', "request/role_id | python:''", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['role_id'] = __value
                __backup_login_name_4959215408 = get('login_name', __marker)

                # <Value "request/login_name | python:''" (68:16)> -> __value
                __token = 2543
                try:
                    __zt_tmp = __attrs_4959934288
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', "request/login_name | python:''", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['login_name'] = __value
                __backup_roles_4961592144 = get('roles', __marker)

                # <Value 'request/roles | python:()' (69:10)> -> __value
                __token = 2586
                try:
                    __zt_tmp = __attrs_4959934288
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'request/roles | python:()', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['roles'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n      ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4686050352
                __attrs_4686050352 = _static_4428767312

                # <h3 ... (0:0)
                # --------------------------------------------------------
                __append('<h3> Add a Role </h3>\n      ')

                # <Static value=<ast.Dict object at 0x12511aa70> name=None at 126aba170> -> __attrs_5109100992
                __attrs_5109100992 = _static_4916882032

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form action="manage_addRole" method="POST">\n        ')

                # <Static value=<ast.Dict object at 0x130869990> name=None at 130868a30> -> __attrs_5109090240
                __attrs_5109090240 = _static_5109094800

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="csrf_token"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109091344
                __default_5109091344 = _DEFAULT_MARKER

                # <Substitution 'context/@@csrf_token/token' (73:32)> -> __attr_value
                __token = 2775
                try:
                    __zt_tmp = __attrs_5109090240
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'context/@@csrf_token/token', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n        ')

                # <Static value=<ast.Dict object at 0x1308681c0> name=None at 130869330> -> __attrs_5109093504
                __attrs_5109093504 = _static_5109088704

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-group row">\n          ')

                # <Static value=<ast.Dict object at 0x130868160> name=None at 130869930> -> __attrs_5109094848
                __attrs_5109094848 = _static_5109088608

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label for="role_id" class="form-label col-sm-3 col-md-2" label>Role ID</label>\n          ')

                # <Static value=<ast.Dict object at 0x1308694b0> name=None at 130869b40> -> __attrs_5109096816
                __attrs_5109096816 = _static_5109093552

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="col-sm-9 col-md-10">\n            ')

                # <Static value=<ast.Dict object at 0x130869db0> name=None at 13086a5c0> -> __attrs_5109102576
                __attrs_5109102576 = _static_5109095856

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="text" name="role_id" class="form-control" />\n          </div>\n        </div>\n        ')

                # <Static value=<ast.Dict object at 0x13086a890> name=None at 130869de0> -> __attrs_5109100176
                __attrs_5109100176 = _static_5109098640

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-group row">\n          ')

                # <Static value=<ast.Dict object at 0x13086a530> name=None at 13086ace0> -> __attrs_5109097680
                __attrs_5109097680 = _static_5109097776

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label for="title" class="form-label col-sm-3 col-md-2" label>Title</label>\n          ')

                # <Static value=<ast.Dict object at 0x13086a110> name=None at 13086b610> -> __attrs_5109103824
                __attrs_5109103824 = _static_5109096720

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="col-sm-9 col-md-10">\n            ')

                # <Static value=<ast.Dict object at 0x13086a440> name=None at 13086b640> -> __attrs_5109104256
                __attrs_5109104256 = _static_5109097536

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="text" name="title" class="form-control" />\n          </div>\n        </div>\n        ')

                # <Static value=<ast.Dict object at 0x13086a350> name=None at 1308686d0> -> __attrs_5109089520
                __attrs_5109089520 = _static_5109097296

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-group row">\n          ')

                # <Static value=<ast.Dict object at 0x127aca4a0> name=None at 127ac8880> -> __attrs_4960584224
                __attrs_4960584224 = _static_4960593056

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label for="title" class="form-label col-sm-3 col-md-2" label>Description</label>\n          ')

                # <Static value=<ast.Dict object at 0x127acbe50> name=None at 127ac9390> -> __attrs_4960585664
                __attrs_4960585664 = _static_4960599632

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="col-sm-9 col-md-10">\n            ')

                # <Static value=<ast.Dict object at 0x127ac9630> name=None at 127aca710> -> __attrs_4960595360
                __attrs_4960595360 = _static_4960589360

                # <textarea ... (0:0)
                # --------------------------------------------------------
                __append('<textarea type="text" name="description" rows="5" class="form-control"></textarea>\n          </div>\n        </div>\n        ')

                # <Static value=<ast.Dict object at 0x127acbee0> name=None at 127ac9150> -> __attrs_4960596224
                __attrs_4960596224 = _static_4960599776

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="zmi-controls">\n          ')

                # <Static value=<ast.Dict object at 0x127acaad0> name=None at 127ac8df0> -> __attrs_4960589984
                __attrs_4960589984 = _static_4960594640

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="submit" value=" Add Role " class="btn btn-primary" />\n        </div>\n      </form>\n    </div>')
                if (__backup_roles_4961592144 is __marker):
                    del econtext['roles']
                else:
                    econtext['roles'] = __backup_roles_4961592144
                if (__backup_login_name_4959215408 is __marker):
                    del econtext['login_name']
                else:
                    econtext['login_name'] = __backup_login_name_4959215408
                if (__backup_role_id_4961051952 is __marker):
                    del econtext['role_id']
                else:
                    econtext['role_id'] = __backup_role_id_4961051952
                __append('\n  </div>')
            __append('\n\n\n  ')

            # <Static value=<ast.Dict object at 0x127ac83a0> name=None at 130869750> -> __attrs_4960594592
            __attrs_4960594592 = _static_4960584608

            # <Value 'updating' (100:22)> -> __condition
            __token = 3828
            try:
                __zt_tmp = __attrs_4960594592
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'updating', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div title="Update a Role">\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4960354896
                __attrs_4960354896 = _static_4428767312
                __backup_role_id_4932612352 = get('role_id', __marker)

                # <Value 'request/role_id' (101:29)> -> __value
                __token = 3890
                try:
                    __zt_tmp = __attrs_4960354896
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'request/role_id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['role_id'] = __value
                __backup_info_4961592288 = get('info', __marker)

                # <Value 'python:here.getRoleInfo(role_id)' (102:10)> -> __value
                __token = 3917
                try:
                    __zt_tmp = __attrs_4960354896
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'here.getRoleInfo(role_id)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['info'] = __value
                __backup_title_4961592528 = get('title', __marker)

                # <Value 'info/title' (103:10)> -> __value
                __token = 3962
                try:
                    __zt_tmp = __attrs_4960354896
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'info/title', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['title'] = __value
                __backup_description_4927090416 = get('description', __marker)

                # <Value 'info/description' (104:15)> -> __value
                __token = 3991
                try:
                    __zt_tmp = __attrs_4960354896
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'info/description', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['description'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n      ')

                # <Static value=<ast.Dict object at 0x127a90d60> name=None at 127a917e0> -> __attrs_4960354368
                __attrs_4960354368 = _static_4960357728

                # <h3 ... (0:0)
                # --------------------------------------------------------
                __append('<h3 class="text-muted py-3">Update Role: \n        ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4960360608
                __attrs_4960360608 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4960362912
                __default_4960362912 = _DEFAULT_MARKER

                # <Value 'role_id' (106:27)> -> __cache_4960359840
                __token = 4089
                try:
                    __zt_tmp = __attrs_4960360608
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4960359840 = _static_4427992992('path', 'role_id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'role_id' (106:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 127a93160> -> __condition
                __expression = __cache_4960359840

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>ROLE_ID</span>')
                else:
                    __content = __cache_4960359840
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x127a91270> name=None at 127a90670> -> __attrs_4897893504
                __attrs_4897893504 = _static_4960359024
                __backup_url_4927092480 = get('url', __marker)

                # <Value 'here/absolute_url' (108:28)> -> __value
                __token = 4201
                try:
                    __zt_tmp = __attrs_4897893504
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'here/absolute_url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['url'] = __value
                __backup_qs_4960793120 = get('qs', __marker)

                # <Value 'string:role_id=${role_id}&assign=1' (109:16)> -> __value
                __token = 4236
                try:
                    __zt_tmp = __attrs_4897893504
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('string', 'role_id=${role_id}&assign=1', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['qs'] = __value

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4960354704
                __default_4960354704 = _DEFAULT_MARKER

                # <Substitution 'string:${url}/manage_roles?${qs}' (110:33)> -> __attr_href
                __token = 4311
                try:
                    __zt_tmp = __attrs_4897893504
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4427992992('string', '${url}/manage_roles?${qs}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', 'manage_roles?role_id=role_id&amp;assign=1', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' >(Assign)</a>')
                if (__backup_qs_4960793120 is __marker):
                    del econtext['qs']
                else:
                    econtext['qs'] = __backup_qs_4960793120
                if (__backup_url_4927092480 is __marker):
                    del econtext['url']
                else:
                    econtext['url'] = __backup_url_4927092480
                __append('\n      </h3>\n      ')

                # <Static value=<ast.Dict object at 0x123bd5d50> name=None at 116897700> -> __attrs_4907719680
                __attrs_4907719680 = _static_4894580048

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form action="manage_updateRole" method="POST">\n        ')

                # <Static value=<ast.Dict object at 0x1174c9c30> name=None at 1174c8550> -> __attrs_4960122240
                __attrs_4960122240 = _static_4685863984

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="csrf_token"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4960124832
                __default_4960124832 = _DEFAULT_MARKER

                # <Substitution 'context/@@csrf_token/token' (115:32)> -> __attr_value
                __token = 4512
                try:
                    __zt_tmp = __attrs_4960122240
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'context/@@csrf_token/token', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n        ')

                # <Static value=<ast.Dict object at 0x127a55600> name=None at 127a55480> -> __attrs_4960109712
                __attrs_4960109712 = _static_4960114176

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="role_id"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4960120704
                __default_4960120704 = _DEFAULT_MARKER

                # <Substitution 'role_id' (117:32)> -> __attr_value
                __token = 4635
                try:
                    __zt_tmp = __attrs_4960109712
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'role_id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', 'ROLE_ID', _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n        ')

                # <Static value=<ast.Dict object at 0x127a55090> name=None at 127a57130> -> __attrs_4960117152
                __attrs_4960117152 = _static_4960112784

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-group row">\n          ')

                # <Static value=<ast.Dict object at 0x124677e80> name=None at 124676140> -> __attrs_4959449680
                __attrs_4959449680 = _static_4905729664

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label for="group_id" class="form-label col-sm-3 col-md-2" label>Role ID</label>\n          ')

                # <Static value=<ast.Dict object at 0x1279b1bd0> name=None at 1279b30a0> -> __attrs_4959448960
                __attrs_4959448960 = _static_4959443920

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="col-sm-9 col-md-10">\n            ')

                # <Static value=<ast.Dict object at 0x125ff02e0> name=None at 125ff10c0> -> __attrs_4959449392
                __attrs_4959449392 = _static_4932436704

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="text" disabled="disabled" class="form-control"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4959440224
                __default_4959440224 = _DEFAULT_MARKER

                # <Substitution 'role_id' (121:94)> -> __attr_value
                __token = 4912
                try:
                    __zt_tmp = __attrs_4959449392
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'role_id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n          </div>\n        </div>\n        ')

                # <Static value=<ast.Dict object at 0x1279b30d0> name=None at 1279b2530> -> __attrs_4959662672
                __attrs_4959662672 = _static_4959449296

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-group row">\n          ')

                # <Static value=<ast.Dict object at 0x1279e7a90> name=None at 1279e50f0> -> __attrs_4959657536
                __attrs_4959657536 = _static_4959664784

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label for="title" class="form-label col-sm-3 col-md-2" label>Title</label>\n          ')

                # <Static value=<ast.Dict object at 0x1279e5930> name=None at 1279e5a20> -> __attrs_4959654464
                __attrs_4959654464 = _static_4959656240

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="col-sm-9 col-md-10">\n            ')

                # <Static value=<ast.Dict object at 0x1279e5150> name=None at 1279e60e0> -> __attrs_4961536368
                __attrs_4961536368 = _static_4959654224

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="text" name="title" class="form-control"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961539536
                __default_4961539536 = _DEFAULT_MARKER

                # <Substitution 'title' (127:87)> -> __attr_value
                __token = 5209
                try:
                    __zt_tmp = __attrs_4961536368
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'title', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n          </div>\n        </div>\n        ')

                # <Static value=<ast.Dict object at 0x127bb20b0> name=None at 127bb2a40> -> __attrs_4961539920
                __attrs_4961539920 = _static_4961542320

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-group row">\n          ')

                # <Static value=<ast.Dict object at 0x127bb00d0> name=None at 127bb1e10> -> __attrs_4961542416
                __attrs_4961542416 = _static_4961534160

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label for="title" class="form-label col-sm-3 col-md-2" label>Description</label>\n          ')

                # <Static value=<ast.Dict object at 0x127bb2e00> name=None at 127bb09d0> -> __attrs_4961543712
                __attrs_4961543712 = _static_4961545728

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="col-sm-9 col-md-10">\n            ')

                # <Static value=<ast.Dict object at 0x127bb1450> name=None at 127bb1390> -> __attrs_4961536128
                __attrs_4961536128 = _static_4961539152

                # <textarea ... (0:0)
                # --------------------------------------------------------
                __append('<textarea type="text" name="description" rows="5" class="form-control">')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961542656
                __default_4961542656 = _DEFAULT_MARKER

                # <Value 'description' (134:27)> -> __cache_4961537568
                __token = 5533
                try:
                    __zt_tmp = __attrs_4961536128
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4961537568 = _static_4427992992('path', 'description', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'description' (134:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 127bb0b80> -> __condition
                __expression = __cache_4961537568

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4961537568
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</textarea>\n          </div>\n        </div>\n        ')

                # <Static value=<ast.Dict object at 0x127bb1840> name=None at 127bb1bd0> -> __attrs_4961548512
                __attrs_4961548512 = _static_4961540160

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="zmi-controls">\n          ')

                # <Static value=<ast.Dict object at 0x127bb3070> name=None at 127bb1cf0> -> __attrs_5109038048
                __attrs_5109038048 = _static_4961546352

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="submit" value=" Update Role " class="btn btn-primary" />\n        </div>\n      </form>\n    </div>')
                if (__backup_description_4927090416 is __marker):
                    del econtext['description']
                else:
                    econtext['description'] = __backup_description_4927090416
                if (__backup_title_4961592528 is __marker):
                    del econtext['title']
                else:
                    econtext['title'] = __backup_title_4961592528
                if (__backup_info_4961592288 is __marker):
                    del econtext['info']
                else:
                    econtext['info'] = __backup_info_4961592288
                if (__backup_role_id_4932612352 is __marker):
                    del econtext['role_id']
                else:
                    econtext['role_id'] = __backup_role_id_4932612352
                __append('\n  </div>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x127bb0250> name=None at 127bb0910> -> __attrs_5109038336
            __attrs_5109038336 = _static_4961534544

            # <Value 'assigning' (144:22)> -> __condition
            __token = 5777
            try:
                __zt_tmp = __attrs_5109038336
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'assigning', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div title="Assign a Role">\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109029792
                __attrs_5109029792 = _static_4428767312
                __backup_role_id_4927087248 = get('role_id', __marker)

                # <Value 'request/role_id' (145:29)> -> __value
                __token = 5840
                try:
                    __zt_tmp = __attrs_5109029792
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'request/role_id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['role_id'] = __value
                __backup_search_id_4932718592 = get('search_id', __marker)

                # <Value 'request/search_id | nothing' (146:15)> -> __value
                __token = 5872
                try:
                    __zt_tmp = __attrs_5109029792
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'request/search_id | nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['search_id'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n      ')

                # <Static value=<ast.Dict object at 0x130858820> name=None at 130859bd0> -> __attrs_5109028496
                __attrs_5109028496 = _static_5109024800

                # <h3 ... (0:0)
                # --------------------------------------------------------
                __append('<h3 class="text-muted py-2">Assign Role: \n        ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109023504
                __attrs_5109023504 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109029648
                __default_5109029648 = _DEFAULT_MARKER

                # <Value 'role_id' (148:27)> -> __cache_5109027104
                __token = 5979
                try:
                    __zt_tmp = __attrs_5109023504
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_5109027104 = _static_4427992992('path', 'role_id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'role_id' (148:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 13085ba60> -> __condition
                __expression = __cache_5109027104

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>ROLE_ID</span>')
                else:
                    __content = __cache_5109027104
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x13085a6e0> name=None at 13085b040> -> __attrs_5109029888
                __attrs_5109029888 = _static_5109032672
                __backup_url_4960795136 = get('url', __marker)

                # <Value 'here/absolute_url' (150:28)> -> __value
                __token = 6078
                try:
                    __zt_tmp = __attrs_5109029888
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'here/absolute_url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['url'] = __value

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109028112
                __default_5109028112 = _DEFAULT_MARKER

                # <Substitution 'string:${url}/manage_roles?role_id=${role_id}' (151:33)> -> __attr_href
                __token = 6130
                try:
                    __zt_tmp = __attrs_5109029888
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4427992992('string', '${url}/manage_roles?role_id=${role_id}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', 'manage_roles?role_id=role_id', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' >(Properties)</a>')
                if (__backup_url_4960795136 is __marker):
                    del econtext['url']
                else:
                    econtext['url'] = __backup_url_4960795136
                __append('\n      </h3>\n      ')

                # <Static value=<ast.Dict object at 0x130859ae0> name=None at 130858e20> -> __attrs_5109024032
                __attrs_5109024032 = _static_5109029600

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109030128
                __default_5109030128 = _DEFAULT_MARKER

                # <Substitution 'string:${here/absolute_url}/manage_roles' (155:31)> -> __attr_action
                __token = 6286
                try:
                    __zt_tmp = __attrs_5109024032
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_action = _static_4427992992('string', '${here/absolute_url}/manage_roles', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_action = __quote(__attr_action, '"', '&quot;', 'HERE', _DEFAULT_MARKER)
                if (__attr_action is not None):
                    __append((' action="%s"' % __attr_action))
                __append(' method="POST">\n        ')

                # <Static value=<ast.Dict object at 0x13085bca0> name=None at 1308585b0> -> __attrs_5109032480
                __attrs_5109032480 = _static_5109038240

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="csrf_token"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109026432
                __default_5109026432 = _DEFAULT_MARKER

                # <Substitution 'context/@@csrf_token/token' (157:32)> -> __attr_value
                __token = 6408
                try:
                    __zt_tmp = __attrs_5109032480
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'context/@@csrf_token/token', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n        ')

                # <Static value=<ast.Dict object at 0x13085bfa0> name=None at 130858790> -> __attrs_5109034784
                __attrs_5109034784 = _static_5109039008

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="role_id"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109032000
                __default_5109032000 = _DEFAULT_MARKER

                # <Substitution 'role_id' (159:32)> -> __attr_value
                __token = 6515
                try:
                    __zt_tmp = __attrs_5109034784
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'role_id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n        ')

                # <Static value=<ast.Dict object at 0x13085a920> name=None at 13085b070> -> __attrs_5109030992
                __attrs_5109030992 = _static_5109033248

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="assign" value="1" />\n        ')

                # <Static value=<ast.Dict object at 0x13083a140> name=None at 130839de0> -> __attrs_5108903904
                __attrs_5108903904 = _static_5108900160

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-row align-items-center py-4 px-2">\n          ')

                # <Static value=<ast.Dict object at 0x130839030> name=None at 13083a170> -> __attrs_5108901360
                __attrs_5108901360 = _static_5108895792

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="input-group">\n            ')

                # <Static value=<ast.Dict object at 0x13083a0b0> name=None at 130838160> -> __attrs_5108904240
                __attrs_5108904240 = _static_5108900016

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="col-10 form-control" placeholder="Enter Principal ID"               type="text" name="search_id"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108894928
                __default_5108894928 = _DEFAULT_MARKER

                # <Substitution 'search_id' (166:36)> -> __attr_value
                __token = 6863
                try:
                    __zt_tmp = __attrs_5108904240
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'search_id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n            ')

                # <Static value=<ast.Dict object at 0x1308395a0> name=None at 130839960> -> __attrs_5108906640
                __attrs_5108906640 = _static_5108897184

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="submit" class="col-2 btn btn-primary zmi-patch" value=" Search " />\n          </div>\n        </div>\n      </form>\n\n      ')

                # <Static value=<ast.Dict object at 0x130838580> name=None at 1308384f0> -> __attrs_5108899248
                __attrs_5108899248 = _static_5108893056
                __backup_matching_4907724192 = get('matching', __marker)

                # <Value 'python:here.listAvailablePrincipals(role_id, search_id)' (173:29)> -> __value
                __token = 7083
                try:
                    __zt_tmp = __attrs_5108899248
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'here.listAvailablePrincipals(role_id, search_id)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['matching'] = __value
                __backup_left_name_4960793168 = get('left_name', __marker)

                # <Value 'string:principal_ids' (174:19)> -> __value
                __token = 7159
                try:
                    __zt_tmp = __attrs_5108899248
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('string', 'principal_ids', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['left_name'] = __value
                __backup_left_list_4960786064 = get('left_list', __marker)

                # <Value 'matching' (175:18)> -> __value
                __token = 7200
                try:
                    __zt_tmp = __attrs_5108899248
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'matching', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['left_list'] = __value
                __backup_right_name_4907718000 = get('right_name', __marker)

                # <Value 'string:principal_ids' (176:18)> -> __value
                __token = 7230
                try:
                    __zt_tmp = __attrs_5108899248
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('string', 'principal_ids', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['right_name'] = __value
                __backup_right_list_4960781072 = get('right_list', __marker)

                # <Value 'python:here.listAssignedPrincipals(role_id)' (177:17)> -> __value
                __token = 7272
                try:
                    __zt_tmp = __attrs_5108899248
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'here.listAssignedPrincipals(role_id)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['right_list'] = __value
                __backup_left_to_right_4961485776 = get('left_to_right', __marker)

                # <Value 'string:manage_assignRoleToPrincipals' (178:19)> -> __value
                __token = 7340
                try:
                    __zt_tmp = __attrs_5108899248
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('string', 'manage_assignRoleToPrincipals', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['left_to_right'] = __value
                __backup_right_to_left_4961485920 = get('right_to_left', __marker)

                # <Value 'string:manage_removeRoleFromPrincipals' (179:18)> -> __value
                __token = 7401
                try:
                    __zt_tmp = __attrs_5108899248
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('string', 'manage_removeRoleFromPrincipals', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['right_to_left'] = __value
                __backup_right_is_ordered_4960796144 = get('right_is_ordered', __marker)

                # <Value 'python:0' (180:20)> -> __value
                __token = 7467
                try:
                    __zt_tmp = __attrs_5108899248
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', '0', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['right_is_ordered'] = __value

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form action="." method="POST">\n        ')

                # <Static value=<ast.Dict object at 0x1308380a0> name=None at 13083ae00> -> __attrs_5108906208
                __attrs_5108906208 = _static_5108891808

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="csrf_token"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108898720
                __default_5108898720 = _DEFAULT_MARKER

                # <Substitution 'context/@@csrf_token/token' (182:32)> -> __attr_value
                __token = 7565
                try:
                    __zt_tmp = __attrs_5108906208
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'context/@@csrf_token/token', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n\n        ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5108903808
                __attrs_5108903808 = _static_4428767312
                __backup_macroname_5109200704 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x13083ae90> name=None at 130839840> -> __value
                __value = _static_5108903568
                econtext['macroname'] = __value

                def __fill_hidden_vars(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                    getname = econtext.get_name
                    get = econtext.get

                    # <Static value=<ast.Dict object at 0x130839c30> name=None at 130839900> -> __attrs_5108896320
                    __attrs_5108896320 = _static_5108898864

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="hidden" name="role_id"')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108892624
                    __default_5108892624 = _DEFAULT_MARKER

                    # <Substitution 'role_id' (186:34)> -> __attr_value
                    __token = 7763
                    try:
                        __zt_tmp = __attrs_5108896320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_4427992992('path', 'role_id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', 'ROLE_ID', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />')
                _slots = econtext['__slot_hidden_vars'] = _deque((__fill_hidden_vars, ))

                # <Value 'here/manage_twoLists/macros/two_lists' (184:30)> -> __macro
                __token = 7627
                try:
                    __zt_tmp = __attrs_5108903808
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_4427992992('path', 'here/manage_twoLists/macros/two_lists', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __token = 7627
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_5109200704 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_5109200704
                __append('\n      </form>')
                if (__backup_right_is_ordered_4960796144 is __marker):
                    del econtext['right_is_ordered']
                else:
                    econtext['right_is_ordered'] = __backup_right_is_ordered_4960796144
                if (__backup_right_to_left_4961485920 is __marker):
                    del econtext['right_to_left']
                else:
                    econtext['right_to_left'] = __backup_right_to_left_4961485920
                if (__backup_left_to_right_4961485776 is __marker):
                    del econtext['left_to_right']
                else:
                    econtext['left_to_right'] = __backup_left_to_right_4961485776
                if (__backup_right_list_4960781072 is __marker):
                    del econtext['right_list']
                else:
                    econtext['right_list'] = __backup_right_list_4960781072
                if (__backup_right_name_4907718000 is __marker):
                    del econtext['right_name']
                else:
                    econtext['right_name'] = __backup_right_name_4907718000
                if (__backup_left_list_4960786064 is __marker):
                    del econtext['left_list']
                else:
                    econtext['left_list'] = __backup_left_list_4960786064
                if (__backup_left_name_4960793168 is __marker):
                    del econtext['left_name']
                else:
                    econtext['left_name'] = __backup_left_name_4960793168
                if (__backup_matching_4907724192 is __marker):
                    del econtext['matching']
                else:
                    econtext['matching'] = __backup_matching_4907724192
                __append('\n    </div>')
                if (__backup_search_id_4932718592 is __marker):
                    del econtext['search_id']
                else:
                    econtext['search_id'] = __backup_search_id_4932718592
                if (__backup_role_id_4927087248 is __marker):
                    del econtext['role_id']
                else:
                    econtext['role_id'] = __backup_role_id_4927087248
                __append('\n  </div>')
            __append('\n\n</main>')
            if (__backup_browsing_4961565808 is __marker):
                del econtext['browsing']
            else:
                econtext['browsing'] = __backup_browsing_4961565808
            if (__backup_updating_4961565664 is __marker):
                del econtext['updating']
            else:
                econtext['updating'] = __backup_updating_4961565664
            if (__backup_assigning_4960595840 is __marker):
                del econtext['assigning']
            else:
                econtext['assigning'] = __backup_assigning_4960595840
            if (__backup_adding_4921478400 is __marker):
                del econtext['adding']
            else:
                econtext['adding'] = __backup_adding_4921478400
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5109704272
            __attrs_5109704272 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5109699328
            __default_5109699328 = _DEFAULT_MARKER

            # <Value 'here/manage_page_footer' (195:27)> -> __cache_5108897232
            __token = 7903
            try:
                __zt_tmp = __attrs_5109704272
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_5108897232 = _static_4427992992('path', 'here/manage_page_footer', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_page_footer' (195:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 130839270> -> __condition
            __expression = __cache_5108897232

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>Footer</h1>')
            else:
                __content = __cache_5108897232
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }