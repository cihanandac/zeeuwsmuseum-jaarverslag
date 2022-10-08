# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/z3cform/templates/select_input.pt'

__tokens = {218: ('view/id', 5, 27), 255: (' string:${view/name}:lis', 6, 28), 387: ('ss string:form-select ${view/kla', 8, 27), 1121: ('         tabi', 23, 15), 1074: ('        disab', 22, 16), 1303: ('             ', 27, 11), 1346: ('         ', 28, 6), 313: ("d python:view.required and 'required' or No", 7, 31), 450: ('yle view/s', 9, 26), 491: ('itle view/', 10, 25), 531: (' lang vie', 11, 23), 573: ('nclick view/', 12, 25), 621: ('blclick view/on', 13, 27), 673: ('ousedown view/on', 14, 27), 724: ('onmouseup view', 15, 24), 775: ('nmouseover view/', 16, 25), 828: ('onmousemove view', 17, 24), 880: ('  onmouseout vi', 18, 22), 931: ('   onkeypress v', 19, 21), 981: ('     onkeydown', 20, 19), 1028: ('        onke', 21, 16), 1167: ('           o', 24, 13), 1211: ('           ', 25, 11), 1256: ('            o', 26, 12), 1405: ('view/items', 29, 24), 1487: ('item/selected', 31, 24), 1530: ('item/id', 32, 28), 1569: (' item/valu', 33, 30), 1604: ('item/content', 34, 22), 1682: ('not:item/selected', 36, 24), 1729: ('item/id', 37, 28), 1768: (' item/valu', 38, 30), 1803: ('item/content', 39, 22), 1940: ('string:${view/name}-empty-marker', 43, 28)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4485572608 = {'name': 'field-empty-marker', 'type': 'hidden', 'value': '1', }
_static_4480102752 = {'id': '', 'value': '', }
_static_4485572752 = {'id': '', 'value': '', 'selected': 'selected', }
_static_4418309904 = {}
_static_4417565216 = __C2ZContextWrapper
_static_4417553984 = __compile_zt_expr
_static_4485566512 = {'id': '', 'name': '', 'class': '', 'tabindex': '', 'disabled': '', 'multiple': '', 'size': '', 'required': "python:view.required and 'required' or None", 'style': 'view/style', 'title': 'view/title', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', }
_static_4485575008 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x10b5c7160> name=None at 10b5c6fe0> -> __attrs_4485568912
            __attrs_4485568912 = _static_4485575008
            __append('\n')

            # <Static value=<ast.Dict object at 0x10b5c5030> name=None at 10b5c4df0> -> __attrs_4485576640
            __attrs_4485576640 = _static_4485566512

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select')

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485569392
            __default_4485569392 = _DEFAULT_MARKER

            # <Substitution 'view/id' (5:27)> -> __attr_id
            __token = 218
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_4417553984('path', 'view/id', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485571456
            __default_4485571456 = _DEFAULT_MARKER

            # <Substitution 'string:${view/name}:list' (6:28)> -> __attr_name
            __token = 255
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_4417553984('string', '${view/name}:list', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485570448
            __default_4485570448 = _DEFAULT_MARKER

            # <Substitution 'string:form-select ${view/klass}' (8:27)> -> __attr_class
            __token = 387
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4417553984('string', 'form-select ${view/klass}', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485567568
            __default_4485567568 = _DEFAULT_MARKER

            # <Substitution 'view/tabindex' (23:15)> -> __attr_tabindex
            __token = 1121
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_tabindex = _static_4417553984('path', 'view/tabindex', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_tabindex is not None):
                __append((' tabindex="%s"' % __attr_tabindex))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485565984
            __default_4485565984 = _DEFAULT_MARKER

            # <Boolean 'view/disabled' (22:16)> -> __attr_disabled
            __token = 1074
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_disabled = _static_4417553984('path', 'view/disabled', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            if (__attr_disabled is _DEFAULT_MARKER):
                __attr_disabled = ''
            else:
                if __attr_disabled:
                    __attr_disabled = 'disabled'
                else:
                    __attr_disabled = None
            if (__attr_disabled is not None):
                __append((' disabled="%s"' % __attr_disabled))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485567808
            __default_4485567808 = _DEFAULT_MARKER

            # <Boolean 'view/multiple' (27:11)> -> __attr_multiple
            __token = 1303
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_multiple = _static_4417553984('path', 'view/multiple', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            if (__attr_multiple is _DEFAULT_MARKER):
                __attr_multiple = ''
            else:
                if __attr_multiple:
                    __attr_multiple = 'multiple'
                else:
                    __attr_multiple = None
            if (__attr_multiple is not None):
                __append((' multiple="%s"' % __attr_multiple))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485571216
            __default_4485571216 = _DEFAULT_MARKER

            # <Substitution 'view/size' (28:6)> -> __attr_size
            __token = 1346
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_size = _static_4417553984('path', 'view/size', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_size = __quote(__attr_size, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_size is not None):
                __append((' size="%s"' % __attr_size))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485570016
            __default_4485570016 = _DEFAULT_MARKER

            # <Substitution "python:view.required and 'required' or None" (7:31)> -> __attr_required
            __token = 313
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_required = _static_4417553984('python', "view.required and 'required' or None", econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_required = __quote(__attr_required, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_required is not None):
                __append((' required="%s"' % __attr_required))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485571360
            __default_4485571360 = _DEFAULT_MARKER

            # <Substitution 'view/style' (9:26)> -> __attr_style
            __token = 450
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_4417553984('path', 'view/style', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485571840
            __default_4485571840 = _DEFAULT_MARKER

            # <Substitution 'view/title' (10:25)> -> __attr_title
            __token = 491
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_4417553984('path', 'view/title', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485571600
            __default_4485571600 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (11:23)> -> __attr_lang
            __token = 531
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_4417553984('path', 'view/lang', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485573616
            __default_4485573616 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (12:25)> -> __attr_onclick
            __token = 573
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_4417553984('path', 'view/onclick', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485569248
            __default_4485569248 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (13:27)> -> __attr_ondblclick
            __token = 621
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_4417553984('path', 'view/ondblclick', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485564400
            __default_4485564400 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (14:27)> -> __attr_onmousedown
            __token = 673
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_4417553984('path', 'view/onmousedown', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485569440
            __default_4485569440 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (15:24)> -> __attr_onmouseup
            __token = 724
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_4417553984('path', 'view/onmouseup', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485578368
            __default_4485578368 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (16:25)> -> __attr_onmouseover
            __token = 775
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_4417553984('path', 'view/onmouseover', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485577024
            __default_4485577024 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (17:24)> -> __attr_onmousemove
            __token = 828
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_4417553984('path', 'view/onmousemove', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485566992
            __default_4485566992 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (18:22)> -> __attr_onmouseout
            __token = 880
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_4417553984('path', 'view/onmouseout', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485563056
            __default_4485563056 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (19:21)> -> __attr_onkeypress
            __token = 931
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_4417553984('path', 'view/onkeypress', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485578224
            __default_4485578224 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (20:19)> -> __attr_onkeydown
            __token = 981
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_4417553984('path', 'view/onkeydown', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485571120
            __default_4485571120 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (21:16)> -> __attr_onkeyup
            __token = 1028
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_4417553984('path', 'view/onkeyup', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485576016
            __default_4485576016 = _DEFAULT_MARKER

            # <Substitution 'view/onfocus' (24:13)> -> __attr_onfocus
            __token = 1167
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_4417553984('path', 'view/onfocus', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485576448
            __default_4485576448 = _DEFAULT_MARKER

            # <Substitution 'view/onblur' (25:11)> -> __attr_onblur
            __token = 1211
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_4417553984('path', 'view/onblur', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4485577696
            __default_4485577696 = _DEFAULT_MARKER

            # <Substitution 'view/onchange' (26:12)> -> __attr_onchange
            __token = 1256
            try:
                __zt_tmp = __attrs_4485576640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_4417553984('path', 'view/onchange', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((' onchange="%s"' % __attr_onchange))
            __append('>\n')

            # <Static value=<ast.Dict object at 0x1075a0f10> name=None at 1075a3f70> -> __attrs_4485578416
            __attrs_4485578416 = _static_4418309904
            __backup_item_4485744528 = get('item', __marker)

            # <Value 'view/items' (29:24)> -> __iterator
            __token = 1405
            try:
                __zt_tmp = __attrs_4485578416
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4417553984('path', 'view/items', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            (__iterator, ____index_4485566560, ) = getname('repeat')('item', __iterator)
            econtext['item'] = None
            for __item in __iterator:
                econtext['item'] = __item

                # <Static value=<ast.Dict object at 0x10b5c6890> name=None at 10b5c4a00> -> __attrs_4480104864
                __attrs_4480104864 = _static_4485572752

                # <Value 'item/selected' (31:24)> -> __condition
                __token = 1487
                try:
                    __zt_tmp = __attrs_4480104864
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4417553984('path', 'item/selected', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                if __condition:

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append('<option')

                    # <Symbol value=<DEFAULT> at 107619600> -> __default_4480105536
                    __default_4480105536 = _DEFAULT_MARKER

                    # <Substitution 'item/id' (32:28)> -> __attr_id
                    __token = 1530
                    try:
                        __zt_tmp = __attrs_4480104864
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_4417553984('path', 'item/id', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 107619600> -> __default_4480106400
                    __default_4480106400 = _DEFAULT_MARKER

                    # <Substitution 'item/value' (33:30)> -> __attr_value
                    __token = 1569
                    try:
                        __zt_tmp = __attrs_4480104864
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_4417553984('path', 'item/value', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' selected="selected">')

                    # <Symbol value=<DEFAULT> at 107619600> -> __default_4485566752
                    __default_4485566752 = _DEFAULT_MARKER

                    # <Value 'item/content' (34:22)> -> __cache_4485570976
                    __token = 1604
                    try:
                        __zt_tmp = __attrs_4480104864
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4485570976 = _static_4417553984('path', 'item/content', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))

                    # <BinOp left=<Value 'item/content' (34:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107619600> at 10b5c6830> -> __condition
                    __expression = __cache_4485570976

                    # <Symbol value=<DEFAULT> at 107619600> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('label')
                    else:
                        __content = __cache_4485570976
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</option\n   >')

                # <Static value=<ast.Dict object at 0x10b08f160> name=None at 10b08f130> -> __attrs_4480102128
                __attrs_4480102128 = _static_4480102752

                # <Value 'not:item/selected' (36:24)> -> __condition
                __token = 1682
                try:
                    __zt_tmp = __attrs_4480102128
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4417553984('not', 'item/selected', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                if __condition:

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append('<option')

                    # <Symbol value=<DEFAULT> at 107619600> -> __default_4480103184
                    __default_4480103184 = _DEFAULT_MARKER

                    # <Substitution 'item/id' (37:28)> -> __attr_id
                    __token = 1729
                    try:
                        __zt_tmp = __attrs_4480102128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_4417553984('path', 'item/id', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 107619600> -> __default_4480102656
                    __default_4480102656 = _DEFAULT_MARKER

                    # <Substitution 'item/value' (38:30)> -> __attr_value
                    __token = 1768
                    try:
                        __zt_tmp = __attrs_4480102128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_4417553984('path', 'item/value', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 107619600> -> __default_4480103808
                    __default_4480103808 = _DEFAULT_MARKER

                    # <Value 'item/content' (39:22)> -> __cache_4480104288
                    __token = 1803
                    try:
                        __zt_tmp = __attrs_4480102128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4480104288 = _static_4417553984('path', 'item/content', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))

                    # <BinOp left=<Value 'item/content' (39:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107619600> at 10b08f6a0> -> __condition
                    __expression = __cache_4480104288

                    # <Symbol value=<DEFAULT> at 107619600> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('label')
                    else:
                        __content = __cache_4480104288
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</option\n >')
                ____index_4485566560 -= 1
                if (____index_4485566560 > 0):
                    __append('')
            if (__backup_item_4485744528 is __marker):
                del econtext['item']
            else:
                econtext['item'] = __backup_item_4485744528
            __append('\n</select>\n')

            # <Static value=<ast.Dict object at 0x10b5c6800> name=None at 10b5c50c0> -> __attrs_4480100592
            __attrs_4480100592 = _static_4485572608

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input')

            # <Symbol value=<DEFAULT> at 107619600> -> __default_4480101312
            __default_4480101312 = _DEFAULT_MARKER

            # <Substitution 'string:${view/name}-empty-marker' (43:28)> -> __attr_name
            __token = 1940
            try:
                __zt_tmp = __attrs_4480100592
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_4417553984('string', '${view/name}-empty-marker', econtext=econtext)(_static_4417565216(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', 'field-empty-marker', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))
            __append(' type="hidden" value="1" />\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }