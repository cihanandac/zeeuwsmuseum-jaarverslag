# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/Products/CMFPlone/controlpanel/browser/prefsmaintemplate.pt'

__tokens = {256: ("python:request.set('disable_border',1)", 6, 43), 345: (" python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel'", 7, 49), 485: ("e python:request.set('disable_plone.leftcolumn', ", 8, 54), 591: ("wo python:request.set('disable_plone.rightcolumn'", 9, 53), 1074: ("python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')", 21, 46), 1198: (" python:controlPanel.getGroups('site'", 22, 39), 1278: ('l controlPanel/site_u', 23, 40), 1345: ('rl request/', 24, 42), 1496: ('string:$portal_url/@@overview-controlpanel', 27, 49), 1573: ("nav-link ${python:'active' if overview_url in current_url else ''}", 28, 32), 1584: ("python:'active' if overview_url in current_url else ''", 28, 43), 1667: ('${overview_url}', 28, 126), 1669: ('overview_url', 28, 128), 1792: ('groups', 30, 49), 1850: ("python:controlPanel.enumConfiglets(group=group['id'])", 31, 49), 1949: (" python:'active' if bool([c for c in configlets if current_url.startswith(c['url'])]) else 'inactive", 32, 44), 2093: ('python:configlets and controlPanel.maySeeSomeConfiglets', 33, 41), 2237: ('nav-link dropdown-toggle ${active}', 35, 34), 2264: ('active', 35, 61), 2344: ('${group/title}', 35, 141), 2346: ('group/title', 35, 143), 2474: ('configlets', 37, 58), 2534: ('configlet/visible', 38, 47), 2608: ("python:'http' in configlet['icon']", 39, 54), 2738: ('${configlet/url}', 41, 39), 2740: ('configlet/url', 41, 41), 2809: ('icon_url', 42, 52), 2938: ('configlet/icon', 44, 56), 3009: (' configlet/titl', 45, 55), 3143: ('not: icon_url', 47, 57), 3223: ("python:icons.tag(configlet['icon'] or 'plone-controlpanel', tag_alt=configlet['title'])", 48, 65), 3347: ('${configlet/title}', 49, 32), 3349: ('configlet/title', 49, 34), 3694: ('nothing', 59, 82), 898: ('context/@@main_template/macros/content', 17, 42), 898: ('context/@@main_template/macros/content', 17, 42), 85: ('context/@@main_template/macros/master', 2, 30), 85: ('context/@@main_template/macros/master', 2, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque

_static_4501879344 = {'src': '', 'alt': '', 'class': 'icon', }
_static_4501901264 = {'class': 'dropdown-item', 'href': '${configlet/url}', }
_static_4501903328 = {'class': 'dropdown-menu', }
_static_4501902608 = {'class': 'nav-link dropdown-toggle ${active}', 'data-bs-toggle': 'dropdown', 'href': '#', 'role': 'button', 'aria-expanded': 'false', }
_static_4501907888 = {'class': 'nav-item dropdown', }
_static_4501910672 = {'class': "nav-link ${python:'active' if overview_url in current_url else ''}", 'aria-current': 'page', 'href': '${overview_url}', }
_static_4501912784 = {'class': 'nav-item', }
_static_4501816992 = {'class': 'nav nav-tabs', }
_static_4501824768 = {'class': 'mb-3', }
_static_4501815888 = 'content'
_static_4443607136 = __C2ZContextWrapper
_static_4443408704 = __compile_zt_expr
_static_4501830192 = 'master'
_static_4443296608 = {}

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

    def render_master(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_prefs_configlet_wrapper = econtext['__slot_prefs_configlet_wrapper'].pop()
        except:
            __slot_prefs_configlet_wrapper = None

        try:
            __slot_prefs_configlet_content = econtext['__slot_prefs_configlet_content'].pop()
        except:
            __slot_prefs_configlet_content = None

        try:
            __slot_prefs_configlet_main = econtext['__slot_prefs_configlet_main'].pop()
        except:
            __slot_prefs_configlet_main = None

        try:
            __slot_top_slot = econtext['__slot_top_slot'].pop()
        except:
            __slot_top_slot = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501829520
            __attrs_4501829520 = _static_4443296608
            __previous_i18n_domain_4501829376 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501823760
            __attrs_4501823760 = _static_4443296608
            __backup_macroname_4492526080 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x10c547a30> name=None at 10c545f90> -> __value
            __value = _static_4501830192
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501822368
                __attrs_4501822368 = _static_4443296608
                __append('\n        ')
                if (__slot_top_slot is None):

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501820592
                    __attrs_4501820592 = _static_4443296608
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501821696
                    __attrs_4501821696 = _static_4443296608
                    __backup_dummy_4497927152 = get('dummy', __marker)

                    # <Value "python:request.set('disable_border',1)" (6:43)> -> __value
                    __token = 256
                    try:
                        __zt_tmp = __attrs_4501821696
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4443408704('python', "request.set('disable_border',1)", econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                    econtext['dummy'] = __value
                    __backup_controlPanel_4497889632 = get('controlPanel', __marker)

                    # <Value "python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')" (7:49)> -> __value
                    __token = 345
                    try:
                        __zt_tmp = __attrs_4501821696
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4443408704('python', "modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')", econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                    econtext['controlPanel'] = __value
                    __backup_disable_column_one_4490644016 = get('disable_column_one', __marker)

                    # <Value "python:request.set('disable_plone.leftcolumn', 1)" (8:54)> -> __value
                    __token = 485
                    try:
                        __zt_tmp = __attrs_4501821696
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4443408704('python', "request.set('disable_plone.leftcolumn', 1)", econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                    econtext['disable_column_one'] = __value
                    __backup_disable_column_two_4497930128 = get('disable_column_two', __marker)

                    # <Value "python:request.set('disable_plone.rightcolumn',1)" (9:53)> -> __value
                    __token = 591
                    try:
                        __zt_tmp = __attrs_4501821696
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4443408704('python', "request.set('disable_plone.rightcolumn',1)", econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                    econtext['disable_column_two'] = __value
                    if (__backup_disable_column_two_4497930128 is __marker):
                        del econtext['disable_column_two']
                    else:
                        econtext['disable_column_two'] = __backup_disable_column_two_4497930128
                    if (__backup_disable_column_one_4490644016 is __marker):
                        del econtext['disable_column_one']
                    else:
                        econtext['disable_column_one'] = __backup_disable_column_one_4490644016
                    if (__backup_controlPanel_4497889632 is __marker):
                        del econtext['controlPanel']
                    else:
                        econtext['controlPanel'] = __backup_controlPanel_4497889632
                    if (__backup_dummy_4497927152 is __marker):
                        del econtext['dummy']
                    else:
                        econtext['dummy'] = __backup_dummy_4497927152
                    __append('\n        ')
                else:
                    __slot_top_slot(__stream, econtext.copy(), rcontext)
                __append('\n    ')
            _slots = econtext['__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_content(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501825872
                __attrs_4501825872 = _static_4443296608
                __append('\n        ')
                if (__slot_prefs_configlet_wrapper is None):

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501818000
                    __attrs_4501818000 = _static_4443296608
                    __append('\n          ')
                    if (__slot_prefs_configlet_content is None):

                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501819776
                        __attrs_4501819776 = _static_4443296608
                        __append('\n\n            ')

                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501817232
                        __attrs_4501817232 = _static_4443296608
                        __backup_macroname_4491510848 = get('macroname', __marker)

                        # <Static value=<ast.Constant object at 0x10c544250> name=None at 10c544280> -> __value
                        __value = _static_4501815888
                        econtext['macroname'] = __value

                        def __fill_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                            getname = econtext.get_name
                            get = econtext.get

                            # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501830384
                            __attrs_4501830384 = _static_4443296608
                            __append('\n\n                ')

                            # <Static value=<ast.Dict object at 0x10c546500> name=None at 10c546530> -> __attrs_4501825152
                            __attrs_4501825152 = _static_4501824768
                            __backup_controlPanel_4494959536 = get('controlPanel', __marker)

                            # <Value "python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')" (21:46)> -> __value
                            __token = 1074
                            try:
                                __zt_tmp = __attrs_4501825152
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4443408704('python', "modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')", econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                            econtext['controlPanel'] = __value
                            __backup_groups_4497904000 = get('groups', __marker)

                            # <Value "python:controlPanel.getGroups('site')" (22:39)> -> __value
                            __token = 1198
                            try:
                                __zt_tmp = __attrs_4501825152
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4443408704('python', "controlPanel.getGroups('site')", econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                            econtext['groups'] = __value
                            __backup_site_url_4494745824 = get('site_url', __marker)

                            # <Value 'controlPanel/site_url' (23:40)> -> __value
                            __token = 1278
                            try:
                                __zt_tmp = __attrs_4501825152
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4443408704('path', 'controlPanel/site_url', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                            econtext['site_url'] = __value
                            __backup_current_url_4494961168 = get('current_url', __marker)

                            # <Value 'request/URL' (24:42)> -> __value
                            __token = 1345
                            try:
                                __zt_tmp = __attrs_4501825152
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4443408704('path', 'request/URL', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                            econtext['current_url'] = __value

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="mb-3">\n                  ')

                            # <Static value=<ast.Dict object at 0x10c5446a0> name=None at 10c546aa0> -> __attrs_4501824096
                            __attrs_4501824096 = _static_4501816992

                            # <ul ... (0:0)
                            # --------------------------------------------------------
                            __append('<ul class="nav nav-tabs">\n                    ')

                            # <Static value=<ast.Dict object at 0x10c55bcd0> name=None at 10c55bca0> -> __attrs_4501912400
                            __attrs_4501912400 = _static_4501912784
                            __backup_overview_url_4497926768 = get('overview_url', __marker)

                            # <Value 'string:$portal_url/@@overview-controlpanel' (27:49)> -> __value
                            __token = 1496
                            try:
                                __zt_tmp = __attrs_4501912400
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4443408704('string', '$portal_url/@@overview-controlpanel', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                            econtext['overview_url'] = __value

                            # <li ... (0:0)
                            # --------------------------------------------------------
                            __append('<li class="nav-item">\n                      ')

                            # <Static value=<ast.Dict object at 0x10c55b490> name=None at 10c55b460> -> __attrs_4501909664
                            __attrs_4501909664 = _static_4501910672

                            # <a ... (0:0)
                            # --------------------------------------------------------
                            __append('<a')

                            # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4501911248
                            __default_4501911248 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution "nav-link ${python:'active' if overview_url in current_url else ''}" (28:32)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10c55b430> -> __attr_class
                            __token = 1573
                            __token = 1584
                            try:
                                __zt_tmp = __attrs_4501909664
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_4443408704('python', "'active' if overview_url in current_url else ''", econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_class = ('%s%s' % ('nav-link ', (__attr_class if (__attr_class is not None) else ''), ))
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
                            __append(' aria-current="page"')

                            # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4501910192
                            __default_4501910192 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${overview_url}' (28:126)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10c55b340> -> __attr_href
                            __token = 1667
                            __token = 1669
                            try:
                                __zt_tmp = __attrs_4501909664
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href = _static_4443408704('path', 'overview_url', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_href = __attr_href
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
                            __stream_4501911584 = []
                            __append_4501911584 = __stream_4501911584.append
                            __append_4501911584('Site Setup')
                            __msgid_4501911584 = __re_whitespace(''.join(__stream_4501911584)).strip()
                            if __msgid_4501911584:
                                __append(translate(__msgid_4501911584, mapping=None, default=__msgid_4501911584, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</a>\n                    </li>')
                            if (__backup_overview_url_4497926768 is __marker):
                                del econtext['overview_url']
                            else:
                                econtext['overview_url'] = __backup_overview_url_4497926768
                            __append('\n                    ')

                            # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501908992
                            __attrs_4501908992 = _static_4443296608
                            __backup_group_4497904912 = get('group', __marker)

                            # <Value 'groups' (30:49)> -> __iterator
                            __token = 1792
                            try:
                                __zt_tmp = __attrs_4501908992
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __iterator = _static_4443408704('path', 'groups', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                            (__iterator, ____index_4501908752, ) = getname('repeat')('group', __iterator)
                            econtext['group'] = None
                            for __item in __iterator:
                                econtext['group'] = __item
                                __append('\n                      ')

                                # <Static value=<ast.Dict object at 0x10c55a9b0> name=None at 10c55a980> -> __attrs_4501907456
                                __attrs_4501907456 = _static_4501907888
                                __backup_configlets_4490668128 = get('configlets', __marker)

                                # <Value "python:controlPanel.enumConfiglets(group=group['id'])" (31:49)> -> __value
                                __token = 1850
                                try:
                                    __zt_tmp = __attrs_4501907456
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __value = _static_4443408704('python', "controlPanel.enumConfiglets(group=group['id'])", econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                econtext['configlets'] = __value
                                __backup_active_4497827456 = get('active', __marker)

                                # <Value "python:'active' if bool([c for c in configlets if current_url.startswith(c['url'])]) else 'inactive'" (32:44)> -> __value
                                __token = 1949
                                try:
                                    __zt_tmp = __attrs_4501907456
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __value = _static_4443408704('python', "'active' if bool([c for c in configlets if current_url.startswith(c['url'])]) else 'inactive'", econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                econtext['active'] = __value

                                # <Value 'python:configlets and controlPanel.maySeeSomeConfiglets' (33:41)> -> __condition
                                __token = 2093
                                try:
                                    __zt_tmp = __attrs_4501907456
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_4443408704('python', 'configlets and controlPanel.maySeeSomeConfiglets', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                if __condition:

                                    # <li ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<li class="nav-item dropdown">\n                        ')

                                    # <Static value=<ast.Dict object at 0x10c559510> name=None at 10c559a50> -> __attrs_4501902224
                                    __attrs_4501902224 = _static_4501902608

                                    # <a ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<a')

                                    # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4501904000
                                    __default_4501904000 = _DEFAULT_MARKER

                                    # <Interpolation value=<Substitution 'nav-link dropdown-toggle ${active}' (35:34)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10c559ff0> -> __attr_class
                                    __token = 2237
                                    __token = 2264
                                    try:
                                        __zt_tmp = __attrs_4501902224
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_class = _static_4443408704('path', 'active', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                    __attr_class = ('%s%s' % ('nav-link dropdown-toggle ', (__attr_class if (__attr_class is not None) else ''), ))
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
                                    __append(' data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">')

                                    # <Interpolation value=<Substitution '${group/title}' (35:141)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10c5596f0> -> __content_4344921712
                                    __token = 2344
                                    __token = 2346
                                    try:
                                        __zt_tmp = __attrs_4501902224
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __content_4344921712 = _static_4443408704('path', 'group/title', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                    __content_4344921712 = __quote(__content_4344921712, '\x00', '&#0;', None, None)
                                    __content_4344921712 = __content_4344921712
                                    if (__content_4344921712 is None):
                                        pass
                                    else:
                                        if (__content_4344921712 is None):
                                            __content_4344921712 = None
                                        else:
                                            __tt = type(__content_4344921712)
                                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                                __content_4344921712 = str(__content_4344921712)
                                            else:
                                                if (__tt is bytes):
                                                    __content_4344921712 = decode(__content_4344921712)
                                                else:
                                                    if (__tt is not str):
                                                        try:
                                                            __content_4344921712 = __content_4344921712.__html__
                                                        except get('AttributeError', AttributeError):
                                                            __converted = convert(__content_4344921712)
                                                            __content_4344921712 = (str(__content_4344921712) if (__content_4344921712 is __converted) else __converted)
                                                        else:
                                                            __content_4344921712 = __content_4344921712()
                                    if (__content_4344921712 is not None):
                                        __append(__content_4344921712)
                                    __append('</a>\n                          ')

                                    # <Static value=<ast.Dict object at 0x10c5597e0> name=None at 10c5595d0> -> __attrs_4501897712
                                    __attrs_4501897712 = _static_4501903328

                                    # <ul ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<ul class="dropdown-menu">\n                          ')

                                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501898336
                                    __attrs_4501898336 = _static_4443296608
                                    __backup_configlet_4440297184 = get('configlet', __marker)

                                    # <Value 'configlets' (37:58)> -> __iterator
                                    __token = 2474
                                    try:
                                        __zt_tmp = __attrs_4501898336
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __iterator = _static_4443408704('path', 'configlets', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                    (__iterator, ____index_4501897376, ) = getname('repeat')('configlet', __iterator)
                                    econtext['configlet'] = None
                                    for __item in __iterator:
                                        econtext['configlet'] = __item
                                        __append('\n                            ')

                                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501898144
                                        __attrs_4501898144 = _static_4443296608

                                        # <Value 'configlet/visible' (38:47)> -> __condition
                                        __token = 2534
                                        try:
                                            __zt_tmp = __attrs_4501898144
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __condition = _static_4443408704('path', 'configlet/visible', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                        if __condition:

                                            # <li ... (0:0)
                                            # --------------------------------------------------------
                                            __append('<li>\n                              ')

                                            # <Static value=<ast.Dict object at 0x10c558fd0> name=None at 10c559060> -> __attrs_4501900880
                                            __attrs_4501900880 = _static_4501901264
                                            __backup_icon_url_4494474736 = get('icon_url', __marker)

                                            # <Value "python:'http' in configlet['icon']" (39:54)> -> __value
                                            __token = 2608
                                            try:
                                                __zt_tmp = __attrs_4501900880
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __value = _static_4443408704('python', "'http' in configlet['icon']", econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                            econtext['icon_url'] = __value

                                            # <a ... (0:0)
                                            # --------------------------------------------------------
                                            __append('<a class="dropdown-item"')

                                            # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4501900688
                                            __default_4501900688 = _DEFAULT_MARKER

                                            # <Interpolation value=<Substitution '${configlet/url}' (41:39)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10c558d30> -> __attr_href
                                            __token = 2738
                                            __token = 2740
                                            try:
                                                __zt_tmp = __attrs_4501900880
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __attr_href = _static_4443408704('path', 'configlet/url', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                                            __attr_href = __attr_href
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
                                            __append('>\n                                ')

                                            # <Static value=<ast.Dict object at 0x10c553a30> name=None at 10c551930> -> __attrs_4501879488
                                            __attrs_4501879488 = _static_4501879344

                                            # <Value 'icon_url' (42:52)> -> __condition
                                            __token = 2809
                                            try:
                                                __zt_tmp = __attrs_4501879488
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __condition = _static_4443408704('path', 'icon_url', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                            if __condition:

                                                # <img ... (0:0)
                                                # --------------------------------------------------------
                                                __append('<img')

                                                # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4501878672
                                                __default_4501878672 = _DEFAULT_MARKER

                                                # <Substitution 'configlet/icon' (44:56)> -> __attr_src
                                                __token = 2938
                                                try:
                                                    __zt_tmp = __attrs_4501879488
                                                except get('NameError', NameError):
                                                    __zt_tmp = None

                                                __attr_src = _static_4443408704('path', 'configlet/icon', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                                __attr_src = __quote(__attr_src, '"', '&quot;', '', _DEFAULT_MARKER)
                                                if (__attr_src is not None):
                                                    __append((' src="%s"' % __attr_src))

                                                # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4501879392
                                                __default_4501879392 = _DEFAULT_MARKER

                                                # <Translate msgid=None node=<Substitution 'configlet/title' (45:55)> at 10c552aa0> -> __attr_alt

                                                # <Substitution 'configlet/title' (45:55)> -> __attr_alt
                                                __token = 3009
                                                try:
                                                    __zt_tmp = __attrs_4501879488
                                                except get('NameError', NameError):
                                                    __zt_tmp = None

                                                __attr_alt = _static_4443408704('path', 'configlet/title', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                                __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                                                __attr_alt = translate(__attr_alt, default=__attr_alt, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                                if (__attr_alt is not None):
                                                    __append((' alt="%s"' % __attr_alt))
                                                __append(' class="icon">')
                                            __append('\n                                ')

                                            # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501878240
                                            __attrs_4501878240 = _static_4443296608

                                            # <Value 'not: icon_url' (47:57)> -> __condition
                                            __token = 3143
                                            try:
                                                __zt_tmp = __attrs_4501878240
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __condition = _static_4443408704('not', ' icon_url', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                            if __condition:

                                                # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4501879920
                                                __default_4501879920 = _DEFAULT_MARKER

                                                # <Value "python:icons.tag(configlet['icon'] or 'plone-controlpanel', tag_alt=configlet['title'])" (48:65)> -> __cache_4501879104
                                                __token = 3223
                                                try:
                                                    __zt_tmp = __attrs_4501878240
                                                except get('NameError', NameError):
                                                    __zt_tmp = None

                                                __cache_4501879104 = _static_4443408704('python', "icons.tag(configlet['icon'] or 'plone-controlpanel', tag_alt=configlet['title'])", econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                                                # <BinOp left=<Value "python:icons.tag(configlet['icon'] or 'plone-controlpanel', tag_alt=configlet['title'])" (48:65)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10c553e20> -> __condition
                                                __expression = __cache_4501879104

                                                # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                                                __value = _DEFAULT_MARKER
                                                __condition = (__expression is __value)
                                                if __condition:
                                                    pass
                                                else:
                                                    __content = __cache_4501879104
                                                    __content = __convert(__content)
                                                    if (__content is not None):
                                                        __append(__content)

                                            # <Interpolation value=<Substitution '\n                                ${configlet/title}\n                              ' (48:156)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10c553ee0> -> __content_4344921712
                                            __token = 3347
                                            __token = 3349
                                            try:
                                                __zt_tmp = __attrs_4501900880
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __content_4344921712 = _static_4443408704('path', 'configlet/title', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                            __content_4344921712 = __quote(__content_4344921712, '\x00', '&#0;', None, None)
                                            __content_4344921712 = ('%s%s%s' % ('\n                                ', (__content_4344921712 if (__content_4344921712 is not None) else ''), '\n                              ', ))
                                            if (__content_4344921712 is None):
                                                pass
                                            else:
                                                if (__content_4344921712 is None):
                                                    __content_4344921712 = None
                                                else:
                                                    __tt = type(__content_4344921712)
                                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                                        __content_4344921712 = str(__content_4344921712)
                                                    else:
                                                        if (__tt is bytes):
                                                            __content_4344921712 = decode(__content_4344921712)
                                                        else:
                                                            if (__tt is not str):
                                                                try:
                                                                    __content_4344921712 = __content_4344921712.__html__
                                                                except get('AttributeError', AttributeError):
                                                                    __converted = convert(__content_4344921712)
                                                                    __content_4344921712 = (str(__content_4344921712) if (__content_4344921712 is __converted) else __converted)
                                                                else:
                                                                    __content_4344921712 = __content_4344921712()
                                            if (__content_4344921712 is not None):
                                                __append(__content_4344921712)
                                            __append('</a>')
                                            if (__backup_icon_url_4494474736 is __marker):
                                                del econtext['icon_url']
                                            else:
                                                econtext['icon_url'] = __backup_icon_url_4494474736
                                            __append('\n                            </li>')
                                        __append('\n                          ')
                                        ____index_4501897376 -= 1
                                        if (____index_4501897376 > 0):
                                            __append('')
                                    if (__backup_configlet_4440297184 is __marker):
                                        del econtext['configlet']
                                    else:
                                        econtext['configlet'] = __backup_configlet_4440297184
                                    __append('\n                        </ul>\n                      </li>')
                                if (__backup_active_4497827456 is __marker):
                                    del econtext['active']
                                else:
                                    econtext['active'] = __backup_active_4497827456
                                if (__backup_configlets_4490668128 is __marker):
                                    del econtext['configlets']
                                else:
                                    econtext['configlets'] = __backup_configlets_4490668128
                                __append('\n                    ')
                                ____index_4501908752 -= 1
                                if (____index_4501908752 > 0):
                                    __append('')
                            if (__backup_group_4497904912 is __marker):
                                del econtext['group']
                            else:
                                econtext['group'] = __backup_group_4497904912
                            __append('\n                  </ul>\n                </div>')
                            if (__backup_current_url_4494961168 is __marker):
                                del econtext['current_url']
                            else:
                                econtext['current_url'] = __backup_current_url_4494961168
                            if (__backup_site_url_4494745824 is __marker):
                                del econtext['site_url']
                            else:
                                econtext['site_url'] = __backup_site_url_4494745824
                            if (__backup_groups_4497904000 is __marker):
                                del econtext['groups']
                            else:
                                econtext['groups'] = __backup_groups_4497904000
                            if (__backup_controlPanel_4494959536 is __marker):
                                del econtext['controlPanel']
                            else:
                                econtext['controlPanel'] = __backup_controlPanel_4494959536
                            __append('\n\n                ')
                            if (__slot_prefs_configlet_main is None):

                                # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501897808
                                __attrs_4501897808 = _static_4443296608

                                # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4501900016
                                __default_4501900016 = _DEFAULT_MARKER

                                # <Value 'nothing' (59:82)> -> __cache_4501909088
                                __token = 3694
                                try:
                                    __zt_tmp = __attrs_4501897808
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_4501909088 = _static_4443408704('path', 'nothing', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                                # <BinOp left=<Value 'nothing' (59:82)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10c55af20> -> __condition
                                __expression = __cache_4501909088

                                # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append('\n                  Page body text\n                ')
                                else:
                                    __content = __cache_4501909088
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                            else:
                                __slot_prefs_configlet_main(__stream, econtext.copy(), rcontext)
                            __append('\n\n              ')
                        _slots = econtext['__slot_main'] = _deque((__fill_main, ))

                        # <Value 'context/@@main_template/macros/content' (17:42)> -> __macro
                        __token = 898
                        try:
                            __zt_tmp = __attrs_4501817232
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __macro = _static_4443408704('path', 'context/@@main_template/macros/content', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                        __token = 898
                        __m = __macro.include
                        __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                        econtext.update(rcontext)
                        if (__backup_macroname_4491510848 is __marker):
                            del econtext['macroname']
                        else:
                            econtext['macroname'] = __backup_macroname_4491510848
                        __append('\n\n          ')
                    else:
                        __slot_prefs_configlet_content(__stream, econtext.copy(), rcontext)
                    __append('\n        ')
                else:
                    __slot_prefs_configlet_wrapper(__stream, econtext.copy(), rcontext)
                __append('\n    ')
            _slots = econtext['__slot_content'] = _deque((__fill_content, ))

            # <Value 'context/@@main_template/macros/master' (2:30)> -> __macro
            __token = 85
            try:
                __zt_tmp = __attrs_4501823760
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4443408704('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
            __token = 85
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4492526080 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4492526080
            __append('\n')
            __i18n_domain = __previous_i18n_domain_4501829376
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
            __token = None
            render_master(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_master': render_master, 'render': render, }