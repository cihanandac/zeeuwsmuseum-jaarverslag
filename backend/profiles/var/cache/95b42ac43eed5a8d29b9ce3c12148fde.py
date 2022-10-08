# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/discussion/browser/comments.pt'

__tokens = {46: ('view/can_reply', 1, 46), 104: (' view/is_discussion_allowe', 2, 42), 183: ('d view/anonymous_discussion_allow', 3, 50), 261: ('ed view/edit_comment_allo', 4, 41), 336: ('wed view/delete_own_comment_all', 5, 45), 398: ('Anon view/is_anon', 6, 25), 449: ('eview view/can_', 7, 27), 496: ('eplies python:view.get_replies(can', 8, 24), 566: ('replies python:view.has_replies(ca', 9, 27), 643: ('terImage view/show_commen', 10, 33), 699: ('   errors options/state/getErro', 11, 20), 760: ('     wtool context/@@plone_too', 12, 18), 825: (' auth_token context/@@authenticator/t', 13, 22), 895: ('python:isDiscussionAllowed or has_replies', 14, 19), 1050: ('python:isAnon and not isAnonymousDiscussionAllowed', 18, 27), 1144: ('view/login_action', 19, 41), 1567: ('has_replies', 29, 27), 1628: ('replies', 30, 47), 1714: ('reply_dict/comment', 33, 38), 1773: (' reply/getI', 34, 39), 1820: ('h reply_dict/depth|python', 35, 33), 1881: ("th python: depth > 10 and '10' or de", 36, 32), 1963: ('url python:view.get_commenter_home_url(username=reply.author_usern', 37, 41), 2075: ('link python:author_home_url and not i', 38, 40), 2155: ('t_url python:view.get_commenter_portrait(reply.author_use', 39, 36), 2255: ("_state python:wtool.getInfoFor(reply, 'review_state', ", 40, 35), 2347: ('canEdit python:view.can_edi', 41, 29), 2414: ('anDelete python:view.can_dele', 42, 30), 2484: ("olorclass python:lambda x: 'state-private' if x=='rejected' else ('state-internal' if x=='spam' else '", 43, 30), 2817: ("python:canReview or review_state == 'published'", 46, 35), 2641: ("python:'comment level-{depth} {state}'.format(depth= depth, state=colorclass(review_state))", 44, 42), 2769: (' comment_i', 45, 35), 3091: ('showCommenterImage', 52, 43), 3198: ('has_author_link', 54, 47), 3268: ('author_home_url', 55, 53), 3444: ('portrait_url', 58, 56), 3461: (' reply/author_nam', 58, 73), 3658: ('not: has_author_link', 62, 47), 3732: ('portrait_url', 63, 52), 3749: (' reply/author_nam', 63, 69), 4001: ('has_author_link', 70, 47), 4071: ('author_home_url', 71, 53), 4088: ('${reply/author_name}', 71, 70), 4090: ('reply/author_name', 71, 72), 4163: ('not: has_author_link', 73, 49), 4185: ('${reply/author_name}', 73, 71), 4187: ('reply/author_name', 73, 73), 4263: ('not: reply/author_name', 75, 49), 4505: ('python:view.format_time(reply.modification_date)', 81, 45), 4842: ('reply/getText', 93, 53), 5107: ('python:isEditCommentAllowed and canEdit', 99, 47), 5364: ('auth_token', 103, 51), 5433: ('string:${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}', 104, 57), 5842: ('not: auth_token', 111, 51), 5918: ('string:${reply/absolute_url}/@@edit-comment', 112, 59), 6013: (' string:edit-${comment_id', 113, 50), 6659: ('python:canDelete', 127, 47), 7011: ('python:not canDelete and isDeleteOwnCommentAllowed and view.could_delete_own(reply)', 134, 51), 7155: ('string:${reply/absolute_url}/@@delete-own-comment', 135, 59), 7259: (" python:view.can_delete_own(reply) and 'display: inline' or 'display: none", 136, 53), 7385: ('d string:delete-${comment_i', 137, 49), 8210: ('python:canDelete', 151, 51), 8287: ('string:${reply/absolute_url}/@@moderate-delete-comment', 152, 59), 8393: (' string:delete-${comment_id', 153, 50), 9070: ('reply_dict/actions|nothing', 165, 47), 9371: ('canReview', 171, 51), 9437: ('reply_dict/actions|nothing', 172, 55), 9625: (' action/i', 174, 52), 9524: ('string:${reply/absolute_url}/@@transmit-comment', 173, 59), 9284: ('comment-action action-${action/id}', 170, 43), 9308: ('action/id', 170, 67), 9686: ('d string:${action/id}-${comment_i', 175, 49), 9956: ('action/id', 179, 62), 10240: ('${action/title}', 183, 58), 10242: ('action/title', 183, 60), 10607: ('python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', 194, 39), 10905: ('python: has_replies and not isDiscussionAllowed', 203, 32), 11179: ('python:has_replies and (isAnon and not isAnonymousDiscussionAllowed)', 212, 27), 11291: ('view/login_action', 213, 41), 11795: ('python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', 225, 27), 12034: ('view/comment_transform_message', 231, 32), 12241: ('view/form/render', 236, 44)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4708793696 = {'id': 'commenting', 'class': 'reply border p-3', }
_static_4708785776 = {'class': 'standalone loginbutton btn btn-primary', 'type': 'submit', 'value': 'Log in to add comments', }
_static_4708718224 = {'class': 'mb-3', 'action': 'view/login_action', }
_static_4708714432 = {'class': 'reply', }
_static_4705567696 = {'class': 'discreet', }
_static_4708727296 = {'class': 'context reply-to-comment-button hide allowMultiSubmit btn btn-primary btn-sm', }
_static_4708714672 = {'name': 'form.button.TransmitComment', 'class': 'context btn btn-primary btn-sm', 'type': 'submit', }
_static_4708722064 = {'type': 'hidden', 'name': 'workflow_action', 'value': 'action/id', }
_static_4708719616 = {'name': '', 'action': '', 'method': 'get', 'class': 'comment-action action-${action/id}', 'id': 'string:${action/id}-${comment_id}', }
_static_4708722400 = {'class': 'comment-actions actions-workflow d-flex flex-row', }
_static_4708630976 = {'name': 'form.button.DeleteComment', 'class': 'destructive btn btn-danger btn-sm', 'type': 'submit', 'value': 'Delete', }
_static_4708636016 = {'name': 'delete', 'action': '', 'method': 'post', 'class': 'comment-action action-delete', 'id': 'string:delete-${comment_id}', }
_static_4708643648 = {'name': 'form.button.DeleteComment', 'class': 'destructive btn btn-danger btn-sm', 'type': 'submit', 'value': 'Delete', }
_static_4708639568 = {'name': 'delete', 'action': '', 'method': 'post', 'class': 'comment-action action-delete', 'style': "python:view.can_delete_own(reply) and 'display: inline' or 'display: none'", 'id': 'string:delete-${comment_id}', }
_static_4708641632 = {'class': 'comment-actions actions-delete', }
_static_4708449536 = {'name': 'form.button.EditComment', 'class': 'context btn btn-primary btn-sm', 'type': 'submit', 'value': 'Edit', }
_static_4708435808 = {'name': 'edit', 'action': '', 'method': 'get', 'class': 'comment-action action-edit', 'id': 'string:edit-${comment_id}', }
_static_4708436336 = {'class': 'pat-plone-modal context comment-action action-edit btn btn-primary btn-sm', 'href': 'string:${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}', }
_static_4708446416 = {'class': 'comment-actions actions-edit', }
_static_4708439024 = {'class': 'd-flex flex-row justify-content-end mb-3', }
_static_4708434704 = {'class': 'comment-body', }
_static_4708436912 = {'class': 'text-muted', }
_static_4709018464 = {'href': '', }
_static_4710159632 = {'class': 'comment-author', }
_static_4709085776 = {'src': 'defaultUser.png', 'alt': '', }
_static_4708199840 = {'src': 'defaultUser.png', 'alt': '', }
_static_4707059504 = {'href': '', }
_static_4705917184 = {'class': 'comment-image me-3', }
_static_4705582720 = {'class': 'd-flex flex-row align-items-center mb-3', }
_static_4705576576 = {'class': 'comment', 'id': 'comment_id', }
_static_4705501824 = {'class': 'discussion', }
_static_4705514640 = {'class': 'btn btn-primary mb-3', 'type': 'submit', 'value': 'Log in to add comments', }
_static_4705512576 = {'action': 'view/login_action', }
_static_4705505376 = {'class': 'reply', }
_static_4560288928 = {'class': 'pat-discussion', }
_static_4459175296 = __C2ZContextWrapper
_static_4459168576 = __compile_zt_expr
_static_4459104240 = {}

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

            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4705223296
            __attrs_4705223296 = _static_4459104240
            __backup_userHasReplyPermission_4705235488 = get('userHasReplyPermission', __marker)

            # <Value 'view/can_reply' (1:46)> -> __value
            __token = 46
            try:
                __zt_tmp = __attrs_4705223296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'view/can_reply', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['userHasReplyPermission'] = __value
            __backup_isDiscussionAllowed_4705235248 = get('isDiscussionAllowed', __marker)

            # <Value 'view/is_discussion_allowed' (2:42)> -> __value
            __token = 104
            try:
                __zt_tmp = __attrs_4705223296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'view/is_discussion_allowed', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['isDiscussionAllowed'] = __value
            __backup_isAnonymousDiscussionAllowed_4705231504 = get('isAnonymousDiscussionAllowed', __marker)

            # <Value 'view/anonymous_discussion_allowed' (3:50)> -> __value
            __token = 183
            try:
                __zt_tmp = __attrs_4705223296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'view/anonymous_discussion_allowed', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['isAnonymousDiscussionAllowed'] = __value
            __backup_isEditCommentAllowed_4705223008 = get('isEditCommentAllowed', __marker)

            # <Value 'view/edit_comment_allowed' (4:41)> -> __value
            __token = 261
            try:
                __zt_tmp = __attrs_4705223296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'view/edit_comment_allowed', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['isEditCommentAllowed'] = __value
            __backup_isDeleteOwnCommentAllowed_4705232608 = get('isDeleteOwnCommentAllowed', __marker)

            # <Value 'view/delete_own_comment_allowed' (5:45)> -> __value
            __token = 336
            try:
                __zt_tmp = __attrs_4705223296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'view/delete_own_comment_allowed', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['isDeleteOwnCommentAllowed'] = __value
            __backup_isAnon_4705232656 = get('isAnon', __marker)

            # <Value 'view/is_anonymous' (6:25)> -> __value
            __token = 398
            try:
                __zt_tmp = __attrs_4705223296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'view/is_anonymous', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['isAnon'] = __value
            __backup_canReview_4705231744 = get('canReview', __marker)

            # <Value 'view/can_review' (7:27)> -> __value
            __token = 449
            try:
                __zt_tmp = __attrs_4705223296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'view/can_review', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['canReview'] = __value
            __backup_replies_4705225312 = get('replies', __marker)

            # <Value 'python:view.get_replies(canReview)' (8:24)> -> __value
            __token = 496
            try:
                __zt_tmp = __attrs_4705223296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('python', 'view.get_replies(canReview)', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['replies'] = __value
            __backup_has_replies_4705223536 = get('has_replies', __marker)

            # <Value 'python:view.has_replies(canReview)' (9:27)> -> __value
            __token = 566
            try:
                __zt_tmp = __attrs_4705223296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('python', 'view.has_replies(canReview)', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['has_replies'] = __value
            __backup_showCommenterImage_4705232800 = get('showCommenterImage', __marker)

            # <Value 'view/show_commenter_image' (10:33)> -> __value
            __token = 643
            try:
                __zt_tmp = __attrs_4705223296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'view/show_commenter_image', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['showCommenterImage'] = __value
            __backup_errors_4705223584 = get('errors', __marker)

            # <Value 'options/state/getErrors|nothing' (11:20)> -> __value
            __token = 699
            try:
                __zt_tmp = __attrs_4705223296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'options/state/getErrors|nothing', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['errors'] = __value
            __backup_wtool_4705237696 = get('wtool', __marker)

            # <Value 'context/@@plone_tools/workflow' (12:18)> -> __value
            __token = 760
            try:
                __zt_tmp = __attrs_4705223296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'context/@@plone_tools/workflow', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['wtool'] = __value
            __backup_auth_token_4705231792 = get('auth_token', __marker)

            # <Value 'context/@@authenticator/token|nothing' (13:22)> -> __value
            __token = 825
            try:
                __zt_tmp = __attrs_4705223296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4459168576('path', 'context/@@authenticator/token|nothing', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            econtext['auth_token'] = __value

            # <Value 'python:isDiscussionAllowed or has_replies' (14:19)> -> __condition
            __token = 895
            try:
                __zt_tmp = __attrs_4705223296
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4459168576('python', 'isDiscussionAllowed or has_replies', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4705461408 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x10fd07ca0> name=None at 10fd07760> -> __attrs_4700483264
                __attrs_4700483264 = _static_4560288928

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="pat-discussion">\n        ')

                # <Static value=<ast.Dict object at 0x118785060> name=None at 118785090> -> __attrs_4705506240
                __attrs_4705506240 = _static_4705505376

                # <Value 'python:isAnon and not isAnonymousDiscussionAllowed' (18:27)> -> __condition
                __token = 1050
                try:
                    __zt_tmp = __attrs_4705506240
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4459168576('python', 'isAnon and not isAnonymousDiscussionAllowed', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="reply">\n            ')

                    # <Static value=<ast.Dict object at 0x118786c80> name=None at 118786f80> -> __attrs_4705503600
                    __attrs_4705503600 = _static_4705512576

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form')

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4705513296
                    __default_4705513296 = _DEFAULT_MARKER

                    # <Substitution 'view/login_action' (19:41)> -> __attr_action
                    __token = 1144
                    try:
                        __zt_tmp = __attrs_4705503600
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_4459168576('path', 'view/login_action', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((' action="%s"' % __attr_action))
                    __append('>\n                ')

                    # <Static value=<ast.Dict object at 0x118787490> name=None at 1187862f0> -> __attrs_4705507200
                    __attrs_4705507200 = _static_4705514640

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="btn btn-primary mb-3" type="submit"')

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4705516368
                    __default_4705516368 = _DEFAULT_MARKER

                    # <Translate msgid='label_login_to_add_comments' node=<ast.Constant object at 0x118787e50> at 1187870a0> -> __attr_value
                    __attr_value = 'Log in to add comments'
                    __attr_value = translate('label_login_to_add_comments', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append('>')
                    __stream_4705508112 = []
                    __append_4705508112 = __stream_4705508112.append
                    __append_4705508112('Log in to add comments')
                    __msgid_4705508112 = __re_whitespace(''.join(__stream_4705508112)).strip()
                    if 'label_login_to_add_comments':
                        __append(translate('label_login_to_add_comments', mapping=None, default=__msgid_4705508112, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n            </form>\n        </div>')
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x118784280> name=None at 118784700> -> __attrs_4700762128
                __attrs_4700762128 = _static_4705501824

                # <Value 'has_replies' (29:27)> -> __condition
                __token = 1567
                try:
                    __zt_tmp = __attrs_4700762128
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4459168576('path', 'has_replies', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="discussion">\n            ')

                    # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4699930384
                    __attrs_4699930384 = _static_4459104240
                    __backup_reply_dict_4705508928 = get('reply_dict', __marker)

                    # <Value 'replies' (30:47)> -> __iterator
                    __token = 1628
                    try:
                        __zt_tmp = __attrs_4699930384
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_4459168576('path', 'replies', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                    (__iterator, ____index_4699928032, ) = getname('repeat')('reply_dict', __iterator)
                    econtext['reply_dict'] = None
                    for __item in __iterator:
                        econtext['reply_dict'] = __item
                        __append('\n\n                ')

                        # <Static value=<ast.Dict object at 0x118796680> name=None at 118794100> -> __attrs_4705574080
                        __attrs_4705574080 = _static_4705576576
                        __backup_reply_4705508448 = get('reply', __marker)

                        # <Value 'reply_dict/comment' (33:38)> -> __value
                        __token = 1714
                        try:
                            __zt_tmp = __attrs_4705574080
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4459168576('path', 'reply_dict/comment', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                        econtext['reply'] = __value
                        __backup_comment_id_4705512528 = get('comment_id', __marker)

                        # <Value 'reply/getId' (34:39)> -> __value
                        __token = 1773
                        try:
                            __zt_tmp = __attrs_4705574080
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4459168576('path', 'reply/getId', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                        econtext['comment_id'] = __value
                        __backup_depth_4705511856 = get('depth', __marker)

                        # <Value 'reply_dict/depth|python:0' (35:33)> -> __value
                        __token = 1820
                        try:
                            __zt_tmp = __attrs_4705574080
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4459168576('path', 'reply_dict/depth|python:0', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                        econtext['depth'] = __value
                        __backup_depth_4705574656 = get('depth', __marker)

                        # <Value "python: depth > 10 and '10' or depth" (36:32)> -> __value
                        __token = 1881
                        try:
                            __zt_tmp = __attrs_4705574080
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4459168576('python', " depth > 10 and '10' or depth", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                        econtext['depth'] = __value
                        __backup_author_home_url_4705575808 = get('author_home_url', __marker)

                        # <Value 'python:view.get_commenter_home_url(username=reply.author_username)' (37:41)> -> __value
                        __token = 1963
                        try:
                            __zt_tmp = __attrs_4705574080
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4459168576('python', 'view.get_commenter_home_url(username=reply.author_username)', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                        econtext['author_home_url'] = __value
                        __backup_has_author_link_4705576192 = get('has_author_link', __marker)

                        # <Value 'python:author_home_url and not isAnon' (38:40)> -> __value
                        __token = 2075
                        try:
                            __zt_tmp = __attrs_4705574080
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4459168576('python', 'author_home_url and not isAnon', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                        econtext['has_author_link'] = __value
                        __backup_portrait_url_4705575376 = get('portrait_url', __marker)

                        # <Value 'python:view.get_commenter_portrait(reply.author_username)' (39:36)> -> __value
                        __token = 2155
                        try:
                            __zt_tmp = __attrs_4705574080
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4459168576('python', 'view.get_commenter_portrait(reply.author_username)', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                        econtext['portrait_url'] = __value
                        __backup_review_state_4705573456 = get('review_state', __marker)

                        # <Value "python:wtool.getInfoFor(reply, 'review_state', 'none')" (40:35)> -> __value
                        __token = 2255
                        try:
                            __zt_tmp = __attrs_4705574080
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4459168576('python', "wtool.getInfoFor(reply, 'review_state', 'none')", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                        econtext['review_state'] = __value
                        __backup_canEdit_4705572784 = get('canEdit', __marker)

                        # <Value 'python:view.can_edit(reply)' (41:29)> -> __value
                        __token = 2347
                        try:
                            __zt_tmp = __attrs_4705574080
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4459168576('python', 'view.can_edit(reply)', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                        econtext['canEdit'] = __value
                        __backup_canDelete_4705573360 = get('canDelete', __marker)

                        # <Value 'python:view.can_delete(reply)' (42:30)> -> __value
                        __token = 2414
                        try:
                            __zt_tmp = __attrs_4705574080
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4459168576('python', 'view.can_delete(reply)', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                        econtext['canDelete'] = __value
                        __backup_colorclass_4705572976 = get('colorclass', __marker)

                        # <Value "python:lambda x: 'state-private' if x=='rejected' else ('state-internal' if x=='spam' else 'state-'+x)" (43:30)> -> __value
                        __token = 2484
                        try:
                            __zt_tmp = __attrs_4705574080
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4459168576('python', "lambda x: 'state-private' if x=='rejected' else ('state-internal' if x=='spam' else 'state-'+x)", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                        econtext['colorclass'] = __value

                        # <Value "python:canReview or review_state == 'published'" (46:35)> -> __condition
                        __token = 2817
                        try:
                            __zt_tmp = __attrs_4705574080
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4459168576('python', "canReview or review_state == 'published'", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div')

                            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4705578832
                            __default_4705578832 = _DEFAULT_MARKER

                            # <Substitution "python:'comment level-{depth} {state}'.format(depth= depth, state=colorclass(review_state))" (44:42)> -> __attr_class
                            __token = 2641
                            try:
                                __zt_tmp = __attrs_4705574080
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_4459168576('python', "'comment level-{depth} {state}'.format(depth= depth, state=colorclass(review_state))", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', 'comment', _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((' class="%s"' % __attr_class))

                            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4705567600
                            __default_4705567600 = _DEFAULT_MARKER

                            # <Substitution 'comment_id' (45:35)> -> __attr_id
                            __token = 2769
                            try:
                                __zt_tmp = __attrs_4705574080
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_id = _static_4459168576('path', 'comment_id', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_id is not None):
                                __append((' id="%s"' % __attr_id))
                            __append('>\n\n                    ')

                            # <Static value=<ast.Dict object at 0x118797e80> name=None at 118797e50> -> __attrs_4705572544
                            __attrs_4705572544 = _static_4705582720

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="d-flex flex-row align-items-center mb-3">\n\n                        <!-- commenter image -->\n                        ')

                            # <Static value=<ast.Dict object at 0x1187e9900> name=None at 1187e9870> -> __attrs_4705913056
                            __attrs_4705913056 = _static_4705917184

                            # <Value 'showCommenterImage' (52:43)> -> __condition
                            __token = 3091
                            try:
                                __zt_tmp = __attrs_4705913056
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4459168576('path', 'showCommenterImage', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="comment-image me-3">\n                            ')

                                # <Static value=<ast.Dict object at 0x118900730> name=None at 1189002e0> -> __attrs_4707074112
                                __attrs_4707074112 = _static_4707059504

                                # <Value 'has_author_link' (54:47)> -> __condition
                                __token = 3198
                                try:
                                    __zt_tmp = __attrs_4707074112
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_4459168576('path', 'has_author_link', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                if __condition:

                                    # <a ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<a')

                                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4707075696
                                    __default_4707075696 = _DEFAULT_MARKER

                                    # <Substitution 'author_home_url' (55:53)> -> __attr_href
                                    __token = 3268
                                    try:
                                        __zt_tmp = __attrs_4707074112
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_href = _static_4459168576('path', 'author_home_url', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_href is not None):
                                        __append((' href="%s"' % __attr_href))
                                    __append('>\n                                ')

                                    # <Static value=<ast.Dict object at 0x118a16da0> name=None at 118934bb0> -> __attrs_4709084624
                                    __attrs_4709084624 = _static_4708199840

                                    # <img ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<img')

                                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708202240
                                    __default_4708202240 = _DEFAULT_MARKER

                                    # <Substitution 'portrait_url' (58:56)> -> __attr_src
                                    __token = 3444
                                    try:
                                        __zt_tmp = __attrs_4709084624
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_src = _static_4459168576('path', 'portrait_url', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                    __attr_src = __quote(__attr_src, '"', '&quot;', 'defaultUser.png', _DEFAULT_MARKER)
                                    if (__attr_src is not None):
                                        __append((' src="%s"' % __attr_src))

                                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708200944
                                    __default_4708200944 = _DEFAULT_MARKER

                                    # <Substitution 'reply/author_name' (58:73)> -> __attr_alt
                                    __token = 3461
                                    try:
                                        __zt_tmp = __attrs_4709084624
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_alt = _static_4459168576('path', 'reply/author_name', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                    __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_alt is not None):
                                        __append((' alt="%s"' % __attr_alt))
                                    __append(' />\n                            </a>')
                                __append('\n                            ')

                                # <Static value=<ast.Dict object at 0x118aef250> name=None at 118aee110> -> __attrs_4710158288
                                __attrs_4710158288 = _static_4709085776

                                # <Value 'not: has_author_link' (62:47)> -> __condition
                                __token = 3658
                                try:
                                    __zt_tmp = __attrs_4710158288
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_4459168576('not', ' has_author_link', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                if __condition:

                                    # <img ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<img')

                                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709088848
                                    __default_4709088848 = _DEFAULT_MARKER

                                    # <Substitution 'portrait_url' (63:52)> -> __attr_src
                                    __token = 3732
                                    try:
                                        __zt_tmp = __attrs_4710158288
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_src = _static_4459168576('path', 'portrait_url', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                    __attr_src = __quote(__attr_src, '"', '&quot;', 'defaultUser.png', _DEFAULT_MARKER)
                                    if (__attr_src is not None):
                                        __append((' src="%s"' % __attr_src))

                                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709086592
                                    __default_4709086592 = _DEFAULT_MARKER

                                    # <Substitution 'reply/author_name' (63:69)> -> __attr_alt
                                    __token = 3749
                                    try:
                                        __zt_tmp = __attrs_4710158288
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_alt = _static_4459168576('path', 'reply/author_name', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                    __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_alt is not None):
                                        __append((' alt="%s"' % __attr_alt))
                                    __append(' />')
                                __append('\n                        </div>')
                            __append('\n\n                        <!-- commenter name and date -->\n                        ')

                            # <Static value=<ast.Dict object at 0x118bf5510> name=None at 118bf59c0> -> __attrs_4709048832
                            __attrs_4709048832 = _static_4710159632

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="comment-author">\n\n                            ')

                            # <Static value=<ast.Dict object at 0x118adeb60> name=None at 118adf5b0> -> __attrs_4709017312
                            __attrs_4709017312 = _static_4709018464

                            # <Value 'has_author_link' (70:47)> -> __condition
                            __token = 4001
                            try:
                                __zt_tmp = __attrs_4709017312
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4459168576('path', 'has_author_link', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                            if __condition:

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append('<a')

                                # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4709009584
                                __default_4709009584 = _DEFAULT_MARKER

                                # <Substitution 'author_home_url' (71:53)> -> __attr_href
                                __token = 4071
                                try:
                                    __zt_tmp = __attrs_4709017312
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_4459168576('path', 'author_home_url', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                                if (__attr_href is not None):
                                    __append((' href="%s"' % __attr_href))
                                __append('>')

                                # <Interpolation value=<Substitution '${reply/author_name}' (71:70)> braces_required=True translation=False default='"?"' default_marker='"?"' at 118adf7c0> -> __content_4356865648
                                __token = 4088
                                __token = 4090
                                try:
                                    __zt_tmp = __attrs_4709017312
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __content_4356865648 = _static_4459168576('path', 'reply/author_name', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                __content_4356865648 = __quote(__content_4356865648, '\x00', '&#0;', None, None)
                                __content_4356865648 = __content_4356865648
                                if (__content_4356865648 is None):
                                    pass
                                else:
                                    if (__content_4356865648 is None):
                                        __content_4356865648 = None
                                    else:
                                        __tt = type(__content_4356865648)
                                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                                            __content_4356865648 = str(__content_4356865648)
                                        else:
                                            if (__tt is bytes):
                                                __content_4356865648 = decode(__content_4356865648)
                                            else:
                                                if (__tt is not str):
                                                    try:
                                                        __content_4356865648 = __content_4356865648.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__content_4356865648)
                                                        __content_4356865648 = (str(__content_4356865648) if (__content_4356865648 is __converted) else __converted)
                                                    else:
                                                        __content_4356865648 = __content_4356865648()
                                if (__content_4356865648 is not None):
                                    __append(__content_4356865648)
                                __append('</a>')
                            __append('\n\n                            ')

                            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4709018224
                            __attrs_4709018224 = _static_4459104240

                            # <Value 'not: has_author_link' (73:49)> -> __condition
                            __token = 4163
                            try:
                                __zt_tmp = __attrs_4709018224
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4459168576('not', ' has_author_link', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span>')

                                # <Interpolation value=<Substitution '${reply/author_name}' (73:71)> braces_required=True translation=False default='"?"' default_marker='"?"' at 118965930> -> __content_4356865648
                                __token = 4185
                                __token = 4187
                                try:
                                    __zt_tmp = __attrs_4709018224
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __content_4356865648 = _static_4459168576('path', 'reply/author_name', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                __content_4356865648 = __quote(__content_4356865648, '\x00', '&#0;', None, None)
                                __content_4356865648 = __content_4356865648
                                if (__content_4356865648 is None):
                                    pass
                                else:
                                    if (__content_4356865648 is None):
                                        __content_4356865648 = None
                                    else:
                                        __tt = type(__content_4356865648)
                                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                                            __content_4356865648 = str(__content_4356865648)
                                        else:
                                            if (__tt is bytes):
                                                __content_4356865648 = decode(__content_4356865648)
                                            else:
                                                if (__tt is not str):
                                                    try:
                                                        __content_4356865648 = __content_4356865648.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__content_4356865648)
                                                        __content_4356865648 = (str(__content_4356865648) if (__content_4356865648 is __converted) else __converted)
                                                    else:
                                                        __content_4356865648 = __content_4356865648()
                                if (__content_4356865648 is not None):
                                    __append(__content_4356865648)
                                __append('</span>')
                            __append('\n\n                            ')

                            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708202816
                            __attrs_4708202816 = _static_4459104240

                            # <Value 'not: reply/author_name' (75:49)> -> __condition
                            __token = 4263
                            try:
                                __zt_tmp = __attrs_4708202816
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4459168576('not', ' reply/author_name', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span>')
                                __stream_4708198736 = []
                                __append_4708198736 = __stream_4708198736.append
                                __append_4708198736('Anonymous')
                                __msgid_4708198736 = __re_whitespace(''.join(__stream_4708198736)).strip()
                                if 'label_anonymous':
                                    __append(translate('label_anonymous', mapping=None, default=__msgid_4708198736, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                __append('</span>')
                            __append('\n\n                            ')

                            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708442240
                            __attrs_4708442240 = _static_4459104240

                            # <br ... (0:0)
                            # --------------------------------------------------------
                            __append('<br />\n\n                            ')

                            # <Static value=<ast.Dict object at 0x118a50bb0> name=None at 118a53220> -> __attrs_4708448240
                            __attrs_4708448240 = _static_4708436912

                            # <small ... (0:0)
                            # --------------------------------------------------------
                            __append('<small class="text-muted">')

                            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708440704
                            __default_4708440704 = _DEFAULT_MARKER

                            # <Value 'python:view.format_time(reply.modification_date)' (81:45)> -> __cache_4708442336
                            __token = 4505
                            try:
                                __zt_tmp = __attrs_4708448240
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4708442336 = _static_4459168576('python', 'view.format_time(reply.modification_date)', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

                            # <BinOp left=<Value 'python:view.format_time(reply.modification_date)' (81:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118a51cf0> -> __condition
                            __expression = __cache_4708442336

                            # <Symbol value=<DEFAULT> at 109c89f90> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append('\n                      8/23/2001 12:40:44 PM\n                            ')
                            else:
                                __content = __cache_4708442336
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('</small>\n\n                        </div>\n                    </div>\n\n\n\n                    <!-- comment body -->\n                    ')

                            # <Static value=<ast.Dict object at 0x118a50310> name=None at 118a52890> -> __attrs_4708441520
                            __attrs_4708441520 = _static_4708434704

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="comment-body">\n\n                        ')

                            # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708448624
                            __attrs_4708448624 = _static_4459104240

                            # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708440224
                            __default_4708440224 = _DEFAULT_MARKER

                            # <Value 'reply/getText' (93:53)> -> __cache_4708434896
                            __token = 4842
                            try:
                                __zt_tmp = __attrs_4708448624
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4708434896 = _static_4459168576('path', 'reply/getText', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

                            # <BinOp left=<Value 'reply/getText' (93:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118a52d70> -> __condition
                            __expression = __cache_4708434896

                            # <Symbol value=<DEFAULT> at 109c89f90> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span />')
                            else:
                                __content = __cache_4708434896
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append('\n\n                        <!-- comment actions -->\n                        ')

                            # <Static value=<ast.Dict object at 0x118a513f0> name=None at 118a52e60> -> __attrs_4708445984
                            __attrs_4708445984 = _static_4708439024

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="d-flex flex-row justify-content-end mb-3">\n\n                            ')

                            # <Static value=<ast.Dict object at 0x118a530d0> name=None at 118a512d0> -> __attrs_4708444592
                            __attrs_4708444592 = _static_4708446416

                            # <Value 'python:isEditCommentAllowed and canEdit' (99:47)> -> __condition
                            __token = 5107
                            try:
                                __zt_tmp = __attrs_4708444592
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4459168576('python', 'isEditCommentAllowed and canEdit', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="comment-actions actions-edit">\n\n                                <!-- edit -->\n                                ')

                                # <Static value=<ast.Dict object at 0x118a50970> name=None at 118a513c0> -> __attrs_4708447472
                                __attrs_4708447472 = _static_4708436336

                                # <Value 'auth_token' (103:51)> -> __condition
                                __token = 5364
                                try:
                                    __zt_tmp = __attrs_4708447472
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_4459168576('path', 'auth_token', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                if __condition:

                                    # <a ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<a class="pat-plone-modal context comment-action action-edit btn btn-primary btn-sm"')

                                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708442960
                                    __default_4708442960 = _DEFAULT_MARKER

                                    # <Substitution 'string:${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}' (104:57)> -> __attr_href
                                    __token = 5433
                                    try:
                                        __zt_tmp = __attrs_4708447472
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_href = _static_4459168576('string', '${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_href is not None):
                                        __append((' href="%s"' % __attr_href))
                                    __append('>')
                                    __stream_4708434416 = []
                                    __append_4708434416 = __stream_4708434416.append
                                    __append_4708434416('Edit')
                                    __msgid_4708434416 = __re_whitespace(''.join(__stream_4708434416)).strip()
                                    if 'Edit':
                                        __append(translate('Edit', mapping=None, default=__msgid_4708434416, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                    __append('</a>')
                                __append('\n\n                                ')

                                # <Static value=<ast.Dict object at 0x118a50760> name=None at 118a522f0> -> __attrs_4708448048
                                __attrs_4708448048 = _static_4708435808

                                # <Value 'not: auth_token' (111:51)> -> __condition
                                __token = 5842
                                try:
                                    __zt_tmp = __attrs_4708448048
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_4459168576('not', ' auth_token', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                if __condition:

                                    # <form ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<form name="edit"')

                                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708449248
                                    __default_4708449248 = _DEFAULT_MARKER

                                    # <Substitution 'string:${reply/absolute_url}/@@edit-comment' (112:59)> -> __attr_action
                                    __token = 5918
                                    try:
                                        __zt_tmp = __attrs_4708448048
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_action = _static_4459168576('string', '${reply/absolute_url}/@@edit-comment', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                    __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_action is not None):
                                        __append((' action="%s"' % __attr_action))
                                    __append(' method="get" class="comment-action action-edit"')

                                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708450112
                                    __default_4708450112 = _DEFAULT_MARKER

                                    # <Substitution 'string:edit-${comment_id}' (113:50)> -> __attr_id
                                    __token = 6013
                                    try:
                                        __zt_tmp = __attrs_4708448048
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_4459168576('string', 'edit-${comment_id}', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((' id="%s"' % __attr_id))
                                    __append('>\n\n                                    ')

                                    # <Static value=<ast.Dict object at 0x118a53d00> name=None at 118a523b0> -> __attrs_4708633280
                                    __attrs_4708633280 = _static_4708449536

                                    # <button ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<button name="form.button.EditComment" class="context btn btn-primary btn-sm" type="submit"')

                                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708637360
                                    __default_4708637360 = _DEFAULT_MARKER

                                    # <Translate msgid='label_edit' node=<ast.Constant object at 0x118a80b50> at 118a809a0> -> __attr_value
                                    __attr_value = 'Edit'
                                    __attr_value = translate('label_edit', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                    if (__attr_value is not None):
                                        __append((' value="%s"' % __attr_value))
                                    __append('>')
                                    __stream_4708434032 = []
                                    __append_4708434032 = __stream_4708434032.append
                                    __append_4708434032('Edit')
                                    __msgid_4708434032 = __re_whitespace(''.join(__stream_4708434032)).strip()
                                    if 'label_edit':
                                        __append(translate('label_edit', mapping=None, default=__msgid_4708434032, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                    __append('</button>\n\n                                </form>')
                                __append('\n\n                            </div>')
                            __append('\n\n                            ')

                            # <Static value=<ast.Dict object at 0x118a82b60> name=None at 118a82800> -> __attrs_4708642256
                            __attrs_4708642256 = _static_4708641632

                            # <Value 'python:canDelete' (127:47)> -> __condition
                            __token = 6659
                            try:
                                __zt_tmp = __attrs_4708642256
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4459168576('python', 'canDelete', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="comment-actions actions-delete">\n\n                                <!-- delete own comment -->\n                                ')

                                # <Static value=<ast.Dict object at 0x118a82350> name=None at 118a83f40> -> __attrs_4708643120
                                __attrs_4708643120 = _static_4708639568

                                # <Value 'python:not canDelete and isDeleteOwnCommentAllowed and view.could_delete_own(reply)' (134:51)> -> __condition
                                __token = 7011
                                try:
                                    __zt_tmp = __attrs_4708643120
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_4459168576('python', 'not canDelete and isDeleteOwnCommentAllowed and view.could_delete_own(reply)', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                if __condition:

                                    # <form ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<form name="delete"')

                                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708633904
                                    __default_4708633904 = _DEFAULT_MARKER

                                    # <Substitution 'string:${reply/absolute_url}/@@delete-own-comment' (135:59)> -> __attr_action
                                    __token = 7155
                                    try:
                                        __zt_tmp = __attrs_4708643120
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_action = _static_4459168576('string', '${reply/absolute_url}/@@delete-own-comment', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                    __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_action is not None):
                                        __append((' action="%s"' % __attr_action))
                                    __append(' method="post" class="comment-action action-delete"')

                                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708645040
                                    __default_4708645040 = _DEFAULT_MARKER

                                    # <Substitution "python:view.can_delete_own(reply) and 'display: inline' or 'display: none'" (136:53)> -> __attr_style
                                    __token = 7259
                                    try:
                                        __zt_tmp = __attrs_4708643120
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_style = _static_4459168576('python', "view.can_delete_own(reply) and 'display: inline' or 'display: none'", econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                    __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_style is not None):
                                        __append((' style="%s"' % __attr_style))

                                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708643936
                                    __default_4708643936 = _DEFAULT_MARKER

                                    # <Substitution 'string:delete-${comment_id}' (137:49)> -> __attr_id
                                    __token = 7385
                                    try:
                                        __zt_tmp = __attrs_4708643120
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_4459168576('string', 'delete-${comment_id}', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((' id="%s"' % __attr_id))
                                    __append('>\n                                    ')

                                    # <Static value=<ast.Dict object at 0x118a83340> name=None at 118a83580> -> __attrs_4708643216
                                    __attrs_4708643216 = _static_4708643648

                                    # <button ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<button name="form.button.DeleteComment" class="destructive btn btn-danger btn-sm" type="submit"')

                                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708643408
                                    __default_4708643408 = _DEFAULT_MARKER

                                    # <Translate msgid='label_delete' node=<ast.Constant object at 0x118a80460> at 118a835e0> -> __attr_value
                                    __attr_value = 'Delete'
                                    __attr_value = translate('label_delete', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                    if (__attr_value is not None):
                                        __append((' value="%s"' % __attr_value))
                                    __append('>')
                                    __stream_4708639136 = []
                                    __append_4708639136 = __stream_4708639136.append
                                    __append_4708639136('Delete')
                                    __msgid_4708639136 = __re_whitespace(''.join(__stream_4708639136)).strip()
                                    if 'label_delete':
                                        __append(translate('label_delete', mapping=None, default=__msgid_4708639136, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                    __append('</button>\n                                </form>')
                                __append('\n\n                                <!-- delete -->\n                                ')

                                # <Static value=<ast.Dict object at 0x118a81570> name=None at 118a823e0> -> __attrs_4708642208
                                __attrs_4708642208 = _static_4708636016

                                # <Value 'python:canDelete' (151:51)> -> __condition
                                __token = 8210
                                try:
                                    __zt_tmp = __attrs_4708642208
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_4459168576('python', 'canDelete', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                if __condition:

                                    # <form ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<form name="delete"')

                                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708638128
                                    __default_4708638128 = _DEFAULT_MARKER

                                    # <Substitution 'string:${reply/absolute_url}/@@moderate-delete-comment' (152:59)> -> __attr_action
                                    __token = 8287
                                    try:
                                        __zt_tmp = __attrs_4708642208
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_action = _static_4459168576('string', '${reply/absolute_url}/@@moderate-delete-comment', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                    __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_action is not None):
                                        __append((' action="%s"' % __attr_action))
                                    __append(' method="post" class="comment-action action-delete"')

                                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708642928
                                    __default_4708642928 = _DEFAULT_MARKER

                                    # <Substitution 'string:delete-${comment_id}' (153:50)> -> __attr_id
                                    __token = 8393
                                    try:
                                        __zt_tmp = __attrs_4708642208
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_4459168576('string', 'delete-${comment_id}', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((' id="%s"' % __attr_id))
                                    __append('>\n                                    ')

                                    # <Static value=<ast.Dict object at 0x118a801c0> name=None at 118a82c20> -> __attrs_4708722832
                                    __attrs_4708722832 = _static_4708630976

                                    # <button ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<button name="form.button.DeleteComment" class="destructive btn btn-danger btn-sm" type="submit"')

                                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708634528
                                    __default_4708634528 = _DEFAULT_MARKER

                                    # <Translate msgid='label_delete' node=<ast.Constant object at 0x118a81f90> at 118a83cd0> -> __attr_value
                                    __attr_value = 'Delete'
                                    __attr_value = translate('label_delete', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                    if (__attr_value is not None):
                                        __append((' value="%s"' % __attr_value))
                                    __append('>')
                                    __stream_4708642112 = []
                                    __append_4708642112 = __stream_4708642112.append
                                    __append_4708642112('Delete')
                                    __msgid_4708642112 = __re_whitespace(''.join(__stream_4708642112)).strip()
                                    if 'label_delete':
                                        __append(translate('label_delete', mapping=None, default=__msgid_4708642112, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                    __append('</button>\n                                </form>')
                                __append('\n\n                            </div>')
                            __append('\n\n                            ')

                            # <Static value=<ast.Dict object at 0x118a966e0> name=None at 118a96f50> -> __attrs_4708713568
                            __attrs_4708713568 = _static_4708722400

                            # <Value 'reply_dict/actions|nothing' (165:47)> -> __condition
                            __token = 9070
                            try:
                                __zt_tmp = __attrs_4708713568
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4459168576('path', 'reply_dict/actions|nothing', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="comment-actions actions-workflow d-flex flex-row">\n\n                                ')

                                # <Static value=<ast.Dict object at 0x118a95c00> name=None at 118a97af0> -> __attrs_4708712608
                                __attrs_4708712608 = _static_4708719616

                                # <Value 'canReview' (171:51)> -> __condition
                                __token = 9371
                                try:
                                    __zt_tmp = __attrs_4708712608
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_4459168576('path', 'canReview', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                if __condition:
                                    __backup_action_4710163712 = get('action', __marker)

                                    # <Value 'reply_dict/actions|nothing' (172:55)> -> __iterator
                                    __token = 9437
                                    try:
                                        __zt_tmp = __attrs_4708712608
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __iterator = _static_4459168576('path', 'reply_dict/actions|nothing', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                    (__iterator, ____index_4708719184, ) = getname('repeat')('action', __iterator)
                                    econtext['action'] = None
                                    for __item in __iterator:
                                        econtext['action'] = __item

                                        # <form ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<form')

                                        # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708716736
                                        __default_4708716736 = _DEFAULT_MARKER

                                        # <Substitution 'action/id' (174:52)> -> __attr_name
                                        __token = 9625
                                        try:
                                            __zt_tmp = __attrs_4708712608
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_name = _static_4459168576('path', 'action/id', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                        __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
                                        if (__attr_name is not None):
                                            __append((' name="%s"' % __attr_name))

                                        # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708713760
                                        __default_4708713760 = _DEFAULT_MARKER

                                        # <Substitution 'string:${reply/absolute_url}/@@transmit-comment' (173:59)> -> __attr_action
                                        __token = 9524
                                        try:
                                            __zt_tmp = __attrs_4708712608
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_action = _static_4459168576('string', '${reply/absolute_url}/@@transmit-comment', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                        __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                                        if (__attr_action is not None):
                                            __append((' action="%s"' % __attr_action))
                                        __append(' method="get"')

                                        # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708723024
                                        __default_4708723024 = _DEFAULT_MARKER

                                        # <Interpolation value=<Substitution 'comment-action action-${action/id}' (170:43)> braces_required=True translation=False default='"?"' default_marker='"?"' at 118a94580> -> __attr_class
                                        __token = 9284
                                        __token = 9308
                                        try:
                                            __zt_tmp = __attrs_4708712608
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_class = _static_4459168576('path', 'action/id', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                        __attr_class = ('%s%s' % ('comment-action action-', (__attr_class if (__attr_class is not None) else ''), ))
                                        if (__attr_class is None):
                                            pass
                                        else:
                                            if (__attr_class is _DEFAULT_MARKER):
                                                __attr_class = None
                                            else:
                                                __tt = type(__attr_class)
                                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                                    __attr_class = str(__attr_class)
                                                else:
                                                    if (__tt is bytes):
                                                        __attr_class = decode(__attr_class)
                                                    else:
                                                        if (__tt is not str):
                                                            try:
                                                                __attr_class = __attr_class.__html__
                                                            except get('AttributeError', AttributeError):
                                                                __converted = convert(__attr_class)
                                                                __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                                            else:
                                                                __attr_class = __attr_class()
                                        if (__attr_class is not None):
                                            __append((' class="%s"' % __attr_class))

                                        # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708718128
                                        __default_4708718128 = _DEFAULT_MARKER

                                        # <Substitution 'string:${action/id}-${comment_id}' (175:49)> -> __attr_id
                                        __token = 9686
                                        try:
                                            __zt_tmp = __attrs_4708712608
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_id = _static_4459168576('string', '${action/id}-${comment_id}', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                        if (__attr_id is not None):
                                            __append((' id="%s"' % __attr_id))
                                        __append('>\n                                    ')

                                        # <Static value=<ast.Dict object at 0x118a96590> name=None at 118a95bd0> -> __attrs_4708715296
                                        __attrs_4708715296 = _static_4708722064

                                        # <input ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<input type="hidden" name="workflow_action"')

                                        # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708718896
                                        __default_4708718896 = _DEFAULT_MARKER

                                        # <Substitution 'action/id' (179:62)> -> __attr_value
                                        __token = 9956
                                        try:
                                            __zt_tmp = __attrs_4708715296
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_value = _static_4459168576('path', 'action/id', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                                        if (__attr_value is not None):
                                            __append((' value="%s"' % __attr_value))
                                        __append(' />\n                                    ')

                                        # <Static value=<ast.Dict object at 0x118a948b0> name=None at 118a95ed0> -> __attrs_4708726432
                                        __attrs_4708726432 = _static_4708714672

                                        # <button ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<button name="form.button.TransmitComment" class="context btn btn-primary btn-sm" type="submit">')
                                        __stream_4708714912 = []
                                        __append_4708714912 = __stream_4708714912.append

                                        # <Interpolation value=<Substitution '${action/title}' (183:58)> braces_required=True translation=False default='"?"' default_marker='"?"' at 118a965c0> -> __content_4356865648
                                        __token = 10240
                                        __token = 10242
                                        try:
                                            __zt_tmp = __attrs_4708726432
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __content_4356865648 = _static_4459168576('path', 'action/title', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                                        __content_4356865648 = __quote(__content_4356865648, '\x00', '&#0;', None, None)
                                        __content_4356865648 = __content_4356865648
                                        if (__content_4356865648 is None):
                                            pass
                                        else:
                                            if (__content_4356865648 is None):
                                                __content_4356865648 = None
                                            else:
                                                __tt = type(__content_4356865648)
                                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                                    __content_4356865648 = str(__content_4356865648)
                                                else:
                                                    if (__tt is bytes):
                                                        __content_4356865648 = decode(__content_4356865648)
                                                    else:
                                                        if (__tt is not str):
                                                            try:
                                                                __content_4356865648 = __content_4356865648.__html__
                                                            except get('AttributeError', AttributeError):
                                                                __converted = convert(__content_4356865648)
                                                                __content_4356865648 = (str(__content_4356865648) if (__content_4356865648 is __converted) else __converted)
                                                            else:
                                                                __content_4356865648 = __content_4356865648()
                                        if (__content_4356865648 is not None):
                                            __append_4708714912(__content_4356865648)
                                        __msgid_4708714912 = __re_whitespace(''.join(__stream_4708714912)).strip()
                                        if __msgid_4708714912:
                                            __append(translate(__msgid_4708714912, mapping=None, default=__msgid_4708714912, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                        __append('</button>\n                                </form>')
                                        ____index_4708719184 -= 1
                                        if (____index_4708719184 > 0):
                                            __append('\n                                ')
                                    if (__backup_action_4710163712 is __marker):
                                        del econtext['action']
                                    else:
                                        econtext['action'] = __backup_action_4710163712
                                __append('\n\n                            </div>')
                            __append('\n\n                        </div>\n                        <!-- end comment actions -->\n\n\n                    </div>\n                    ')

                            # <Static value=<ast.Dict object at 0x118a97a00> name=None at 118a97a90> -> __attrs_4708724896
                            __attrs_4708724896 = _static_4708727296

                            # <Value 'python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)' (194:39)> -> __condition
                            __token = 10607
                            try:
                                __zt_tmp = __attrs_4708724896
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4459168576('python', 'isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                            if __condition:

                                # <button ... (0:0)
                                # --------------------------------------------------------
                                __append('<button class="context reply-to-comment-button hide allowMultiSubmit btn btn-primary btn-sm">')
                                __stream_4708719424 = []
                                __append_4708719424 = __stream_4708719424.append
                                __append_4708719424('\n                    Reply\n                    ')
                                __msgid_4708719424 = __re_whitespace(''.join(__stream_4708719424)).strip()
                                if 'label_reply':
                                    __append(translate('label_reply', mapping=None, default=__msgid_4708719424, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                __append('</button>')
                            __append('\n\n                </div>')
                        if (__backup_colorclass_4705572976 is __marker):
                            del econtext['colorclass']
                        else:
                            econtext['colorclass'] = __backup_colorclass_4705572976
                        if (__backup_canDelete_4705573360 is __marker):
                            del econtext['canDelete']
                        else:
                            econtext['canDelete'] = __backup_canDelete_4705573360
                        if (__backup_canEdit_4705572784 is __marker):
                            del econtext['canEdit']
                        else:
                            econtext['canEdit'] = __backup_canEdit_4705572784
                        if (__backup_review_state_4705573456 is __marker):
                            del econtext['review_state']
                        else:
                            econtext['review_state'] = __backup_review_state_4705573456
                        if (__backup_portrait_url_4705575376 is __marker):
                            del econtext['portrait_url']
                        else:
                            econtext['portrait_url'] = __backup_portrait_url_4705575376
                        if (__backup_has_author_link_4705576192 is __marker):
                            del econtext['has_author_link']
                        else:
                            econtext['has_author_link'] = __backup_has_author_link_4705576192
                        if (__backup_author_home_url_4705575808 is __marker):
                            del econtext['author_home_url']
                        else:
                            econtext['author_home_url'] = __backup_author_home_url_4705575808
                        if (__backup_depth_4705574656 is __marker):
                            del econtext['depth']
                        else:
                            econtext['depth'] = __backup_depth_4705574656
                        if (__backup_depth_4705511856 is __marker):
                            del econtext['depth']
                        else:
                            econtext['depth'] = __backup_depth_4705511856
                        if (__backup_comment_id_4705512528 is __marker):
                            del econtext['comment_id']
                        else:
                            econtext['comment_id'] = __backup_comment_id_4705512528
                        if (__backup_reply_4705508448 is __marker):
                            del econtext['reply']
                        else:
                            econtext['reply'] = __backup_reply_4705508448
                        __append('\n\n            ')
                        ____index_4699928032 -= 1
                        if (____index_4699928032 > 0):
                            __append('')
                    if (__backup_reply_dict_4705508928 is __marker):
                        del econtext['reply_dict']
                    else:
                        econtext['reply_dict'] = __backup_reply_dict_4705508928
                    __append('\n\n            ')

                    # <Static value=<ast.Dict object at 0x1187943d0> name=None at 118795750> -> __attrs_4708724080
                    __attrs_4708724080 = _static_4705567696

                    # <Value 'python: has_replies and not isDiscussionAllowed' (203:32)> -> __condition
                    __token = 10905
                    try:
                        __zt_tmp = __attrs_4708724080
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4459168576('python', ' has_replies and not isDiscussionAllowed', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="discreet">')
                        __stream_4699929328 = []
                        __append_4699929328 = __stream_4699929328.append
                        __append_4699929328('\n            Commenting has been disabled.\n            ')
                        __msgid_4699929328 = __re_whitespace(''.join(__stream_4699929328)).strip()
                        if 'label_commenting_disabled':
                            __append(translate('label_commenting_disabled', mapping=None, default=__msgid_4699929328, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</div>')
                    __append('\n\n        </div>')
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x118a947c0> name=None at 118a94700> -> __attrs_4708713616
                __attrs_4708713616 = _static_4708714432

                # <Value 'python:has_replies and (isAnon and not isAnonymousDiscussionAllowed)' (212:27)> -> __condition
                __token = 11179
                try:
                    __zt_tmp = __attrs_4708713616
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4459168576('python', 'has_replies and (isAnon and not isAnonymousDiscussionAllowed)', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="reply">\n            ')

                    # <Static value=<ast.Dict object at 0x118a95690> name=None at 118a95120> -> __attrs_4708787024
                    __attrs_4708787024 = _static_4708718224

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form class="mb-3"')

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708790144
                    __default_4708790144 = _DEFAULT_MARKER

                    # <Substitution 'view/login_action' (213:41)> -> __attr_action
                    __token = 11291
                    try:
                        __zt_tmp = __attrs_4708787024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_4459168576('path', 'view/login_action', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((' action="%s"' % __attr_action))
                    __append('>\n                ')

                    # <Static value=<ast.Dict object at 0x118aa5e70> name=None at 118aa64a0> -> __attrs_4708784432
                    __attrs_4708784432 = _static_4708785776

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="standalone loginbutton btn btn-primary" type="submit"')

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708792976
                    __default_4708792976 = _DEFAULT_MARKER

                    # <Translate msgid='label_login_to_add_comments' node=<ast.Constant object at 0x118aa4340> at 118aa7100> -> __attr_value
                    __attr_value = 'Log in to add comments'
                    __attr_value = translate('label_login_to_add_comments', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append('>')
                    __stream_4708788368 = []
                    __append_4708788368 = __stream_4708788368.append
                    __append_4708788368('Log in to add comments')
                    __msgid_4708788368 = __re_whitespace(''.join(__stream_4708788368)).strip()
                    if 'label_login_to_add_comments':
                        __append(translate('label_login_to_add_comments', mapping=None, default=__msgid_4708788368, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n            </form>\n        </div>')
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x118aa7d60> name=None at 118aa58d0> -> __attrs_4708781744
                __attrs_4708781744 = _static_4708793696

                # <Value 'python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)' (225:27)> -> __condition
                __token = 11795
                try:
                    __zt_tmp = __attrs_4708781744
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4459168576('python', 'isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="commenting" class="reply border p-3">\n\n            ')

                    # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708787984
                    __attrs_4708787984 = _static_4459104240

                    # <fieldset ... (0:0)
                    # --------------------------------------------------------
                    __append('<fieldset>\n\n                ')

                    # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708791296
                    __attrs_4708791296 = _static_4459104240

                    # <legend ... (0:0)
                    # --------------------------------------------------------
                    __append('<legend>')
                    __stream_4708790912 = []
                    __append_4708790912 = __stream_4708790912.append
                    __append_4708790912('Add comment')
                    __msgid_4708790912 = __re_whitespace(''.join(__stream_4708790912)).strip()
                    if 'label_add_comment':
                        __append(translate('label_add_comment', mapping=None, default=__msgid_4708790912, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</legend>\n\n                ')

                    # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708782032
                    __attrs_4708782032 = _static_4459104240

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p>')

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708788080
                    __default_4708788080 = _DEFAULT_MARKER

                    # <Value 'view/comment_transform_message' (231:32)> -> __cache_4708779776
                    __token = 12034
                    try:
                        __zt_tmp = __attrs_4708782032
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4708779776 = _static_4459168576('path', 'view/comment_transform_message', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/comment_transform_message' (231:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118aa6fb0> -> __condition
                    __expression = __cache_4708779776

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                You can add a comment by filling out the form below. Plain text\n                formatting.\n                ')
                    else:
                        __content = __cache_4708779776
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</p>\n\n                ')

                    # <Static value=<ast.Dict object at 0x109c887f0> name=None at 109c881f0> -> __attrs_4708790432
                    __attrs_4708790432 = _static_4459104240

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __default_4708782560
                    __default_4708782560 = _DEFAULT_MARKER

                    # <Value 'view/form/render' (236:44)> -> __cache_4708788512
                    __token = 12241
                    try:
                        __zt_tmp = __attrs_4708790432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4708788512 = _static_4459168576('path', 'view/form/render', econtext=econtext)(_static_4459175296(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/form/render' (236:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 109c89f90> at 118aa4940> -> __condition
                    __expression = __cache_4708788512

                    # <Symbol value=<DEFAULT> at 109c89f90> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div />')
                    else:
                        __content = __cache_4708788512
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n\n            </fieldset>\n        </div>')
                __append('\n    </div>\n')
                __i18n_domain = __previous_i18n_domain_4705461408
            if (__backup_auth_token_4705231792 is __marker):
                del econtext['auth_token']
            else:
                econtext['auth_token'] = __backup_auth_token_4705231792
            if (__backup_wtool_4705237696 is __marker):
                del econtext['wtool']
            else:
                econtext['wtool'] = __backup_wtool_4705237696
            if (__backup_errors_4705223584 is __marker):
                del econtext['errors']
            else:
                econtext['errors'] = __backup_errors_4705223584
            if (__backup_showCommenterImage_4705232800 is __marker):
                del econtext['showCommenterImage']
            else:
                econtext['showCommenterImage'] = __backup_showCommenterImage_4705232800
            if (__backup_has_replies_4705223536 is __marker):
                del econtext['has_replies']
            else:
                econtext['has_replies'] = __backup_has_replies_4705223536
            if (__backup_replies_4705225312 is __marker):
                del econtext['replies']
            else:
                econtext['replies'] = __backup_replies_4705225312
            if (__backup_canReview_4705231744 is __marker):
                del econtext['canReview']
            else:
                econtext['canReview'] = __backup_canReview_4705231744
            if (__backup_isAnon_4705232656 is __marker):
                del econtext['isAnon']
            else:
                econtext['isAnon'] = __backup_isAnon_4705232656
            if (__backup_isDeleteOwnCommentAllowed_4705232608 is __marker):
                del econtext['isDeleteOwnCommentAllowed']
            else:
                econtext['isDeleteOwnCommentAllowed'] = __backup_isDeleteOwnCommentAllowed_4705232608
            if (__backup_isEditCommentAllowed_4705223008 is __marker):
                del econtext['isEditCommentAllowed']
            else:
                econtext['isEditCommentAllowed'] = __backup_isEditCommentAllowed_4705223008
            if (__backup_isAnonymousDiscussionAllowed_4705231504 is __marker):
                del econtext['isAnonymousDiscussionAllowed']
            else:
                econtext['isAnonymousDiscussionAllowed'] = __backup_isAnonymousDiscussionAllowed_4705231504
            if (__backup_isDiscussionAllowed_4705235248 is __marker):
                del econtext['isDiscussionAllowed']
            else:
                econtext['isDiscussionAllowed'] = __backup_isDiscussionAllowed_4705235248
            if (__backup_userHasReplyPermission_4705235488 is __marker):
                del econtext['userHasReplyPermission']
            else:
                econtext['userHasReplyPermission'] = __backup_userHasReplyPermission_4705235488
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }