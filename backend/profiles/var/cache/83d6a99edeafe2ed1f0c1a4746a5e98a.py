# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/Products/CMFPlone/controlpanel/browser/overview.pt'

__tokens = {421: ("python:request.set('disable_plone.leftcolumn',1)", 12, 47), 517: (" python:request.set('disable_plone.rightcolumn',1", 13, 46), 979: ('view/upgrade_warning', 26, 23), 1261: ('string:${context/portal_url}/@@plone-upgrade', 34, 35), 1644: ('view/mailhost_warning', 46, 23), 2215: ('string:${portal_url}/@@mail-controlpanel', 57, 39), 2449: ('view/timezone_warning', 66, 23), 2982: ('string:${portal_url}/@@dateandtime-controlpanel', 78, 39), 3241: ('not:view/pil', 87, 23), 3522: ('view/categories', 96, 37), 3574: ("python:view.sublists(category.get('id'))", 97, 34), 3680: ('sublist', 98, 63), 3724: ('category/title', 99, 34), 3823: ('sublist', 102, 40), 3978: ('sublist', 105, 29), 4032: ('sublist', 106, 44), 4092: ('action/visible', 107, 50), 4244: ('action/icon', 109, 37), 4297: (" python:'http' in action['icon'", 110, 40), 4372: ('action/url', 111, 41), 4466: ('icon_url', 113, 42), 4571: ('action/icon', 115, 44), 4627: (' action/titl', 116, 43), 4736: ('not: icon_url', 118, 47), 4798: ("python:icons.tag(action['icon'] or 'plone-controlpanel', tag_alt=action['title'], tag_class='overview-icon')", 119, 47), 4976: ('action/title', 121, 38), 5339: ('not:sublist', 133, 31), 5702: ('view/version_overview', 145, 41), 5751: ('version', 146, 25), 5842: ('view/server_info', 148, 42), 5898: (' server_info/wsg', 149, 38), 6042: ('has_wsgi', 152, 51), 6113: ('not:has_wsgi', 153, 51), 6246: ('${server_info/server_name}', 157, 18), 6248: ('server_info/server_name', 157, 20), 6298: ('${server_info/version}', 158, 18), 6300: ('server_info/version', 158, 20), 6397: ('not:view/is_dev_mode', 163, 22), 6969: ('view/is_dev_mode', 175, 22), 261: ('here/prefs_main_template/macros/master', 6, 23), 261: ('here/prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque

_static_4500096336 = {'class': '', }
_static_4500078352 = {'class': '', }
_static_4500013008 = {'class': 'controlPanelSectionFooter', }
_static_4500040976 = {'class': 'discreet', }
_static_4500063808 = {'class': 'text-decoration-none text-center ', }
_static_4500043760 = {'src': '', 'alt': '', 'class': 'icon', }
_static_4500041840 = {'class': 'mb-3', }
_static_4500040064 = {'href': '', 'class': 'd-block text-dark text-center py-4 rounded btn btn-light h-100', }
_static_4500038480 = {'class': 'col mb-4', }
_static_4500035840 = {'class': 'configlets row row-cols-3 row-cols-sm-4 row-cols-lg-6 row-cols-xl-8 list-unstyled list w-100', }
_static_4500034352 = {'class': 'row', }
_static_4500033104 = {'class': '', }
_static_4500030944 = {'class': 'controlPanelSection mb-4', }
_static_4500009504 = {'class': 'alert alert-warning mb-5', 'role': 'status', }
_static_4500008400 = {'href': '', }
_static_4500004032 = {'class': 'alert alert-warning mb-5', 'role': 'status', }
_static_4500002976 = {'href': '', }
_static_4499717136 = {'class': 'alert alert-warning mb-5', 'role': 'status', }
_static_4499718048 = {'href': '#', 'title': 'Go to the upgrade page', }
_static_4499714496 = {'class': 'alert alert-warning mb-5', 'role': 'status', }
_static_4499712912 = {'class': 'lead', }
_static_4499711616 = {'class': 'documentFirstHeading', }
_static_4499709120 = {'class': 'controlPanel controlPanelOverview', }
_static_4443607136 = __C2ZContextWrapper
_static_4443408704 = __compile_zt_expr
_static_4499705856 = 'master'
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

            # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4499706192
            __attrs_4499706192 = _static_4443296608
            __previous_i18n_domain_4499706336 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4462481152 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x10c341000> name=None at 10c341030> -> __value
            __value = _static_4499705856
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4499708016
                __attrs_4499708016 = _static_4443296608
                __backup_disable_column_one_4497929456 = get('disable_column_one', __marker)

                # <Value "python:request.set('disable_plone.leftcolumn',1)" (12:47)> -> __value
                __token = 421
                try:
                    __zt_tmp = __attrs_4499708016
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4443408704('python', "request.set('disable_plone.leftcolumn',1)", econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                econtext['disable_column_one'] = __value
                __backup_disable_column_two_4497929600 = get('disable_column_two', __marker)

                # <Value "python:request.set('disable_plone.rightcolumn',1)" (13:46)> -> __value
                __token = 517
                try:
                    __zt_tmp = __attrs_4499708016
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4443408704('python', "request.set('disable_plone.rightcolumn',1)", econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                econtext['disable_column_two'] = __value
                if (__backup_disable_column_two_4497929600 is __marker):
                    del econtext['disable_column_two']
                else:
                    econtext['disable_column_two'] = __backup_disable_column_two_4497929600
                if (__backup_disable_column_one_4497929456 is __marker):
                    del econtext['disable_column_one']
                else:
                    econtext['disable_column_one'] = __backup_disable_column_one_4497929456
            _slots = econtext['__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x10c341cc0> name=None at 10c341b10> -> __attrs_4499709456
                __attrs_4499709456 = _static_4499709120

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="controlPanel controlPanelOverview">\n  ')

                # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4499710512
                __attrs_4499710512 = _static_4443296608

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n    ')

                # <Static value=<ast.Dict object at 0x10c342680> name=None at 10c342500> -> __attrs_4499711952
                __attrs_4499711952 = _static_4499711616

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">')
                __stream_4499711088 = []
                __append_4499711088 = __stream_4499711088.append
                __append_4499711088('Site Setup')
                __msgid_4499711088 = __re_whitespace(''.join(__stream_4499711088)).strip()
                if __msgid_4499711088:
                    __append(translate(__msgid_4499711088, mapping=None, default=__msgid_4499711088, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n\n    ')

                # <Static value=<ast.Dict object at 0x10c342b90> name=None at 10c342bc0> -> __attrs_4499713296
                __attrs_4499713296 = _static_4499712912

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="lead">')
                __stream_4499712432 = []
                __append_4499712432 = __stream_4499712432.append
                __append_4499712432('\n        Configuration area for Plone and add-on Products.\n    ')
                __msgid_4499712432 = __re_whitespace(''.join(__stream_4499712432)).strip()
                if 'description_control_panel':
                    __append(translate('description_control_panel', mapping=None, default=__msgid_4499712432, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n  </header>\n  ')

                # <Static value=<ast.Dict object at 0x10c3431c0> name=None at 10c3431f0> -> __attrs_4499714688
                __attrs_4499714688 = _static_4499714496

                # <Value 'view/upgrade_warning' (26:23)> -> __condition
                __token = 979
                try:
                    __zt_tmp = __attrs_4499714688
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4443408704('path', 'view/upgrade_warning', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-warning mb-5" role="status">\n      ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4499715936
                    __attrs_4499715936 = _static_4443296608

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_4499715456 = []
                    __append_4499715456 = __stream_4499715456.append
                    __append_4499715456('\n          Warning\n      ')
                    __msgid_4499715456 = __re_whitespace(''.join(__stream_4499715456)).strip()
                    if __msgid_4499715456:
                        __append(translate(__msgid_4499715456, mapping=None, default=__msgid_4499715456, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n      ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4499716800
                    __attrs_4499716800 = _static_4443296608
                    __stream_4499416768_link_continue_with_the_upgrade = ''
                    __stream_4499716416 = []
                    __append_4499716416 = __stream_4499716416.append
                    __append_4499716416('\n          The site configuration is outdated and needs to be\n          upgraded. Please\n          ')
                    __stream_4499416768_link_continue_with_the_upgrade = []
                    __append_4499416768_link_continue_with_the_upgrade = __stream_4499416768_link_continue_with_the_upgrade.append

                    # <Static value=<ast.Dict object at 0x10c343fa0> name=None at 10c343fd0> -> __attrs_4499997696
                    __attrs_4499997696 = _static_4499718048

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_4499416768_link_continue_with_the_upgrade('<a')

                    # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4499996976
                    __default_4499996976 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/portal_url}/@@plone-upgrade' (34:35)> -> __attr_href
                    __token = 1261
                    try:
                        __zt_tmp = __attrs_4499997696
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4443408704('string', '${context/portal_url}/@@plone-upgrade', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_4499416768_link_continue_with_the_upgrade((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4499997168
                    __default_4499997168 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<ast.Constant object at 0x10c388040> at 10c388160> -> __attr_title
                    __attr_title = 'Go to the upgrade page'
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append_4499416768_link_continue_with_the_upgrade((' title="%s"' % __attr_title))
                    __append_4499416768_link_continue_with_the_upgrade('>')
                    __stream_4499717376 = []
                    __append_4499717376 = __stream_4499717376.append
                    __append_4499717376('\n            continue with the upgrade\n          ')
                    __msgid_4499717376 = __re_whitespace(''.join(__stream_4499717376)).strip()
                    if __msgid_4499717376:
                        __append_4499416768_link_continue_with_the_upgrade(translate(__msgid_4499717376, mapping=None, default=__msgid_4499717376, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_4499416768_link_continue_with_the_upgrade('</a>')
                    __append_4499716416('${link_continue_with_the_upgrade}')
                    __stream_4499416768_link_continue_with_the_upgrade = ''.join(__stream_4499416768_link_continue_with_the_upgrade)
                    __append_4499716416('.\n      ')
                    __msgid_4499716416 = __re_whitespace(''.join(__stream_4499716416)).strip()
                    if __msgid_4499716416:
                        __append(translate(__msgid_4499716416, mapping={'link_continue_with_the_upgrade': __stream_4499416768_link_continue_with_the_upgrade, }, default=__msgid_4499716416, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n  </div>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x10c343c10> name=None at 10c343dc0> -> __attrs_4499998752
                __attrs_4499998752 = _static_4499717136

                # <Value 'view/mailhost_warning' (46:23)> -> __condition
                __token = 1644
                try:
                    __zt_tmp = __attrs_4499998752
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4443408704('path', 'view/mailhost_warning', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-warning mb-5" role="status">\n      ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500000000
                    __attrs_4500000000 = _static_4443296608

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_4499999520 = []
                    __append_4499999520 = __stream_4499999520.append
                    __append_4499999520('\n          Warning\n      ')
                    __msgid_4499999520 = __re_whitespace(''.join(__stream_4499999520)).strip()
                    if __msgid_4499999520:
                        __append(translate(__msgid_4499999520, mapping=None, default=__msgid_4499999520, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n      ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500000864
                    __attrs_4500000864 = _static_4443296608
                    __stream_4499416768_label_mail_control_panel_link = ''
                    __stream_4500000480 = []
                    __append_4500000480 = __stream_4500000480.append
                    __append_4500000480("\n          You have not configured a mail host or a site 'From'\n          address, various features including contact forms, email\n          notification and password reset will not work. Go to the\n          ")
                    __stream_4499416768_label_mail_control_panel_link = []
                    __append_4499416768_label_mail_control_panel_link = __stream_4499416768_label_mail_control_panel_link.append

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500001728
                    __attrs_4500001728 = _static_4443296608
                    __append_4499416768_label_mail_control_panel_link('\n              ')

                    # <Static value=<ast.Dict object at 0x10c3898a0> name=None at 10c3898d0> -> __attrs_4500003648
                    __attrs_4500003648 = _static_4500002976

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_4499416768_label_mail_control_panel_link('<a')

                    # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4500003120
                    __default_4500003120 = _DEFAULT_MARKER

                    # <Substitution 'string:${portal_url}/@@mail-controlpanel' (57:39)> -> __attr_href
                    __token = 2215
                    try:
                        __zt_tmp = __attrs_4500003648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4443408704('string', '${portal_url}/@@mail-controlpanel', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_4499416768_label_mail_control_panel_link((' href="%s"' % __attr_href))
                    __append_4499416768_label_mail_control_panel_link(' >')
                    __stream_4500002448 = []
                    __append_4500002448 = __stream_4500002448.append
                    __append_4500002448('Mail control panel')
                    __msgid_4500002448 = __re_whitespace(''.join(__stream_4500002448)).strip()
                    if 'text_no_mailhost_configured_control_panel_link':
                        __append_4499416768_label_mail_control_panel_link(translate('text_no_mailhost_configured_control_panel_link', mapping=None, default=__msgid_4500002448, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_4499416768_label_mail_control_panel_link('</a>\n          ')
                    __append_4500000480('${label_mail_control_panel_link}')
                    __stream_4499416768_label_mail_control_panel_link = ''.join(__stream_4499416768_label_mail_control_panel_link)
                    __append_4500000480('\n          to fix this.\n      ')
                    __msgid_4500000480 = __re_whitespace(''.join(__stream_4500000480)).strip()
                    if 'text_no_mailhost_configured':
                        __append(translate('text_no_mailhost_configured', mapping={'label_mail_control_panel_link': __stream_4499416768_label_mail_control_panel_link, }, default=__msgid_4500000480, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n  </div>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x10c389cc0> name=None at 10c389cf0> -> __attrs_4500004224
                __attrs_4500004224 = _static_4500004032

                # <Value 'view/timezone_warning' (66:23)> -> __condition
                __token = 2449
                try:
                    __zt_tmp = __attrs_4500004224
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4443408704('path', 'view/timezone_warning', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-warning mb-5" role="status">\n      ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500005472
                    __attrs_4500005472 = _static_4443296608

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_4500004992 = []
                    __append_4500004992 = __stream_4500004992.append
                    __append_4500004992('\n          Warning\n      ')
                    __msgid_4500004992 = __re_whitespace(''.join(__stream_4500004992)).strip()
                    if __msgid_4500004992:
                        __append(translate(__msgid_4500004992, mapping=None, default=__msgid_4500004992, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n      ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500006336
                    __attrs_4500006336 = _static_4443296608
                    __stream_4499416768_label_mail_event_settings_link = ''
                    __stream_4500005952 = []
                    __append_4500005952 = __stream_4500005952.append
                    __append_4500005952('\n\n          You have not set the portal timezone. Date/Time handling will not\n          work properly for timezone aware date/time values.\n          Go to the\n          ')
                    __stream_4499416768_label_mail_event_settings_link = []
                    __append_4499416768_label_mail_event_settings_link = __stream_4499416768_label_mail_event_settings_link.append

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500007200
                    __attrs_4500007200 = _static_4443296608
                    __append_4499416768_label_mail_event_settings_link('\n              ')

                    # <Static value=<ast.Dict object at 0x10c38add0> name=None at 10c38ae00> -> __attrs_4500009072
                    __attrs_4500009072 = _static_4500008400

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_4499416768_label_mail_event_settings_link('<a')

                    # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4500008544
                    __default_4500008544 = _DEFAULT_MARKER

                    # <Substitution 'string:${portal_url}/@@dateandtime-controlpanel' (78:39)> -> __attr_href
                    __token = 2982
                    try:
                        __zt_tmp = __attrs_4500009072
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4443408704('string', '${portal_url}/@@dateandtime-controlpanel', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_4499416768_label_mail_event_settings_link((' href="%s"' % __attr_href))
                    __append_4499416768_label_mail_event_settings_link(' >')
                    __stream_4500007872 = []
                    __append_4500007872 = __stream_4500007872.append
                    __append_4500007872('Date and Time Settings control panel')
                    __msgid_4500007872 = __re_whitespace(''.join(__stream_4500007872)).strip()
                    if 'text_no_timezone_configured_control_panel_link':
                        __append_4499416768_label_mail_event_settings_link(translate('text_no_timezone_configured_control_panel_link', mapping=None, default=__msgid_4500007872, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_4499416768_label_mail_event_settings_link('</a>\n          ')
                    __append_4500005952('${label_mail_event_settings_link}')
                    __stream_4499416768_label_mail_event_settings_link = ''.join(__stream_4499416768_label_mail_event_settings_link)
                    __append_4500005952('\n          to fix this.\n      ')
                    __msgid_4500005952 = __re_whitespace(''.join(__stream_4500005952)).strip()
                    if 'text_no_timezone_configured':
                        __append(translate('text_no_timezone_configured', mapping={'label_mail_event_settings_link': __stream_4499416768_label_mail_event_settings_link, }, default=__msgid_4500005952, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n  </div>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x10c38b220> name=None at 10c38b250> -> __attrs_4500009696
                __attrs_4500009696 = _static_4500009504

                # <Value 'not:view/pil' (87:23)> -> __condition
                __token = 3241
                try:
                    __zt_tmp = __attrs_4500009696
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4443408704('not', 'view/pil', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-warning mb-5" role="status">\n      ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500010944
                    __attrs_4500010944 = _static_4443296608

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_4500010464 = []
                    __append_4500010464 = __stream_4500010464.append
                    __append_4500010464('\n          Warning\n      ')
                    __msgid_4500010464 = __re_whitespace(''.join(__stream_4500010464)).strip()
                    if __msgid_4500010464:
                        __append(translate(__msgid_4500010464, mapping=None, default=__msgid_4500010464, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n      ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500011808
                    __attrs_4500011808 = _static_4443296608
                    __stream_4500011424 = []
                    __append_4500011424 = __stream_4500011424.append
                    __append_4500011424('\n          PIL is not installed properly, image scaling will not work.\n      ')
                    __msgid_4500011424 = __re_whitespace(''.join(__stream_4500011424)).strip()
                    if 'text_no_pil_installed':
                        __append(translate('text_no_pil_installed', mapping=None, default=__msgid_4500011424, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n  </div>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500012192
                __attrs_4500012192 = _static_4443296608
                __backup_category_4497485264 = get('category', __marker)

                # <Value 'view/categories' (96:37)> -> __iterator
                __token = 3522
                try:
                    __zt_tmp = __attrs_4500012192
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4443408704('path', 'view/categories', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                (__iterator, ____index_4500012432, ) = getname('repeat')('category', __iterator)
                econtext['category'] = None
                for __item in __iterator:
                    econtext['category'] = __item
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500029696
                    __attrs_4500029696 = _static_4443296608
                    __backup_sublist_4487817312 = get('sublist', __marker)

                    # <Value "python:view.sublists(category.get('id'))" (97:34)> -> __value
                    __token = 3574
                    try:
                        __zt_tmp = __attrs_4500029696
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4443408704('python', "view.sublists(category.get('id'))", econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                    econtext['sublist'] = __value
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x10c3905e0> name=None at 10c390430> -> __attrs_4500031280
                    __attrs_4500031280 = _static_4500030944

                    # <Value 'sublist' (98:63)> -> __condition
                    __token = 3680
                    try:
                        __zt_tmp = __attrs_4500031280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4443408704('path', 'sublist', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                    if __condition:

                        # <section ... (0:0)
                        # --------------------------------------------------------
                        __append('<section class="controlPanelSection mb-4">\n        ')

                        # <Static value=<ast.Dict object at 0x10c390e50> name=None at 10c390e80> -> __attrs_4500033488
                        __attrs_4500033488 = _static_4500033104

                        # <h3 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h3 class="">')

                        # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4500032528
                        __default_4500032528 = _DEFAULT_MARKER

                        # <Value 'category/title' (99:34)> -> __cache_4500032048
                        __token = 3724
                        try:
                            __zt_tmp = __attrs_4500033488
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4500032048 = _static_4443408704('path', 'category/title', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                        # <BinOp left=<Value 'category/title' (99:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10c390af0> -> __condition
                        __expression = __cache_4500032048

                        # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Category')
                        else:
                            __content = __cache_4500032048
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</h3>\n\n        ')

                        # <Static value=<ast.Dict object at 0x10c391330> name=None at 10c391360> -> __attrs_4500034736
                        __attrs_4500034736 = _static_4500034352

                        # <Value 'sublist' (102:40)> -> __condition
                        __token = 3823
                        try:
                            __zt_tmp = __attrs_4500034736
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4443408704('path', 'sublist', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                        if __condition:

                            # <nav ... (0:0)
                            # --------------------------------------------------------
                            __append('<nav class="row">\n\n          ')

                            # <Static value=<ast.Dict object at 0x10c391900> name=None at 10c391930> -> __attrs_4500036272
                            __attrs_4500036272 = _static_4500035840

                            # <Value 'sublist' (105:29)> -> __condition
                            __token = 3978
                            try:
                                __zt_tmp = __attrs_4500036272
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4443408704('path', 'sublist', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                            if __condition:

                                # <ul ... (0:0)
                                # --------------------------------------------------------
                                __append('<ul class="configlets row row-cols-3 row-cols-sm-4 row-cols-lg-6 row-cols-xl-8 list-unstyled list w-100">\n            ')

                                # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500037328
                                __attrs_4500037328 = _static_4443296608
                                __backup_action_4497917936 = get('action', __marker)

                                # <Value 'sublist' (106:44)> -> __iterator
                                __token = 4032
                                try:
                                    __zt_tmp = __attrs_4500037328
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __iterator = _static_4443408704('path', 'sublist', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                (__iterator, ____index_4500037568, ) = getname('repeat')('action', __iterator)
                                econtext['action'] = None
                                for __item in __iterator:
                                    econtext['action'] = __item
                                    __append('\n              ')

                                    # <Static value=<ast.Dict object at 0x10c392350> name=None at 10c392380> -> __attrs_4500038144
                                    __attrs_4500038144 = _static_4500038480

                                    # <Value 'action/visible' (107:50)> -> __condition
                                    __token = 4092
                                    try:
                                        __zt_tmp = __attrs_4500038144
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __condition = _static_4443408704('path', 'action/visible', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                    if __condition:

                                        # <li ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<li class="col mb-4">\n                ')

                                        # <Static value=<ast.Dict object at 0x10c392980> name=None at 10c3929b0> -> __attrs_4500040544
                                        __attrs_4500040544 = _static_4500040064
                                        __backup_icon_4490662080 = get('icon', __marker)

                                        # <Value 'action/icon' (109:37)> -> __value
                                        __token = 4244
                                        try:
                                            __zt_tmp = __attrs_4500040544
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __value = _static_4443408704('path', 'action/icon', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                        econtext['icon'] = __value
                                        __backup_icon_url_4490669088 = get('icon_url', __marker)

                                        # <Value "python:'http' in action['icon']" (110:40)> -> __value
                                        __token = 4297
                                        try:
                                            __zt_tmp = __attrs_4500040544
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __value = _static_4443408704('python', "'http' in action['icon']", econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                        econtext['icon_url'] = __value

                                        # <a ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<a')

                                        # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4500039632
                                        __default_4500039632 = _DEFAULT_MARKER

                                        # <Substitution 'action/url' (111:41)> -> __attr_href
                                        __token = 4372
                                        try:
                                            __zt_tmp = __attrs_4500040544
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_href = _static_4443408704('path', 'action/url', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                        __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                                        if (__attr_href is not None):
                                            __append((' href="%s"' % __attr_href))
                                        __append(' class="d-block text-dark text-center py-4 rounded btn btn-light h-100">\n                    ')

                                        # <Static value=<ast.Dict object at 0x10c393070> name=None at 10c3930a0> -> __attrs_4500042224
                                        __attrs_4500042224 = _static_4500041840

                                        # <div ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<div class="mb-3">\n                      ')

                                        # <Static value=<ast.Dict object at 0x10c3937f0> name=None at 10c393430> -> __attrs_4500044528
                                        __attrs_4500044528 = _static_4500043760

                                        # <Value 'icon_url' (113:42)> -> __condition
                                        __token = 4466
                                        try:
                                            __zt_tmp = __attrs_4500044528
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __condition = _static_4443408704('path', 'icon_url', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                        if __condition:

                                            # <img ... (0:0)
                                            # --------------------------------------------------------
                                            __append('<img')

                                            # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4500043856
                                            __default_4500043856 = _DEFAULT_MARKER

                                            # <Substitution 'action/icon' (115:44)> -> __attr_src
                                            __token = 4571
                                            try:
                                                __zt_tmp = __attrs_4500044528
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __attr_src = _static_4443408704('path', 'action/icon', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                            __attr_src = __quote(__attr_src, '"', '&quot;', '', _DEFAULT_MARKER)
                                            if (__attr_src is not None):
                                                __append((' src="%s"' % __attr_src))

                                            # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4500043952
                                            __default_4500043952 = _DEFAULT_MARKER

                                            # <Translate msgid=None node=<Substitution 'action/title' (116:43)> at 10c393460> -> __attr_alt

                                            # <Substitution 'action/title' (116:43)> -> __attr_alt
                                            __token = 4627
                                            try:
                                                __zt_tmp = __attrs_4500044528
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __attr_alt = _static_4443408704('path', 'action/title', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                            __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                                            __attr_alt = translate(__attr_alt, default=__attr_alt, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                            if (__attr_alt is not None):
                                                __append((' alt="%s"' % __attr_alt))
                                            __append(' class="icon">')
                                        __append('\n                      ')

                                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500062416
                                        __attrs_4500062416 = _static_4443296608

                                        # <Value 'not: icon_url' (118:47)> -> __condition
                                        __token = 4736
                                        try:
                                            __zt_tmp = __attrs_4500062416
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __condition = _static_4443408704('not', ' icon_url', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                                        if __condition:

                                            # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4500045776
                                            __default_4500045776 = _DEFAULT_MARKER

                                            # <Value "python:icons.tag(action['icon'] or 'plone-controlpanel', tag_alt=action['title'], tag_class='overview-icon')" (119:47)> -> __cache_4500045296
                                            __token = 4798
                                            try:
                                                __zt_tmp = __attrs_4500062416
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __cache_4500045296 = _static_4443408704('python', "icons.tag(action['icon'] or 'plone-controlpanel', tag_alt=action['title'], tag_class='overview-icon')", econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                                            # <BinOp left=<Value "python:icons.tag(action['icon'] or 'plone-controlpanel', tag_alt=action['title'], tag_class='overview-icon')" (119:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10c393eb0> -> __condition
                                            __expression = __cache_4500045296

                                            # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                                            __value = _DEFAULT_MARKER
                                            __condition = (__expression is __value)
                                            if __condition:
                                                pass
                                            else:
                                                __content = __cache_4500045296
                                                __content = __convert(__content)
                                                if (__content is not None):
                                                    __append(__content)
                                        __append('\n                    </div>\n                    ')

                                        # <Static value=<ast.Dict object at 0x10c398640> name=None at 10c398490> -> __attrs_4500064144
                                        __attrs_4500064144 = _static_4500063808

                                        # <div ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<div class="text-decoration-none text-center ">')

                                        # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4500063184
                                        __default_4500063184 = _DEFAULT_MARKER

                                        # <Value 'action/title' (121:38)> -> __cache_4500045104
                                        __token = 4976
                                        try:
                                            __zt_tmp = __attrs_4500064144
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __cache_4500045104 = _static_4443408704('path', 'action/title', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                                        # <BinOp left=<Value 'action/title' (121:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10c3982b0> -> __condition
                                        __expression = __cache_4500045104

                                        # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                                        __value = _DEFAULT_MARKER
                                        __condition = (__expression is __value)
                                        if __condition:
                                            __append('\n                        Title\n                    ')
                                        else:
                                            __content = __cache_4500045104
                                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                            __content = __quote(__content, None, '\xad', None, None)
                                            if (__content is not None):
                                                __append(__content)
                                        __append('</div>\n                </a>')
                                        if (__backup_icon_url_4490669088 is __marker):
                                            del econtext['icon_url']
                                        else:
                                            econtext['icon_url'] = __backup_icon_url_4490669088
                                        if (__backup_icon_4490662080 is __marker):
                                            del econtext['icon']
                                        else:
                                            econtext['icon'] = __backup_icon_4490662080
                                        __append('\n              </li>')
                                    __append('\n            ')
                                    ____index_4500037568 -= 1
                                    if (____index_4500037568 > 0):
                                        __append('')
                                if (__backup_action_4497917936 is __marker):
                                    del econtext['action']
                                else:
                                    econtext['action'] = __backup_action_4497917936
                                __append('\n            </ul>')
                            __append('\n          </nav>')
                        __append('\n\n          ')

                        # <Static value=<ast.Dict object at 0x10c392d10> name=None at 10c392e00> -> __attrs_4500064720
                        __attrs_4500064720 = _static_4500040976

                        # <Value 'not:sublist' (133:31)> -> __condition
                        __token = 5339
                        try:
                            __zt_tmp = __attrs_4500064720
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4443408704('not', 'sublist', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="discreet">')
                            __stream_4500037232 = []
                            __append_4500037232 = __stream_4500037232.append
                            __append_4500037232('\n              No preference panels available.\n          ')
                            __msgid_4500037232 = __re_whitespace(''.join(__stream_4500037232)).strip()
                            if 'label_no_prefs_panels_available':
                                __append(translate('label_no_prefs_panels_available', mapping=None, default=__msgid_4500037232, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</div>')
                        __append('\n\n      </section>')
                    __append('\n    ')
                    if (__backup_sublist_4487817312 is __marker):
                        del econtext['sublist']
                    else:
                        econtext['sublist'] = __backup_sublist_4487817312
                    __append('\n  ')
                    ____index_4500012432 -= 1
                    if (____index_4500012432 > 0):
                        __append('')
                if (__backup_category_4497485264 is __marker):
                    del econtext['category']
                else:
                    econtext['category'] = __backup_category_4497485264
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x10c38bfd0> name=None at 10c38ba60> -> __attrs_4500065296
                __attrs_4500065296 = _static_4500013008

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section class="controlPanelSectionFooter">\n    ')

                # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500066352
                __attrs_4500066352 = _static_4443296608

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2>')
                __stream_4500065872 = []
                __append_4500065872 = __stream_4500065872.append
                __append_4500065872('Version Overview')
                __msgid_4500065872 = __re_whitespace(''.join(__stream_4500065872)).strip()
                if 'heading_version_overview':
                    __append(translate('heading_version_overview', mapping=None, default=__msgid_4500065872, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h2>\n    ')

                # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500067216
                __attrs_4500067216 = _static_4443296608

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul>\n      ')

                # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500068080
                __attrs_4500068080 = _static_4443296608
                __backup_version_4497477584 = get('version', __marker)

                # <Value 'view/version_overview' (145:41)> -> __iterator
                __token = 5702
                try:
                    __zt_tmp = __attrs_4500068080
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4443408704('path', 'view/version_overview', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                (__iterator, ____index_4500068320, ) = getname('repeat')('version', __iterator)
                econtext['version'] = None
                for __item in __iterator:
                    econtext['version'] = __item
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500069904
                    __attrs_4500069904 = _static_4443296608

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li>')

                    # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4500069328
                    __default_4500069328 = _DEFAULT_MARKER

                    # <Value 'version' (146:25)> -> __cache_4500068848
                    __token = 5751
                    try:
                        __zt_tmp = __attrs_4500069904
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4500068848 = _static_4443408704('path', 'version', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                    # <BinOp left=<Value 'version' (146:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10c399ab0> -> __condition
                    __expression = __cache_4500068848

                    # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Version')
                    else:
                        __content = __cache_4500068848
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</li>\n      ')
                    ____index_4500068320 -= 1
                    if (____index_4500068320 > 0):
                        __append('')
                if (__backup_version_4497477584 is __marker):
                    del econtext['version']
                else:
                    econtext['version'] = __backup_version_4497477584
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500070288
                __attrs_4500070288 = _static_4443296608
                __backup_server_info_4497821792 = get('server_info', __marker)

                # <Value 'view/server_info' (148:42)> -> __value
                __token = 5842
                try:
                    __zt_tmp = __attrs_4500070288
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4443408704('path', 'view/server_info', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                econtext['server_info'] = __value
                __backup_has_wsgi_4497825344 = get('has_wsgi', __marker)

                # <Value 'server_info/wsgi' (149:38)> -> __value
                __token = 5898
                try:
                    __zt_tmp = __attrs_4500070288
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4443408704('path', 'server_info/wsgi', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                econtext['has_wsgi'] = __value
                __append('\n          ')

                # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500071632
                __attrs_4500071632 = _static_4443296608

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li>\n            ')

                # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500072592
                __attrs_4500072592 = _static_4443296608
                __stream_4500072208 = []
                __append_4500072208 = __stream_4500072208.append
                __append_4500072208('WSGI:')
                __msgid_4500072208 = __re_whitespace(''.join(__stream_4500072208)).strip()
                if __msgid_4500072208:
                    __append(translate(__msgid_4500072208, mapping=None, default=__msgid_4500072208, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500073264
                __attrs_4500073264 = _static_4443296608

                # <Value 'has_wsgi' (152:51)> -> __condition
                __token = 6042
                try:
                    __zt_tmp = __attrs_4500073264
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4443408704('path', 'has_wsgi', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_4500072304 = []
                    __append_4500072304 = __stream_4500072304.append
                    __append_4500072304('On')
                    __msgid_4500072304 = __re_whitespace(''.join(__stream_4500072304)).strip()
                    if __msgid_4500072304:
                        __append(translate(__msgid_4500072304, mapping=None, default=__msgid_4500072304, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>')
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500074416
                __attrs_4500074416 = _static_4443296608

                # <Value 'not:has_wsgi' (153:51)> -> __condition
                __token = 6113
                try:
                    __zt_tmp = __attrs_4500074416
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4443408704('not', 'has_wsgi', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_4500073936 = []
                    __append_4500073936 = __stream_4500073936.append
                    __append_4500073936('Off')
                    __msgid_4500073936 = __re_whitespace(''.join(__stream_4500073936)).strip()
                    if __msgid_4500073936:
                        __append(translate(__msgid_4500073936, mapping=None, default=__msgid_4500073936, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>')
                __append('\n          </li>\n          ')

                # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500075376
                __attrs_4500075376 = _static_4443296608

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li>\n            ')

                # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500076336
                __attrs_4500076336 = _static_4443296608
                __stream_4500075952 = []
                __append_4500075952 = __stream_4500075952.append
                __append_4500075952('Server:')
                __msgid_4500075952 = __re_whitespace(''.join(__stream_4500075952)).strip()
                if __msgid_4500075952:
                    __append(translate(__msgid_4500075952, mapping=None, default=__msgid_4500075952, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500076912
                __attrs_4500076912 = _static_4443296608

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')

                # <Interpolation value=<Substitution '${server_info/server_name}' (157:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10c39bac0> -> __content_4344921712
                __token = 6246
                __token = 6248
                try:
                    __zt_tmp = __attrs_4500076912
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_4344921712 = _static_4443408704('path', 'server_info/server_name', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
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
                __append('</span>\n            ')

                # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500077872
                __attrs_4500077872 = _static_4443296608

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')

                # <Interpolation value=<Substitution '${server_info/version}' (158:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 10c39be80> -> __content_4344921712
                __token = 6298
                __token = 6300
                try:
                    __zt_tmp = __attrs_4500077872
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_4344921712 = _static_4443408704('path', 'server_info/version', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
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
                __append('</span>\n          </li>\n      ')
                if (__backup_has_wsgi_4497825344 is __marker):
                    del econtext['has_wsgi']
                else:
                    econtext['has_wsgi'] = __backup_has_wsgi_4497825344
                if (__backup_server_info_4497821792 is __marker):
                    del econtext['server_info']
                else:
                    econtext['server_info'] = __backup_server_info_4497821792
                __append('\n    </ul>\n\n    ')

                # <Static value=<ast.Dict object at 0x10c39bf10> name=None at 10c39bf40> -> __attrs_4500095184
                __attrs_4500095184 = _static_4500078352

                # <Value 'not:view/is_dev_mode' (163:22)> -> __condition
                __token = 6397
                try:
                    __zt_tmp = __attrs_4500095184
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4443408704('not', 'view/is_dev_mode', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="">')
                    __stream_4500068272 = []
                    __append_4500068272 = __stream_4500068272.append
                    __append_4500068272('\n      You are running in "production mode". This is the preferred mode of\n      operation for a live Plone site, but means that some\n      configuration changes will not take effect until your server is\n      restarted or a product refreshed. If this is a development instance,\n      and you want to enable debug mode, stop the server, set \'debug-mode=on\'\n      in your buildout.cfg, re-run bin/buildout and then restart the server\n      process.\n    ')
                    __msgid_4500068272 = __re_whitespace(''.join(__stream_4500068272)).strip()
                    if 'description_production_mode':
                        __append(translate('description_production_mode', mapping=None, default=__msgid_4500068272, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>')
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x10c3a0550> name=None at 10c3a0580> -> __attrs_4500096720
                __attrs_4500096720 = _static_4500096336

                # <Value 'view/is_dev_mode' (175:22)> -> __condition
                __token = 6969
                try:
                    __zt_tmp = __attrs_4500096720
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4443408704('path', 'view/is_dev_mode', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="">')
                    __stream_4500095856 = []
                    __append_4500095856 = __stream_4500095856.append
                    __append_4500095856('\n      You are running in "debug mode". This mode is intended for sites that\n      are under development. This allows many configuration changes to be\n      immediately visible, but will make your site run more slowly. To turn\n      off debug mode, stop the server, set \'debug-mode=off\' in your\n      buildout.cfg, re-run bin/buildout and then restart the server\n      process.\n    ')
                    __msgid_4500095856 = __re_whitespace(''.join(__stream_4500095856)).strip()
                    if 'description_debug_mode':
                        __append(translate('description_debug_mode', mapping=None, default=__msgid_4500095856, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>')
                __append('\n  </section>\n\n</div>')
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'here/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_4499706192
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4443408704('path', 'here/prefs_main_template/macros/master', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4462481152 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4462481152
            __i18n_domain = __previous_i18n_domain_4499706336
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }