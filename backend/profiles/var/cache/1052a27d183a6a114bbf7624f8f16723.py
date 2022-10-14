# -*- coding: utf-8 -*-
__filename = 'manage_users'

__tokens = {27: ('here/manage_page_header', 1, 27), 92: ('string:ZODB Users', 3, 27), 138: ('here/manage_tabs', 4, 27), 224: ('request/adding | nothing', 7, 25), 274: (" python: not adding and request.get('user_id')\n                                            and request.get('passwd'", 8, 24), 417: ("g python: not adding and not passwd\n                                             and request.get('user_id", 10, 25), 550: ('ng python: not adding and not passwd\n                               and not updat', 12, 24), 679: ('browsing', 16, 22), 879: ('context/@@csrf_token/token', 22, 32), 1292: ('here/listUserInfo', 36, 28), 1454: ('info/user_id', 40, 39), 1646: ('string:?user_id=${info/user_id}', 47, 34), 1705: ('info/user_id', 48, 26), 1849: ('string:?user_id=${info/user_id}&amp;pass', 53, 33), 1992: ('info/login_name', 57, 47), 2403: ('adding', 75, 22), 2439: ("request/user_id | python:''", 76, 27), 2497: (" request/login_name | python:'", 77, 29), 2696: ('context/@@csrf_token/token', 84, 31), 2974: ('here/manage_widgets/macros/authentication_widgets', 97, 27), 2974: ('here/manage_widgets/macros/authentication_widgets', 97, 27), 3203: ('passwd', 109, 22), 3239: ('request/user_id', 110, 27), 3279: (' python:here.getUserInfo( user_id ', 111, 23), 3344: ('e info/login_na', 112, 28), 3488: ('string:?user_id=${user_id}', 116, 52), 3699: ('context/@@csrf_token/token', 121, 31), 3940: ('user_id', 130, 34), 3994: ('user_id', 131, 42), 4165: ('login_name', 140, 45), 4791: ('updating', 173, 22), 4829: ('request/user_id', 174, 27), 4869: (' python:here.getUserInfo(user_id', 175, 23), 4932: ('e info/login_na', 176, 28), 5073: ('string:?user_id=${user_id}&amp;pass', 180, 43), 5284: ('context/@@csrf_token/token', 185, 31), 5525: ('user_id', 194, 34), 5579: ('user_id', 195, 42), 5812: ('login_name', 205, 34), 6043: ('here/manage_page_footer', 222, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4960793744 = {'type': 'submit', 'value': ' Update User ', 'class': 'btn btn-primary', }
_static_4960789904 = {'class': 'form-controls', }
_static_4960785200 = {'type': 'text', 'name': 'login_name', 'size': '40', 'class': 'form-control', 'value': 'login_name', }
_static_4891943184 = {'class': 'form-label', }
_static_4900197312 = {'class': 'form-label', }
_static_4900977344 = {'type': 'hidden', 'name': 'user_id', 'class': 'form-control', 'value': 'user_id', }
_static_4961048976 = {'class': 'form-label', }
_static_4961056848 = {'class': 'table table-sm', }
_static_4961047920 = {'type': 'hidden', 'name': 'csrf_token', 'value': 'context/@@csrf_token/token', }
_static_4961052384 = {'action': 'manage_updateUser', 'method': 'POST', }
_static_4961043120 = {'href': '?user_id=XXX&amp;passwd=1', }
_static_4960591424 = {'type': 'submit', 'value': ' Update Password ', 'class': 'btn btn-primary', }
_static_4960594928 = {'class': 'form-controls', }
_static_4960594592 = {'type': 'password', 'name': 'confirm', 'size': '20', 'value': 'confirm', 'class': 'form-control', }
_static_4960590752 = {'class': 'form-label', }
_static_4961586960 = {'type': 'password', 'name': 'password', 'size': '20', 'value': 'password', 'class': 'form-control', }
_static_4961592480 = {'class': 'form-label', }
_static_4961599296 = {'class': 'form-control', }
_static_4961598720 = {'class': 'form-label', }
_static_4907253712 = {'class': 'form-label', }
_static_4960116096 = {'type': 'hidden', 'name': 'user_id', 'class': 'form-control', 'value': 'user_id', }
_static_4960118016 = {'class': 'form-label', }
_static_4961553088 = {'class': 'table table-sm', }
_static_4961562688 = {'type': 'hidden', 'name': 'csrf_token', 'value': 'context/@@csrf_token/token', }
_static_4961551888 = {'action': 'manage_updateUserPassword', 'method': 'POST', }
_static_4961566624 = {'href': '?user_id=XXX', }
_static_4960354800 = {'type': 'submit', 'value': ' Add User ', 'class': 'btn btn-primary', }
_static_4960361760 = {'class': 'form-controls', }
_static_4960358880 = 'authentication_widgets'
_static_4960359696 = {'type': 'text', 'name': 'user_id', 'size': '20', 'class': 'form-control', }
_static_4960355952 = {'class': 'form-label', }
_static_4620646432 = {'scope': 'row', }
_static_4932651760 = {'class': 'table table-sm', }
_static_4905522928 = {'type': 'hidden', 'name': 'csrf_token', 'value': 'context/@@csrf_token/token', }
_static_4923846384 = {'action': 'manage_addUser', 'method': 'POST', }
_static_4927176768 = {'type': 'submit', 'name': 'manage_removeUsers:method', 'class': 'btn btn-primary zmi-patch', 'value': ' Remove Users ', }
_static_4900092272 = {'type': 'hidden', 'name': 'user_ids:list:default', 'value': '', }
_static_4900477376 = {'class': 'form-group zmi-controls', }
_static_4905776944 = {'class': 'form-text', }
_static_4932613600 = {'href': '?passwd=1', 'class': 'form-text', }
_static_4958789184 = {'href': '?user_id=foo', 'class': 'form-text', }
_static_4959213872 = {'class': 'far fa-user', }
_static_4959215024 = {'type': 'checkbox', 'name': 'user_ids:list', 'value': 'info/user_id', }
_static_4907238256 = {'class': 'text-right', }
_static_4959652832 = {'scope': 'col', }
_static_4959656480 = {'scope': 'col', }
_static_4909524464 = {'scope': 'col', }
_static_4900619264 = {'scope': 'col', 'style': 'width:2em', }
_static_4897894032 = {'class': 'text-right', 'scope': 'col', 'style': 'width:2em', }
_static_4959442288 = {'class': 'table table-sm table-striped table-hover', }
_static_4909711808 = {'type': 'hidden', 'name': 'csrf_token', 'value': 'context/@@csrf_token/token', }
_static_4909717184 = {'action': '.', 'method': 'POST', 'id': 'users', }
_static_4921579488 = {'href': '?adding=1', }
_static_4932410848 = {'class': 'container-fluid', }
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

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4959932272
            __attrs_4959932272 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4959930544
            __default_4959930544 = _DEFAULT_MARKER

            # <Value 'here/manage_page_header' (1:27)> -> __cache_4959938800
            __token = 27
            try:
                __zt_tmp = __attrs_4959932272
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4959938800 = _static_4427992992('path', 'here/manage_page_header', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_page_header' (1:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 127a2a980> -> __condition
            __expression = __cache_4959938800

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>Header</h1>')
            else:
                __content = __cache_4959938800
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4895405920
            __attrs_4895405920 = _static_4428767312
            __backup_form_title_4959221504 = get('form_title', __marker)

            # <Value 'string:ZODB Users' (3:27)> -> __value
            __token = 92
            try:
                __zt_tmp = __attrs_4895405920
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('string', 'ZODB Users', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['form_title'] = __value

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4909551472
            __default_4909551472 = _DEFAULT_MARKER

            # <Value 'here/manage_tabs' (4:27)> -> __cache_4909555696
            __token = 138
            try:
                __zt_tmp = __attrs_4895405920
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4909555696 = _static_4427992992('path', 'here/manage_tabs', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_tabs' (4:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 124a1ec50> -> __condition
            __expression = __cache_4909555696

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2> TABS </h2>')
            else:
                __content = __cache_4909555696
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            if (__backup_form_title_4959221504 is __marker):
                del econtext['form_title']
            else:
                econtext['form_title'] = __backup_form_title_4959221504
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x125fe9de0> name=None at 125feae60> -> __attrs_4932417520
            __attrs_4932417520 = _static_4932410848
            __backup_adding_4961488800 = get('adding', __marker)

            # <Value 'request/adding | nothing' (7:25)> -> __value
            __token = 224
            try:
                __zt_tmp = __attrs_4932417520
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'request/adding | nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['adding'] = __value
            __backup_passwd_4961491584 = get('passwd', __marker)

            # <Value "python: not adding and request.get('user_id')\n                                            and request.get('passwd')" (8:24)> -> __value
            __token = 274
            try:
                __zt_tmp = __attrs_4932417520
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', " not adding and request.get('user_id')\n                                            and request.get('passwd')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['passwd'] = __value
            __backup_updating_4961491728 = get('updating', __marker)

            # <Value "python: not adding and not passwd\n                                             and request.get('user_id')" (10:25)> -> __value
            __token = 417
            try:
                __zt_tmp = __attrs_4932417520
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', " not adding and not passwd\n                                             and request.get('user_id')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['updating'] = __value
            __backup_browsing_4960365600 = get('browsing', __marker)

            # <Value 'python: not adding and not passwd\n                               and not updating' (12:24)> -> __value
            __token = 550
            try:
                __zt_tmp = __attrs_4932417520
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', ' not adding and not passwd\n                               and not updating', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['browsing'] = __value

            # <main ... (0:0)
            # --------------------------------------------------------
            __append('<main class="container-fluid">\n\n  ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4923919376
            __attrs_4923919376 = _static_4428767312

            # <Value 'browsing' (16:22)> -> __condition
            __token = 679
            try:
                __zt_tmp = __attrs_4923919376
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'browsing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4921586688
                __attrs_4921586688 = _static_4428767312

                # <h3 ... (0:0)
                # --------------------------------------------------------
                __append('<h3> Current Users ')

                # <Static value=<ast.Dict object at 0x1255957e0> name=None at 125597280> -> __attrs_4909717904
                __attrs_4909717904 = _static_4921579488

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a href="?adding=1">(Add a user)</a></h3>\n\n    ')

                # <Static value=<ast.Dict object at 0x124a456c0> name=None at 124a46b30> -> __attrs_4909724288
                __attrs_4909724288 = _static_4909717184

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form action="." method="POST" id="users">\n    ')

                # <Static value=<ast.Dict object at 0x124a441c0> name=None at 124a469b0> -> __attrs_4959446320
                __attrs_4959446320 = _static_4909711808

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="csrf_token"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4959443824
                __default_4959443824 = _DEFAULT_MARKER

                # <Substitution 'context/@@csrf_token/token' (22:32)> -> __attr_value
                __token = 879
                try:
                    __zt_tmp = __attrs_4959446320
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'context/@@csrf_token/token', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n\n    ')

                # <Static value=<ast.Dict object at 0x1279b1570> name=None at 1279b3af0> -> __attrs_4959444640
                __attrs_4959444640 = _static_4959442288

                # <table ... (0:0)
                # --------------------------------------------------------
                __append('<table class="table table-sm table-striped table-hover">\n     ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4959445696
                __attrs_4959445696 = _static_4428767312

                # <thead ... (0:0)
                # --------------------------------------------------------
                __append('<thead>\n       ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4923895152
                __attrs_4923895152 = _static_4428767312

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n        ')

                # <Static value=<ast.Dict object at 0x123efee90> name=None at 1257cbf10> -> __attrs_4922699216
                __attrs_4922699216 = _static_4897894032

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th class="text-right" scope="col" style="width:2em"></th>\n        ')

                # <Static value=<ast.Dict object at 0x124198400> name=None at 12419b340> -> __attrs_4676622640
                __attrs_4676622640 = _static_4900619264

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th scope="col" style="width:2em"></th>\n        ')

                # <Static value=<ast.Dict object at 0x124a165f0> name=None at 124a14760> -> __attrs_4932375536
                __attrs_4932375536 = _static_4909524464

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th scope="col"> User ID </th>\n        ')

                # <Static value=<ast.Dict object at 0x1279e5a20> name=None at 1279e6770> -> __attrs_4959665408
                __attrs_4959665408 = _static_4959656480

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th scope="col"></th>\n        ')

                # <Static value=<ast.Dict object at 0x1279e4be0> name=None at 1279e6dd0> -> __attrs_4959664640
                __attrs_4959664640 = _static_4959652832

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th scope="col"> Login Name </th>\n       </tr>\n     </thead>\n\n     ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4959658352
                __attrs_4959658352 = _static_4428767312

                # <tbody ... (0:0)
                # --------------------------------------------------------
                __append('<tbody>\n       ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4959651536
                __attrs_4959651536 = _static_4428767312
                __backup_info_4660583376 = get('info', __marker)

                # <Value 'here/listUserInfo' (36:28)> -> __iterator
                __token = 1292
                try:
                    __zt_tmp = __attrs_4959651536
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4427992992('path', 'here/listUserInfo', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                (__iterator, ____index_4907862528, ) = getname('repeat')('info', __iterator)
                econtext['info'] = None
                for __item in __iterator:
                    econtext['info'] = __item

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr>\n        ')

                    # <Static value=<ast.Dict object at 0x1247e8370> name=None at 1247eb6a0> -> __attrs_4907250736
                    __attrs_4907250736 = _static_4907238256

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td class="text-right">\n          ')

                    # <Static value=<ast.Dict object at 0x127979db0> name=None at 12797a110> -> __attrs_4959213968
                    __attrs_4959213968 = _static_4959215024

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="checkbox" name="user_ids:list"')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4959217136
                    __default_4959217136 = _DEFAULT_MARKER

                    # <Substitution 'info/user_id' (40:39)> -> __attr_value
                    __token = 1454
                    try:
                        __zt_tmp = __attrs_4959213968
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_4427992992('path', 'info/user_id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n        </td>\n        ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4959217712
                    __attrs_4959217712 = _static_4428767312

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td>\n          ')

                    # <Static value=<ast.Dict object at 0x127979930> name=None at 12797af20> -> __attrs_4922682304
                    __attrs_4922682304 = _static_4959213872

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i class="far fa-user" />\n        </td>\n        ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4958793984
                    __attrs_4958793984 = _static_4428767312

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td>\n          ')

                    # <Static value=<ast.Dict object at 0x127911e40> name=None at 1279135e0> -> __attrs_4932607504
                    __attrs_4932607504 = _static_4958789184

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4958789616
                    __default_4958789616 = _DEFAULT_MARKER

                    # <Substitution 'string:?user_id=${info/user_id}' (47:34)> -> __attr_href
                    __token = 1646
                    try:
                        __zt_tmp = __attrs_4932607504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4427992992('string', '?user_id=${info/user_id}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?user_id=foo', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' class="form-text" >')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4958783472
                    __default_4958783472 = _DEFAULT_MARKER

                    # <Value 'info/user_id' (48:26)> -> __cache_4958786640
                    __token = 1705
                    try:
                        __zt_tmp = __attrs_4932607504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4958786640 = _static_4427992992('path', 'info/user_id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'info/user_id' (48:26)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 127910b50> -> __condition
                    __expression = __cache_4958786640

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('USER_ID')
                    else:
                        __content = __cache_4958786640
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</a>\n        </td>\n        ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4932602464
                    __attrs_4932602464 = _static_4428767312

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td>\n         ')

                    # <Static value=<ast.Dict object at 0x12601b5e0> name=None at 126019a50> -> __attrs_4932614992
                    __attrs_4932614992 = _static_4932613600

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4932608560
                    __default_4932608560 = _DEFAULT_MARKER

                    # <Substitution 'string:?user_id=${info/user_id}&passwd=1' (53:33)> -> __attr_href
                    __token = 1849
                    try:
                        __zt_tmp = __attrs_4932614992
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4427992992('string', '?user_id=${info/user_id}&passwd=1', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?passwd=1', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' class="form-text" >Password</a>\n        </td>\n        ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4921389888
                    __attrs_4921389888 = _static_4428767312

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td>\n          ')

                    # <Static value=<ast.Dict object at 0x124683730> name=None at 1246830d0> -> __attrs_4680815024
                    __attrs_4680815024 = _static_4905776944

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="form-text">')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4921386816
                    __default_4921386816 = _DEFAULT_MARKER

                    # <Value 'info/login_name' (57:47)> -> __cache_4921385088
                    __token = 1992
                    try:
                        __zt_tmp = __attrs_4680815024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4921385088 = _static_4427992992('path', 'info/login_name', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'info/login_name' (57:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 125564e80> -> __condition
                    __expression = __cache_4921385088

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n            LOGIN_NAME\n          ')
                    else:
                        __content = __cache_4921385088
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n        </td>\n       </tr>')
                    ____index_4907862528 -= 1
                    if (____index_4907862528 > 0):
                        __append('\n       ')
                if (__backup_info_4660583376 is __marker):
                    del econtext['info']
                else:
                    econtext['info'] = __backup_info_4660583376
                __append('\n\n    </tbody>\n    </table>\n\n    ')

                # <Static value=<ast.Dict object at 0x1241759c0> name=None at 1279e5a50> -> __attrs_4905398864
                __attrs_4905398864 = _static_4900477376

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-group zmi-controls">\n      ')

                # <Static value=<ast.Dict object at 0x124117970> name=None at 124114ac0> -> __attrs_4958104464
                __attrs_4958104464 = _static_4900092272

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="user_ids:list:default" value="" />\n      ')

                # <Static value=<ast.Dict object at 0x125aec040> name=None at 126acceb0> -> __attrs_4921346080
                __attrs_4921346080 = _static_4927176768

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="submit" name="manage_removeUsers:method" class="btn btn-primary zmi-patch" value=" Remove Users " />\n    </div>\n  </form>\n\n  </div>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4891673792
            __attrs_4891673792 = _static_4428767312

            # <Value 'adding' (75:22)> -> __condition
            __token = 2403
            try:
                __zt_tmp = __attrs_4891673792
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'adding', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n  ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4932464896
                __attrs_4932464896 = _static_4428767312
                __backup_user_id_4960792112 = get('user_id', __marker)

                # <Value "request/user_id | python:''" (76:27)> -> __value
                __token = 2439
                try:
                    __zt_tmp = __attrs_4932464896
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', "request/user_id | python:''", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['user_id'] = __value
                __backup_login_name_4961058000 = get('login_name', __marker)

                # <Value "request/login_name | python:''" (77:29)> -> __value
                __token = 2497
                try:
                    __zt_tmp = __attrs_4932464896
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', "request/login_name | python:''", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['login_name'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n\n  ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4923841440
                __attrs_4923841440 = _static_4428767312

                # <h3 ... (0:0)
                # --------------------------------------------------------
                __append('<h3> Add a User </h3>\n\n  ')

                # <Static value=<ast.Dict object at 0x1257beef0> name=None at 12488de10> -> __attrs_4908144752
                __attrs_4908144752 = _static_4923846384

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form action="manage_addUser" method="POST">\n  ')

                # <Static value=<ast.Dict object at 0x1246456f0> name=None at 123e25840> -> __attrs_4932661600
                __attrs_4932661600 = _static_4905522928

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="csrf_token"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900429904
                __default_4900429904 = _DEFAULT_MARKER

                # <Substitution 'context/@@csrf_token/token' (84:31)> -> __attr_value
                __token = 2696
                try:
                    __zt_tmp = __attrs_4932661600
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'context/@@csrf_token/token', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n\n  ')

                # <Static value=<ast.Dict object at 0x126024af0> name=None at 126027ac0> -> __attrs_4905682448
                __attrs_4905682448 = _static_4932651760

                # <table ... (0:0)
                # --------------------------------------------------------
                __append('<table class="table table-sm">\n\n   ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4900114048
                __attrs_4900114048 = _static_4428767312

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n    ')

                # <Static value=<ast.Dict object at 0x113697820> name=None at 113694b50> -> __attrs_4673074944
                __attrs_4673074944 = _static_4620646432

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th scope="row">\n     ')

                # <Static value=<ast.Dict object at 0x127a90670> name=None at 124155ae0> -> __attrs_4960370448
                __attrs_4960370448 = _static_4960355952

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-label">User ID:</div>\n    </th>\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4960364448
                __attrs_4960364448 = _static_4428767312

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td>\n     ')

                # <Static value=<ast.Dict object at 0x127a91510> name=None at 127a937c0> -> __attrs_4960369344
                __attrs_4960369344 = _static_4960359696

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="text" name="user_id" size="20" class="form-control" />\n    </td>\n   </tr>\n\n   ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4960354656
                __attrs_4960354656 = _static_4428767312
                __backup_macroname_4936757056 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x127a911e0> name=None at 127a90b20> -> __value
                __value = _static_4960358880
                econtext['macroname'] = __value

                # <Value 'here/manage_widgets/macros/authentication_widgets' (97:27)> -> __macro
                __token = 2974
                try:
                    __zt_tmp = __attrs_4960354656
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_4427992992('path', 'here/manage_widgets/macros/authentication_widgets', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __token = 2974
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_4936757056 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_4936757056
                __append('\n\n  </table>\n\n  ')

                # <Static value=<ast.Dict object at 0x127a91d20> name=None at 127a91090> -> __attrs_4960368144
                __attrs_4960368144 = _static_4960361760

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-controls">\n    ')

                # <Static value=<ast.Dict object at 0x127a901f0> name=None at 127a90340> -> __attrs_4961550640
                __attrs_4961550640 = _static_4960354800

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="submit" value=" Add User " class="btn btn-primary" />\n  </div>\n  </form>\n\n  </div>')
                if (__backup_login_name_4961058000 is __marker):
                    del econtext['login_name']
                else:
                    econtext['login_name'] = __backup_login_name_4961058000
                if (__backup_user_id_4960792112 is __marker):
                    del econtext['user_id']
                else:
                    econtext['user_id'] = __backup_user_id_4960792112
                __append('\n  </div>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961558608
            __attrs_4961558608 = _static_4428767312

            # <Value 'passwd' (109:22)> -> __condition
            __token = 3203
            try:
                __zt_tmp = __attrs_4961558608
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'passwd', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n  ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961558080
                __attrs_4961558080 = _static_4428767312
                __backup_user_id_4960117776 = get('user_id', __marker)

                # <Value 'request/user_id' (110:27)> -> __value
                __token = 3239
                try:
                    __zt_tmp = __attrs_4961558080
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'request/user_id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['user_id'] = __value
                __backup_info_4960120608 = get('info', __marker)

                # <Value 'python:here.getUserInfo( user_id )' (111:23)> -> __value
                __token = 3279
                try:
                    __zt_tmp = __attrs_4961558080
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'here.getUserInfo( user_id )', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['info'] = __value
                __backup_login_name_4960124352 = get('login_name', __marker)

                # <Value 'info/login_name' (112:28)> -> __value
                __token = 3344
                try:
                    __zt_tmp = __attrs_4961558080
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'info/login_name', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['login_name'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n\n  ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961554240
                __attrs_4961554240 = _static_4428767312

                # <h3 ... (0:0)
                # --------------------------------------------------------
                __append('<h3> Update User Password ')

                # <Static value=<ast.Dict object at 0x127bb7fa0> name=None at 127bb7eb0> -> __attrs_4961554864
                __attrs_4961554864 = _static_4961566624

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961566432
                __default_4961566432 = _DEFAULT_MARKER

                # <Substitution 'string:?user_id=${user_id}' (116:52)> -> __attr_href
                __token = 3488
                try:
                    __zt_tmp = __attrs_4961554864
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4427992992('string', '?user_id=${user_id}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '?user_id=XXX', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' >(update user)</a></h3>\n\n  ')

                # <Static value=<ast.Dict object at 0x127bb4610> name=None at 127bb46a0> -> __attrs_4961550784
                __attrs_4961550784 = _static_4961551888

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form action="manage_updateUserPassword" method="POST">\n  ')

                # <Static value=<ast.Dict object at 0x127bb7040> name=None at 127bb7070> -> __attrs_4961552512
                __attrs_4961552512 = _static_4961562688

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="csrf_token"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961551504
                __default_4961551504 = _DEFAULT_MARKER

                # <Substitution 'context/@@csrf_token/token' (121:31)> -> __attr_value
                __token = 3699
                try:
                    __zt_tmp = __attrs_4961552512
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'context/@@csrf_token/token', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n  ')

                # <Static value=<ast.Dict object at 0x127bb4ac0> name=None at 127bb4970> -> __attrs_4961559088
                __attrs_4961559088 = _static_4961553088

                # <table ... (0:0)
                # --------------------------------------------------------
                __append('<table class="table table-sm">\n\n   ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961553472
                __attrs_4961553472 = _static_4428767312

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961554336
                __attrs_4961554336 = _static_4428767312

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>\n     ')

                # <Static value=<ast.Dict object at 0x127a56500> name=None at 127a56110> -> __attrs_4960117296
                __attrs_4960117296 = _static_4960118016

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-label">User ID:</div>\n    </th>\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4960120800
                __attrs_4960120800 = _static_4428767312

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td>\n     ')

                # <Static value=<ast.Dict object at 0x127a55d80> name=None at 127a55060> -> __attrs_4895394688
                __attrs_4895394688 = _static_4960116096

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="user_id" class="form-control"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4907987824
                __default_4907987824 = _DEFAULT_MARKER

                # <Substitution 'user_id' (130:34)> -> __attr_value
                __token = 3940
                try:
                    __zt_tmp = __attrs_4895394688
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'user_id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n     ')

                # <Static value=<ast.Dict object at 0x1247ebfd0> name=None at 1247e8d30> -> __attrs_4959934720
                __attrs_4959934720 = _static_4907253712

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-label">')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4909531040
                __default_4909531040 = _DEFAULT_MARKER

                # <Value 'user_id' (131:42)> -> __cache_4943217712
                __token = 3994
                try:
                    __zt_tmp = __attrs_4959934720
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4943217712 = _static_4427992992('path', 'user_id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'user_id' (131:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 124029ab0> -> __condition
                __expression = __cache_4943217712

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('USER_ID')
                else:
                    __content = __cache_4943217712
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</div>\n    </td>\n   </tr>\n\n   ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4960121472
                __attrs_4960121472 = _static_4428767312

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961589168
                __attrs_4961589168 = _static_4428767312

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>\n     ')

                # <Static value=<ast.Dict object at 0x127bbfd00> name=None at 127bbd2a0> -> __attrs_4961598528
                __attrs_4961598528 = _static_4961598720

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-label">Login name:</div>\n    </th>\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961588640
                __attrs_4961588640 = _static_4428767312

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td>\n      ')

                # <Static value=<ast.Dict object at 0x127bbff40> name=None at 127bbc640> -> __attrs_4961598960
                __attrs_4961598960 = _static_4961599296

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-control">')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961590224
                __default_4961590224 = _DEFAULT_MARKER

                # <Value 'login_name' (140:45)> -> __cache_4961583936
                __token = 4165
                try:
                    __zt_tmp = __attrs_4961598960
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4961583936 = _static_4427992992('path', 'login_name', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'login_name' (140:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 127bbdc00> -> __condition
                __expression = __cache_4961583936

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(' Login ')
                else:
                    __content = __cache_4961583936
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</div>\n    </td>\n   </tr>\n\n   ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961591952
                __attrs_4961591952 = _static_4428767312

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961598048
                __attrs_4961598048 = _static_4428767312

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>\n     ')

                # <Static value=<ast.Dict object at 0x127bbe4a0> name=None at 127bbedd0> -> __attrs_4961592240
                __attrs_4961592240 = _static_4961592480

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-label">Password:</div>\n    </th>\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961594016
                __attrs_4961594016 = _static_4428767312

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td>\n     ')

                # <Static value=<ast.Dict object at 0x127bbcf10> name=None at 127bbcb50> -> __attrs_4961597856
                __attrs_4961597856 = _static_4961586960

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="password" name="password" size="20" value="password" class="form-control" />\n    </td>\n   </tr>\n\n   ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961585760
                __attrs_4961585760 = _static_4428767312

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961595600
                __attrs_4961595600 = _static_4428767312

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>\n     ')

                # <Static value=<ast.Dict object at 0x127ac9ba0> name=None at 127ac91b0> -> __attrs_4960598384
                __attrs_4960598384 = _static_4960590752

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-label">Confirm password:</div>\n    </th>\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4960599776
                __attrs_4960599776 = _static_4428767312

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td>\n     ')

                # <Static value=<ast.Dict object at 0x127acaaa0> name=None at 127acb9d0> -> __attrs_4960597328
                __attrs_4960597328 = _static_4960594592

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="password" name="confirm" size="20" value="confirm" class="form-control" />\n    </td>\n   </tr>\n\n\n  </table>\n\n  ')

                # <Static value=<ast.Dict object at 0x127acabf0> name=None at 127acb0d0> -> __attrs_4960599440
                __attrs_4960599440 = _static_4960594928

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-controls">\n    ')

                # <Static value=<ast.Dict object at 0x127ac9e40> name=None at 127ac85b0> -> __attrs_4960596512
                __attrs_4960596512 = _static_4960591424

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="submit" value=" Update Password " class="btn btn-primary" />\n  </div>\n  </form>\n\n  </div>')
                if (__backup_login_name_4960124352 is __marker):
                    del econtext['login_name']
                else:
                    econtext['login_name'] = __backup_login_name_4960124352
                if (__backup_info_4960120608 is __marker):
                    del econtext['info']
                else:
                    econtext['info'] = __backup_info_4960120608
                if (__backup_user_id_4960117776 is __marker):
                    del econtext['user_id']
                else:
                    econtext['user_id'] = __backup_user_id_4960117776
                __append('\n  </div>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4960589024
            __attrs_4960589024 = _static_4428767312

            # <Value 'updating' (173:22)> -> __condition
            __token = 4791
            try:
                __zt_tmp = __attrs_4960589024
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'updating', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n  ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961058432
                __attrs_4961058432 = _static_4428767312
                __backup_user_id_4961545008 = get('user_id', __marker)

                # <Value 'request/user_id' (174:27)> -> __value
                __token = 4829
                try:
                    __zt_tmp = __attrs_4961058432
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'request/user_id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['user_id'] = __value
                __backup_info_4961545152 = get('info', __marker)

                # <Value 'python:here.getUserInfo(user_id)' (175:23)> -> __value
                __token = 4869
                try:
                    __zt_tmp = __attrs_4961058432
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', 'here.getUserInfo(user_id)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['info'] = __value
                __backup_login_name_4960788512 = get('login_name', __marker)

                # <Value 'info/login_name' (176:28)> -> __value
                __token = 4932
                try:
                    __zt_tmp = __attrs_4961058432
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('path', 'info/login_name', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['login_name'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div >\n  ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961054880
                __attrs_4961054880 = _static_4428767312

                # <h3 ... (0:0)
                # --------------------------------------------------------
                __append('<h3> Update User ')

                # <Static value=<ast.Dict object at 0x127b382b0> name=None at 127b3b7f0> -> __attrs_4961044272
                __attrs_4961044272 = _static_4961043120

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961051088
                __default_4961051088 = _DEFAULT_MARKER

                # <Substitution 'string:?user_id=${user_id}&passwd=1' (180:43)> -> __attr_href
                __token = 5073
                try:
                    __zt_tmp = __attrs_4961044272
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4427992992('string', '?user_id=${user_id}&passwd=1', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '?user_id=XXX&amp;passwd=1', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' >(change password)</a></h3>\n\n  ')

                # <Static value=<ast.Dict object at 0x127b3a6e0> name=None at 127b3a710> -> __attrs_4961051904
                __attrs_4961051904 = _static_4961052384

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form action="manage_updateUser" method="POST">\n  ')

                # <Static value=<ast.Dict object at 0x127b39570> name=None at 127b395d0> -> __attrs_4961043456
                __attrs_4961043456 = _static_4961047920

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="csrf_token"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961052624
                __default_4961052624 = _DEFAULT_MARKER

                # <Substitution 'context/@@csrf_token/token' (185:31)> -> __attr_value
                __token = 5284
                try:
                    __zt_tmp = __attrs_4961043456
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'context/@@csrf_token/token', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n  ')

                # <Static value=<ast.Dict object at 0x127b3b850> name=None at 127b3ba30> -> __attrs_4961051232
                __attrs_4961051232 = _static_4961056848

                # <table ... (0:0)
                # --------------------------------------------------------
                __append('<table class="table table-sm">\n\n   ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961046288
                __attrs_4961046288 = _static_4428767312

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961057568
                __attrs_4961057568 = _static_4428767312

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>\n     ')

                # <Static value=<ast.Dict object at 0x127b39990> name=None at 127b388e0> -> __attrs_4961044368
                __attrs_4961044368 = _static_4961048976

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-label">User ID:</div>\n    </th>\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961049648
                __attrs_4961049648 = _static_4428767312

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td>\n     ')

                # <Static value=<ast.Dict object at 0x1241efac0> name=None at 1241efa00> -> __attrs_4907343040
                __attrs_4907343040 = _static_4900977344

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="user_id" class="form-control"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4927128960
                __default_4927128960 = _DEFAULT_MARKER

                # <Substitution 'user_id' (194:34)> -> __attr_value
                __token = 5525
                try:
                    __zt_tmp = __attrs_4907343040
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'user_id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n     ')

                # <Static value=<ast.Dict object at 0x1241313c0> name=None at 124131420> -> __attrs_4899645632
                __attrs_4899645632 = _static_4900197312

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-label">')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4900197888
                __default_4900197888 = _DEFAULT_MARKER

                # <Value 'user_id' (195:42)> -> __cache_4900194432
                __token = 5579
                try:
                    __zt_tmp = __attrs_4899645632
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4900194432 = _static_4427992992('path', 'user_id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'user_id' (195:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 124131f00> -> __condition
                __expression = __cache_4900194432

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('USER_ID')
                else:
                    __content = __cache_4900194432
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</div>\n    </td>\n   </tr>\n\n   ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4921489776
                __attrs_4921489776 = _static_4428767312

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4921479168
                __attrs_4921479168 = _static_4428767312

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>\n     ')

                # <Static value=<ast.Dict object at 0x123952110> name=None at 1239526b0> -> __attrs_4894727120
                __attrs_4894727120 = _static_4891943184

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-label">Login name:</div>\n    </th>\n    ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4927032624
                __attrs_4927032624 = _static_4428767312

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td>\n     ')

                # <Static value=<ast.Dict object at 0x127af9330> name=None at 127afa410> -> __attrs_4960785104
                __attrs_4960785104 = _static_4960785200

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="text" name="login_name" size="40" class="form-control"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4960784576
                __default_4960784576 = _DEFAULT_MARKER

                # <Substitution 'login_name' (205:34)> -> __attr_value
                __token = 5812
                try:
                    __zt_tmp = __attrs_4960785104
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'login_name', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n    </td>\n   </tr>\n\n  </table>\n\n  ')

                # <Static value=<ast.Dict object at 0x127afa590> name=None at 125acbdc0> -> __attrs_4960795904
                __attrs_4960795904 = _static_4960789904

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-controls">\n    ')

                # <Static value=<ast.Dict object at 0x127afb490> name=None at 127af8a30> -> __attrs_4961539152
                __attrs_4961539152 = _static_4960793744

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="submit" value=" Update User " class="btn btn-primary" />\n  </div>\n  </form>\n\n  </div>')
                if (__backup_login_name_4960788512 is __marker):
                    del econtext['login_name']
                else:
                    econtext['login_name'] = __backup_login_name_4960788512
                if (__backup_info_4961545152 is __marker):
                    del econtext['info']
                else:
                    econtext['info'] = __backup_info_4961545152
                if (__backup_user_id_4961545008 is __marker):
                    del econtext['user_id']
                else:
                    econtext['user_id'] = __backup_user_id_4961545008
                __append('\n  </div>')
            __append('\n\n</main>')
            if (__backup_browsing_4960365600 is __marker):
                del econtext['browsing']
            else:
                econtext['browsing'] = __backup_browsing_4960365600
            if (__backup_updating_4961491728 is __marker):
                del econtext['updating']
            else:
                econtext['updating'] = __backup_updating_4961491728
            if (__backup_passwd_4961491584 is __marker):
                del econtext['passwd']
            else:
                econtext['passwd'] = __backup_passwd_4961491584
            if (__backup_adding_4961488800 is __marker):
                del econtext['adding']
            else:
                econtext['adding'] = __backup_adding_4961488800
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961534688
            __attrs_4961534688 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961534496
            __default_4961534496 = _DEFAULT_MARKER

            # <Value 'here/manage_page_footer' (222:27)> -> __cache_4961539632
            __token = 6043
            try:
                __zt_tmp = __attrs_4961534688
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4961539632 = _static_4427992992('path', 'here/manage_page_footer', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_page_footer' (222:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 127bb2bf0> -> __condition
            __expression = __cache_4961539632

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>Footer</h1>')
            else:
                __content = __cache_4961539632
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }