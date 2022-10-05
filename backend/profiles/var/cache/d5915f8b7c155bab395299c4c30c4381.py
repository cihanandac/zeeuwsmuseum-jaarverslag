# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/viewlets/document_byline.pt'

__tokens = {53: ('view/show', 2, 24), 154: ('here/creators', 6, 30), 206: (' context/@@plone_portal_state/navigation_root_ur', 7, 37), 306: ('python:creator_ids and view.show_about()', 9, 31), 427: ('creator_ids', 12, 29), 493: ('python: view.get_url_path(user_id)', 14, 27), 555: (' python:view.get_fullname(user_id', 15, 26), 761: ('url_path', 19, 26), 699: ('${navigation_root_url}/${url_path}', 18, 17), 701: ('navigation_root_url', 18, 19), 724: ('url_path', 18, 42), 780: ('${fullname}', 20, 9), 782: ('fullname', 20, 11), 900: ('not:url_path', 22, 29), 923: ('${fullname}', 23, 9), 925: ('fullname', 23, 11), 1031: ('view/pub_date', 29, 31), 1075: (' context/ModificationDat', 30, 29), 1144: ('e python:view.show_modification_date', 31, 42), 1234: ('published', 32, 49), 1327: ('python:context.toLocalizedTime(published)', 34, 23), 1406: ('show_modification_date', 34, 102), 1501: ('show_modification_date', 37, 48), 1627: ('python:context.toLocalizedTime(modified)', 41, 23), 1753: ('view/isExpired', 47, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4982492992 = {'class': 'state-expired', }
_static_4983931376 = {'class': 'documentModified', }
_static_4983937904 = {'class': 'documentPublished', }
_static_4771514400 = {'class': 'badge rounded-pill bg-light text-dark fw-normal fs-6', }
_static_4982399104 = {'class': 'badge rounded-pill bg-light text-dark fw-normal fs-6', 'href': '${navigation_root_url}/${url_path}', }
_static_4753720080 = {}
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4982403904 = {'id': 'section-byline', }

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

            # <Static value=<ast.Dict object at 0x128f97340> name=None at 128f97be0> -> __attrs_4982403232
            __attrs_4982403232 = _static_4982403904

            # <Value 'view/show' (2:24)> -> __condition
            __token = 53
            try:
                __zt_tmp = __attrs_4982403232
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4754050160('path', 'view/show', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4982400832 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-byline" >\n  ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982393872
                __attrs_4982393872 = _static_4753720080
                __backup_creator_ids_4760145488 = get('creator_ids', __marker)

                # <Value 'here/creators' (6:30)> -> __value
                __token = 154
                try:
                    __zt_tmp = __attrs_4982393872
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('path', 'here/creators', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['creator_ids'] = __value
                __backup_navigation_root_url_4760157248 = get('navigation_root_url', __marker)

                # <Value 'context/@@plone_portal_state/navigation_root_url' (7:37)> -> __value
                __token = 206
                try:
                    __zt_tmp = __attrs_4982393872
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('path', 'context/@@plone_portal_state/navigation_root_url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['navigation_root_url'] = __value

                # <Value 'python:creator_ids and view.show_about()' (9:31)> -> __condition
                __token = 306
                try:
                    __zt_tmp = __attrs_4982393872
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4754050160('python', 'creator_ids and view.show_about()', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                if __condition:
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982392576
                    __attrs_4982392576 = _static_4753720080
                    __stream_4982402416 = []
                    __append_4982402416 = __stream_4982402416.append
                    __append_4982402416('by')
                    __msgid_4982402416 = __re_whitespace(''.join(__stream_4982402416)).strip()
                    if __msgid_4982402416:
                        __append(translate(__msgid_4982402416, mapping=None, default=__msgid_4982402416, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982391520
                    __attrs_4982391520 = _static_4753720080
                    __backup_user_id_4760155232 = get('user_id', __marker)

                    # <Value 'creator_ids' (12:29)> -> __iterator
                    __token = 427
                    try:
                        __zt_tmp = __attrs_4982391520
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_4754050160('path', 'creator_ids', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    (__iterator, ____index_4982391952, ) = getname('repeat')('user_id', __iterator)
                    econtext['user_id'] = None
                    for __item in __iterator:
                        econtext['user_id'] = __item
                        __append('\n      ')

                        # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982404528
                        __attrs_4982404528 = _static_4753720080
                        __backup_url_path_4760157296 = get('url_path', __marker)

                        # <Value 'python: view.get_url_path(user_id)' (14:27)> -> __value
                        __token = 493
                        try:
                            __zt_tmp = __attrs_4982404528
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4754050160('python', ' view.get_url_path(user_id)', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                        econtext['url_path'] = __value
                        __backup_fullname_4760148224 = get('fullname', __marker)

                        # <Value 'python:view.get_fullname(user_id)' (15:26)> -> __value
                        __token = 555
                        try:
                            __zt_tmp = __attrs_4982404528
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4754050160('python', 'view.get_fullname(user_id)', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                        econtext['fullname'] = __value
                        __append('\n        ')

                        # <Static value=<ast.Dict object at 0x128f96080> name=None at 128f972e0> -> __attrs_4982401120
                        __attrs_4982401120 = _static_4982399104

                        # <Value 'url_path' (19:26)> -> __condition
                        __token = 761
                        try:
                            __zt_tmp = __attrs_4982401120
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4754050160('path', 'url_path', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                        if __condition:

                            # <a ... (0:0)
                            # --------------------------------------------------------
                            __append('<a class="badge rounded-pill bg-light text-dark fw-normal fs-6"')

                            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982391424
                            __default_4982391424 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${navigation_root_url}/${url_path}' (18:17)> braces_required=True translation=False default='"?"' default_marker='"?"' at 128f97cd0> -> __attr_href
                            __token = 699
                            __token = 701
                            try:
                                __zt_tmp = __attrs_4982401120
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href = _static_4754050160('path', 'navigation_root_url', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                            __token = 724
                            try:
                                __zt_tmp = __attrs_4982401120
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href_722 = _static_4754050160('path', 'url_path', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                            __attr_href_722 = __quote(__attr_href_722, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_href = ('%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/', (__attr_href_722 if (__attr_href_722 is not None) else ''), ))
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
                            __append(' >')

                            # <Interpolation value=<Substitution '${fullname}' (20:9)> braces_required=True translation=False default='"?"' default_marker='"?"' at 128f94af0> -> __content_4355604080
                            __token = 780
                            __token = 782
                            try:
                                __zt_tmp = __attrs_4982401120
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __content_4355604080 = _static_4754050160('path', 'fullname', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                            __content_4355604080 = __quote(__content_4355604080, '\x00', '&#0;', None, None)
                            __content_4355604080 = __content_4355604080
                            if (__content_4355604080 is None):
                                pass
                            else:
                                if (__content_4355604080 is None):
                                    __content_4355604080 = None
                                else:
                                    __tt = type(__content_4355604080)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __content_4355604080 = str(__content_4355604080)
                                    else:
                                        if (__tt is bytes):
                                            __content_4355604080 = decode(__content_4355604080)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __content_4355604080 = __content_4355604080.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__content_4355604080)
                                                    __content_4355604080 = (str(__content_4355604080) if (__content_4355604080 is __converted) else __converted)
                                                else:
                                                    __content_4355604080 = __content_4355604080()
                            if (__content_4355604080 is not None):
                                __append(__content_4355604080)
                            __append('</a>')
                        __append('\n        ')

                        # <Static value=<ast.Dict object at 0x11c678820> name=None at 11c678430> -> __attrs_4983939728
                        __attrs_4983939728 = _static_4771514400

                        # <Value 'not:url_path' (22:29)> -> __condition
                        __token = 900
                        try:
                            __zt_tmp = __attrs_4983939728
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4754050160('not', 'url_path', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span class="badge rounded-pill bg-light text-dark fw-normal fs-6" >')

                            # <Interpolation value=<Substitution '${fullname}' (23:9)> braces_required=True translation=False default='"?"' default_marker='"?"' at 12910ceb0> -> __content_4355604080
                            __token = 923
                            __token = 925
                            try:
                                __zt_tmp = __attrs_4983939728
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __content_4355604080 = _static_4754050160('path', 'fullname', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                            __content_4355604080 = __quote(__content_4355604080, '\x00', '&#0;', None, None)
                            __content_4355604080 = __content_4355604080
                            if (__content_4355604080 is None):
                                pass
                            else:
                                if (__content_4355604080 is None):
                                    __content_4355604080 = None
                                else:
                                    __tt = type(__content_4355604080)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __content_4355604080 = str(__content_4355604080)
                                    else:
                                        if (__tt is bytes):
                                            __content_4355604080 = decode(__content_4355604080)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __content_4355604080 = __content_4355604080.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__content_4355604080)
                                                    __content_4355604080 = (str(__content_4355604080) if (__content_4355604080 is __converted) else __converted)
                                                else:
                                                    __content_4355604080 = __content_4355604080()
                            if (__content_4355604080 is not None):
                                __append(__content_4355604080)
                            __append('</span>')
                        __append('\n      ')
                        if (__backup_fullname_4760148224 is __marker):
                            del econtext['fullname']
                        else:
                            econtext['fullname'] = __backup_fullname_4760148224
                        if (__backup_url_path_4760157296 is __marker):
                            del econtext['url_path']
                        else:
                            econtext['url_path'] = __backup_url_path_4760157296
                        __append('\n    ')
                        ____index_4982391952 -= 1
                        if (____index_4982391952 > 0):
                            __append('')
                    if (__backup_user_id_4760155232 is __marker):
                        del econtext['user_id']
                    else:
                        econtext['user_id'] = __backup_user_id_4760155232
                    __append('\n    —\n  ')
                if (__backup_navigation_root_url_4760157248 is __marker):
                    del econtext['navigation_root_url']
                else:
                    econtext['navigation_root_url'] = __backup_navigation_root_url_4760157248
                if (__backup_creator_ids_4760145488 is __marker):
                    del econtext['creator_ids']
                else:
                    econtext['creator_ids'] = __backup_creator_ids_4760145488
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982399440
                __attrs_4982399440 = _static_4753720080
                __backup_published_4760155424 = get('published', __marker)

                # <Value 'view/pub_date' (29:31)> -> __value
                __token = 1031
                try:
                    __zt_tmp = __attrs_4982399440
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('path', 'view/pub_date', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['published'] = __value
                __backup_modified_4760150240 = get('modified', __marker)

                # <Value 'context/ModificationDate' (30:29)> -> __value
                __token = 1075
                try:
                    __zt_tmp = __attrs_4982399440
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('path', 'context/ModificationDate', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['modified'] = __value
                __backup_show_modification_date_4760145056 = get('show_modification_date', __marker)

                # <Value 'python:view.show_modification_date()' (31:42)> -> __value
                __token = 1144
                try:
                    __zt_tmp = __attrs_4982399440
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4754050160('python', 'view.show_modification_date()', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                econtext['show_modification_date'] = __value
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x12910db70> name=None at 12910cac0> -> __attrs_4983941888
                __attrs_4983941888 = _static_4983937904

                # <Value 'published' (32:49)> -> __condition
                __token = 1234
                try:
                    __zt_tmp = __attrs_4983941888
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4754050160('path', 'published', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="documentPublished">\n    ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4983941840
                    __attrs_4983941840 = _static_4753720080

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_4983934064 = []
                    __append_4983934064 = __stream_4983934064.append
                    __append_4983934064('published')
                    __msgid_4983934064 = __re_whitespace(''.join(__stream_4983934064)).strip()
                    if 'box_published':
                        __append(translate('box_published', mapping=None, default=__msgid_4983934064, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n    ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4983942416
                    __attrs_4983942416 = _static_4753720080

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4983937952
                    __default_4983937952 = _DEFAULT_MARKER

                    # <Value 'python:context.toLocalizedTime(published)' (34:23)> -> __cache_4983945776
                    __token = 1327
                    try:
                        __zt_tmp = __attrs_4983942416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4983945776 = _static_4754050160('python', 'context.toLocalizedTime(published)', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'python:context.toLocalizedTime(published)' (34:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 12910d150> -> __condition
                    __expression = __cache_4983945776

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Published')
                    else:
                        __content = __cache_4983945776
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4983947168
                    __attrs_4983947168 = _static_4753720080

                    # <Value 'show_modification_date' (34:102)> -> __condition
                    __token = 1406
                    try:
                        __zt_tmp = __attrs_4983947168
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4754050160('path', 'show_modification_date', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                    if __condition:
                        __append(',')
                    __append('\n  </span>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x12910c1f0> name=None at 12910ea70> -> __attrs_4983943664
                __attrs_4983943664 = _static_4983931376

                # <Value 'show_modification_date' (37:48)> -> __condition
                __token = 1501
                try:
                    __zt_tmp = __attrs_4983943664
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4754050160('path', 'show_modification_date', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="documentModified">\n    ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4983941408
                    __attrs_4983941408 = _static_4753720080

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_4983938384 = []
                    __append_4983938384 = __stream_4983938384.append
                    __append_4983938384('\n      last modified\n    ')
                    __msgid_4983938384 = __re_whitespace(''.join(__stream_4983938384)).strip()
                    if 'box_last_modified':
                        __append(translate('box_last_modified', mapping=None, default=__msgid_4983938384, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n    ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4983940736
                    __attrs_4983940736 = _static_4753720080

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4983942272
                    __default_4983942272 = _DEFAULT_MARKER

                    # <Value 'python:context.toLocalizedTime(modified)' (41:23)> -> __cache_4983944384
                    __token = 1627
                    try:
                        __zt_tmp = __attrs_4983940736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4983944384 = _static_4754050160('python', 'context.toLocalizedTime(modified)', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'python:context.toLocalizedTime(modified)' (41:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 12910ed40> -> __condition
                    __expression = __cache_4983944384

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n      Modified\n    ')
                    else:
                        __content = __cache_4983944384
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n  </span>')
                __append('\n  ')
                if (__backup_show_modification_date_4760145056 is __marker):
                    del econtext['show_modification_date']
                else:
                    econtext['show_modification_date'] = __backup_show_modification_date_4760145056
                if (__backup_modified_4760150240 is __marker):
                    del econtext['modified']
                else:
                    econtext['modified'] = __backup_modified_4760150240
                if (__backup_published_4760155424 is __marker):
                    del econtext['published']
                else:
                    econtext['published'] = __backup_published_4760155424
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4983944480
                __attrs_4983944480 = _static_4753720080

                # <Value 'view/isExpired' (47:30)> -> __condition
                __token = 1753
                try:
                    __zt_tmp = __attrs_4983944480
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4754050160('path', 'view/isExpired', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                if __condition:
                    __append('\n    —\n    ')

                    # <Static value=<ast.Dict object at 0x128facf40> name=None at 128faefb0> -> __attrs_4982499520
                    __attrs_4982499520 = _static_4982492992

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="state-expired">')
                    __stream_4982495008 = []
                    __append_4982495008 = __stream_4982495008.append
                    __append_4982495008('expired')
                    __msgid_4982495008 = __re_whitespace(''.join(__stream_4982495008)).strip()
                    if 'time_expired':
                        __append(translate('time_expired', mapping=None, default=__msgid_4982495008, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n  ')
                __append('\n\n</section>')
                __i18n_domain = __previous_i18n_domain_4982400832
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }