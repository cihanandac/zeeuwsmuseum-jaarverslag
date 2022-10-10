# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/backend/env/lib/python3.10/site-packages/plone/app/theming/browser/controlpanel.pt'

__tokens = {2797: ('provider:plone.abovecontenttitle', 76, 73), 3044: ('string:$site_url/@@overview-controlpanel', 81, 37), 4043: ('string:$site_url/test_rendering#top', 109, 36), 4249: ('string:$site_url/@@theming-controlpanel-help', 114, 36), 4679: ('view/themeList', 126, 34), 4733: ("python:theme['selected'] and 'themeEntry activeThemeEntry' or 'themeEntry'", 127, 38), 4843: (' string:themeEntry-${theme/name', 128, 34), 4918: ('e theme/na', 129, 41), 4978: ('le theme/ti', 130, 46), 5138: ('theme/title', 135, 43), 5225: ('theme/override', 136, 61), 5381: ('theme/selected', 138, 43), 5702: ('theme/preview', 146, 53), 5819: ('theme/description', 149, 67), 5971: ('request/URL', 153, 71), 6047: ('context/@@authenticator/authenticator', 154, 62), 6181: ('theme/name', 155, 92), 6287: ('not:theme/selected', 157, 51), 6667: ('theme/selected', 163, 51), 7041: ('theme/selected', 169, 51), 7420: ('theme/selected', 175, 51), 7840: ('string:${context/absolute_url}/++theme++${theme/name}/@@download-zip', 182, 86), 8235: ('theme/editable', 188, 47), 8304: ('string:#modal-delete-${theme/name}', 189, 53), 8709: ('theme/editable', 195, 47), 8627: ('string:modal-delete-${theme/name}', 194, 51), 8972: ('string:${theme/name}', 198, 53), 9530: ('request/URL', 207, 89), 9610: ('context/@@authenticator/authenticator', 208, 66), 9854: ('string:${theme/name}', 211, 62), 11353: ('view/errors', 250, 31), 11309: ('request/URL', 249, 35), 12021: ("python:request.get('themeEnabled', view.theme_settings.enabled)", 266, 45), 12336: ("python:'themeEnabled' if selected else None", 270, 52), 12861: ('errors/rules | nothing', 281, 42), 12926: (" python:request.get('rules', view.theme_settings.rules", 282, 41), 13029: ("python:'field error' if error else 'field'", 283, 46), 13432: ('error', 290, 85), 13410: ('error', 290, 63), 13682: ('rules', 297, 50), 13816: ('errors/absolutePrefix | nothing', 303, 42), 13899: (" python:request.get('absolutePrefix', view.theme_settings.absolutePrefix", 304, 50), 14020: ("python:'field error' if error else 'field'", 305, 46), 14690: ('error', 315, 85), 14668: ('error', 315, 63), 14958: ('absolutePrefix', 322, 50), 15101: ('errors/doctype | nothing', 328, 42), 15170: (" python:request.get('doctype', view.theme_settings.doctype", 329, 43), 15277: ("python:'field error' if error else 'field'", 330, 46), 15922: ('error', 340, 85), 15900: ('error', 340, 63), 16176: ('doctype', 347, 50), 16353: ("python:request.get('readNetwork', view.theme_settings.readNetwork)", 354, 45), 16668: ("python:'readNetwork' if selected else None", 358, 52), 17141: ('errors/hostnameBlacklist | nothing', 368, 42), 17230: (' view/theme_settings/hostnameBlacklist | python:[', 369, 53), 17334: ('t python: view.hostname_blacklist or hostnameBlackli', 370, 52), 17436: ("python:'field error' if error else 'field'", 371, 46), 18328: ('error', 384, 85), 18306: ('error', 384, 63), 18599: ("python: '\\n'.join(hostnameBlacklist)", 391, 41), 18774: ('errors/parameterExpressions | nothing', 397, 42), 18869: (' python:view.theme_settings.parameterExpressions or {', 398, 56), 18980: ("s python:['%s = %s' % (k,v) for k,v in parameterExpressions.items(", 399, 55), 19104: ("ns python:request.get('parameterExpressions', parameterExpressio", 400, 54), 19219: ("python:'field error' if error else 'field'", 401, 46), 20368: ('error', 417, 85), 20346: ('error', 417, 63), 20645: ("python:'\\n'.join(parameterExpressions)", 424, 41), 21378: ("python:request.get('themeBase', view.pskin.getDefaultSkin())", 441, 45), 22160: ('view/skinsVocabulary', 454, 49), 22236: ('skin/value', 455, 54), 22304: (" python:skin.value == selected and 'selected' or Non", 456, 56), 22404: ('skin/title', 457, 45), 22622: ("python:request.get('markSpecialLinks', view.mark_special_links)", 465, 45), 22949: ("python:'markSpecialLinks' if selected else None", 469, 52), 23512: ("python:request.get('extLinksOpenInNewWindow', view.ext_links_open_new_window)", 480, 45), 23874: ("python:'extLinksOpenInNewWindow' if selected else None", 484, 52), 24562: ('errors/custom_css | nothing', 498, 42), 24637: (" view/theme_settings/custom_css | python: '", 499, 46), 24728: ("s python:request.get('custom_css', custom_cs", 500, 45), 24822: ("python:'field error' if error else 'field'", 501, 46), 25838: ('error', 511, 85), 25816: ('error', 511, 63), 26213: ('custom_css', 520, 41), 27050: ('context/@@authenticator/authenticator', 546, 42), 27989: ('view/errors', 575, 31), 27945: ('request/URL', 574, 35), 28085: ('errors/themeArchive | nothing', 579, 34), 28154: ("python:'field error' if error else 'field'", 580, 38), 28421: ('error', 586, 77), 28399: ('error', 586, 55), 28693: ("python:request.get('enableNewTheme', False)", 598, 37), 28969: ("python:'enableNewTheme' if selected else None", 601, 44), 29472: ("python:request.get('replaceExisting', False)", 612, 37), 29752: ("python:'replaceExisting' if selected else None", 615, 44), 30758: ('context/@@authenticator/authenticator', 640, 42), 36: ('string:&lt;!DOCTYPE ht', 1, 36), 335: ('context/@@plone_portal_state', 8, 31), 385: (' context/@@plon', 9, 20), 424: ('t context/@@plone_layo', 10, 21), 462: ('ng portal_state/langu', 11, 12), 499: ('iew nocall:view | nocall: plone_', 12, 11), 553: ('_url portal_state/porta', 13, 16), 597: ('_load python', 14, 14), 626: (" dummy python: request.set('disable_toolbar'", 15, 9), 690: ('ite_url view/', 16, 11), 740: ('lang', 17, 27), 789: ('provider:plone.httpheaders', 19, 40), 892: ('provider:plone.htmlhead', 24, 32), 953: ('provider:plone.htmlhead.links', 25, 33), 1075: ('string:${context/portal_url}/++theme++barceloneta/css/barceloneta.min.css', 29, 29), 1249: ('string:${context/portal_url}/++resource++plone.app.theming/controlpanel.css', 34, 29), 1364: ('nothing', 37, 26), 1509: ('provider:plone.scripts', 41, 32), 1640: ('portal_state/is_rtl', 47, 26), 1683: (" python:plone_layout.have_portlets('plone.leftcolumn', view", 48, 22), 1766: ("r python:plone_layout.have_portlets('plone.rightcolumn', vie", 49, 21), 1858: ('ss python:plone_layout.bodyClass(template, vi', 50, 28), 2034: ('  python:plone_view.patterns_settings', 53, 22), 1939: ('body_class', 51, 30), 1978: (" python:isRTL and 'rtl' or 'ltr", 52, 27), 2144: ('provider:plone.toolbar', 56, 32), 2536: ('provider:plone.globalstatusmessage', 65, 42)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4680812144 = {'id': 'portal-column-content', }
_static_4680818480 = {'class': 'portalMessage info', 'role': 'status', }
_static_4680437664 = {'id': 'global_statusmessage', }
_static_4685955184 = set([])
_static_4680446400 = {'id': 'visual-portal-wrapper', 'class': 'body_class', 'dir': "python:isRTL and 'rtl' or 'ltr'", }
_static_4680447456 = {'name': 'generator', 'content': 'Plone - http://plone.org', }
_static_4680541104 = {'rel': 'stylesheet', 'type': 'text/css', 'href': 'string:${context/portal_url}/++resource++plone.app.theming/controlpanel.css', }
_static_4680539184 = {'rel': 'stylesheet', 'type': 'text/css', 'href': 'string:${context/portal_url}/++theme++barceloneta/css/barceloneta.min.css', }
_static_4680542256 = {'charset': 'utf-8', }
_static_4678303648 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'lang': 'lang', }
_static_4681903232 = {'type': 'submit', 'name': 'form.button.Cancel', 'class': 'btn btn-primary cancel', 'value': 'Cancel', }
_static_4681894160 = {'type': 'submit', 'name': 'form.button.Import', 'class': 'btn btn-success save', 'value': 'Import', }
_static_4681893536 = {'class': 'btn-group', }
_static_4682779136 = {'class': 'formHelp', }
_static_4682782400 = {'for': 'replaceExisting', }
_static_4682778128 = {'type': 'checkbox', 'value': '1', 'name': 'replaceExisting:boolean', 'id': 'replaceExisting', 'checked': "python:'replaceExisting' if selected else None", }
_static_4682777648 = {'type': 'hidden', 'value': '', 'name': 'replaceExisting:boolean:default', }
_static_4682792192 = {'class': 'field', }
_static_4682789216 = {'class': 'formHelp', }
_static_4682788496 = {'for': 'enableNewTheme', }
_static_4682791808 = {'type': 'checkbox', 'value': '1', 'name': 'enableNewTheme:boolean', 'id': 'enableNewTheme', 'checked': "python:'enableNewTheme' if selected else None", }
_static_4682784032 = {'type': 'hidden', 'value': '', 'name': 'enableNewTheme:boolean:default', }
_static_4683182288 = {'class': 'field', }
_static_4683173408 = {'type': 'file', 'name': 'themeArchive', 'id': 'themeArchive', }
_static_4683171920 = {'class': 'errorMessage', }
_static_4683184880 = {'class': 'formHelp', }
_static_4683175568 = {'class': 'field', }
_static_4683171680 = {'name': 'import', 'method': 'post', 'enctype': 'multipart/form-data', 'class': 'pat-formunloadalert', 'action': 'request/URL', }
_static_4677995872 = {'class': 'documentDescription', }
_static_4678002016 = {'class': 'documentFirstHeading', }
_static_4678008352 = {'id': 'overlay-upload', 'class': 'modal', }
_static_4680513568 = {'type': 'submit', 'name': 'form.button.Cancel', 'class': 'btn btn-primary cancel', 'value': 'Cancel', }
_static_4680508912 = {'type': 'submit', 'name': 'form.button.AdvancedSave', 'class': 'btn btn-success save', 'value': 'Save', }
_static_4681944176 = {'class': 'btn-group', }
_static_4680505600 = {'name': 'custom_css', 'id': 'custom_css', 'rows': '40', 'cols': '160', 'placeholder': 'Put your plain css...', 'class': 'pat-code-editor', 'data-pat-code-editor': 'language: css; theme: tomorrow', }
_static_4680513184 = {'class': 'errorMessage', }
_static_4681949408 = {'href': 'https://docs.plone.org/adapt-and-extend/theming', 'target': '_blank', }
_static_4681955360 = {'class': 'theming_doc_link', }
_static_4681953248 = {'class': 'formHelp', }
_static_4681948064 = {'for': 'custom_css', }
_static_4681953200 = {'class': "python:'field error' if error else 'field'", }
_static_4681945040 = {'class': 'formHelp', }
_static_4681955216 = {'for': 'extLinksOpenInNewWindow', }
_static_4681954784 = {'type': 'checkbox', 'value': '1', 'name': 'extLinksOpenInNewWindow:boolean', 'id': 'extLinksOpenInNewWindow', 'checked': "python:'extLinksOpenInNewWindow' if selected else None", }
_static_4681935232 = {'type': 'hidden', 'value': '', 'name': 'extLinksOpenInNewWindow:boolean:default', }
_static_4681931632 = {'class': 'field', }
_static_4681925728 = {'class': 'formHelp', }
_static_4681930816 = {'for': 'markSpecialLinks', }
_static_4681938064 = {'type': 'checkbox', 'value': '1', 'name': 'markSpecialLinks:boolean', 'id': 'markSpecialLinks', 'checked': "python:'markSpecialLinks' if selected else None", }
_static_4681939264 = {'type': 'hidden', 'value': '', 'name': 'markSpecialLinks:boolean:default', }
_static_4681939552 = {'class': 'field', }
_static_4681937536 = {'value': 'skin/value', 'selected': "python:skin.value == selected and 'selected' or None", }
_static_4681931344 = {'size': '1', 'name': 'themeBase', 'id': 'themeBase', }
_static_4682982368 = {'class': 'formHelp', }
_static_4682989472 = {'for': 'themeBase', }
_static_4682978192 = {'class': 'field', }
_static_4682973248 = {'name': 'parameterExpressions:lines', 'id': 'parameterExpressions', 'rows': '8', 'cols': '50', }
_static_4682983520 = {'class': 'errorMessage', }
_static_4680557392 = {'class': 'formHelp', }
_static_4680553888 = {'for': 'parameterExpressions', }
_static_4680560752 = {'class': "python:'field error' if error else 'field'", }
_static_4680551248 = {'name': 'hostnameBlacklist:lines', 'id': 'hostnameBlacklist', 'rows': '5', 'cols': '50', }
_static_4680560032 = {'class': 'errorMessage', }
_static_4680558400 = {'class': 'formHelp', }
_static_4680559072 = {'for': 'hostnameBlacklist', }
_static_4682539904 = {'class': "python:'field error' if error else 'field'", }
_static_4682539472 = {'class': 'formHelp', }
_static_4682538416 = {'for': 'readNetwork', }
_static_4682543600 = {'type': 'checkbox', 'value': '1', 'name': 'readNetwork:boolean', 'id': 'readNetwork', 'checked': "python:'readNetwork' if selected else None", }
_static_4682545280 = {'type': 'hidden', 'value': '', 'name': 'readNetwork:boolean:default', }
_static_4682545952 = {'class': 'field', }
_static_4682542928 = {'name': 'doctype', 'id': 'doctype', 'type': 'text', 'size': '50', 'value': 'doctype', }
_static_4682540048 = {'class': 'errorMessage', }
_static_4683087680 = {'class': 'formHelp', }
_static_4683087392 = {'for': 'doctype', }
_static_4683084176 = {'class': "python:'field error' if error else 'field'", }
_static_4683075680 = {'name': 'absolutePrefix', 'id': 'absolutePrefix', 'type': 'text', 'size': '50', 'value': 'absolutePrefix', }
_static_4683081584 = {'class': 'errorMessage', }
_static_4683072032 = {'class': 'formHelp', }
_static_4683080240 = {'for': 'absolutePrefix', }
_static_4680482768 = {'class': "python:'field error' if error else 'field'", }
_static_4680481376 = {'name': 'rules', 'id': 'rules', 'type': 'text', 'size': '50', 'value': 'rules', }
_static_4680467840 = {'class': 'errorMessage', }
_static_4680477584 = {'class': 'formHelp', }
_static_4682797392 = {'for': 'rules', }
_static_4682804688 = {'class': "python:'field error' if error else 'field'", }
_static_4682796720 = {'class': 'formHelp', }
_static_4682809296 = {'for': 'themeEnabled', }
_static_4682808000 = {'type': 'checkbox', 'value': '1', 'name': 'themeEnabled:boolean', 'id': 'themeEnabled', 'checked': "python:'themeEnabled' if selected else None", }
_static_4682794896 = {'type': 'hidden', 'value': '', 'name': 'themeEnabled:boolean:default', }
_static_4682804064 = {'class': 'field', }
_static_4682855328 = {'class': 'pat-autotoc autotabs', 'data-pat-autotoc': 'section:fieldset;levels:legend;', }
_static_4682851248 = {'name': 'advanced', 'method': 'post', 'class': 'pat-formunloadalert', 'action': 'request/URL', }
_static_4664499968 = {'class': 'visualClear', }
_static_4651553440 = {'type': 'submit', 'class': 'btn btn-primary cancel', 'name': 'form.button.Cancel', 'value': 'Cancel', }
_static_4665367456 = {'type': 'submit', 'name': 'form.button.DeleteSelected', 'class': 'btn btn-danger save', 'value': 'Delete', }
_static_4676574352 = {'class': 'btn-group', }
_static_4672927872 = {'type': 'hidden', 'name': 'themes:list', 'id': 'deleteConfirmTheme', 'value': 'string:${theme/name}', }
_static_4676628448 = {'name': 'delete', 'method': 'post', 'action': 'request/URL', }
_static_4682580128 = {'class': 'documentDescription', }
_static_4682583392 = {'class': 'documentFirstHeading', }
_static_4682594432 = {'class': 'plone-modal', 'style': 'display:none', 'id': 'string:modal-delete-${theme/name}', }
_static_4680793488 = {'href': '#', 'class': 'btn btn-danger pat-plone-modal', }
_static_4680789792 = {'class': 'btn btn-outline-primary btn-light btn-sm', }
_static_4680789600 = {'method': 'get', 'target': '_blank', 'action': 'string:${context/absolute_url}/++theme++${theme/name}/@@download-zip', }
_static_4680784704 = {'class': 'btn btn-outline-primary btn-light btn-sm', 'type': 'submit', 'name': 'form.button.InvalidateCache', }
_static_4680782880 = {'class': 'btn btn-outline-primary btn-light btn-sm', 'type': 'submit', 'name': 'form.button.Disable', }
_static_4680792528 = {'class': 'btn btn-outline-primary btn-light btn-sm', 'type': 'submit', 'name': 'form.button.Enable', }
_static_4680581424 = {'class': 'btn btn-outline-primary btn-light btn-sm', 'type': 'submit', 'name': 'form.button.Enable', }
_static_4680595008 = {'type': 'hidden', 'name': 'themeName', 'value': 'theme/name', }
_static_4677845536 = {'method': 'post', 'action': 'request/URL', }
_static_4680593664 = {'class': 'themeEntryControls', }
_static_4680594432 = {'class': 'themeDescription', }
_static_4680584784 = {'src': 'theme/preview', }
_static_4680365296 = {'class': 'previewImageContainer', }
_static_4680358576 = {'class': 'themeEntryWrapper', }
_static_4680363232 = {'class': 'themeActive', }
_static_4680364768 = {'class': 'warning', }
_static_4680359200 = {'class': 'themeEntryTitle', }
_static_4683049392 = {'clas': 'themeEntryDetail', }
_static_4683053856 = {'class': 'themeEntry', 'id': 'string:themeEntry-${theme/name}', 'data-theme': 'theme/name', 'data-theme-title': 'theme/title', }
_static_4683042912 = {'id': 'themesList', }
_static_4683052416 = {'class': 'btn btn-large btn-primary pat-plone-modal', 'data-pat-plone-modal': '\n                    width: 85%;\n                    loadLinksWithinModal: true;\n                    content: .content', 'href': 'string:$site_url/@@theming-controlpanel-help', }
_static_4683050784 = {'class': 'btn btn-large btn-primary', 'target': '_blank', 'href': 'string:$site_url/test_rendering#top', }
_static_4683045504 = {'href': '#overlay-upload', 'class': 'btn btn-large btn-primary pat-plone-modal', 'data-pat-plone-modal': 'width: 80%', }
_static_4682741888 = {'class': 'm-1', }
_static_4660409680 = {'id': 'themeControlPanel', 'class': 'pat-autotoc autotabs', 'data-pat-autotoc': 'section:section;levels:h2;', }
_static_4678237920 = {'id': 'content-core', }
_static_4677776624 = {'id': 'setup-link', 'class': 'link-parent', 'href': 'string:$site_url/@@overview-controlpanel', }
_static_4677774320 = {'class': 'documentFirstHeading', }
_static_4427994864 = __C2ZContextWrapper
_static_4427992992 = __compile_zt_expr
_static_4680822608 = {'id': 'viewlet-above-content-title', }
_static_4680813920 = {'id': 'content', }
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
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680821792
            __attrs_4680821792 = _static_4428767312

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div>\n\n        ')

            # <Static value=<ast.Dict object at 0x116ff8d60> name=None at 116ffab60> -> __attrs_4680811136
            __attrs_4680811136 = _static_4680813920

            # <article ... (0:0)
            # --------------------------------------------------------
            __append('<article id="content">\n\n          ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680818288
            __attrs_4680818288 = _static_4428767312

            # <header ... (0:0)
            # --------------------------------------------------------
            __append('<header>\n            ')

            # <Static value=<ast.Dict object at 0x116ffaf50> name=None at 116ffb730> -> __attrs_4677763616
            __attrs_4677763616 = _static_4680822608

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="viewlet-above-content-title">')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680820976
            __default_4680820976 = _DEFAULT_MARKER

            # <Value 'provider:plone.abovecontenttitle' (76:73)> -> __cache_4680813584
            __token = 2797
            try:
                __zt_tmp = __attrs_4677763616
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4680813584 = _static_4427992992('provider', 'plone.abovecontenttitle', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.abovecontenttitle' (76:73)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116ff9bd0> -> __condition
            __expression = __cache_4680813584

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4680813584
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n            ')

            # <Static value=<ast.Dict object at 0x116d12bf0> name=None at 116d10ac0> -> __attrs_4677778016
            __attrs_4677778016 = _static_4677774320

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1 class="documentFirstHeading">')
            __stream_4677777488 = []
            __append_4677777488 = __stream_4677777488.append
            __append_4677777488('Theme settings')
            __msgid_4677777488 = __re_whitespace(''.join(__stream_4677777488)).strip()
            if 'heading_theme_settings':
                __append(translate('heading_theme_settings', mapping=None, default=__msgid_4677777488, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h1>\n\n            ')

            # <Static value=<ast.Dict object at 0x116d134f0> name=None at 116d11d20> -> __attrs_4678231872
            __attrs_4678231872 = _static_4677776624

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a id="setup-link" class="link-parent"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678230240
            __default_4678230240 = _DEFAULT_MARKER

            # <Substitution 'string:$site_url/@@overview-controlpanel' (81:37)> -> __attr_href
            __token = 3044
            try:
                __zt_tmp = __attrs_4678231872
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4427992992('string', '$site_url/@@overview-controlpanel', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append('>')
            __stream_4677776864 = []
            __append_4677776864 = __stream_4677776864.append
            __append_4677776864('\n              Site Setup\n            ')
            __msgid_4677776864 = __re_whitespace(''.join(__stream_4677776864)).strip()
            if __msgid_4677776864:
                __append(translate(__msgid_4677776864, mapping=None, default=__msgid_4677776864, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n          </header>\n\n          ')

            # <Static value=<ast.Dict object at 0x116d83ee0> name=None at 116d81570> -> __attrs_4678240288
            __attrs_4678240288 = _static_4678237920

            # <section ... (0:0)
            # --------------------------------------------------------
            __append('<section id="content-core">\n\n')

            # <Static value=<ast.Dict object at 0x115c83550> name=None at 115c811b0> -> __attrs_4682732048
            __attrs_4682732048 = _static_4660409680

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="themeControlPanel" class="pat-autotoc autotabs" data-pat-autotoc="section:section;levels:h2;">\n\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682730944
            __attrs_4682730944 = _static_4428767312

            # <section ... (0:0)
            # --------------------------------------------------------
            __append('<section>\n        ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682728112
            __attrs_4682728112 = _static_4428767312

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append('<h2>')
            __stream_4682739632 = []
            __append_4682739632 = __stream_4682739632.append
            __append_4682739632('Themes')
            __msgid_4682739632 = __re_whitespace(''.join(__stream_4682739632)).strip()
            if __msgid_4682739632:
                __append(translate(__msgid_4682739632, mapping=None, default=__msgid_4682739632, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h2>\n\n        ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682741504
            __attrs_4682741504 = _static_4428767312

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')
            __stream_4682739872 = []
            __append_4682739872 = __stream_4682739872.append
            __append_4682739872('\n            Use the buttons to create or upload a new Diazo theme,\n            or select an existing theme from a the list below.\n        ')
            __msgid_4682739872 = __re_whitespace(''.join(__stream_4682739872)).strip()
            if 'description_basic_settings':
                __append(translate('description_basic_settings', mapping=None, default=__msgid_4682739872, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n\n        ')

            # <Static value=<ast.Dict object at 0x1171cf880> name=None at 1171cc970> -> __attrs_4682742368
            __attrs_4682742368 = _static_4682741888

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="m-1">\n            <!-- <a href="#overlay-new-theme" class="btn btn-large btn-primary pat-plone-modal"\n                data-pat-plone-modal="width: 80%"\n                i18n:translate="">New theme</a> -->\n\n            ')

            # <Static value=<ast.Dict object at 0x117219a80> name=None at 117219450> -> __attrs_4683041424
            __attrs_4683041424 = _static_4683045504

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a href="#overlay-upload" class="btn btn-large btn-primary pat-plone-modal" data-pat-plone-modal="width: 80%">')
            __stream_4683039360 = []
            __append_4683039360 = __stream_4683039360.append
            __append_4683039360('Upload Zip file')
            __msgid_4683039360 = __re_whitespace(''.join(__stream_4683039360)).strip()
            if __msgid_4683039360:
                __append(translate(__msgid_4683039360, mapping=None, default=__msgid_4683039360, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n\n            ')

            # <Static value=<ast.Dict object at 0x11721af20> name=None at 11721abc0> -> __attrs_4683049296
            __attrs_4683049296 = _static_4683050784

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="btn btn-large btn-primary" target="_blank"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4683054480
            __default_4683054480 = _DEFAULT_MARKER

            # <Substitution 'string:$site_url/test_rendering#top' (109:36)> -> __attr_href
            __token = 4043
            try:
                __zt_tmp = __attrs_4683049296
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4427992992('string', '$site_url/test_rendering#top', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append('>')
            __stream_4683041952 = []
            __append_4683041952 = __stream_4683041952.append
            __append_4683041952('Test Styles')
            __msgid_4683041952 = __re_whitespace(''.join(__stream_4683041952)).strip()
            if __msgid_4683041952:
                __append(translate(__msgid_4683041952, mapping=None, default=__msgid_4683041952, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n\n            ')

            # <Static value=<ast.Dict object at 0x11721b580> name=None at 11721a350> -> __attrs_4683040656
            __attrs_4683040656 = _static_4683052416

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="btn btn-large btn-primary pat-plone-modal" data-pat-plone-modal="\n                    width: 85%;\n                    loadLinksWithinModal: true;\n                    content: .content"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4683043296
            __default_4683043296 = _DEFAULT_MARKER

            # <Substitution 'string:$site_url/@@theming-controlpanel-help' (114:36)> -> __attr_href
            __token = 4249
            try:
                __zt_tmp = __attrs_4683040656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4427992992('string', '$site_url/@@theming-controlpanel-help', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append('>')
            __stream_4683048240 = []
            __append_4683048240 = __stream_4683048240.append
            __append_4683048240('Help')
            __msgid_4683048240 = __re_whitespace(''.join(__stream_4683048240)).strip()
            if __msgid_4683048240:
                __append(translate(__msgid_4683048240, mapping=None, default=__msgid_4683048240, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n        </div>\n\n        ')

            # <Static value=<ast.Dict object at 0x117219060> name=None at 117218370> -> __attrs_4683039456
            __attrs_4683039456 = _static_4683042912

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="themesList">\n\n            ')

            # <Static value=<ast.Dict object at 0x11721bb20> name=None at 117219540> -> __attrs_4683053568
            __attrs_4683053568 = _static_4683053856
            __backup_theme_4683047568 = get('theme', __marker)

            # <Value 'view/themeList' (126:34)> -> __iterator
            __token = 4679
            try:
                __zt_tmp = __attrs_4683053568
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4427992992('path', 'view/themeList', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            (__iterator, ____index_4683054864, ) = getname('repeat')('theme', __iterator)
            econtext['theme'] = None
            for __item in __iterator:
                econtext['theme'] = __item

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4683046752
                __default_4683046752 = _DEFAULT_MARKER

                # <Substitution "python:theme['selected'] and 'themeEntry activeThemeEntry' or 'themeEntry'" (127:38)> -> __attr_class
                __token = 4733
                try:
                    __zt_tmp = __attrs_4683053568
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_4427992992('python', "theme['selected'] and 'themeEntry activeThemeEntry' or 'themeEntry'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', 'themeEntry', _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4683039936
                __default_4683039936 = _DEFAULT_MARKER

                # <Substitution 'string:themeEntry-${theme/name}' (128:34)> -> __attr_id
                __token = 4843
                try:
                    __zt_tmp = __attrs_4683053568
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_4427992992('string', 'themeEntry-${theme/name}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4683044208
                __default_4683044208 = _DEFAULT_MARKER

                # <Substitution 'theme/name' (129:41)> -> __attr_data_theme
                __token = 4918
                try:
                    __zt_tmp = __attrs_4683053568
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_theme = _static_4427992992('path', 'theme/name', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_data_theme = __quote(__attr_data_theme, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_data_theme is not None):
                    __append((' data-theme="%s"' % __attr_data_theme))

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4683052752
                __default_4683052752 = _DEFAULT_MARKER

                # <Substitution 'theme/title' (130:46)> -> __attr_data_theme_title
                __token = 4978
                try:
                    __zt_tmp = __attrs_4683053568
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_theme_title = _static_4427992992('path', 'theme/title', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_data_theme_title = __quote(__attr_data_theme_title, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_data_theme_title is not None):
                    __append((' data-theme-title="%s"' % __attr_data_theme_title))
                __append('>\n\n                ')

                # <Static value=<ast.Dict object at 0x11721a9b0> name=None at 117218100> -> __attrs_4680352816
                __attrs_4680352816 = _static_4683049392

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div clas="themeEntryDetail">\n\n                    ')

                # <Static value=<ast.Dict object at 0x116f89d20> name=None at 116f89720> -> __attrs_4680360256
                __attrs_4680360256 = _static_4680359200

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span class="themeEntryTitle">\n                        ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680352384
                __attrs_4680352384 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680366400
                __default_4680366400 = _DEFAULT_MARKER

                # <Value 'theme/title' (135:43)> -> __cache_4680362512
                __token = 5138
                try:
                    __zt_tmp = __attrs_4680352384
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4680362512 = _static_4427992992('path', 'theme/title', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'theme/title' (135:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116f8bf70> -> __condition
                __expression = __cache_4680362512

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>Title</span>')
                else:
                    __content = __cache_4680362512
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('\n                        ')

                # <Static value=<ast.Dict object at 0x116f8b2e0> name=None at 116f8b9a0> -> __attrs_4680368080
                __attrs_4680368080 = _static_4680364768

                # <Value 'theme/override' (136:61)> -> __condition
                __token = 5225
                try:
                    __zt_tmp = __attrs_4680368080
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'theme/override', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="warning">')
                    __stream_4680358480 = []
                    __append_4680358480 = __stream_4680358480.append
                    __append_4680358480('(this theme overrides a filesystem theme)')
                    __msgid_4680358480 = __re_whitespace(''.join(__stream_4680358480)).strip()
                    if __msgid_4680358480:
                        __append(translate(__msgid_4680358480, mapping=None, default=__msgid_4680358480, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>')
                __append('\n                        ')

                # <Static value=<ast.Dict object at 0x116f8ace0> name=None at 116f88520> -> __attrs_4680364624
                __attrs_4680364624 = _static_4680363232

                # <Value 'theme/selected' (138:43)> -> __condition
                __token = 5381
                try:
                    __zt_tmp = __attrs_4680364624
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'theme/selected', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="themeActive">')
                    __stream_4680366112 = []
                    __append_4680366112 = __stream_4680366112.append
                    __append_4680366112('(active)')
                    __msgid_4680366112 = __re_whitespace(''.join(__stream_4680366112)).strip()
                    if __msgid_4680366112:
                        __append(translate(__msgid_4680366112, mapping=None, default=__msgid_4680366112, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>')
                __append('\n                    </span>\n\n                    ')

                # <Static value=<ast.Dict object at 0x116f89ab0> name=None at 116f8a8f0> -> __attrs_4680364384
                __attrs_4680364384 = _static_4680358576

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="themeEntryWrapper">\n\n                        ')

                # <Static value=<ast.Dict object at 0x116f8b4f0> name=None at 116f89ed0> -> __attrs_4680588960
                __attrs_4680588960 = _static_4680365296

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="previewImageContainer">\n                            ')

                # <Static value=<ast.Dict object at 0x116fc0e50> name=None at 116fc28f0> -> __attrs_4680583872
                __attrs_4680583872 = _static_4680584784

                # <img ... (0:0)
                # --------------------------------------------------------
                __append('<img')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680595392
                __default_4680595392 = _DEFAULT_MARKER

                # <Substitution 'theme/preview' (146:53)> -> __attr_src
                __token = 5702
                try:
                    __zt_tmp = __attrs_4680583872
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_src = _static_4427992992('path', 'theme/preview', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_src is not None):
                    __append((' src="%s"' % __attr_src))
                __append(' />\n                        </div>\n\n                        ')

                # <Static value=<ast.Dict object at 0x116fc3400> name=None at 116fc0970> -> __attrs_4680586944
                __attrs_4680586944 = _static_4680594432

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="themeDescription">')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680584304
                __default_4680584304 = _DEFAULT_MARKER

                # <Value 'theme/description' (149:67)> -> __cache_4680591744
                __token = 5819
                try:
                    __zt_tmp = __attrs_4680586944
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4680591744 = _static_4427992992('path', 'theme/description', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'theme/description' (149:67)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116fc2ef0> -> __condition
                __expression = __cache_4680591744

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4680591744
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</div>\n\n                        ')

                # <Static value=<ast.Dict object at 0x116fc3100> name=None at 116fc0730> -> __attrs_4680590256
                __attrs_4680590256 = _static_4680593664

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="themeEntryControls">\n\n                            ')

                # <Static value=<ast.Dict object at 0x116d24220> name=None at 116d263e0> -> __attrs_4678252624
                __attrs_4678252624 = _static_4677845536

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form method="post"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678249504
                __default_4678249504 = _DEFAULT_MARKER

                # <Substitution 'request/URL' (153:71)> -> __attr_action
                __token = 5971
                try:
                    __zt_tmp = __attrs_4678252624
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_action = _static_4427992992('path', 'request/URL', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_action is not None):
                    __append((' action="%s"' % __attr_action))
                __append('>\n                                ')

                # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680591168
                __attrs_4680591168 = _static_4428767312

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678014512
                __default_4678014512 = _DEFAULT_MARKER

                # <Value 'context/@@authenticator/authenticator' (154:62)> -> __cache_4677770144
                __token = 6047
                try:
                    __zt_tmp = __attrs_4680591168
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4677770144 = _static_4427992992('path', 'context/@@authenticator/authenticator', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'context/@@authenticator/authenticator' (154:62)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116d4ee90> -> __condition
                __expression = __cache_4677770144

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input />')
                else:
                    __content = __cache_4677770144
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n                                ')

                # <Static value=<ast.Dict object at 0x116fc3640> name=None at 116fc19f0> -> __attrs_4680591216
                __attrs_4680591216 = _static_4680595008

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="themeName"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680589248
                __default_4680589248 = _DEFAULT_MARKER

                # <Substitution 'theme/name' (155:92)> -> __attr_value
                __token = 6181
                try:
                    __zt_tmp = __attrs_4680591216
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'theme/name', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n                                ')

                # <Static value=<ast.Dict object at 0x116fc0130> name=None at 116fc0a90> -> __attrs_4680785760
                __attrs_4680785760 = _static_4680581424

                # <Value 'not:theme/selected' (157:51)> -> __condition
                __token = 6287
                try:
                    __zt_tmp = __attrs_4680785760
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('not', 'theme/selected', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="btn btn-outline-primary btn-light btn-sm" type="submit" name="form.button.Enable">')
                    __stream_4680589536 = []
                    __append_4680589536 = __stream_4680589536.append
                    __append_4680589536('Activate')
                    __msgid_4680589536 = __re_whitespace(''.join(__stream_4680589536)).strip()
                    if __msgid_4680589536:
                        __append(translate(__msgid_4680589536, mapping=None, default=__msgid_4680589536, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>')
                __append('\n                                ')

                # <Static value=<ast.Dict object at 0x116ff39d0> name=None at 116ff1c60> -> __attrs_4680781200
                __attrs_4680781200 = _static_4680792528

                # <Value 'theme/selected' (163:51)> -> __condition
                __token = 6667
                try:
                    __zt_tmp = __attrs_4680781200
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'theme/selected', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="btn btn-outline-primary btn-light btn-sm" type="submit" name="form.button.Enable">')
                    __stream_4680792144 = []
                    __append_4680792144 = __stream_4680792144.append
                    __append_4680792144('Update')
                    __msgid_4680792144 = __re_whitespace(''.join(__stream_4680792144)).strip()
                    if __msgid_4680792144:
                        __append(translate(__msgid_4680792144, mapping=None, default=__msgid_4680792144, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>')
                __append('\n                                ')

                # <Static value=<ast.Dict object at 0x116ff1420> name=None at 116ff1ea0> -> __attrs_4680790656
                __attrs_4680790656 = _static_4680782880

                # <Value 'theme/selected' (169:51)> -> __condition
                __token = 7041
                try:
                    __zt_tmp = __attrs_4680790656
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'theme/selected', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="btn btn-outline-primary btn-light btn-sm" type="submit" name="form.button.Disable">')
                    __stream_4680778368 = []
                    __append_4680778368 = __stream_4680778368.append
                    __append_4680778368('Deactivate')
                    __msgid_4680778368 = __re_whitespace(''.join(__stream_4680778368)).strip()
                    if __msgid_4680778368:
                        __append(translate(__msgid_4680778368, mapping=None, default=__msgid_4680778368, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>')
                __append('\n                                ')

                # <Static value=<ast.Dict object at 0x116ff1b40> name=None at 116ff1360> -> __attrs_4680788688
                __attrs_4680788688 = _static_4680784704

                # <Value 'theme/selected' (175:51)> -> __condition
                __token = 7420
                try:
                    __zt_tmp = __attrs_4680788688
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'theme/selected', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="btn btn-outline-primary btn-light btn-sm" type="submit" name="form.button.InvalidateCache">')
                    __stream_4680777840 = []
                    __append_4680777840 = __stream_4680777840.append
                    __append_4680777840('Clear Cache')
                    __msgid_4680777840 = __re_whitespace(''.join(__stream_4680777840)).strip()
                    if __msgid_4680777840:
                        __append(translate(__msgid_4680777840, mapping=None, default=__msgid_4680777840, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>')
                __append('\n                            </form>\n\n                            ')

                # <Static value=<ast.Dict object at 0x116ff2e60> name=None at 116ff0f10> -> __attrs_4680788208
                __attrs_4680788208 = _static_4680789600

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form method="get" target="_blank"')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680786096
                __default_4680786096 = _DEFAULT_MARKER

                # <Substitution 'string:${context/absolute_url}/++theme++${theme/name}/@@download-zip' (182:86)> -> __attr_action
                __token = 7840
                try:
                    __zt_tmp = __attrs_4680788208
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_action = _static_4427992992('string', '${context/absolute_url}/++theme++${theme/name}/@@download-zip', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_action is not None):
                    __append((' action="%s"' % __attr_action))
                __append('>\n                                ')

                # <Static value=<ast.Dict object at 0x116ff2f20> name=None at 116ff1f30> -> __attrs_4680788928
                __attrs_4680788928 = _static_4680789792

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="btn btn-outline-primary btn-light btn-sm">')
                __stream_4680793440 = []
                __append_4680793440 = __stream_4680793440.append
                __append_4680793440('Download')
                __msgid_4680793440 = __re_whitespace(''.join(__stream_4680793440)).strip()
                if __msgid_4680793440:
                    __append(translate(__msgid_4680793440, mapping=None, default=__msgid_4680793440, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</button>\n                            </form>\n\n                            ')

                # <Static value=<ast.Dict object at 0x116ff3d90> name=None at 116ff3970> -> __attrs_4682591504
                __attrs_4682591504 = _static_4680793488

                # <Value 'theme/editable' (188:47)> -> __condition
                __token = 8235
                try:
                    __zt_tmp = __attrs_4682591504
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'theme/editable', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680787056
                    __default_4680787056 = _DEFAULT_MARKER

                    # <Substitution 'string:#modal-delete-${theme/name}' (189:53)> -> __attr_href
                    __token = 8304
                    try:
                        __zt_tmp = __attrs_4682591504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4427992992('string', '#modal-delete-${theme/name}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' class="btn btn-danger pat-plone-modal">')
                    __stream_4680789264 = []
                    __append_4680789264 = __stream_4680789264.append
                    __append_4680789264('Delete')
                    __msgid_4680789264 = __re_whitespace(''.join(__stream_4680789264)).strip()
                    if __msgid_4680789264:
                        __append(translate(__msgid_4680789264, mapping=None, default=__msgid_4680789264, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</a>')
                __append('\n                                <!-- Delete confirmation overlay -->\n                            ')

                # <Static value=<ast.Dict object at 0x1171ab880> name=None at 1171abe80> -> __attrs_4682581280
                __attrs_4682581280 = _static_4682594432

                # <Value 'theme/editable' (195:47)> -> __condition
                __token = 8709
                try:
                    __zt_tmp = __attrs_4682581280
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4427992992('path', 'theme/editable', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="plone-modal" style="display:none"')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682584352
                    __default_4682584352 = _DEFAULT_MARKER

                    # <Substitution 'string:modal-delete-${theme/name}' (194:51)> -> __attr_id
                    __token = 8627
                    try:
                        __zt_tmp = __attrs_4682581280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_4427992992('string', 'modal-delete-${theme/name}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))
                    __append('>\n                                ')

                    # <Static value=<ast.Dict object at 0x1171a8d60> name=None at 1171a8370> -> __attrs_4682589152
                    __attrs_4682589152 = _static_4682583392

                    # <h1 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h1 class="documentFirstHeading">')
                    __stream_4671786784_theme_name = ''
                    __stream_4682587424 = []
                    __append_4682587424 = __stream_4682587424.append
                    __append_4682587424('\n                                    Are you sure you want to delete ')
                    __stream_4671786784_theme_name = []
                    __append_4671786784_theme_name = __stream_4671786784_theme_name.append

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682595248
                    __attrs_4682595248 = _static_4428767312

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_4671786784_theme_name('<span>')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682596304
                    __default_4682596304 = _DEFAULT_MARKER

                    # <Value 'string:${theme/name}' (198:53)> -> __cache_4682583584
                    __token = 8972
                    try:
                        __zt_tmp = __attrs_4682595248
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4682583584 = _static_4427992992('string', '${theme/name}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'string:${theme/name}' (198:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1171a8a60> -> __condition
                    __expression = __cache_4682583584

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4682583584
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_4671786784_theme_name(__content)
                    __append_4671786784_theme_name('</span>')
                    __append_4682587424('${theme_name}')
                    __stream_4671786784_theme_name = ''.join(__stream_4671786784_theme_name)
                    __append_4682587424('\n                                ')
                    __msgid_4682587424 = __re_whitespace(''.join(__stream_4682587424)).strip()
                    if 'theming_controlpanel_delete_confirm':
                        __append(translate('theming_controlpanel_delete_confirm', mapping={'theme_name': __stream_4671786784_theme_name, }, default=__msgid_4682587424, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</h1>\n\n                                ')

                    # <Static value=<ast.Dict object at 0x1171a80a0> name=None at 1171aa350> -> __attrs_4664163584
                    __attrs_4664163584 = _static_4682580128

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="documentDescription">')
                    __stream_4682582096 = []
                    __append_4682582096 = __stream_4682582096.append
                    __append_4682582096('\n                                    This operation cannot be undone. Note that filesystem themes\n                                    cannot be deleted from within Plone.\n                                ')
                    __msgid_4682582096 = __re_whitespace(''.join(__stream_4682582096)).strip()
                    if 'theming_controlpanel_delete_confirm_description':
                        __append(translate('theming_controlpanel_delete_confirm_description', mapping=None, default=__msgid_4682582096, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>\n\n                                ')

                    # <Static value=<ast.Dict object at 0x116bfafe0> name=None at 116bfbdc0> -> __attrs_4664494400
                    __attrs_4664494400 = _static_4676628448

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form name="delete" method="post"')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4664154608
                    __default_4664154608 = _DEFAULT_MARKER

                    # <Substitution 'request/URL' (207:89)> -> __attr_action
                    __token = 9530
                    try:
                        __zt_tmp = __attrs_4664494400
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_4427992992('path', 'request/URL', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((' action="%s"' % __attr_action))
                    __append('>\n                                    ')

                    # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4672917024
                    __attrs_4672917024 = _static_4428767312

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4672923936
                    __default_4672923936 = _DEFAULT_MARKER

                    # <Value 'context/@@authenticator/authenticator' (208:66)> -> __cache_4672919856
                    __token = 9610
                    try:
                        __zt_tmp = __attrs_4672917024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4672919856 = _static_4427992992('path', 'context/@@authenticator/authenticator', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                    # <BinOp left=<Value 'context/@@authenticator/authenticator' (208:66)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116872c20> -> __condition
                    __expression = __cache_4672919856

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input />')
                    else:
                        __content = __cache_4672919856
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n                                    ')

                    # <Static value=<ast.Dict object at 0x116873880> name=None at 116871600> -> __attrs_4672921968
                    __attrs_4672921968 = _static_4672927872

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="hidden" name="themes:list" id="deleteConfirmTheme"')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4672916784
                    __default_4672916784 = _DEFAULT_MARKER

                    # <Substitution 'string:${theme/name}' (211:62)> -> __attr_value
                    __token = 9854
                    try:
                        __zt_tmp = __attrs_4672921968
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_4427992992('string', '${theme/name}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n                                    ')

                    # <Static value=<ast.Dict object at 0x116bedc90> name=None at 116befb20> -> __attrs_4676576512
                    __attrs_4676576512 = _static_4676574352

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="btn-group">\n                                        ')

                    # <Static value=<ast.Dict object at 0x11613dba0> name=None at 11618a950> -> __attrs_4676501616
                    __attrs_4676501616 = _static_4665367456

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="submit" name="form.button.DeleteSelected" class="btn btn-danger save"')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4676516160
                    __default_4676516160 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<ast.Constant object at 0x115f4a650> at 115f4afe0> -> __attr_value
                    __attr_value = 'Delete'
                    __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n                                        ')

                    # <Static value=<ast.Dict object at 0x1154112a0> name=None at 107cbe8c0> -> __attrs_4682843760
                    __attrs_4682843760 = _static_4651553440

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="submit" class="btn btn-primary cancel" name="form.button.Cancel"')

                    # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4664909760
                    __default_4664909760 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<ast.Constant object at 0x1160cce20> at 1160cf7f0> -> __attr_value
                    __attr_value = 'Cancel'
                    __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n                                    </div>\n                                </form>\n                            </div>')
                __append('\n\n                        </div>\n\n                    </div>\n\n                 </div>\n            </div>')
                ____index_4683054864 -= 1
                if (____index_4683054864 > 0):
                    __append('\n            ')
            if (__backup_theme_4683047568 is __marker):
                del econtext['theme']
            else:
                econtext['theme'] = __backup_theme_4683047568
            __append('\n\n            ')

            # <Static value=<ast.Dict object at 0x116069f00> name=None at 116bee920> -> __attrs_4682844336
            __attrs_4682844336 = _static_4664499968

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="visualClear"><!-- --></div>\n\n        </div>\n    </section>\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682858448
            __attrs_4682858448 = _static_4428767312

            # <section ... (0:0)
            # --------------------------------------------------------
            __append('<section>\n        ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682848080
            __attrs_4682848080 = _static_4428767312

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append('<h2>')
            __stream_4682846592 = []
            __append_4682846592 = __stream_4682846592.append
            __append_4682846592('Advanced settings')
            __msgid_4682846592 = __re_whitespace(''.join(__stream_4682846592)).strip()
            if __msgid_4682846592:
                __append(translate(__msgid_4682846592, mapping=None, default=__msgid_4682846592, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h2>\n\n        ')

            # <Static value=<ast.Dict object at 0x1171ea3b0> name=None at 1171e9ea0> -> __attrs_4682850720
            __attrs_4682850720 = _static_4682851248
            __backup_errors_4683050880 = get('errors', __marker)

            # <Value 'view/errors' (250:31)> -> __value
            __token = 11353
            try:
                __zt_tmp = __attrs_4682850720
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'view/errors', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['errors'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form name="advanced" method="post" class="pat-formunloadalert"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682858112
            __default_4682858112 = _DEFAULT_MARKER

            # <Substitution 'request/URL' (249:35)> -> __attr_action
            __token = 11309
            try:
                __zt_tmp = __attrs_4682850720
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_4427992992('path', 'request/URL', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append('>\n\n            ')

            # <Static value=<ast.Dict object at 0x1171eb3a0> name=None at 1171e9e70> -> __attrs_4682843472
            __attrs_4682843472 = _static_4682855328

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="pat-autotoc autotabs" data-pat-autotoc="section:fieldset;levels:legend;">\n                ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682844912
            __attrs_4682844912 = _static_4428767312

            # <fieldset ... (0:0)
            # --------------------------------------------------------
            __append('<fieldset>\n                    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682850144
            __attrs_4682850144 = _static_4428767312

            # <legend ... (0:0)
            # --------------------------------------------------------
            __append('<legend>')
            __stream_4682848128 = []
            __append_4682848128 = __stream_4682848128.append
            __append_4682848128('Theme details')
            __msgid_4682848128 = __re_whitespace(''.join(__stream_4682848128)).strip()
            if __msgid_4682848128:
                __append(translate(__msgid_4682848128, mapping=None, default=__msgid_4682848128, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</legend>\n\n                    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682845104
            __attrs_4682845104 = _static_4428767312

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')
            __stream_4682845152 = []
            __append_4682845152 = __stream_4682845152.append
            __append_4682845152('\n                       Use the fields below to configure the Diazo theme\n                       manually. Usually, these settings are applied by\n                       enabling a theme from the ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682853696
            __attrs_4682853696 = _static_4428767312

            # <strong ... (0:0)
            # --------------------------------------------------------
            __append_4682845152('<strong>Themes</strong>\n                       tab.\n                    ')
            __msgid_4682845152 = __re_whitespace(''.join(__stream_4682845152)).strip()
            if 'description_advanced':
                __append(translate('description_advanced', mapping=None, default=__msgid_4682845152, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n\n                    ')

            # <Static value=<ast.Dict object at 0x1171deb60> name=None at 1171de080> -> __attrs_4682799504
            __attrs_4682799504 = _static_4682804064
            __backup_selected_4678273152 = get('selected', __marker)

            # <Value "python:request.get('themeEnabled', view.theme_settings.enabled)" (266:45)> -> __value
            __token = 12021
            try:
                __zt_tmp = __attrs_4682799504
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', "request.get('themeEnabled', view.theme_settings.enabled)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['selected'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="field">\n\n                        ')

            # <Static value=<ast.Dict object at 0x1171dc790> name=None at 1171ddea0> -> __attrs_4682799264
            __attrs_4682799264 = _static_4682794896

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" value="" name="themeEnabled:boolean:default" />\n                        ')

            # <Static value=<ast.Dict object at 0x1171dfac0> name=None at 1171dfe80> -> __attrs_4682809200
            __attrs_4682809200 = _static_4682808000

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="checkbox" value="1" name="themeEnabled:boolean" id="themeEnabled"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682798784
            __default_4682798784 = _DEFAULT_MARKER

            # <Boolean "python:'themeEnabled' if selected else None" (270:52)> -> __attr_checked
            __token = 12336
            try:
                __zt_tmp = __attrs_4682809200
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_checked = _static_4427992992('python', "'themeEnabled' if selected else None", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if (__attr_checked is _DEFAULT_MARKER):
                __attr_checked = None
            else:
                if __attr_checked:
                    __attr_checked = 'checked'
                else:
                    __attr_checked = None
            if (__attr_checked is not None):
                __append((' checked="%s"' % __attr_checked))
            __append(' />\n                        ')

            # <Static value=<ast.Dict object at 0x1171dffd0> name=None at 1171dfdc0> -> __attrs_4682797104
            __attrs_4682797104 = _static_4682809296

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="themeEnabled">')
            __stream_4682803008 = []
            __append_4682803008 = __stream_4682803008.append
            __append_4682803008('Theme enabled')
            __msgid_4682803008 = __re_whitespace(''.join(__stream_4682803008)).strip()
            if 'label_theme_enabled':
                __append(translate('label_theme_enabled', mapping=None, default=__msgid_4682803008, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n                        ')

            # <Static value=<ast.Dict object at 0x1171dceb0> name=None at 1171de140> -> __attrs_4682806560
            __attrs_4682806560 = _static_4682796720

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="formHelp">')
            __stream_4682803440 = []
            __append_4682803440 = __stream_4682803440.append
            __append_4682803440('\n                            If enabled the currently configured Diazo theme (if any)\n                            will be applied.\n                        ')
            __msgid_4682803440 = __re_whitespace(''.join(__stream_4682803440)).strip()
            if 'help_theme_enabled':
                __append(translate('help_theme_enabled', mapping=None, default=__msgid_4682803440, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n                    </div>')
            if (__backup_selected_4678273152 is __marker):
                del econtext['selected']
            else:
                econtext['selected'] = __backup_selected_4678273152
            __append('\n\n                    ')

            # <Static value=<ast.Dict object at 0x1171dedd0> name=None at 1171dc0a0> -> __attrs_4682802912
            __attrs_4682802912 = _static_4682804688
            __backup_error_4683177536 = get('error', __marker)

            # <Value 'errors/rules | nothing' (281:42)> -> __value
            __token = 12861
            try:
                __zt_tmp = __attrs_4682802912
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'errors/rules | nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['error'] = __value
            __backup_rules_4678285776 = get('rules', __marker)

            # <Value "python:request.get('rules', view.theme_settings.rules)" (282:41)> -> __value
            __token = 12926
            try:
                __zt_tmp = __attrs_4682802912
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', "request.get('rules', view.theme_settings.rules)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['rules'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682793984
            __default_4682793984 = _DEFAULT_MARKER

            # <Substitution "python:'field error' if error else 'field'" (283:46)> -> __attr_class
            __token = 13029
            try:
                __zt_tmp = __attrs_4682802912
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4427992992('python', "'field error' if error else 'field'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))
            __append('>\n\n                        ')

            # <Static value=<ast.Dict object at 0x1171dd150> name=None at 1171dd0c0> -> __attrs_4682794224
            __attrs_4682794224 = _static_4682797392

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="rules">')
            __stream_4682799408 = []
            __append_4682799408 = __stream_4682799408.append
            __append_4682799408('Rules file')
            __msgid_4682799408 = __re_whitespace(''.join(__stream_4682799408)).strip()
            if 'label_rules':
                __append(translate('label_rules', mapping=None, default=__msgid_4682799408, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n                        ')

            # <Static value=<ast.Dict object at 0x116fa6b90> name=None at 116fa5000> -> __attrs_4680478112
            __attrs_4680478112 = _static_4680477584

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="formHelp">')
            __stream_4680466592 = []
            __append_4680466592 = __stream_4680466592.append
            __append_4680466592('\n                            Enter a path or URL for the theme rules file.\n                        ')
            __msgid_4680466592 = __re_whitespace(''.join(__stream_4680466592)).strip()
            if 'help_rules':
                __append(translate('help_rules', mapping=None, default=__msgid_4680466592, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n                        ')

            # <Static value=<ast.Dict object at 0x116fa4580> name=None at 116fa4370> -> __attrs_4680470816
            __attrs_4680470816 = _static_4680467840

            # <Value 'error' (290:85)> -> __condition
            __token = 13432
            try:
                __zt_tmp = __attrs_4680470816
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="errorMessage">')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680479552
                __default_4680479552 = _DEFAULT_MARKER

                # <Value 'error' (290:63)> -> __cache_4680469616
                __token = 13410
                try:
                    __zt_tmp = __attrs_4680470816
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4680469616 = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'error' (290:63)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116fa6aa0> -> __condition
                __expression = __cache_4680469616

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4680469616
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</div>')
            __append('\n\n                        ')

            # <Static value=<ast.Dict object at 0x116fa7a60> name=None at 116fa4ca0> -> __attrs_4680481280
            __attrs_4680481280 = _static_4680481376

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input name="rules" id="rules" type="text" size="50"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680479168
            __default_4680479168 = _DEFAULT_MARKER

            # <Substitution 'rules' (297:50)> -> __attr_value
            __token = 13682
            try:
                __zt_tmp = __attrs_4680481280
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_4427992992('path', 'rules', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' />\n\n                    </div>')
            if (__backup_rules_4678285776 is __marker):
                del econtext['rules']
            else:
                econtext['rules'] = __backup_rules_4678285776
            if (__backup_error_4683177536 is __marker):
                del econtext['error']
            else:
                econtext['error'] = __backup_error_4683177536
            __append('\n\n                    ')

            # <Static value=<ast.Dict object at 0x116fa7fd0> name=None at 116fa7970> -> __attrs_4680466928
            __attrs_4680466928 = _static_4680482768
            __backup_error_4683178448 = get('error', __marker)

            # <Value 'errors/absolutePrefix | nothing' (303:42)> -> __value
            __token = 13816
            try:
                __zt_tmp = __attrs_4680466928
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'errors/absolutePrefix | nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['error'] = __value
            __backup_absolutePrefix_4672922064 = get('absolutePrefix', __marker)

            # <Value "python:request.get('absolutePrefix', view.theme_settings.absolutePrefix)" (304:50)> -> __value
            __token = 13899
            try:
                __zt_tmp = __attrs_4680466928
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', "request.get('absolutePrefix', view.theme_settings.absolutePrefix)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['absolutePrefix'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680473312
            __default_4680473312 = _DEFAULT_MARKER

            # <Substitution "python:'field error' if error else 'field'" (305:46)> -> __attr_class
            __token = 14020
            try:
                __zt_tmp = __attrs_4680466928
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4427992992('python', "'field error' if error else 'field'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))
            __append('>\n\n                        ')

            # <Static value=<ast.Dict object at 0x117222230> name=None at 117220bb0> -> __attrs_4683074048
            __attrs_4683074048 = _static_4683080240

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="absolutePrefix">')
            __stream_4683083696 = []
            __append_4683083696 = __stream_4683083696.append
            __append_4683083696('Absolute path prefix')
            __msgid_4683083696 = __re_whitespace(''.join(__stream_4683083696)).strip()
            if 'label_absolute_prefix':
                __append(translate('label_absolute_prefix', mapping=None, default=__msgid_4683083696, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n                        ')

            # <Static value=<ast.Dict object at 0x117220220> name=None at 117222bc0> -> __attrs_4683078800
            __attrs_4683078800 = _static_4683072032

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="formHelp">')
            __stream_4683075632 = []
            __append_4683075632 = __stream_4683075632.append
            __append_4683075632('\n                            If your theme uses relative paths for images, stylesheets\n                            or other resources, you can enter a prefix here to make\n                            sure these resources will work regardless of which page\n                            Plone is rendering.\n                        ')
            __msgid_4683075632 = __re_whitespace(''.join(__stream_4683075632)).strip()
            if 'help_absolute_prefix':
                __append(translate('help_absolute_prefix', mapping=None, default=__msgid_4683075632, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n                        ')

            # <Static value=<ast.Dict object at 0x117222770> name=None at 117222680> -> __attrs_4683086816
            __attrs_4683086816 = _static_4683081584

            # <Value 'error' (315:85)> -> __condition
            __token = 14690
            try:
                __zt_tmp = __attrs_4683086816
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="errorMessage">')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4683085952
                __default_4683085952 = _DEFAULT_MARKER

                # <Value 'error' (315:63)> -> __cache_4683071984
                __token = 14668
                try:
                    __zt_tmp = __attrs_4683086816
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4683071984 = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'error' (315:63)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1172221d0> -> __condition
                __expression = __cache_4683071984

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4683071984
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</div>')
            __append('\n\n                        ')

            # <Static value=<ast.Dict object at 0x117221060> name=None at 1172228f0> -> __attrs_4683077360
            __attrs_4683077360 = _static_4683075680

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input name="absolutePrefix" id="absolutePrefix" type="text" size="50"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4683080816
            __default_4683080816 = _DEFAULT_MARKER

            # <Substitution 'absolutePrefix' (322:50)> -> __attr_value
            __token = 14958
            try:
                __zt_tmp = __attrs_4683077360
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_4427992992('path', 'absolutePrefix', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' />\n\n                    </div>')
            if (__backup_absolutePrefix_4672922064 is __marker):
                del econtext['absolutePrefix']
            else:
                econtext['absolutePrefix'] = __backup_absolutePrefix_4672922064
            if (__backup_error_4683178448 is __marker):
                del econtext['error']
            else:
                econtext['error'] = __backup_error_4683178448
            __append('\n\n                    ')

            # <Static value=<ast.Dict object at 0x117223190> name=None at 1172230d0> -> __attrs_4683074528
            __attrs_4683074528 = _static_4683084176
            __backup_error_4680363904 = get('error', __marker)

            # <Value 'errors/doctype | nothing' (328:42)> -> __value
            __token = 15101
            try:
                __zt_tmp = __attrs_4683074528
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'errors/doctype | nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['error'] = __value
            __backup_doctype_4682846832 = get('doctype', __marker)

            # <Value "python:request.get('doctype', view.theme_settings.doctype)" (329:43)> -> __value
            __token = 15170
            try:
                __zt_tmp = __attrs_4683074528
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', "request.get('doctype', view.theme_settings.doctype)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['doctype'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4683084512
            __default_4683084512 = _DEFAULT_MARKER

            # <Substitution "python:'field error' if error else 'field'" (330:46)> -> __attr_class
            __token = 15277
            try:
                __zt_tmp = __attrs_4683074528
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4427992992('python', "'field error' if error else 'field'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))
            __append('>\n\n                        ')

            # <Static value=<ast.Dict object at 0x117223e20> name=None at 117220400> -> __attrs_4683076064
            __attrs_4683076064 = _static_4683087392

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="doctype">')
            __stream_4683074240 = []
            __append_4683074240 = __stream_4683074240.append
            __append_4683074240('Doctype')
            __msgid_4683074240 = __re_whitespace(''.join(__stream_4683074240)).strip()
            if 'label_doctype':
                __append(translate('label_doctype', mapping=None, default=__msgid_4683074240, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n                        ')

            # <Static value=<ast.Dict object at 0x117223f40> name=None at 117223d60> -> __attrs_4683076112
            __attrs_4683076112 = _static_4683087680

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="formHelp">')
            __stream_4683083504 = []
            __append_4683083504 = __stream_4683083504.append
            __append_4683083504('\n                            You can specify a Doctype string which will be set on\n                            the output, for example "&lt;!DOCTYPE html&gt;". If left\n                            blank the default XHTML 1.0 transistional Doctype or\n                            that set in the Diazo theme is used.\n                        ')
            __msgid_4683083504 = __re_whitespace(''.join(__stream_4683083504)).strip()
            if 'help_doctype':
                __append(translate('help_doctype', mapping=None, default=__msgid_4683083504, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n                        ')

            # <Static value=<ast.Dict object at 0x11719e410> name=None at 11719ed70> -> __attrs_4682540528
            __attrs_4682540528 = _static_4682540048

            # <Value 'error' (340:85)> -> __condition
            __token = 15922
            try:
                __zt_tmp = __attrs_4682540528
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="errorMessage">')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682540144
                __default_4682540144 = _DEFAULT_MARKER

                # <Value 'error' (340:63)> -> __cache_4682541296
                __token = 15900
                try:
                    __zt_tmp = __attrs_4682540528
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4682541296 = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'error' (340:63)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 11719f0a0> -> __condition
                __expression = __cache_4682541296

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4682541296
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</div>')
            __append('\n\n                        ')

            # <Static value=<ast.Dict object at 0x11719ef50> name=None at 11719ef80> -> __attrs_4682535968
            __attrs_4682535968 = _static_4682542928

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input name="doctype" id="doctype" type="text" size="50"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682532320
            __default_4682532320 = _DEFAULT_MARKER

            # <Substitution 'doctype' (347:50)> -> __attr_value
            __token = 16176
            try:
                __zt_tmp = __attrs_4682535968
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_4427992992('path', 'doctype', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' />\n\n                    </div>')
            if (__backup_doctype_4682846832 is __marker):
                del econtext['doctype']
            else:
                econtext['doctype'] = __backup_doctype_4682846832
            if (__backup_error_4680363904 is __marker):
                del econtext['error']
            else:
                econtext['error'] = __backup_error_4680363904
            __append('\n\n                    ')

            # <Static value=<ast.Dict object at 0x11719fb20> name=None at 11719f940> -> __attrs_4682537264
            __attrs_4682537264 = _static_4682545952
            __backup_selected_4683079808 = get('selected', __marker)

            # <Value "python:request.get('readNetwork', view.theme_settings.readNetwork)" (354:45)> -> __value
            __token = 16353
            try:
                __zt_tmp = __attrs_4682537264
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', "request.get('readNetwork', view.theme_settings.readNetwork)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['selected'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="field">\n\n                        ')

            # <Static value=<ast.Dict object at 0x11719f880> name=None at 11719cfd0> -> __attrs_4682539424
            __attrs_4682539424 = _static_4682545280

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" value="" name="readNetwork:boolean:default" />\n                        ')

            # <Static value=<ast.Dict object at 0x11719f1f0> name=None at 11719d9f0> -> __attrs_4682543984
            __attrs_4682543984 = _static_4682543600

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="checkbox" value="1" name="readNetwork:boolean" id="readNetwork"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682541632
            __default_4682541632 = _DEFAULT_MARKER

            # <Boolean "python:'readNetwork' if selected else None" (358:52)> -> __attr_checked
            __token = 16668
            try:
                __zt_tmp = __attrs_4682543984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_checked = _static_4427992992('python', "'readNetwork' if selected else None", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if (__attr_checked is _DEFAULT_MARKER):
                __attr_checked = None
            else:
                if __attr_checked:
                    __attr_checked = 'checked'
                else:
                    __attr_checked = None
            if (__attr_checked is not None):
                __append((' checked="%s"' % __attr_checked))
            __append(' />\n                        ')

            # <Static value=<ast.Dict object at 0x11719ddb0> name=None at 11719de10> -> __attrs_4682537936
            __attrs_4682537936 = _static_4682538416

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="readNetwork">')
            __stream_4682531120 = []
            __append_4682531120 = __stream_4682531120.append
            __append_4682531120('Read network')
            __msgid_4682531120 = __re_whitespace(''.join(__stream_4682531120)).strip()
            if 'label_read_network':
                __append(translate('label_read_network', mapping=None, default=__msgid_4682531120, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n                        ')

            # <Static value=<ast.Dict object at 0x11719e1d0> name=None at 11719cb50> -> __attrs_4682531696
            __attrs_4682531696 = _static_4682539472

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="formHelp">')
            __stream_4682539136 = []
            __append_4682539136 = __stream_4682539136.append
            __append_4682539136('\n                            Allow rules and themes to be read from remote servers.\n                        ')
            __msgid_4682539136 = __re_whitespace(''.join(__stream_4682539136)).strip()
            if 'help_read_network':
                __append(translate('help_read_network', mapping=None, default=__msgid_4682539136, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n                    </div>')
            if (__backup_selected_4683079808 is __marker):
                del econtext['selected']
            else:
                econtext['selected'] = __backup_selected_4683079808
            __append('\n\n                    ')

            # <Static value=<ast.Dict object at 0x11719e380> name=None at 11719fb80> -> __attrs_4682535584
            __attrs_4682535584 = _static_4682539904
            __backup_error_4682852544 = get('error', __marker)

            # <Value 'errors/hostnameBlacklist | nothing' (368:42)> -> __value
            __token = 17141
            try:
                __zt_tmp = __attrs_4682535584
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'errors/hostnameBlacklist | nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['error'] = __value
            __backup_hostnameBlacklist_4682849712 = get('hostnameBlacklist', __marker)

            # <Value 'view/theme_settings/hostnameBlacklist | python:[]' (369:53)> -> __value
            __token = 17230
            try:
                __zt_tmp = __attrs_4682535584
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'view/theme_settings/hostnameBlacklist | python:[]', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['hostnameBlacklist'] = __value
            __backup_hostnameBlacklist_4680470144 = get('hostnameBlacklist', __marker)

            # <Value 'python: view.hostname_blacklist or hostnameBlacklist' (370:52)> -> __value
            __token = 17334
            try:
                __zt_tmp = __attrs_4682535584
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', ' view.hostname_blacklist or hostnameBlacklist', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['hostnameBlacklist'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682545856
            __default_4682545856 = _DEFAULT_MARKER

            # <Substitution "python:'field error' if error else 'field'" (371:46)> -> __attr_class
            __token = 17436
            try:
                __zt_tmp = __attrs_4682535584
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4427992992('python', "'field error' if error else 'field'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))
            __append('>\n\n                        ')

            # <Static value=<ast.Dict object at 0x116fba9e0> name=None at 116fb8220> -> __attrs_4680564496
            __attrs_4680564496 = _static_4680559072

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="hostnameBlacklist">')
            __stream_4680559744 = []
            __append_4680559744 = __stream_4680559744.append
            __append_4680559744('Unthemed host names')
            __msgid_4680559744 = __re_whitespace(''.join(__stream_4680559744)).strip()
            if 'label_hostname_blacklist':
                __append(translate('label_hostname_blacklist', mapping=None, default=__msgid_4680559744, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n                        ')

            # <Static value=<ast.Dict object at 0x116fba740> name=None at 116fbb010> -> __attrs_4680554992
            __attrs_4680554992 = _static_4680558400

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="formHelp">')
            __stream_4680553408 = []
            __append_4680553408 = __stream_4680553408.append
            __append_4680553408("\n                            If there are hostnames that you do not want to be\n                            themed, you can list them here, one per line. This is\n                            useful during theme development, so that you can\n                            compare the themed and unthemed sites. In some cases,\n                            you may also want to provided an unthemed host alias\n                            for content administrators to be able to use 'plain'\n                            Plone.\n                        ")
            __msgid_4680553408 = __re_whitespace(''.join(__stream_4680553408)).strip()
            if 'help_hostname_blacklist':
                __append(translate('help_hostname_blacklist', mapping=None, default=__msgid_4680553408, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n                        ')

            # <Static value=<ast.Dict object at 0x116fbada0> name=None at 116fb8160> -> __attrs_4680555424
            __attrs_4680555424 = _static_4680560032

            # <Value 'error' (384:85)> -> __condition
            __token = 18328
            try:
                __zt_tmp = __attrs_4680555424
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="errorMessage">')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680550480
                __default_4680550480 = _DEFAULT_MARKER

                # <Value 'error' (384:63)> -> __cache_4680552880
                __token = 18306
                try:
                    __zt_tmp = __attrs_4680555424
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4680552880 = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'error' (384:63)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116fbb310> -> __condition
                __expression = __cache_4680552880

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4680552880
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</div>')
            __append('\n\n                        ')

            # <Static value=<ast.Dict object at 0x116fb8b50> name=None at 116fb9e70> -> __attrs_4680561328
            __attrs_4680561328 = _static_4680551248

            # <textarea ... (0:0)
            # --------------------------------------------------------
            __append('<textarea name="hostnameBlacklist:lines" id="hostnameBlacklist" rows="5" cols="50" >')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680553792
            __default_4680553792 = _DEFAULT_MARKER

            # <Value "python: '\\n'.join(hostnameBlacklist)" (391:41)> -> __cache_4680553936
            __token = 18599
            try:
                __zt_tmp = __attrs_4680561328
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4680553936 = _static_4427992992('python', " '\\n'.join(hostnameBlacklist)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value "python: '\\n'.join(hostnameBlacklist)" (391:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116fb96c0> -> __condition
            __expression = __cache_4680553936

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4680553936
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</textarea>\n\n                    </div>')
            if (__backup_hostnameBlacklist_4680470144 is __marker):
                del econtext['hostnameBlacklist']
            else:
                econtext['hostnameBlacklist'] = __backup_hostnameBlacklist_4680470144
            if (__backup_hostnameBlacklist_4682849712 is __marker):
                del econtext['hostnameBlacklist']
            else:
                econtext['hostnameBlacklist'] = __backup_hostnameBlacklist_4682849712
            if (__backup_error_4682852544 is __marker):
                del econtext['error']
            else:
                econtext['error'] = __backup_error_4682852544
            __append('\n\n                    ')

            # <Static value=<ast.Dict object at 0x116fbb070> name=None at 116fbb100> -> __attrs_4680556768
            __attrs_4680556768 = _static_4680560752
            __backup_error_4680472400 = get('error', __marker)

            # <Value 'errors/parameterExpressions | nothing' (397:42)> -> __value
            __token = 18774
            try:
                __zt_tmp = __attrs_4680556768
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'errors/parameterExpressions | nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['error'] = __value
            __backup_parameterExpressions_4682856528 = get('parameterExpressions', __marker)

            # <Value 'python:view.theme_settings.parameterExpressions or {}' (398:56)> -> __value
            __token = 18869
            try:
                __zt_tmp = __attrs_4680556768
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', 'view.theme_settings.parameterExpressions or {}', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['parameterExpressions'] = __value
            __backup_parameterExpressions_4680468704 = get('parameterExpressions', __marker)

            # <Value "python:['%s = %s' % (k,v) for k,v in parameterExpressions.items()]" (399:55)> -> __value
            __token = 18980
            try:
                __zt_tmp = __attrs_4680556768
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', "['%s = %s' % (k,v) for k,v in parameterExpressions.items()]", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['parameterExpressions'] = __value
            __backup_parameterExpressions_4682856576 = get('parameterExpressions', __marker)

            # <Value "python:request.get('parameterExpressions', parameterExpressions)" (400:54)> -> __value
            __token = 19104
            try:
                __zt_tmp = __attrs_4680556768
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', "request.get('parameterExpressions', parameterExpressions)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['parameterExpressions'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680552256
            __default_4680552256 = _DEFAULT_MARKER

            # <Substitution "python:'field error' if error else 'field'" (401:46)> -> __attr_class
            __token = 19219
            try:
                __zt_tmp = __attrs_4680556768
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4427992992('python', "'field error' if error else 'field'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))
            __append('>\n\n                        ')

            # <Static value=<ast.Dict object at 0x116fb95a0> name=None at 116fb9570> -> __attrs_4680550192
            __attrs_4680550192 = _static_4680553888

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="parameterExpressions">')
            __stream_4680549280 = []
            __append_4680549280 = __stream_4680549280.append
            __append_4680549280('Parameter expressions')
            __msgid_4680549280 = __re_whitespace(''.join(__stream_4680549280)).strip()
            if 'label_parameter_expressions':
                __append(translate('label_parameter_expressions', mapping=None, default=__msgid_4680549280, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n                        ')

            # <Static value=<ast.Dict object at 0x116fba350> name=None at 116fba620> -> __attrs_4680557968
            __attrs_4680557968 = _static_4680557392

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="formHelp">')
            __stream_4680551968 = []
            __append_4680551968 = __stream_4680551968.append
            __append_4680551968('\n                            You can define parameters that will be passed\n                            to the compiled theme here. In your rules file, you can\n                            refer to a parameter by ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680552496
            __attrs_4680552496 = _static_4428767312

            # <code ... (0:0)
            # --------------------------------------------------------
            __append_4680551968('<code>$name</code>. Parameters\n                            are defined using TALES expressions, which should\n                            evaluate to a string, a number, a boolean or None.\n                            Available variables are ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680556096
            __attrs_4680556096 = _static_4428767312

            # <code ... (0:0)
            # --------------------------------------------------------
            __append_4680551968('<code>context</code>,\n                            ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680562000
            __attrs_4680562000 = _static_4428767312

            # <code ... (0:0)
            # --------------------------------------------------------
            __append_4680551968('<code>request</code>, ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4672562720
            __attrs_4672562720 = _static_4428767312

            # <code ... (0:0)
            # --------------------------------------------------------
            __append_4680551968('<code>portal</code>,\n                            ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4672554320
            __attrs_4672554320 = _static_4428767312

            # <code ... (0:0)
            # --------------------------------------------------------
            __append_4680551968('<code>portal_state</code>, and\n                            ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682987168
            __attrs_4682987168 = _static_4428767312

            # <code ... (0:0)
            # --------------------------------------------------------
            __append_4680551968('<code>context_state</code>. Define one variable\n                            per line, in the format ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682981840
            __attrs_4682981840 = _static_4428767312

            # <code ... (0:0)
            # --------------------------------------------------------
            __append_4680551968('<code>name = expression</code>.\n                        ')
            __msgid_4680551968 = __re_whitespace(''.join(__stream_4680551968)).strip()
            if 'help_parameter_expressions':
                __append(translate('help_parameter_expressions', mapping=None, default=__msgid_4680551968, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n                        ')

            # <Static value=<ast.Dict object at 0x11720a860> name=None at 11720b6d0> -> __attrs_4682977664
            __attrs_4682977664 = _static_4682983520

            # <Value 'error' (417:85)> -> __condition
            __token = 20368
            try:
                __zt_tmp = __attrs_4682977664
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="errorMessage">')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682978240
                __default_4682978240 = _DEFAULT_MARKER

                # <Value 'error' (417:63)> -> __cache_4682984432
                __token = 20346
                try:
                    __zt_tmp = __attrs_4682977664
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4682984432 = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'error' (417:63)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 117208550> -> __condition
                __expression = __cache_4682984432

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4682984432
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</div>')
            __append('\n\n                        ')

            # <Static value=<ast.Dict object at 0x117208040> name=None at 1172095d0> -> __attrs_4682977808
            __attrs_4682977808 = _static_4682973248

            # <textarea ... (0:0)
            # --------------------------------------------------------
            __append('<textarea name="parameterExpressions:lines" id="parameterExpressions" rows="8" cols="50" >')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682976272
            __default_4682976272 = _DEFAULT_MARKER

            # <Value "python:'\\n'.join(parameterExpressions)" (424:41)> -> __cache_4682979728
            __token = 20645
            try:
                __zt_tmp = __attrs_4682977808
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4682979728 = _static_4427992992('python', "'\\n'.join(parameterExpressions)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value "python:'\\n'.join(parameterExpressions)" (424:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1172099c0> -> __condition
            __expression = __cache_4682979728

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4682979728
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</textarea>\n                    </div>')
            if (__backup_parameterExpressions_4682856576 is __marker):
                del econtext['parameterExpressions']
            else:
                econtext['parameterExpressions'] = __backup_parameterExpressions_4682856576
            if (__backup_parameterExpressions_4680468704 is __marker):
                del econtext['parameterExpressions']
            else:
                econtext['parameterExpressions'] = __backup_parameterExpressions_4680468704
            if (__backup_parameterExpressions_4682856528 is __marker):
                del econtext['parameterExpressions']
            else:
                econtext['parameterExpressions'] = __backup_parameterExpressions_4682856528
            if (__backup_error_4680472400 is __marker):
                del econtext['error']
            else:
                econtext['error'] = __backup_error_4680472400
            __append('\n\n                </fieldset>\n                ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682983664
            __attrs_4682983664 = _static_4428767312

            # <fieldset ... (0:0)
            # --------------------------------------------------------
            __append('<fieldset>\n                    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682983712
            __attrs_4682983712 = _static_4428767312

            # <legend ... (0:0)
            # --------------------------------------------------------
            __append('<legend>')
            __stream_4682974640 = []
            __append_4682974640 = __stream_4682974640.append
            __append_4682974640('Theme base')
            __msgid_4682974640 = __re_whitespace(''.join(__stream_4682974640)).strip()
            if __msgid_4682974640:
                __append(translate(__msgid_4682974640, mapping=None, default=__msgid_4682974640, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</legend>\n\n                    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682986112
            __attrs_4682986112 = _static_4428767312

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')
            __stream_4682980736 = []
            __append_4682980736 = __stream_4682980736.append
            __append_4682980736('\n                       The settings below control the presentation of the\n                       ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4682984624
            __attrs_4682984624 = _static_4428767312

            # <em ... (0:0)
            # --------------------------------------------------------
            __append_4682980736('<em>content</em> produced by Plone before a Diazo theme\n                       is applied. Note that these settings will have an effect\n                       even if no Diazo theme is currently enabled.\n                    ')
            __msgid_4682980736 = __re_whitespace(''.join(__stream_4682980736)).strip()
            if 'description_advanced_base':
                __append(translate('description_advanced_base', mapping=None, default=__msgid_4682980736, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n\n                    ')

            # <Static value=<ast.Dict object at 0x117209390> name=None at 11720ae00> -> __attrs_4682974832
            __attrs_4682974832 = _static_4682978192
            __backup_selected_4682851824 = get('selected', __marker)

            # <Value "python:request.get('themeBase', view.pskin.getDefaultSkin())" (441:45)> -> __value
            __token = 21378
            try:
                __zt_tmp = __attrs_4682974832
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', "request.get('themeBase', view.pskin.getDefaultSkin())", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['selected'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="field">\n\n                        ')

            # <Static value=<ast.Dict object at 0x11720bfa0> name=None at 117208b20> -> __attrs_4682982992
            __attrs_4682982992 = _static_4682989472

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="themeBase">')
            __stream_4682977088 = []
            __append_4682977088 = __stream_4682977088.append
            __append_4682977088('Theme base')
            __msgid_4682977088 = __re_whitespace(''.join(__stream_4682977088)).strip()
            if 'label_theme_base':
                __append(translate('label_theme_base', mapping=None, default=__msgid_4682977088, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n\n                        ')

            # <Static value=<ast.Dict object at 0x11720a3e0> name=None at 117208610> -> __attrs_4681930144
            __attrs_4681930144 = _static_4682982368

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="formHelp">')
            __stream_4682980304 = []
            __append_4682980304 = __stream_4682980304.append
            __append_4682980304('\n                            The theme base defines a collection of templates and other\n                            resources that makes up the raw content to which a theme is\n                            applied. Most Diazo themes will assume the default theme base,\n                            so only change this if you know what you are doing.\n                        ')
            __msgid_4682980304 = __re_whitespace(''.join(__stream_4682980304)).strip()
            if 'help_theme_base':
                __append(translate('help_theme_base', mapping=None, default=__msgid_4682980304, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n                        ')

            # <Static value=<ast.Dict object at 0x117109a50> name=None at 1171099c0> -> __attrs_4681926496
            __attrs_4681926496 = _static_4681931344

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select size="1" name="themeBase" id="themeBase">\n                            ')

            # <Static value=<ast.Dict object at 0x11710b280> name=None at 116d91780> -> __attrs_4681940320
            __attrs_4681940320 = _static_4681937536
            __backup_skin_4683076640 = get('skin', __marker)

            # <Value 'view/skinsVocabulary' (454:49)> -> __iterator
            __token = 22160
            try:
                __zt_tmp = __attrs_4681940320
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4427992992('path', 'view/skinsVocabulary', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            (__iterator, ____index_4681938208, ) = getname('repeat')('skin', __iterator)
            econtext['skin'] = None
            for __item in __iterator:
                econtext['skin'] = __item

                # <option ... (0:0)
                # --------------------------------------------------------
                __append('<option')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4681935568
                __default_4681935568 = _DEFAULT_MARKER

                # <Substitution 'skin/value' (455:54)> -> __attr_value
                __token = 22236
                try:
                    __zt_tmp = __attrs_4681940320
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4427992992('path', 'skin/value', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4681932160
                __default_4681932160 = _DEFAULT_MARKER

                # <Boolean "python:skin.value == selected and 'selected' or None" (456:56)> -> __attr_selected
                __token = 22304
                try:
                    __zt_tmp = __attrs_4681940320
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_selected = _static_4427992992('python', "skin.value == selected and 'selected' or None", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
                if (__attr_selected is _DEFAULT_MARKER):
                    __attr_selected = None
                else:
                    if __attr_selected:
                        __attr_selected = 'selected'
                    else:
                        __attr_selected = None
                if (__attr_selected is not None):
                    __append((' selected="%s"' % __attr_selected))
                __append('>')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4681938448
                __default_4681938448 = _DEFAULT_MARKER

                # <Value 'skin/title' (457:45)> -> __cache_4681935136
                __token = 22404
                try:
                    __zt_tmp = __attrs_4681940320
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4681935136 = _static_4427992992('path', 'skin/title', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'skin/title' (457:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 117109480> -> __condition
                __expression = __cache_4681935136

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4681935136
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</option>')
                ____index_4681938208 -= 1
                if (____index_4681938208 > 0):
                    __append('\n                            ')
            if (__backup_skin_4683076640 is __marker):
                del econtext['skin']
            else:
                econtext['skin'] = __backup_skin_4683076640
            __append('\n                        </select>\n\n                    </div>')
            if (__backup_selected_4682851824 is __marker):
                del econtext['selected']
            else:
                econtext['selected'] = __backup_selected_4682851824
            __append('\n\n                    ')

            # <Static value=<ast.Dict object at 0x11710ba60> name=None at 11710b3a0> -> __attrs_4681927600
            __attrs_4681927600 = _static_4681939552
            __backup_selected_4682806416 = get('selected', __marker)

            # <Value "python:request.get('markSpecialLinks', view.mark_special_links)" (465:45)> -> __value
            __token = 22622
            try:
                __zt_tmp = __attrs_4681927600
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', "request.get('markSpecialLinks', view.mark_special_links)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['selected'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="field">\n\n                        ')

            # <Static value=<ast.Dict object at 0x11710b940> name=None at 11710bc10> -> __attrs_4681936624
            __attrs_4681936624 = _static_4681939264

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" value="" name="markSpecialLinks:boolean:default" />\n                        ')

            # <Static value=<ast.Dict object at 0x11710b490> name=None at 11710b640> -> __attrs_4681938736
            __attrs_4681938736 = _static_4681938064

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="checkbox" value="1" name="markSpecialLinks:boolean" id="markSpecialLinks"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4681931872
            __default_4681931872 = _DEFAULT_MARKER

            # <Boolean "python:'markSpecialLinks' if selected else None" (469:52)> -> __attr_checked
            __token = 22949
            try:
                __zt_tmp = __attrs_4681938736
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_checked = _static_4427992992('python', "'markSpecialLinks' if selected else None", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if (__attr_checked is _DEFAULT_MARKER):
                __attr_checked = None
            else:
                if __attr_checked:
                    __attr_checked = 'checked'
                else:
                    __attr_checked = None
            if (__attr_checked is not None):
                __append((' checked="%s"' % __attr_checked))
            __append(' />\n                        ')

            # <Static value=<ast.Dict object at 0x117109840> name=None at 11710a5c0> -> __attrs_4681927744
            __attrs_4681927744 = _static_4681930816

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="markSpecialLinks">')
            __stream_4681934416 = []
            __append_4681934416 = __stream_4681934416.append
            __append_4681934416('Mark special links')
            __msgid_4681934416 = __re_whitespace(''.join(__stream_4681934416)).strip()
            if 'label_mark_special_links':
                __append(translate('label_mark_special_links', mapping=None, default=__msgid_4681934416, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n                        ')

            # <Static value=<ast.Dict object at 0x117108460> name=None at 11710a6e0> -> __attrs_4681924864
            __attrs_4681924864 = _static_4681925728

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="formHelp">')
            __stream_4681927360 = []
            __append_4681927360 = __stream_4681927360.append
            __append_4681927360('\n                            If enabled all external links will be marked with link type specific icons.\n                        ')
            __msgid_4681927360 = __re_whitespace(''.join(__stream_4681927360)).strip()
            if 'help_mark_special_links':
                __append(translate('help_mark_special_links', mapping=None, default=__msgid_4681927360, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n                    </div>')
            if (__backup_selected_4682806416 is __marker):
                del econtext['selected']
            else:
                econtext['selected'] = __backup_selected_4682806416
            __append('\n\n                    ')

            # <Static value=<ast.Dict object at 0x117109b70> name=None at 1171094e0> -> __attrs_4681925872
            __attrs_4681925872 = _static_4681931632
            __backup_selected_4682806704 = get('selected', __marker)

            # <Value "python:request.get('extLinksOpenInNewWindow', view.ext_links_open_new_window)" (480:45)> -> __value
            __token = 23512
            try:
                __zt_tmp = __attrs_4681925872
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', "request.get('extLinksOpenInNewWindow', view.ext_links_open_new_window)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['selected'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="field">\n\n                        ')

            # <Static value=<ast.Dict object at 0x11710a980> name=None at 117108d30> -> __attrs_4681949792
            __attrs_4681949792 = _static_4681935232

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" value="" name="extLinksOpenInNewWindow:boolean:default" />\n                        ')

            # <Static value=<ast.Dict object at 0x11710f5e0> name=None at 11710c5e0> -> __attrs_4681949072
            __attrs_4681949072 = _static_4681954784

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="checkbox" value="1" name="extLinksOpenInNewWindow:boolean" id="extLinksOpenInNewWindow"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4681941680
            __default_4681941680 = _DEFAULT_MARKER

            # <Boolean "python:'extLinksOpenInNewWindow' if selected else None" (484:52)> -> __attr_checked
            __token = 23874
            try:
                __zt_tmp = __attrs_4681949072
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_checked = _static_4427992992('python', "'extLinksOpenInNewWindow' if selected else None", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if (__attr_checked is _DEFAULT_MARKER):
                __attr_checked = None
            else:
                if __attr_checked:
                    __attr_checked = 'checked'
                else:
                    __attr_checked = None
            if (__attr_checked is not None):
                __append((' checked="%s"' % __attr_checked))
            __append(' />\n                        ')

            # <Static value=<ast.Dict object at 0x11710f790> name=None at 11710ebf0> -> __attrs_4681943888
            __attrs_4681943888 = _static_4681955216

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="extLinksOpenInNewWindow">')
            __stream_4681954304 = []
            __append_4681954304 = __stream_4681954304.append
            __append_4681954304('External links open in new window')
            __msgid_4681954304 = __re_whitespace(''.join(__stream_4681954304)).strip()
            if 'label_ext_links_open_new_window':
                __append(translate('label_ext_links_open_new_window', mapping=None, default=__msgid_4681954304, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n                        ')

            # <Static value=<ast.Dict object at 0x11710cfd0> name=None at 11710ce20> -> __attrs_4681941392
            __attrs_4681941392 = _static_4681945040

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="formHelp">')
            __stream_4681949648 = []
            __append_4681949648 = __stream_4681949648.append
            __append_4681949648('\n                            If enabled all external links in the content region open in a new window.\n                        ')
            __msgid_4681949648 = __re_whitespace(''.join(__stream_4681949648)).strip()
            if 'help_ext_links_open_new_window':
                __append(translate('help_ext_links_open_new_window', mapping=None, default=__msgid_4681949648, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n                    </div>')
            if (__backup_selected_4682806704 is __marker):
                del econtext['selected']
            else:
                econtext['selected'] = __backup_selected_4682806704
            __append('\n\n                </fieldset>\n                ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4681949312
            __attrs_4681949312 = _static_4428767312

            # <fieldset ... (0:0)
            # --------------------------------------------------------
            __append('<fieldset>\n                    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4681948256
            __attrs_4681948256 = _static_4428767312

            # <legend ... (0:0)
            # --------------------------------------------------------
            __append('<legend>')
            __stream_4681955840 = []
            __append_4681955840 = __stream_4681955840.append
            __append_4681955840('Custom Styles')
            __msgid_4681955840 = __re_whitespace(''.join(__stream_4681955840)).strip()
            if __msgid_4681955840:
                __append(translate(__msgid_4681955840, mapping=None, default=__msgid_4681955840, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</legend>\n\n                    ')

            # <Static value=<ast.Dict object at 0x11710efb0> name=None at 11710fa60> -> __attrs_4681943456
            __attrs_4681943456 = _static_4681953200
            __backup_error_4682806272 = get('error', __marker)

            # <Value 'errors/custom_css | nothing' (498:42)> -> __value
            __token = 24562
            try:
                __zt_tmp = __attrs_4681943456
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'errors/custom_css | nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['error'] = __value
            __backup_custom_css_4683084464 = get('custom_css', __marker)

            # <Value "view/theme_settings/custom_css | python: ''" (499:46)> -> __value
            __token = 24637
            try:
                __zt_tmp = __attrs_4681943456
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', "view/theme_settings/custom_css | python: ''", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['custom_css'] = __value
            __backup_custom_css_4683087824 = get('custom_css', __marker)

            # <Value "python:request.get('custom_css', custom_css)" (500:45)> -> __value
            __token = 24728
            try:
                __zt_tmp = __attrs_4681943456
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', "request.get('custom_css', custom_css)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['custom_css'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4681954640
            __default_4681954640 = _DEFAULT_MARKER

            # <Substitution "python:'field error' if error else 'field'" (501:46)> -> __attr_class
            __token = 24822
            try:
                __zt_tmp = __attrs_4681943456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4427992992('python', "'field error' if error else 'field'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))
            __append('>\n\n                        ')

            # <Static value=<ast.Dict object at 0x11710dba0> name=None at 11710cc10> -> __attrs_4681951952
            __attrs_4681951952 = _static_4681948064

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="custom_css">')
            __stream_4681950896 = []
            __append_4681950896 = __stream_4681950896.append
            __append_4681950896('Custom CSS')
            __msgid_4681950896 = __re_whitespace(''.join(__stream_4681950896)).strip()
            if 'label_custom_css':
                __append(translate('label_custom_css', mapping=None, default=__msgid_4681950896, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n                        ')

            # <Static value=<ast.Dict object at 0x11710efe0> name=None at 11710ebc0> -> __attrs_4681944944
            __attrs_4681944944 = _static_4681953248

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="formHelp">')
            __stream_4681957328 = []
            __append_4681957328 = __stream_4681957328.append
            __append_4681957328('\n                            Define your own custom CSS in the field below. This is a good place for quick customizations of things like colors and the toolbar. Definitions here will override previously defined CSS of Plone. Please use this only for small customizations, as it is hard to keep track of changes here. For bigger changes you most likely want to customize a full theme and make your changes there.\n                        ')
            __msgid_4681957328 = __re_whitespace(''.join(__stream_4681957328)).strip()
            if 'help_custom_css':
                __append(translate('help_custom_css', mapping=None, default=__msgid_4681957328, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n                        ')

            # <Static value=<ast.Dict object at 0x11710f820> name=None at 11710fb50> -> __attrs_4681954016
            __attrs_4681954016 = _static_4681955360

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="theming_doc_link">\n                            ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4681956464
            __attrs_4681956464 = _static_4428767312

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')

            # <Static value=<ast.Dict object at 0x11710e0e0> name=None at 11710dff0> -> __attrs_4680507760
            __attrs_4680507760 = _static_4681949408

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a href="https://docs.plone.org/adapt-and-extend/theming" target="_blank">')
            __stream_4681943600 = []
            __append_4681943600 = __stream_4681943600.append
            __append_4681943600('Theming documentation')
            __msgid_4681943600 = __re_whitespace(''.join(__stream_4681943600)).strip()
            if 'label_theming_doc_link':
                __append(translate('label_theming_doc_link', mapping=None, default=__msgid_4681943600, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a></p>\n                        </div>\n\n                        ')

            # <Static value=<ast.Dict object at 0x116faf6a0> name=None at 116fafb80> -> __attrs_4680501616
            __attrs_4680501616 = _static_4680513184

            # <Value 'error' (511:85)> -> __condition
            __token = 25838
            try:
                __zt_tmp = __attrs_4680501616
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="errorMessage">')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680511744
                __default_4680511744 = _DEFAULT_MARKER

                # <Value 'error' (511:63)> -> __cache_4681952576
                __token = 25816
                try:
                    __zt_tmp = __attrs_4680501616
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4681952576 = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'error' (511:63)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116fae110> -> __condition
                __expression = __cache_4681952576

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4681952576
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</div>')
            __append('\n\n                        ')

            # <Static value=<ast.Dict object at 0x116fad900> name=None at 116fad4b0> -> __attrs_4680501760
            __attrs_4680501760 = _static_4680505600

            # <textarea ... (0:0)
            # --------------------------------------------------------
            __append('<textarea name="custom_css" id="custom_css" rows="40" cols="160"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680515488
            __default_4680515488 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x116fafa00> at 116fac550> -> __attr_placeholder
            __attr_placeholder = 'Put your plain css...'
            __attr_placeholder = translate(__attr_placeholder, default=__attr_placeholder, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_placeholder is not None):
                __append((' placeholder="%s"' % __attr_placeholder))
            __append(' class="pat-code-editor" data-pat-code-editor="language: css; theme: tomorrow" >')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680501328
            __default_4680501328 = _DEFAULT_MARKER

            # <Value 'custom_css' (520:41)> -> __cache_4680505696
            __token = 26213
            try:
                __zt_tmp = __attrs_4680501760
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4680505696 = _static_4427992992('path', 'custom_css', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'custom_css' (520:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116fac6a0> -> __condition
            __expression = __cache_4680505696

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4680505696
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</textarea>\n\n                    </div>')
            if (__backup_custom_css_4683087824 is __marker):
                del econtext['custom_css']
            else:
                econtext['custom_css'] = __backup_custom_css_4683087824
            if (__backup_custom_css_4683084464 is __marker):
                del econtext['custom_css']
            else:
                econtext['custom_css'] = __backup_custom_css_4683084464
            if (__backup_error_4682806272 is __marker):
                del econtext['error']
            else:
                econtext['error'] = __backup_error_4682806272
            __append('\n                </fieldset>\n            </div>\n\n\n            ')

            # <Static value=<ast.Dict object at 0x11710cc70> name=None at 11710c910> -> __attrs_4680502576
            __attrs_4680502576 = _static_4681944176

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="btn-group">\n                ')

            # <Static value=<ast.Dict object at 0x116fae5f0> name=None at 116faceb0> -> __attrs_4680502240
            __attrs_4680502240 = _static_4680508912

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="submit" name="form.button.AdvancedSave" class="btn btn-success save"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680513904
            __default_4680513904 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x116faf760> at 116faf1c0> -> __attr_value
            __attr_value = 'Save'
            __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' />\n\n                ')

            # <Static value=<ast.Dict object at 0x116faf820> name=None at 116fac9d0> -> __attrs_4677996880
            __attrs_4677996880 = _static_4680513568

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="submit" name="form.button.Cancel" class="btn btn-primary cancel"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680505648
            __default_4680505648 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x116fad420> at 116fafc10> -> __attr_value
            __attr_value = 'Cancel'
            __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' />\n            </div>\n\n            ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4678008064
            __attrs_4678008064 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678004032
            __default_4678004032 = _DEFAULT_MARKER

            # <Value 'context/@@authenticator/authenticator' (546:42)> -> __cache_4678008256
            __token = 27050
            try:
                __zt_tmp = __attrs_4678008064
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4678008256 = _static_4427992992('path', 'context/@@authenticator/authenticator', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/@@authenticator/authenticator' (546:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116d4bfa0> -> __condition
            __expression = __cache_4678008256

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input />')
            else:
                __content = __cache_4678008256
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n\n\n        </form>')
            if (__backup_errors_4683050880 is __marker):
                del econtext['errors']
            else:
                econtext['errors'] = __backup_errors_4683050880
            __append('\n\n    </section>\n\n</div>\n\n<!-- Upload overlay -->\n')

            # <Static value=<ast.Dict object at 0x116d4be20> name=None at 116d4a050> -> __attrs_4677998560
            __attrs_4677998560 = _static_4678008352

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="overlay-upload" class="modal">\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4678008304
            __attrs_4678008304 = _static_4428767312

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div>\n        ')

            # <Static value=<ast.Dict object at 0x116d4a560> name=None at 116d483a0> -> __attrs_4677995296
            __attrs_4677995296 = _static_4678002016

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1 class="documentFirstHeading">')
            __stream_4678003216 = []
            __append_4678003216 = __stream_4678003216.append
            __append_4678003216('Upload theme')
            __msgid_4678003216 = __re_whitespace(''.join(__stream_4678003216)).strip()
            if 'theming_controlpanel_upload':
                __append(translate('theming_controlpanel_upload', mapping=None, default=__msgid_4678003216, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h1>\n\n        ')

            # <Static value=<ast.Dict object at 0x116d48d60> name=None at 116d49e70> -> __attrs_4677999904
            __attrs_4677999904 = _static_4677995872

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="documentDescription">')
            __stream_4677992992 = []
            __append_4677992992 = __stream_4677992992.append
            __append_4677992992('\n           You can import a Zip file containing an existing theme.\n           This should contain a single top level directory, which will be used as\n           the theme identifier. If no Diazo ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4683176336
            __attrs_4683176336 = _static_4428767312

            # <code ... (0:0)
            # --------------------------------------------------------
            __append_4677992992('<code>rules.xml</code> or\n           ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4683171824
            __attrs_4683171824 = _static_4428767312

            # <code ... (0:0)
            # --------------------------------------------------------
            __append_4677992992('<code>manifest.cfg</code> file is found in this directory, a\n           default ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4683172688
            __attrs_4683172688 = _static_4428767312

            # <code ... (0:0)
            # --------------------------------------------------------
            __append_4677992992('<code>rules.xml</code> file will be created.\n        ')
            __msgid_4677992992 = __re_whitespace(''.join(__stream_4677992992)).strip()
            if 'description_import':
                __append(translate('description_import', mapping=None, default=__msgid_4677992992, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n\n        ')

            # <Static value=<ast.Dict object at 0x117238760> name=None at 1172389d0> -> __attrs_4683185456
            __attrs_4683185456 = _static_4683171680
            __backup_errors_4683043152 = get('errors', __marker)

            # <Value 'view/errors' (575:31)> -> __value
            __token = 27989
            try:
                __zt_tmp = __attrs_4683185456
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'view/errors', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['errors'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form name="import" method="post" enctype="multipart/form-data" class="pat-formunloadalert"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4683171584
            __default_4683171584 = _DEFAULT_MARKER

            # <Substitution 'request/URL' (574:35)> -> __attr_action
            __token = 27945
            try:
                __zt_tmp = __attrs_4683185456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_4427992992('path', 'request/URL', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append('>\n\n            ')

            # <Static value=<ast.Dict object at 0x117239690> name=None at 11723bf10> -> __attrs_4683176240
            __attrs_4683176240 = _static_4683175568
            __backup_error_4683084368 = get('error', __marker)

            # <Value 'errors/themeArchive | nothing' (579:34)> -> __value
            __token = 28085
            try:
                __zt_tmp = __attrs_4683176240
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'errors/themeArchive | nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['error'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4683173936
            __default_4683173936 = _DEFAULT_MARKER

            # <Substitution "python:'field error' if error else 'field'" (580:38)> -> __attr_class
            __token = 28154
            try:
                __zt_tmp = __attrs_4683176240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4427992992('python', "'field error' if error else 'field'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', 'field', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))
            __append('>\n\n                ')

            # <Static value=<ast.Dict object at 0x11723baf0> name=None at 11723a470> -> __attrs_4683176000
            __attrs_4683176000 = _static_4683184880

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="formHelp">')
            __stream_4683170000 = []
            __append_4683170000 = __stream_4683170000.append
            __append_4683170000('\n                    Select a file to upload.\n                ')
            __msgid_4683170000 = __re_whitespace(''.join(__stream_4683170000)).strip()
            if 'help_theme_archive':
                __append(translate('help_theme_archive', mapping=None, default=__msgid_4683170000, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n                ')

            # <Static value=<ast.Dict object at 0x117238850> name=None at 11723b7c0> -> __attrs_4683180512
            __attrs_4683180512 = _static_4683171920

            # <Value 'error' (586:77)> -> __condition
            __token = 28421
            try:
                __zt_tmp = __attrs_4683180512
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="errorMessage">')

                # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4683180320
                __default_4683180320 = _DEFAULT_MARKER

                # <Value 'error' (586:55)> -> __cache_4683180080
                __token = 28399
                try:
                    __zt_tmp = __attrs_4683180512
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4683180080 = _static_4427992992('path', 'error', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

                # <BinOp left=<Value 'error' (586:55)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 11723b310> -> __condition
                __expression = __cache_4683180080

                # <Symbol value=<DEFAULT> at 107f9a410> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4683180080
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</div>')
            __append('\n\n                ')

            # <Static value=<ast.Dict object at 0x117238e20> name=None at 117239bd0> -> __attrs_4683182672
            __attrs_4683182672 = _static_4683173408

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="file" name="themeArchive" id="themeArchive" />\n\n            </div>')
            if (__backup_error_4683084368 is __marker):
                del econtext['error']
            else:
                econtext['error'] = __backup_error_4683084368
            __append('\n\n            ')

            # <Static value=<ast.Dict object at 0x11723b0d0> name=None at 117238c70> -> __attrs_4683178256
            __attrs_4683178256 = _static_4683182288
            __backup_selected_4683072224 = get('selected', __marker)

            # <Value "python:request.get('enableNewTheme', False)" (598:37)> -> __value
            __token = 28693
            try:
                __zt_tmp = __attrs_4683178256
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', "request.get('enableNewTheme', False)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['selected'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="field">\n                ')

            # <Static value=<ast.Dict object at 0x1171d9d20> name=None at 1171da860> -> __attrs_4682782160
            __attrs_4682782160 = _static_4682784032

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" value="" name="enableNewTheme:boolean:default" />\n                ')

            # <Static value=<ast.Dict object at 0x1171dbb80> name=None at 1171d81c0> -> __attrs_4682784656
            __attrs_4682784656 = _static_4682791808

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="checkbox" value="1" name="enableNewTheme:boolean" id="enableNewTheme"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682778464
            __default_4682778464 = _DEFAULT_MARKER

            # <Boolean "python:'enableNewTheme' if selected else None" (601:44)> -> __attr_checked
            __token = 28969
            try:
                __zt_tmp = __attrs_4682784656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_checked = _static_4427992992('python', "'enableNewTheme' if selected else None", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if (__attr_checked is _DEFAULT_MARKER):
                __attr_checked = None
            else:
                if __attr_checked:
                    __attr_checked = 'checked'
                else:
                    __attr_checked = None
            if (__attr_checked is not None):
                __append((' checked="%s"' % __attr_checked))
            __append(' />\n                ')

            # <Static value=<ast.Dict object at 0x1171dae90> name=None at 1171d9cc0> -> __attrs_4682788736
            __attrs_4682788736 = _static_4682788496

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="enableNewTheme">')
            __stream_4682790080 = []
            __append_4682790080 = __stream_4682790080.append
            __append_4682790080('Immediately enable new theme')
            __msgid_4682790080 = __re_whitespace(''.join(__stream_4682790080)).strip()
            if 'label_enable_new_theme':
                __append(translate('label_enable_new_theme', mapping=None, default=__msgid_4682790080, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n                ')

            # <Static value=<ast.Dict object at 0x1171db160> name=None at 1171db250> -> __attrs_4682788400
            __attrs_4682788400 = _static_4682789216

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="formHelp">')
            __stream_4682789840 = []
            __append_4682789840 = __stream_4682789840.append
            __append_4682789840('\n                    Select this option to enable the newly uploaded theme\n                    immediately.\n                ')
            __msgid_4682789840 = __re_whitespace(''.join(__stream_4682789840)).strip()
            if 'help_enable_new_theme':
                __append(translate('help_enable_new_theme', mapping=None, default=__msgid_4682789840, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n            </div>')
            if (__backup_selected_4683072224 is __marker):
                del econtext['selected']
            else:
                econtext['selected'] = __backup_selected_4683072224
            __append('\n\n            ')

            # <Static value=<ast.Dict object at 0x1171dbd00> name=None at 1171dbb50> -> __attrs_4682778032
            __attrs_4682778032 = _static_4682792192
            __backup_selected_4683073904 = get('selected', __marker)

            # <Value "python:request.get('replaceExisting', False)" (612:37)> -> __value
            __token = 29472
            try:
                __zt_tmp = __attrs_4682778032
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', "request.get('replaceExisting', False)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['selected'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="field">\n                ')

            # <Static value=<ast.Dict object at 0x1171d8430> name=None at 1171d9cf0> -> __attrs_4682777408
            __attrs_4682777408 = _static_4682777648

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" value="" name="replaceExisting:boolean:default" />\n                ')

            # <Static value=<ast.Dict object at 0x1171d8610> name=None at 1171d87f0> -> __attrs_4682783696
            __attrs_4682783696 = _static_4682778128

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="checkbox" value="1" name="replaceExisting:boolean" id="replaceExisting"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4682790272
            __default_4682790272 = _DEFAULT_MARKER

            # <Boolean "python:'replaceExisting' if selected else None" (615:44)> -> __attr_checked
            __token = 29752
            try:
                __zt_tmp = __attrs_4682783696
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_checked = _static_4427992992('python', "'replaceExisting' if selected else None", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if (__attr_checked is _DEFAULT_MARKER):
                __attr_checked = None
            else:
                if __attr_checked:
                    __attr_checked = 'checked'
                else:
                    __attr_checked = None
            if (__attr_checked is not None):
                __append((' checked="%s"' % __attr_checked))
            __append(' />\n                ')

            # <Static value=<ast.Dict object at 0x1171d96c0> name=None at 1171d9a20> -> __attrs_4682782448
            __attrs_4682782448 = _static_4682782400

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="replaceExisting">')
            __stream_4682776784 = []
            __append_4682776784 = __stream_4682776784.append
            __append_4682776784('Replace existing theme')
            __msgid_4682776784 = __re_whitespace(''.join(__stream_4682776784)).strip()
            if 'label_replace_existing':
                __append(translate('label_replace_existing', mapping=None, default=__msgid_4682776784, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n                ')

            # <Static value=<ast.Dict object at 0x1171d8a00> name=None at 1171db1f0> -> __attrs_4681897376
            __attrs_4681897376 = _static_4682779136

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="formHelp">')
            __stream_4682789504 = []
            __append_4682789504 = __stream_4682789504.append
            __append_4682789504('\n                    Select this option to replace any existing theme that\n                    may have been uploaded previously.\n                ')
            __msgid_4682789504 = __re_whitespace(''.join(__stream_4682789504)).strip()
            if 'help_replace_existing':
                __append(translate('help_replace_existing', mapping=None, default=__msgid_4682789504, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n            </div>')
            if (__backup_selected_4683073904 is __marker):
                del econtext['selected']
            else:
                econtext['selected'] = __backup_selected_4683073904
            __append('\n\n            ')

            # <Static value=<ast.Dict object at 0x1171006a0> name=None at 117103d30> -> __attrs_4681892384
            __attrs_4681892384 = _static_4681893536

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="btn-group">\n                ')

            # <Static value=<ast.Dict object at 0x117100910> name=None at 117101000> -> __attrs_4681892288
            __attrs_4681892288 = _static_4681894160

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="submit" name="form.button.Import" class="btn btn-success save"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4681899728
            __default_4681899728 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x117101c00> at 117100df0> -> __attr_value
            __attr_value = 'Import'
            __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' />\n\n                ')

            # <Static value=<ast.Dict object at 0x117102c80> name=None at 117103a90> -> __attrs_4681893392
            __attrs_4681893392 = _static_4681903232

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="submit" name="form.button.Cancel" class="btn btn-primary cancel"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4681899632
            __default_4681899632 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x117101c30> at 117102da0> -> __attr_value
            __attr_value = 'Cancel'
            __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' />\n            </div>\n\n            ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4681894640
            __attrs_4681894640 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4681906064
            __default_4681906064 = _DEFAULT_MARKER

            # <Value 'context/@@authenticator/authenticator' (640:42)> -> __cache_4681894976
            __token = 30758
            try:
                __zt_tmp = __attrs_4681894640
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4681894976 = _static_4427992992('path', 'context/@@authenticator/authenticator', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/@@authenticator/authenticator' (640:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 1171025c0> -> __condition
            __expression = __cache_4681894976

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input />')
            else:
                __content = __cache_4681894976
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n        </form>')
            if (__backup_errors_4683043152 is __marker):
                del econtext['errors']
            else:
                econtext['errors'] = __backup_errors_4683043152
            __append('\n\n    </div>\n</div>\n\n\n    </section>\n        </article>\n      </div>')
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

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4678295248
            __attrs_4678295248 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678303216
            __default_4678303216 = _DEFAULT_MARKER

            # <Value 'string:<!DOCTYPE html>' (1:36)> -> __cache_4678289248
            __token = 36
            try:
                __zt_tmp = __attrs_4678295248
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4678289248 = _static_4427992992('string', '<!DOCTYPE html>', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'string:<!DOCTYPE html>' (1:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116d937c0> -> __condition
            __expression = __cache_4678289248

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4678289248
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x116d93fa0> name=None at 116d90100> -> __attrs_4678299712
            __attrs_4678299712 = _static_4678303648
            __backup_portal_state_4682799744 = get('portal_state', __marker)

            # <Value 'context/@@plone_portal_state' (8:31)> -> __value
            __token = 335
            try:
                __zt_tmp = __attrs_4678299712
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'context/@@plone_portal_state', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['portal_state'] = __value
            __backup_plone_view_4680595104 = get('plone_view', __marker)

            # <Value 'context/@@plone' (9:20)> -> __value
            __token = 385
            try:
                __zt_tmp = __attrs_4678299712
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'context/@@plone', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['plone_view'] = __value
            __backup_plone_layout_4680596160 = get('plone_layout', __marker)

            # <Value 'context/@@plone_layout' (10:21)> -> __value
            __token = 424
            try:
                __zt_tmp = __attrs_4678299712
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'context/@@plone_layout', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['plone_layout'] = __value
            __backup_lang_4680584976 = get('lang', __marker)

            # <Value 'portal_state/language' (11:12)> -> __value
            __token = 462
            try:
                __zt_tmp = __attrs_4678299712
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'portal_state/language', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['lang'] = __value
            __backup_view_4680595440 = get('view', __marker)

            # <Value 'nocall:view | nocall: plone_view' (12:11)> -> __value
            __token = 499
            try:
                __zt_tmp = __attrs_4678299712
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('nocall', 'view | nocall: plone_view', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['view'] = __value
            __backup_portal_url_4680595776 = get('portal_url', __marker)

            # <Value 'portal_state/portal_url' (13:16)> -> __value
            __token = 553
            try:
                __zt_tmp = __attrs_4678299712
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'portal_state/portal_url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['portal_url'] = __value
            __backup_ajax_load_4680478976 = get('ajax_load', __marker)

            # <Value 'python:False' (14:14)> -> __value
            __token = 597
            try:
                __zt_tmp = __attrs_4678299712
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', 'False', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['ajax_load'] = __value
            __backup_dummy_4680354160 = get('dummy', __marker)

            # <Value "python: request.set('disable_toolbar', True)" (15:9)> -> __value
            __token = 626
            try:
                __zt_tmp = __attrs_4678299712
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', " request.set('disable_toolbar', True)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['dummy'] = __value
            __backup_site_url_4680360640 = get('site_url', __marker)

            # <Value 'view/site_url' (16:11)> -> __value
            __token = 690
            try:
                __zt_tmp = __attrs_4678299712
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'view/site_url', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['site_url'] = __value
            __previous_i18n_domain_4678295632 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4678300096
            __default_4678300096 = _DEFAULT_MARKER

            # <Substitution 'lang' (17:27)> -> __attr_lang
            __token = 740
            try:
                __zt_tmp = __attrs_4678299712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_4427992992('path', 'lang', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))
            __append('>\n\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680546240
            __attrs_4680546240 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680541056
            __default_4680541056 = _DEFAULT_MARKER

            # <Value 'provider:plone.httpheaders' (19:40)> -> __cache_4680546192
            __token = 789
            try:
                __zt_tmp = __attrs_4680546240
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4680546192 = _static_4427992992('provider', 'plone.httpheaders', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.httpheaders' (19:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116fb56f0> -> __condition
            __expression = __cache_4680546192

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4680546192
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680533760
            __attrs_4680533760 = _static_4428767312

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n    ')

            # <Static value=<ast.Dict object at 0x116fb6830> name=None at 116fb4dc0> -> __attrs_4680546336
            __attrs_4680546336 = _static_4680542256

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta charset="utf-8" />\n\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680538320
            __attrs_4680538320 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680542832
            __default_4680542832 = _DEFAULT_MARKER

            # <Value 'provider:plone.htmlhead' (24:32)> -> __cache_4680536736
            __token = 892
            try:
                __zt_tmp = __attrs_4680538320
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4680536736 = _static_4427992992('provider', 'plone.htmlhead', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.htmlhead' (24:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116fb6230> -> __condition
            __expression = __cache_4680536736

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_4680536736
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680543552
            __attrs_4680543552 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680538800
            __default_4680538800 = _DEFAULT_MARKER

            # <Value 'provider:plone.htmlhead.links' (25:33)> -> __cache_4680545760
            __token = 953
            try:
                __zt_tmp = __attrs_4680543552
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4680545760 = _static_4427992992('provider', 'plone.htmlhead.links', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.htmlhead.links' (25:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116fb5780> -> __condition
            __expression = __cache_4680545760

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <link ... (0:0)
                # --------------------------------------------------------
                __append('<link />')
            else:
                __content = __cache_4680545760
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x116fb5c30> name=None at 116fb4970> -> __attrs_4680538992
            __attrs_4680538992 = _static_4680539184

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680532176
            __default_4680532176 = _DEFAULT_MARKER

            # <Substitution 'string:${context/portal_url}/++theme++barceloneta/css/barceloneta.min.css' (29:29)> -> __attr_href
            __token = 1075
            try:
                __zt_tmp = __attrs_4680538992
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4427992992('string', '${context/portal_url}/++theme++barceloneta/css/barceloneta.min.css', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' />\n    ')

            # <Static value=<ast.Dict object at 0x116fb63b0> name=None at 116fb7a90> -> __attrs_4680547632
            __attrs_4680547632 = _static_4680541104

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680546432
            __default_4680546432 = _DEFAULT_MARKER

            # <Substitution 'string:${context/portal_url}/++resource++plone.app.theming/controlpanel.css' (34:29)> -> __attr_href
            __token = 1249
            try:
                __zt_tmp = __attrs_4680547632
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4427992992('string', '${context/portal_url}/++resource++plone.app.theming/controlpanel.css', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' />\n\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680532992
            __attrs_4680532992 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680533280
            __default_4680533280 = _DEFAULT_MARKER

            # <Value 'nothing' (37:26)> -> __cache_4680541872
            __token = 1364
            try:
                __zt_tmp = __attrs_4680532992
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4680541872 = _static_4427992992('path', 'nothing', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'nothing' (37:26)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116fb6020> -> __condition
            __expression = __cache_4680541872

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('\n        Various slots where you can insert elements in the header from a template.\n    ')
            else:
                __content = __cache_4680541872
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680436032
            __attrs_4680436032 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680441264
            __default_4680441264 = _DEFAULT_MARKER

            # <Value 'provider:plone.scripts' (41:32)> -> __cache_4680533088
            __token = 1509
            try:
                __zt_tmp = __attrs_4680436032
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4680533088 = _static_4427992992('provider', 'plone.scripts', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.scripts' (41:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116fb4040> -> __condition
            __expression = __cache_4680533088

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_4680533088
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x116f9f5e0> name=None at 116f9c070> -> __attrs_4680445680
            __attrs_4680445680 = _static_4680447456

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta name="generator" content="Plone - http://plone.org" />\n\n  </head>\n\n  ')

            # <Static value=<ast.Dict object at 0x116f9f1c0> name=None at 116f9e980> -> __attrs_4680440688
            __attrs_4680440688 = _static_4680446400
            __backup_isRTL_4680357376 = get('isRTL', __marker)

            # <Value 'portal_state/is_rtl' (47:26)> -> __value
            __token = 1640
            try:
                __zt_tmp = __attrs_4680440688
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('path', 'portal_state/is_rtl', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['isRTL'] = __value
            __backup_sl_4680363520 = get('sl', __marker)

            # <Value "python:plone_layout.have_portlets('plone.leftcolumn', view)" (48:22)> -> __value
            __token = 1683
            try:
                __zt_tmp = __attrs_4680440688
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', "plone_layout.have_portlets('plone.leftcolumn', view)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['sl'] = __value
            __backup_sr_4682843952 = get('sr', __marker)

            # <Value "python:plone_layout.have_portlets('plone.rightcolumn', view)" (49:21)> -> __value
            __token = 1766
            try:
                __zt_tmp = __attrs_4680440688
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', "plone_layout.have_portlets('plone.rightcolumn', view)", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['sr'] = __value
            __backup_body_class_4682843808 = get('body_class', __marker)

            # <Value 'python:plone_layout.bodyClass(template, view)' (50:28)> -> __value
            __token = 1858
            try:
                __zt_tmp = __attrs_4680440688
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4427992992('python', 'plone_layout.bodyClass(template, view)', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            econtext['body_class'] = __value

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body')

            # <Value 'python:plone_view.patterns_settings()' (53:22)> -> __cache_4680443232
            __token = 2034
            try:
                __zt_tmp = __attrs_4680440688
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4680443232 = _static_4427992992('python', 'plone_view.patterns_settings()', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            if ('id' not in __chain(__cache_4680443232)):
                __append(' id="visual-portal-wrapper"')

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680448128
            __default_4680448128 = _DEFAULT_MARKER

            # <Substitution 'body_class' (51:30)> -> __attr_class
            __token = 1939
            try:
                __zt_tmp = __attrs_4680440688
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4427992992('path', 'body_class', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_class is not None) and ('class' not in __chain(__cache_4680443232))):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680449808
            __default_4680449808 = _DEFAULT_MARKER

            # <Substitution "python:isRTL and 'rtl' or 'ltr'" (52:27)> -> __attr_dir
            __token = 1978
            try:
                __zt_tmp = __attrs_4680440688
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_dir = _static_4427992992('python', "isRTL and 'rtl' or 'ltr'", econtext=econtext)(_static_4427994864(econtext, __zt_tmp))
            __attr_dir = __quote(__attr_dir, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_dir is not None) and ('dir' not in __chain(__cache_4680443232))):
                __append((' dir="%s"' % __attr_dir))
            __attr_4680439152 = __cache_4680443232
            for (name, value, ) in __attr_4680439152.items():
                if ((name not in _static_4685955184) and (value is not None)):
                    __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
            __append('>\n\n    ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680443760
            __attrs_4680443760 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680437088
            __default_4680437088 = _DEFAULT_MARKER

            # <Value 'provider:plone.toolbar' (56:32)> -> __cache_4680445392
            __token = 2144
            try:
                __zt_tmp = __attrs_4680443760
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4680445392 = _static_4427992992('provider', 'plone.toolbar', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.toolbar' (56:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116f9f6d0> -> __condition
            __expression = __cache_4680445392

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_4680445392
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x116f9cfa0> name=None at 116f9fd60> -> __attrs_4680825392
            __attrs_4680825392 = _static_4680437664

            # <aside ... (0:0)
            # --------------------------------------------------------
            __append('<aside id="global_statusmessage">\n      ')

            # <Static value=<ast.Dict object at 0x116ff9f30> name=None at 116ffab30> -> __attrs_4680820256
            __attrs_4680820256 = _static_4680818480

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="portalMessage info" role="status">\n        ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680816944
            __attrs_4680816944 = _static_4428767312

            # <strong ... (0:0)
            # --------------------------------------------------------
            __append('<strong>')
            __stream_4680816896 = []
            __append_4680816896 = __stream_4680816896.append
            __append_4680816896('Note')
            __msgid_4680816896 = __re_whitespace(''.join(__stream_4680816896)).strip()
            if __msgid_4680816896:
                __append(translate(__msgid_4680816896, mapping=None, default=__msgid_4680816896, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</strong>\n        ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680812192
            __attrs_4680812192 = _static_4428767312
            __stream_4680822800 = []
            __append_4680822800 = __stream_4680822800.append
            __append_4680822800('\n          Please note that this control panel page will never be themed.\n        ')
            __msgid_4680822800 = __re_whitespace(''.join(__stream_4680822800)).strip()
            if 'description_notheme_controlpanel':
                __append(translate('description_notheme_controlpanel', mapping=None, default=__msgid_4680822800, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n      </div>\n      ')

            # <Static value=<ast.Dict object at 0x107f9a050> name=None at 107f99c90> -> __attrs_4680811472
            __attrs_4680811472 = _static_4428767312

            # <Symbol value=<DEFAULT> at 107f9a410> -> __default_4680818624
            __default_4680818624 = _DEFAULT_MARKER

            # <Value 'provider:plone.globalstatusmessage' (65:42)> -> __cache_4680821840
            __token = 2536
            try:
                __zt_tmp = __attrs_4680811472
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4680821840 = _static_4427992992('provider', 'plone.globalstatusmessage', econtext=econtext)(_static_4427994864(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.globalstatusmessage' (65:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 107f9a410> at 116ff9de0> -> __condition
            __expression = __cache_4680821840

            # <Symbol value=<DEFAULT> at 107f9a410> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4680821840
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n    </aside>\n\n\n    ')

            # <Static value=<ast.Dict object at 0x116ff8670> name=None at 116ffa0b0> -> __attrs_4680812528
            __attrs_4680812528 = _static_4680812144

            # <article ... (0:0)
            # --------------------------------------------------------
            __append('<article id="portal-column-content">\n\n      ')
            __token = None
            render_content(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n    </article>\n  </body>')
            if (__backup_body_class_4682843808 is __marker):
                del econtext['body_class']
            else:
                econtext['body_class'] = __backup_body_class_4682843808
            if (__backup_sr_4682843952 is __marker):
                del econtext['sr']
            else:
                econtext['sr'] = __backup_sr_4682843952
            if (__backup_sl_4680363520 is __marker):
                del econtext['sl']
            else:
                econtext['sl'] = __backup_sl_4680363520
            if (__backup_isRTL_4680357376 is __marker):
                del econtext['isRTL']
            else:
                econtext['isRTL'] = __backup_isRTL_4680357376
            __append('\n</html>')
            __i18n_domain = __previous_i18n_domain_4678295632
            if (__backup_site_url_4680360640 is __marker):
                del econtext['site_url']
            else:
                econtext['site_url'] = __backup_site_url_4680360640
            if (__backup_dummy_4680354160 is __marker):
                del econtext['dummy']
            else:
                econtext['dummy'] = __backup_dummy_4680354160
            if (__backup_ajax_load_4680478976 is __marker):
                del econtext['ajax_load']
            else:
                econtext['ajax_load'] = __backup_ajax_load_4680478976
            if (__backup_portal_url_4680595776 is __marker):
                del econtext['portal_url']
            else:
                econtext['portal_url'] = __backup_portal_url_4680595776
            if (__backup_view_4680595440 is __marker):
                del econtext['view']
            else:
                econtext['view'] = __backup_view_4680595440
            if (__backup_lang_4680584976 is __marker):
                del econtext['lang']
            else:
                econtext['lang'] = __backup_lang_4680584976
            if (__backup_plone_layout_4680596160 is __marker):
                del econtext['plone_layout']
            else:
                econtext['plone_layout'] = __backup_plone_layout_4680596160
            if (__backup_plone_view_4680595104 is __marker):
                del econtext['plone_view']
            else:
                econtext['plone_view'] = __backup_plone_view_4680595104
            if (__backup_portal_state_4682799744 is __marker):
                del econtext['portal_state']
            else:
                econtext['portal_state'] = __backup_portal_state_4682799744
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content': render_content, 'render': render, }