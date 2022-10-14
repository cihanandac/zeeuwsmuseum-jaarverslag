# -*- coding: utf-8 -*-
__filename = 'manage_main'

__tokens = {31: ('here/manage_page_header', 1, 31), 89: ('here/manage_tabs', 3, 29), 238: ("python:getattr(here.aq_explicit, 'has_order_support', 0)", 7, 38), 318: (' modules/AccessControl/getSecurityManage', 8, 22), 392: ("t python: 'position' if has_order_support else 'i", 9, 31), 467: ("ey python:request.get('skey',default_so", 10, 22), 532: ("key python:request.get('rkey','a", 11, 21), 594: ("_alt python:'desc' if rkey=='asc' else ", 12, 24), 666: ('lt_up rkey_alt', 13, 26), 705: ('   obs python: here.manage_get_sortedObjects(sortkey = skey, revkey ', 14, 17), 801: (' my_url string:${context/absolute_url}/man', 15, 19), 905: ('string:${request/URL1}/', 17, 31), 962: ('obs', 19, 30), 1057: ('obs', 20, 89), 1120: ("python:'thead-light sorted_%s'%(request.get('rkey',''))", 21, 57), 1550: ('string:Sort ${rkey_alt_up} by meta-type', 29, 39), 1628: (' string:${my_url}?skey=meta_type&rkey=${rkey_alt', 30, 37), 1716: ("s python:skey=='meta_type' and 'zmi-sort_key' or No", 31, 37), 2066: ('string:Sort ${rkey_alt_up} by name', 39, 39), 2139: (' string:${my_url}?skey=id&rkey=${rkey_alt', 40, 37), 2220: ("s python:skey=='id' and 'zmi-sort_key' or No", 41, 37), 2879: ('string:Sort ${rkey_alt_up} by size', 52, 39), 2952: (' string:${my_url}?skey=get_size&rkey=${rkey_alt', 53, 37), 3039: ("s python:skey=='get_size' and 'zmi-sort_key' or No", 54, 37), 3451: ('string:Sort ${rkey_alt_up} by modification date', 63, 39), 3537: (' string:${my_url}?skey=_p_mtime&rkey=${rkey_alt', 64, 37), 3624: ("s python:skey=='_p_mtime' and 'zmi-sort_key' or No", 65, 37), 3906: ('obs', 74, 34), 3944: ('nocall:ob_dict/obj', 75, 32), 4178: ('ob_dict/id', 77, 104), 4519: (' ob/meta_type | defaul', 81, 122), 4491: ('ob/zmi_icon | default', 81, 94), 4598: ('ob/meta_type | default', 82, 53), 4765: ("python:'%s/manage_workspace'%(ob_dict['quoted_id'])", 86, 40), 4856: ('ob_dict/id', 87, 37), 4989: ('ob/wl_isLocked | nothing', 88, 111), 5163: ('ob/title|nothing', 91, 74), 5228: ('ob/title', 92, 46), 5390: ('python:here.compute_size(ob)', 96, 76), 5522: ('python:here.last_modified(ob)', 98, 81), 5737: ("python:sm.checkPermission('Delete objects', context)", 106, 23), 5806: ('obs', 106, 92), 5883: ('not:context/dontAllowCopyAndPaste|nothing', 108, 37), 6160: ('delete_allowed', 110, 121), 6415: ('here/cb_dataValid', 112, 125), 6587: ('delete_allowed', 114, 122), 6741: ("python:sm.checkPermission('Import/Export objects', context)", 115, 135), 6856: ("python: has_order_support and sm.checkPermission('Manage properties', context)", 117, 50), 7050: ('python:range(1,min(5,len(obs)))', 119, 38), 7096: ('val', 119, 84), 7142: ('python:range(5,len(obs),5)', 120, 38), 7183: ('val', 120, 79), 8444: ('not:obs', 146, 26), 8558: ('here/title_or_id', 148, 57), 8662: ('not:context/dontAllowCopyAndPaste|nothing', 151, 35), 8824: ('here/cb_dataValid', 152, 118), 9000: ("python:sm.checkPermission('Import/Export objects', context)", 154, 128), 12921: ('here/manage_page_footer', 281, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4961819312 = {'class': 'zmi-typename_show', }
_static_5108864896 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'manage_importExportForm:method', 'value': 'Import/Export', }
_static_5108862400 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'manage_pasteObjects:method', 'value': 'Paste', }
_static_5108861584 = {'class': 'form-group', }
_static_5108869840 = {'class': 'alert alert-info mt-4 mb-4', }
_static_5108875120 = {'class': 'fas fa-arrow-down', 'style': 'border-bottom: 0.2rem solid silver;', }
_static_5108861008 = {'type': 'submit', 'name': 'manage_move_objects_to_bottom:method', 'value': 'Move to bottom', 'title': 'Move selected items to bottom', 'class': 'btn btn-primary', }
_static_5108873488 = {'class': 'fas fa-arrow-up', 'style': 'border-top: 0.2rem solid silver;', }
_static_5108864608 = {'type': 'submit', 'name': 'manage_move_objects_to_top:method', 'value': 'Move to top', 'title': 'Move selected items to top', 'class': 'btn btn-primary ml-2 mr-2', }
_static_5108873776 = {'class': 'fas fa-arrow-down', }
_static_5108818096 = {'type': 'submit', 'name': 'manage_move_objects_down:method', 'value': 'Move down', 'title': 'Move selected items down', 'class': 'btn btn-primary rounded-right', }
_static_5108816608 = {'class': 'fas fa-arrow-up', }
_static_5108814544 = {'type': 'submit', 'name': 'manage_move_objects_up:method', 'value': 'Move up', 'title': 'Move selected items up', 'class': 'btn btn-primary', }
_static_5108812864 = {'class': 'input-group-append', }
_static_5108820448 = {'class': 'form-control btn btn-primary', 'name': 'delta:int', }
_static_5108819056 = {'class': 'input-group', }
_static_5108816848 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_importExportForm:method', 'value': 'Import/Export', }
_static_5108758080 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_delObjects:method', 'value': 'Delete', }
_static_5108749152 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_pasteObjects:method', 'value': 'Paste', }
_static_5108759712 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_copyObjects:method', 'value': 'Copy', }
_static_5108756736 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_cutObjects:method', 'value': 'Cut', }
_static_5108755536 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_renameForm:method', 'value': 'Rename', }
_static_5108753472 = {'class': 'input-group', }
_static_4961845056 = {'class': 'form-group form-inline zmi-controls', }
_static_5108749632 = {'class': 'text-right zmi-object-date hidden-xs pl-3', }
_static_5108748240 = {'class': 'text-right zmi-object-size hidden-xs', }
_static_5108793296 = {'class': 'zmi-object-title hidden-xs', }
_static_5108789552 = {'class': 'fa fa-lock', }
_static_5108786480 = {'class': 'badge badge-warning', 'title': 'This item has been locked by WebDAV', }
_static_5108788928 = {'href': "python:'%s/manage_workspace'%(ob_dict['quoted_id'])", }
_static_5108783360 = {'class': 'zmi-object-id', }
_static_5108784848 = {'class': 'sr-only', }
_static_5108781200 = {'title': 'Broken object', 'class': 'fas fa-ban text-danger', }
_static_5108780336 = {'class': 'zmi-object-type', 'onclick': "$(this).prev().children('input').trigger('click')", }
_static_4961834688 = {'type': 'checkbox', 'class': 'checkbox-list-item', 'name': 'ids:list', 'onclick': 'event.stopPropagation();select_objectitem($(this));', 'value': 'ob_dict/id', }
_static_4961833824 = {'class': 'zmi-object-check text-right', 'onclick': "$(this).children('input').trigger('click');", }
_static_4961841840 = {'class': 'fa fa-sort', }
_static_4961836992 = {'title': 'Sort Ascending by Modification Date', 'href': '?skey=_p_mtime&rkey=asc', 'class': "python:skey=='_p_mtime' and 'zmi-sort_key' or None", }
_static_4961837568 = {'scope': 'col', 'class': 'zmi-object-date text-right hidden-xs', }
_static_4961837376 = {'class': 'fa fa-sort', }
_static_4961831184 = {'title': 'Sort Ascending by File-Size', 'href': '?skey=get_size&rkey=asc', 'class': "python:skey=='get_size' and 'zmi-sort_key' or None", }
_static_5108722096 = {'scope': 'col', 'class': 'zmi-object-size text-right hidden-xs', }
_static_5108722144 = {'id': 'tablefilter', 'name': 'obj_ids:tokens', 'type': 'text', 'title': 'Filter object list by entering a name. Pressing the Enter key starts recursive search.', }
_static_5108719120 = {'class': 'fa fa-search tablefilter', 'onclick': "$('#tablefilter').focus()", }
_static_5108715472 = {'class': 'fa fa-sort', }
_static_5108724352 = {'title': 'Sort Ascending by Name', 'href': '?skey=id&rkey=asc', 'class': "python:skey=='id' and 'zmi-sort_key' or None", }
_static_5108720704 = {'scope': 'col', 'class': 'zmi-object-id', }
_static_5108717968 = {'class': 'fa fa-sort', }
_static_5108716864 = {'title': 'Sort Ascending by Meta-Type', 'href': '?skey=meta_type&rkey=asc', 'class': "python:skey=='meta_type' and 'zmi-sort_key' or None", }
_static_5108713600 = {'scope': 'col', 'class': 'zmi-object-type', }
_static_4961619344 = {'type': 'checkbox', 'id': 'checkAll', 'onclick': 'checkbox_all();', }
_static_4961632208 = {'scope': 'col', 'class': 'zmi-object-check text-right', }
_static_4961623040 = {'class': 'thead-light', }
_static_4961618096 = {'class': 'table table-striped table-hover table-sm objectItems', }
_static_4961623856 = {'id': 'objectItems', 'name': 'objectItems', 'method': 'post', 'action': 'string:${request/URL1}/', }
_static_4961626160 = {'class': 'container-fluid', }
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
_static_4428767312 = {}

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

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961485536
            __attrs_4961485536 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961499456
            __default_4961499456 = _DEFAULT_MARKER

            # <Value 'here/manage_page_header' (1:31)> -> __cache_4961488464
            __token = 31
            try:
                __zt_tmp = __attrs_4961485536
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4961488464 = _static_4427992992('path', 'here/manage_page_header', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_page_header' (1:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 127ba42b0> -> __condition
            __expression = __cache_4961488464

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4961488464
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961625104
            __attrs_4961625104 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961628512
            __default_4961628512 = _DEFAULT_MARKER

            # <Value 'here/manage_tabs' (3:29)> -> __cache_4961499312
            __token = 89
            try:
                __zt_tmp = __attrs_4961625104
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4961499312 = _static_4427992992('path', 'here/manage_tabs', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_tabs' (3:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 127bc6200> -> __condition
            __expression = __cache_4961499312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4961499312
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x127bc6830> name=None at 127bc62f0> -> __attrs_4961628416
            __attrs_4961628416 = _static_4961626160

            # <main ... (0:0)
            # --------------------------------------------------------
            __append('<main class="container-fluid">\n  ')

            # <Static value=<ast.Dict object at 0x127bc5f30> name=None at 127bc5ea0> -> __attrs_4961626400
            __attrs_4961626400 = _static_4961623856
            __backup_has_order_support_4961539728 = get('has_order_support', __marker)

            # <Value "python:getattr(here.aq_explicit, 'has_order_support', 0)" (7:38)> -> __value
            __token = 238
            try:
                __zt_tmp = __attrs_4961626400
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', "getattr(here.aq_explicit, 'has_order_support', 0)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['has_order_support'] = __value
            __backup_sm_4961539872 = get('sm', __marker)

            # <Value 'modules/AccessControl/getSecurityManager' (8:22)> -> __value
            __token = 318
            try:
                __zt_tmp = __attrs_4961626400
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'modules/AccessControl/getSecurityManager', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['sm'] = __value
            __backup_default_sort_4961540112 = get('default_sort', __marker)

            # <Value "python: 'position' if has_order_support else 'id'" (9:31)> -> __value
            __token = 392
            try:
                __zt_tmp = __attrs_4961626400
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', " 'position' if has_order_support else 'id'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['default_sort'] = __value
            __backup_skey_4961547648 = get('skey', __marker)

            # <Value "python:request.get('skey',default_sort)" (10:22)> -> __value
            __token = 467
            try:
                __zt_tmp = __attrs_4961626400
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', "request.get('skey',default_sort)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['skey'] = __value
            __backup_rkey_4961547792 = get('rkey', __marker)

            # <Value "python:request.get('rkey','asc')" (11:21)> -> __value
            __token = 532
            try:
                __zt_tmp = __attrs_4961626400
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', "request.get('rkey','asc')", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['rkey'] = __value
            __backup_rkey_alt_4961548032 = get('rkey_alt', __marker)

            # <Value "python:'desc' if rkey=='asc' else 'asc'" (12:24)> -> __value
            __token = 594
            try:
                __zt_tmp = __attrs_4961626400
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', "'desc' if rkey=='asc' else 'asc'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['rkey_alt'] = __value
            __backup_rkey_alt_up_4960788752 = get('rkey_alt_up', __marker)

            # <Value 'rkey_alt/upper' (13:26)> -> __value
            __token = 666
            try:
                __zt_tmp = __attrs_4961626400
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'rkey_alt/upper', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['rkey_alt_up'] = __value
            __backup_obs_4960793504 = get('obs', __marker)

            # <Value 'python: here.manage_get_sortedObjects(sortkey = skey, revkey = rkey)' (14:17)> -> __value
            __token = 705
            try:
                __zt_tmp = __attrs_4961626400
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', ' here.manage_get_sortedObjects(sortkey = skey, revkey = rkey)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['obs'] = __value
            __backup_my_url_4960795664 = get('my_url', __marker)

            # <Value 'string:${context/absolute_url}/manage_main' (15:19)> -> __value
            __token = 801
            try:
                __zt_tmp = __attrs_4961626400
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('string', '${context/absolute_url}/manage_main', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['my_url'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form id="objectItems" name="objectItems" method="post"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961629424
            __default_4961629424 = _DEFAULT_MARKER

            # <Substitution 'string:${request/URL1}/' (17:31)> -> __attr_action
            __token = 905
            try:
                __zt_tmp = __attrs_4961626400
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_4427992992('string', '${request/URL1}/', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append('>\n\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961623232
            __attrs_4961623232 = _static_4428767312

            # <Value 'obs' (19:30)> -> __condition
            __token = 962
            try:
                __zt_tmp = __attrs_4961623232
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'obs', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x127bc48b0> name=None at 127bc5600> -> __attrs_4961621312
                __attrs_4961621312 = _static_4961618096

                # <Value 'obs' (20:89)> -> __condition
                __token = 1057
                try:
                    __zt_tmp = __attrs_4961621312
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'obs', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <table ... (0:0)
                    # --------------------------------------------------------
                    __append('<table class="table table-striped table-hover table-sm objectItems">\n        ')

                    # <Static value=<ast.Dict object at 0x127bc5c00> name=None at 127bc5450> -> __attrs_4961632064
                    __attrs_4961632064 = _static_4961623040

                    # <thead ... (0:0)
                    # --------------------------------------------------------
                    __append('<thead')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961619728
                    __default_4961619728 = _DEFAULT_MARKER

                    # <Substitution "python:'thead-light sorted_%s'%(request.get('rkey',''))" (21:57)> -> __attr_class
                    __token = 1120
                    try:
                        __zt_tmp = __attrs_4961632064
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4427992992('python', "'thead-light sorted_%s'%(request.get('rkey',''))", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', 'thead-light', _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n          ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961621120
                    __attrs_4961621120 = _static_4428767312

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr>\n            ')

                    # <Static value=<ast.Dict object at 0x127bc7fd0> name=None at 127bc4f70> -> __attrs_4961620352
                    __attrs_4961620352 = _static_4961632208

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th scope="col" class="zmi-object-check text-right">\n              ')

                    # <Static value=<ast.Dict object at 0x127bc4d90> name=None at 127bc5360> -> __attrs_5108718400
                    __attrs_5108718400 = _static_4961619344

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="checkbox" id="checkAll" onclick="checkbox_all();" />\n            </th>\n            ')

                    # <Static value=<ast.Dict object at 0x13080c880> name=None at 13080cf40> -> __attrs_5108716096
                    __attrs_5108716096 = _static_5108713600

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th scope="col" class="zmi-object-type">\n              ')

                    # <Static value=<ast.Dict object at 0x13080d540> name=None at 13080d5a0> -> __attrs_5108716672
                    __attrs_5108716672 = _static_5108716864

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108716240
                    __default_5108716240 = _DEFAULT_MARKER

                    # <Substitution 'string:Sort ${rkey_alt_up} by meta-type' (29:39)> -> __attr_title
                    __token = 1550
                    try:
                        __zt_tmp = __attrs_5108716672
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_4427992992('string', 'Sort ${rkey_alt_up} by meta-type', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by Meta-Type', _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108717152
                    __default_5108717152 = _DEFAULT_MARKER

                    # <Substitution 'string:${my_url}?skey=meta_type&rkey=${rkey_alt}' (30:37)> -> __attr_href
                    __token = 1628
                    try:
                        __zt_tmp = __attrs_5108716672
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4427992992('string', '${my_url}?skey=meta_type&rkey=${rkey_alt}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=meta_type&rkey=asc', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108717920
                    __default_5108717920 = _DEFAULT_MARKER

                    # <Substitution "python:skey=='meta_type' and 'zmi-sort_key' or None" (31:37)> -> __attr_class
                    __token = 1716
                    try:
                        __zt_tmp = __attrs_5108716672
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4427992992('python', "skey=='meta_type' and 'zmi-sort_key' or None", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n                ')

                    # <Static value=<ast.Dict object at 0x13080d990> name=None at 13080da50> -> __attrs_5108714560
                    __attrs_5108714560 = _static_5108717968

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i class="fa fa-sort"></i>\n              </a>\n            </th>\n            ')

                    # <Static value=<ast.Dict object at 0x13080e440> name=None at 13080d120> -> __attrs_5108720752
                    __attrs_5108720752 = _static_5108720704

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th scope="col" class="zmi-object-id">\n              ')

                    # <Static value=<ast.Dict object at 0x13080f280> name=None at 13080f2b0> -> __attrs_5108721952
                    __attrs_5108721952 = _static_5108724352

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108721616
                    __default_5108721616 = _DEFAULT_MARKER

                    # <Substitution 'string:Sort ${rkey_alt_up} by name' (39:39)> -> __attr_title
                    __token = 2066
                    try:
                        __zt_tmp = __attrs_5108721952
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_4427992992('string', 'Sort ${rkey_alt_up} by name', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by Name', _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108720032
                    __default_5108720032 = _DEFAULT_MARKER

                    # <Substitution 'string:${my_url}?skey=id&rkey=${rkey_alt}' (40:37)> -> __attr_href
                    __token = 2139
                    try:
                        __zt_tmp = __attrs_5108721952
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4427992992('string', '${my_url}?skey=id&rkey=${rkey_alt}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=id&rkey=asc', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108724640
                    __default_5108724640 = _DEFAULT_MARKER

                    # <Substitution "python:skey=='id' and 'zmi-sort_key' or None" (41:37)> -> __attr_class
                    __token = 2220
                    try:
                        __zt_tmp = __attrs_5108721952
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4427992992('python', "skey=='id' and 'zmi-sort_key' or None", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n                Name\n                ')

                    # <Static value=<ast.Dict object at 0x13080cfd0> name=None at 13080c370> -> __attrs_5108724928
                    __attrs_5108724928 = _static_5108715472

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i class="fa fa-sort"></i>\n              </a>\n              ')

                    # <Static value=<ast.Dict object at 0x13080de10> name=None at 13080ece0> -> __attrs_5108726512
                    __attrs_5108726512 = _static_5108719120

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i class="fa fa-search tablefilter" onclick="$(\'#tablefilter\').focus()"></i>\n              ')

                    # <Static value=<ast.Dict object at 0x13080e9e0> name=None at 13080e8f0> -> __attrs_5108722480
                    __attrs_5108722480 = _static_5108722144

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input id="tablefilter" name="obj_ids:tokens" type="text" title="Filter object list by entering a name. Pressing the Enter key starts recursive search." />\n            </th>\n            ')

                    # <Static value=<ast.Dict object at 0x13080e9b0> name=None at 13080ded0> -> __attrs_4961830272
                    __attrs_4961830272 = _static_5108722096

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th scope="col" class="zmi-object-size text-right hidden-xs">\n              ')

                    # <Static value=<ast.Dict object at 0x127bf8910> name=None at 127bf8a30> -> __attrs_4961840304
                    __attrs_4961840304 = _static_4961831184

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961830944
                    __default_4961830944 = _DEFAULT_MARKER

                    # <Substitution 'string:Sort ${rkey_alt_up} by size' (52:39)> -> __attr_title
                    __token = 2879
                    try:
                        __zt_tmp = __attrs_4961840304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_4427992992('string', 'Sort ${rkey_alt_up} by size', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by File-Size', _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961832144
                    __default_4961832144 = _DEFAULT_MARKER

                    # <Substitution 'string:${my_url}?skey=get_size&rkey=${rkey_alt}' (53:37)> -> __attr_href
                    __token = 2952
                    try:
                        __zt_tmp = __attrs_4961840304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4427992992('string', '${my_url}?skey=get_size&rkey=${rkey_alt}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=get_size&rkey=asc', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961835600
                    __default_4961835600 = _DEFAULT_MARKER

                    # <Substitution "python:skey=='get_size' and 'zmi-sort_key' or None" (54:37)> -> __attr_class
                    __token = 3039
                    try:
                        __zt_tmp = __attrs_4961840304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4427992992('python', "skey=='get_size' and 'zmi-sort_key' or None", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n                Size\n                ')

                    # <Static value=<ast.Dict object at 0x127bfa140> name=None at 127bfa2f0> -> __attrs_4961832576
                    __attrs_4961832576 = _static_4961837376

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i class="fa fa-sort"></i>\n              </a>\n            </th>\n            ')

                    # <Static value=<ast.Dict object at 0x127bfa200> name=None at 127bfa830> -> __attrs_4961832336
                    __attrs_4961832336 = _static_4961837568

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th scope="col" class="zmi-object-date text-right hidden-xs">\n              ')

                    # <Static value=<ast.Dict object at 0x127bf9fc0> name=None at 127bf9ff0> -> __attrs_4961836176
                    __attrs_4961836176 = _static_4961836992

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961838720
                    __default_4961838720 = _DEFAULT_MARKER

                    # <Substitution 'string:Sort ${rkey_alt_up} by modification date' (63:39)> -> __attr_title
                    __token = 3451
                    try:
                        __zt_tmp = __attrs_4961836176
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_4427992992('string', 'Sort ${rkey_alt_up} by modification date', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by Modification Date', _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961834016
                    __default_4961834016 = _DEFAULT_MARKER

                    # <Substitution 'string:${my_url}?skey=_p_mtime&rkey=${rkey_alt}' (64:37)> -> __attr_href
                    __token = 3537
                    try:
                        __zt_tmp = __attrs_4961836176
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4427992992('string', '${my_url}?skey=_p_mtime&rkey=${rkey_alt}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=_p_mtime&rkey=asc', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961834352
                    __default_4961834352 = _DEFAULT_MARKER

                    # <Substitution "python:skey=='_p_mtime' and 'zmi-sort_key' or None" (65:37)> -> __attr_class
                    __token = 3624
                    try:
                        __zt_tmp = __attrs_4961836176
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4427992992('python', "skey=='_p_mtime' and 'zmi-sort_key' or None", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n                Last Modified\n                ')

                    # <Static value=<ast.Dict object at 0x127bfb2b0> name=None at 127bfaef0> -> __attrs_4961845008
                    __attrs_4961845008 = _static_4961841840

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i class="fa fa-sort"></i>\n              </a>\n            </th>\n          </tr>\n        </thead>\n        ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961844624
                    __attrs_4961844624 = _static_4428767312

                    # <tbody ... (0:0)
                    # --------------------------------------------------------
                    __append('<tbody>\n          ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961843952
                    __attrs_4961843952 = _static_4428767312
                    __backup_ob_dict_4961051424 = get('ob_dict', __marker)

                    # <Value 'obs' (74:34)> -> __iterator
                    __token = 3906
                    try:
                        __zt_tmp = __attrs_4961843952
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_4427992992('path', 'obs', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    (__iterator, ____index_4961844336, ) = getname('repeat')('ob_dict', __iterator)
                    econtext['ob_dict'] = None
                    for __item in __iterator:
                        econtext['ob_dict'] = __item

                        # <tr ... (0:0)
                        # --------------------------------------------------------
                        __append('<tr>\n            ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961841984
                        __attrs_4961841984 = _static_4428767312
                        __backup_ob_4961051664 = get('ob', __marker)

                        # <Value 'nocall:ob_dict/obj' (75:32)> -> __value
                        __token = 3944
                        try:
                            __zt_tmp = __attrs_4961841984
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4427992992('nocall', 'ob_dict/obj', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        econtext['ob'] = __value
                        __append('\n              ')

                        # <Static value=<ast.Dict object at 0x127bf9360> name=None at 127bf9240> -> __attrs_4961840592
                        __attrs_4961840592 = _static_4961833824

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="zmi-object-check text-right" onclick="$(this).children(\'input\').trigger(\'click\');">\n                ')

                        # <Static value=<ast.Dict object at 0x127bf96c0> name=None at 127bf9450> -> __attrs_5108780672
                        __attrs_5108780672 = _static_4961834688

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="checkbox" class="checkbox-list-item" name="ids:list"                   onclick="event.stopPropagation();select_objectitem($(this));"')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108780960
                        __default_5108780960 = _DEFAULT_MARKER

                        # <Substitution 'ob_dict/id' (77:104)> -> __attr_value
                        __token = 4178
                        try:
                            __zt_tmp = __attrs_5108780672
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_4427992992('path', 'ob_dict/id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' />\n              </td>\n              ')

                        # <Static value=<ast.Dict object at 0x13081cd30> name=None at 13081cdc0> -> __attrs_5108778272
                        __attrs_5108778272 = _static_5108780336

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="zmi-object-type" onclick="$(this).prev().children(\'input\').trigger(\'click\')">\n                ')

                        # <Static value=<ast.Dict object at 0x13081d090> name=None at 13081d030> -> __attrs_5108782880
                        __attrs_5108782880 = _static_5108781200

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append('<i')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108777216
                        __default_5108777216 = _DEFAULT_MARKER

                        # <Substitution 'ob/meta_type | default' (81:122)> -> __attr_title
                        __token = 4519
                        try:
                            __zt_tmp = __attrs_5108782880
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_4427992992('path', 'ob/meta_type | default', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', 'Broken object', _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108781392
                        __default_5108781392 = _DEFAULT_MARKER

                        # <Substitution 'ob/zmi_icon | default' (81:94)> -> __attr_class
                        __token = 4491
                        try:
                            __zt_tmp = __attrs_5108782880
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_4427992992('path', 'ob/zmi_icon | default', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', 'fas fa-ban text-danger', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))
                        __append('>\n                  ')

                        # <Static value=<ast.Dict object at 0x13081ded0> name=None at 13081df60> -> __attrs_5108784320
                        __attrs_5108784320 = _static_5108784848

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="sr-only">')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108784944
                        __default_5108784944 = _DEFAULT_MARKER

                        # <Value 'ob/meta_type | default' (82:53)> -> __cache_5108781008
                        __token = 4598
                        try:
                            __zt_tmp = __attrs_5108784320
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_5108781008 = _static_4427992992('path', 'ob/meta_type | default', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value 'ob/meta_type | default' (82:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 13081c490> -> __condition
                        __expression = __cache_5108781008

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Broken object')
                        else:
                            __content = __cache_5108781008
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>\n                </i>\n              </td>\n              ')

                        # <Static value=<ast.Dict object at 0x13081d900> name=None at 13081d960> -> __attrs_5108789168
                        __attrs_5108789168 = _static_5108783360

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="zmi-object-id">\n                ')

                        # <Static value=<ast.Dict object at 0x13081eec0> name=None at 13081ee60> -> __attrs_5108788736
                        __attrs_5108788736 = _static_5108788928

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108788496
                        __default_5108788496 = _DEFAULT_MARKER

                        # <Substitution "python:'%s/manage_workspace'%(ob_dict['quoted_id'])" (86:40)> -> __attr_href
                        __token = 4765
                        try:
                            __zt_tmp = __attrs_5108788736
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4427992992('python', "'%s/manage_workspace'%(ob_dict['quoted_id'])", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>\n                  ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5108791136
                        __attrs_5108791136 = _static_4428767312

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108792432
                        __default_5108792432 = _DEFAULT_MARKER

                        # <Value 'ob_dict/id' (87:37)> -> __cache_5108787536
                        __token = 4856
                        try:
                            __zt_tmp = __attrs_5108791136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_5108787536 = _static_4427992992('path', 'ob_dict/id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value 'ob_dict/id' (87:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 13081f370> -> __condition
                        __expression = __cache_5108787536

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>Id</span>')
                        else:
                            __content = __cache_5108787536
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x13081e530> name=None at 13081fb20> -> __attrs_5108788160
                        __attrs_5108788160 = _static_5108786480

                        # <Value 'ob/wl_isLocked | nothing' (88:111)> -> __condition
                        __token = 4989
                        try:
                            __zt_tmp = __attrs_5108788160
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4427992992('path', 'ob/wl_isLocked | nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span class="badge badge-warning" title="This item has been locked by WebDAV">\n                    ')

                            # <Static value=<ast.Dict object at 0x13081f130> name=None at 13081f910> -> __attrs_5108785712
                            __attrs_5108785712 = _static_5108789552

                            # <i ... (0:0)
                            # --------------------------------------------------------
                            __append('<i class="fa fa-lock"></i>\n                  </span>')
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x13081ffd0> name=None at 13081f8b0> -> __attrs_5108793104
                        __attrs_5108793104 = _static_5108793296

                        # <Value 'ob/title|nothing' (91:74)> -> __condition
                        __token = 5163
                        try:
                            __zt_tmp = __attrs_5108793104
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4427992992('path', 'ob/title|nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span class="zmi-object-title hidden-xs">\n                    &nbsp;(')

                            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5108744688
                            __attrs_5108744688 = _static_4428767312

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108744304
                            __default_5108744304 = _DEFAULT_MARKER

                            # <Value 'ob/title' (92:46)> -> __cache_5108781488
                            __token = 5228
                            try:
                                __zt_tmp = __attrs_5108744688
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_5108781488 = _static_4427992992('path', 'ob/title', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                            # <BinOp left=<Value 'ob/title' (92:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 13081f5b0> -> __condition
                            __expression = __cache_5108781488

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span></span>')
                            else:
                                __content = __cache_5108781488
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(')\n                  </span>')
                        __append('\n                </a>\n              </td>\n              ')

                        # <Static value=<ast.Dict object at 0x130814fd0> name=None at 130814e80> -> __attrs_5108745264
                        __attrs_5108745264 = _static_5108748240

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="text-right zmi-object-size hidden-xs">')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108745120
                        __default_5108745120 = _DEFAULT_MARKER

                        # <Value 'python:here.compute_size(ob)' (96:76)> -> __cache_5108783744
                        __token = 5390
                        try:
                            __zt_tmp = __attrs_5108745264
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_5108783744 = _static_4427992992('python', 'here.compute_size(ob)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value 'python:here.compute_size(ob)' (96:76)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 130815090> -> __condition
                        __expression = __cache_5108783744

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n              ')
                        else:
                            __content = __cache_5108783744
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</td>\n              ')

                        # <Static value=<ast.Dict object at 0x130815540> name=None at 130814100> -> __attrs_5108746704
                        __attrs_5108746704 = _static_5108749632

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="text-right zmi-object-date hidden-xs pl-3">')

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108746320
                        __default_5108746320 = _DEFAULT_MARKER

                        # <Value 'python:here.last_modified(ob)' (98:81)> -> __cache_5108747328
                        __token = 5522
                        try:
                            __zt_tmp = __attrs_5108746704
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_5108747328 = _static_4427992992('python', 'here.last_modified(ob)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                        # <BinOp left=<Value 'python:here.last_modified(ob)' (98:81)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 130814cd0> -> __condition
                        __expression = __cache_5108747328

                        # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n              ')
                        else:
                            __content = __cache_5108747328
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</td>\n            ')
                        if (__backup_ob_4961051664 is __marker):
                            del econtext['ob']
                        else:
                            econtext['ob'] = __backup_ob_4961051664
                        __append('\n          </tr>')
                        ____index_4961844336 -= 1
                        if (____index_4961844336 > 0):
                            __append('\n          ')
                    if (__backup_ob_dict_4961051424 is __marker):
                        del econtext['ob_dict']
                    else:
                        econtext['ob_dict'] = __backup_ob_dict_4961051424
                    __append('\n        </tbody>\n      </table>')
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x127bfbf40> name=None at 127bfaf20> -> __attrs_5108751936
                __attrs_5108751936 = _static_4961845056
                __backup_delete_allowed_4960594736 = get('delete_allowed', __marker)

                # <Value "python:sm.checkPermission('Delete objects', context)" (106:23)> -> __value
                __token = 5737
                try:
                    __zt_tmp = __attrs_5108751936
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4427992992('python', "sm.checkPermission('Delete objects', context)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                econtext['delete_allowed'] = __value

                # <Value 'obs' (106:92)> -> __condition
                __token = 5806
                try:
                    __zt_tmp = __attrs_5108751936
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'obs', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-group form-inline zmi-controls">\n        ')

                    # <Static value=<ast.Dict object at 0x130816440> name=None at 130816110> -> __attrs_5108749728
                    __attrs_5108749728 = _static_5108753472

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="input-group">\n          ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5108752512
                    __attrs_5108752512 = _static_4428767312

                    # <Value 'not:context/dontAllowCopyAndPaste|nothing' (108:37)> -> __condition
                    __token = 5883
                    try:
                        __zt_tmp = __attrs_5108752512
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('not', 'context/dontAllowCopyAndPaste|nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x130816c50> name=None at 130816ad0> -> __attrs_5108754864
                        __attrs_5108754864 = _static_5108755536

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary mr-2" type="submit" name="manage_renameForm:method" value="Rename" />\n            ')

                        # <Static value=<ast.Dict object at 0x130817100> name=None at 130817460> -> __attrs_5108757024
                        __attrs_5108757024 = _static_5108756736

                        # <Value 'delete_allowed' (110:121)> -> __condition
                        __token = 6160
                        try:
                            __zt_tmp = __attrs_5108757024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4427992992('path', 'delete_allowed', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        if __condition:

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input class="btn btn-primary mr-2" type="submit" name="manage_cutObjects:method" value="Cut" />')
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x130817ca0> name=None at 130816b00> -> __attrs_5108760192
                        __attrs_5108760192 = _static_5108759712

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary mr-2" type="submit" name="manage_copyObjects:method" value="Copy" />\n            ')

                        # <Static value=<ast.Dict object at 0x130815360> name=None at 130816890> -> __attrs_5108745600
                        __attrs_5108745600 = _static_5108749152

                        # <Value 'here/cb_dataValid' (112:125)> -> __condition
                        __token = 6415
                        try:
                            __zt_tmp = __attrs_5108745600
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4427992992('path', 'here/cb_dataValid', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        if __condition:

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input class="btn btn-primary mr-2" type="submit" name="manage_pasteObjects:method" value="Paste" />')
                        __append('\n          ')
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x130817640> name=None at 130816860> -> __attrs_5108824432
                    __attrs_5108824432 = _static_5108758080

                    # <Value 'delete_allowed' (114:122)> -> __condition
                    __token = 6587
                    try:
                        __zt_tmp = __attrs_5108824432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('path', 'delete_allowed', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary mr-2" type="submit" name="manage_delObjects:method" value="Delete" />')
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x130825bd0> name=None at 130827a00> -> __attrs_5108823904
                    __attrs_5108823904 = _static_5108816848

                    # <Value "python:sm.checkPermission('Import/Export objects', context)" (115:135)> -> __condition
                    __token = 6741
                    try:
                        __zt_tmp = __attrs_5108823904
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('python', "sm.checkPermission('Import/Export objects', context)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary mr-2" type="submit" name="manage_importExportForm:method" value="Import/Export" />')
                    __append('\n\n          ')

                    # <Static value=<ast.Dict object at 0x130826470> name=None at 130826980> -> __attrs_5108824912
                    __attrs_5108824912 = _static_5108819056

                    # <Value "python: has_order_support and sm.checkPermission('Manage properties', context)" (117:50)> -> __condition
                    __token = 6856
                    try:
                        __zt_tmp = __attrs_5108824912
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('python', " has_order_support and sm.checkPermission('Manage properties', context)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="input-group">\n            ')

                        # <Static value=<ast.Dict object at 0x1308269e0> name=None at 130826b00> -> __attrs_5108819920
                        __attrs_5108819920 = _static_5108820448

                        # <select ... (0:0)
                        # --------------------------------------------------------
                        __append('<select class="form-control btn btn-primary" name="delta:int">\n              ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5108821408
                        __attrs_5108821408 = _static_4428767312
                        __backup_val_4961553136 = get('val', __marker)

                        # <Value 'python:range(1,min(5,len(obs)))' (119:38)> -> __iterator
                        __token = 7050
                        try:
                            __zt_tmp = __attrs_5108821408
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_4427992992('python', 'range(1,min(5,len(obs)))', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        (__iterator, ____index_5108812480, ) = getname('repeat')('val', __iterator)
                        econtext['val'] = None
                        for __item in __iterator:
                            econtext['val'] = __item

                            # <option ... (0:0)
                            # --------------------------------------------------------
                            __append('<option>')

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108817856
                            __default_5108817856 = _DEFAULT_MARKER

                            # <Value 'val' (119:84)> -> __cache_5108811616
                            __token = 7096
                            try:
                                __zt_tmp = __attrs_5108821408
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_5108811616 = _static_4427992992('path', 'val', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                            # <BinOp left=<Value 'val' (119:84)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 130826740> -> __condition
                            __expression = __cache_5108811616

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_5108811616
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('</option>')
                            ____index_5108812480 -= 1
                            if (____index_5108812480 > 0):
                                __append('\n              ')
                        if (__backup_val_4961553136 is __marker):
                            del econtext['val']
                        else:
                            econtext['val'] = __backup_val_4961553136
                        __append('\n              ')

                        # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5108811424
                        __attrs_5108811424 = _static_4428767312
                        __backup_val_4961553376 = get('val', __marker)

                        # <Value 'python:range(5,len(obs),5)' (120:38)> -> __iterator
                        __token = 7142
                        try:
                            __zt_tmp = __attrs_5108811424
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_4427992992('python', 'range(5,len(obs),5)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                        (__iterator, ____index_5108813392, ) = getname('repeat')('val', __iterator)
                        econtext['val'] = None
                        for __item in __iterator:
                            econtext['val'] = __item

                            # <option ... (0:0)
                            # --------------------------------------------------------
                            __append('<option>')

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108812240
                            __default_5108812240 = _DEFAULT_MARKER

                            # <Value 'val' (120:79)> -> __cache_5108812960
                            __token = 7183
                            try:
                                __zt_tmp = __attrs_5108811424
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_5108812960 = _static_4427992992('path', 'val', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                            # <BinOp left=<Value 'val' (120:79)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 130826ef0> -> __condition
                            __expression = __cache_5108812960

                            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_5108812960
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('</option>')
                            ____index_5108813392 -= 1
                            if (____index_5108813392 > 0):
                                __append('\n              ')
                        if (__backup_val_4961553376 is __marker):
                            del econtext['val']
                        else:
                            econtext['val'] = __backup_val_4961553376
                        __append('\n            </select>\n            ')

                        # <Static value=<ast.Dict object at 0x130824c40> name=None at 1308242b0> -> __attrs_5108810080
                        __attrs_5108810080 = _static_5108812864

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="input-group-append">\n              ')

                        # <Static value=<ast.Dict object at 0x1308252d0> name=None at 130825120> -> __attrs_5108815312
                        __attrs_5108815312 = _static_5108814544

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" name="manage_move_objects_up:method" value="Move up"                 title="Move selected items up" class="btn btn-primary">\n                ')

                        # <Static value=<ast.Dict object at 0x130825ae0> name=None at 130827670> -> __attrs_5108818336
                        __attrs_5108818336 = _static_5108816608

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append('<i class="fas fa-arrow-up"></i>\n              </button>\n              ')

                        # <Static value=<ast.Dict object at 0x1308260b0> name=None at 130826ec0> -> __attrs_5108822992
                        __attrs_5108822992 = _static_5108818096

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" name="manage_move_objects_down:method" value="Move down"                 title="Move selected items down" class="btn btn-primary rounded-right">\n                ')

                        # <Static value=<ast.Dict object at 0x130833a30> name=None at 130833fd0> -> __attrs_5108874160
                        __attrs_5108874160 = _static_5108873776

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append('<i class="fas fa-arrow-down"></i>\n              </button>\n            </div>\n            ')

                        # <Static value=<ast.Dict object at 0x130831660> name=None at 1308319c0> -> __attrs_5108872816
                        __attrs_5108872816 = _static_5108864608

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" name="manage_move_objects_to_top:method" value="Move to top"               title="Move selected items to top" class="btn btn-primary ml-2 mr-2">\n              ')

                        # <Static value=<ast.Dict object at 0x130833910> name=None at 130830d90> -> __attrs_5108860336
                        __attrs_5108860336 = _static_5108873488

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append('<i class="fas fa-arrow-up" style="border-top: 0.2rem solid silver;"></i>\n            </button>\n            ')

                        # <Static value=<ast.Dict object at 0x130830850> name=None at 1308314e0> -> __attrs_5108861440
                        __attrs_5108861440 = _static_5108861008

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" name="manage_move_objects_to_bottom:method" value="Move to bottom"                title="Move selected items to bottom" class="btn btn-primary">\n              ')

                        # <Static value=<ast.Dict object at 0x130833f70> name=None at 130833b50> -> __attrs_5108871280
                        __attrs_5108871280 = _static_5108875120

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append('<i class="fas fa-arrow-down" style="border-bottom: 0.2rem solid silver;"></i>\n            </button>\n          </div>')
                    __append('\n        </div>\n\n      </div>')
                if (__backup_delete_allowed_4960594736 is __marker):
                    del econtext['delete_allowed']
                else:
                    econtext['delete_allowed'] = __backup_delete_allowed_4960594736
                __append('\n    ')
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5108752128
            __attrs_5108752128 = _static_4428767312

            # <Value 'not:obs' (146:26)> -> __condition
            __token = 8444
            try:
                __zt_tmp = __attrs_5108752128
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('not', 'obs', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x130832ad0> name=None at 130833130> -> __attrs_5108869696
                __attrs_5108869696 = _static_5108869840

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="alert alert-info mt-4 mb-4">\n        There are currently no items in ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5108867008
                __attrs_5108867008 = _static_4428767312

                # <em ... (0:0)
                # --------------------------------------------------------
                __append('<em>')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_5108860480
                __default_5108860480 = _DEFAULT_MARKER

                # <Value 'here/title_or_id' (148:57)> -> __cache_5108867440
                __token = 8558
                try:
                    __zt_tmp = __attrs_5108867008
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_5108867440 = _static_4427992992('path', 'here/title_or_id', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'here/title_or_id' (148:57)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 130831d50> -> __condition
                __expression = __cache_5108867440

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_5108867440
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</em>.\n      </div>\n      ')

                # <Static value=<ast.Dict object at 0x130830a90> name=None at 1308300a0> -> __attrs_5108867200
                __attrs_5108867200 = _static_5108861584

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-group">\n        ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5108868112
                __attrs_5108868112 = _static_4428767312

                # <Value 'not:context/dontAllowCopyAndPaste|nothing' (151:35)> -> __condition
                __token = 8662
                try:
                    __zt_tmp = __attrs_5108868112
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('not', 'context/dontAllowCopyAndPaste|nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x130830dc0> name=None at 130830a30> -> __attrs_5108859616
                    __attrs_5108859616 = _static_5108862400

                    # <Value 'here/cb_dataValid' (152:118)> -> __condition
                    __token = 8824
                    try:
                        __zt_tmp = __attrs_5108859616
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4427992992('path', 'here/cb_dataValid', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary" type="submit" name="manage_pasteObjects:method" value="Paste" />')
                    __append('\n        ')
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x130831780> name=None at 1308325c0> -> __attrs_4961817488
                __attrs_4961817488 = _static_5108864896

                # <Value "python:sm.checkPermission('Import/Export objects', context)" (154:128)> -> __condition
                __token = 9000
                try:
                    __zt_tmp = __attrs_4961817488
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('python', "sm.checkPermission('Import/Export objects', context)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input class="btn btn-primary" type="submit" name="manage_importExportForm:method" value="Import/Export" />')
                __append('\n      </div>\n    ')
            __append('\n  </form>')
            if (__backup_my_url_4960795664 is __marker):
                del econtext['my_url']
            else:
                econtext['my_url'] = __backup_my_url_4960795664
            if (__backup_obs_4960793504 is __marker):
                del econtext['obs']
            else:
                econtext['obs'] = __backup_obs_4960793504
            if (__backup_rkey_alt_up_4960788752 is __marker):
                del econtext['rkey_alt_up']
            else:
                econtext['rkey_alt_up'] = __backup_rkey_alt_up_4960788752
            if (__backup_rkey_alt_4961548032 is __marker):
                del econtext['rkey_alt']
            else:
                econtext['rkey_alt'] = __backup_rkey_alt_4961548032
            if (__backup_rkey_4961547792 is __marker):
                del econtext['rkey']
            else:
                econtext['rkey'] = __backup_rkey_4961547792
            if (__backup_skey_4961547648 is __marker):
                del econtext['skey']
            else:
                econtext['skey'] = __backup_skey_4961547648
            if (__backup_default_sort_4961540112 is __marker):
                del econtext['default_sort']
            else:
                econtext['default_sort'] = __backup_default_sort_4961540112
            if (__backup_sm_4961539872 is __marker):
                del econtext['sm']
            else:
                econtext['sm'] = __backup_sm_4961539872
            if (__backup_has_order_support_4961539728 is __marker):
                del econtext['has_order_support']
            else:
                econtext['has_order_support'] = __backup_has_order_support_4961539728
            __append('\n\n</main>\n\n\n')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_5108865040
            __attrs_5108865040 = _static_4428767312

            # <script ... (0:0)
            # --------------------------------------------------------
            __append('<script>\n  // +++++++++++++++++++++++++++\n  // Item  Selection\n  // +++++++++++++++++++++++++++\n  function checkbox_all() {\n    var checkboxes = document.getElementsByClassName(\'checkbox-list-item\');\n    // Toggle Highlighting CSS-Class\n    if (document.getElementById(\'checkAll\').checked) {\n      $(\'table.objectItems tbody tr\').addClass(\'checked\');\n    } else {\n      $(\'table.objectItems tbody tr\').removeClass(\'checked\');\n    };\n    // Set Checkbox like checkAll-Box\n    for (i = 0; i < checkboxes.length; i++) {\n      checkboxes[i].checked = document.getElementById(\'checkAll\').checked;\n    }\n  };\n\n  function zmicontrols_visible() {\n    var zmicontrols = $(\'form#objectItems .zmi-controls\');\n    var zmicontrols_top = zmicontrols.offset().top;\n    var zmicontrols_bottom = zmicontrols_top + zmicontrols.outerHeight();\n    var viewport_top = $(window).scrollTop();\n    var viewport_bottom = viewport_top + $(window).height();\n    return zmicontrols_bottom > viewport_top && zmicontrols_top < viewport_bottom;\n  };\n\n  function select_objectitem(ob) {\n    ob.parent().parent().toggleClass(\'checked\');\n    if ( !zmicontrols_visible() ) {\n      $(\'form#objectItems\').addClass(\'selected\');\n    }\n    // Anything selected?\n    var checkboxes = document.getElementsByClassName(\'checkbox-list-item\');\n    var selected = false;\n    for (i = 0; i < checkboxes.length; i++) {\n      if ( checkboxes[i].checked ) {\n        selected = true;\n        break;\n      }\n    }\n    if ( !selected ) {\n      $(\'form#objectItems\').removeClass(\'selected\');\n      console.log(\'form#objectItems removed .selected\');\n    }\n  };\n\n\n  $(function () {\n\n    // +++++++++++++++++++++++++++\n    // Icon Tooltips\n    // +++++++++++++++++++++++++++\n    $(\'td.zmi-object-type i\').tooltip({\n      \'placement\': \'top\'\n    });\n\n    // +++++++++++++++++++++++++++\n    // Tablefilter/Search Element\n    // +++++++++++++++++++++++++++\n\n    function isModifierKeyPressed(event) {\n      return event.altKey ||\n        event.ctrlKey ||\n        event.metaKey;\n    }\n\n    $(document).keypress(function (event) {\n\n      if (isModifierKeyPressed(event)) {\n        return; // ignore\n      }\n\n      // Set Focus to Tablefilter only when Modal Dialog is not Shown\n      if (!$(\'#zmi-modal\').hasClass(\'show\')) {\n        $(\'#tablefilter\').focus();\n        // Prevent Submitting a form by hitting Enter\n        // https://stackoverflow.com/questions/895171/prevent-users-from-submitting-a-form-by-hitting-enter\n        if (event.which == 13) {\n          event.preventDefault();\n          return false;\n        };\n      };\n    })\n\n    $(\'#tablefilter\').keyup(function (event) {\n\n      if (isModifierKeyPressed(event)) {\n        return; // ignore\n      }\n\n      var tablefilter = $(this).val();\n      if (event.which == 13) {\n        if (1 === $(\'tbody tr:visible\').length) {\n          window.location.href = $(\'tbody tr:visible a\').attr(\'href\');\n        } else {\n          window.location.href = \'manage_findForm?btn_submit=Find&search_sub:int=1&obj_ids%3Atokens=\' + tablefilter;\n        }\n        event.preventDefault();\n      };\n      $(\'table.objectItems\').find("tbody tr").hide();\n      $(\'table.objectItems\').find("tbody tr td.zmi-object-id a:contains(" + tablefilter + ")").closest(\'tbody tr\').show();\n    });\n\n    // +++++++++++++++++++++++++++\n    // OBJECTIST SORTING: Show skey=meta_type\n    // +++++++++++++++++++++++++++\n    let searchParams = new URLSearchParams(window.location.search);\n    if (searchParams.get(\'skey\') == \'meta_type\') {\n      $(\'td.zmi-object-type i\').each(function () {\n        $(this).parent().parent().find(\'td.zmi-object-id\').prepend(\'')

            # <Static value=<ast.Dict object at 0x127bf5ab0> name=None at 127bf5fc0> -> __attrs_4961821520
            __attrs_4961821520 = _static_4961819312

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span class="zmi-typename_show">\' + $(this).text() + \'</span>\')\n      });\n      $(\'th.zmi-object-id\').addClass(\'zmi-typename_show\');\n    }\n\n  });\n\n</script>\n\n')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4961822720
            __attrs_4961822720 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4961814848
            __default_4961814848 = _DEFAULT_MARKER

            # <Value 'here/manage_page_footer' (281:31)> -> __cache_4961822768
            __token = 12921
            try:
                __zt_tmp = __attrs_4961822720
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4961822768 = _static_4427992992('path', 'here/manage_page_footer', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_page_footer' (281:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 127bf65f0> -> __condition
            __expression = __cache_4961822768

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4961822768
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }