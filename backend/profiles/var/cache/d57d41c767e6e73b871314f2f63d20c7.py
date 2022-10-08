# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/portlets/portlets/navigation.pt'

__tokens = {248: ('view/navigation_root', 7, 23), 357: ("python:view.hasName() and 'card-header' or 'card-header hiddenStructure'", 11, 30), 504: ('string:${view/heading_link_target}', 14, 31), 563: ('view/title', 15, 23), 737: ('view/root_item_class', 21, 38), 791: (" python:selectedClass and ' navTreeCurrentNode' or '", 22, 32), 884: ('g nocall:context/plone_utils/normalizeStri', 23, 38), 965: ('le root/Ti', 24, 35), 1008: ('ion python:normalizeString(section_ti', 25, 28), 1079: ('view/include_top', 26, 27), 1131: ('string:navTreeItem navTreeTopNode${li_class} nav-section-${section}', 27, 34), 1260: ('view/root_is_portal', 29, 31), 1308: (' root/portal_typ', 30, 27), 1359: ("s python:'contenttype-' + normalizeString(root_typ", 31, 32), 1439: ("ss python:rootIsPortal and 'contenttype-plone-site' or root_type_cl", 32, 26), 1564: ('root/absolute_url', 34, 36), 1618: (' root/Descriptio', 35, 35), 1671: ("s python:' '.join([root_class, selectedClass]).strip", 36, 34), 1798: ('rootIsPortal', 38, 33), 1904: ('not:rootIsPortal', 40, 35), 1953: ('root/Title', 41, 31), 2071: ('view/createNavTree', 45, 35)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4496196704 = {'href': 'root/absolute_url', 'title': 'root/Description', 'class': "python:' '.join([root_class, selectedClass]).strip()", }
_static_4438430896 = {}
_static_4496204576 = {'class': 'string:navTreeItem navTreeTopNode${li_class} nav-section-${section}', }
_static_4496201168 = {'class': 'navTree navTreeLevel0', }
_static_4496197760 = {'class': 'card-body', }
_static_4496199584 = {'href': '#', 'class': 'tile', }
_static_4496555552 = {'class': 'card-header', }
_static_4438741184 = __C2ZContextWrapper
_static_4438540496 = __compile_zt_expr
_static_4496518704 = {'class': 'card portlet portletNavigationTree', }
_static_4496377552 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x10c0146d0> name=None at 10c016770> -> __attrs_4496045104
            __attrs_4496045104 = _static_4496377552
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x10c036e30> name=None at 10c034820> -> __attrs_4496513904
            __attrs_4496513904 = _static_4496518704
            __backup_root_4495719056 = get('root', __marker)

            # <Value 'view/navigation_root' (7:23)> -> __value
            __token = 248
            try:
                __zt_tmp = __attrs_4496513904
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('path', 'view/navigation_root', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['root'] = __value
            __previous_i18n_domain_4496542448 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card portlet portletNavigationTree">\n\n    ')

            # <Static value=<ast.Dict object at 0x10c03fe20> name=None at 10c03ffa0> -> __attrs_4496196752
            __attrs_4496196752 = _static_4496555552

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div')

            # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4496203280
            __default_4496203280 = _DEFAULT_MARKER

            # <Substitution "python:view.hasName() and 'card-header' or 'card-header hiddenStructure'" (11:30)> -> __attr_class
            __token = 357
            try:
                __zt_tmp = __attrs_4496196752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4438540496('python', "view.hasName() and 'card-header' or 'card-header hiddenStructure'", econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', 'card-header', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))
            __append('>\n      ')

            # <Static value=<ast.Dict object at 0x10bfe8fa0> name=None at 10bfe8af0> -> __attrs_4496199200
            __attrs_4496199200 = _static_4496199584

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4496200160
            __default_4496200160 = _DEFAULT_MARKER

            # <Substitution 'string:${view/heading_link_target}' (14:31)> -> __attr_href
            __token = 504
            try:
                __zt_tmp = __attrs_4496199200
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4438540496('string', '${view/heading_link_target}', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' class="tile">')

            # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4496199440
            __default_4496199440 = _DEFAULT_MARKER

            # <Value 'view/title' (15:23)> -> __cache_4496200784
            __token = 563
            try:
                __zt_tmp = __attrs_4496199200
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4496200784 = _static_4438540496('path', 'view/title', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/title' (15:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088d2740> at 10bfe8f40> -> __condition
            __expression = __cache_4496200784

            # <Symbol value=<DEFAULT> at 1088d2740> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('Navigation')
            else:
                __content = __cache_4496200784
                __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</a>\n    </div>\n\n    ')

            # <Static value=<ast.Dict object at 0x10bfe8880> name=None at 10bfe8820> -> __attrs_4496201264
            __attrs_4496201264 = _static_4496197760

            # <nav ... (0:0)
            # --------------------------------------------------------
            __append('<nav class="card-body">\n      ')

            # <Static value=<ast.Dict object at 0x10bfe95d0> name=None at 10bfe8580> -> __attrs_4496202704
            __attrs_4496202704 = _static_4496201168

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append('<ul class="navTree navTreeLevel0">\n        ')

            # <Static value=<ast.Dict object at 0x10bfea320> name=None at 10bfea2f0> -> __attrs_4496206352
            __attrs_4496206352 = _static_4496204576
            __backup_selectedClass_4495714544 = get('selectedClass', __marker)

            # <Value 'view/root_item_class' (21:38)> -> __value
            __token = 737
            try:
                __zt_tmp = __attrs_4496206352
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('path', 'view/root_item_class', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['selectedClass'] = __value
            __backup_li_class_4496555216 = get('li_class', __marker)

            # <Value "python:selectedClass and ' navTreeCurrentNode' or ''" (22:32)> -> __value
            __token = 791
            try:
                __zt_tmp = __attrs_4496206352
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('python', "selectedClass and ' navTreeCurrentNode' or ''", econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['li_class'] = __value
            __backup_normalizeString_4496198864 = get('normalizeString', __marker)

            # <Value 'nocall:context/plone_utils/normalizeString' (23:38)> -> __value
            __token = 884
            try:
                __zt_tmp = __attrs_4496206352
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('nocall', 'context/plone_utils/normalizeString', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['normalizeString'] = __value
            __backup_section_title_4496205632 = get('section_title', __marker)

            # <Value 'root/Title' (24:35)> -> __value
            __token = 965
            try:
                __zt_tmp = __attrs_4496206352
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('path', 'root/Title', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['section_title'] = __value
            __backup_section_4496205536 = get('section', __marker)

            # <Value 'python:normalizeString(section_title)' (25:28)> -> __value
            __token = 1008
            try:
                __zt_tmp = __attrs_4496206352
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4438540496('python', 'normalizeString(section_title)', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            econtext['section'] = __value

            # <Value 'view/include_top' (26:27)> -> __condition
            __token = 1079
            try:
                __zt_tmp = __attrs_4496206352
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4438540496('path', 'view/include_top', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
            if __condition:

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li')

                # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4496204672
                __default_4496204672 = _DEFAULT_MARKER

                # <Substitution 'string:navTreeItem navTreeTopNode${li_class} nav-section-${section}' (27:34)> -> __attr_class
                __token = 1131
                try:
                    __zt_tmp = __attrs_4496206352
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_4438540496('string', 'navTreeItem navTreeTopNode${li_class} nav-section-${section}', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append('>\n          ')

                # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4496209472
                __attrs_4496209472 = _static_4438430896
                __backup_rootIsPortal_4496205200 = get('rootIsPortal', __marker)

                # <Value 'view/root_is_portal' (29:31)> -> __value
                __token = 1260
                try:
                    __zt_tmp = __attrs_4496209472
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4438540496('path', 'view/root_is_portal', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                econtext['rootIsPortal'] = __value
                __backup_root_type_4496206496 = get('root_type', __marker)

                # <Value 'root/portal_type' (30:27)> -> __value
                __token = 1308
                try:
                    __zt_tmp = __attrs_4496209472
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4438540496('path', 'root/portal_type', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                econtext['root_type'] = __value
                __backup_root_type_class_4496208464 = get('root_type_class', __marker)

                # <Value "python:'contenttype-' + normalizeString(root_type)" (31:32)> -> __value
                __token = 1359
                try:
                    __zt_tmp = __attrs_4496209472
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4438540496('python', "'contenttype-' + normalizeString(root_type)", econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                econtext['root_type_class'] = __value
                __backup_root_class_4496206784 = get('root_class', __marker)

                # <Value "python:rootIsPortal and 'contenttype-plone-site' or root_type_class" (32:26)> -> __value
                __token = 1439
                try:
                    __zt_tmp = __attrs_4496209472
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4438540496('python', "rootIsPortal and 'contenttype-plone-site' or root_type_class", econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                econtext['root_class'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n            ')

                # <Static value=<ast.Dict object at 0x10bfe8460> name=None at 10bfe9e40> -> __attrs_4496207696
                __attrs_4496207696 = _static_4496196704

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4496208896
                __default_4496208896 = _DEFAULT_MARKER

                # <Substitution 'root/absolute_url' (34:36)> -> __attr_href
                __token = 1564
                try:
                    __zt_tmp = __attrs_4496207696
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4438540496('path', 'root/absolute_url', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))

                # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4496201936
                __default_4496201936 = _DEFAULT_MARKER

                # <Substitution 'root/Description' (35:35)> -> __attr_title
                __token = 1618
                try:
                    __zt_tmp = __attrs_4496207696
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_title = _static_4438540496('path', 'root/Description', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_title is not None):
                    __append((' title="%s"' % __attr_title))

                # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4496207744
                __default_4496207744 = _DEFAULT_MARKER

                # <Substitution "python:' '.join([root_class, selectedClass]).strip()" (36:34)> -> __attr_class
                __token = 1671
                try:
                    __zt_tmp = __attrs_4496207696
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_4438540496('python', "' '.join([root_class, selectedClass]).strip()", econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append('>\n              ')

                # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4496196512
                __attrs_4496196512 = _static_4438430896

                # <Value 'rootIsPortal' (38:33)> -> __condition
                __token = 1798
                try:
                    __zt_tmp = __attrs_4496196512
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4438540496('path', 'rootIsPortal', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                if __condition:
                    __stream_4496207360 = []
                    __append_4496207360 = __stream_4496207360.append
                    __append_4496207360('Home')
                    __msgid_4496207360 = __re_whitespace(''.join(__stream_4496207360)).strip()
                    if 'tabs_home':
                        __append(translate('tabs_home', mapping=None, default=__msgid_4496207360, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n              ')

                # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4496203376
                __attrs_4496203376 = _static_4438430896

                # <Value 'not:rootIsPortal' (40:35)> -> __condition
                __token = 1904
                try:
                    __zt_tmp = __attrs_4496203376
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4438540496('not', 'rootIsPortal', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))
                if __condition:

                    # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4496211296
                    __default_4496211296 = _DEFAULT_MARKER

                    # <Value 'root/Title' (41:31)> -> __cache_4496208656
                    __token = 1953
                    try:
                        __zt_tmp = __attrs_4496203376
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4496208656 = _static_4438540496('path', 'root/Title', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))

                    # <BinOp left=<Value 'root/Title' (41:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088d2740> at 10bfebe20> -> __condition
                    __expression = __cache_4496208656

                    # <Symbol value=<DEFAULT> at 1088d2740> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>Root item title</span>')
                    else:
                        __content = __cache_4496208656
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                __append('\n            </a>\n          </div>')
                if (__backup_root_class_4496206784 is __marker):
                    del econtext['root_class']
                else:
                    econtext['root_class'] = __backup_root_class_4496206784
                if (__backup_root_type_class_4496208464 is __marker):
                    del econtext['root_type_class']
                else:
                    econtext['root_type_class'] = __backup_root_type_class_4496208464
                if (__backup_root_type_4496206496 is __marker):
                    del econtext['root_type']
                else:
                    econtext['root_type'] = __backup_root_type_4496206496
                if (__backup_rootIsPortal_4496205200 is __marker):
                    del econtext['rootIsPortal']
                else:
                    econtext['rootIsPortal'] = __backup_rootIsPortal_4496205200
                __append('\n        </li>')
            if (__backup_section_4496205536 is __marker):
                del econtext['section']
            else:
                econtext['section'] = __backup_section_4496205536
            if (__backup_section_title_4496205632 is __marker):
                del econtext['section_title']
            else:
                econtext['section_title'] = __backup_section_title_4496205632
            if (__backup_normalizeString_4496198864 is __marker):
                del econtext['normalizeString']
            else:
                econtext['normalizeString'] = __backup_normalizeString_4496198864
            if (__backup_li_class_4496555216 is __marker):
                del econtext['li_class']
            else:
                econtext['li_class'] = __backup_li_class_4496555216
            if (__backup_selectedClass_4495714544 is __marker):
                del econtext['selectedClass']
            else:
                econtext['selectedClass'] = __backup_selectedClass_4495714544
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x1088d14b0> name=None at 1088d2cb0> -> __attrs_4496237632
            __attrs_4496237632 = _static_4438430896

            # <Symbol value=<DEFAULT> at 1088d2740> -> __default_4496242192
            __default_4496242192 = _DEFAULT_MARKER

            # <Value 'view/createNavTree' (45:35)> -> __cache_4496239744
            __token = 2071
            try:
                __zt_tmp = __attrs_4496237632
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4496239744 = _static_4438540496('path', 'view/createNavTree', econtext=econtext)(_static_4438741184(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/createNavTree' (45:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088d2740> at 10bff3f10> -> __condition
            __expression = __cache_4496239744

            # <Symbol value=<DEFAULT> at 1088d2740> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li>\n            SUBTREE\n        </li>')
            else:
                __content = __cache_4496239744
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n      </ul>\n    </nav>\n\n  </div>')
            __i18n_domain = __previous_i18n_domain_4496542448
            if (__backup_root_4495719056 is __marker):
                del econtext['root']
            else:
                econtext['root'] = __backup_root_4495719056
            __append('\n\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }