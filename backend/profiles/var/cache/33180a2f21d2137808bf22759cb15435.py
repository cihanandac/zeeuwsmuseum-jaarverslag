# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/Products/CMFPlone/browser/templates/main_template.pt'

__tokens = {71: ('string:&lt;!DOCTYPE ht', 2, 36), 344: ("python:context.restrictedTraverse('@@plone_portal_state')", 8, 31), 426: (" python:context.restrictedTraverse('@@plone_context_state'", 9, 23), 506: ("w python:context.restrictedTraverse('@@plone", 10, 19), 567: ("ns python:context.restrictedTraverse('@@iconresolve", 11, 13), 642: ("out python:context.restrictedTraverse('@@plone_layo", 12, 19), 709: ('lang python:portal_state.langu', 13, 10), 755: (' view nocall:view | nocall: plon', 14, 9), 804: (' dummy python: plone_layout.mark_vie', 15, 9), 862: ('tal_url python:portal_state.port', 16, 13), 921: ("rmission python:context.restrictedTraverse('portal_membership').checkP", 17, 17), 1018: ("roperties python:context.restrictedTraverse('portal_properties').site_", 18, 16), 1117: ("clude_head python:request.get('ajax_include_he", 19, 17), 1184: ('  ajax_load ', 20, 8), 1264: ('lang', 22, 27), 1313: ('provider:plone.httpheaders', 24, 40), 1416: ('provider:plone.htmlhead', 29, 32), 1471: ('nothing', 31, 26), 1757: ('provider:plone.scripts', 38, 32), 1882: ('provider:plone.htmlhead.links', 41, 33), 2021: ('portal_state/is_rtl', 46, 26), 2064: (" python:plone_layout.have_portlets('plone.leftcolumn', view", 47, 22), 2147: ("r python:plone_layout.have_portlets('plone.rightcolumn', vie", 48, 21), 2239: ('ss python:plone_layout.bodyClass(template, vi', 49, 28), 2415: ("  python:context.restrictedTraverse('@@plone_patterns_settings')", 52, 22), 2320: ('body_class', 50, 30), 2359: (" python:isRTL and 'rtl' or 'ltr", 51, 27), 2553: ('provider:plone.toolbar', 55, 32), 2664: ('provider:plone.portaltop', 58, 34), 2760: ('provider:plone.portalheader', 60, 36), 2880: ('provider:plone.mainnavigation', 65, 59), 3032: ('provider:plone.globalstatusmessage', 70, 42), 3211: ('provider:plone.abovecontent', 75, 59), 5052: ('sl', 130, 26), 5150: ('provider:plone.leftcolumn', 132, 38), 5325: ('sr', 138, 26), 5423: ('provider:plone.rightcolumn', 140, 38), 5586: ('provider:plone.portalfooter', 145, 34), 3606: ('provider:plone.abovecontenttitle', 91, 77), 3747: ('context/@@title', 94, 45), 3876: ('provider:plone.belowcontenttitle', 97, 77), 4028: ('context/@@description', 100, 44), 4175: ('provider:plone.belowcontentdescription', 103, 83), 4318: ('provider:plone.abovecontentbody', 107, 74), 4461: ('nothing', 110, 68), 4630: ('provider:plone.belowcontentbody', 115, 74), 4787: ('provider:plone.belowcontent', 119, 69)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4803161264 = {'id': 'viewlet-below-content', }
_static_4975329232 = {'id': 'viewlet-below-content-body', }
_static_4975083184 = {'id': 'content-core', }
_static_4975078432 = {'id': 'viewlet-above-content-body', }
_static_4975082080 = {'id': 'viewlet-below-content-description', }
_static_4975172704 = {'id': 'viewlet-below-content-title', }
_static_4975178608 = {'id': 'viewlet-above-content-title', }
_static_4975177072 = {'id': 'content', }
_static_4803160208 = {'id': 'portal-footer-wrapper', }
_static_4803151856 = {'id': 'portal-column-two', }
_static_4975170592 = {'id': 'portal-column-one', }
_static_4975171456 = {'id': 'portal-column-content', }
_static_4975167376 = {'id': 'viewlet-above-content', }
_static_4975262832 = {'id': 'global_statusmessage', }
_static_4975250448 = {'id': 'portal-mainnavigation', }
_static_4975256592 = {'id': 'portal-header', }
_static_4975250592 = {'id': 'portal-top', }
_static_4982429664 = set([])
_static_4760144336 = {'id': 'visual-portal-wrapper', 'class': 'body_class', 'dir': "python:isRTL and 'rtl' or 'ltr'", }
_static_4760144480 = {'name': 'generator', 'content': 'Plone - https://plone.org/', }
_static_4975126720 = {'charset': 'utf-8', }
_static_4975120528 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'lang': 'lang', }
_static_4754049008 = __C2ZContextWrapper
_static_4754050160 = __compile_zt_expr
_static_4753720080 = {}

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
            __slot_column_one_slot = econtext['__slot_column_one_slot'].pop()
        except:
            __slot_column_one_slot = None

        try:
            __slot_head_slot = econtext['__slot_head_slot'].pop()
        except:
            __slot_head_slot = None

        try:
            __slot_style_slot = econtext['__slot_style_slot'].pop()
        except:
            __slot_style_slot = None

        try:
            __slot_global_statusmessage = econtext['__slot_global_statusmessage'].pop()
        except:
            __slot_global_statusmessage = None

        try:
            __slot_portlets_two_slot = econtext['__slot_portlets_two_slot'].pop()
        except:
            __slot_portlets_two_slot = None

        try:
            __slot_portlets_one_slot = econtext['__slot_portlets_one_slot'].pop()
        except:
            __slot_portlets_one_slot = None

        try:
            __slot_javascript_head_slot = econtext['__slot_javascript_head_slot'].pop()
        except:
            __slot_javascript_head_slot = None

        try:
            __slot_top_slot = econtext['__slot_top_slot'].pop()
        except:
            __slot_top_slot = None

        try:
            __slot_content = econtext['__slot_content'].pop()
        except:
            __slot_content = None

        try:
            __slot_column_two_slot = econtext['__slot_column_two_slot'].pop()
        except:
            __slot_column_two_slot = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975117696
            __attrs_4975117696 = _static_4753720080
            __append('\n')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975131568
            __attrs_4975131568 = _static_4753720080

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975122400
            __default_4975122400 = _DEFAULT_MARKER

            # <Value 'string:<!DOCTYPE html>' (2:36)> -> __cache_4975121440
            __token = 71
            try:
                __zt_tmp = __attrs_4975131568
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4975121440 = _static_4754050160('string', '<!DOCTYPE html>', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

            # <BinOp left=<Value 'string:<!DOCTYPE html>' (2:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 1288a5270> -> __condition
            __expression = __cache_4975121440

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4975121440
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x1288a5090> name=None at 1288a7fa0> -> __attrs_4975123024
            __attrs_4975123024 = _static_4975120528
            __backup_portal_state_4974780928 = get('portal_state', __marker)

            # <Value "python:context.restrictedTraverse('@@plone_portal_state')" (8:31)> -> __value
            __token = 344
            try:
                __zt_tmp = __attrs_4975123024
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', "context.restrictedTraverse('@@plone_portal_state')", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['portal_state'] = __value
            __backup_context_state_4982517008 = get('context_state', __marker)

            # <Value "python:context.restrictedTraverse('@@plone_context_state')" (9:23)> -> __value
            __token = 426
            try:
                __zt_tmp = __attrs_4975123024
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', "context.restrictedTraverse('@@plone_context_state')", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['context_state'] = __value
            __backup_plone_view_4974782800 = get('plone_view', __marker)

            # <Value "python:context.restrictedTraverse('@@plone')" (10:19)> -> __value
            __token = 506
            try:
                __zt_tmp = __attrs_4975123024
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', "context.restrictedTraverse('@@plone')", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['plone_view'] = __value
            __backup_icons_4974787888 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (11:13)> -> __value
            __token = 567
            try:
                __zt_tmp = __attrs_4975123024
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_plone_layout_4982519696 = get('plone_layout', __marker)

            # <Value "python:context.restrictedTraverse('@@plone_layout')" (12:19)> -> __value
            __token = 642
            try:
                __zt_tmp = __attrs_4975123024
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', "context.restrictedTraverse('@@plone_layout')", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['plone_layout'] = __value
            __backup_lang_4982519264 = get('lang', __marker)

            # <Value 'python:portal_state.language()' (13:10)> -> __value
            __token = 709
            try:
                __zt_tmp = __attrs_4975123024
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', 'portal_state.language()', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['lang'] = __value
            __backup_view_4974773872 = get('view', __marker)

            # <Value 'nocall:view | nocall: plone_view' (14:9)> -> __value
            __token = 755
            try:
                __zt_tmp = __attrs_4975123024
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('nocall', 'view | nocall: plone_view', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['view'] = __value
            __backup_dummy_4974780688 = get('dummy', __marker)

            # <Value 'python: plone_layout.mark_view(view)' (15:9)> -> __value
            __token = 804
            try:
                __zt_tmp = __attrs_4975123024
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', ' plone_layout.mark_view(view)', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['dummy'] = __value
            __backup_portal_url_4974780640 = get('portal_url', __marker)

            # <Value 'python:portal_state.portal_url()' (16:13)> -> __value
            __token = 862
            try:
                __zt_tmp = __attrs_4975123024
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', 'portal_state.portal_url()', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['portal_url'] = __value
            __backup_checkPermission_4974782272 = get('checkPermission', __marker)

            # <Value "python:context.restrictedTraverse('portal_membership').checkPermission" (17:17)> -> __value
            __token = 921
            try:
                __zt_tmp = __attrs_4975123024
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', "context.restrictedTraverse('portal_membership').checkPermission", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['checkPermission'] = __value
            __backup_site_properties_4974783520 = get('site_properties', __marker)

            # <Value "python:context.restrictedTraverse('portal_properties').site_properties" (18:16)> -> __value
            __token = 1018
            try:
                __zt_tmp = __attrs_4975123024
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', "context.restrictedTraverse('portal_properties').site_properties", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['site_properties'] = __value
            __backup_ajax_include_head_4982518400 = get('ajax_include_head', __marker)

            # <Value "python:request.get('ajax_include_head', False)" (19:17)> -> __value
            __token = 1117
            try:
                __zt_tmp = __attrs_4975123024
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', "request.get('ajax_include_head', False)", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['ajax_include_head'] = __value
            __backup_ajax_load_4974782368 = get('ajax_load', __marker)

            # <Value 'python:False' (20:8)> -> __value
            __token = 1184
            try:
                __zt_tmp = __attrs_4975123024
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', 'False', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['ajax_load'] = __value
            __previous_i18n_domain_4975130656 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975127200
            __default_4975127200 = _DEFAULT_MARKER

            # <Substitution 'lang' (22:27)> -> __attr_lang
            __token = 1264
            try:
                __zt_tmp = __attrs_4975123024
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_4754050160('path', 'lang', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))
            __append('>\n\n    ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975125568
            __attrs_4975125568 = _static_4753720080

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975121536
            __default_4975121536 = _DEFAULT_MARKER

            # <Value 'provider:plone.httpheaders' (24:40)> -> __cache_4975130320
            __token = 1313
            try:
                __zt_tmp = __attrs_4975125568
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4975130320 = _static_4754050160('provider', 'plone.httpheaders', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.httpheaders' (24:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 1288a64d0> -> __condition
            __expression = __cache_4975130320

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4975130320
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975123648
            __attrs_4975123648 = _static_4753720080

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n    ')

            # <Static value=<ast.Dict object at 0x1288a68c0> name=None at 1288a5b70> -> __attrs_4975125232
            __attrs_4975125232 = _static_4975126720

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta charset="utf-8" />\n\n    ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975118416
            __attrs_4975118416 = _static_4753720080

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975117120
            __default_4975117120 = _DEFAULT_MARKER

            # <Value 'provider:plone.htmlhead' (29:32)> -> __cache_4975119280
            __token = 1416
            try:
                __zt_tmp = __attrs_4975118416
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4975119280 = _static_4754050160('provider', 'plone.htmlhead', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.htmlhead' (29:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 1288a63b0> -> __condition
            __expression = __cache_4975119280

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_4975119280
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4760148560
            __attrs_4760148560 = _static_4753720080

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4760145392
            __default_4760145392 = _DEFAULT_MARKER

            # <Value 'nothing' (31:26)> -> __cache_4975120960
            __token = 1471
            try:
                __zt_tmp = __attrs_4760148560
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4975120960 = _static_4754050160('path', 'nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

            # <BinOp left=<Value 'nothing' (31:26)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 1288a4460> -> __condition
            __expression = __cache_4975120960

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('\n        Various slots where you can insert elements in the header from a template.\n    ')
            else:
                __content = __cache_4975120960
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('\n    ')
            if (__slot_top_slot is None):

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4760148608
                __attrs_4760148608 = _static_4753720080
            else:
                __slot_top_slot(__stream, econtext.copy(), rcontext)
            __append('\n    ')
            if (__slot_head_slot is None):

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4760143232
                __attrs_4760143232 = _static_4753720080
            else:
                __slot_head_slot(__stream, econtext.copy(), rcontext)
            __append('\n    ')
            if (__slot_style_slot is None):

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4760156576
                __attrs_4760156576 = _static_4753720080
            else:
                __slot_style_slot(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4760155616
            __attrs_4760155616 = _static_4753720080

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4760148512
            __default_4760148512 = _DEFAULT_MARKER

            # <Value 'provider:plone.scripts' (38:32)> -> __cache_4760150288
            __token = 1757
            try:
                __zt_tmp = __attrs_4760155616
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4760150288 = _static_4754050160('provider', 'plone.scripts', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.scripts' (38:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 11bba1210> -> __condition
            __expression = __cache_4760150288

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_4760150288
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n    ')
            if (__slot_javascript_head_slot is None):

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4760156528
                __attrs_4760156528 = _static_4753720080
            else:
                __slot_javascript_head_slot(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4760156288
            __attrs_4760156288 = _static_4753720080

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4760142032
            __default_4760142032 = _DEFAULT_MARKER

            # <Value 'provider:plone.htmlhead.links' (41:33)> -> __cache_4760151440
            __token = 1882
            try:
                __zt_tmp = __attrs_4760156288
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4760151440 = _static_4754050160('provider', 'plone.htmlhead.links', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.htmlhead.links' (41:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 11bba2d70> -> __condition
            __expression = __cache_4760151440

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <link ... (0:0)
                # --------------------------------------------------------
                __append('<link />')
            else:
                __content = __cache_4760151440
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x11bba0a60> name=None at 11bba1ed0> -> __attrs_4760149232
            __attrs_4760149232 = _static_4760144480

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta name="generator" content="Plone - https://plone.org/" />\n\n  </head>\n\n  ')

            # <Static value=<ast.Dict object at 0x11bba09d0> name=None at 11bba0a30> -> __attrs_4975258560
            __attrs_4975258560 = _static_4760144336
            __backup_isRTL_4982518544 = get('isRTL', __marker)

            # <Value 'portal_state/is_rtl' (46:26)> -> __value
            __token = 2021
            try:
                __zt_tmp = __attrs_4975258560
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('path', 'portal_state/is_rtl', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['isRTL'] = __value
            __backup_sl_4974773488 = get('sl', __marker)

            # <Value "python:plone_layout.have_portlets('plone.leftcolumn', view)" (47:22)> -> __value
            __token = 2064
            try:
                __zt_tmp = __attrs_4975258560
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', "plone_layout.have_portlets('plone.leftcolumn', view)", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['sl'] = __value
            __backup_sr_4974787648 = get('sr', __marker)

            # <Value "python:plone_layout.have_portlets('plone.rightcolumn', view)" (48:21)> -> __value
            __token = 2147
            try:
                __zt_tmp = __attrs_4975258560
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', "plone_layout.have_portlets('plone.rightcolumn', view)", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['sr'] = __value
            __backup_body_class_4974777520 = get('body_class', __marker)

            # <Value 'python:plone_layout.bodyClass(template, view)' (49:28)> -> __value
            __token = 2239
            try:
                __zt_tmp = __attrs_4975258560
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4754050160('python', 'plone_layout.bodyClass(template, view)', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            econtext['body_class'] = __value

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body')

            # <Value "python:context.restrictedTraverse('@@plone_patterns_settings')()" (52:22)> -> __cache_4975247808
            __token = 2415
            try:
                __zt_tmp = __attrs_4975258560
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4975247808 = _static_4754050160('python', "context.restrictedTraverse('@@plone_patterns_settings')()", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            if ('id' not in __chain(__cache_4975247808)):
                __append(' id="visual-portal-wrapper"')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4760153600
            __default_4760153600 = _DEFAULT_MARKER

            # <Substitution 'body_class' (50:30)> -> __attr_class
            __token = 2320
            try:
                __zt_tmp = __attrs_4975258560
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4754050160('path', 'body_class', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_class is not None) and ('class' not in __chain(__cache_4975247808))):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4760146592
            __default_4760146592 = _DEFAULT_MARKER

            # <Substitution "python:isRTL and 'rtl' or 'ltr'" (51:27)> -> __attr_dir
            __token = 2359
            try:
                __zt_tmp = __attrs_4975258560
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_dir = _static_4754050160('python', "isRTL and 'rtl' or 'ltr'", econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
            __attr_dir = __quote(__attr_dir, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_dir is not None) and ('dir' not in __chain(__cache_4975247808))):
                __append((' dir="%s"' % __attr_dir))
            __attr_4975252464 = __cache_4975247808
            for (name, value, ) in __attr_4975252464.items():
                if ((name not in _static_4982429664) and (value is not None)):
                    __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
            __append('>\n\n    ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975252128
            __attrs_4975252128 = _static_4753720080

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975248624
            __default_4975248624 = _DEFAULT_MARKER

            # <Value 'provider:plone.toolbar' (55:32)> -> __cache_4975249440
            __token = 2553
            try:
                __zt_tmp = __attrs_4975252128
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4975249440 = _static_4754050160('provider', 'plone.toolbar', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.toolbar' (55:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 1288c7910> -> __condition
            __expression = __cache_4975249440

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_4975249440
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x1288c4ca0> name=None at 1288c45e0> -> __attrs_4975258848
            __attrs_4975258848 = _static_4975250592
            __previous_i18n_domain_4975256304 = __i18n_domain
            __i18n_domain = 'plone'

            # <header ... (0:0)
            # --------------------------------------------------------
            __append('<header id="portal-top">\n      ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975257936
            __attrs_4975257936 = _static_4753720080

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975261872
            __default_4975261872 = _DEFAULT_MARKER

            # <Value 'provider:plone.portaltop' (58:34)> -> __cache_4975252368
            __token = 2664
            try:
                __zt_tmp = __attrs_4975257936
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4975252368 = _static_4754050160('provider', 'plone.portaltop', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.portaltop' (58:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 1288c7160> -> __condition
            __expression = __cache_4975252368

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_4975252368
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n      ')

            # <Static value=<ast.Dict object at 0x1288c6410> name=None at 1288c4d90> -> __attrs_4975260768
            __attrs_4975260768 = _static_4975256592

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="portal-header">\n        ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975261344
            __attrs_4975261344 = _static_4753720080

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975247904
            __default_4975247904 = _DEFAULT_MARKER

            # <Value 'provider:plone.portalheader' (60:36)> -> __cache_4975259952
            __token = 2760
            try:
                __zt_tmp = __attrs_4975261344
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4975259952 = _static_4754050160('provider', 'plone.portalheader', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.portalheader' (60:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 1288c5780> -> __condition
            __expression = __cache_4975259952

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_4975259952
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n      </div>\n\n    </header>')
            __i18n_domain = __previous_i18n_domain_4975256304
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x1288c4c10> name=None at 1288c6d10> -> __attrs_4975251792
            __attrs_4975251792 = _static_4975250448

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="portal-mainnavigation">')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975256784
            __default_4975256784 = _DEFAULT_MARKER

            # <Value 'provider:plone.mainnavigation' (65:59)> -> __cache_4975258032
            __token = 2880
            try:
                __zt_tmp = __attrs_4975251792
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4975258032 = _static_4754050160('provider', 'plone.mainnavigation', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.mainnavigation' (65:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 1288c4580> -> __condition
            __expression = __cache_4975258032

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('\n      The main navigation\n    ')
            else:
                __content = __cache_4975258032
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n\n    ')

            # <Static value=<ast.Dict object at 0x1288c7c70> name=None at 1288c7100> -> __attrs_4975248816
            __attrs_4975248816 = _static_4975262832

            # <section ... (0:0)
            # --------------------------------------------------------
            __append('<section id="global_statusmessage">\n      ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975254912
            __attrs_4975254912 = _static_4753720080

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975255488
            __default_4975255488 = _DEFAULT_MARKER

            # <Value 'provider:plone.globalstatusmessage' (70:42)> -> __cache_4975249728
            __token = 3032
            try:
                __zt_tmp = __attrs_4975254912
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4975249728 = _static_4754050160('provider', 'plone.globalstatusmessage', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.globalstatusmessage' (70:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 1288c6260> -> __condition
            __expression = __cache_4975249728

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4975249728
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n      ')
            if (__slot_global_statusmessage is None):

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975254288
                __attrs_4975254288 = _static_4753720080

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n      </div>')
            else:
                __slot_global_statusmessage(__stream, econtext.copy(), rcontext)
            __append('\n    </section>\n\n    ')

            # <Static value=<ast.Dict object at 0x1288b0790> name=None at 1288b1480> -> __attrs_4975177456
            __attrs_4975177456 = _static_4975167376

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="viewlet-above-content">')

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975257504
            __default_4975257504 = _DEFAULT_MARKER

            # <Value 'provider:plone.abovecontent' (75:59)> -> __cache_4975254336
            __token = 3211
            try:
                __zt_tmp = __attrs_4975177456
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4975254336 = _static_4754050160('provider', 'plone.abovecontent', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.abovecontent' (75:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 1288c6170> -> __condition
            __expression = __cache_4975254336

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4975254336
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n\n    ')

            # <Static value=<ast.Dict object at 0x1288b1780> name=None at 1288b0c70> -> __attrs_4975166848
            __attrs_4975166848 = _static_4975171456

            # <article ... (0:0)
            # --------------------------------------------------------
            __append('<article id="portal-column-content">\n\n      ')
            if (__slot_content is None):

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975166944
                __attrs_4975166944 = _static_4753720080
                __append('\n\n      ')
                __token = None
                render_content(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n\n      ')
            else:
                __slot_content(__stream, econtext.copy(), rcontext)
            __append('\n    </article>\n\n    ')
            if (__slot_column_one_slot is None):

                # <Static value=<ast.Dict object at 0x1288b1420> name=None at 1288b0100> -> __attrs_4975176208
                __attrs_4975176208 = _static_4975170592

                # <Value 'sl' (130:26)> -> __condition
                __token = 5052
                try:
                    __zt_tmp = __attrs_4975176208
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4754050160('path', 'sl', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                if __condition:

                    # <aside ... (0:0)
                    # --------------------------------------------------------
                    __append('<aside id="portal-column-one">\n      ')
                    if (__slot_portlets_one_slot is None):

                        # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4803159536
                        __attrs_4803159536 = _static_4753720080
                        __append('\n        ')

                        # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4803152000
                        __attrs_4803152000 = _static_4753720080

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4803164768
                        __default_4803164768 = _DEFAULT_MARKER

                        # <Value 'provider:plone.leftcolumn' (132:38)> -> __cache_4803152144
                        __token = 5150
                        try:
                            __zt_tmp = __attrs_4803152000
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4803152144 = _static_4754050160('provider', 'plone.leftcolumn', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                        # <BinOp left=<Value 'provider:plone.leftcolumn' (132:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 11e4a44f0> -> __condition
                        __expression = __cache_4803152144

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4803152144
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n      ')
                    else:
                        __slot_portlets_one_slot(__stream, econtext.copy(), rcontext)
                    __append('\n    </aside>')
            else:
                __slot_column_one_slot(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')
            if (__slot_column_two_slot is None):

                # <Static value=<ast.Dict object at 0x11e4a47f0> name=None at 11e4a7340> -> __attrs_4803151904
                __attrs_4803151904 = _static_4803151856

                # <Value 'sr' (138:26)> -> __condition
                __token = 5325
                try:
                    __zt_tmp = __attrs_4803151904
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4754050160('path', 'sr', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))
                if __condition:

                    # <aside ... (0:0)
                    # --------------------------------------------------------
                    __append('<aside id="portal-column-two">\n      ')
                    if (__slot_portlets_two_slot is None):

                        # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4803151520
                        __attrs_4803151520 = _static_4753720080
                        __append('\n        ')

                        # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4803166016
                        __attrs_4803166016 = _static_4753720080

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4803160832
                        __default_4803160832 = _DEFAULT_MARKER

                        # <Value 'provider:plone.rightcolumn' (140:38)> -> __cache_4803160640
                        __token = 5423
                        try:
                            __zt_tmp = __attrs_4803166016
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4803160640 = _static_4754050160('provider', 'plone.rightcolumn', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                        # <BinOp left=<Value 'provider:plone.rightcolumn' (140:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 11e4a6f20> -> __condition
                        __expression = __cache_4803160640

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4803160640
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n      ')
                    else:
                        __slot_portlets_two_slot(__stream, econtext.copy(), rcontext)
                    __append('\n    </aside>')
            else:
                __slot_column_two_slot(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x11e4a6890> name=None at 11e4a7580> -> __attrs_4803162272
            __attrs_4803162272 = _static_4803160208
            __previous_i18n_domain_4803165872 = __i18n_domain
            __i18n_domain = 'plone'

            # <footer ... (0:0)
            # --------------------------------------------------------
            __append('<footer id="portal-footer-wrapper">\n      ')

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4982507024
            __attrs_4982507024 = _static_4753720080

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4982520416
            __default_4982520416 = _DEFAULT_MARKER

            # <Value 'provider:plone.portalfooter' (145:34)> -> __cache_4982508080
            __token = 5586
            try:
                __zt_tmp = __attrs_4982507024
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4982508080 = _static_4754050160('provider', 'plone.portalfooter', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.portalfooter' (145:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128fb09a0> -> __condition
            __expression = __cache_4982508080

            # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_4982508080
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n    </footer>')
            __i18n_domain = __previous_i18n_domain_4803165872
            __append('\n\n  </body>')
            if (__backup_body_class_4974777520 is __marker):
                del econtext['body_class']
            else:
                econtext['body_class'] = __backup_body_class_4974777520
            if (__backup_sr_4974787648 is __marker):
                del econtext['sr']
            else:
                econtext['sr'] = __backup_sr_4974787648
            if (__backup_sl_4974773488 is __marker):
                del econtext['sl']
            else:
                econtext['sl'] = __backup_sl_4974773488
            if (__backup_isRTL_4982518544 is __marker):
                del econtext['isRTL']
            else:
                econtext['isRTL'] = __backup_isRTL_4982518544
            __append('\n</html>')
            __i18n_domain = __previous_i18n_domain_4975130656
            if (__backup_ajax_load_4974782368 is __marker):
                del econtext['ajax_load']
            else:
                econtext['ajax_load'] = __backup_ajax_load_4974782368
            if (__backup_ajax_include_head_4982518400 is __marker):
                del econtext['ajax_include_head']
            else:
                econtext['ajax_include_head'] = __backup_ajax_include_head_4982518400
            if (__backup_site_properties_4974783520 is __marker):
                del econtext['site_properties']
            else:
                econtext['site_properties'] = __backup_site_properties_4974783520
            if (__backup_checkPermission_4974782272 is __marker):
                del econtext['checkPermission']
            else:
                econtext['checkPermission'] = __backup_checkPermission_4974782272
            if (__backup_portal_url_4974780640 is __marker):
                del econtext['portal_url']
            else:
                econtext['portal_url'] = __backup_portal_url_4974780640
            if (__backup_dummy_4974780688 is __marker):
                del econtext['dummy']
            else:
                econtext['dummy'] = __backup_dummy_4974780688
            if (__backup_view_4974773872 is __marker):
                del econtext['view']
            else:
                econtext['view'] = __backup_view_4974773872
            if (__backup_lang_4982519264 is __marker):
                del econtext['lang']
            else:
                econtext['lang'] = __backup_lang_4982519264
            if (__backup_plone_layout_4982519696 is __marker):
                del econtext['plone_layout']
            else:
                econtext['plone_layout'] = __backup_plone_layout_4982519696
            if (__backup_icons_4974787888 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_4974787888
            if (__backup_plone_view_4974782800 is __marker):
                del econtext['plone_view']
            else:
                econtext['plone_view'] = __backup_plone_view_4974782800
            if (__backup_context_state_4982517008 is __marker):
                del econtext['context_state']
            else:
                econtext['context_state'] = __backup_context_state_4982517008
            if (__backup_portal_state_4974780928 is __marker):
                del econtext['portal_state']
            else:
                econtext['portal_state'] = __backup_portal_state_4974780928
            __append('\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_content(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_body = econtext['__slot_body'].pop()
        except:
            __slot_body = None

        try:
            __slot_content_title = econtext['__slot_content_title'].pop()
        except:
            __slot_content_title = None

        try:
            __slot_content_description = econtext['__slot_content_description'].pop()
        except:
            __slot_content_description = None

        try:
            __slot_content_core = econtext['__slot_content_core'].pop()
        except:
            __slot_content_core = None

        try:
            __slot_main = econtext['__slot_main'].pop()
        except:
            __slot_main = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975169008
            __attrs_4975169008 = _static_4753720080
            __append('\n\n        ')
            if (__slot_body is None):

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975168096
                __attrs_4975168096 = _static_4753720080
                __append('\n\n          ')

                # <Static value=<ast.Dict object at 0x1288b2d70> name=None at 1288b18a0> -> __attrs_4975174480
                __attrs_4975174480 = _static_4975177072

                # <article ... (0:0)
                # --------------------------------------------------------
                __append('<article id="content">\n\n            ')
                if (__slot_main is None):

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975179808
                    __attrs_4975179808 = _static_4753720080
                    __append('\n\n              ')

                    # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975172512
                    __attrs_4975172512 = _static_4753720080

                    # <header ... (0:0)
                    # --------------------------------------------------------
                    __append('<header>\n\n                ')

                    # <Static value=<ast.Dict object at 0x1288b3370> name=None at 1288b2740> -> __attrs_4975179712
                    __attrs_4975179712 = _static_4975178608

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-above-content-title">')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975169488
                    __default_4975169488 = _DEFAULT_MARKER

                    # <Value 'provider:plone.abovecontenttitle' (91:77)> -> __cache_4975168576
                    __token = 3606
                    try:
                        __zt_tmp = __attrs_4975179712
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4975168576 = _static_4754050160('provider', 'plone.abovecontenttitle', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.abovecontenttitle' (91:77)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 1288b0f10> -> __condition
                    __expression = __cache_4975168576

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4975168576
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n                ')
                    if (__slot_content_title is None):

                        # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975168480
                        __attrs_4975168480 = _static_4753720080
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975180720
                        __attrs_4975180720 = _static_4753720080

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975175872
                        __default_4975175872 = _DEFAULT_MARKER

                        # <Value 'context/@@title' (94:45)> -> __cache_4975181440
                        __token = 3747
                        try:
                            __zt_tmp = __attrs_4975180720
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4975181440 = _static_4754050160('path', 'context/@@title', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                        # <BinOp left=<Value 'context/@@title' (94:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 1288b3fa0> -> __condition
                        __expression = __cache_4975181440

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <h1 ... (0:0)
                            # --------------------------------------------------------
                            __append('<h1 />')
                        else:
                            __content = __cache_4975181440
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n                ')
                    else:
                        __slot_content_title(__stream, econtext.copy(), rcontext)
                    __append('\n\n                ')

                    # <Static value=<ast.Dict object at 0x1288b1c60> name=None at 1288b3520> -> __attrs_4975168432
                    __attrs_4975168432 = _static_4975172704

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-below-content-title">')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975175680
                    __default_4975175680 = _DEFAULT_MARKER

                    # <Value 'provider:plone.belowcontenttitle' (97:77)> -> __cache_4975181104
                    __token = 3876
                    try:
                        __zt_tmp = __attrs_4975168432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4975181104 = _static_4754050160('provider', 'plone.belowcontenttitle', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.belowcontenttitle' (97:77)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 1288b3f40> -> __condition
                    __expression = __cache_4975181104

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4975181104
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n                ')
                    if (__slot_content_description is None):

                        # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975073440
                        __attrs_4975073440 = _static_4753720080
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4975077904
                        __attrs_4975077904 = _static_4753720080

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975081024
                        __default_4975081024 = _DEFAULT_MARKER

                        # <Value 'context/@@description' (100:44)> -> __cache_4975075120
                        __token = 4028
                        try:
                            __zt_tmp = __attrs_4975077904
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4975075120 = _static_4754050160('path', 'context/@@description', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                        # <BinOp left=<Value 'context/@@description' (100:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128899300> -> __condition
                        __expression = __cache_4975075120

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <p ... (0:0)
                            # --------------------------------------------------------
                            __append('<p />')
                        else:
                            __content = __cache_4975075120
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n                ')
                    else:
                        __slot_content_description(__stream, econtext.copy(), rcontext)
                    __append('\n\n                ')

                    # <Static value=<ast.Dict object at 0x12889ba60> name=None at 12889b0d0> -> __attrs_4975080640
                    __attrs_4975080640 = _static_4975082080

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-below-content-description">')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975081600
                    __default_4975081600 = _DEFAULT_MARKER

                    # <Value 'provider:plone.belowcontentdescription' (103:83)> -> __cache_4975083280
                    __token = 4175
                    try:
                        __zt_tmp = __attrs_4975080640
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4975083280 = _static_4754050160('provider', 'plone.belowcontentdescription', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.belowcontentdescription' (103:83)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 12889a530> -> __condition
                    __expression = __cache_4975083280

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4975083280
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n              </header>\n\n              ')

                    # <Static value=<ast.Dict object at 0x12889ac20> name=None at 12889a260> -> __attrs_4975076320
                    __attrs_4975076320 = _static_4975078432

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-above-content-body">')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975072960
                    __default_4975072960 = _DEFAULT_MARKER

                    # <Value 'provider:plone.abovecontentbody' (107:74)> -> __cache_4975081936
                    __token = 4318
                    try:
                        __zt_tmp = __attrs_4975076320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4975081936 = _static_4754050160('provider', 'plone.abovecontentbody', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.abovecontentbody' (107:74)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 12889b5b0> -> __condition
                    __expression = __cache_4975081936

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4975081936
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n              ')

                    # <Static value=<ast.Dict object at 0x12889beb0> name=None at 12889a200> -> __attrs_4981126624
                    __attrs_4981126624 = _static_4975083184

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="content-core">\n                ')
                    if (__slot_content_core is None):

                        # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4981125520
                        __attrs_4981125520 = _static_4753720080

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4981125808
                        __default_4981125808 = _DEFAULT_MARKER

                        # <Value 'nothing' (110:68)> -> __cache_4981125664
                        __token = 4461
                        try:
                            __zt_tmp = __attrs_4981125520
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4981125664 = _static_4754050160('path', 'nothing', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                        # <BinOp left=<Value 'nothing' (110:68)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 128e5fc40> -> __condition
                        __expression = __cache_4981125664

                        # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n                  Page body text\n                ')
                        else:
                            __content = __cache_4981125664
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    else:
                        __slot_content_core(__stream, econtext.copy(), rcontext)
                    __append('\n              </div>\n\n              ')

                    # <Static value=<ast.Dict object at 0x1288d7fd0> name=None at 1288d5600> -> __attrs_4975321120
                    __attrs_4975321120 = _static_4975329232

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-below-content-body">')

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4975321408
                    __default_4975321408 = _DEFAULT_MARKER

                    # <Value 'provider:plone.belowcontentbody' (115:74)> -> __cache_4981129120
                    __token = 4630
                    try:
                        __zt_tmp = __attrs_4975321120
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4981129120 = _static_4754050160('provider', 'plone.belowcontentbody', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.belowcontentbody' (115:74)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 1288d4bb0> -> __condition
                    __expression = __cache_4981129120

                    # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4981129120
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n            ')
                else:
                    __slot_main(__stream, econtext.copy(), rcontext)
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x11b580310> name=None at 11b5839d0> -> __attrs_4803164096
                __attrs_4803164096 = _static_4753720080

                # <footer ... (0:0)
                # --------------------------------------------------------
                __append('<footer>\n              ')

                # <Static value=<ast.Dict object at 0x11e4a6cb0> name=None at 11e4a7af0> -> __attrs_4803151664
                __attrs_4803151664 = _static_4803161264

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="viewlet-below-content">')

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __default_4803160304
                __default_4803160304 = _DEFAULT_MARKER

                # <Value 'provider:plone.belowcontent' (119:69)> -> __cache_4803157664
                __token = 4787
                try:
                    __zt_tmp = __attrs_4803151664
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4803157664 = _static_4754050160('provider', 'plone.belowcontent', econtext=econtext)(_static_4754049008(econtext, __zt_tmp))

                # <BinOp left=<Value 'provider:plone.belowcontent' (119:69)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 11b5820b0> at 11e4a45b0> -> __condition
                __expression = __cache_4803157664

                # <Symbol value=<DEFAULT> at 11b5820b0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4803157664
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('</div>\n            </footer>\n          </article>\n        ')
            else:
                __slot_body(__stream, econtext.copy(), rcontext)
            __append('\n      ')
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

    return {'render_master': render_master, 'render_content': render_content, 'render': render, }