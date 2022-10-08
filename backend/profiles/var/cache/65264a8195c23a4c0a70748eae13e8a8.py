# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/z3cform/templates/image_input.pt'

__tokens = {933: ('view/download_url', 23, 29), 974: (' python: view.value is not Non', 24, 22), 1028: ('n view/acti', 25, 21), 1071: ('ge view/allow_nocha', 26, 28), 1116: ('ype view/file_content_', 27, 21), 1160: ('icon view/file', 28, 16), 1200: ('ename view/fi', 29, 19), 52: ('view/id', 3, 23), 86: (' view/styl', 4, 25), 123: ('e view/tit', 5, 24), 159: ('ng view/l', 6, 22), 197: ('ick view/onc', 7, 24), 241: ('lick view/ondbl', 8, 26), 289: ('edown view/onmou', 9, 26), 336: ('ouseup view/on', 10, 23), 383: ('useover view/onm', 11, 24), 432: ('ousemove view/on', 12, 23), 480: ('nmouseout view/', 13, 21), 527: ('onkeypress view', 14, 20), 573: ('  onkeydown vi', 15, 18), 616: ('     onkeyup', 16, 15), 657: ('      onfocu', 17, 14), 697: ('        onb', 18, 12), 738: ('       onchan', 19, 13), 781: ('        reado', 20, 12), 825: ('        access', 21, 12), 869: ('          ons', 22, 10), 1253: ('view/file_upload_id', 30, 30), 1289: ('up_id', 30, 66), 1330: ('${view/name}.file_upload_id', 31, 33), 1332: ('view/name', 31, 35), 1366: ('${up_id}', 31, 69), 1368: ('up_id', 31, 71), 1492: ('${view/value/filename}', 34, 8), 1494: ('view/value/filename', 34, 10), 1568: ("python:exists and download_url and action=='nochange'", 37, 25), 1654: ('download_url', 38, 30), 1707: ('view/thumb_tag', 39, 38), 1770: ('icon', 41, 28), 1823: ('icon', 42, 33), 1861: (' doc_typ', 43, 32), 1905: ('e filena', 44, 33), 1999: ('download_url', 47, 33), 1956: ('filename', 46, 25), 2103: ('doc_type', 49, 64), 2145: ('doc_type', 50, 31), 2263: ('view/file_size', 52, 37), 2292: ('sizekb', 52, 66), 2401: ('allow_nochange', 56, 26), 2610: ('string:${view/name}.action', 62, 37), 2672: (' string:${view/id}-nochang', 63, 34), 2739: ("k string:document.getElementById('${view/id}-input').disabled=tr", 64, 38), 2844: ("ed python:'checked' if action == 'nochange' else N", 65, 37), 2998: ('string:${view/id}-nochange', 68, 36), 3144: ('not:view/field/required', 70, 47), 3327: ('string:${view/name}.action', 75, 37), 3389: (' string:${view/id}-remov', 76, 34), 3454: ("k string:document.getElementById('${view/id}-input').disabled=tr", 77, 38), 3559: ("ed python:'checked' if action == 'remove' else N", 78, 37), 3711: ('string:${view/id}-remove', 81, 36), 4004: ('string:${view/name}.action', 89, 37), 4066: (' string:${view/id}-replac', 90, 34), 4132: ("k string:document.getElementById('${view/id}-input').disabled=fal", 91, 38), 4238: ("ed python:'checked' if action == 'replace' else N", 92, 37), 4391: ('string:${view/id}-replace', 95, 36), 4600: ('string:${view/id}-input', 102, 27), 4653: (' view/nam', 103, 28), 4696: ("d python:view.required and 'required' or No", 104, 31), 4769: ('ze view/s', 105, 26), 4812: ('led view/disa', 106, 29), 4860: ('ngth view/maxl', 107, 29), 4921: ("python:allow_nochange and action != 'replace'", 110, 27), 5012: ("string:document.getElementById('${view/id}-input').disabled=true;", 111, 21)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4485013056 = {'type': 'text/javascript', }
_static_4483063744 = {'type': 'file', 'class': 'form-control', 'id': 'string:${view/id}-input', 'name': 'view/name', 'required': "python:view.required and 'required' or None", 'size': 'view/size', 'disabled': 'view/disabled', 'maxlength': 'view/maxlength', }
_static_4485013728 = {'class': 'form-check-label', 'for': 'string:${view/id}-replace', }
_static_4485013968 = {'type': 'radio', 'value': 'replace', 'class': 'form-check-input', 'name': 'string:${view/name}.action', 'id': 'string:${view/id}-replace', 'onclick': "string:document.getElementById('${view/id}-input').disabled=false", 'checked': "python:'checked' if action == 'replace' else None", }
_static_4485017760 = {'class': 'form-check', }
_static_4483056400 = {'class': 'form-check-label', 'for': 'string:${view/id}-remove', }
_static_4483059088 = {'type': 'radio', 'value': 'remove', 'class': 'form-check-input', 'name': 'string:${view/name}.action', 'id': 'string:${view/id}-remove', 'onclick': "string:document.getElementById('${view/id}-input').disabled=true", 'checked': "python:'checked' if action == 'remove' else None", }
_static_4483059568 = {'class': 'form-check', }
_static_4483071232 = {'class': 'form-check-label', 'for': 'string:${view/id}-nochange', }
_static_4483064176 = {'type': 'radio', 'value': 'nochange', 'class': 'form-check-input', 'name': 'string:${view/name}.action', 'id': 'string:${view/id}-nochange', 'onclick': "string:document.getElementById('${view/id}-input').disabled=true", 'checked': "python:'checked' if action == 'nochange' else None", }
_static_4483066336 = {'class': 'form-check', }
_static_4485070128 = {'class': 'discreet', }
_static_4485070368 = {'href': 'download_url', }
_static_4485066144 = {'src': '', 'alt': '', 'title': 'filename', }
_static_4485061152 = {'href': 'download_url', }
_static_4485056880 = {'type': 'hidden', 'name': '${view/name}.file_upload_id', 'value': '${up_id}', }
_static_4418309904 = {}
_static_4417565216 = __C2ZContextWrapper
_static_4417553984 = __compile_zt_expr
_static_4485155040 = {'id': 'view/id', 'style': 'view/style', 'title': 'view/title', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'readonly': 'view/readonly', 'accesskey': 'view/accesskey', 'onselect': 'view/onselect', }

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

            # <Static value=<ast.Dict object at 0x10b5608e0> name=None at 10b5607f0> -> __attrs_4485159696
            __attrs_4485159696 = _static_4485155040
            __backup_download_url_4482928112 = get('download_url', __marker)

            # <Value 'view/download_url' (23:29)> -> __value
            __token = 933
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4417553984('path', 'view/download_url', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            econtext['download_url'] = __value
            __backup_exists_4483148256 = get('exists', __marker)

            # <Value 'python: view.value is not None' (24:22)> -> __value
            __token = 974
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4417553984('python', ' view.value is not None', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            econtext['exists'] = __value
            __backup_action_4482926528 = get('action', __marker)

            # <Value 'view/action' (25:21)> -> __value
            __token = 1028
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4417553984('path', 'view/action', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            econtext['action'] = __value
            __backup_allow_nochange_4484845808 = get('allow_nochange', __marker)

            # <Value 'view/allow_nochange' (26:28)> -> __value
            __token = 1071
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4417553984('path', 'view/allow_nochange', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            econtext['allow_nochange'] = __value
            __backup_doc_type_4484948576 = get('doc_type', __marker)

            # <Value 'view/file_content_type' (27:21)> -> __value
            __token = 1116
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4417553984('path', 'view/file_content_type', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            econtext['doc_type'] = __value
            __backup_icon_4482934064 = get('icon', __marker)

            # <Value 'view/file_icon' (28:16)> -> __value
            __token = 1160
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4417553984('path', 'view/file_icon', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            econtext['icon'] = __value
            __backup_filename_4484948336 = get('filename', __marker)

            # <Value 'view/filename' (29:19)> -> __value
            __token = 1200
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4417553984('path', 'view/filename', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            econtext['filename'] = __value
            __previous_i18n_domain_4485158016 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div')

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485165072
            __default_4485165072 = _DEFAULT_MARKER

            # <Substitution 'view/id' (3:23)> -> __attr_id
            __token = 52
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_4417553984('path', 'view/id', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485163248
            __default_4485163248 = _DEFAULT_MARKER

            # <Substitution 'view/style' (4:25)> -> __attr_style
            __token = 86
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_4417553984('path', 'view/style', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485161376
            __default_4485161376 = _DEFAULT_MARKER

            # <Substitution 'view/title' (5:24)> -> __attr_title
            __token = 123
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_4417553984('path', 'view/title', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485154272
            __default_4485154272 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (6:22)> -> __attr_lang
            __token = 159
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_4417553984('path', 'view/lang', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485160032
            __default_4485160032 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (7:24)> -> __attr_onclick
            __token = 197
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_4417553984('path', 'view/onclick', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485155328
            __default_4485155328 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (8:26)> -> __attr_ondblclick
            __token = 241
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_4417553984('path', 'view/ondblclick', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485160464
            __default_4485160464 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (9:26)> -> __attr_onmousedown
            __token = 289
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_4417553984('path', 'view/onmousedown', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485161712
            __default_4485161712 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (10:23)> -> __attr_onmouseup
            __token = 336
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_4417553984('path', 'view/onmouseup', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485162048
            __default_4485162048 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (11:24)> -> __attr_onmouseover
            __token = 383
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_4417553984('path', 'view/onmouseover', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485162384
            __default_4485162384 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (12:23)> -> __attr_onmousemove
            __token = 432
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_4417553984('path', 'view/onmousemove', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485162720
            __default_4485162720 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (13:21)> -> __attr_onmouseout
            __token = 480
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_4417553984('path', 'view/onmouseout', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485163056
            __default_4485163056 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (14:20)> -> __attr_onkeypress
            __token = 527
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_4417553984('path', 'view/onkeypress', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485163632
            __default_4485163632 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (15:18)> -> __attr_onkeydown
            __token = 573
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_4417553984('path', 'view/onkeydown', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485164688
            __default_4485164688 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (16:15)> -> __attr_onkeyup
            __token = 616
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_4417553984('path', 'view/onkeyup', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485165216
            __default_4485165216 = _DEFAULT_MARKER

            # <Substitution 'view/onfocus' (17:14)> -> __attr_onfocus
            __token = 657
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_4417553984('path', 'view/onfocus', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485164208
            __default_4485164208 = _DEFAULT_MARKER

            # <Substitution 'view/onblur' (18:12)> -> __attr_onblur
            __token = 697
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_4417553984('path', 'view/onblur', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485153024
            __default_4485153024 = _DEFAULT_MARKER

            # <Substitution 'view/onchange' (19:13)> -> __attr_onchange
            __token = 738
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_4417553984('path', 'view/onchange', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((' onchange="%s"' % __attr_onchange))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485154704
            __default_4485154704 = _DEFAULT_MARKER

            # <Boolean 'view/readonly' (20:12)> -> __attr_readonly
            __token = 781
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_readonly = _static_4417553984('path', 'view/readonly', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            if (__attr_readonly is _DEFAULT_MARKER):
                __attr_readonly = None
            else:
                if __attr_readonly:
                    __attr_readonly = 'readonly'
                else:
                    __attr_readonly = None
            if (__attr_readonly is not None):
                __append((' readonly="%s"' % __attr_readonly))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485155904
            __default_4485155904 = _DEFAULT_MARKER

            # <Substitution 'view/accesskey' (21:12)> -> __attr_accesskey
            __token = 825
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_accesskey = _static_4417553984('path', 'view/accesskey', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_accesskey is not None):
                __append((' accesskey="%s"' % __attr_accesskey))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485154560
            __default_4485154560 = _DEFAULT_MARKER

            # <Substitution 'view/onselect' (22:10)> -> __attr_onselect
            __token = 869
            try:
                __zt_tmp = __attrs_4485159696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onselect = _static_4417553984('path', 'view/onselect', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onselect is not None):
                __append((' onselect="%s"' % __attr_onselect))
            __append('>\n    ')

            # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4485157200
            __attrs_4485157200 = _static_4418309904
            __backup_up_id_4484941616 = get('up_id', __marker)

            # <Value 'view/file_upload_id' (30:30)> -> __value
            __token = 1253
            try:
                __zt_tmp = __attrs_4485157200
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4417553984('path', 'view/file_upload_id', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            econtext['up_id'] = __value

            # <Value 'up_id' (30:66)> -> __condition
            __token = 1289
            try:
                __zt_tmp = __attrs_4485157200
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4417553984('path', 'up_id', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            if __condition:
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x10b548970> name=None at 10b548a90> -> __attrs_4485058128
                __attrs_4485058128 = _static_4485056880

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden"')

                # <Symbol value=<DEFAULT> at 107619600> -> __default_4485059232
                __default_4485059232 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${view/name}.file_upload_id' (31:33)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10b548cd0> -> __attr_name
                __token = 1330
                __token = 1332
                try:
                    __zt_tmp = __attrs_4485058128
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_4417553984('path', 'view/name', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_name = ('%s%s' % ((__attr_name if (__attr_name is not None) else ''), '.file_upload_id', ))
                if (__attr_name is None):
                    pass
                else:
                    if (__attr_name is _DEFAULT_MARKER):
                        __attr_name = None
                    else:
                        __tt = type(__attr_name)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __attr_name = str(__attr_name)
                        else:
                            if (__tt is bytes):
                                __attr_name = decode(__attr_name)
                            else:
                                if (__tt is not str):
                                    try:
                                        __attr_name = __attr_name.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__attr_name)
                                        __attr_name = (str(__attr_name) if (__attr_name is __converted) else __converted)
                                    else:
                                        __attr_name = __attr_name()
                if (__attr_name is not None):
                    __append((' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 107619600> -> __default_4485058368
                __default_4485058368 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${up_id}' (31:69)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10b548130> -> __attr_value
                __token = 1366
                __token = 1368
                try:
                    __zt_tmp = __attrs_4485058128
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4417553984('path', 'up_id', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_value = __attr_value
                if (__attr_value is None):
                    pass
                else:
                    if (__attr_value is _DEFAULT_MARKER):
                        __attr_value = None
                    else:
                        __tt = type(__attr_value)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __attr_value = str(__attr_value)
                        else:
                            if (__tt is bytes):
                                __attr_value = decode(__attr_value)
                            else:
                                if (__tt is not str):
                                    try:
                                        __attr_value = __attr_value.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__attr_value)
                                        __attr_value = (str(__attr_value) if (__attr_value is __converted) else __converted)
                                    else:
                                        __attr_value = __attr_value()
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append('/>\n      ')

                # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4485056112
                __attrs_4485056112 = _static_4418309904

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>\n        ')

                # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4485056544
                __attrs_4485056544 = _static_4418309904
                __stream_4485055872 = []
                __append_4485055872 = __stream_4485055872.append
                __append_4485055872('Image already uploaded:')
                __msgid_4485055872 = __re_whitespace(''.join(__stream_4485055872)).strip()
                if 'image_already_uploaded':
                    __append(translate('image_already_uploaded', mapping=None, default=__msgid_4485055872, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))

                # <Interpolation value=<Substitution '\n        ${view/value/filename}\n      ' (33:92)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10b5484f0> -> __content_4320017904
                __token = 1492
                __token = 1494
                try:
                    __zt_tmp = __attrs_4485056112
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_4320017904 = _static_4417553984('path', 'view/value/filename', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                __content_4320017904 = __quote(__content_4320017904, '\x00', '&#0;', None, None)
                __content_4320017904 = ('%s%s%s' % ('\n        ', (__content_4320017904 if (__content_4320017904 is not None) else ''), '\n      ', ))
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
                __append('</span>\n    ')
            if (__backup_up_id_4484941616 is __marker):
                del econtext['up_id']
            else:
                econtext['up_id'] = __backup_up_id_4484941616
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4485055488
            __attrs_4485055488 = _static_4418309904

            # <Value "python:exists and download_url and action=='nochange'" (37:25)> -> __condition
            __token = 1568
            try:
                __zt_tmp = __attrs_4485055488
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4417553984('python', "exists and download_url and action=='nochange'", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>\n      ')

                # <Static value=<ast.Dict object at 0x10b549a20> name=None at 10b549b70> -> __attrs_4485060576
                __attrs_4485060576 = _static_4485061152

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 107619600> -> __default_4485055392
                __default_4485055392 = _DEFAULT_MARKER

                # <Substitution 'download_url' (38:30)> -> __attr_href
                __token = 1654
                try:
                    __zt_tmp = __attrs_4485060576
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4417553984('path', 'download_url', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append('>\n          ')

                # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4485063504
                __attrs_4485063504 = _static_4418309904

                # <Symbol value=<DEFAULT> at 107619600> -> __default_4485059664
                __default_4485059664 = _DEFAULT_MARKER

                # <Value 'view/thumb_tag' (39:38)> -> __cache_4485060720
                __token = 1707
                try:
                    __zt_tmp = __attrs_4485063504
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4485060720 = _static_4417553984('path', 'view/thumb_tag', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/thumb_tag' (39:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107619600> at 10b549540> -> __condition
                __expression = __cache_4485060720

                # <Symbol value=<DEFAULT> at 107619600> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <img ... (0:0)
                    # --------------------------------------------------------
                    __append('<img/>')
                else:
                    __content = __cache_4485060720
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      </a>')

                # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4485066528
                __attrs_4485066528 = _static_4418309904

                # <br ... (0:0)
                # --------------------------------------------------------
                __append('<br />\n        ')

                # <Static value=<ast.Dict object at 0x10b54ada0> name=None at 10b5486d0> -> __attrs_4485063408
                __attrs_4485063408 = _static_4485066144

                # <Value 'icon' (41:28)> -> __condition
                __token = 1770
                try:
                    __zt_tmp = __attrs_4485063408
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4417553984('path', 'icon', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                if __condition:

                    # <img ... (0:0)
                    # --------------------------------------------------------
                    __append('<img')

                    # <Symbol value=<DEFAULT> at 107619600> -> __default_4485054864
                    __default_4485054864 = _DEFAULT_MARKER

                    # <Substitution 'icon' (42:33)> -> __attr_src
                    __token = 1823
                    try:
                        __zt_tmp = __attrs_4485063408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_src = _static_4417553984('path', 'icon', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    __attr_src = __quote(__attr_src, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_src is not None):
                        __append((' src="%s"' % __attr_src))

                    # <Symbol value=<DEFAULT> at 107619600> -> __default_4485066624
                    __default_4485066624 = _DEFAULT_MARKER

                    # <Substitution 'doc_type' (43:32)> -> __attr_alt
                    __token = 1861
                    try:
                        __zt_tmp = __attrs_4485063408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_alt = _static_4417553984('path', 'doc_type', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_alt is not None):
                        __append((' alt="%s"' % __attr_alt))

                    # <Symbol value=<DEFAULT> at 107619600> -> __default_4485062928
                    __default_4485062928 = _DEFAULT_MARKER

                    # <Substitution 'filename' (44:33)> -> __attr_title
                    __token = 1905
                    try:
                        __zt_tmp = __attrs_4485063408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_4417553984('path', 'filename', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append('/>')
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x10b54be20> name=None at 10b54be50> -> __attrs_4485067440
                __attrs_4485067440 = _static_4485070368

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 107619600> -> __default_4485068208
                __default_4485068208 = _DEFAULT_MARKER

                # <Substitution 'download_url' (47:33)> -> __attr_href
                __token = 1999
                try:
                    __zt_tmp = __attrs_4485067440
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4417553984('path', 'download_url', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' >')

                # <Symbol value=<DEFAULT> at 107619600> -> __default_4485056928
                __default_4485056928 = _DEFAULT_MARKER

                # <Value 'filename' (46:25)> -> __cache_4485064608
                __token = 1956
                try:
                    __zt_tmp = __attrs_4485067440
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4485064608 = _static_4417553984('path', 'filename', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))

                # <BinOp left=<Value 'filename' (46:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107619600> at 10b54a7d0> -> __condition
                __expression = __cache_4485064608

                # <Symbol value=<DEFAULT> at 107619600> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Filename')
                else:
                    __content = __cache_4485064608
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</a>\n        ')

                # <Static value=<ast.Dict object at 0x10b54bd30> name=None at 10b54bdc0> -> __attrs_4485069936
                __attrs_4485069936 = _static_4485070128

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span class="discreet"> &mdash;')

                # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4485062208
                __attrs_4485062208 = _static_4418309904

                # <Value 'doc_type' (49:64)> -> __condition
                __token = 2103
                try:
                    __zt_tmp = __attrs_4485062208
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4417553984('path', 'doc_type', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                if __condition:
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4483067296
                    __attrs_4483067296 = _static_4418309904

                    # <Symbol value=<DEFAULT> at 107619600> -> __default_4483066912
                    __default_4483066912 = _DEFAULT_MARKER

                    # <Value 'doc_type' (50:31)> -> __cache_4485068496
                    __token = 2145
                    try:
                        __zt_tmp = __attrs_4483067296
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4485068496 = _static_4417553984('path', 'doc_type', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))

                    # <BinOp left=<Value 'doc_type' (50:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107619600> at 10b362e30> -> __condition
                    __expression = __cache_4485068496

                    # <Symbol value=<DEFAULT> at 107619600> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>ContentType</span>')
                    else:
                        __content = __cache_4485068496
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(',')
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4483068208
                __attrs_4483068208 = _static_4418309904
                __backup_sizekb_4482442688 = get('sizekb', __marker)

                # <Value 'view/file_size' (52:37)> -> __value
                __token = 2263
                try:
                    __zt_tmp = __attrs_4483068208
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4417553984('path', 'view/file_size', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                econtext['sizekb'] = __value

                # <Symbol value=<DEFAULT> at 107619600> -> __default_4483068784
                __default_4483068784 = _DEFAULT_MARKER

                # <Value 'sizekb' (52:66)> -> __cache_4483068592
                __token = 2292
                try:
                    __zt_tmp = __attrs_4483068208
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4483068592 = _static_4417553984('path', 'sizekb', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))

                # <BinOp left=<Value 'sizekb' (52:66)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107619600> at 10b362e90> -> __condition
                __expression = __cache_4483068592

                # <Symbol value=<DEFAULT> at 107619600> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>100</span>')
                else:
                    __content = __cache_4483068592
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                if (__backup_sizekb_4482442688 is __marker):
                    del econtext['sizekb']
                else:
                    econtext['sizekb'] = __backup_sizekb_4482442688
                __append('\n        </span>\n    </span>')
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4483067824
            __attrs_4483067824 = _static_4418309904

            # <Value 'allow_nochange' (56:26)> -> __condition
            __token = 2401
            try:
                __zt_tmp = __attrs_4483067824
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4417553984('path', 'allow_nochange', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            if __condition:
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x10b3629e0> name=None at 10b362980> -> __attrs_4483065856
                __attrs_4483065856 = _static_4483066336

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-check">\n            ')

                # <Static value=<ast.Dict object at 0x10b362170> name=None at 10b361b10> -> __attrs_4483063888
                __attrs_4483063888 = _static_4483064176

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="radio" value="nochange" class="form-check-input"')

                # <Symbol value=<DEFAULT> at 107619600> -> __default_4483070896
                __default_4483070896 = _DEFAULT_MARKER

                # <Substitution 'string:${view/name}.action' (62:37)> -> __attr_name
                __token = 2610
                try:
                    __zt_tmp = __attrs_4483063888
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_4417553984('string', '${view/name}.action', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 107619600> -> __default_4483067200
                __default_4483067200 = _DEFAULT_MARKER

                # <Substitution 'string:${view/id}-nochange' (63:34)> -> __attr_id
                __token = 2672
                try:
                    __zt_tmp = __attrs_4483063888
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_4417553984('string', '${view/id}-nochange', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 107619600> -> __default_4483061776
                __default_4483061776 = _DEFAULT_MARKER

                # <Substitution "string:document.getElementById('${view/id}-input').disabled=true" (64:38)> -> __attr_onclick
                __token = 2739
                try:
                    __zt_tmp = __attrs_4483063888
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_onclick = _static_4417553984('string', "document.getElementById('${view/id}-input').disabled=true", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_onclick is not None):
                    __append((' onclick="%s"' % __attr_onclick))

                # <Symbol value=<DEFAULT> at 107619600> -> __default_4483062928
                __default_4483062928 = _DEFAULT_MARKER

                # <Boolean "python:'checked' if action == 'nochange' else None" (65:37)> -> __attr_checked
                __token = 2844
                try:
                    __zt_tmp = __attrs_4483063888
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_checked = _static_4417553984('python', "'checked' if action == 'nochange' else None", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                if (__attr_checked is _DEFAULT_MARKER):
                    __attr_checked = None
                else:
                    if __attr_checked:
                        __attr_checked = 'checked'
                    else:
                        __attr_checked = None
                if (__attr_checked is not None):
                    __append((' checked="%s"' % __attr_checked))
                __append(' />\n            ')

                # <Static value=<ast.Dict object at 0x10b363d00> name=None at 10b360550> -> __attrs_4483056688
                __attrs_4483056688 = _static_4483071232

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="form-check-label"')

                # <Symbol value=<DEFAULT> at 107619600> -> __default_4483065232
                __default_4483065232 = _DEFAULT_MARKER

                # <Substitution 'string:${view/id}-nochange' (68:36)> -> __attr_for
                __token = 2998
                try:
                    __zt_tmp = __attrs_4483056688
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_for = _static_4417553984('string', '${view/id}-nochange', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_for is not None):
                    __append((' for="%s"' % __attr_for))
                __append('>')
                __stream_4483064752 = []
                __append_4483064752 = __stream_4483064752.append
                __append_4483064752('Keep existing image')
                __msgid_4483064752 = __re_whitespace(''.join(__stream_4483064752)).strip()
                if 'image_keep':
                    __append(translate('image_keep', mapping=None, default=__msgid_4483064752, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>\n        </div>\n        ')

                # <Static value=<ast.Dict object at 0x10b360f70> name=None at 10b360f10> -> __attrs_4483059664
                __attrs_4483059664 = _static_4483059568

                # <Value 'not:view/field/required' (70:47)> -> __condition
                __token = 3144
                try:
                    __zt_tmp = __attrs_4483059664
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4417553984('not', 'view/field/required', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-check">\n            ')

                    # <Static value=<ast.Dict object at 0x10b360d90> name=None at 10b360700> -> __attrs_4483064272
                    __attrs_4483064272 = _static_4483059088

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="radio" value="remove" class="form-check-input"')

                    # <Symbol value=<DEFAULT> at 107619600> -> __default_4483060528
                    __default_4483060528 = _DEFAULT_MARKER

                    # <Substitution 'string:${view/name}.action' (75:37)> -> __attr_name
                    __token = 3327
                    try:
                        __zt_tmp = __attrs_4483064272
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_name = _static_4417553984('string', '${view/name}.action', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_name is not None):
                        __append((' name="%s"' % __attr_name))

                    # <Symbol value=<DEFAULT> at 107619600> -> __default_4483061248
                    __default_4483061248 = _DEFAULT_MARKER

                    # <Substitution 'string:${view/id}-remove' (76:34)> -> __attr_id
                    __token = 3389
                    try:
                        __zt_tmp = __attrs_4483064272
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_4417553984('string', '${view/id}-remove', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 107619600> -> __default_4483057696
                    __default_4483057696 = _DEFAULT_MARKER

                    # <Substitution "string:document.getElementById('${view/id}-input').disabled=true" (77:38)> -> __attr_onclick
                    __token = 3454
                    try:
                        __zt_tmp = __attrs_4483064272
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_onclick = _static_4417553984('string', "document.getElementById('${view/id}-input').disabled=true", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_onclick is not None):
                        __append((' onclick="%s"' % __attr_onclick))

                    # <Symbol value=<DEFAULT> at 107619600> -> __default_4483057792
                    __default_4483057792 = _DEFAULT_MARKER

                    # <Boolean "python:'checked' if action == 'remove' else None" (78:37)> -> __attr_checked
                    __token = 3559
                    try:
                        __zt_tmp = __attrs_4483064272
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_checked = _static_4417553984('python', "'checked' if action == 'remove' else None", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    if (__attr_checked is _DEFAULT_MARKER):
                        __attr_checked = None
                    else:
                        if __attr_checked:
                            __attr_checked = 'checked'
                        else:
                            __attr_checked = None
                    if (__attr_checked is not None):
                        __append((' checked="%s"' % __attr_checked))
                    __append(' />\n            ')

                    # <Static value=<ast.Dict object at 0x10b360310> name=None at 10b3602b0> -> __attrs_4483055920
                    __attrs_4483055920 = _static_4483056400

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append('<label class="form-check-label"')

                    # <Symbol value=<DEFAULT> at 107619600> -> __default_4483059040
                    __default_4483059040 = _DEFAULT_MARKER

                    # <Substitution 'string:${view/id}-remove' (81:36)> -> __attr_for
                    __token = 3711
                    try:
                        __zt_tmp = __attrs_4483055920
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_for = _static_4417553984('string', '${view/id}-remove', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_for is not None):
                        __append((' for="%s"' % __attr_for))
                    __append('>')
                    __stream_4483058272 = []
                    __append_4483058272 = __stream_4483058272.append
                    __append_4483058272('Remove existing image')
                    __msgid_4483058272 = __re_whitespace(''.join(__stream_4483058272)).strip()
                    if 'image_remove':
                        __append(translate('image_remove', mapping=None, default=__msgid_4483058272, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</label>\n        </div>')
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x10b53f0a0> name=None at 10b53f400> -> __attrs_4485017520
                __attrs_4485017520 = _static_4485017760

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-check">\n            ')

                # <Static value=<ast.Dict object at 0x10b53e1d0> name=None at 10b53d540> -> __attrs_4485019296
                __attrs_4485019296 = _static_4485013968

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="radio" value="replace" class="form-check-input"')

                # <Symbol value=<DEFAULT> at 107619600> -> __default_4485019920
                __default_4485019920 = _DEFAULT_MARKER

                # <Substitution 'string:${view/name}.action' (89:37)> -> __attr_name
                __token = 4004
                try:
                    __zt_tmp = __attrs_4485019296
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_4417553984('string', '${view/name}.action', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 107619600> -> __default_4485011088
                __default_4485011088 = _DEFAULT_MARKER

                # <Substitution 'string:${view/id}-replace' (90:34)> -> __attr_id
                __token = 4066
                try:
                    __zt_tmp = __attrs_4485019296
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_4417553984('string', '${view/id}-replace', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 107619600> -> __default_4485020448
                __default_4485020448 = _DEFAULT_MARKER

                # <Substitution "string:document.getElementById('${view/id}-input').disabled=false" (91:38)> -> __attr_onclick
                __token = 4132
                try:
                    __zt_tmp = __attrs_4485019296
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_onclick = _static_4417553984('string', "document.getElementById('${view/id}-input').disabled=false", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_onclick is not None):
                    __append((' onclick="%s"' % __attr_onclick))

                # <Symbol value=<DEFAULT> at 107619600> -> __default_4485020736
                __default_4485020736 = _DEFAULT_MARKER

                # <Boolean "python:'checked' if action == 'replace' else None" (92:37)> -> __attr_checked
                __token = 4238
                try:
                    __zt_tmp = __attrs_4485019296
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_checked = _static_4417553984('python', "'checked' if action == 'replace' else None", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                if (__attr_checked is _DEFAULT_MARKER):
                    __attr_checked = None
                else:
                    if __attr_checked:
                        __attr_checked = 'checked'
                    else:
                        __attr_checked = None
                if (__attr_checked is not None):
                    __append((' checked="%s"' % __attr_checked))
                __append(' />\n            ')

                # <Static value=<ast.Dict object at 0x10b53e0e0> name=None at 10b53e560> -> __attrs_4485011232
                __attrs_4485011232 = _static_4485013728

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="form-check-label"')

                # <Symbol value=<DEFAULT> at 107619600> -> __default_4485021312
                __default_4485021312 = _DEFAULT_MARKER

                # <Substitution 'string:${view/id}-replace' (95:36)> -> __attr_for
                __token = 4391
                try:
                    __zt_tmp = __attrs_4485011232
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_for = _static_4417553984('string', '${view/id}-replace', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_for is not None):
                    __append((' for="%s"' % __attr_for))
                __append('>')
                __stream_4485020928 = []
                __append_4485020928 = __stream_4485020928.append
                __append_4485020928('Replace with new image')
                __msgid_4485020928 = __re_whitespace(''.join(__stream_4485020928)).strip()
                if 'image_replace':
                    __append(translate('image_replace', mapping=None, default=__msgid_4485020928, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>\n        </div>\n    ')
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x10b361fc0> name=None at 10b362770> -> __attrs_4485008016
            __attrs_4485008016 = _static_4483063744

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="file" class="form-control"')

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485015312
            __default_4485015312 = _DEFAULT_MARKER

            # <Substitution 'string:${view/id}-input' (102:27)> -> __attr_id
            __token = 4600
            try:
                __zt_tmp = __attrs_4485008016
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_4417553984('string', '${view/id}-input', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485011376
            __default_4485011376 = _DEFAULT_MARKER

            # <Substitution 'view/name' (103:28)> -> __attr_name
            __token = 4653
            try:
                __zt_tmp = __attrs_4485008016
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_4417553984('path', 'view/name', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485016800
            __default_4485016800 = _DEFAULT_MARKER

            # <Substitution "python:view.required and 'required' or None" (104:31)> -> __attr_required
            __token = 4696
            try:
                __zt_tmp = __attrs_4485008016
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_required = _static_4417553984('python', "view.required and 'required' or None", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_required = __quote(__attr_required, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_required is not None):
                __append((' required="%s"' % __attr_required))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485013872
            __default_4485013872 = _DEFAULT_MARKER

            # <Substitution 'view/size' (105:26)> -> __attr_size
            __token = 4769
            try:
                __zt_tmp = __attrs_4485008016
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_size = _static_4417553984('path', 'view/size', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_size = __quote(__attr_size, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_size is not None):
                __append((' size="%s"' % __attr_size))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485016416
            __default_4485016416 = _DEFAULT_MARKER

            # <Boolean 'view/disabled' (106:29)> -> __attr_disabled
            __token = 4812
            try:
                __zt_tmp = __attrs_4485008016
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_disabled = _static_4417553984('path', 'view/disabled', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            if (__attr_disabled is _DEFAULT_MARKER):
                __attr_disabled = None
            else:
                if __attr_disabled:
                    __attr_disabled = 'disabled'
                else:
                    __attr_disabled = None
            if (__attr_disabled is not None):
                __append((' disabled="%s"' % __attr_disabled))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485015792
            __default_4485015792 = _DEFAULT_MARKER

            # <Substitution 'view/maxlength' (107:29)> -> __attr_maxlength
            __token = 4860
            try:
                __zt_tmp = __attrs_4485008016
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_maxlength = _static_4417553984('path', 'view/maxlength', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_maxlength = __quote(__attr_maxlength, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_maxlength is not None):
                __append((' maxlength="%s"' % __attr_maxlength))
            __append(' />\n\n    ')

            # <Static value=<ast.Dict object at 0x10b53de40> name=None at 10b53dea0> -> __attrs_4485011616
            __attrs_4485011616 = _static_4485013056

            # <Value "python:allow_nochange and action != 'replace'" (110:27)> -> __condition
            __token = 4921
            try:
                __zt_tmp = __attrs_4485011616
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4417553984('python', "allow_nochange and action != 'replace'", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            if __condition:

                # <script ... (0:0)
                # --------------------------------------------------------
                __append('<script type="text/javascript">')

                # <Symbol value=<DEFAULT> at 107619600> -> __default_4485009456
                __default_4485009456 = _DEFAULT_MARKER

                # <Value "string:document.getElementById('${view/id}-input').disabled=true;" (111:21)> -> __cache_4485009744
                __token = 5012
                try:
                    __zt_tmp = __attrs_4485011616
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4485009744 = _static_4417553984('string', "document.getElementById('${view/id}-input').disabled=true;", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))

                # <BinOp left=<Value "string:document.getElementById('${view/id}-input').disabled=true;" (111:21)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107619600> at 10b53dba0> -> __condition
                __expression = __cache_4485009744

                # <Symbol value=<DEFAULT> at 107619600> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n    ')
                else:
                    __content = __cache_4485009744
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</script>')
            __append('\n\n</div>')
            __i18n_domain = __previous_i18n_domain_4485158016
            if (__backup_filename_4484948336 is __marker):
                del econtext['filename']
            else:
                econtext['filename'] = __backup_filename_4484948336
            if (__backup_icon_4482934064 is __marker):
                del econtext['icon']
            else:
                econtext['icon'] = __backup_icon_4482934064
            if (__backup_doc_type_4484948576 is __marker):
                del econtext['doc_type']
            else:
                econtext['doc_type'] = __backup_doc_type_4484948576
            if (__backup_allow_nochange_4484845808 is __marker):
                del econtext['allow_nochange']
            else:
                econtext['allow_nochange'] = __backup_allow_nochange_4484845808
            if (__backup_action_4482926528 is __marker):
                del econtext['action']
            else:
                econtext['action'] = __backup_action_4482926528
            if (__backup_exists_4483148256 is __marker):
                del econtext['exists']
            else:
                econtext['exists'] = __backup_exists_4483148256
            if (__backup_download_url_4482928112 is __marker):
                del econtext['download_url']
            else:
                econtext['download_url'] = __backup_download_url_4482928112
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }