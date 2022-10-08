# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/Products/CMFPlone/controlpanel/browser/quickinstaller.pt'

__tokens = {1150: ('view/get_upgrades', 35, 36), 1208: (' python:len(products', 36, 39), 1386: ('not:products', 39, 30), 1667: ('products', 43, 27), 1781: ('products', 45, 44), 1822: ('product/id', 46, 30), 2084: ('pid', 50, 44), 2355: ('string:Upgrade ${pid}', 56, 44), 2451: ('product/title', 59, 33), 2648: ('product/description', 64, 39), 2682: ('product/description', 64, 73), 2809: ('pid', 65, 58), 2856: ('product/version', 65, 105), 3022: ('product/upgrade_info', 68, 43), 3237: ('not:upgrade_info/hasProfile', 72, 39), 3419: ('upgrade_info/installedVersion', 74, 77), 3533: ('upgrade_info/hasProfile', 76, 39), 3736: ('upgrade_info/installedVersion', 78, 87), 3993: ('upgrade_info/newVersion', 81, 86), 4133: ('not:upgrade_info/available', 85, 38), 4617: ('python:num_products > 1', 96, 29), 4787: ('products', 98, 51), 4953: ('product/id', 101, 44), 5522: ('view/get_available', 116, 36), 5578: (' python:len(products', 117, 36), 5829: ('products', 121, 34), 5909: ('product/id', 122, 35), 6129: ('pid', 126, 46), 6485: ('product/title', 137, 33), 6682: ('product/description', 142, 39), 6766: ('product/description', 144, 29), 6875: ('pid', 145, 58), 6922: ('product/version', 145, 105), 7091: ('not:product/uninstall_profile', 149, 31), 7389: ('view/get_installed', 158, 36), 7448: (' python:len(products', 159, 39), 7701: ('products', 163, 34), 7781: ('product/id', 164, 35), 7995: ('pid', 168, 42), 8213: ('product/uninstall_profile', 173, 37), 8405: ('product/title', 179, 35), 8612: ('product/description', 184, 41), 8700: ('product/description', 186, 31), 8811: ('pid', 187, 60), 8858: ('product/version', 187, 107), 9032: ('not:product/uninstall_profile', 191, 33), 9331: ('view/get_broken', 200, 36), 9388: (' python:len(products', 201, 40), 9443: ('num_products', 202, 31), 9685: ('products', 206, 34), 9780: ('product/product_id', 208, 33), 9976: ('product/type', 213, 33), 10087: ('product/value', 214, 61), 261: ('context/prefs_main_template/macros/master', 6, 23), 261: ('context/prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4490645264 = {'class': 'discreet', }
_static_4498104256 = {'class': 'configletDescription discreet', }
_static_4498380240 = {'class': 'list-group-item mt-2 pb-3', }
_static_4501718160 = {'class': 'configlets list-group list-group-flush', }
_static_4498374864 = {'class': 'card-header', }
_static_4501612400 = {'id': 'broken-products', 'class': 'card mb-4', }
_static_4499717520 = {'class': 'alert alert-info mt-2 mb-0', 'role': 'status', }
_static_4499718000 = {'class': 'discreet', }
_static_4499715648 = {'class': 'configletDescription discreet', }
_static_4499708784 = {'class': 'btn btn-sm btn-danger', 'type': 'submit', 'value': 'Uninstall', 'name': 'form.submitted', }
_static_4501611440 = {'type': 'hidden', 'name': 'uninstall_product', 'value': 'pid', }
_static_4501615520 = {'action': 'uninstall_products', 'method': 'post', 'class': 'float-end', }
_static_4501608176 = {'class': 'list-group-item mt-2 pb-3', }
_static_4501610480 = {'class': 'configlets list-group list-group-flush', }
_static_4501608512 = {'class': 'card-header', }
_static_4500074560 = {'id': 'activated-products', 'class': 'card mb-4', }
_static_4501612064 = {'class': 'alert alert-warning mt-2 mb-0', 'role': 'status', }
_static_4500065824 = {'class': 'discreet', }
_static_4500077488 = {'class': 'configletDescription discreet', }
_static_4500064720 = {'class': 'btn btn-sm btn-primary', 'type': 'submit', 'value': 'Install', 'name': 'form.submitted', }
_static_4500066064 = {'type': 'hidden', 'name': 'install_product', 'value': 'pid', }
_static_4500075136 = {'action': 'install_products', 'method': 'post', 'class': 'float-end', }
_static_4501387008 = {'class': 'list-group-item mt-2 pb-3', }
_static_4501381968 = {'class': 'configlets list-group list-group-flush', }
_static_4501384896 = {'class': 'card-header', }
_static_4501378944 = {'id': 'install-products', 'class': 'card mb-4', }
_static_4501380432 = {'class': 'btn btn-primary', 'type': 'submit', 'value': 'Upgrade them ALL!', 'name': 'form.submitted', }
_static_4501382928 = {'type': 'hidden', 'value': 'product', 'name': 'prefs_reinstallProducts:list', }
_static_4501382064 = {'action': 'upgrade_products', 'method': 'post', }
_static_4500287360 = {'class': 'list-group-item mt-2 pb-3', }
_static_4501762928 = {'class': 'list-group-item mt-2 pb-3', }
_static_4501764464 = {'class': 'configletDetails list-group list-group-flush', }
_static_4500283616 = {'class': 'discreet', }
_static_4500283184 = {'class': 'configletDescription discreet', }
_static_4500279968 = {'class': 'btn btn-secondary', 'type': 'submit', 'value': 'Upgrade ${pid}', 'name': 'form.submitted', }
_static_4500282992 = {'type': 'hidden', 'name': 'prefs_reinstallProducts:list', 'value': 'pid', }
_static_4500280400 = {'action': 'upgrade_products', 'method': 'post', 'class': 'float-end', }
_static_4500228512 = {'class': 'list-group-item mt-2 pb-3', }
_static_4500241424 = {'class': 'configlets list-group list-group-flush', }
_static_4500228032 = {'id': 'up-to-date-message', 'class': 'alert alert-info m-3 mb-0', 'role': 'status', }
_static_4500236960 = {'class': 'card-header', }
_static_4443607136 = __C2ZContextWrapper
_static_4443408704 = __compile_zt_expr
_static_4500226976 = {'id': 'upgrade-products', 'class': 'card mb-4', }
_static_4500241376 = {'id': 'content-core', }
_static_4500228368 = {'href': 'http://docs.plone.org/manage/installing/installing_addons.html', }
_static_4500234992 = {'class': 'discreet', }
_static_4497895920 = {'class': 'lead', }
_static_4497892704 = {'class': 'documentFirstHeading', }
_static_4501719408 = 'master'
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

            # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501724352
            __attrs_4501724352 = _static_4443296608
            __backup_macroname_4491874176 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x10c52c970> name=None at 10c52c9a0> -> __value
            __value = _static_4501719408
            econtext['macroname'] = __value

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501725792
                __attrs_4501725792 = _static_4443296608
                __previous_i18n_domain_4501722144 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4498144272
                __attrs_4498144272 = _static_4443296608

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n\n    ')

                # <Static value=<ast.Dict object at 0x10c186560> name=None at 10c1878e0> -> __attrs_4497898512
                __attrs_4497898512 = _static_4497892704

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">')
                __stream_4497883584 = []
                __append_4497883584 = __stream_4497883584.append
                __append_4497883584('Add-ons')
                __msgid_4497883584 = __re_whitespace(''.join(__stream_4497883584)).strip()
                if __msgid_4497883584:
                    __append(translate(__msgid_4497883584, mapping=None, default=__msgid_4497883584, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n\n    ')

                # <Static value=<ast.Dict object at 0x10c1871f0> name=None at 10c187be0> -> __attrs_4497885312
                __attrs_4497885312 = _static_4497895920

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="lead">')
                __stream_4497885024 = []
                __append_4497885024 = __stream_4497885024.append
                __append_4497885024('\n      This is the Add-on configuration section, you can activate and deactivate\n      add-ons in the lists below.\n    ')
                __msgid_4497885024 = __re_whitespace(''.join(__stream_4497885024)).strip()
                if __msgid_4497885024:
                    __append(translate(__msgid_4497885024, mapping=None, default=__msgid_4497885024, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n    ')

                # <Static value=<ast.Dict object at 0x10c3c22f0> name=None at 10c3c26e0> -> __attrs_4500239456
                __attrs_4500239456 = _static_4500234992

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="discreet">')
                __stream_4495011712_third_party_product = ''
                __stream_4500227168 = []
                __append_4500227168 = __stream_4500227168.append
                __append_4500227168('\n      To make new add-ons show up here, add them to your buildout\n      configuration, run buildout, and restart the server process.\n      For detailed instructions see\n      ')
                __stream_4495011712_third_party_product = []
                __append_4495011712_third_party_product = __stream_4495011712_third_party_product.append

                # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500236336
                __attrs_4500236336 = _static_4443296608

                # <span ... (0:0)
                # --------------------------------------------------------
                __append_4495011712_third_party_product('<span>\n      ')

                # <Static value=<ast.Dict object at 0x10c3c0910> name=None at 10c3c1180> -> __attrs_4500227024
                __attrs_4500227024 = _static_4500228368

                # <a ... (0:0)
                # --------------------------------------------------------
                __append_4495011712_third_party_product('<a href="http://docs.plone.org/manage/installing/installing_addons.html">')
                __stream_4500230144 = []
                __append_4500230144 = __stream_4500230144.append
                __append_4500230144('\n        Installing a third party add-on\n      ')
                __msgid_4500230144 = __re_whitespace(''.join(__stream_4500230144)).strip()
                if __msgid_4500230144:
                    __append_4495011712_third_party_product(translate(__msgid_4500230144, mapping=None, default=__msgid_4500230144, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append_4495011712_third_party_product('</a>\n      </span>')
                __append_4500227168('${third_party_product}')
                __stream_4495011712_third_party_product = ''.join(__stream_4495011712_third_party_product)
                __append_4500227168('.\n    ')
                __msgid_4500227168 = __re_whitespace(''.join(__stream_4500227168)).strip()
                if __msgid_4500227168:
                    __append(translate(__msgid_4500227168, mapping={'third_party_product': __stream_4495011712_third_party_product, }, default=__msgid_4500227168, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n  </header>\n  ')

                # <Static value=<ast.Dict object at 0x10c3c3be0> name=None at 10c3c2fb0> -> __attrs_4500239504
                __attrs_4500239504 = _static_4500241376

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n\n\n      ')

                # <Static value=<ast.Dict object at 0x10c3c03a0> name=None at 10c3c1750> -> __attrs_4500232640
                __attrs_4500232640 = _static_4500226976
                __backup_products_4501724784 = get('products', __marker)

                # <Value 'view/get_upgrades' (35:36)> -> __value
                __token = 1150
                try:
                    __zt_tmp = __attrs_4500232640
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4443408704('path', 'view/get_upgrades', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_4497892944 = get('num_products', __marker)

                # <Value 'python:len(products)' (36:39)> -> __value
                __token = 1208
                try:
                    __zt_tmp = __attrs_4500232640
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4443408704('python', 'len(products)', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="upgrade-products" class="card mb-4">\n        ')

                # <Static value=<ast.Dict object at 0x10c3c2aa0> name=None at 10c3c1390> -> __attrs_4500240560
                __attrs_4500240560 = _static_4500236960

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="card-header">')
                __stream_4500240704 = []
                __append_4500240704 = __stream_4500240704.append
                __append_4500240704('Upgrades')
                __msgid_4500240704 = __re_whitespace(''.join(__stream_4500240704)).strip()
                if __msgid_4500240704:
                    __append(translate(__msgid_4500240704, mapping=None, default=__msgid_4500240704, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n          ')

                # <Static value=<ast.Dict object at 0x10c3c07c0> name=None at 10c3c1de0> -> __attrs_4500234416
                __attrs_4500234416 = _static_4500228032

                # <Value 'not:products' (39:30)> -> __condition
                __token = 1386
                try:
                    __zt_tmp = __attrs_4500234416
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4443408704('not', 'products', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="up-to-date-message" class="alert alert-info m-3 mb-0" role="status">\n            ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500230864
                    __attrs_4500230864 = _static_4443296608

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_4500231152 = []
                    __append_4500231152 = __stream_4500231152.append
                    __append_4500231152('No upgrades in this corner.')
                    __msgid_4500231152 = __re_whitespace(''.join(__stream_4500231152)).strip()
                    if __msgid_4500231152:
                        __append(translate(__msgid_4500231152, mapping=None, default=__msgid_4500231152, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n            ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500233120
                    __attrs_4500233120 = _static_4443296608

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_4500237728 = []
                    __append_4500237728 = __stream_4500237728.append
                    __append_4500237728('You are up to date. High fives.')
                    __msgid_4500237728 = __re_whitespace(''.join(__stream_4500237728)).strip()
                    if __msgid_4500237728:
                        __append(translate(__msgid_4500237728, mapping=None, default=__msgid_4500237728, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n          </div>')
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x10c3c3c10> name=None at 10c3c2d10> -> __attrs_4500227984
                __attrs_4500227984 = _static_4500241424

                # <Value 'products' (43:27)> -> __condition
                __token = 1667
                try:
                    __zt_tmp = __attrs_4500227984
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4443408704('path', 'products', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                if __condition:

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="configlets list-group list-group-flush">\n          ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500228320
                    __attrs_4500228320 = _static_4443296608
                    __backup_product_4500229328 = get('product', __marker)

                    # <Value 'products' (45:44)> -> __iterator
                    __token = 1781
                    try:
                        __zt_tmp = __attrs_4500228320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_4443408704('path', 'products', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                    (__iterator, ____index_4500235424, ) = getname('repeat')('product', __iterator)
                    econtext['product'] = None
                    for __item in __iterator:
                        econtext['product'] = __item
                        __append('\n          ')

                        # <Static value=<ast.Dict object at 0x10c3c09a0> name=None at 10c3c2e60> -> __attrs_4500289088
                        __attrs_4500289088 = _static_4500228512
                        __backup_pid_4500238928 = get('pid', __marker)

                        # <Value 'product/id' (46:30)> -> __value
                        __token = 1822
                        try:
                            __zt_tmp = __attrs_4500289088
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4443408704('path', 'product/id', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                        econtext['pid'] = __value

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="list-group-item mt-2 pb-3">\n            ')

                        # <Static value=<ast.Dict object at 0x10c3cd450> name=None at 10c3cce50> -> __attrs_4500276320
                        __attrs_4500276320 = _static_4500280400

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append('<form action="upgrade_products" method="post" class="float-end">\n              ')

                        # <Static value=<ast.Dict object at 0x10c3cde70> name=None at 10c3cd8a0> -> __attrs_4500290240
                        __attrs_4500290240 = _static_4500282992

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="hidden" name="prefs_reinstallProducts:list"')

                        # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4500275792
                        __default_4500275792 = _DEFAULT_MARKER

                        # <Substitution 'pid' (50:44)> -> __attr_value
                        __token = 2084
                        try:
                            __zt_tmp = __attrs_4500290240
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_4443408704('path', 'pid', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' />\n              ')

                        # <Static value=<ast.Dict object at 0x10c3cd2a0> name=None at 10c3cd300> -> __attrs_4500286112
                        __attrs_4500286112 = _static_4500279968

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-secondary" type="submit"')

                        # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4500282032
                        __default_4500282032 = _DEFAULT_MARKER

                        # <Translate msgid=None node=<Substitution 'string:Upgrade ${pid}' (56:44)> at 10c3cda50> -> __attr_value

                        # <Substitution 'string:Upgrade ${pid}' (56:44)> -> __attr_value
                        __token = 2355
                        try:
                            __zt_tmp = __attrs_4500286112
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_4443408704('string', 'Upgrade ${pid}', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', 'Upgrade ${pid}', _DEFAULT_MARKER)
                        __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' name="form.submitted"/>\n            </form>\n            ')

                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500277472
                        __attrs_4500277472 = _static_4443296608

                        # <h3 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h3>\n              ')

                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500287744
                        __attrs_4500287744 = _static_4443296608

                        # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4500287936
                        __default_4500287936 = _DEFAULT_MARKER

                        # <Value 'product/title' (59:33)> -> __cache_4500287648
                        __token = 2451
                        try:
                            __zt_tmp = __attrs_4500287744
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4500287648 = _static_4443408704('path', 'product/title', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/title' (59:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10c3cd990> -> __condition
                        __expression = __cache_4500287648

                        # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>\n                Add-on Name\n              </span>')
                        else:
                            __content = __cache_4500287648
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n            </h3>\n            ')

                        # <Static value=<ast.Dict object at 0x10c3cdf30> name=None at 10c3cf940> -> __attrs_4500289184
                        __attrs_4500289184 = _static_4500283184

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="configletDescription discreet">\n              ')

                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500283568
                        __attrs_4500283568 = _static_4443296608

                        # <Value 'product/description' (64:39)> -> __condition
                        __token = 2648
                        try:
                            __zt_tmp = __attrs_4500283568
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4443408704('path', 'product/description', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                        if __condition:

                            # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4500276752
                            __default_4500276752 = _DEFAULT_MARKER

                            # <Value 'product/description' (64:73)> -> __cache_4500289808
                            __token = 2682
                            try:
                                __zt_tmp = __attrs_4500283568
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4500289808 = _static_4443408704('path', 'product/description', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                            # <BinOp left=<Value 'product/description' (64:73)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10c3cf670> -> __condition
                            __expression = __cache_4500289808

                            # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append('add-on description')
                            else:
                                __content = __cache_4500289808
                                __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                        __append('\n              ')

                        # <Static value=<ast.Dict object at 0x10c3ce0e0> name=None at 10c3ccf70> -> __attrs_4500281840
                        __attrs_4500281840 = _static_4500283616

                        # <em ... (0:0)
                        # --------------------------------------------------------
                        __append('<em class="discreet"> – (')

                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500291440
                        __attrs_4500291440 = _static_4443296608

                        # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4500286064
                        __default_4500286064 = _DEFAULT_MARKER

                        # <Value 'pid' (65:58)> -> __cache_4500286592
                        __token = 2809
                        try:
                            __zt_tmp = __attrs_4500291440
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4500286592 = _static_4443408704('path', 'pid', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                        # <BinOp left=<Value 'pid' (65:58)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10c3cc070> -> __condition
                        __expression = __cache_4500286592

                        # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>plugin.app.name</span>')
                        else:
                            __content = __cache_4500286592
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(' ')

                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501754192
                        __attrs_4501754192 = _static_4443296608

                        # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4501760864
                        __default_4501760864 = _DEFAULT_MARKER

                        # <Value 'product/version' (65:105)> -> __cache_4501752848
                        __token = 2856
                        try:
                            __zt_tmp = __attrs_4501754192
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4501752848 = _static_4443408704('path', 'product/version', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/version' (65:105)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10c537a00> -> __condition
                        __expression = __cache_4501752848

                        # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>1.0</span>')
                        else:
                            __content = __cache_4501752848
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(')</em>\n            </div>\n            ')

                        # <Static value=<ast.Dict object at 0x10c537970> name=None at 10c535bd0> -> __attrs_4501765424
                        __attrs_4501765424 = _static_4501764464

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append('<ul class="configletDetails list-group list-group-flush">\n              ')

                        # <Static value=<ast.Dict object at 0x10c537370> name=None at 10c534f70> -> __attrs_4501765952
                        __attrs_4501765952 = _static_4501762928
                        __backup_upgrade_info_4500285008 = get('upgrade_info', __marker)

                        # <Value 'product/upgrade_info' (68:43)> -> __value
                        __token = 3022
                        try:
                            __zt_tmp = __attrs_4501765952
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4443408704('path', 'product/upgrade_info', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                        econtext['upgrade_info'] = __value

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="list-group-item mt-2 pb-3">\n                  ')

                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501765760
                        __attrs_4501765760 = _static_4443296608

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')
                        __stream_4501753376 = []
                        __append_4501753376 = __stream_4501753376.append
                        __append_4501753376('\n                    This addon has been upgraded.\n                  ')
                        __msgid_4501753376 = __re_whitespace(''.join(__stream_4501753376)).strip()
                        if __msgid_4501753376:
                            __append(translate(__msgid_4501753376, mapping=None, default=__msgid_4501753376, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n                  ')

                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501754144
                        __attrs_4501754144 = _static_4443296608

                        # <Value 'not:upgrade_info/hasProfile' (72:39)> -> __condition
                        __token = 3237
                        try:
                            __zt_tmp = __attrs_4501754144
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4443408704('not', 'upgrade_info/hasProfile', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>')
                            __stream_4490274048_version = ''
                            __stream_4501754720 = []
                            __append_4501754720 = __stream_4501754720.append
                            __append_4501754720('\n                    Old version was ')
                            __stream_4490274048_version = []
                            __append_4490274048_version = __stream_4490274048_version.append

                            # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501751504
                            __attrs_4501751504 = _static_4443296608

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append_4490274048_version('<strong>')

                            # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4501755440
                            __default_4501755440 = _DEFAULT_MARKER

                            # <Value 'upgrade_info/installedVersion' (74:77)> -> __cache_4501762352
                            __token = 3419
                            try:
                                __zt_tmp = __attrs_4501751504
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4501762352 = _static_4443408704('path', 'upgrade_info/installedVersion', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                            # <BinOp left=<Value 'upgrade_info/installedVersion' (74:77)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10c535db0> -> __condition
                            __expression = __cache_4501762352

                            # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append_4490274048_version('version')
                            else:
                                __content = __cache_4501762352
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append_4490274048_version(__content)
                            __append_4490274048_version('</strong>')
                            __append_4501754720('${version}')
                            __stream_4490274048_version = ''.join(__stream_4490274048_version)
                            __append_4501754720('.\n                  ')
                            __msgid_4501754720 = __re_whitespace(''.join(__stream_4501754720)).strip()
                            if 'label_product_upgrade_old_version':
                                __append(translate('label_product_upgrade_old_version', mapping={'version': __stream_4490274048_version, }, default=__msgid_4501754720, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</span>')
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501757024
                        __attrs_4501757024 = _static_4443296608

                        # <Value 'upgrade_info/hasProfile' (76:39)> -> __condition
                        __token = 3533
                        try:
                            __zt_tmp = __attrs_4501757024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4443408704('path', 'upgrade_info/hasProfile', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>\n                    ')

                            # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501756160
                            __attrs_4501756160 = _static_4443296608
                            __stream_4490424192_version = ''
                            __stream_4501763552 = []
                            __append_4501763552 = __stream_4501763552.append
                            __append_4501763552('\n                      Old profile version was ')
                            __stream_4490424192_version = []
                            __append_4490424192_version = __stream_4490424192_version.append

                            # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501749920
                            __attrs_4501749920 = _static_4443296608

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append_4490424192_version('<strong>')

                            # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4501764896
                            __default_4501764896 = _DEFAULT_MARKER

                            # <Value 'upgrade_info/installedVersion' (78:87)> -> __cache_4501751648
                            __token = 3736
                            try:
                                __zt_tmp = __attrs_4501749920
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4501751648 = _static_4443408704('path', 'upgrade_info/installedVersion', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                            # <BinOp left=<Value 'upgrade_info/installedVersion' (78:87)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10c534a30> -> __condition
                            __expression = __cache_4501751648

                            # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append_4490424192_version('version')
                            else:
                                __content = __cache_4501751648
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append_4490424192_version(__content)
                            __append_4490424192_version('</strong>')
                            __append_4501763552('${version}')
                            __stream_4490424192_version = ''.join(__stream_4490424192_version)
                            __append_4501763552('.\n                    ')
                            __msgid_4501763552 = __re_whitespace(''.join(__stream_4501763552)).strip()
                            if 'label_product_upgrade_old_profile_version':
                                __append(translate('label_product_upgrade_old_profile_version', mapping={'version': __stream_4490424192_version, }, default=__msgid_4501763552, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('\n                    ')

                            # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501758992
                            __attrs_4501758992 = _static_4443296608
                            __stream_4490424192_version = ''
                            __stream_4501761536 = []
                            __append_4501761536 = __stream_4501761536.append
                            __append_4501761536('\n                      New profile version is ')
                            __stream_4490424192_version = []
                            __append_4490424192_version = __stream_4490424192_version.append

                            # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501752512
                            __attrs_4501752512 = _static_4443296608

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append_4490424192_version('<strong>')

                            # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4501760816
                            __default_4501760816 = _DEFAULT_MARKER

                            # <Value 'upgrade_info/newVersion' (81:86)> -> __cache_4501753856
                            __token = 3993
                            try:
                                __zt_tmp = __attrs_4501752512
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4501753856 = _static_4443408704('path', 'upgrade_info/newVersion', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                            # <BinOp left=<Value 'upgrade_info/newVersion' (81:86)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10c5373d0> -> __condition
                            __expression = __cache_4501753856

                            # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append_4490424192_version('version')
                            else:
                                __content = __cache_4501753856
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append_4490424192_version(__content)
                            __append_4490424192_version('</strong>')
                            __append_4501761536('${version}')
                            __stream_4490424192_version = ''.join(__stream_4490424192_version)
                            __append_4501761536('.\n                    ')
                            __msgid_4501761536 = __re_whitespace(''.join(__stream_4501761536)).strip()
                            if 'label_product_upgrade_new_profile_version':
                                __append(translate('label_product_upgrade_new_profile_version', mapping={'version': __stream_4490424192_version, }, default=__msgid_4501761536, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('\n                  </span>')
                        __append('\n\n                  ')

                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501758608
                        __attrs_4501758608 = _static_4443296608

                        # <Value 'not:upgrade_info/available' (85:38)> -> __condition
                        __token = 4133
                        try:
                            __zt_tmp = __attrs_4501758608
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4443408704('not', 'upgrade_info/available', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div>\n                    ')

                            # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501384272
                            __attrs_4501384272 = _static_4443296608

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append('<strong>')
                            __stream_4501379568 = []
                            __append_4501379568 = __stream_4501379568.append
                            __append_4501379568('Warning')
                            __msgid_4501379568 = __re_whitespace(''.join(__stream_4501379568)).strip()
                            if __msgid_4501379568:
                                __append(translate(__msgid_4501379568, mapping=None, default=__msgid_4501379568, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</strong>\n                    ')

                            # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501379856
                            __attrs_4501379856 = _static_4443296608

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>')
                            __stream_4501376736 = []
                            __append_4501376736 = __stream_4501376736.append
                            __append_4501376736('There is no upgrade procedure defined for this\n                    addon. Please consult the addon documentation\n                    for upgrade information, or contact the addon\n                    author.')
                            __msgid_4501376736 = __re_whitespace(''.join(__stream_4501376736)).strip()
                            if __msgid_4501376736:
                                __append(translate(__msgid_4501376736, mapping=None, default=__msgid_4501376736, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</span>\n                  </div>')
                        __append('\n              </li>')
                        if (__backup_upgrade_info_4500285008 is __marker):
                            del econtext['upgrade_info']
                        else:
                            econtext['upgrade_info'] = __backup_upgrade_info_4500285008
                        __append('\n            </ul>\n          </li>')
                        if (__backup_pid_4500238928 is __marker):
                            del econtext['pid']
                        else:
                            econtext['pid'] = __backup_pid_4500238928
                        __append('\n          ')
                        ____index_4500235424 -= 1
                        if (____index_4500235424 > 0):
                            __append('')
                    if (__backup_product_4500229328 is __marker):
                        del econtext['product']
                    else:
                        econtext['product'] = __backup_product_4500229328
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x10c3cef80> name=None at 10c3cc6d0> -> __attrs_4501374048
                    __attrs_4501374048 = _static_4500287360

                    # <Value 'python:num_products > 1' (96:29)> -> __condition
                    __token = 4617
                    try:
                        __zt_tmp = __attrs_4501374048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4443408704('python', 'num_products > 1', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="list-group-item mt-2 pb-3">\n            ')

                        # <Static value=<ast.Dict object at 0x10c4da3b0> name=None at 10c4d9060> -> __attrs_4501380672
                        __attrs_4501380672 = _static_4501382064

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append('<form action="upgrade_products" method="post">\n                ')

                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501384464
                        __attrs_4501384464 = _static_4443296608
                        __backup_product_4500284288 = get('product', __marker)

                        # <Value 'products' (98:51)> -> __iterator
                        __token = 4787
                        try:
                            __zt_tmp = __attrs_4501384464
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_4443408704('path', 'products', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                        (__iterator, ____index_4501373136, ) = getname('repeat')('product', __iterator)
                        econtext['product'] = None
                        for __item in __iterator:
                            econtext['product'] = __item
                            __append('\n                ')

                            # <Static value=<ast.Dict object at 0x10c4da710> name=None at 10c4dae00> -> __attrs_4501380816
                            __attrs_4501380816 = _static_4501382928

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input type="hidden"')

                            # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4501384608
                            __default_4501384608 = _DEFAULT_MARKER

                            # <Substitution 'product/id' (101:44)> -> __attr_value
                            __token = 4953
                            try:
                                __zt_tmp = __attrs_4501380816
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_4443408704('path', 'product/id', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', 'product', _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))
                            __append(' name="prefs_reinstallProducts:list" />\n                ')
                            ____index_4501373136 -= 1
                            if (____index_4501373136 > 0):
                                __append('')
                        if (__backup_product_4500284288 is __marker):
                            del econtext['product']
                        else:
                            econtext['product'] = __backup_product_4500284288
                        __append('\n                ')

                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501389216
                        __attrs_4501389216 = _static_4443296608

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>\n                  ')

                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501379184
                        __attrs_4501379184 = _static_4443296608

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div>')
                        __stream_4501373232 = []
                        __append_4501373232 = __stream_4501373232.append
                        __append_4501373232('This can be risky, are you sure you want to do this?')
                        __msgid_4501373232 = __re_whitespace(''.join(__stream_4501373232)).strip()
                        if 'label_product_upgrade_all_action':
                            __append(translate('label_product_upgrade_all_action', mapping=None, default=__msgid_4501373232, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</div>\n                  ')

                        # <Static value=<ast.Dict object at 0x10c4d9d50> name=None at 10c4d9330> -> __attrs_4501385568
                        __attrs_4501385568 = _static_4501380432

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary" type="submit"')

                        # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4501377888
                        __default_4501377888 = _DEFAULT_MARKER

                        # <Translate msgid=None node=<ast.Constant object at 0x10c4d9150> at 10c4d9fc0> -> __attr_value
                        __attr_value = 'Upgrade them ALL!'
                        __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' name="form.submitted" />\n                </span>\n            </form>\n            </li>')
                    __append('\n          </ul>')
                __append('\n      </section>')
                if (__backup_num_products_4497892944 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_4497892944
                if (__backup_products_4501724784 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_4501724784
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x10c4d9780> name=None at 10c4d83d0> -> __attrs_4501380384
                __attrs_4501380384 = _static_4501378944
                __backup_products_4501718544 = get('products', __marker)

                # <Value 'view/get_available' (116:36)> -> __value
                __token = 5522
                try:
                    __zt_tmp = __attrs_4501380384
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4443408704('path', 'view/get_available', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_4497888384 = get('num_products', __marker)

                # <Value 'python:len(products)' (117:36)> -> __value
                __token = 5578
                try:
                    __zt_tmp = __attrs_4501380384
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4443408704('python', 'len(products)', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="install-products" class="card mb-4">\n        ')

                # <Static value=<ast.Dict object at 0x10c4daec0> name=None at 10c4da6b0> -> __attrs_4501378368
                __attrs_4501378368 = _static_4501384896

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="card-header">')
                __stream_4501378560 = []
                __append_4501378560 = __stream_4501378560.append
                __append_4501378560('Available add-ons')
                __msgid_4501378560 = __re_whitespace(''.join(__stream_4501378560)).strip()
                if __msgid_4501378560:
                    __append(translate(__msgid_4501378560, mapping=None, default=__msgid_4501378560, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n        ')

                # <Static value=<ast.Dict object at 0x10c4da350> name=None at 10c4d8190> -> __attrs_4501381440
                __attrs_4501381440 = _static_4501381968

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="configlets list-group list-group-flush">\n          ')

                # <Static value=<ast.Dict object at 0x10c4db700> name=None at 10c4d9e10> -> __attrs_4500072400
                __attrs_4500072400 = _static_4501387008
                __backup_product_4500228080 = get('product', __marker)

                # <Value 'products' (121:34)> -> __iterator
                __token = 5829
                try:
                    __zt_tmp = __attrs_4500072400
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4443408704('path', 'products', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                (__iterator, ____index_4500076000, ) = getname('repeat')('product', __iterator)
                econtext['product'] = None
                for __item in __iterator:
                    econtext['product'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="list-group-item mt-2 pb-3">\n          ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500065056
                    __attrs_4500065056 = _static_4443296608
                    __backup_pid_4500284384 = get('pid', __marker)

                    # <Value 'product/id' (122:35)> -> __value
                    __token = 5909
                    try:
                        __zt_tmp = __attrs_4500065056
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4443408704('path', 'product/id', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                    econtext['pid'] = __value
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x10c39b280> name=None at 10c39a530> -> __attrs_4500065392
                    __attrs_4500065392 = _static_4500075136

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form action="install_products" method="post" class="float-end">\n                ')

                    # <Static value=<ast.Dict object at 0x10c398f10> name=None at 10c399000> -> __attrs_4500073264
                    __attrs_4500073264 = _static_4500066064

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="hidden" name="install_product"')

                    # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4500068416
                    __default_4500068416 = _DEFAULT_MARKER

                    # <Substitution 'pid' (126:46)> -> __attr_value
                    __token = 6129
                    try:
                        __zt_tmp = __attrs_4500073264
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_4443408704('path', 'pid', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n                ')

                    # <Static value=<ast.Dict object at 0x10c3989d0> name=None at 10c39a4d0> -> __attrs_4500073984
                    __attrs_4500073984 = _static_4500064720

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="btn btn-sm btn-primary" type="submit" value="Install" name="form.submitted">')
                    __stream_4500073024 = []
                    __append_4500073024 = __stream_4500073024.append
                    __append_4500073024('\n                    Install\n                ')
                    __msgid_4500073024 = __re_whitespace(''.join(__stream_4500073024)).strip()
                    if __msgid_4500073024:
                        __append(translate(__msgid_4500073024, mapping=None, default=__msgid_4500073024, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n            </form>\n\n            ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500068320
                    __attrs_4500068320 = _static_4443296608

                    # <h3 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h3>\n              ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500077200
                    __attrs_4500077200 = _static_4443296608

                    # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4500075616
                    __default_4500075616 = _DEFAULT_MARKER

                    # <Value 'product/title' (137:33)> -> __cache_4500069520
                    __token = 6485
                    try:
                        __zt_tmp = __attrs_4500077200
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4500069520 = _static_4443408704('path', 'product/title', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                    # <BinOp left=<Value 'product/title' (137:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10c39b550> -> __condition
                    __expression = __cache_4500069520

                    # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>\n                Add-on Name\n              </span>')
                    else:
                        __content = __cache_4500069520
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n            </h3>\n            ')

                    # <Static value=<ast.Dict object at 0x10c39bbb0> name=None at 10c39bfa0> -> __attrs_4500078208
                    __attrs_4500078208 = _static_4500077488

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="configletDescription discreet">\n              ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500078400
                    __attrs_4500078400 = _static_4443296608

                    # <Value 'product/description' (142:39)> -> __condition
                    __token = 6682
                    try:
                        __zt_tmp = __attrs_4500078400
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4443408704('path', 'product/description', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4500069616
                        __default_4500069616 = _DEFAULT_MARKER

                        # <Value 'product/description' (144:29)> -> __cache_4500068032
                        __token = 6766
                        try:
                            __zt_tmp = __attrs_4500078400
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4500068032 = _static_4443408704('path', 'product/description', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/description' (144:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10c399db0> -> __condition
                        __expression = __cache_4500068032

                        # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('add-on description')
                        else:
                            __content = __cache_4500068032
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    __append('\n              ')

                    # <Static value=<ast.Dict object at 0x10c398e20> name=None at 10c398fd0> -> __attrs_4500076144
                    __attrs_4500076144 = _static_4500065824

                    # <em ... (0:0)
                    # --------------------------------------------------------
                    __append('<em class="discreet"> – (')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4500069184
                    __attrs_4500069184 = _static_4443296608

                    # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4500076720
                    __default_4500076720 = _DEFAULT_MARKER

                    # <Value 'pid' (145:58)> -> __cache_4500063040
                    __token = 6875
                    try:
                        __zt_tmp = __attrs_4500069184
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4500063040 = _static_4443408704('path', 'pid', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                    # <BinOp left=<Value 'pid' (145:58)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10c399d20> -> __condition
                    __expression = __cache_4500063040

                    # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>plugin.app.name</span>')
                    else:
                        __content = __cache_4500063040
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(' ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501612784
                    __attrs_4501612784 = _static_4443296608

                    # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4501604912
                    __default_4501604912 = _DEFAULT_MARKER

                    # <Value 'product/version' (145:105)> -> __cache_4501610240
                    __token = 6922
                    try:
                        __zt_tmp = __attrs_4501612784
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4501610240 = _static_4443408704('path', 'product/version', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                    # <BinOp left=<Value 'product/version' (145:105)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10c512140> -> __condition
                    __expression = __cache_4501610240

                    # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>1.0</span>')
                    else:
                        __content = __cache_4501610240
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(')</em>\n            </div>\n            ')

                    # <Static value=<ast.Dict object at 0x10c512620> name=None at 10c513070> -> __attrs_4501612976
                    __attrs_4501612976 = _static_4501612064

                    # <Value 'not:product/uninstall_profile' (149:31)> -> __condition
                    __token = 7091
                    try:
                        __zt_tmp = __attrs_4501612976
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4443408704('not', 'product/uninstall_profile', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="alert alert-warning mt-2 mb-0" role="status">\n              ')

                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501606256
                        __attrs_4501606256 = _static_4443296608

                        # <strong ... (0:0)
                        # --------------------------------------------------------
                        __append('<strong>')
                        __stream_4501617152 = []
                        __append_4501617152 = __stream_4501617152.append
                        __append_4501617152('Warning')
                        __msgid_4501617152 = __re_whitespace(''.join(__stream_4501617152)).strip()
                        if __msgid_4501617152:
                            __append(translate(__msgid_4501617152, mapping=None, default=__msgid_4501617152, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</strong>\n              ')

                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501607744
                        __attrs_4501607744 = _static_4443296608

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')
                        __stream_4501605728 = []
                        __append_4501605728 = __stream_4501605728.append
                        __append_4501605728('This product cannot be uninstalled!')
                        __msgid_4501605728 = __re_whitespace(''.join(__stream_4501605728)).strip()
                        if __msgid_4501605728:
                            __append(translate(__msgid_4501605728, mapping=None, default=__msgid_4501605728, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n            </div>')
                    __append('\n          ')
                    if (__backup_pid_4500284384 is __marker):
                        del econtext['pid']
                    else:
                        econtext['pid'] = __backup_pid_4500284384
                    __append('\n          </li>')
                    ____index_4500076000 -= 1
                    if (____index_4500076000 > 0):
                        __append('\n          ')
                if (__backup_product_4500228080 is __marker):
                    del econtext['product']
                else:
                    econtext['product'] = __backup_product_4500228080
                __append('\n        </ul>\n      </section>')
                if (__backup_num_products_4497888384 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_4497888384
                if (__backup_products_4501718544 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_4501718544
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x10c39b040> name=None at 10c398490> -> __attrs_4501611296
                __attrs_4501611296 = _static_4500074560
                __backup_products_4500227840 = get('products', __marker)

                # <Value 'view/get_installed' (158:36)> -> __value
                __token = 7389
                try:
                    __zt_tmp = __attrs_4501611296
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4443408704('path', 'view/get_installed', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_4500240944 = get('num_products', __marker)

                # <Value 'python:len(products)' (159:39)> -> __value
                __token = 7448
                try:
                    __zt_tmp = __attrs_4501611296
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4443408704('python', 'len(products)', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="activated-products" class="card mb-4">\n        ')

                # <Static value=<ast.Dict object at 0x10c511840> name=None at 10c511b10> -> __attrs_4501603568
                __attrs_4501603568 = _static_4501608512

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="card-header">')
                __stream_4501609664 = []
                __append_4501609664 = __stream_4501609664.append
                __append_4501609664('Activated add-ons')
                __msgid_4501609664 = __re_whitespace(''.join(__stream_4501609664)).strip()
                if __msgid_4501609664:
                    __append(translate(__msgid_4501609664, mapping=None, default=__msgid_4501609664, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n        ')

                # <Static value=<ast.Dict object at 0x10c511ff0> name=None at 10c511f90> -> __attrs_4501609280
                __attrs_4501609280 = _static_4501610480

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="configlets list-group list-group-flush">\n          ')

                # <Static value=<ast.Dict object at 0x10c5116f0> name=None at 10c512dd0> -> __attrs_4501618208
                __attrs_4501618208 = _static_4501608176
                __backup_product_4501761200 = get('product', __marker)

                # <Value 'products' (163:34)> -> __iterator
                __token = 7701
                try:
                    __zt_tmp = __attrs_4501618208
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4443408704('path', 'products', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                (__iterator, ____index_4501605920, ) = getname('repeat')('product', __iterator)
                econtext['product'] = None
                for __item in __iterator:
                    econtext['product'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="list-group-item mt-2 pb-3">\n          ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4501604864
                    __attrs_4501604864 = _static_4443296608
                    __backup_pid_4500288416 = get('pid', __marker)

                    # <Value 'product/id' (164:35)> -> __value
                    __token = 7781
                    try:
                        __zt_tmp = __attrs_4501604864
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4443408704('path', 'product/id', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                    econtext['pid'] = __value
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x10c5133a0> name=None at 10c513430> -> __attrs_4501607408
                    __attrs_4501607408 = _static_4501615520

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form action="uninstall_products" method="post" class="float-end">\n              ')

                    # <Static value=<ast.Dict object at 0x10c5123b0> name=None at 10c5127a0> -> __attrs_4501605776
                    __attrs_4501605776 = _static_4501611440

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="hidden" name="uninstall_product"')

                    # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4501612016
                    __default_4501612016 = _DEFAULT_MARKER

                    # <Substitution 'pid' (168:42)> -> __attr_value
                    __token = 7995
                    try:
                        __zt_tmp = __attrs_4501605776
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_4443408704('path', 'pid', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n              ')

                    # <Static value=<ast.Dict object at 0x10c341b70> name=None at 10c340ac0> -> __attrs_4499710416
                    __attrs_4499710416 = _static_4499708784

                    # <Value 'product/uninstall_profile' (173:37)> -> __condition
                    __token = 8213
                    try:
                        __zt_tmp = __attrs_4499710416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4443408704('path', 'product/uninstall_profile', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                    if __condition:

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button class="btn btn-sm btn-danger" type="submit" value="Uninstall" name="form.submitted">')
                        __stream_4499703120 = []
                        __append_4499703120 = __stream_4499703120.append
                        __append_4499703120('\n                Uninstall\n              ')
                        __msgid_4499703120 = __re_whitespace(''.join(__stream_4499703120)).strip()
                        if __msgid_4499703120:
                            __append(translate(__msgid_4499703120, mapping=None, default=__msgid_4499703120, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</button>')
                    __append('\n            </form>\n              ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4499714016
                    __attrs_4499714016 = _static_4443296608

                    # <h3 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h3>\n                ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4499716704
                    __attrs_4499716704 = _static_4443296608

                    # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4499717568
                    __default_4499717568 = _DEFAULT_MARKER

                    # <Value 'product/title' (179:35)> -> __cache_4499708592
                    __token = 8405
                    try:
                        __zt_tmp = __attrs_4499716704
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4499708592 = _static_4443408704('path', 'product/title', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                    # <BinOp left=<Value 'product/title' (179:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10c341ae0> -> __condition
                    __expression = __cache_4499708592

                    # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>\n                  Add-on Name\n                </span>')
                    else:
                        __content = __cache_4499708592
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n              </h3>\n              ')

                    # <Static value=<ast.Dict object at 0x10c343640> name=None at 10c343790> -> __attrs_4499708544
                    __attrs_4499708544 = _static_4499715648

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="configletDescription discreet">\n                ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4499709504
                    __attrs_4499709504 = _static_4443296608

                    # <Value 'product/description' (184:41)> -> __condition
                    __token = 8612
                    try:
                        __zt_tmp = __attrs_4499709504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4443408704('path', 'product/description', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4499717232
                        __default_4499717232 = _DEFAULT_MARKER

                        # <Value 'product/description' (186:31)> -> __cache_4499713104
                        __token = 8700
                        try:
                            __zt_tmp = __attrs_4499709504
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4499713104 = _static_4443408704('path', 'product/description', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/description' (186:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10c342dd0> -> __condition
                        __expression = __cache_4499713104

                        # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('add-on description')
                        else:
                            __content = __cache_4499713104
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x10c343f70> name=None at 10c343040> -> __attrs_4499716032
                    __attrs_4499716032 = _static_4499718000

                    # <em ... (0:0)
                    # --------------------------------------------------------
                    __append('<em class="discreet"> – (')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4499711472
                    __attrs_4499711472 = _static_4443296608

                    # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4499711520
                    __default_4499711520 = _DEFAULT_MARKER

                    # <Value 'pid' (187:60)> -> __cache_4499703168
                    __token = 8811
                    try:
                        __zt_tmp = __attrs_4499711472
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4499703168 = _static_4443408704('path', 'pid', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                    # <BinOp left=<Value 'pid' (187:60)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10c3424d0> -> __condition
                    __expression = __cache_4499703168

                    # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>plugin.app.name</span>')
                    else:
                        __content = __cache_4499703168
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(' ')

                    # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4499707728
                    __attrs_4499707728 = _static_4443296608

                    # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4499707392
                    __default_4499707392 = _DEFAULT_MARKER

                    # <Value 'product/version' (187:107)> -> __cache_4499704464
                    __token = 8858
                    try:
                        __zt_tmp = __attrs_4499707728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4499704464 = _static_4443408704('path', 'product/version', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                    # <BinOp left=<Value 'product/version' (187:107)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10c3420e0> -> __condition
                    __expression = __cache_4499704464

                    # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>1.0</span>')
                    else:
                        __content = __cache_4499704464
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(')</em>\n              </div>\n              ')

                    # <Static value=<ast.Dict object at 0x10c343d90> name=None at 10c343d30> -> __attrs_4499709072
                    __attrs_4499709072 = _static_4499717520

                    # <Value 'not:product/uninstall_profile' (191:33)> -> __condition
                    __token = 9032
                    try:
                        __zt_tmp = __attrs_4499709072
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4443408704('not', 'product/uninstall_profile', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="alert alert-info mt-2 mb-0" role="status">\n                ')

                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4497990864
                        __attrs_4497990864 = _static_4443296608

                        # <strong ... (0:0)
                        # --------------------------------------------------------
                        __append('<strong>')
                        __stream_4499705136 = []
                        __append_4499705136 = __stream_4499705136.append
                        __append_4499705136('Info')
                        __msgid_4499705136 = __re_whitespace(''.join(__stream_4499705136)).strip()
                        if __msgid_4499705136:
                            __append(translate(__msgid_4499705136, mapping=None, default=__msgid_4499705136, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</strong>\n                ')

                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4490662944
                        __attrs_4490662944 = _static_4443296608

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')
                        __stream_4497984672 = []
                        __append_4497984672 = __stream_4497984672.append
                        __append_4497984672('This product cannot be uninstalled!')
                        __msgid_4497984672 = __re_whitespace(''.join(__stream_4497984672)).strip()
                        if __msgid_4497984672:
                            __append(translate(__msgid_4497984672, mapping=None, default=__msgid_4497984672, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n            </div>')
                    __append('\n          ')
                    if (__backup_pid_4500288416 is __marker):
                        del econtext['pid']
                    else:
                        econtext['pid'] = __backup_pid_4500288416
                    __append('\n          </li>')
                    ____index_4501605920 -= 1
                    if (____index_4501605920 > 0):
                        __append('\n          ')
                if (__backup_product_4501761200 is __marker):
                    del econtext['product']
                else:
                    econtext['product'] = __backup_product_4501761200
                __append('\n        </ul>\n      </section>')
                if (__backup_num_products_4500240944 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_4500240944
                if (__backup_products_4500227840 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_4500227840
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x10c512770> name=None at 10c343280> -> __attrs_4490661696
                __attrs_4490661696 = _static_4501612400
                __backup_products_4500227648 = get('products', __marker)

                # <Value 'view/get_broken' (200:36)> -> __value
                __token = 9331
                try:
                    __zt_tmp = __attrs_4490661696
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4443408704('path', 'view/get_broken', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_4500286352 = get('num_products', __marker)

                # <Value 'python:len(products)' (201:40)> -> __value
                __token = 9388
                try:
                    __zt_tmp = __attrs_4490661696
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4443408704('python', 'len(products)', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <Value 'num_products' (202:31)> -> __condition
                __token = 9443
                try:
                    __zt_tmp = __attrs_4490661696
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4443408704('path', 'num_products', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                if __condition:

                    # <section ... (0:0)
                    # --------------------------------------------------------
                    __append('<section id="broken-products" class="card mb-4">\n        ')

                    # <Static value=<ast.Dict object at 0x10c1fc0d0> name=None at 10c1b05b0> -> __attrs_4501726368
                    __attrs_4501726368 = _static_4498374864

                    # <header ... (0:0)
                    # --------------------------------------------------------
                    __append('<header class="card-header">')
                    __stream_4498076768 = []
                    __append_4498076768 = __stream_4498076768.append
                    __append_4498076768('Broken add-ons')
                    __msgid_4498076768 = __re_whitespace(''.join(__stream_4498076768)).strip()
                    if __msgid_4498076768:
                        __append(translate(__msgid_4498076768, mapping=None, default=__msgid_4498076768, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</header>\n        ')

                    # <Static value=<ast.Dict object at 0x10c52c490> name=None at 10c52fc10> -> __attrs_4498383024
                    __attrs_4498383024 = _static_4501718160

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="configlets list-group list-group-flush">\n          ')

                    # <Static value=<ast.Dict object at 0x10c1fd5d0> name=None at 10c1fe3e0> -> __attrs_4498228608
                    __attrs_4498228608 = _static_4498380240
                    __backup_product_4501616240 = get('product', __marker)

                    # <Value 'products' (206:34)> -> __iterator
                    __token = 9685
                    try:
                        __zt_tmp = __attrs_4498228608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_4443408704('path', 'products', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
                    (__iterator, ____index_4487817312, ) = getname('repeat')('product', __iterator)
                    econtext['product'] = None
                    for __item in __iterator:
                        econtext['product'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="list-group-item mt-2 pb-3">\n            ')

                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4498104496
                        __attrs_4498104496 = _static_4443296608

                        # <h3 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h3>\n              ')

                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4498104592
                        __attrs_4498104592 = _static_4443296608

                        # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4498102144
                        __default_4498102144 = _DEFAULT_MARKER

                        # <Value 'product/product_id' (208:33)> -> __cache_4498099696
                        __token = 9780
                        try:
                            __zt_tmp = __attrs_4498104592
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4498099696 = _static_4443408704('path', 'product/product_id', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/product_id' (208:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10c1b9030> -> __condition
                        __expression = __cache_4498099696

                        # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>\n                Add-on Name\n              </span>')
                        else:
                            __content = __cache_4498099696
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n            </h3>\n            ')

                        # <Static value=<ast.Dict object at 0x10c1b9fc0> name=None at 10c1b8190> -> __attrs_4494746784
                        __attrs_4494746784 = _static_4498104256

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="configletDescription discreet">\n              ')

                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4490655776
                        __attrs_4490655776 = _static_4443296608

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')

                        # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4490647952
                        __default_4490647952 = _DEFAULT_MARKER

                        # <Value 'product/type' (213:33)> -> __cache_4353075008
                        __token = 9976
                        try:
                            __zt_tmp = __attrs_4490655776
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4353075008 = _static_4443408704('path', 'product/type', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/type' (213:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10376b9a0> -> __condition
                        __expression = __cache_4353075008

                        # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Error Type')
                        else:
                            __content = __cache_4353075008
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>\n              ')

                        # <Static value=<ast.Dict object at 0x10ba9cf10> name=None at 10ba9ce80> -> __attrs_4490656880
                        __attrs_4490656880 = _static_4490645264

                        # <em ... (0:0)
                        # --------------------------------------------------------
                        __append('<em class="discreet"> - ')

                        # <Static value=<ast.Dict object at 0x108d75360> name=None at 108d76890> -> __attrs_4490642672
                        __attrs_4490642672 = _static_4443296608

                        # <Symbol value=<DEFAULT> at 108d766e0> -> __default_4490653280
                        __default_4490653280 = _DEFAULT_MARKER

                        # <Value 'product/value' (214:61)> -> __cache_4490644976
                        __token = 10087
                        try:
                            __zt_tmp = __attrs_4490642672
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4490644976 = _static_4443408704('path', 'product/value', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/value' (214:61)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 108d766e0> at 10ba9e140> -> __condition
                        __expression = __cache_4490644976

                        # <Symbol value=<DEFAULT> at 108d766e0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Error Reason')
                        else:
                            __content = __cache_4490644976
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</em>\n            </div>\n          </li>')
                        ____index_4487817312 -= 1
                        if (____index_4487817312 > 0):
                            __append('\n          ')
                    if (__backup_product_4501616240 is __marker):
                        del econtext['product']
                    else:
                        econtext['product'] = __backup_product_4501616240
                    __append('\n        </ul>\n      </section>')
                if (__backup_num_products_4500286352 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_4500286352
                if (__backup_products_4500227648 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_4500227648
                __append('\n\n  </div>\n')
                __i18n_domain = __previous_i18n_domain_4501722144
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'context/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_4501724352
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4443408704('path', 'context/prefs_main_template/macros/master', econtext=econtext)(_static_4443607136(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4491874176 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4491874176
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }