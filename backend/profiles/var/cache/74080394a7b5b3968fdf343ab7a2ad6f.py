# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/formwidget/namedfile/image_display.pt'

__tokens = {749: ('view/value', 17, 26), 787: (' python:value is not Non', 18, 26), 66: ('view/id', 2, 25), 102: (' view/klas', 3, 27), 141: ('e view/sty', 4, 26), 180: ('le view/ti', 5, 25), 218: ('ang view/', 6, 23), 258: ('lick view/on', 7, 25), 304: ('click view/ondb', 8, 27), 354: ('sedown view/onmo', 9, 27), 403: ('mouseup view/o', 10, 24), 452: ('ouseover view/on', 11, 25), 503: ('mousemove view/o', 12, 24), 553: ('onmouseout view', 13, 22), 602: (' onkeypress vie', 14, 21), 650: ('   onkeydown v', 15, 19), 695: ('      onkeyu', 16, 16), 851: ('view/field/__name__ | nothing', 19, 35), 915: (' view/filenam', 20, 33), 971: ('d view/filename_encod', 21, 40), 1024: ('th view/wi', 22, 28), 1067: ('ght view/he', 23, 28), 1108: (' alt vie', 24, 24), 1151: ('python:exists and fieldname', 25, 28), 1213: ('view/download_url', 26, 33), 1267: (' view/heigh', 27, 35), 1314: ('h view/wid', 28, 33), 1358: ('lt view/', 29, 30), 1415: ('not:exists', 31, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4900790784 = {'class': 'discreet', }
_static_4900483520 = {'src': 'view/download_url', 'height': 'view/height', 'width': 'view/width', 'alt': 'view/alt', }
_static_4439051040 = __C2ZContextWrapper
_static_4439058528 = __compile_zt_expr
_static_4899294464 = {'id': '', 'class': '', 'style': 'view/style', 'title': 'view/title', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', }

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

            # <Static value=<ast.Dict object at 0x124054d00> name=None at 124054ee0> -> __attrs_4900472144
            __attrs_4900472144 = _static_4899294464
            __backup_value_4607368768 = get('value', __marker)

            # <Value 'view/value' (17:26)> -> __value
            __token = 749
            try:
                __zt_tmp = __attrs_4900472144
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'view/value', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['value'] = __value
            __backup_exists_4685234672 = get('exists', __marker)

            # <Value 'python:value is not None' (18:26)> -> __value
            __token = 787
            try:
                __zt_tmp = __attrs_4900472144
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('python', 'value is not None', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['exists'] = __value
            __previous_i18n_domain_4900471904 = __i18n_domain
            __i18n_domain = 'plone'

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span')

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900783872
            __default_4900783872 = _DEFAULT_MARKER

            # <Substitution 'view/id' (2:25)> -> __attr_id
            __token = 66
            try:
                __zt_tmp = __attrs_4900472144
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_4439058528('path', 'view/id', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900795584
            __default_4900795584 = _DEFAULT_MARKER

            # <Substitution 'view/klass' (3:27)> -> __attr_class
            __token = 102
            try:
                __zt_tmp = __attrs_4900472144
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4439058528('path', 'view/klass', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900796736
            __default_4900796736 = _DEFAULT_MARKER

            # <Substitution 'view/style' (4:26)> -> __attr_style
            __token = 141
            try:
                __zt_tmp = __attrs_4900472144
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_4439058528('path', 'view/style', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900791744
            __default_4900791744 = _DEFAULT_MARKER

            # <Substitution 'view/title' (5:25)> -> __attr_title
            __token = 180
            try:
                __zt_tmp = __attrs_4900472144
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_4439058528('path', 'view/title', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900792464
            __default_4900792464 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (6:23)> -> __attr_lang
            __token = 218
            try:
                __zt_tmp = __attrs_4900472144
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_4439058528('path', 'view/lang', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900485008
            __default_4900485008 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (7:25)> -> __attr_onclick
            __token = 258
            try:
                __zt_tmp = __attrs_4900472144
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_4439058528('path', 'view/onclick', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900477664
            __default_4900477664 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (8:27)> -> __attr_ondblclick
            __token = 304
            try:
                __zt_tmp = __attrs_4900472144
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_4439058528('path', 'view/ondblclick', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900477040
            __default_4900477040 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (9:27)> -> __attr_onmousedown
            __token = 354
            try:
                __zt_tmp = __attrs_4900472144
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_4439058528('path', 'view/onmousedown', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900472192
            __default_4900472192 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (10:24)> -> __attr_onmouseup
            __token = 403
            try:
                __zt_tmp = __attrs_4900472144
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_4439058528('path', 'view/onmouseup', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900478336
            __default_4900478336 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (11:25)> -> __attr_onmouseover
            __token = 452
            try:
                __zt_tmp = __attrs_4900472144
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_4439058528('path', 'view/onmouseover', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900473296
            __default_4900473296 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (12:24)> -> __attr_onmousemove
            __token = 503
            try:
                __zt_tmp = __attrs_4900472144
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_4439058528('path', 'view/onmousemove', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900484960
            __default_4900484960 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (13:22)> -> __attr_onmouseout
            __token = 553
            try:
                __zt_tmp = __attrs_4900472144
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_4439058528('path', 'view/onmouseout', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900477280
            __default_4900477280 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (14:21)> -> __attr_onkeypress
            __token = 602
            try:
                __zt_tmp = __attrs_4900472144
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_4439058528('path', 'view/onkeypress', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900486160
            __default_4900486160 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (15:19)> -> __attr_onkeydown
            __token = 650
            try:
                __zt_tmp = __attrs_4900472144
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_4439058528('path', 'view/onkeydown', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900478144
            __default_4900478144 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (16:16)> -> __attr_onkeyup
            __token = 695
            try:
                __zt_tmp = __attrs_4900472144
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_4439058528('path', 'view/onkeyup', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))
            __append('>\n        ')

            # <Static value=<ast.Dict object at 0x1241771c0> name=None at 124176950> -> __attrs_4900783536
            __attrs_4900783536 = _static_4900483520
            __backup_fieldname_4880314384 = get('fieldname', __marker)

            # <Value 'view/field/__name__ | nothing' (19:35)> -> __value
            __token = 851
            try:
                __zt_tmp = __attrs_4900783536
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'view/field/__name__ | nothing', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['fieldname'] = __value
            __backup_filename_4877132864 = get('filename', __marker)

            # <Value 'view/filename' (20:33)> -> __value
            __token = 915
            try:
                __zt_tmp = __attrs_4900783536
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'view/filename', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['filename'] = __value
            __backup_filename_encoded_4880698240 = get('filename_encoded', __marker)

            # <Value 'view/filename_encoded' (21:40)> -> __value
            __token = 971
            try:
                __zt_tmp = __attrs_4900783536
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'view/filename_encoded', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['filename_encoded'] = __value
            __backup_width_4880700496 = get('width', __marker)

            # <Value 'view/width' (22:28)> -> __value
            __token = 1024
            try:
                __zt_tmp = __attrs_4900783536
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'view/width', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['width'] = __value
            __backup_height_4877781936 = get('height', __marker)

            # <Value 'view/height' (23:28)> -> __value
            __token = 1067
            try:
                __zt_tmp = __attrs_4900783536
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'view/height', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['height'] = __value
            __backup_alt_4877125520 = get('alt', __marker)

            # <Value 'view/alt' (24:24)> -> __value
            __token = 1108
            try:
                __zt_tmp = __attrs_4900783536
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'view/alt', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['alt'] = __value

            # <Value 'python:exists and fieldname' (25:28)> -> __condition
            __token = 1151
            try:
                __zt_tmp = __attrs_4900783536
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4439058528('python', 'exists and fieldname', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            if __condition:

                # <img ... (0:0)
                # --------------------------------------------------------
                __append('<img')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900474112
                __default_4900474112 = _DEFAULT_MARKER

                # <Substitution 'view/download_url' (26:33)> -> __attr_src
                __token = 1213
                try:
                    __zt_tmp = __attrs_4900783536
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_src = _static_4439058528('path', 'view/download_url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_src is not None):
                    __append((' src="%s"' % __attr_src))

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900472384
                __default_4900472384 = _DEFAULT_MARKER

                # <Substitution 'view/height' (27:35)> -> __attr_height
                __token = 1267
                try:
                    __zt_tmp = __attrs_4900783536
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_height = _static_4439058528('path', 'view/height', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __attr_height = __quote(__attr_height, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_height is not None):
                    __append((' height="%s"' % __attr_height))

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900486592
                __default_4900486592 = _DEFAULT_MARKER

                # <Substitution 'view/width' (28:33)> -> __attr_width
                __token = 1314
                try:
                    __zt_tmp = __attrs_4900783536
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_width = _static_4439058528('path', 'view/width', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __attr_width = __quote(__attr_width, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_width is not None):
                    __append((' width="%s"' % __attr_width))

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900782672
                __default_4900782672 = _DEFAULT_MARKER

                # <Substitution 'view/alt' (29:30)> -> __attr_alt
                __token = 1358
                try:
                    __zt_tmp = __attrs_4900783536
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_alt = _static_4439058528('path', 'view/alt', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __attr_alt = __quote(__attr_alt, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_alt is not None):
                    __append((' alt="%s"' % __attr_alt))
                __append(' />')
            if (__backup_alt_4877125520 is __marker):
                del econtext['alt']
            else:
                econtext['alt'] = __backup_alt_4877125520
            if (__backup_height_4877781936 is __marker):
                del econtext['height']
            else:
                econtext['height'] = __backup_height_4877781936
            if (__backup_width_4880700496 is __marker):
                del econtext['width']
            else:
                econtext['width'] = __backup_width_4880700496
            if (__backup_filename_encoded_4880698240 is __marker):
                del econtext['filename_encoded']
            else:
                econtext['filename_encoded'] = __backup_filename_encoded_4880698240
            if (__backup_filename_4877132864 is __marker):
                del econtext['filename']
            else:
                econtext['filename'] = __backup_filename_4877132864
            if (__backup_fieldname_4880314384 is __marker):
                del econtext['fieldname']
            else:
                econtext['fieldname'] = __backup_fieldname_4880314384
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x1241c2200> name=None at 1241c1540> -> __attrs_4900786608
            __attrs_4900786608 = _static_4900790784

            # <Value 'not:exists' (31:29)> -> __condition
            __token = 1415
            try:
                __zt_tmp = __attrs_4900786608
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4439058528('not', 'exists', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span class="discreet">')
                __stream_4900795200 = []
                __append_4900795200 = __stream_4900795200.append
                __append_4900795200('\n            No image\n        ')
                __msgid_4900795200 = __re_whitespace(''.join(__stream_4900795200)).strip()
                if 'no_image':
                    __append(translate('no_image', mapping=None, default=__msgid_4900795200, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</span>')
            __append('\n</span>')
            __i18n_domain = __previous_i18n_domain_4900471904
            if (__backup_exists_4685234672 is __marker):
                del econtext['exists']
            else:
                econtext['exists'] = __backup_exists_4685234672
            if (__backup_value_4607368768 is __marker):
                del econtext['value']
            else:
                econtext['value'] = __backup_value_4607368768
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }