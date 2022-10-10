# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/volto/browser/migrate_to_volto.pt'

__tokens = {1919: ('request/URL', 30, 83), 3311: ('python:view.migrate_folders', 59, 40), 3781: ('python:view.migrate_default_pages', 72, 40), 4626: ('python:view.purge_richtext', 90, 40), 5366: ('python:view.service_url', 106, 42), 257: ('context/main_template/macros/master', 6, 23), 257: ('context/main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4672737424 = 'master'
_static_4854630096 = {'class': 'form-text', }
_static_4854635904 = {'class': 'form-control', 'type': 'text', 'name': 'service_url', 'id': 'service_url', 'value': '', }
_static_4854633936 = {'for': 'service_url', 'class': 'form-label', }
_static_4854630480 = {'class': 'field mb-3', }
_static_4854629904 = {'class': 'form-text', }
_static_4677769232 = {'class': 'form-check-label', 'for': 'purge_richtext', }
_static_4677770816 = {'class': 'form-check-input', 'type': 'checkbox', 'name': 'purge_richtext:boolean', 'id': 'purge_richtext', 'checked': 'python:view.purge_richtext', }
_static_4677776816 = {'class': 'form-check mb-3', }
_static_4677768752 = {'class': 'form-text', }
_static_4677772832 = {'class': 'form-check-label', 'for': 'migrate_default_pages', }
_static_4677777392 = {'class': 'form-check-input', 'type': 'checkbox', 'name': 'migrate_default_pages:boolean', 'id': 'migrate_default_pages', 'checked': 'python:view.migrate_default_pages', }
_static_4854521744 = {'class': 'form-check mb-3 ms-4', }
_static_4854517376 = {'class': 'form-check-label', 'for': 'migrate_folders', }
_static_4854523856 = {'class': 'form-check-input', 'type': 'checkbox', 'name': 'migrate_folders:boolean', 'id': 'migrate_folders', 'checked': 'python:view.migrate_folders', }
_static_4854524816 = {'class': 'form-check mb-3', }
_static_4854528704 = {'href': 'https://github.com/plone/blocks-conversion-tool', }
_static_4854522032 = {'class': 'mt-5', }
_static_4664348144 = {'class': 'btn btn-primary submit-widget button-field context', 'type': 'submit', 'name': 'submit', 'value': 'export', }
_static_4854552928 = {'type': 'hidden', 'name': 'form.submitted', 'value': '1', }
_static_4854559936 = {'class': 'formControls form-group', }
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
_static_4854561664 = {'id': 'migrate_to_volto', 'action': '@@migrate_to_volto', 'method': 'post', 'enctype': 'multipart/form-data', }
_static_4680586800 = {'class': 'lead', }
_static_4680586224 = {'class': 'documentFirstHeading', }
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

    def render_main(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680585264
            __attrs_4680585264 = _static_4428767312
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x116fc13f0> name=None at 116fc1ab0> -> __attrs_4680584736
            __attrs_4680584736 = _static_4680586224

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1 class="documentFirstHeading">')
            __stream_4680585216 = []
            __append_4680585216 = __stream_4680585216.append
            __append_4680585216('Migrate to Volto')
            __msgid_4680585216 = __re_whitespace(''.join(__stream_4680585216)).strip()
            if __msgid_4680585216:
                __append(translate(__msgid_4680585216, mapping=None, default=__msgid_4680585216, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h1>\n\n    ')

            # <Static value=<ast.Dict object at 0x116fc1630> name=None at 116fc0280> -> __attrs_4680596688
            __attrs_4680596688 = _static_4680586800

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="lead">')
            __stream_4680586080 = []
            __append_4680586080 = __stream_4680586080.append
            __append_4680586080('Here you can prepare this site for Volto.')
            __msgid_4680586080 = __re_whitespace(''.join(__stream_4680586080)).strip()
            if __msgid_4680586080:
                __append(translate(__msgid_4680586080, mapping=None, default=__msgid_4680586080, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680596832
            __attrs_4680596832 = _static_4428767312

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3>')
            __stream_4680595344 = []
            __append_4680595344 = __stream_4680595344.append
            __append_4680595344('What is Volto?')
            __msgid_4680595344 = __re_whitespace(''.join(__stream_4680595344)).strip()
            if __msgid_4680595344:
                __append(translate(__msgid_4680595344, mapping=None, default=__msgid_4680595344, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h3>\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680584112
            __attrs_4680584112 = _static_4428767312

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')
            __stream_4680583056 = []
            __append_4680583056 = __stream_4680583056.append
            __append_4680583056('Volto is a React-based frontend for Plone. It is the default UI for Plone 6.')
            __msgid_4680583056 = __re_whitespace(''.join(__stream_4680583056)).strip()
            if __msgid_4680583056:
                __append(translate(__msgid_4680583056, mapping=None, default=__msgid_4680583056, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4854554320
            __attrs_4854554320 = _static_4428767312

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3>')
            __stream_4854555808 = []
            __append_4854555808 = __stream_4854555808.append
            __append_4854555808('What will happen?')
            __msgid_4854555808 = __re_whitespace(''.join(__stream_4854555808)).strip()
            if __msgid_4854555808:
                __append(translate(__msgid_4854555808, mapping=None, default=__msgid_4854555808, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h3>\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4854554128
            __attrs_4854554128 = _static_4428767312

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')
            __stream_4854560560 = []
            __append_4854560560 = __stream_4854560560.append
            __append_4854560560('When you click on "Migrate to Volto" the following things will happen:')
            __msgid_4854560560 = __re_whitespace(''.join(__stream_4854560560)).strip()
            if __msgid_4854560560:
                __append(translate(__msgid_4854560560, mapping=None, default=__msgid_4854560560, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4854554176
            __attrs_4854554176 = _static_4428767312

            # <ol ... (0:0)
            # --------------------------------------------------------
            __append('<ol>\n        ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4854555472
            __attrs_4854555472 = _static_4428767312

            # <li ... (0:0)
            # --------------------------------------------------------
            __append('<li>')
            __stream_4854557104 = []
            __append_4854557104 = __stream_4854557104.append
            __append_4854557104('Install the package ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4854554704
            __attrs_4854554704 = _static_4428767312

            # <code ... (0:0)
            # --------------------------------------------------------
            __append_4854557104('<code>plone.volto</code> and ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4854559264
            __attrs_4854559264 = _static_4428767312

            # <code ... (0:0)
            # --------------------------------------------------------
            __append_4854557104('<code>plone.restapi</code>.')
            __msgid_4854557104 = __re_whitespace(''.join(__stream_4854557104)).strip()
            if __msgid_4854557104:
                __append(translate(__msgid_4854557104, mapping=None, default=__msgid_4854557104, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</li>\n        ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4854551776
            __attrs_4854551776 = _static_4428767312

            # <li ... (0:0)
            # --------------------------------------------------------
            __append('<li>')
            __stream_4854556384 = []
            __append_4854556384 = __stream_4854556384.append
            __append_4854556384('The html of Richtext-Fields (previously edited using TinyMCE) is converted into Volto blocks so you can edit it in Volto.')
            __msgid_4854556384 = __re_whitespace(''.join(__stream_4854556384)).strip()
            if __msgid_4854556384:
                __append(translate(__msgid_4854556384, mapping=None, default=__msgid_4854556384, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</li>\n        ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4854549232
            __attrs_4854549232 = _static_4428767312

            # <li ... (0:0)
            # --------------------------------------------------------
            __append('<li>')
            __stream_4854549088 = []
            __append_4854549088 = __stream_4854549088.append
            __append_4854549088('Pages, News Items and Events are made folderish. That means they can contain other content like Images or Pages.')
            __msgid_4854549088 = __re_whitespace(''.join(__stream_4854549088)).strip()
            if __msgid_4854549088:
                __append(translate(__msgid_4854549088, mapping=None, default=__msgid_4854549088, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</li>\n        ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4854558736
            __attrs_4854558736 = _static_4428767312

            # <li ... (0:0)
            # --------------------------------------------------------
            __append('<li>')
            __stream_4854558880 = []
            __append_4854558880 = __stream_4854558880.append
            __append_4854558880('Default Pages of Folders are merged with the Folderish Pages that replace the Folder whereever that is possible.\n            This works well with Pages and Collections where the text and/or query are added to the folderish page that repalces the Folder.')
            __msgid_4854558880 = __re_whitespace(''.join(__stream_4854558880)).strip()
            if __msgid_4854558880:
                __append(translate(__msgid_4854558880, mapping=None, default=__msgid_4854558880, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</li>\n        ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4854551344
            __attrs_4854551344 = _static_4428767312

            # <li ... (0:0)
            # --------------------------------------------------------
            __append('<li>')
            __stream_4854561136 = []
            __append_4854561136 = __stream_4854561136.append
            __append_4854561136('Collections are migrated to Pages with Listing Blocks configured like the Collection.')
            __msgid_4854561136 = __re_whitespace(''.join(__stream_4854561136)).strip()
            if __msgid_4854561136:
                __append(translate(__msgid_4854561136, mapping=None, default=__msgid_4854561136, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</li>\n        ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4854553216
            __attrs_4854553216 = _static_4428767312

            # <li ... (0:0)
            # --------------------------------------------------------
            __append('<li>')
            __stream_4854555520 = []
            __append_4854555520 = __stream_4854555520.append
            __append_4854555520('A migrated site will still work in Plone Classic but behave different. Editors can only work with the Data using Volto.')
            __msgid_4854555520 = __re_whitespace(''.join(__stream_4854555520)).strip()
            if __msgid_4854555520:
                __append(translate(__msgid_4854555520, mapping=None, default=__msgid_4854555520, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</li>\n    </ol>\n\n    ')

            # <Static value=<ast.Dict object at 0x1215abb80> name=None at 1215abbe0> -> __attrs_4854553696
            __attrs_4854553696 = _static_4854561664

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form id="migrate_to_volto"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4854548416
            __default_4854548416 = _DEFAULT_MARKER

            # <Substitution 'request/URL' (30:83)> -> __attr_action
            __token = 1919
            try:
                __zt_tmp = __attrs_4854553696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_4427992992('path', 'request/URL', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', '@@migrate_to_volto', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append(' method="post" enctype="multipart/form-data">\n\n        ')

            # <Static value=<ast.Dict object at 0x1215ab4c0> name=None at 1215a8910> -> __attrs_4854546736
            __attrs_4854546736 = _static_4854559936

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="formControls form-group">\n            ')

            # <Static value=<ast.Dict object at 0x1215a9960> name=None at 1215a97b0> -> __attrs_4664359424
            __attrs_4664359424 = _static_4854552928

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" name="form.submitted" value="1"/>\n            ')

            # <Static value=<ast.Dict object at 0x116044df0> name=None at 116044790> -> __attrs_4854526544
            __attrs_4854526544 = _static_4664348144

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button class="btn btn-primary submit-widget button-field context" type="submit" name="submit" value="export">Migrate to Volto\n            </button>\n        </div>\n\n        ')

            # <Static value=<ast.Dict object at 0x1215a20b0> name=None at 1215a2110> -> __attrs_4854522416
            __attrs_4854522416 = _static_4854522032

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3 class="mt-5">')
            __stream_4854519488 = []
            __append_4854519488 = __stream_4854519488.append
            __append_4854519488('Requirements')
            __msgid_4854519488 = __re_whitespace(''.join(__stream_4854519488)).strip()
            if __msgid_4854519488:
                __append(translate(__msgid_4854519488, mapping=None, default=__msgid_4854519488, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h3>\n        ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4854522848
            __attrs_4854522848 = _static_4428767312

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append('<ul>\n            ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4854519680
            __attrs_4854519680 = _static_4428767312

            # <li ... (0:0)
            # --------------------------------------------------------
            __append('<li>')
            __stream_4854527552 = []
            __append_4854527552 = __stream_4854527552.append
            __append_4854527552('\n            To migrate Richtext to Volto Blocks you need to have ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4854522752
            __attrs_4854522752 = _static_4428767312

            # <code ... (0:0)
            # --------------------------------------------------------
            __append_4854527552('<code>blocks-conversion-tool</code> running on a accessible url.\n            The easiest way to have that running on your machine is: ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4854517856
            __attrs_4854517856 = _static_4428767312

            # <code ... (0:0)
            # --------------------------------------------------------
            __append_4854527552('<code>docker run -it -p 5000:5000 plone/blocks-conversion-tool:latest</code>.\n            More for options read ')

            # <Static value=<ast.Dict object at 0x1215a3ac0> name=None at 1215a3b20> -> __attrs_4854520208
            __attrs_4854520208 = _static_4854528704

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_4854527552('<a href="https://github.com/plone/blocks-conversion-tool">https://github.com/plone/blocks-conversion-tool</a>.\n            ')
            __msgid_4854527552 = __re_whitespace(''.join(__stream_4854527552)).strip()
            if __msgid_4854527552:
                __append(translate(__msgid_4854527552, mapping=None, default=__msgid_4854527552, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</li>\n        </ul>\n\n        ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4854527888
            __attrs_4854527888 = _static_4428767312

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3>')
            __stream_4854520784 = []
            __append_4854520784 = __stream_4854520784.append
            __append_4854520784('Advanced settings')
            __msgid_4854520784 = __re_whitespace(''.join(__stream_4854520784)).strip()
            if __msgid_4854520784:
                __append(translate(__msgid_4854520784, mapping=None, default=__msgid_4854520784, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h3>\n        ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4854518720
            __attrs_4854518720 = _static_4428767312

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')
            __stream_4854518288 = []
            __append_4854518288 = __stream_4854518288.append
            __append_4854518288('\n        It is recommendet to use the default settings but here you can disable some of the migration-steps.\n        ')
            __msgid_4854518288 = __re_whitespace(''.join(__stream_4854518288)).strip()
            if __msgid_4854518288:
                __append(translate(__msgid_4854518288, mapping=None, default=__msgid_4854518288, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n\n        ')

            # <Static value=<ast.Dict object at 0x1215a2b90> name=None at 1215a2a10> -> __attrs_4854516320
            __attrs_4854516320 = _static_4854524816

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-check mb-3">\n            ')

            # <Static value=<ast.Dict object at 0x1215a27d0> name=None at 1215a2830> -> __attrs_4854525248
            __attrs_4854525248 = _static_4854523856

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-check-input" type="checkbox" name="migrate_folders:boolean" id="migrate_folders"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4854521024
            __default_4854521024 = _DEFAULT_MARKER

            # <Boolean 'python:view.migrate_folders' (59:40)> -> __attr_checked
            __token = 3311
            try:
                __zt_tmp = __attrs_4854525248
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_checked = _static_4427992992('python', 'view.migrate_folders', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if (__attr_checked is _DEFAULT_MARKER):
                __attr_checked = None
            else:
                if __attr_checked:
                    __attr_checked = 'checked'
                else:
                    __attr_checked = None
            if (__attr_checked is not None):
                __append((' checked="%s"' % __attr_checked))
            __append(' />\n            ')

            # <Static value=<ast.Dict object at 0x1215a0e80> name=None at 1215a0ee0> -> __attrs_4854517712
            __attrs_4854517712 = _static_4854517376

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-check-label" for="migrate_folders">\n            Migrate Folders to Folderish Pages\n            </label>\n        </div>\n\n        ')

            # <Static value=<ast.Dict object at 0x1215a1f90> name=None at 1215a08e0> -> __attrs_4854514928
            __attrs_4854514928 = _static_4854521744

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-check mb-3 ms-4">\n            ')

            # <Static value=<ast.Dict object at 0x116d137f0> name=None at 116d10910> -> __attrs_4677764624
            __attrs_4677764624 = _static_4677777392

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-check-input" type="checkbox" name="migrate_default_pages:boolean" id="migrate_default_pages"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4677773888
            __default_4677773888 = _DEFAULT_MARKER

            # <Boolean 'python:view.migrate_default_pages' (72:40)> -> __attr_checked
            __token = 3781
            try:
                __zt_tmp = __attrs_4677764624
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_checked = _static_4427992992('python', 'view.migrate_default_pages', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if (__attr_checked is _DEFAULT_MARKER):
                __attr_checked = None
            else:
                if __attr_checked:
                    __attr_checked = 'checked'
                else:
                    __attr_checked = None
            if (__attr_checked is not None):
                __append((' checked="%s"' % __attr_checked))
            __append(' />\n            ')

            # <Static value=<ast.Dict object at 0x116d12620> name=None at 116d110c0> -> __attrs_4677773120
            __attrs_4677773120 = _static_4677772832

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-check-label" for="migrate_default_pages">\n            Migrate default Pages into the Folderish Pages if possible\n            </label>\n            ')

            # <Static value=<ast.Dict object at 0x116d11630> name=None at 116d10b80> -> __attrs_4677776912
            __attrs_4677776912 = _static_4677768752

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-text">')
            __stream_4677770144 = []
            __append_4677770144 = __stream_4677770144.append
            __append_4677770144('\n            Collections and Pages that are the default-page of a Folder will be applied on the migrated Folderish Page.\n            For Collections that means adding a listing block with the same query.\n            This only happens if you also you migrate Folders to Folderish Pages.\n            ')
            __msgid_4677770144 = __re_whitespace(''.join(__stream_4677770144)).strip()
            if __msgid_4677770144:
                __append(translate(__msgid_4677770144, mapping=None, default=__msgid_4677770144, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n        </div>\n\n        ')

            # <Static value=<ast.Dict object at 0x116d135b0> name=None at 116d11240> -> __attrs_4677776768
            __attrs_4677776768 = _static_4677776816

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-check mb-3">\n            ')

            # <Static value=<ast.Dict object at 0x116d11e40> name=None at 116d133a0> -> __attrs_4677771824
            __attrs_4677771824 = _static_4677770816

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-check-input" type="checkbox" name="purge_richtext:boolean" id="purge_richtext"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4677768176
            __default_4677768176 = _DEFAULT_MARKER

            # <Boolean 'python:view.purge_richtext' (90:40)> -> __attr_checked
            __token = 4626
            try:
                __zt_tmp = __attrs_4677771824
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_checked = _static_4427992992('python', 'view.purge_richtext', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if (__attr_checked is _DEFAULT_MARKER):
                __attr_checked = None
            else:
                if __attr_checked:
                    __attr_checked = 'checked'
                else:
                    __attr_checked = None
            if (__attr_checked is not None):
                __append((' checked="%s"' % __attr_checked))
            __append(' />\n            ')

            # <Static value=<ast.Dict object at 0x116d11810> name=None at 116d11090> -> __attrs_4854636816
            __attrs_4854636816 = _static_4677769232

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-check-label" for="purge_richtext">\n            Purge old Richtext-fields after migrating to Volto blocks\n            </label>\n            ')

            # <Static value=<ast.Dict object at 0x1215bc610> name=None at 1215bc5e0> -> __attrs_4854633984
            __attrs_4854633984 = _static_4854629904

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-text">')
            __stream_4854637248 = []
            __append_4854637248 = __stream_4854637248.append
            __append_4854637248('\n            The RichtextValue objects will be removed from the migrated objects. The old fields (from the behavior plone.volto) are no longer available.\n            ')
            __msgid_4854637248 = __re_whitespace(''.join(__stream_4854637248)).strip()
            if __msgid_4854637248:
                __append(translate(__msgid_4854637248, mapping=None, default=__msgid_4854637248, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n        </div>\n\n        ')

            # <Static value=<ast.Dict object at 0x1215bc850> name=None at 1215bc8b0> -> __attrs_4854630864
            __attrs_4854630864 = _static_4854630480

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="field mb-3">\n            ')

            # <Static value=<ast.Dict object at 0x1215bd5d0> name=None at 1215bc400> -> __attrs_4854634032
            __attrs_4854634032 = _static_4854633936

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="service_url" class="form-label">\n            URL of blocks-conversion-tool.\n            </label>\n            ')

            # <Static value=<ast.Dict object at 0x1215bdd80> name=None at 1215bdde0> -> __attrs_4854634992
            __attrs_4854634992 = _static_4854635904

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-control" type="text" name="service_url" id="service_url"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4854633120
            __default_4854633120 = _DEFAULT_MARKER

            # <Substitution 'python:view.service_url' (106:42)> -> __attr_value
            __token = 5366
            try:
                __zt_tmp = __attrs_4854634992
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_4427992992('python', 'view.service_url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append('>\n            ')

            # <Static value=<ast.Dict object at 0x1215bc6d0> name=None at 1215bc730> -> __attrs_4854635376
            __attrs_4854635376 = _static_4854630096

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-text">')
            __stream_4854636432 = []
            __append_4854636432 = __stream_4854636432.append
            __append_4854636432('\n            The migration requires a service to run. See https://github.com/plone/blocks-conversion-tool for details.\n            ')
            __msgid_4854636432 = __re_whitespace(''.join(__stream_4854636432)).strip()
            if __msgid_4854636432:
                __append(translate(__msgid_4854636432, mapping=None, default=__msgid_4854636432, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n        </div>\n\n    </form>\n\n')
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

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4678241056
            __attrs_4678241056 = _static_4428767312
            __previous_i18n_domain_4678244320 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4885871296 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x116845090> name=None at 116847940> -> __value
            __value = _static_4672737424
            econtext['macroname'] = __value

            def __fill_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680591456
                __attrs_4680591456 = _static_4428767312

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n')
                __token = None
                render_main(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n</div>')
            _slots = econtext['__slot_main'] = _deque((__fill_main, ))

            # <Value 'context/main_template/macros/master' (6:23)> -> __macro
            __token = 257
            try:
                __zt_tmp = __attrs_4678241056
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4427992992('path', 'context/main_template/macros/master', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __token = 257
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4885871296 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4885871296
            __i18n_domain = __previous_i18n_domain_4678244320
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_main': render_main, 'render': render, }