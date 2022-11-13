# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/dexterity/browser/container.pt'

__tokens = {451: ('view/widgets/values|nothing', 13, 28), 513: ("python:widget.__name__ not in ('IBasic.title', 'IBasic.description', 'title', 'description',)", 14, 32), 654: ('widget/@@ploneform-render-widget', 15, 45), 755: ('view/groups|nothing', 19, 30), 807: ("python:''.join((group.prefix, 'groups.', group.__name__)).replace('.', '-')", 20, 31), 912: ('group/label', 21, 27), 964: ('group/widgets/values', 22, 36), 1032: ('widget/@@ploneform-render-widget', 23, 45), 1235: ('nocall:context/folder_listing', 29, 30), 1279: (' view/macros/listing|view/index/macros/listin', 29, 74), 1366: ('listing_macro', 30, 38), 1366: ('listing_macro', 30, 38), 261: ('context/@@main_template/macros/master', 6, 23), 261: ('context/@@main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4900718624 = 'master'
_static_4901952752 = 'listing_macro'
_static_4903358560 = {'id': 'folder-listing', }
_static_4903365904 = {'id': "python:''.join((group.prefix, 'groups.', group.__name__)).replace('.', '-')", }
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

    def render_content_core(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903364944
            __attrs_4903364944 = _static_4438893776
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903366048
            __attrs_4903366048 = _static_4438893776
            __backup_widget_4855517712 = get('widget', __marker)

            # <Value 'view/widgets/values|nothing' (13:28)> -> __iterator
            __token = 451
            try:
                __zt_tmp = __attrs_4903366048
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4439058528('path', 'view/widgets/values|nothing', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            (__iterator, ____index_4903366960, ) = getname('repeat')('widget', __iterator)
            econtext['widget'] = None
            for __item in __iterator:
                econtext['widget'] = __item
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903367488
                __attrs_4903367488 = _static_4438893776

                # <Value "python:widget.__name__ not in ('IBasic.title', 'IBasic.description', 'title', 'description',)" (14:32)> -> __condition
                __token = 513
                try:
                    __zt_tmp = __attrs_4903367488
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('python', "widget.__name__ not in ('IBasic.title', 'IBasic.description', 'title', 'description',)", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903370128
                    __attrs_4903370128 = _static_4438893776

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4903370368
                    __default_4903370368 = _DEFAULT_MARKER

                    # <Value 'widget/@@ploneform-render-widget' (15:45)> -> __cache_4903368352
                    __token = 654
                    try:
                        __zt_tmp = __attrs_4903370128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4903368352 = _static_4439058528('path', 'widget/@@ploneform-render-widget', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value 'widget/@@ploneform-render-widget' (15:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 124437a90> -> __condition
                    __expression = __cache_4903368352

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4903368352
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')
                __append('\n  ')
                ____index_4903366960 -= 1
                if (____index_4903366960 > 0):
                    __append('')
            if (__backup_widget_4855517712 is __marker):
                del econtext['widget']
            else:
                econtext['widget'] = __backup_widget_4855517712
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x124436d10> name=None at 124436800> -> __attrs_4903362016
            __attrs_4903362016 = _static_4903365904
            __backup_group_4880698096 = get('group', __marker)

            # <Value 'view/groups|nothing' (19:30)> -> __iterator
            __token = 755
            try:
                __zt_tmp = __attrs_4903362016
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4439058528('path', 'view/groups|nothing', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            (__iterator, ____index_4903361776, ) = getname('repeat')('group', __iterator)
            econtext['group'] = None
            for __item in __iterator:
                econtext['group'] = __item

                # <fieldset ... (0:0)
                # --------------------------------------------------------
                __append('<fieldset')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4903365088
                __default_4903365088 = _DEFAULT_MARKER

                # <Substitution "python:''.join((group.prefix, 'groups.', group.__name__)).replace('.', '-')" (20:31)> -> __attr_id
                __token = 807
                try:
                    __zt_tmp = __attrs_4903362016
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_4439058528('python', "''.join((group.prefix, 'groups.', group.__name__)).replace('.', '-')", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))
                __append('>\n      ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903360192
                __attrs_4903360192 = _static_4438893776

                # <legend ... (0:0)
                # --------------------------------------------------------
                __append('<legend>')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4903360768
                __default_4903360768 = _DEFAULT_MARKER

                # <Value 'group/label' (21:27)> -> __cache_4903361248
                __token = 912
                try:
                    __zt_tmp = __attrs_4903360192
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4903361248 = _static_4439058528('path', 'group/label', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'group/label' (21:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 124435a20> -> __condition
                __expression = __cache_4903361248

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4903361248
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</legend>\n      ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903359520
                __attrs_4903359520 = _static_4438893776
                __backup_widget_4879964752 = get('widget', __marker)

                # <Value 'group/widgets/values' (22:36)> -> __iterator
                __token = 964
                try:
                    __zt_tmp = __attrs_4903359520
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4439058528('path', 'group/widgets/values', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                (__iterator, ____index_4903359280, ) = getname('repeat')('widget', __iterator)
                econtext['widget'] = None
                for __item in __iterator:
                    econtext['widget'] = __item
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903356880
                    __attrs_4903356880 = _static_4438893776

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4903357840
                    __default_4903357840 = _DEFAULT_MARKER

                    # <Value 'widget/@@ploneform-render-widget' (23:45)> -> __cache_4903358512
                    __token = 1032
                    try:
                        __zt_tmp = __attrs_4903356880
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4903358512 = _static_4439058528('path', 'widget/@@ploneform-render-widget', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value 'widget/@@ploneform-render-widget' (23:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 124434f40> -> __condition
                    __expression = __cache_4903358512

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4903358512
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')
                    ____index_4903359280 -= 1
                    if (____index_4903359280 > 0):
                        __append('')
                if (__backup_widget_4879964752 is __marker):
                    del econtext['widget']
                else:
                    econtext['widget'] = __backup_widget_4879964752
                __append('\n  </fieldset>')
                ____index_4903361776 -= 1
                if (____index_4903361776 > 0):
                    __append('\n  ')
            if (__backup_group_4880698096 is __marker):
                del econtext['group']
            else:
                econtext['group'] = __backup_group_4880698096
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x124435060> name=None at 1244350f0> -> __attrs_4903357744
            __attrs_4903357744 = _static_4903358560

            # <fieldset ... (0:0)
            # --------------------------------------------------------
            __append('<fieldset id="folder-listing">\n      ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903357456
            __attrs_4903357456 = _static_4438893776
            __previous_i18n_domain_4903355632 = __i18n_domain
            __i18n_domain = 'plone'

            # <legend ... (0:0)
            # --------------------------------------------------------
            __append('<legend>')
            __stream_4903356496 = []
            __append_4903356496 = __stream_4903356496.append
            __append_4903356496('Contents')
            __msgid_4903356496 = __re_whitespace(''.join(__stream_4903356496)).strip()
            if __msgid_4903356496:
                __append(translate(__msgid_4903356496, mapping=None, default=__msgid_4903356496, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</legend>')
            __i18n_domain = __previous_i18n_domain_4903355632
            __append('\n      ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903356784
            __attrs_4903356784 = _static_4438893776
            __backup_view_4880703136 = get('view', __marker)

            # <Value 'nocall:context/folder_listing' (29:30)> -> __value
            __token = 1235
            try:
                __zt_tmp = __attrs_4903356784
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('nocall', 'context/folder_listing', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['view'] = __value
            __backup_listing_macro_4880493936 = get('listing_macro', __marker)

            # <Value 'view/macros/listing|view/index/macros/listing' (29:74)> -> __value
            __token = 1279
            try:
                __zt_tmp = __attrs_4903356784
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'view/macros/listing|view/index/macros/listing', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['listing_macro'] = __value
            __append('\n          ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901952656
            __attrs_4901952656 = _static_4438893776
            __backup_macroname_4903457152 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x1242ddcf0> name=None at 1242ddfc0> -> __value
            __value = _static_4901952752
            econtext['macroname'] = __value

            # <Value 'listing_macro' (30:38)> -> __macro
            __token = 1366
            try:
                __zt_tmp = __attrs_4901952656
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4439058528('path', 'listing_macro', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __token = 1366
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4903457152 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4903457152
            __append('\n      ')
            if (__backup_listing_macro_4880493936 is __marker):
                del econtext['listing_macro']
            else:
                econtext['listing_macro'] = __backup_listing_macro_4880493936
            if (__backup_view_4880703136 is __marker):
                del econtext['view']
            else:
                econtext['view'] = __backup_view_4880703136
            __append('\n  </fieldset>\n\n')
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900718000
            __attrs_4900718000 = _static_4438893776
            __previous_i18n_domain_4900724816 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4903297088 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x1241b0820> name=None at 1241b0250> -> __value
            __value = _static_4900718624
            econtext['macroname'] = __value

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900725536
                __attrs_4900725536 = _static_4438893776
                __append('\n')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/@@main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_4900718000
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4439058528('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4903297088 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4903297088
            __i18n_domain = __previous_i18n_domain_4900724816
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render': render, }