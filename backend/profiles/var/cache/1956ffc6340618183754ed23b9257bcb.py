# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/event/browser/event_listing.pt'

__tokens = {2115: ('view/events', 62, 31), 2160: (' nocall: context/@@plone/toLocalizedTim', 63, 32), 2262: ('batch', 67, 36), 2485: ('python:view.date_speller(data.start)', 73, 37), 2708: ('data/start/isoformat', 79, 35), 2873: ('data/end/isoformat', 83, 35), 3201: ('data/location', 91, 37), 3468: ('string:${startf/month_name}', 98, 35), 3713: ('string:${startf/day}', 103, 37), 3858: ("python:startf['wkday_name']", 106, 37), 4214: ('data/url', 116, 45), 4376: ('data/title', 120, 39), 4550: ('python:view.formatted_date(data)', 124, 53), 4758: ('data/description', 130, 37), 4811: ('data/description', 131, 35), 4964: ('context/batch_macros/macros/navigation', 142, 32), 4964: ('context/batch_macros/macros/navigation', 142, 32), 416: ('view/header_string', 14, 27), 556: ('header/main', 18, 27), 516: ('header/main', 17, 25), 612: ('request/mode|string:future', 20, 28), 651: (' view/show_filte', 20, 67), 761: ('show_filter', 22, 31), 855: ("python:mode=='past'", 25, 31), 1006: ('view/mode_future_url', 29, 39), 1191: ("python:mode=='future'", 34, 31), 1342: ('view/mode_past_url', 38, 39), 1612: ('view/ical_url', 46, 37), 1944: ('header/sub', 57, 25), 1907: ('header/sub', 56, 23), 259: ('context/main_template/macros/master', 8, 21), 259: ('context/main_template/macros/master', 8, 21)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4900793856 = {'class': 'mode_ical nav-link', 'href': '', 'title': 'Download this event in iCal format', }
_static_4900340928 = {'class': 'nav-item', }
_static_4900354176 = {'class': 'mode_past nav-link', 'href': '', }
_static_4900354944 = {'class': 'nav-item', }
_static_4900346304 = {'class': 'mode_future nav-link', 'href': '', }
_static_4900340496 = {'class': 'nav-item', }
_static_4901039856 = {'class': 'mode_selector nav justify-content-end', }
_static_4903062976 = {'class': 'documentFirstHeading', }
_static_4901607392 = 'master'
_static_4900784112 = 'navigation'
_static_4903354528 = {'itemprop': 'description', 'class': 'description', }
_static_4903355536 = {'class': 'documentByLine', }
_static_4903359520 = {'itemprop': 'name', 'class': 'summary', }
_static_4903355392 = {'href': '', 'itemprop': 'url', 'class': 'url', }
_static_4903358464 = {'class': 'tileHeadline', }
_static_4903355152 = {'class': 'cal_info clearfix', }
_static_4903362352 = {'class': 'cal_wkday card-text', }
_static_4881123024 = {'class': 'cal_day card-title fs-1 m-0', }
_static_4844383696 = {'class': 'card-body d-flex flex-column p-2', }
_static_4903005552 = {'class': 'cal_month card-header p-2', }
_static_4902995328 = {'class': 'cal_date card me-3 flex-shrink-0 text-center', }
_static_4902996336 = {'itemprop': 'address', }
_static_4903002816 = {'class': 'location', 'itemscope': '', 'itemprop': 'location', 'itemtype': 'http://schema.org/Place', }
_static_4903008384 = {'itemprop': 'endDate', 'class': 'dtend', }
_static_4900731248 = {'itemprop': 'startDate', 'class': 'dtstart', }
_static_4900796256 = {'class': 'hiddenStructure', }
_static_4900795680 = {'itemscope': '', 'itemtype': 'https://schema.org/Event', 'class': 'vevent tileItem d-flex align-items-start mb-3', }
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900786368
            __attrs_4900786368 = _static_4438893776
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900793424
            __attrs_4900793424 = _static_4438893776
            __backup_batch_4880492640 = get('batch', __marker)

            # <Value 'view/events' (62:31)> -> __value
            __token = 2115
            try:
                __zt_tmp = __attrs_4900793424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('path', 'view/events', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['batch'] = __value
            __backup_toLocalizedTime_4881070688 = get('toLocalizedTime', __marker)

            # <Value 'nocall: context/@@plone/toLocalizedTime' (63:32)> -> __value
            __token = 2160
            try:
                __zt_tmp = __attrs_4900793424
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4439058528('nocall', ' context/@@plone/toLocalizedTime', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            econtext['toLocalizedTime'] = __value
            __append('\n\n          ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900793232
            __attrs_4900793232 = _static_4438893776

            # <section ... (0:0)
            # --------------------------------------------------------
            __append('<section>\n\n            ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900789104
            __attrs_4900789104 = _static_4438893776
            __backup_data_4900719392 = get('data', __marker)

            # <Value 'batch' (67:36)> -> __iterator
            __token = 2262
            try:
                __zt_tmp = __attrs_4900789104
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4439058528('path', 'batch', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            (__iterator, ____index_4900795920, ) = getname('repeat')('data', __iterator)
            econtext['data'] = None
            for __item in __iterator:
                econtext['data'] = __item
                __append('\n\n              ')

                # <Static value=<ast.Dict object at 0x1241c3520> name=None at 1241c12a0> -> __attrs_4900794864
                __attrs_4900794864 = _static_4900795680
                __backup_startf_4880312416 = get('startf', __marker)

                # <Value 'python:view.date_speller(data.start)' (73:37)> -> __value
                __token = 2485
                try:
                    __zt_tmp = __attrs_4900794864
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('python', 'view.date_speller(data.start)', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['startf'] = __value

                # <article ... (0:0)
                # --------------------------------------------------------
                __append('<article itemscope itemtype="https://schema.org/Event" class="vevent tileItem d-flex align-items-start mb-3">\n\n                ')

                # <Static value=<ast.Dict object at 0x1241c3760> name=None at 1241c2f50> -> __attrs_4900787520
                __attrs_4900787520 = _static_4900796256

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="hiddenStructure">\n                  ')

                # <Static value=<ast.Dict object at 0x1241b3970> name=None at 1241b1480> -> __attrs_4900723712
                __attrs_4900723712 = _static_4900731248

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li itemprop="startDate" class="dtstart">')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900718480
                __default_4900718480 = _DEFAULT_MARKER

                # <Value 'data/start/isoformat' (79:35)> -> __cache_4900728800
                __token = 2708
                try:
                    __zt_tmp = __attrs_4900723712
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4900728800 = _static_4439058528('path', 'data/start/isoformat', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'data/start/isoformat' (79:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1241b04c0> -> __condition
                __expression = __cache_4900728800

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('end')
                else:
                    __content = __cache_4900728800
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</li>\n                  ')

                # <Static value=<ast.Dict object at 0x1243df880> name=None at 1243ddcc0> -> __attrs_4902999216
                __attrs_4902999216 = _static_4903008384

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li itemprop="endDate" class="dtend">')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4902998880
                __default_4902998880 = _DEFAULT_MARKER

                # <Value 'data/end/isoformat' (83:35)> -> __cache_4900719152
                __token = 2873
                try:
                    __zt_tmp = __attrs_4902999216
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4900719152 = _static_4439058528('path', 'data/end/isoformat', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'data/end/isoformat' (83:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1241b3880> -> __condition
                __expression = __cache_4900719152

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('end')
                else:
                    __content = __cache_4900719152
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</li>\n                  ')

                # <Static value=<ast.Dict object at 0x1243de2c0> name=None at 1243dd000> -> __attrs_4902994800
                __attrs_4902994800 = _static_4903002816

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li class="location" itemscope itemprop="location" itemtype="http://schema.org/Place">\n                    ')

                # <Static value=<ast.Dict object at 0x1243dc970> name=None at 1243df070> -> __attrs_4902994944
                __attrs_4902994944 = _static_4902996336

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span itemprop="address">')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4903004688
                __default_4903004688 = _DEFAULT_MARKER

                # <Value 'data/location' (91:37)> -> __cache_4903007328
                __token = 3201
                try:
                    __zt_tmp = __attrs_4902994944
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4903007328 = _static_4439058528('path', 'data/location', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'data/location' (91:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1243dc430> -> __condition
                __expression = __cache_4903007328

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('location')
                else:
                    __content = __cache_4903007328
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</span>\n                  </li>\n                </ul>\n\n                ')

                # <Static value=<ast.Dict object at 0x1243dc580> name=None at 1243dffd0> -> __attrs_4902998496
                __attrs_4902998496 = _static_4902995328

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="cal_date card me-3 flex-shrink-0 text-center">\n                  ')

                # <Static value=<ast.Dict object at 0x1243ded70> name=None at 1243df790> -> __attrs_4844387824
                __attrs_4844387824 = _static_4903005552

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="cal_month card-header p-2">')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4902998448
                __default_4902998448 = _DEFAULT_MARKER

                # <Value 'string:${startf/month_name}' (98:35)> -> __cache_4903005696
                __token = 3468
                try:
                    __zt_tmp = __attrs_4844387824
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4903005696 = _static_4439058528('string', '${startf/month_name}', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'string:${startf/month_name}' (98:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1243de1a0> -> __condition
                __expression = __cache_4903005696

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Oct.\n                  ')
                else:
                    __content = __cache_4903005696
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</div>\n                  ')

                # <Static value=<ast.Dict object at 0x120bf6dd0> name=None at 120bf42e0> -> __attrs_4881127872
                __attrs_4881127872 = _static_4844383696

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="card-body d-flex flex-column p-2">\n                    ')

                # <Static value=<ast.Dict object at 0x122f006d0> name=None at 1217862c0> -> __attrs_4903364704
                __attrs_4903364704 = _static_4881123024

                # <h3 ... (0:0)
                # --------------------------------------------------------
                __append('<h3 class="cal_day card-title fs-1 m-0">')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4881134304
                __default_4881134304 = _DEFAULT_MARKER

                # <Value 'string:${startf/day}' (103:37)> -> __cache_4881133680
                __token = 3713
                try:
                    __zt_tmp = __attrs_4903364704
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4881133680 = _static_4439058528('string', '${startf/day}', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'string:${startf/day}' (103:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 122f030a0> -> __condition
                __expression = __cache_4881133680

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('15')
                else:
                    __content = __cache_4881133680
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</h3>\n                    ')

                # <Static value=<ast.Dict object at 0x124435f30> name=None at 1244369b0> -> __attrs_4903368688
                __attrs_4903368688 = _static_4903362352

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span class="cal_wkday card-text">')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4903354720
                __default_4903354720 = _DEFAULT_MARKER

                # <Value "python:startf['wkday_name']" (106:37)> -> __cache_4903360048
                __token = 3858
                try:
                    __zt_tmp = __attrs_4903368688
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4903360048 = _static_4439058528('python', "startf['wkday_name']", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value "python:startf['wkday_name']" (106:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 124437df0> -> __condition
                __expression = __cache_4903360048

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Tue')
                else:
                    __content = __cache_4903360048
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</span>\n                  </div>\n                </div>\n\n                ')

                # <Static value=<ast.Dict object at 0x124434310> name=None at 124436d40> -> __attrs_4903362688
                __attrs_4903362688 = _static_4903355152

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="cal_info clearfix">\n                  ')

                # <Static value=<ast.Dict object at 0x124435000> name=None at 124436b00> -> __attrs_4903364848
                __attrs_4903364848 = _static_4903358464

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2 class="tileHeadline">\n                    ')

                # <Static value=<ast.Dict object at 0x124434400> name=None at 124435960> -> __attrs_4903364032
                __attrs_4903364032 = _static_4903355392

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4903356928
                __default_4903356928 = _DEFAULT_MARKER

                # <Substitution 'data/url' (116:45)> -> __attr_href
                __token = 4214
                try:
                    __zt_tmp = __attrs_4903364032
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4439058528('path', 'data/url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' itemprop="url" class="url">\n                      ')

                # <Static value=<ast.Dict object at 0x124435420> name=None at 124434f70> -> __attrs_4903354480
                __attrs_4903354480 = _static_4903359520

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span itemprop="name" class="summary">')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4903361056
                __default_4903361056 = _DEFAULT_MARKER

                # <Value 'data/title' (120:39)> -> __cache_4903366768
                __token = 4376
                try:
                    __zt_tmp = __attrs_4903354480
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4903366768 = _static_4439058528('path', 'data/title', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'data/title' (120:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 124437760> -> __condition
                __expression = __cache_4903366768

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Title')
                else:
                    __content = __cache_4903366768
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</span>\n                    </a>\n                  </h2>\n                  ')

                # <Static value=<ast.Dict object at 0x124434490> name=None at 124434850> -> __attrs_4903361680
                __attrs_4903361680 = _static_4903355536

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="documentByLine">\n                    ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903362544
                __attrs_4903362544 = _static_4438893776

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4903369840
                __default_4903369840 = _DEFAULT_MARKER

                # <Value 'python:view.formatted_date(data)' (124:53)> -> __cache_4903355008
                __token = 4550
                try:
                    __zt_tmp = __attrs_4903362544
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4903355008 = _static_4439058528('python', 'view.formatted_date(data)', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:view.formatted_date(data)' (124:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 124434ca0> -> __condition
                __expression = __cache_4903355008

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4903355008
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n                  </div>\n\n                  ')

                # <Static value=<ast.Dict object at 0x1244340a0> name=None at 124436a40> -> __attrs_4880311120
                __attrs_4880311120 = _static_4903354528

                # <Value 'data/description' (130:37)> -> __condition
                __token = 4758
                try:
                    __zt_tmp = __attrs_4880311120
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('path', 'data/description', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p itemprop="description" class="description">')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4903360624
                    __default_4903360624 = _DEFAULT_MARKER

                    # <Value 'data/description' (131:35)> -> __cache_4903368448
                    __token = 4811
                    try:
                        __zt_tmp = __attrs_4880311120
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4903368448 = _static_4439058528('path', 'data/description', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value 'data/description' (131:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 124437850> -> __condition
                    __expression = __cache_4903368448

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4903368448
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</p>')
                __append('\n\n\n                </div>\n\n              </article>')
                if (__backup_startf_4880312416 is __marker):
                    del econtext['startf']
                else:
                    econtext['startf'] = __backup_startf_4880312416
                __append('\n\n            ')
                ____index_4900795920 -= 1
                if (____index_4900795920 > 0):
                    __append('')
            if (__backup_data_4900719392 is __marker):
                del econtext['data']
            else:
                econtext['data'] = __backup_data_4900719392
            __append('\n\n          </section>\n\n          ')

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4880305504
            __attrs_4880305504 = _static_4438893776
            __backup_macroname_4696927424 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x1241c07f0> name=None at 1241c1390> -> __value
            __value = _static_4900784112
            econtext['macroname'] = __value

            # <Value 'context/batch_macros/macros/navigation' (142:32)> -> __macro
            __token = 4964
            try:
                __zt_tmp = __attrs_4880305504
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4439058528('path', 'context/batch_macros/macros/navigation', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __token = 4964
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4696927424 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4696927424
            __append('\n\n        ')
            if (__backup_toLocalizedTime_4881070688 is __marker):
                del econtext['toLocalizedTime']
            else:
                econtext['toLocalizedTime'] = __backup_toLocalizedTime_4881070688
            if (__backup_batch_4880492640 is __marker):
                del econtext['batch']
            else:
                econtext['batch'] = __backup_batch_4880492640
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

            # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901613680
            __attrs_4901613680 = _static_4438893776
            __previous_i18n_domain_4901613248 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4680504704 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x1242897e0> name=None at 12428b9d0> -> __value
            __value = _static_4901607392
            econtext['macroname'] = __value

            def __fill_content_title(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4880498544
                __attrs_4880498544 = _static_4438893776
                __backup_header_4881066896 = get('header', __marker)

                # <Value 'view/header_string' (14:27)> -> __value
                __token = 416
                try:
                    __zt_tmp = __attrs_4880498544
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'view/header_string', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['header'] = __value
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x1243ecdc0> name=None at 1243ecc40> -> __attrs_4903064416
                __attrs_4903064416 = _static_4903062976

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">\n        ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4903067536
                __attrs_4903067536 = _static_4438893776

                # <Value 'header/main' (18:27)> -> __condition
                __token = 556
                try:
                    __zt_tmp = __attrs_4903067536
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('path', 'header/main', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4903059616
                    __default_4903059616 = _DEFAULT_MARKER

                    # <Value 'header/main' (17:25)> -> __cache_4903062208
                    __token = 516
                    try:
                        __zt_tmp = __attrs_4903067536
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4903062208 = _static_4439058528('path', 'header/main', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value 'header/main' (17:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1243ef9d0> -> __condition
                    __expression = __cache_4903062208

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span />')
                    else:
                        __content = __cache_4903062208
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                __append('\n      </h1>\n      ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4901032320
                __attrs_4901032320 = _static_4438893776
                __backup_mode_4880490288 = get('mode', __marker)

                # <Value 'request/mode|string:future' (20:28)> -> __value
                __token = 612
                try:
                    __zt_tmp = __attrs_4901032320
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'request/mode|string:future', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['mode'] = __value
                __backup_show_filter_4880485920 = get('show_filter', __marker)

                # <Value 'view/show_filter' (20:67)> -> __value
                __token = 651
                try:
                    __zt_tmp = __attrs_4901032320
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4439058528('path', 'view/show_filter', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                econtext['show_filter'] = __value

                # <nav ... (0:0)
                # --------------------------------------------------------
                __append('<nav>\n        ')

                # <Static value=<ast.Dict object at 0x1241feef0> name=None at 1241fcca0> -> __attrs_4901043408
                __attrs_4901043408 = _static_4901039856

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="mode_selector nav justify-content-end">\n          ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900346928
                __attrs_4900346928 = _static_4438893776

                # <Value 'show_filter' (22:31)> -> __condition
                __token = 761
                try:
                    __zt_tmp = __attrs_4900346928
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('path', 'show_filter', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x124154310> name=None at 1241565c0> -> __attrs_4900347264
                    __attrs_4900347264 = _static_4900340496

                    # <Value "python:mode=='past'" (25:31)> -> __condition
                    __token = 855
                    try:
                        __zt_tmp = __attrs_4900347264
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4439058528('python', "mode=='past'", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="nav-item">\n              ')

                        # <Static value=<ast.Dict object at 0x1241559c0> name=None at 124156380> -> __attrs_4900353120
                        __attrs_4900353120 = _static_4900346304

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="mode_future nav-link"')

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900354272
                        __default_4900354272 = _DEFAULT_MARKER

                        # <Substitution 'view/mode_future_url' (29:39)> -> __attr_href
                        __token = 1006
                        try:
                            __zt_tmp = __attrs_4900353120
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4439058528('path', 'view/mode_future_url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>')
                        __stream_4900350864 = []
                        __append_4900350864 = __stream_4900350864.append
                        __append_4900350864('Upcoming')
                        __msgid_4900350864 = __re_whitespace(''.join(__stream_4900350864)).strip()
                        if 'mode_future_link':
                            __append(translate('mode_future_link', mapping=None, default=__msgid_4900350864, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</a>\n            </li>')
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x124157b80> name=None at 124154580> -> __attrs_4900352304
                    __attrs_4900352304 = _static_4900354944

                    # <Value "python:mode=='future'" (34:31)> -> __condition
                    __token = 1191
                    try:
                        __zt_tmp = __attrs_4900352304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4439058528('python', "mode=='future'", econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="nav-item">\n              ')

                        # <Static value=<ast.Dict object at 0x124157880> name=None at 124155450> -> __attrs_4900348080
                        __attrs_4900348080 = _static_4900354176

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="mode_past nav-link"')

                        # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900355664
                        __default_4900355664 = _DEFAULT_MARKER

                        # <Substitution 'view/mode_past_url' (38:39)> -> __attr_href
                        __token = 1342
                        try:
                            __zt_tmp = __attrs_4900348080
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4439058528('path', 'view/mode_past_url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>')
                        __stream_4900353552 = []
                        __append_4900353552 = __stream_4900353552.append
                        __append_4900353552('Past')
                        __msgid_4900353552 = __re_whitespace(''.join(__stream_4900353552)).strip()
                        if 'mode_past_link':
                            __append(translate('mode_past_link', mapping=None, default=__msgid_4900353552, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</a>\n            </li>')
                    __append('\n          ')
                __append('\n          ')

                # <Static value=<ast.Dict object at 0x1241544c0> name=None at 124154670> -> __attrs_4900797888
                __attrs_4900797888 = _static_4900340928

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li class="nav-item">\n            ')

                # <Static value=<ast.Dict object at 0x1241c2e00> name=None at 1241c3c10> -> __attrs_4900796736
                __attrs_4900796736 = _static_4900793856

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="mode_ical nav-link"')

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900790544
                __default_4900790544 = _DEFAULT_MARKER

                # <Substitution 'view/ical_url' (46:37)> -> __attr_href
                __token = 1612
                try:
                    __zt_tmp = __attrs_4900796736
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4439058528('path', 'view/ical_url', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))

                # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900784064
                __default_4900784064 = _DEFAULT_MARKER

                # <Translate msgid='title_add_to_ical' node=<ast.Constant object at 0x1241c0340> at 1241c1f00> -> __attr_title
                __attr_title = 'Download this event in iCal format'
                __attr_title = translate('title_add_to_ical', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_title is not None):
                    __append((' title="%s"' % __attr_title))
                __append('>\n              ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900792800
                __attrs_4900792800 = _static_4438893776

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')
                __stream_4900795056 = []
                __append_4900795056 = __stream_4900795056.append
                __append_4900795056('iCal')
                __msgid_4900795056 = __re_whitespace(''.join(__stream_4900795056)).strip()
                if 'label_add_to_ical':
                    __append(translate('label_add_to_ical', mapping=None, default=__msgid_4900795056, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</span>\n            </a>\n\n          </li>\n        </ul>\n      </nav>')
                if (__backup_show_filter_4880485920 is __marker):
                    del econtext['show_filter']
                else:
                    econtext['show_filter'] = __backup_show_filter_4880485920
                if (__backup_mode_4880490288 is __marker):
                    del econtext['mode']
                else:
                    econtext['mode'] = __backup_mode_4880490288
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900792656
                __attrs_4900792656 = _static_4438893776

                # <Value 'header/sub' (57:25)> -> __condition
                __token = 1944
                try:
                    __zt_tmp = __attrs_4900792656
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4439058528('path', 'header/sub', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
                if __condition:

                    # <h2 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h2>')

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __default_4900794816
                    __default_4900794816 = _DEFAULT_MARKER

                    # <Value 'header/sub' (56:23)> -> __cache_4900798272
                    __token = 1907
                    try:
                        __zt_tmp = __attrs_4900792656
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4900798272 = _static_4439058528('path', 'header/sub', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))

                    # <BinOp left=<Value 'header/sub' (56:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 1088dffa0> at 1241c3cd0> -> __condition
                    __expression = __cache_4900798272

                    # <Symbol value=<DEFAULT> at 1088dffa0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4900798272
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</h2>')
                __append('\n    ')
                if (__backup_header_4881066896 is __marker):
                    del econtext['header']
                else:
                    econtext['header'] = __backup_header_4881066896
            _slots = econtext['__slot_content_title'] = _deque((__fill_content_title, ))

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x1089424d0> name=None at 108940190> -> __attrs_4900787664
                __attrs_4900787664 = _static_4438893776
                __append('\n      ')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n    ')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/main_template/macros/master' (8:21)> -> __macro
            __token = 259
            try:
                __zt_tmp = __attrs_4901613680
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4439058528('path', 'context/main_template/macros/master', econtext=econtext)(_static_4439051040(econtext, __zt_tmp))
            __token = 259
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4680504704 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4680504704
            __i18n_domain = __previous_i18n_domain_4901613248
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render': render, }