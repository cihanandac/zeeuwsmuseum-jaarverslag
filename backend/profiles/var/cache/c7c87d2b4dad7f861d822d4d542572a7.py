# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/layout/viewlets/content_history.pt'

__tokens = {50: ('view/fullHistory', 2, 25), 116: ('not: history', 4, 25), 197: ('history', 6, 58), 608: ('history', 16, 36), 682: ('item/comments|nothing', 18, 35), 734: (' item/acto', 19, 29), 780: ("e python:actor and actor.get('fullname','username') or item['actorid", 20, 33), 884: ('me item/actor_h', 21, 32), 931: ('ion item/transition_t', 22, 27), 987: ("n_id python:item['action'] or item['review_st", 23, 29), 1067: ('ctive item/effective_date|n', 24, 28), 1133: ("veDate python:effective and view.toLocalizedTime(item['effective_date'],long_forma", 25, 31), 1250: ("Version python:item['type']=='ver", 26, 26), 1314: ("   icons python:context.restrictedTraverse('@@iconr", 27, 21), 1400: ("historyRecord ${python:'table-secondary' if not isVersion else ''}", 28, 23), 1416: ("python:'table-secondary' if not isVersion else ''", 28, 39), 1775: ('string:historyAction state-${action_id}', 33, 53), 1677: ('action', 32, 69), 1993: ('actor_home', 37, 47), 2058: ('actor_home', 38, 53), 2115: ('actor_name', 39, 45), 2191: ('not: actor_home', 40, 50), 2256: ('actor_name', 41, 48), 2424: ("python:view.toLocalizedTime(item['time'],long_format=True)", 44, 82), 2578: ('effective|nothing', 46, 54), 2709: (': ${effectiveDate})', 47, 111), 2713: ('effectiveDate', 47, 115), 2856: ('rhComments', 51, 57), 3015: ('rhComments', 53, 61), 3160: ('isVersion', 57, 62), 3280: ('item/preview_url', 59, 49), 3505: ('isVersion', 64, 62), 3665: ('exists:item/diff_current_url', 66, 43), 3599: ('item/diff_current_url', 65, 82), 3753: ("python:icons.tag('arrow-up')", 67, 57), 4050: ('exists:item/diff_previous_url', 73, 64), 4126: ('item/diff_previous_url', 74, 45), 4347: ("python:icons.tag('arrow-down')", 77, 53), 4604: ('isVersion', 82, 62), 4681: ('item/revert_url', 83, 65), 4721: ('item/revert_url', 83, 105), 4833: ('item/version_id', 84, 94), 4970: ('exists:item/diff_current_url', 86, 47)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4900690512 = {'class': 'btn btn-warning', 'type': 'submit', }
_static_4900688592 = {'type': 'hidden', 'name': 'version_id', 'value': '', }
_static_4900686672 = {'action': '', 'method': 'post', }
_static_4900684560 = {'class': 'historyTools', }
_static_4900163296 = {'class': 'btn btn-secondary', 'title': 'Compare with previous revision', 'href': 'item/diff_previous_url', }
_static_4900172176 = {'class': 'btn btn-secondary', 'href': '', }
_static_4900358704 = {'class': 'historyLinks', }
_static_4900370176 = {'class': 'btn btn-primary', 'href': '', }
_static_4900365568 = {'class': 'historyLinks', }
_static_4900342512 = {'class': 'text-muted', }
_static_4900372144 = {'href': '', }
_static_4900344576 = {'class': 'historyAction', }
_static_4900352736 = {'class': 'historyByLine', }
_static_4900340400 = {'class': "historyRecord ${python:'table-secondary' if not isVersion else ''}", }
_static_4900354800 = {'colspan': '2', }
_static_4900471616 = {'class': 'odd', }
_static_4900475984 = {'class': 'table', 'id': 'history-list', 'summary': 'Content history', }
_static_4439051040 = __C2ZContextWrapper
_static_4439058528 = __compile_zt_expr
_static_4438893776 = {}

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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900478336
            __attrs_4900478336 = _static_4438893776
            __backup_history_4880304448 = get('history', __marker)

            # <Value 'view/fullHistory' (2:25)> -> __value
            __token = 50
            try:
                __zt_tmp = __attrs_4900478336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'view/fullHistory', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['history'] = __value
            __previous_i18n_domain_4900478240 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n     ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900482128
            __attrs_4900482128 = _static_4438893776

            # <Value 'not: history' (4:25)> -> __condition
            __token = 116
            try:
                __zt_tmp = __attrs_4900482128
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4439058528('not', ' history', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>—</div>')
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x124175450> name=None at 124175420> -> __attrs_4900474736
            __attrs_4900474736 = _static_4900475984

            # <Value 'history' (6:58)> -> __condition
            __token = 197
            try:
                __zt_tmp = __attrs_4900474736
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4439058528('path', 'history', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            if __condition:

                # <table ... (0:0)
                # --------------------------------------------------------
                __append('<table class="table" id="history-list"')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900481312
                __default_4900481312 = _DEFAULT_MARKER

                # <Translate msgid='summary_content_history' node=<ast.Constant object at 0x124175e40> at 1241759f0> -> __attr_summary
                __attr_summary = 'Content history'
                __attr_summary = translate('summary_content_history', default=__attr_summary, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_summary is not None):
                    __append((' summary="%s"' % __attr_summary))
                __append('>\n        ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900473152
                __attrs_4900473152 = _static_4438893776

                # <tbody ... (0:0)
                # --------------------------------------------------------
                __append('<tbody>\n            ')

                # <Static value=<ast.Dict object at 0x124174340> name=None at 124174310> -> __attrs_4900473920
                __attrs_4900473920 = _static_4900471616

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr class="odd">\n                ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900355616
                __attrs_4900355616 = _static_4438893776

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>')
                __stream_4900351056 = []
                __append_4900351056 = __stream_4900351056.append
                __append_4900351056('What')
                __msgid_4900351056 = __re_whitespace(''.join(__stream_4900351056)).strip()
                if __msgid_4900351056:
                    __append(translate(__msgid_4900351056, mapping=None, default=__msgid_4900351056, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</th>\n                ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900350816
                __attrs_4900350816 = _static_4438893776

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>')
                __stream_4900352112 = []
                __append_4900352112 = __stream_4900352112.append
                __append_4900352112('View')
                __msgid_4900352112 = __re_whitespace(''.join(__stream_4900352112)).strip()
                if __msgid_4900352112:
                    __append(translate(__msgid_4900352112, mapping=None, default=__msgid_4900352112, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</th>\n                ')

                # <Static value=<ast.Dict object at 0x124157af0> name=None at 124157ac0> -> __attrs_4900349280
                __attrs_4900349280 = _static_4900354800

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th colspan="2">')
                __stream_4900347648 = []
                __append_4900347648 = __stream_4900347648.append
                __append_4900347648('Compare')
                __msgid_4900347648 = __re_whitespace(''.join(__stream_4900347648)).strip()
                if __msgid_4900347648:
                    __append(translate(__msgid_4900347648, mapping=None, default=__msgid_4900347648, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</th>\n                ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900349616
                __attrs_4900349616 = _static_4438893776

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>')
                __stream_4900354896 = []
                __append_4900354896 = __stream_4900354896.append
                __append_4900354896('Revert')
                __msgid_4900354896 = __re_whitespace(''.join(__stream_4900354896)).strip()
                if __msgid_4900354896:
                    __append(translate(__msgid_4900354896, mapping=None, default=__msgid_4900354896, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</th>\n            </tr>\n            ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900350576
                __attrs_4900350576 = _static_4438893776
                __backup_item_4874862800 = get('item', __marker)

                # <Value 'history' (16:36)> -> __iterator
                __token = 608
                try:
                    __zt_tmp = __attrs_4900350576
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4439058528('path', 'history', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                (__iterator, ____index_4900354032, ) = getname('repeat')('item', __iterator)
                econtext['item'] = None
                for __item in __iterator:
                    econtext['item'] = __item
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900342848
                    __attrs_4900342848 = _static_4438893776
                    __backup_rhComments_4877565472 = get('rhComments', __marker)

                    # <Value 'item/comments|nothing' (18:35)> -> __value
                    __token = 682
                    try:
                        __zt_tmp = __attrs_4900342848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('path', 'item/comments|nothing', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['rhComments'] = __value
                    __backup_actor_4880311216 = get('actor', __marker)

                    # <Value 'item/actor' (19:29)> -> __value
                    __token = 734
                    try:
                        __zt_tmp = __attrs_4900342848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('path', 'item/actor', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['actor'] = __value
                    __backup_actor_name_4880315296 = get('actor_name', __marker)

                    # <Value "python:actor and actor.get('fullname','username') or item['actorid']" (20:33)> -> __value
                    __token = 780
                    try:
                        __zt_tmp = __attrs_4900342848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('python', "actor and actor.get('fullname','username') or item['actorid']", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['actor_name'] = __value
                    __backup_actor_home_4841595536 = get('actor_home', __marker)

                    # <Value 'item/actor_home' (21:32)> -> __value
                    __token = 884
                    try:
                        __zt_tmp = __attrs_4900342848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('path', 'item/actor_home', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['actor_home'] = __value
                    __backup_action_4841599136 = get('action', __marker)

                    # <Value 'item/transition_title' (22:27)> -> __value
                    __token = 931
                    try:
                        __zt_tmp = __attrs_4900342848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('path', 'item/transition_title', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['action'] = __value
                    __backup_action_id_4841591072 = get('action_id', __marker)

                    # <Value "python:item['action'] or item['review_state']" (23:29)> -> __value
                    __token = 987
                    try:
                        __zt_tmp = __attrs_4900342848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('python', "item['action'] or item['review_state']", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['action_id'] = __value
                    __backup_effective_4877783808 = get('effective', __marker)

                    # <Value 'item/effective_date|nothing' (24:28)> -> __value
                    __token = 1067
                    try:
                        __zt_tmp = __attrs_4900342848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('path', 'item/effective_date|nothing', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['effective'] = __value
                    __backup_effectiveDate_4877785296 = get('effectiveDate', __marker)

                    # <Value "python:effective and view.toLocalizedTime(item['effective_date'],long_format=True)" (25:31)> -> __value
                    __token = 1133
                    try:
                        __zt_tmp = __attrs_4900342848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('python', "effective and view.toLocalizedTime(item['effective_date'],long_format=True)", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['effectiveDate'] = __value
                    __backup_isVersion_4877784432 = get('isVersion', __marker)

                    # <Value "python:item['type']=='versioning'" (26:26)> -> __value
                    __token = 1250
                    try:
                        __zt_tmp = __attrs_4900342848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('python', "item['type']=='versioning'", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['isVersion'] = __value
                    __backup_icons_4879774000 = get('icons', __marker)

                    # <Value "python:context.restrictedTraverse('@@iconresolver')" (27:21)> -> __value
                    __token = 1314
                    try:
                        __zt_tmp = __attrs_4900342848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4439058528('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    econtext['icons'] = __value
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x1241542b0> name=None at 1241542e0> -> __attrs_4900353840
                    __attrs_4900353840 = _static_4900340400

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900353312
                    __default_4900353312 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "historyRecord ${python:'table-secondary' if not isVersion else ''}" (28:23)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1241560e0> -> __attr_class
                    __token = 1400
                    __token = 1416
                    try:
                        __zt_tmp = __attrs_4900353840
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4439058528('python', "'table-secondary' if not isVersion else ''", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s' % ('historyRecord ', (__attr_class if (__attr_class is not None) else ''), ))
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
                    __append('>\n                ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900339968
                    __attrs_4900339968 = _static_4438893776

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td>\n                    ')

                    # <Static value=<ast.Dict object at 0x1241572e0> name=None at 124157280> -> __attrs_4900347744
                    __attrs_4900347744 = _static_4900352736

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="historyByLine">\n                        ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900343280
                    __attrs_4900343280 = _static_4438893776
                    __stream_4900214080_actor = ''
                    __stream_4900214080_action = ''
                    __stream_4900214080_time = ''
                    __stream_4900343568 = []
                    __append_4900343568 = __stream_4900343568.append
                    __append_4900343568('\n                            ')
                    __stream_4900214080_action = []
                    __append_4900214080_action = __stream_4900214080_action.append

                    # <Static value=<ast.Dict object at 0x124155300> name=None at 1241552d0> -> __attrs_4900344912
                    __attrs_4900344912 = _static_4900344576

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_4900214080_action('<span')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900341744
                    __default_4900341744 = _DEFAULT_MARKER

                    # <Substitution 'string:historyAction state-${action_id}' (33:53)> -> __attr_class
                    __token = 1775
                    try:
                        __zt_tmp = __attrs_4900344912
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4439058528('string', 'historyAction state-${action_id}', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', 'historyAction', _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append_4900214080_action((' class="%s"' % __attr_class))
                    __append_4900214080_action('>')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900345680
                    __default_4900345680 = _DEFAULT_MARKER

                    # <Value 'action' (32:69)> -> __cache_4900346064
                    __token = 1677
                    try:
                        __zt_tmp = __attrs_4900344912
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4900346064 = _static_4439058528('path', 'action', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value 'action' (32:69)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 124155810> -> __condition
                    __expression = __cache_4900346064

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4900346064
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_4900214080_action(__content)
                    __append_4900214080_action('</span>')
                    __append_4900343568('${action}')
                    __stream_4900214080_action = ''.join(__stream_4900214080_action)
                    __append_4900343568('\n                            —\n                            ')
                    __stream_4900214080_actor = []
                    __append_4900214080_actor = __stream_4900214080_actor.append

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900346976
                    __attrs_4900346976 = _static_4438893776
                    __append_4900214080_actor('\n                             ')

                    # <Static value=<ast.Dict object at 0x12415beb0> name=None at 12415be80> -> __attrs_4900359904
                    __attrs_4900359904 = _static_4900372144

                    # <Value 'actor_home' (37:47)> -> __condition
                    __token = 1993
                    try:
                        __zt_tmp = __attrs_4900359904
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4439058528('path', 'actor_home', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append_4900214080_actor('<a')

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900372048
                        __default_4900372048 = _DEFAULT_MARKER

                        # <Substitution 'actor_home' (38:53)> -> __attr_href
                        __token = 2058
                        try:
                            __zt_tmp = __attrs_4900359904
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4439058528('path', 'actor_home', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append_4900214080_actor((' href="%s"' % __attr_href))
                        __append_4900214080_actor('>')

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900370896
                        __default_4900370896 = _DEFAULT_MARKER

                        # <Value 'actor_name' (39:45)> -> __cache_4900370512
                        __token = 2115
                        try:
                            __zt_tmp = __attrs_4900359904
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4900370512 = _static_4439058528('path', 'actor_name', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                        # <BinOp left=<Value 'actor_name' (39:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 12415bac0> -> __condition
                        __expression = __cache_4900370512

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append_4900214080_actor(' runyaga ')
                        else:
                            __content = __cache_4900370512
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_4900214080_actor(__content)
                        __append_4900214080_actor('</a>')
                    __append_4900214080_actor('\n                             ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900356496
                    __attrs_4900356496 = _static_4438893776

                    # <Value 'not: actor_home' (40:50)> -> __condition
                    __token = 2191
                    try:
                        __zt_tmp = __attrs_4900356496
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4439058528('not', ' actor_home', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900356304
                        __default_4900356304 = _DEFAULT_MARKER

                        # <Value 'actor_name' (41:48)> -> __cache_4900356832
                        __token = 2256
                        try:
                            __zt_tmp = __attrs_4900356496
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4900356832 = _static_4439058528('path', 'actor_name', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                        # <BinOp left=<Value 'actor_name' (41:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 124158310> -> __condition
                        __expression = __cache_4900356832

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append_4900214080_actor('<span/>')
                        else:
                            __content = __cache_4900356832
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_4900214080_actor(__content)
                    __append_4900214080_actor('\n                            ')
                    __append_4900343568('${actor}')
                    __stream_4900214080_actor = ''.join(__stream_4900214080_actor)
                    __append_4900343568('\n                            on\n                            ')
                    __stream_4900214080_time = []
                    __append_4900214080_time = __stream_4900214080_time.append

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900361248
                    __attrs_4900361248 = _static_4438893776

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_4900214080_time('<span>')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900361728
                    __default_4900361728 = _DEFAULT_MARKER

                    # <Value "python:view.toLocalizedTime(item['time'],long_format=True)" (44:82)> -> __cache_4900345968
                    __token = 2424
                    try:
                        __zt_tmp = __attrs_4900361248
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4900345968 = _static_4439058528('python', "view.toLocalizedTime(item['time'],long_format=True)", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:view.toLocalizedTime(item['time'],long_format=True)" (44:82)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 124158430> -> __condition
                    __expression = __cache_4900345968

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4900345968
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_4900214080_time(__content)
                    __append_4900214080_time('</span>')
                    __append_4900343568('${time}')
                    __stream_4900214080_time = ''.join(__stream_4900214080_time)
                    __append_4900343568('\n                        ')
                    __msgid_4900343568 = __re_whitespace(''.join(__stream_4900343568)).strip()
                    if 'history_action':
                        __append(translate('history_action', mapping={'time': __stream_4900214080_time, 'action': __stream_4900214080_action, 'actor': __stream_4900214080_actor, }, default=__msgid_4900343568, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n                        ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900357984
                    __attrs_4900357984 = _static_4438893776

                    # <Value 'effective|nothing' (46:54)> -> __condition
                    __token = 2578
                    try:
                        __zt_tmp = __attrs_4900357984
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4439058528('path', 'effective|nothing', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    if __condition:
                        __append('\n                            (')

                        # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900363024
                        __attrs_4900363024 = _static_4438893776
                        __stream_4900362976 = []
                        __append_4900362976 = __stream_4900362976.append
                        __append_4900362976('effective')
                        __msgid_4900362976 = __re_whitespace(''.join(__stream_4900362976)).strip()
                        if 'label_publishing_effective':
                            __append(translate('label_publishing_effective', mapping=None, default=__msgid_4900362976, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))

                        # <Interpolation value=<Substitution ': ${effectiveDate})\n                        ' (47:111)> braces_required=True translation=False default='"?"' default_marker='"?"' at 124158d90> -> __content_4340547312
                        __token = 2709
                        __token = 2713
                        try:
                            __zt_tmp = __attrs_4900357984
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_4340547312 = _static_4439058528('path', 'effectiveDate', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        __content_4340547312 = __quote(__content_4340547312, '\x00', '&#0;', None, None)
                        __content_4340547312 = ('%s%s%s' % (': ', (__content_4340547312 if (__content_4340547312 is not None) else ''), ')\n                        ', ))
                        if (__content_4340547312 is None):
                            pass
                        else:
                            if (__content_4340547312 is None):
                                __content_4340547312 = None
                            else:
                                __tt = type(__content_4340547312)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __content_4340547312 = str(__content_4340547312)
                                else:
                                    if (__tt is bytes):
                                        __content_4340547312 = decode(__content_4340547312)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __content_4340547312 = __content_4340547312.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__content_4340547312)
                                                __content_4340547312 = (str(__content_4340547312) if (__content_4340547312 is __converted) else __converted)
                                            else:
                                                __content_4340547312 = __content_4340547312()
                        if (__content_4340547312 is not None):
                            __append(__content_4340547312)
                    __append('\n\n                    </span>\n                    ')

                    # <Static value=<ast.Dict object at 0x124154af0> name=None at 124154a30> -> __attrs_4900362544
                    __attrs_4900362544 = _static_4900342512

                    # <Value 'rhComments' (51:57)> -> __condition
                    __token = 2856
                    try:
                        __zt_tmp = __attrs_4900362544
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4439058528('path', 'rhComments', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    if __condition:

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append('<p class="text-muted">\n                        ')

                        # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900363120
                        __attrs_4900363120 = _static_4438893776

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')
                        __stream_4900364512 = []
                        __append_4900364512 = __stream_4900364512.append
                        __append_4900364512('Change Note')
                        __msgid_4900364512 = __re_whitespace(''.join(__stream_4900364512)).strip()
                        if 'label_change_note':
                            __append(translate('label_change_note', mapping=None, default=__msgid_4900364512, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>:\n                        ')

                        # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900360576
                        __attrs_4900360576 = _static_4438893776

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900361152
                        __default_4900361152 = _DEFAULT_MARKER

                        # <Value 'rhComments' (53:61)> -> __cache_4900360912
                        __token = 3015
                        try:
                            __zt_tmp = __attrs_4900360576
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4900360912 = _static_4439058528('path', 'rhComments', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                        # <BinOp left=<Value 'rhComments' (53:61)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 124159300> -> __condition
                        __expression = __cache_4900360912

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4900360912
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>\n                    </p>')
                    __append('\n                </td>\n                ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900368256
                    __attrs_4900368256 = _static_4438893776

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td>\n                    ')

                    # <Static value=<ast.Dict object at 0x12415a500> name=None at 12415a590> -> __attrs_4900366336
                    __attrs_4900366336 = _static_4900365568

                    # <Value 'isVersion' (57:62)> -> __condition
                    __token = 3160
                    try:
                        __zt_tmp = __attrs_4900366336
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4439058528('path', 'isVersion', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="historyLinks">\n                        ')

                        # <Static value=<ast.Dict object at 0x12415b700> name=None at 12415ad40> -> __attrs_4900359328
                        __attrs_4900359328 = _static_4900370176

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="btn btn-primary"')

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900367296
                        __default_4900367296 = _DEFAULT_MARKER

                        # <Substitution 'item/preview_url' (59:49)> -> __attr_href
                        __token = 3280
                        try:
                            __zt_tmp = __attrs_4900359328
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4439058528('path', 'item/preview_url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>')
                        __stream_4900367056 = []
                        __append_4900367056 = __stream_4900367056.append
                        __append_4900367056('View')
                        __msgid_4900367056 = __re_whitespace(''.join(__stream_4900367056)).strip()
                        if 'title_view_revision':
                            __append(translate('title_view_revision', mapping=None, default=__msgid_4900367056, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</a>\n                    </span>')
                    __append('\n                </td>\n                ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900368880
                    __attrs_4900368880 = _static_4438893776

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td>\n                    ')

                    # <Static value=<ast.Dict object at 0x124158a30> name=None at 12415bb50> -> __attrs_4900371472
                    __attrs_4900371472 = _static_4900358704

                    # <Value 'isVersion' (64:62)> -> __condition
                    __token = 3505
                    try:
                        __zt_tmp = __attrs_4900371472
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4439058528('path', 'isVersion', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="historyLinks">\n                        ')

                        # <Static value=<ast.Dict object at 0x12412b190> name=None at 124128b80> -> __attrs_4900174864
                        __attrs_4900174864 = _static_4900172176

                        # <Value 'exists:item/diff_current_url' (66:43)> -> __condition
                        __token = 3665
                        try:
                            __zt_tmp = __attrs_4900174864
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4439058528('exists', 'item/diff_current_url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        if __condition:

                            # <a ... (0:0)
                            # --------------------------------------------------------
                            __append('<a class="btn btn-secondary"')

                            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900163536
                            __default_4900163536 = _DEFAULT_MARKER

                            # <Substitution 'item/diff_current_url' (65:82)> -> __attr_href
                            __token = 3599
                            try:
                                __zt_tmp = __attrs_4900174864
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href = _static_4439058528('path', 'item/diff_current_url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                            __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                            if (__attr_href is not None):
                                __append((' href="%s"' % __attr_href))
                            __append('>\n                            ')

                            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900175728
                            __attrs_4900175728 = _static_4438893776

                            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900163344
                            __default_4900163344 = _DEFAULT_MARKER

                            # <Value "python:icons.tag('arrow-up')" (67:57)> -> __cache_4900162864
                            __token = 3753
                            try:
                                __zt_tmp = __attrs_4900175728
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4900162864 = _static_4439058528('python', "icons.tag('arrow-up')", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                            # <BinOp left=<Value "python:icons.tag('arrow-up')" (67:57)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 12412bfd0> -> __condition
                            __expression = __cache_4900162864

                            # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_4900162864
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append('\n                            ')

                            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900173184
                            __attrs_4900173184 = _static_4438893776

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>')
                            __stream_4900175632 = []
                            __append_4900175632 = __stream_4900175632.append
                            __append_4900175632('Compare to current')
                            __msgid_4900175632 = __re_whitespace(''.join(__stream_4900175632)).strip()
                            if 'title_compare_revision':
                                __append(translate('title_compare_revision', mapping=None, default=__msgid_4900175632, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</span>\n                        </a>')
                        __append('\n                    </span>')
                    __append('\n                </td>\n                ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900173424
                    __attrs_4900173424 = _static_4438893776

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td>\n                    ')

                    # <Static value=<ast.Dict object at 0x124128ee0> name=None at 124128be0> -> __attrs_4900171600
                    __attrs_4900171600 = _static_4900163296

                    # <Value 'exists:item/diff_previous_url' (73:64)> -> __condition
                    __token = 4050
                    try:
                        __zt_tmp = __attrs_4900171600
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4439058528('exists', 'item/diff_previous_url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="btn btn-secondary"')

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900163872
                        __default_4900163872 = _DEFAULT_MARKER

                        # <Translate msgid='title_compare_previous_revision' node=<ast.Constant object at 0x1241290c0> at 1241295a0> -> __attr_title
                        __attr_title = 'Compare with previous revision'
                        __attr_title = translate('title_compare_previous_revision', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900172512
                        __default_4900172512 = _DEFAULT_MARKER

                        # <Substitution 'item/diff_previous_url' (74:45)> -> __attr_href
                        __token = 4126
                        try:
                            __zt_tmp = __attrs_4900171600
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4439058528('path', 'item/diff_previous_url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>\n                        ')

                        # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900165456
                        __attrs_4900165456 = _static_4438893776

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900163488
                        __default_4900163488 = _DEFAULT_MARKER

                        # <Value "python:icons.tag('arrow-down')" (77:53)> -> __cache_4900164928
                        __token = 4347
                        try:
                            __zt_tmp = __attrs_4900165456
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4900164928 = _static_4439058528('python', "icons.tag('arrow-down')", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:icons.tag('arrow-down')" (77:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 12412a5f0> -> __condition
                        __expression = __cache_4900164928

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4900164928
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n                        ')

                        # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4899296048
                        __attrs_4899296048 = _static_4438893776
                        __stream_4900172464 = []
                        __append_4900172464 = __stream_4900172464.append
                        __append_4900172464('Compare')
                        __msgid_4900172464 = __re_whitespace(''.join(__stream_4900172464)).strip()
                        if 'label_compare':
                            __append(translate('label_compare', mapping=None, default=__msgid_4900172464, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('\n                    </a>')
                    __append('\n                </td>\n                ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4899304640
                    __attrs_4899304640 = _static_4438893776

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td>\n                    ')

                    # <Static value=<ast.Dict object at 0x1241a8310> name=None at 1241a8340> -> __attrs_4900684944
                    __attrs_4900684944 = _static_4900684560

                    # <Value 'isVersion' (82:62)> -> __condition
                    __token = 4604
                    try:
                        __zt_tmp = __attrs_4900684944
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4439058528('path', 'isVersion', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="historyTools">\n                    ')

                        # <Static value=<ast.Dict object at 0x1241a8b50> name=None at 1241a87f0> -> __attrs_4900686960
                        __attrs_4900686960 = _static_4900686672

                        # <Value 'item/revert_url' (83:65)> -> __condition
                        __token = 4681
                        try:
                            __zt_tmp = __attrs_4900686960
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4439058528('path', 'item/revert_url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        if __condition:

                            # <form ... (0:0)
                            # --------------------------------------------------------
                            __append('<form')

                            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900686336
                            __default_4900686336 = _DEFAULT_MARKER

                            # <Substitution 'item/revert_url' (83:105)> -> __attr_action
                            __token = 4721
                            try:
                                __zt_tmp = __attrs_4900686960
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_action = _static_4439058528('path', 'item/revert_url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                            __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                            if (__attr_action is not None):
                                __append((' action="%s"' % __attr_action))
                            __append(' method="post">\n                        ')

                            # <Static value=<ast.Dict object at 0x1241a92d0> name=None at 1241a9300> -> __attrs_4900689120
                            __attrs_4900689120 = _static_4900688592

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input type="hidden" name="version_id"')

                            # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900687824
                            __default_4900687824 = _DEFAULT_MARKER

                            # <Substitution 'item/version_id' (84:94)> -> __attr_value
                            __token = 4833
                            try:
                                __zt_tmp = __attrs_4900689120
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_4439058528('path', 'item/version_id', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))
                            __append(' />\n                        ')

                            # <Static value=<ast.Dict object at 0x1241a9a50> name=None at 1241a96c0> -> __attrs_4900690608
                            __attrs_4900690608 = _static_4900690512

                            # <Value 'exists:item/diff_current_url' (86:47)> -> __condition
                            __token = 4970
                            try:
                                __zt_tmp = __attrs_4900690608
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4439058528('exists', 'item/diff_current_url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                            if __condition:

                                # <button ... (0:0)
                                # --------------------------------------------------------
                                __append('<button class="btn btn-warning" type="submit">')
                                __stream_4900689504 = []
                                __append_4900689504 = __stream_4900689504.append
                                __append_4900689504('Revert to this revision')
                                __msgid_4900689504 = __re_whitespace(''.join(__stream_4900689504)).strip()
                                if 'title_revert_revision':
                                    __append(translate('title_revert_revision', mapping=None, default=__msgid_4900689504, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                __append('</button>')
                            __append('\n                    </form>')
                        __append('\n                    </span>')
                    __append('\n                </td>\n            </tr>\n            ')
                    if (__backup_icons_4879774000 is __marker):
                        del econtext['icons']
                    else:
                        econtext['icons'] = __backup_icons_4879774000
                    if (__backup_isVersion_4877784432 is __marker):
                        del econtext['isVersion']
                    else:
                        econtext['isVersion'] = __backup_isVersion_4877784432
                    if (__backup_effectiveDate_4877785296 is __marker):
                        del econtext['effectiveDate']
                    else:
                        econtext['effectiveDate'] = __backup_effectiveDate_4877785296
                    if (__backup_effective_4877783808 is __marker):
                        del econtext['effective']
                    else:
                        econtext['effective'] = __backup_effective_4877783808
                    if (__backup_action_id_4841591072 is __marker):
                        del econtext['action_id']
                    else:
                        econtext['action_id'] = __backup_action_id_4841591072
                    if (__backup_action_4841599136 is __marker):
                        del econtext['action']
                    else:
                        econtext['action'] = __backup_action_4841599136
                    if (__backup_actor_home_4841595536 is __marker):
                        del econtext['actor_home']
                    else:
                        econtext['actor_home'] = __backup_actor_home_4841595536
                    if (__backup_actor_name_4880315296 is __marker):
                        del econtext['actor_name']
                    else:
                        econtext['actor_name'] = __backup_actor_name_4880315296
                    if (__backup_actor_4880311216 is __marker):
                        del econtext['actor']
                    else:
                        econtext['actor'] = __backup_actor_4880311216
                    if (__backup_rhComments_4877565472 is __marker):
                        del econtext['rhComments']
                    else:
                        econtext['rhComments'] = __backup_rhComments_4877565472
                    __append('\n            ')
                    ____index_4900354032 -= 1
                    if (____index_4900354032 > 0):
                        __append('')
                if (__backup_item_4874862800 is __marker):
                    del econtext['item']
                else:
                    econtext['item'] = __backup_item_4874862800
                __append('\n        </tbody>\n    </table>')
            __append('\n\n')
            __i18n_domain = __previous_i18n_domain_4900478240
            if (__backup_history_4880304448 is __marker):
                del econtext['history']
            else:
                econtext['history'] = __backup_history_4880304448
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }