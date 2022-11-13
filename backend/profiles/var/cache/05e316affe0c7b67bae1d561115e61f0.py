# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/Products/CMFPlone/browser/templates/author.pt'

__tokens = {1088: ('context/@@plone_portal_state/navigation_root_url', 27, 43), 1178: (' context/@@plone_context_state/object_ur', 28, 40), 1258: ('l context/@@plone_portal_state/port', 29, 37), 1345: ('ss view/email_from_addr', 30, 48), 1408: ('hor view/au', 31, 35), 1461: ('name view/use', 32, 36), 1516: ('not: author', 34, 33), 1998: ('view/is_owner', 50, 32), 2043: (' view/is_anonymou', 51, 30), 2096: ('o author/info | nothi', 52, 33), 2151: ('it author/portrait | noth', 53, 30), 2213: ('nfo view/member_', 54, 32), 1958: ('author', 49, 35), 2271: ('context/global_statusmessage/macros/portal_message', 56, 34), 2271: ('context/global_statusmessage/macros/portal_message', 56, 34), 2662: ('portrait/absolute_url', 67, 40), 2772: ('authorinfo/fullname', 69, 35), 2826: ('authorinfo/fullname', 70, 33), 2987: ('not: authorinfo/fullname', 75, 35), 3046: ('username', 76, 33), 3162: ('not:isOwner', 80, 52), 3247: ('isOwner', 81, 71), 3333: ('${portal_url}/author/${view/member_info/url}', 83, 29), 3335: ('portal_url', 83, 31), 3356: ('view/member_info/url', 83, 52), 3485: ('${portal_url}/@@personal-information', 85, 46), 3487: ('portal_url', 85, 48), 3696: ('authorinfo/description', 90, 36), 3927: ('authorinfo/location', 96, 51), 4109: ('authorinfo/location', 99, 49), 4420: ('authorinfo/language', 106, 51), 4670: ('authorinfo/language', 111, 45), 4943: ('python:view.home_folder(username)', 119, 40), 5063: ('python:view.home_folder(username).absolute_url()', 121, 48), 5353: ("python: not view.home_folder(username) and authorinfo['home_page']", 127, 40), 5548: ('authorinfo/home_page', 130, 48), 5821: ('python:not email_from_address', 136, 55), 6231: ("python:not isAnon and not member_info.get('email', None)", 144, 50), 6725: ("python:email_from_address and authorinfo['has_email']", 153, 52), 6849: ('isAnon', 155, 67), 6941: ('string:$portal_url/login', 157, 51), 7436: ("python: not isOwner and not isAnon and member_info.get('email', None)", 169, 52), 7868: ('nocall:view/feedback_form', 177, 66), 7960: (' nocall:for', 178, 65), 8031: ('form/@@ploneform-macros/titlelessform', 179, 56), 8031: ('form/@@ploneform-macros/titlelessform', 179, 56), 8369: ('view/author_content', 187, 49), 8428: ('author_content', 188, 37), 10118: ('string:$here_url/search?Creator=${username}&amp;sort_on=created&amp;sort_order', 222, 50), 10416: ("python:authorinfo['fullname'] or username", 225, 82), 9274: ('author_content', 204, 55), 9385: ('item/date', 206, 55), 9716: ('item/url', 212, 64), 9782: ('item/title', 213, 56), 408: ("python:request.set('disable_border',1)", 11, 35), 495: (" python:request.set('disable_plone.leftcolumn',1", 12, 47), 592: ("o python:request.set('disable_plone.rightcolumn',", 13, 46), 261: ('context/@@main_template/macros/master', 6, 23), 261: ('context/@@main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4901958416 = 'master'
_static_4900698336 = {'href': '', }
_static_4900695360 = {'style': 'white-space: nowrap', }
_static_4900791600 = {'class': 'table', 'summary': 'Lists content written by an author grouped by content type', }
_static_4900699440 = {'href': '', }
_static_4900793424 = 'titlelessform'
_static_4900796976 = {'class': 'discreet', }
_static_4900796256 = {'class': 'btn btn-secondary', 'type': 'submit', 'value': 'Log in to send feedback', }
_static_4901176176 = {'action': 'string:$portal_url/login', }
_static_4901178240 = {'class': 'formControls', }
_static_4901180304 = {'class': 'discreet', }
_static_4901185584 = {'class': 'discreet', }
_static_4901189232 = {'href': '#', 'rel': 'nofollow', }
_static_4901180160 = {'href': '#', }
_static_4901534736 = {'class': 'visualClear', }
_static_4901532672 = {'class': 'discreet', }
_static_4901519424 = {'id': 'content-core', }
_static_4901530560 = {'class': 'documentDescription', }
_static_4901530176 = {'class': 'nav-link', 'href': '${portal_url}/@@personal-information', }
_static_4901527632 = {'class': 'nav-link active', 'href': '${portal_url}/author/${view/member_info/url}', }
_static_4901527680 = {'class': 'autotoc-nav nav nav-tabs', }
_static_4901521536 = {'class': 'autotabs', }
_static_4901735776 = {'class': 'documentFirstHeading', }
_static_4901740960 = {'class': 'documentFirstHeading', }
_static_4901736064 = {'src': '', 'alt': 'User portrait picture', 'class': 'portraitPhoto', }
_static_4901742160 = {'id': 'content', }
_static_4901738512 = 'portal_message'
_static_4901742832 = {'id': 'content', }
_static_4901744176 = {'class': 'portalMessage error', 'role': 'alert', }
_static_4439051040 = __C2ZContextWrapper
_static_4439058528 = __compile_zt_expr
_static_4438893776 = {}

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

    def render_main(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901961584
            __attrs_4901961584 = _static_4438893776
            __backup_portal_url_4877784672 = get('portal_url', __marker)

            # <Value 'context/@@plone_portal_state/navigation_root_url' (27:43)> -> __value
            __token = 1088
            try:
                __zt_tmp = __attrs_4901961584
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'context/@@plone_portal_state/navigation_root_url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['portal_url'] = __value
            __backup_here_url_4877557504 = get('here_url', __marker)

            # <Value 'context/@@plone_context_state/object_url' (28:40)> -> __value
            __token = 1178
            try:
                __zt_tmp = __attrs_4901961584
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'context/@@plone_context_state/object_url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['here_url'] = __value
            __backup_portal_4877557120 = get('portal', __marker)

            # <Value 'context/@@plone_portal_state/portal' (29:37)> -> __value
            __token = 1258
            try:
                __zt_tmp = __attrs_4901961584
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'context/@@plone_portal_state/portal', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['portal'] = __value
            __backup_email_from_address_4877557648 = get('email_from_address', __marker)

            # <Value 'view/email_from_address' (30:48)> -> __value
            __token = 1345
            try:
                __zt_tmp = __attrs_4901961584
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'view/email_from_address', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['email_from_address'] = __value
            __backup_author_4877132912 = get('author', __marker)

            # <Value 'view/author' (31:35)> -> __value
            __token = 1408
            try:
                __zt_tmp = __attrs_4901961584
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'view/author', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['author'] = __value
            __backup_username_4877128352 = get('username', __marker)

            # <Value 'view/username' (32:36)> -> __value
            __token = 1461
            try:
                __zt_tmp = __attrs_4901961584
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'view/username', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['username'] = __value
            __append('\n\n        ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901734864
            __attrs_4901734864 = _static_4438893776

            # <Value 'not: author' (34:33)> -> __condition
            __token = 1516
            try:
                __zt_tmp = __attrs_4901734864
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4439058528('not', ' author', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            if __condition:
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x1242aae30> name=None at 1242aaf80> -> __attrs_4901744848
                __attrs_4901744848 = _static_4901744176

                # <dl ... (0:0)
                # --------------------------------------------------------
                __append('<dl class="portalMessage error" role="alert">\n                ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901748592
                __attrs_4901748592 = _static_4438893776

                # <dt ... (0:0)
                # --------------------------------------------------------
                __append('<dt>')
                __stream_4901747344 = []
                __append_4901747344 = __stream_4901747344.append
                __append_4901747344('\n                    Error\n                ')
                __msgid_4901747344 = __re_whitespace(''.join(__stream_4901747344)).strip()
                if __msgid_4901747344:
                    __append(translate(__msgid_4901747344, mapping=None, default=__msgid_4901747344, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</dt>\n                ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901743024
                __attrs_4901743024 = _static_4438893776

                # <dd ... (0:0)
                # --------------------------------------------------------
                __append('<dd>')
                __stream_4901748352 = []
                __append_4901748352 = __stream_4901748352.append
                __append_4901748352('\n                    No user by that name.\n                ')
                __msgid_4901748352 = __re_whitespace(''.join(__stream_4901748352)).strip()
                if 'text_no_user_by_name':
                    __append(translate('text_no_user_by_name', mapping=None, default=__msgid_4901748352, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</dd>\n            </dl>\n            ')

                # <Static value=<ast.Dict object at 0x1242aa8f0> name=None at 1242ab640> -> __attrs_4901745952
                __attrs_4901745952 = _static_4901742832

                # <article ... (0:0)
                # --------------------------------------------------------
                __append('<article id="content">\n                &nbsp;\n            </article>\n        ')
            __append('\n\n\n        ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901742928
            __attrs_4901742928 = _static_4438893776
            __backup_isOwner_4874867024 = get('isOwner', __marker)

            # <Value 'view/is_owner' (50:32)> -> __value
            __token = 1998
            try:
                __zt_tmp = __attrs_4901742928
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'view/is_owner', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['isOwner'] = __value
            __backup_isAnon_4874864768 = get('isAnon', __marker)

            # <Value 'view/is_anonymous' (51:30)> -> __value
            __token = 2043
            try:
                __zt_tmp = __attrs_4901742928
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'view/is_anonymous', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['isAnon'] = __value
            __backup_authorinfo_4874870576 = get('authorinfo', __marker)

            # <Value 'author/info | nothing' (52:33)> -> __value
            __token = 2096
            try:
                __zt_tmp = __attrs_4901742928
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'author/info | nothing', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['authorinfo'] = __value
            __backup_portrait_4879774960 = get('portrait', __marker)

            # <Value 'author/portrait | nothing' (53:30)> -> __value
            __token = 2151
            try:
                __zt_tmp = __attrs_4901742928
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'author/portrait | nothing', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['portrait'] = __value
            __backup_member_info_4877554384 = get('member_info', __marker)

            # <Value 'view/member_info' (54:32)> -> __value
            __token = 2213
            try:
                __zt_tmp = __attrs_4901742928
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'view/member_info', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['member_info'] = __value

            # <Value 'author' (49:35)> -> __condition
            __token = 1958
            try:
                __zt_tmp = __attrs_4901742928
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4439058528('path', 'author', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            if __condition:
                __append('\n\n            ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901741248
                __attrs_4901741248 = _static_4438893776
                __backup_macroname_4902420928 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x1242a9810> name=None at 1242a8610> -> __value
                __value = _static_4901738512
                econtext['macroname'] = __value

                # <Value 'context/global_statusmessage/macros/portal_message' (56:34)> -> __macro
                __token = 2271
                try:
                    __zt_tmp = __attrs_4901741248
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_4439058528('path', 'context/global_statusmessage/macros/portal_message', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __token = 2271
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_4902420928 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_4902420928
                __append('\n\n            ')

                # <Static value=<ast.Dict object at 0x1242aa650> name=None at 1242a97b0> -> __attrs_4901738656
                __attrs_4901738656 = _static_4901742160

                # <article ... (0:0)
                # --------------------------------------------------------
                __append('<article id="content">\n                <!-- Author information -->\n\n                ')

                # <Static value=<ast.Dict object at 0x1242a8e80> name=None at 1242a9b10> -> __attrs_4901740240
                __attrs_4901740240 = _static_4901736064

                # <img ... (0:0)
                # --------------------------------------------------------
                __append('<img')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901738704
                __default_4901738704 = _DEFAULT_MARKER

                # <Substitution 'portrait/absolute_url' (67:40)> -> __attr_src
                __token = 2662
                try:
                    __zt_tmp = __attrs_4901740240
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_src = _static_4439058528('path', 'portrait/absolute_url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __attr_src = __quote(__attr_src, '"', '&quot;', '', _DEFAULT_MARKER)
                if (__attr_src is not None):
                    __append((' src="%s"' % __attr_src))

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901739856
                __default_4901739856 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x1242a85e0> at 1242a9030> -> __attr_alt
                __attr_alt = 'User portrait picture'
                __attr_alt = translate(__attr_alt, default=__attr_alt, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_alt is not None):
                    __append((' alt="%s"' % __attr_alt))
                __append(' class="portraitPhoto" />\n                ')

                # <Static value=<ast.Dict object at 0x1242aa1a0> name=None at 1242a9060> -> __attrs_4901732416
                __attrs_4901732416 = _static_4901740960

                # <Value 'authorinfo/fullname' (69:35)> -> __condition
                __token = 2772
                try:
                    __zt_tmp = __attrs_4901732416
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('path', 'authorinfo/fullname', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:

                    # <h1 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h1 class="documentFirstHeading">')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901740912
                    __default_4901740912 = _DEFAULT_MARKER

                    # <Value 'authorinfo/fullname' (70:33)> -> __cache_4901740000
                    __token = 2826
                    try:
                        __zt_tmp = __attrs_4901732416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4901740000 = _static_4439058528('path', 'authorinfo/fullname', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value 'authorinfo/fullname' (70:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1242aa140> -> __condition
                    __expression = __cache_4901740000

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                    Author name\n                ')
                    else:
                        __content = __cache_4901740000
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</h1>')
                __append('\n\n                ')

                # <Static value=<ast.Dict object at 0x1242a8d60> name=None at 1242a8df0> -> __attrs_4901520192
                __attrs_4901520192 = _static_4901735776

                # <Value 'not: authorinfo/fullname' (75:35)> -> __condition
                __token = 2987
                try:
                    __zt_tmp = __attrs_4901520192
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('not', ' authorinfo/fullname', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:

                    # <h1 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h1 class="documentFirstHeading">')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901735056
                    __default_4901735056 = _DEFAULT_MARKER

                    # <Value 'username' (76:33)> -> __cache_4901737216
                    __token = 3046
                    try:
                        __zt_tmp = __attrs_4901520192
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4901737216 = _static_4439058528('path', 'username', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value 'username' (76:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1242a8bb0> -> __condition
                    __expression = __cache_4901737216

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                    Author ID\n                ')
                    else:
                        __content = __cache_4901737216
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</h1>')
                __append('\n\n                ')

                # <Static value=<ast.Dict object at 0x124274880> name=None at 124274d90> -> __attrs_4901521344
                __attrs_4901521344 = _static_4901521536

                # <Negate value=<Value 'not:isOwner' (80:52)> at 124275180> -> __cache_4901523840

                # <Value 'not:isOwner' (80:52)> -> __cache_4901523840
                __token = 3162
                try:
                    __zt_tmp = __attrs_4901521344
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4901523840 = _static_4439058528('not', 'isOwner', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __cache_4901523840 = not __cache_4901523840
                __condition = __cache_4901523840
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="autotabs">')
                __append('\n                  ')

                # <Static value=<ast.Dict object at 0x124276080> name=None at 124275480> -> __attrs_4901522256
                __attrs_4901522256 = _static_4901527680

                # <Value 'isOwner' (81:71)> -> __condition
                __token = 3247
                try:
                    __zt_tmp = __attrs_4901522256
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('path', 'isOwner', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:

                    # <nav ... (0:0)
                    # --------------------------------------------------------
                    __append('<nav class="autotoc-nav nav nav-tabs">\n                    ')

                    # <Static value=<ast.Dict object at 0x124276050> name=None at 124275ff0> -> __attrs_4901527056
                    __attrs_4901527056 = _static_4901527632

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a class="nav-link active"')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901524224
                    __default_4901524224 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution '${portal_url}/author/${view/member_info/url}' (83:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 124275ae0> -> __attr_href
                    __token = 3333
                    __token = 3335
                    try:
                        __zt_tmp = __attrs_4901527056
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4439058528('path', 'portal_url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    __token = 3356
                    try:
                        __zt_tmp = __attrs_4901527056
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href_3354 = _static_4439058528('path', 'view/member_info/url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    __attr_href_3354 = __quote(__attr_href_3354, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_href = ('%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/author/', (__attr_href_3354 if (__attr_href_3354 is not None) else ''), ))
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
                    __append('>')
                    __stream_4901524272 = []
                    __append_4901524272 = __stream_4901524272.append
                    __append_4901524272('View')
                    __msgid_4901524272 = __re_whitespace(''.join(__stream_4901524272)).strip()
                    if 'label_view':
                        __append(translate('label_view', mapping=None, default=__msgid_4901524272, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</a>\n                    ')

                    # <Static value=<ast.Dict object at 0x124276a40> name=None at 124277190> -> __attrs_4901535072
                    __attrs_4901535072 = _static_4901530176

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a class="nav-link"')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901527344
                    __default_4901527344 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution '${portal_url}/@@personal-information' (85:46)> braces_required=True translation=False default='"?"' default_marker='"?"' at 124274e80> -> __attr_href
                    __token = 3485
                    __token = 3487
                    try:
                        __zt_tmp = __attrs_4901535072
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4439058528('path', 'portal_url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_href = ('%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/@@personal-information', ))
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
                    __append('>')
                    __stream_4901525760 = []
                    __append_4901525760 = __stream_4901525760.append
                    __append_4901525760('Edit')
                    __msgid_4901525760 = __re_whitespace(''.join(__stream_4901525760)).strip()
                    if 'label_edit':
                        __append(translate('label_edit', mapping=None, default=__msgid_4901525760, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</a>\n                  </nav>')
                __append('\n\n                  ')

                # <Static value=<ast.Dict object at 0x124276bc0> name=None at 1242758a0> -> __attrs_4901529360
                __attrs_4901529360 = _static_4901530560

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="documentDescription">')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901531280
                __default_4901531280 = _DEFAULT_MARKER

                # <Value 'authorinfo/description' (90:36)> -> __cache_4901525952
                __token = 3696
                try:
                    __zt_tmp = __attrs_4901529360
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4901525952 = _static_4439058528('path', 'authorinfo/description', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'authorinfo/description' (90:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 124276f80> -> __condition
                __expression = __cache_4901525952

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n                      Author description.\n                  ')
                else:
                    __content = __cache_4901525952
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</div>\n\n                  ')

                # <Static value=<ast.Dict object at 0x124274040> name=None at 124274a60> -> __attrs_4901529984
                __attrs_4901529984 = _static_4901519424

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n                      ')

                # <Static value=<ast.Dict object at 0x124277400> name=None at 1242773d0> -> __attrs_4901533440
                __attrs_4901533440 = _static_4901532672

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="discreet">\n                          ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901523408
                __attrs_4901523408 = _static_4438893776

                # <Value 'authorinfo/location' (96:51)> -> __condition
                __token = 3927
                try:
                    __zt_tmp = __attrs_4901523408
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('path', 'authorinfo/location', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:
                    __stream_4901358272_location = ''
                    __stream_4901533296 = []
                    __append_4901533296 = __stream_4901533296.append
                    __append_4901533296('\n                              Location:\n                              ')
                    __stream_4901358272_location = []
                    __append_4901358272_location = __stream_4901358272_location.append

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901529648
                    __attrs_4901529648 = _static_4438893776

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901532192
                    __default_4901532192 = _DEFAULT_MARKER

                    # <Value 'authorinfo/location' (99:49)> -> __cache_4901532240
                    __token = 4109
                    try:
                        __zt_tmp = __attrs_4901529648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4901532240 = _static_4439058528('path', 'authorinfo/location', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value 'authorinfo/location' (99:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 124276680> -> __condition
                    __expression = __cache_4901532240

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append_4901358272_location('\n                                  Some location\n                              ')
                    else:
                        __content = __cache_4901532240
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_4901358272_location(__content)
                    __append_4901533296('${location}')
                    __stream_4901358272_location = ''.join(__stream_4901358272_location)
                    __append_4901533296('\n                          ')
                    __msgid_4901533296 = __re_whitespace(''.join(__stream_4901533296)).strip()
                    if 'text_location':
                        __append(translate('text_location', mapping={'location': __stream_4901358272_location, }, default=__msgid_4901533296, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n\n                          ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901532528
                __attrs_4901532528 = _static_4438893776

                # <Value 'authorinfo/language' (106:51)> -> __condition
                __token = 4420
                try:
                    __zt_tmp = __attrs_4901532528
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('path', 'authorinfo/language', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:
                    __append('\n                          &mdash;\n                          ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901189136
                    __attrs_4901189136 = _static_4438893776

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_4901530704 = []
                    __append_4901530704 = __stream_4901530704.append
                    __append_4901530704('\n                              Main Language:\n                          ')
                    __msgid_4901530704 = __re_whitespace(''.join(__stream_4901530704)).strip()
                    if 'label_main_language':
                        __append(translate('label_main_language', mapping=None, default=__msgid_4901530704, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n                          ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901187024
                    __attrs_4901187024 = _static_4438893776

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901186976
                    __default_4901186976 = _DEFAULT_MARKER

                    # <Value 'authorinfo/language' (111:45)> -> __cache_4901188176
                    __token = 4670
                    try:
                        __zt_tmp = __attrs_4901187024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4901188176 = _static_4439058528('path', 'authorinfo/language', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value 'authorinfo/language' (111:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 124221d80> -> __condition
                    __expression = __cache_4901188176

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>\n                            Some language\n                          </span>')
                    else:
                        __content = __cache_4901188176
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n                          ')
                __append('\n                      </div>\n\n                      ')

                # <Static value=<ast.Dict object at 0x124277c10> name=None at 1242775e0> -> __attrs_4901189760
                __attrs_4901189760 = _static_4901534736

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="visualClear"><!-- --></div>\n\n                      ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901183376
                __attrs_4901183376 = _static_4438893776

                # <Value 'python:view.home_folder(username)' (119:40)> -> __condition
                __token = 4943
                try:
                    __zt_tmp = __attrs_4901183376
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('python', 'view.home_folder(username)', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p>\n                        ')

                    # <Static value=<ast.Dict object at 0x124221300> name=None at 1242209d0> -> __attrs_4901190432
                    __attrs_4901190432 = _static_4901180160

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901178288
                    __default_4901178288 = _DEFAULT_MARKER

                    # <Substitution 'python:view.home_folder(username).absolute_url()' (121:48)> -> __attr_href
                    __token = 5063
                    try:
                        __zt_tmp = __attrs_4901190432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4439058528('python', 'view.home_folder(username).absolute_url()', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append('>')
                    __stream_4901191056 = []
                    __append_4901191056 = __stream_4901191056.append
                    __append_4901191056("\n                          Author's home page in this site&hellip;\n                        ")
                    __msgid_4901191056 = __re_whitespace(''.join(__stream_4901191056)).strip()
                    if 'label_author_internal_home_page':
                        __append(translate('label_author_internal_home_page', mapping=None, default=__msgid_4901191056, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</a>\n                      </p>')
                __append('\n\n                      ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901191632
                __attrs_4901191632 = _static_4438893776

                # <Value "python: not view.home_folder(username) and authorinfo['home_page']" (127:40)> -> __condition
                __token = 5353
                try:
                    __zt_tmp = __attrs_4901191632
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('python', " not view.home_folder(username) and authorinfo['home_page']", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p>\n                        ')

                    # <Static value=<ast.Dict object at 0x124223670> name=None at 124220130> -> __attrs_4901184144
                    __attrs_4901184144 = _static_4901189232

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901187552
                    __default_4901187552 = _DEFAULT_MARKER

                    # <Substitution 'authorinfo/home_page' (130:48)> -> __attr_href
                    __token = 5548
                    try:
                        __zt_tmp = __attrs_4901184144
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4439058528('path', 'authorinfo/home_page', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' rel="nofollow">')
                    __stream_4901176128 = []
                    __append_4901176128 = __stream_4901176128.append
                    __append_4901176128("\n                          Author's external home page&hellip;\n                        ")
                    __msgid_4901176128 = __re_whitespace(''.join(__stream_4901176128)).strip()
                    if 'label_author_external_home_page':
                        __append(translate('label_author_external_home_page', mapping=None, default=__msgid_4901176128, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</a>\n                      </p>')
                __append('\n\n                      ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901184576
                __attrs_4901184576 = _static_4438893776

                # <Value 'python:not email_from_address' (136:55)> -> __condition
                __token = 5821
                try:
                    __zt_tmp = __attrs_4901184576
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('python', 'not email_from_address', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:
                    __append('\n                          ')

                    # <Static value=<ast.Dict object at 0x124222830> name=None at 1242216f0> -> __attrs_4901185632
                    __attrs_4901185632 = _static_4901185584

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="discreet">')
                    __stream_4901184528 = []
                    __append_4901184528 = __stream_4901184528.append
                    __append_4901184528("\n                              This site doesn't have a valid email setup, so you cannot use\n                              any contact forms.\n                          ")
                    __msgid_4901184528 = __re_whitespace(''.join(__stream_4901184528)).strip()
                    if 'text_no_email_setup':
                        __append(translate('text_no_email_setup', mapping=None, default=__msgid_4901184528, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>\n                      ')
                __append('\n\n                      ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901181360
                __attrs_4901181360 = _static_4438893776

                # <Value "python:not isAnon and not member_info.get('email', None)" (144:50)> -> __condition
                __token = 6231
                try:
                    __zt_tmp = __attrs_4901181360
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('python', "not isAnon and not member_info.get('email', None)", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:
                    __append('\n                          ')

                    # <Static value=<ast.Dict object at 0x124221390> name=None at 1242213c0> -> __attrs_4901186736
                    __attrs_4901186736 = _static_4901180304

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="discreet">')
                    __stream_4901185920 = []
                    __append_4901185920 = __stream_4901185920.append
                    __append_4901185920('\n                              You do not have an email address, so you\n                              cannot use any contact forms. Please edit\n                              your personal information.\n                          ')
                    __msgid_4901185920 = __re_whitespace(''.join(__stream_4901185920)).strip()
                    if 'text_no_member_email':
                        __append(translate('text_no_member_email', mapping=None, default=__msgid_4901185920, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>\n                      ')
                __append('\n\n                      ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901179296
                __attrs_4901179296 = _static_4438893776

                # <Value "python:email_from_address and authorinfo['has_email']" (153:52)> -> __condition
                __token = 6725
                try:
                    __zt_tmp = __attrs_4901179296
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('python', "email_from_address and authorinfo['has_email']", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:
                    __append('\n\n                          ')

                    # <Static value=<ast.Dict object at 0x124220b80> name=None at 124220b50> -> __attrs_4901176896
                    __attrs_4901176896 = _static_4901178240

                    # <Value 'isAnon' (155:67)> -> __condition
                    __token = 6849
                    try:
                        __zt_tmp = __attrs_4901176896
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4439058528('path', 'isAnon', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="formControls">\n                          ')

                        # <Static value=<ast.Dict object at 0x124220370> name=None at 124220070> -> __attrs_4900785792
                        __attrs_4900785792 = _static_4901176176

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append('<form')

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4901176512
                        __default_4901176512 = _DEFAULT_MARKER

                        # <Substitution 'string:$portal_url/login' (157:51)> -> __attr_action
                        __token = 6941
                        try:
                            __zt_tmp = __attrs_4900785792
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_action = _static_4439058528('string', '$portal_url/login', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_action is not None):
                            __append((' action="%s"' % __attr_action))
                        __append('>\n                             ')

                        # <Static value=<ast.Dict object at 0x1241c3760> name=None at 1241c3d90> -> __attrs_4900796832
                        __attrs_4900796832 = _static_4900796256

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-secondary" type="submit"')

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900797792
                        __default_4900797792 = _DEFAULT_MARKER

                        # <Translate msgid='label_login_to_send_feedback' node=<ast.Constant object at 0x1241c3610> at 1241c3a00> -> __attr_value
                        __attr_value = 'Log in to send feedback'
                        __attr_value = translate('label_login_to_send_feedback', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' />\n                          </form>\n                          </div>')
                    __append('\n\n                          <!-- feedback form -->\n\n\n                          ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900796784
                    __attrs_4900796784 = _static_4438893776

                    # <Value "python: not isOwner and not isAnon and member_info.get('email', None)" (169:52)> -> __condition
                    __token = 7436
                    try:
                        __zt_tmp = __attrs_4900796784
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4439058528('python', " not isOwner and not isAnon and member_info.get('email', None)", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    if __condition:
                        __append('\n                              ')

                        # <Static value=<ast.Dict object at 0x1241c3a30> name=None at 1241c3ac0> -> __attrs_4900795392
                        __attrs_4900795392 = _static_4900796976

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append('<p class="discreet">')
                        __stream_4900798272 = []
                        __append_4900798272 = __stream_4900798272.append
                        __append_4900798272('\n                                  If you want to contact this author, fill in the form\n                                  below.\n                              ')
                        __msgid_4900798272 = __re_whitespace(''.join(__stream_4900798272)).strip()
                        if 'description_author_feedback':
                            __append(translate('description_author_feedback', mapping=None, default=__msgid_4900798272, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</p>\n\n\n                              ')

                        # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900789776
                        __attrs_4900789776 = _static_4438893776
                        __backup_form_4880497824 = get('form', __marker)

                        # <Value 'nocall:view/feedback_form' (177:66)> -> __value
                        __token = 7868
                        try:
                            __zt_tmp = __attrs_4900789776
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4439058528('nocall', 'view/feedback_form', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        econtext['form'] = __value
                        __backup_view_4880312752 = get('view', __marker)

                        # <Value 'nocall:form' (178:65)> -> __value
                        __token = 7960
                        try:
                            __zt_tmp = __attrs_4900789776
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4439058528('nocall', 'form', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        econtext['view'] = __value
                        __append('\n                                ')

                        # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900793856
                        __attrs_4900793856 = _static_4438893776
                        __backup_macroname_4900517888 = get('macroname', __marker)

                        # <Static value=<ast.Constant object at 0x1241c2c50> name=None at 1241c2c80> -> __value
                        __value = _static_4900793424
                        econtext['macroname'] = __value

                        # <Value 'form/@@ploneform-macros/titlelessform' (179:56)> -> __macro
                        __token = 8031
                        try:
                            __zt_tmp = __attrs_4900793856
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __macro = _static_4439058528('path', 'form/@@ploneform-macros/titlelessform', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        __token = 8031
                        __m = __macro.include
                        __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                        econtext.update(rcontext)
                        if (__backup_macroname_4900517888 is __marker):
                            del econtext['macroname']
                        else:
                            econtext['macroname'] = __backup_macroname_4900517888
                        __append('\n                              ')
                        if (__backup_view_4880312752 is __marker):
                            del econtext['view']
                        else:
                            econtext['view'] = __backup_view_4880312752
                        if (__backup_form_4880497824 is __marker):
                            del econtext['form']
                        else:
                            econtext['form'] = __backup_form_4880497824
                        __append('\n\n                          ')
                    __append('\n                      ')
                __append('\n\n                      <!-- listing of content created by this user -->\n                      ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900794816
                __attrs_4900794816 = _static_4438893776
                __backup_author_content_4850903424 = get('author_content', __marker)

                # <Value 'view/author_content' (187:49)> -> __value
                __token = 8369
                try:
                    __zt_tmp = __attrs_4900794816
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'view/author_content', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['author_content'] = __value

                # <Value 'author_content' (188:37)> -> __condition
                __token = 8428
                try:
                    __zt_tmp = __attrs_4900794816
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('path', 'author_content', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:
                    __append('\n\n                          ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900793280
                    __attrs_4900793280 = _static_4438893776

                    # <h2 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h2>')
                    __stream_4900782288 = []
                    __append_4900782288 = __stream_4900782288.append
                    __append_4900782288('\n                              Latest content created by this user\n                          ')
                    __msgid_4900782288 = __re_whitespace(''.join(__stream_4900782288)).strip()
                    if 'heading_author_content':
                        __append(translate('heading_author_content', mapping=None, default=__msgid_4900782288, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</h2>\n\n                          ')
                    __token = None
                    render_user_content_listing(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    __append('\n\n                          ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900691664
                    __attrs_4900691664 = _static_4438893776

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p>\n                          ')

                    # <Static value=<ast.Dict object at 0x1241abd30> name=None at 1241abdf0> -> __attrs_4900700064
                    __attrs_4900700064 = _static_4900699440

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900694448
                    __default_4900694448 = _DEFAULT_MARKER

                    # <Substitution 'string:$here_url/search?Creator=${username}&sort_on=created&sort_order=reverse' (222:50)> -> __attr_href
                    __token = 10118
                    try:
                        __zt_tmp = __attrs_4900700064
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4439058528('string', '$here_url/search?Creator=${username}&sort_on=created&sort_order=reverse', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append('>')
                    __stream_4901357824_user = ''
                    __stream_4900697616 = []
                    __append_4900697616 = __stream_4900697616.append
                    __append_4900697616('\n                              All content created by\n                              ')
                    __stream_4901357824_user = []
                    __append_4901357824_user = __stream_4901357824_user.append

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900684608
                    __attrs_4900684608 = _static_4438893776

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900692816
                    __default_4900692816 = _DEFAULT_MARKER

                    # <Value "python:authorinfo['fullname'] or username" (225:82)> -> __cache_4900691712
                    __token = 10416
                    try:
                        __zt_tmp = __attrs_4900684608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4900691712 = _static_4439058528('python', "authorinfo['fullname'] or username", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:authorinfo['fullname'] or username" (225:82)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1241aa1d0> -> __condition
                    __expression = __cache_4900691712

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4900691712
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_4901357824_user(__content)
                    __append_4900697616('${user}')
                    __stream_4901357824_user = ''.join(__stream_4901357824_user)
                    __append_4900697616('&hellip;\n                          ')
                    __msgid_4900697616 = __re_whitespace(''.join(__stream_4900697616)).strip()
                    if 'go_to_search_author_content':
                        __append(translate('go_to_search_author_content', mapping={'user': __stream_4901357824_user, }, default=__msgid_4900697616, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</a>\n                          </p>\n\n                      ')
                if (__backup_author_content_4850903424 is __marker):
                    del econtext['author_content']
                else:
                    econtext['author_content'] = __backup_author_content_4850903424
                __append('\n                  </div>\n                ')
                __condition = __cache_4901523840
                if __condition:
                    __append('</div>')
                __append('\n\n            </article>\n\n        ')
            if (__backup_member_info_4877554384 is __marker):
                del econtext['member_info']
            else:
                econtext['member_info'] = __backup_member_info_4877554384
            if (__backup_portrait_4879774960 is __marker):
                del econtext['portrait']
            else:
                econtext['portrait'] = __backup_portrait_4879774960
            if (__backup_authorinfo_4874870576 is __marker):
                del econtext['authorinfo']
            else:
                econtext['authorinfo'] = __backup_authorinfo_4874870576
            if (__backup_isAnon_4874864768 is __marker):
                del econtext['isAnon']
            else:
                econtext['isAnon'] = __backup_isAnon_4874864768
            if (__backup_isOwner_4874867024 is __marker):
                del econtext['isOwner']
            else:
                econtext['isOwner'] = __backup_isOwner_4874867024
            __append('\n\n    ')
            if (__backup_username_4877128352 is __marker):
                del econtext['username']
            else:
                econtext['username'] = __backup_username_4877128352
            if (__backup_author_4877132912 is __marker):
                del econtext['author']
            else:
                econtext['author'] = __backup_author_4877132912
            if (__backup_email_from_address_4877557648 is __marker):
                del econtext['email_from_address']
            else:
                econtext['email_from_address'] = __backup_email_from_address_4877557648
            if (__backup_portal_4877557120 is __marker):
                del econtext['portal']
            else:
                econtext['portal'] = __backup_portal_4877557120
            if (__backup_here_url_4877557504 is __marker):
                del econtext['here_url']
            else:
                econtext['here_url'] = __backup_here_url_4877557504
            if (__backup_portal_url_4877784672 is __marker):
                del econtext['portal_url']
            else:
                econtext['portal_url'] = __backup_portal_url_4877784672
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_user_content_listing(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900792080
            __attrs_4900792080 = _static_4438893776

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div>\n                          ')

            # <Static value=<ast.Dict object at 0x1241c2530> name=None at 1241c2560> -> __attrs_4900790640
            __attrs_4900790640 = _static_4900791600

            # <table ... (0:0)
            # --------------------------------------------------------
            __append('<table class="table"')

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900790064
            __default_4900790064 = _DEFAULT_MARKER

            # <Translate msgid='summary_author_content_list' node=<ast.Constant object at 0x1241c2440> at 1241c2350> -> __attr_summary
            __attr_summary = 'Lists content written by an author grouped by content type'
            __attr_summary = translate('summary_author_content_list', default=__attr_summary, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_summary is not None):
                __append((' summary="%s"' % __attr_summary))
            __append('>\n                              ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900788288
            __attrs_4900788288 = _static_4438893776

            # <thead ... (0:0)
            # --------------------------------------------------------
            __append('<thead>\n                                ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900786416
            __attrs_4900786416 = _static_4438893776

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append('<tr>\n                                    ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900786080
            __attrs_4900786080 = _static_4438893776

            # <th ... (0:0)
            # --------------------------------------------------------
            __append('<th>')
            __stream_4900783200 = []
            __append_4900783200 = __stream_4900783200.append
            __append_4900783200('Date')
            __msgid_4900783200 = __re_whitespace(''.join(__stream_4900783200)).strip()
            if __msgid_4900783200:
                __append(translate(__msgid_4900783200, mapping=None, default=__msgid_4900783200, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</th>\n                                    ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900782144
            __attrs_4900782144 = _static_4438893776

            # <th ... (0:0)
            # --------------------------------------------------------
            __append('<th>')
            __stream_4900784400 = []
            __append_4900784400 = __stream_4900784400.append
            __append_4900784400('Content')
            __msgid_4900784400 = __re_whitespace(''.join(__stream_4900784400)).strip()
            if __msgid_4900784400:
                __append(translate(__msgid_4900784400, mapping=None, default=__msgid_4900784400, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</th>\n                                </tr>\n                              </thead>\n                              ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900784496
            __attrs_4900784496 = _static_4438893776
            __backup_item_4879769104 = get('item', __marker)

            # <Value 'author_content' (204:55)> -> __iterator
            __token = 9274
            try:
                __zt_tmp = __attrs_4900784496
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4439058528('path', 'author_content', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            (__iterator, ____index_4900783344, ) = getname('repeat')('item', __iterator)
            econtext['item'] = None
            for __item in __iterator:
                econtext['item'] = __item
                __append('\n                                  ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900693248
                __attrs_4900693248 = _static_4438893776

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n                                      ')

                # <Static value=<ast.Dict object at 0x1241aad40> name=None at 1241a8550> -> __attrs_4900695744
                __attrs_4900695744 = _static_4900695360

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th style="white-space: nowrap">')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900694976
                __default_4900694976 = _DEFAULT_MARKER

                # <Value 'item/date' (206:55)> -> __cache_4900691952
                __token = 9385
                try:
                    __zt_tmp = __attrs_4900695744
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4900691952 = _static_4439058528('path', 'item/date', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'item/date' (206:55)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1241aab00> -> __condition
                __expression = __cache_4900691952

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n                                          Date\n                                      ')
                else:
                    __content = __cache_4900691952
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</th>\n                                      ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900694256
                __attrs_4900694256 = _static_4438893776

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td>\n                                        ')

                # <Static value=<ast.Dict object at 0x1241ab8e0> name=None at 1241ab8b0> -> __attrs_4900697760
                __attrs_4900697760 = _static_4900698336

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900698384
                __default_4900698384 = _DEFAULT_MARKER

                # <Substitution 'item/url' (212:64)> -> __attr_href
                __token = 9716
                try:
                    __zt_tmp = __attrs_4900697760
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4439058528('path', 'item/url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append('>')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900694736
                __default_4900694736 = _DEFAULT_MARKER

                # <Value 'item/title' (213:56)> -> __cache_4900698960
                __token = 9782
                try:
                    __zt_tmp = __attrs_4900697760
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4900698960 = _static_4439058528('path', 'item/title', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'item/title' (213:56)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1241abc40> -> __condition
                __expression = __cache_4900698960

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('title')
                else:
                    __content = __cache_4900698960
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</a>\n                                      </td>\n                                  </tr>\n                              ')
                ____index_4900783344 -= 1
                if (____index_4900783344 > 0):
                    __append('')
            if (__backup_item_4879769104 is __marker):
                del econtext['item']
            else:
                econtext['item'] = __backup_item_4879769104
            __append('\n                          </table>\n                          </div>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901957024
            __attrs_4901957024 = _static_4438893776
            __previous_i18n_domain_4901954432 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4902583296 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x1242df310> name=None at 1242dedd0> -> __value
            __value = _static_4901958416
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901950304
                __attrs_4901950304 = _static_4438893776
                __backup_dummy_4685603136 = get('dummy', __marker)

                # <Value "python:request.set('disable_border',1)" (11:35)> -> __value
                __token = 408
                try:
                    __zt_tmp = __attrs_4901950304
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', "request.set('disable_border',1)", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['dummy'] = __value
                __backup_disable_column_one_4689333888 = get('disable_column_one', __marker)

                # <Value "python:request.set('disable_plone.leftcolumn',1)" (12:47)> -> __value
                __token = 495
                try:
                    __zt_tmp = __attrs_4901950304
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', "request.set('disable_plone.leftcolumn',1)", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['disable_column_one'] = __value
                __backup_disable_column_two_4877282480 = get('disable_column_two', __marker)

                # <Value "python:request.set('disable_plone.rightcolumn',1)" (13:46)> -> __value
                __token = 592
                try:
                    __zt_tmp = __attrs_4901950304
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', "request.set('disable_plone.rightcolumn',1)", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['disable_column_two'] = __value
                if (__backup_disable_column_two_4877282480 is __marker):
                    del econtext['disable_column_two']
                else:
                    econtext['disable_column_two'] = __backup_disable_column_two_4877282480
                if (__backup_disable_column_one_4689333888 is __marker):
                    del econtext['disable_column_one']
                else:
                    econtext['disable_column_one'] = __backup_disable_column_one_4689333888
                if (__backup_dummy_4685603136 is __marker):
                    del econtext['dummy']
                else:
                    econtext['dummy'] = __backup_dummy_4685603136
            _slots = econtext['__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_content(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901959040
                __attrs_4901959040 = _static_4438893776
                __append('\n    ')
                __token = None
                render_main(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n\n')
            _slots = econtext['__slot_content'] = _deque((__fill_content, ))

            # <Value 'context/@@main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_4901957024
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4439058528('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4902583296 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4902583296
            __i18n_domain = __previous_i18n_domain_4901954432
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_main': render_main, 'render_user_content_listing': render_user_content_listing, 'render': render, }