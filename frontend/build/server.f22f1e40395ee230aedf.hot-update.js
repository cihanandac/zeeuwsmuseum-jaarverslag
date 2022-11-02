exports.id = "server";
exports.modules = {

/***/ "./node_modules/@plone/volto/src/components/index.js":
/*!***********************************************************!*\
  !*** ./node_modules/@plone/volto/src/components/index.js ***!
  \***********************************************************/
/*! exports provided: AppExtras, Header, Logo, Anontools, Navigation, Breadcrumbs, SearchWidget, Footer, Title, DefaultView, Pagination, Tags, OutdatedBrowser, LanguageSelector, RenderBlocks, SkipLinks, EventDetails, PreviewImage, Error, NotFound, Forbidden, Unauthorized, Avatar, Icon, ConditionalLink, UniversalLink, LinkMore, ContactForm, Login, Logout, Sitemap, Search, Comments, SocialSharing, Register, PasswordReset, RequestPasswordReset, ChangePassword, PersonalPreferences, PersonalInformation, CreateTranslation, TranslationObject, CompareLanguages, FileView, ImageView, NewsItemView, EventView, ListingView, SummaryView, TabularView, AlbumView, Actions, Add, AddonsControlpanel, Contents, Circle, DatabaseInformation, Controlpanel, Controlpanels, ContentTypes, ContentType, ContentTypeLayout, ContentTypeSchema, ContentTypesActions, UsersControlpanel, UserGroupMembershipControlPanel, GroupsControlpanel, ModerateComments, VersionOverview, Delete, Diff, Display, Edit, ModalForm, History, Sharing, Workflow, Messages, BlockChooser, BlockChooserButton, Toolbar, Sidebar, SidebarPopup, SidebarPortal, PersonalTools, More, Types, Toast, ManageTranslations, Form, BlocksToolbar, UndoToolbar, Field, SearchTags, CommentEditModal, ContentsBreadcrumbs, ContentsIndexHeader, ContentsItem, ContentsUploadModal, ContentsPropertiesModal, ContentsRenameModal, ContentsWorkflowModal, ContentsTagsModal, RenderUsers, RenderGroups, DiffField, DragDropList, InlineForm, BlocksForm, BlockDataForm, FormFieldWrapper, ArrayWidget, CheckboxWidget, DatetimeWidget, RecurrenceWidget, FileWidget, IdWidget, PasswordWidget, ReferenceWidget, SchemaWidget, SchemaWidgetFieldset, SelectWidget, TextareaWidget, TextWidget, WysiwygWidget, ObjectBrowserWidget, ObjectBrowserWidgetMode, ObjectWidget, ObjectListWidget, EditDescriptionBlock, EditTitleBlock, EditToCBlock, EditTextBlock, EditImageBlock, EditListingBlock, EditVideoBlock, EditBlock, EditHeroImageLeftBlock, ViewHeroImageLeftBlock, EditMapBlock, EditHTMLBlock, ViewDescriptionBlock, ViewTitleBlock, ViewToCBlock, ViewTextBlock, ViewImageBlock, ViewListingBlock, ViewVideoBlock, ViewMapBlock, ViewHTMLBlock, ListingBlockBody, ListingBlockData, ImageSidebar, MapsSidebar, VideoSidebar, LeadImageSidebar, Style, BlockSettingsSidebar, BlockSettingsSchema, TextSettingsSchema, ImageSettingsSchema, ToCSettingsSchema, MaybeWrap, ContentMetadataTags, FormattedDate, FormattedRelativeDate, Component, App */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "EventView", function() { return EventView; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "DatetimeWidget", function() { return DatetimeWidget; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "RecurrenceWidget", function() { return RecurrenceWidget; });
/* harmony import */ var _loadable_component__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @loadable/component */ "@loadable/component");
/* harmony import */ var _loadable_component__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_loadable_component__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _plone_volto_components_theme_AppExtras_AppExtras__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @plone/volto/components/theme/AppExtras/AppExtras */ "./node_modules/@plone/volto/src/components/theme/AppExtras/AppExtras.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "AppExtras", function() { return _plone_volto_components_theme_AppExtras_AppExtras__WEBPACK_IMPORTED_MODULE_1__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Header_Header__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @plone/volto/components/theme/Header/Header */ "./src/customizations/components/theme/Header/Header.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Header", function() { return _plone_volto_components_theme_Header_Header__WEBPACK_IMPORTED_MODULE_2__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Logo_Logo__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @plone/volto/components/theme/Logo/Logo */ "./node_modules/@plone/volto/src/components/theme/Logo/Logo.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Logo", function() { return _plone_volto_components_theme_Logo_Logo__WEBPACK_IMPORTED_MODULE_3__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Anontools_Anontools__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @plone/volto/components/theme/Anontools/Anontools */ "./node_modules/@plone/volto/src/components/theme/Anontools/Anontools.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Anontools", function() { return _plone_volto_components_theme_Anontools_Anontools__WEBPACK_IMPORTED_MODULE_4__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Navigation_Navigation__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @plone/volto/components/theme/Navigation/Navigation */ "./src/customizations/components/theme/Navigation/Navigation.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Navigation", function() { return _plone_volto_components_theme_Navigation_Navigation__WEBPACK_IMPORTED_MODULE_5__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Breadcrumbs_Breadcrumbs__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @plone/volto/components/theme/Breadcrumbs/Breadcrumbs */ "./src/customizations/components/theme/Breadcrumbs/Breadcrumbs.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Breadcrumbs", function() { return _plone_volto_components_theme_Breadcrumbs_Breadcrumbs__WEBPACK_IMPORTED_MODULE_6__["default"]; });

/* harmony import */ var _plone_volto_components_theme_SearchWidget_SearchWidget__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @plone/volto/components/theme/SearchWidget/SearchWidget */ "./node_modules/@plone/volto/src/components/theme/SearchWidget/SearchWidget.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "SearchWidget", function() { return _plone_volto_components_theme_SearchWidget_SearchWidget__WEBPACK_IMPORTED_MODULE_7__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Footer_Footer__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @plone/volto/components/theme/Footer/Footer */ "./src/customizations/components/theme/Footer/Footer.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Footer", function() { return _plone_volto_components_theme_Footer_Footer__WEBPACK_IMPORTED_MODULE_8__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Title_Title__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @plone/volto/components/theme/Title/Title */ "./node_modules/@plone/volto/src/components/theme/Title/Title.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Title", function() { return _plone_volto_components_theme_Title_Title__WEBPACK_IMPORTED_MODULE_9__["default"]; });

/* harmony import */ var _plone_volto_components_theme_View_DefaultView__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @plone/volto/components/theme/View/DefaultView */ "./node_modules/@plone/volto/src/components/theme/View/DefaultView.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "DefaultView", function() { return _plone_volto_components_theme_View_DefaultView__WEBPACK_IMPORTED_MODULE_10__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Pagination_Pagination__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! @plone/volto/components/theme/Pagination/Pagination */ "./node_modules/@plone/volto/src/components/theme/Pagination/Pagination.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Pagination", function() { return _plone_volto_components_theme_Pagination_Pagination__WEBPACK_IMPORTED_MODULE_11__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Tags_Tags__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! @plone/volto/components/theme/Tags/Tags */ "./node_modules/@plone/volto/src/components/theme/Tags/Tags.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Tags", function() { return _plone_volto_components_theme_Tags_Tags__WEBPACK_IMPORTED_MODULE_12__["default"]; });

/* harmony import */ var _plone_volto_components_theme_OutdatedBrowser_OutdatedBrowser__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! @plone/volto/components/theme/OutdatedBrowser/OutdatedBrowser */ "./node_modules/@plone/volto/src/components/theme/OutdatedBrowser/OutdatedBrowser.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "OutdatedBrowser", function() { return _plone_volto_components_theme_OutdatedBrowser_OutdatedBrowser__WEBPACK_IMPORTED_MODULE_13__["default"]; });

/* harmony import */ var _plone_volto_components_theme_LanguageSelector_LanguageSelector__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! @plone/volto/components/theme/LanguageSelector/LanguageSelector */ "./node_modules/@plone/volto/src/components/theme/LanguageSelector/LanguageSelector.js");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "LanguageSelector", function() { return _plone_volto_components_theme_LanguageSelector_LanguageSelector__WEBPACK_IMPORTED_MODULE_14__["default"]; });

/* harmony import */ var _plone_volto_components_theme_View_RenderBlocks__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! @plone/volto/components/theme/View/RenderBlocks */ "./node_modules/@plone/volto/src/components/theme/View/RenderBlocks.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "RenderBlocks", function() { return _plone_volto_components_theme_View_RenderBlocks__WEBPACK_IMPORTED_MODULE_15__["default"]; });

/* harmony import */ var _plone_volto_components_theme_SkipLinks_SkipLinks__WEBPACK_IMPORTED_MODULE_16__ = __webpack_require__(/*! @plone/volto/components/theme/SkipLinks/SkipLinks */ "./node_modules/@plone/volto/src/components/theme/SkipLinks/SkipLinks.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "SkipLinks", function() { return _plone_volto_components_theme_SkipLinks_SkipLinks__WEBPACK_IMPORTED_MODULE_16__["default"]; });

/* harmony import */ var _plone_volto_components_theme_EventDetails_EventDetails__WEBPACK_IMPORTED_MODULE_17__ = __webpack_require__(/*! @plone/volto/components/theme/EventDetails/EventDetails */ "./node_modules/@plone/volto/src/components/theme/EventDetails/EventDetails.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "EventDetails", function() { return _plone_volto_components_theme_EventDetails_EventDetails__WEBPACK_IMPORTED_MODULE_17__["default"]; });

/* harmony import */ var _plone_volto_components_theme_PreviewImage_PreviewImage__WEBPACK_IMPORTED_MODULE_18__ = __webpack_require__(/*! @plone/volto/components/theme/PreviewImage/PreviewImage */ "./node_modules/@plone/volto/src/components/theme/PreviewImage/PreviewImage.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "PreviewImage", function() { return _plone_volto_components_theme_PreviewImage_PreviewImage__WEBPACK_IMPORTED_MODULE_18__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Error_Error__WEBPACK_IMPORTED_MODULE_19__ = __webpack_require__(/*! @plone/volto/components/theme/Error/Error */ "./node_modules/@plone/volto/src/components/theme/Error/Error.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Error", function() { return _plone_volto_components_theme_Error_Error__WEBPACK_IMPORTED_MODULE_19__["default"]; });

/* harmony import */ var _plone_volto_components_theme_NotFound_NotFound__WEBPACK_IMPORTED_MODULE_20__ = __webpack_require__(/*! @plone/volto/components/theme/NotFound/NotFound */ "./node_modules/@plone/volto/src/components/theme/NotFound/NotFound.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "NotFound", function() { return _plone_volto_components_theme_NotFound_NotFound__WEBPACK_IMPORTED_MODULE_20__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Forbidden_Forbidden__WEBPACK_IMPORTED_MODULE_21__ = __webpack_require__(/*! @plone/volto/components/theme/Forbidden/Forbidden */ "./node_modules/@plone/volto/src/components/theme/Forbidden/Forbidden.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Forbidden", function() { return _plone_volto_components_theme_Forbidden_Forbidden__WEBPACK_IMPORTED_MODULE_21__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Unauthorized_Unauthorized__WEBPACK_IMPORTED_MODULE_22__ = __webpack_require__(/*! @plone/volto/components/theme/Unauthorized/Unauthorized */ "./node_modules/@plone/volto/src/components/theme/Unauthorized/Unauthorized.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Unauthorized", function() { return _plone_volto_components_theme_Unauthorized_Unauthorized__WEBPACK_IMPORTED_MODULE_22__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Avatar_Avatar__WEBPACK_IMPORTED_MODULE_23__ = __webpack_require__(/*! @plone/volto/components/theme/Avatar/Avatar */ "./node_modules/@plone/volto/src/components/theme/Avatar/Avatar.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Avatar", function() { return _plone_volto_components_theme_Avatar_Avatar__WEBPACK_IMPORTED_MODULE_23__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Icon_Icon__WEBPACK_IMPORTED_MODULE_24__ = __webpack_require__(/*! @plone/volto/components/theme/Icon/Icon */ "./node_modules/@plone/volto/src/components/theme/Icon/Icon.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Icon", function() { return _plone_volto_components_theme_Icon_Icon__WEBPACK_IMPORTED_MODULE_24__["default"]; });

/* harmony import */ var _plone_volto_components_manage_ConditionalLink_ConditionalLink__WEBPACK_IMPORTED_MODULE_25__ = __webpack_require__(/*! @plone/volto/components/manage/ConditionalLink/ConditionalLink */ "./node_modules/@plone/volto/src/components/manage/ConditionalLink/ConditionalLink.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ConditionalLink", function() { return _plone_volto_components_manage_ConditionalLink_ConditionalLink__WEBPACK_IMPORTED_MODULE_25__["default"]; });

/* harmony import */ var _plone_volto_components_manage_UniversalLink_UniversalLink__WEBPACK_IMPORTED_MODULE_26__ = __webpack_require__(/*! @plone/volto/components/manage/UniversalLink/UniversalLink */ "./node_modules/@plone/volto/src/components/manage/UniversalLink/UniversalLink.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "UniversalLink", function() { return _plone_volto_components_manage_UniversalLink_UniversalLink__WEBPACK_IMPORTED_MODULE_26__["default"]; });

/* harmony import */ var _plone_volto_components_manage_LinkMore_LinkMore__WEBPACK_IMPORTED_MODULE_27__ = __webpack_require__(/*! @plone/volto/components/manage/LinkMore/LinkMore */ "./node_modules/@plone/volto/src/components/manage/LinkMore/LinkMore.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "LinkMore", function() { return _plone_volto_components_manage_LinkMore_LinkMore__WEBPACK_IMPORTED_MODULE_27__["default"]; });

/* harmony import */ var _plone_volto_components_theme_ContactForm_ContactForm__WEBPACK_IMPORTED_MODULE_28__ = __webpack_require__(/*! @plone/volto/components/theme/ContactForm/ContactForm */ "./node_modules/@plone/volto/src/components/theme/ContactForm/ContactForm.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ContactForm", function() { return _plone_volto_components_theme_ContactForm_ContactForm__WEBPACK_IMPORTED_MODULE_28__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Login_Login__WEBPACK_IMPORTED_MODULE_29__ = __webpack_require__(/*! @plone/volto/components/theme/Login/Login */ "./node_modules/@plone/volto/src/components/theme/Login/Login.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Login", function() { return _plone_volto_components_theme_Login_Login__WEBPACK_IMPORTED_MODULE_29__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Logout_Logout__WEBPACK_IMPORTED_MODULE_30__ = __webpack_require__(/*! @plone/volto/components/theme/Logout/Logout */ "./node_modules/@plone/volto/src/components/theme/Logout/Logout.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Logout", function() { return _plone_volto_components_theme_Logout_Logout__WEBPACK_IMPORTED_MODULE_30__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Sitemap_Sitemap__WEBPACK_IMPORTED_MODULE_31__ = __webpack_require__(/*! @plone/volto/components/theme/Sitemap/Sitemap */ "./node_modules/@plone/volto/src/components/theme/Sitemap/Sitemap.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Sitemap", function() { return _plone_volto_components_theme_Sitemap_Sitemap__WEBPACK_IMPORTED_MODULE_31__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Search_Search__WEBPACK_IMPORTED_MODULE_32__ = __webpack_require__(/*! @plone/volto/components/theme/Search/Search */ "./node_modules/@plone/volto/src/components/theme/Search/Search.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Search", function() { return _plone_volto_components_theme_Search_Search__WEBPACK_IMPORTED_MODULE_32__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Comments_Comments__WEBPACK_IMPORTED_MODULE_33__ = __webpack_require__(/*! @plone/volto/components/theme/Comments/Comments */ "./node_modules/@plone/volto/src/components/theme/Comments/Comments.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Comments", function() { return _plone_volto_components_theme_Comments_Comments__WEBPACK_IMPORTED_MODULE_33__["default"]; });

/* harmony import */ var _plone_volto_components_theme_SocialSharing_SocialSharing__WEBPACK_IMPORTED_MODULE_34__ = __webpack_require__(/*! @plone/volto/components/theme/SocialSharing/SocialSharing */ "./node_modules/@plone/volto/src/components/theme/SocialSharing/SocialSharing.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "SocialSharing", function() { return _plone_volto_components_theme_SocialSharing_SocialSharing__WEBPACK_IMPORTED_MODULE_34__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Register_Register__WEBPACK_IMPORTED_MODULE_35__ = __webpack_require__(/*! @plone/volto/components/theme/Register/Register */ "./node_modules/@plone/volto/src/components/theme/Register/Register.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Register", function() { return _plone_volto_components_theme_Register_Register__WEBPACK_IMPORTED_MODULE_35__["default"]; });

/* harmony import */ var _plone_volto_components_theme_PasswordReset_PasswordReset__WEBPACK_IMPORTED_MODULE_36__ = __webpack_require__(/*! @plone/volto/components/theme/PasswordReset/PasswordReset */ "./node_modules/@plone/volto/src/components/theme/PasswordReset/PasswordReset.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "PasswordReset", function() { return _plone_volto_components_theme_PasswordReset_PasswordReset__WEBPACK_IMPORTED_MODULE_36__["default"]; });

/* harmony import */ var _plone_volto_components_theme_PasswordReset_RequestPasswordReset__WEBPACK_IMPORTED_MODULE_37__ = __webpack_require__(/*! @plone/volto/components/theme/PasswordReset/RequestPasswordReset */ "./node_modules/@plone/volto/src/components/theme/PasswordReset/RequestPasswordReset.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "RequestPasswordReset", function() { return _plone_volto_components_theme_PasswordReset_RequestPasswordReset__WEBPACK_IMPORTED_MODULE_37__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Preferences_ChangePassword__WEBPACK_IMPORTED_MODULE_38__ = __webpack_require__(/*! @plone/volto/components/manage/Preferences/ChangePassword */ "./node_modules/@plone/volto/src/components/manage/Preferences/ChangePassword.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ChangePassword", function() { return _plone_volto_components_manage_Preferences_ChangePassword__WEBPACK_IMPORTED_MODULE_38__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Preferences_PersonalPreferences__WEBPACK_IMPORTED_MODULE_39__ = __webpack_require__(/*! @plone/volto/components/manage/Preferences/PersonalPreferences */ "./node_modules/@plone/volto/src/components/manage/Preferences/PersonalPreferences.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "PersonalPreferences", function() { return _plone_volto_components_manage_Preferences_PersonalPreferences__WEBPACK_IMPORTED_MODULE_39__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Preferences_PersonalInformation__WEBPACK_IMPORTED_MODULE_40__ = __webpack_require__(/*! @plone/volto/components/manage/Preferences/PersonalInformation */ "./node_modules/@plone/volto/src/components/manage/Preferences/PersonalInformation.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "PersonalInformation", function() { return _plone_volto_components_manage_Preferences_PersonalInformation__WEBPACK_IMPORTED_MODULE_40__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Multilingual_CreateTranslation__WEBPACK_IMPORTED_MODULE_41__ = __webpack_require__(/*! @plone/volto/components/manage/Multilingual/CreateTranslation */ "./node_modules/@plone/volto/src/components/manage/Multilingual/CreateTranslation.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "CreateTranslation", function() { return _plone_volto_components_manage_Multilingual_CreateTranslation__WEBPACK_IMPORTED_MODULE_41__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Multilingual_TranslationObject__WEBPACK_IMPORTED_MODULE_42__ = __webpack_require__(/*! @plone/volto/components/manage/Multilingual/TranslationObject */ "./node_modules/@plone/volto/src/components/manage/Multilingual/TranslationObject.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "TranslationObject", function() { return _plone_volto_components_manage_Multilingual_TranslationObject__WEBPACK_IMPORTED_MODULE_42__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Multilingual_CompareLanguages__WEBPACK_IMPORTED_MODULE_43__ = __webpack_require__(/*! @plone/volto/components/manage/Multilingual/CompareLanguages */ "./node_modules/@plone/volto/src/components/manage/Multilingual/CompareLanguages.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "CompareLanguages", function() { return _plone_volto_components_manage_Multilingual_CompareLanguages__WEBPACK_IMPORTED_MODULE_43__["default"]; });

/* harmony import */ var _plone_volto_components_theme_View_FileView__WEBPACK_IMPORTED_MODULE_44__ = __webpack_require__(/*! @plone/volto/components/theme/View/FileView */ "./node_modules/@plone/volto/src/components/theme/View/FileView.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "FileView", function() { return _plone_volto_components_theme_View_FileView__WEBPACK_IMPORTED_MODULE_44__["default"]; });

/* harmony import */ var _plone_volto_components_theme_View_ImageView__WEBPACK_IMPORTED_MODULE_45__ = __webpack_require__(/*! @plone/volto/components/theme/View/ImageView */ "./node_modules/@plone/volto/src/components/theme/View/ImageView.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ImageView", function() { return _plone_volto_components_theme_View_ImageView__WEBPACK_IMPORTED_MODULE_45__["default"]; });

/* harmony import */ var _plone_volto_components_theme_View_NewsItemView__WEBPACK_IMPORTED_MODULE_46__ = __webpack_require__(/*! @plone/volto/components/theme/View/NewsItemView */ "./node_modules/@plone/volto/src/components/theme/View/NewsItemView.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "NewsItemView", function() { return _plone_volto_components_theme_View_NewsItemView__WEBPACK_IMPORTED_MODULE_46__["default"]; });

/* harmony import */ var _plone_volto_components_theme_View_ListingView__WEBPACK_IMPORTED_MODULE_47__ = __webpack_require__(/*! @plone/volto/components/theme/View/ListingView */ "./node_modules/@plone/volto/src/components/theme/View/ListingView.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ListingView", function() { return _plone_volto_components_theme_View_ListingView__WEBPACK_IMPORTED_MODULE_47__["default"]; });

/* harmony import */ var _plone_volto_components_theme_View_SummaryView__WEBPACK_IMPORTED_MODULE_48__ = __webpack_require__(/*! @plone/volto/components/theme/View/SummaryView */ "./node_modules/@plone/volto/src/components/theme/View/SummaryView.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "SummaryView", function() { return _plone_volto_components_theme_View_SummaryView__WEBPACK_IMPORTED_MODULE_48__["default"]; });

/* harmony import */ var _plone_volto_components_theme_View_TabularView__WEBPACK_IMPORTED_MODULE_49__ = __webpack_require__(/*! @plone/volto/components/theme/View/TabularView */ "./node_modules/@plone/volto/src/components/theme/View/TabularView.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "TabularView", function() { return _plone_volto_components_theme_View_TabularView__WEBPACK_IMPORTED_MODULE_49__["default"]; });

/* harmony import */ var _plone_volto_components_theme_View_AlbumView__WEBPACK_IMPORTED_MODULE_50__ = __webpack_require__(/*! @plone/volto/components/theme/View/AlbumView */ "./node_modules/@plone/volto/src/components/theme/View/AlbumView.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "AlbumView", function() { return _plone_volto_components_theme_View_AlbumView__WEBPACK_IMPORTED_MODULE_50__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Actions_Actions__WEBPACK_IMPORTED_MODULE_51__ = __webpack_require__(/*! @plone/volto/components/manage/Actions/Actions */ "./node_modules/@plone/volto/src/components/manage/Actions/Actions.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Actions", function() { return _plone_volto_components_manage_Actions_Actions__WEBPACK_IMPORTED_MODULE_51__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Add_Add__WEBPACK_IMPORTED_MODULE_52__ = __webpack_require__(/*! @plone/volto/components/manage/Add/Add */ "./node_modules/@plone/volto/src/components/manage/Add/Add.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Add", function() { return _plone_volto_components_manage_Add_Add__WEBPACK_IMPORTED_MODULE_52__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Controlpanels_AddonsControlpanel__WEBPACK_IMPORTED_MODULE_53__ = __webpack_require__(/*! @plone/volto/components/manage/Controlpanels/AddonsControlpanel */ "./node_modules/@plone/volto/src/components/manage/Controlpanels/AddonsControlpanel.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "AddonsControlpanel", function() { return _plone_volto_components_manage_Controlpanels_AddonsControlpanel__WEBPACK_IMPORTED_MODULE_53__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Contents_Contents__WEBPACK_IMPORTED_MODULE_54__ = __webpack_require__(/*! @plone/volto/components/manage/Contents/Contents */ "./node_modules/@plone/volto/src/components/manage/Contents/Contents.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Contents", function() { return _plone_volto_components_manage_Contents_Contents__WEBPACK_IMPORTED_MODULE_54__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Contents_circle__WEBPACK_IMPORTED_MODULE_55__ = __webpack_require__(/*! @plone/volto/components/manage/Contents/circle */ "./node_modules/@plone/volto/src/components/manage/Contents/circle.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Circle", function() { return _plone_volto_components_manage_Contents_circle__WEBPACK_IMPORTED_MODULE_55__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Controlpanels_DatabaseInformation__WEBPACK_IMPORTED_MODULE_56__ = __webpack_require__(/*! @plone/volto/components/manage/Controlpanels/DatabaseInformation */ "./node_modules/@plone/volto/src/components/manage/Controlpanels/DatabaseInformation.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "DatabaseInformation", function() { return _plone_volto_components_manage_Controlpanels_DatabaseInformation__WEBPACK_IMPORTED_MODULE_56__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Controlpanels_Controlpanel__WEBPACK_IMPORTED_MODULE_57__ = __webpack_require__(/*! @plone/volto/components/manage/Controlpanels/Controlpanel */ "./node_modules/@plone/volto/src/components/manage/Controlpanels/Controlpanel.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Controlpanel", function() { return _plone_volto_components_manage_Controlpanels_Controlpanel__WEBPACK_IMPORTED_MODULE_57__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Controlpanels_Controlpanels__WEBPACK_IMPORTED_MODULE_58__ = __webpack_require__(/*! @plone/volto/components/manage/Controlpanels/Controlpanels */ "./node_modules/@plone/volto/src/components/manage/Controlpanels/Controlpanels.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Controlpanels", function() { return _plone_volto_components_manage_Controlpanels_Controlpanels__WEBPACK_IMPORTED_MODULE_58__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Controlpanels_ContentTypes__WEBPACK_IMPORTED_MODULE_59__ = __webpack_require__(/*! @plone/volto/components/manage/Controlpanels/ContentTypes */ "./node_modules/@plone/volto/src/components/manage/Controlpanels/ContentTypes.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ContentTypes", function() { return _plone_volto_components_manage_Controlpanels_ContentTypes__WEBPACK_IMPORTED_MODULE_59__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Controlpanels_ContentType__WEBPACK_IMPORTED_MODULE_60__ = __webpack_require__(/*! @plone/volto/components/manage/Controlpanels/ContentType */ "./node_modules/@plone/volto/src/components/manage/Controlpanels/ContentType.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ContentType", function() { return _plone_volto_components_manage_Controlpanels_ContentType__WEBPACK_IMPORTED_MODULE_60__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Controlpanels_ContentTypeLayout__WEBPACK_IMPORTED_MODULE_61__ = __webpack_require__(/*! @plone/volto/components/manage/Controlpanels/ContentTypeLayout */ "./node_modules/@plone/volto/src/components/manage/Controlpanels/ContentTypeLayout.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ContentTypeLayout", function() { return _plone_volto_components_manage_Controlpanels_ContentTypeLayout__WEBPACK_IMPORTED_MODULE_61__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Controlpanels_ContentTypeSchema__WEBPACK_IMPORTED_MODULE_62__ = __webpack_require__(/*! @plone/volto/components/manage/Controlpanels/ContentTypeSchema */ "./node_modules/@plone/volto/src/components/manage/Controlpanels/ContentTypeSchema.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ContentTypeSchema", function() { return _plone_volto_components_manage_Controlpanels_ContentTypeSchema__WEBPACK_IMPORTED_MODULE_62__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Controlpanels_ContentTypesActions__WEBPACK_IMPORTED_MODULE_63__ = __webpack_require__(/*! @plone/volto/components/manage/Controlpanels/ContentTypesActions */ "./node_modules/@plone/volto/src/components/manage/Controlpanels/ContentTypesActions.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ContentTypesActions", function() { return _plone_volto_components_manage_Controlpanels_ContentTypesActions__WEBPACK_IMPORTED_MODULE_63__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Controlpanels_Users_UsersControlpanel__WEBPACK_IMPORTED_MODULE_64__ = __webpack_require__(/*! @plone/volto/components/manage/Controlpanels/Users/UsersControlpanel */ "./node_modules/@plone/volto/src/components/manage/Controlpanels/Users/UsersControlpanel.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "UsersControlpanel", function() { return _plone_volto_components_manage_Controlpanels_Users_UsersControlpanel__WEBPACK_IMPORTED_MODULE_64__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Controlpanels_Users_UserGroupMembershipControlPanel__WEBPACK_IMPORTED_MODULE_65__ = __webpack_require__(/*! @plone/volto/components/manage/Controlpanels/Users/UserGroupMembershipControlPanel */ "./node_modules/@plone/volto/src/components/manage/Controlpanels/Users/UserGroupMembershipControlPanel.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "UserGroupMembershipControlPanel", function() { return _plone_volto_components_manage_Controlpanels_Users_UserGroupMembershipControlPanel__WEBPACK_IMPORTED_MODULE_65__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Controlpanels_Groups_GroupsControlpanel__WEBPACK_IMPORTED_MODULE_66__ = __webpack_require__(/*! @plone/volto/components/manage/Controlpanels/Groups/GroupsControlpanel */ "./node_modules/@plone/volto/src/components/manage/Controlpanels/Groups/GroupsControlpanel.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "GroupsControlpanel", function() { return _plone_volto_components_manage_Controlpanels_Groups_GroupsControlpanel__WEBPACK_IMPORTED_MODULE_66__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Controlpanels_ModerateComments__WEBPACK_IMPORTED_MODULE_67__ = __webpack_require__(/*! @plone/volto/components/manage/Controlpanels/ModerateComments */ "./node_modules/@plone/volto/src/components/manage/Controlpanels/ModerateComments.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ModerateComments", function() { return _plone_volto_components_manage_Controlpanels_ModerateComments__WEBPACK_IMPORTED_MODULE_67__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Controlpanels_VersionOverview__WEBPACK_IMPORTED_MODULE_68__ = __webpack_require__(/*! @plone/volto/components/manage/Controlpanels/VersionOverview */ "./node_modules/@plone/volto/src/components/manage/Controlpanels/VersionOverview.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "VersionOverview", function() { return _plone_volto_components_manage_Controlpanels_VersionOverview__WEBPACK_IMPORTED_MODULE_68__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Delete_Delete__WEBPACK_IMPORTED_MODULE_69__ = __webpack_require__(/*! @plone/volto/components/manage/Delete/Delete */ "./node_modules/@plone/volto/src/components/manage/Delete/Delete.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Delete", function() { return _plone_volto_components_manage_Delete_Delete__WEBPACK_IMPORTED_MODULE_69__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Diff_Diff__WEBPACK_IMPORTED_MODULE_70__ = __webpack_require__(/*! @plone/volto/components/manage/Diff/Diff */ "./node_modules/@plone/volto/src/components/manage/Diff/Diff.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Diff", function() { return _plone_volto_components_manage_Diff_Diff__WEBPACK_IMPORTED_MODULE_70__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Display_Display__WEBPACK_IMPORTED_MODULE_71__ = __webpack_require__(/*! @plone/volto/components/manage/Display/Display */ "./node_modules/@plone/volto/src/components/manage/Display/Display.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Display", function() { return _plone_volto_components_manage_Display_Display__WEBPACK_IMPORTED_MODULE_71__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Edit_Edit__WEBPACK_IMPORTED_MODULE_72__ = __webpack_require__(/*! @plone/volto/components/manage/Edit/Edit */ "./node_modules/@plone/volto/src/components/manage/Edit/Edit.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Edit", function() { return _plone_volto_components_manage_Edit_Edit__WEBPACK_IMPORTED_MODULE_72__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Form_ModalForm__WEBPACK_IMPORTED_MODULE_73__ = __webpack_require__(/*! @plone/volto/components/manage/Form/ModalForm */ "./node_modules/@plone/volto/src/components/manage/Form/ModalForm.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ModalForm", function() { return _plone_volto_components_manage_Form_ModalForm__WEBPACK_IMPORTED_MODULE_73__["default"]; });

/* harmony import */ var _plone_volto_components_manage_History_History__WEBPACK_IMPORTED_MODULE_74__ = __webpack_require__(/*! @plone/volto/components/manage/History/History */ "./node_modules/@plone/volto/src/components/manage/History/History.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "History", function() { return _plone_volto_components_manage_History_History__WEBPACK_IMPORTED_MODULE_74__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Sharing_Sharing__WEBPACK_IMPORTED_MODULE_75__ = __webpack_require__(/*! @plone/volto/components/manage/Sharing/Sharing */ "./node_modules/@plone/volto/src/components/manage/Sharing/Sharing.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Sharing", function() { return _plone_volto_components_manage_Sharing_Sharing__WEBPACK_IMPORTED_MODULE_75__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Workflow_Workflow__WEBPACK_IMPORTED_MODULE_76__ = __webpack_require__(/*! @plone/volto/components/manage/Workflow/Workflow */ "./node_modules/@plone/volto/src/components/manage/Workflow/Workflow.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Workflow", function() { return _plone_volto_components_manage_Workflow_Workflow__WEBPACK_IMPORTED_MODULE_76__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Messages_Messages__WEBPACK_IMPORTED_MODULE_77__ = __webpack_require__(/*! @plone/volto/components/manage/Messages/Messages */ "./node_modules/@plone/volto/src/components/manage/Messages/Messages.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Messages", function() { return _plone_volto_components_manage_Messages_Messages__WEBPACK_IMPORTED_MODULE_77__["default"]; });

/* harmony import */ var _plone_volto_components_manage_BlockChooser_BlockChooser__WEBPACK_IMPORTED_MODULE_78__ = __webpack_require__(/*! @plone/volto/components/manage/BlockChooser/BlockChooser */ "./node_modules/@plone/volto/src/components/manage/BlockChooser/BlockChooser.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "BlockChooser", function() { return _plone_volto_components_manage_BlockChooser_BlockChooser__WEBPACK_IMPORTED_MODULE_78__["default"]; });

/* harmony import */ var _plone_volto_components_manage_BlockChooser_BlockChooserButton__WEBPACK_IMPORTED_MODULE_79__ = __webpack_require__(/*! @plone/volto/components/manage/BlockChooser/BlockChooserButton */ "./node_modules/@plone/volto/src/components/manage/BlockChooser/BlockChooserButton.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "BlockChooserButton", function() { return _plone_volto_components_manage_BlockChooser_BlockChooserButton__WEBPACK_IMPORTED_MODULE_79__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Toolbar_Toolbar__WEBPACK_IMPORTED_MODULE_80__ = __webpack_require__(/*! @plone/volto/components/manage/Toolbar/Toolbar */ "./node_modules/@plone/volto/src/components/manage/Toolbar/Toolbar.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Toolbar", function() { return _plone_volto_components_manage_Toolbar_Toolbar__WEBPACK_IMPORTED_MODULE_80__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Sidebar_Sidebar__WEBPACK_IMPORTED_MODULE_81__ = __webpack_require__(/*! @plone/volto/components/manage/Sidebar/Sidebar */ "./node_modules/@plone/volto/src/components/manage/Sidebar/Sidebar.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Sidebar", function() { return _plone_volto_components_manage_Sidebar_Sidebar__WEBPACK_IMPORTED_MODULE_81__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Sidebar_SidebarPopup__WEBPACK_IMPORTED_MODULE_82__ = __webpack_require__(/*! @plone/volto/components/manage/Sidebar/SidebarPopup */ "./node_modules/@plone/volto/src/components/manage/Sidebar/SidebarPopup.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "SidebarPopup", function() { return _plone_volto_components_manage_Sidebar_SidebarPopup__WEBPACK_IMPORTED_MODULE_82__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Sidebar_SidebarPortal__WEBPACK_IMPORTED_MODULE_83__ = __webpack_require__(/*! @plone/volto/components/manage/Sidebar/SidebarPortal */ "./node_modules/@plone/volto/src/components/manage/Sidebar/SidebarPortal.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "SidebarPortal", function() { return _plone_volto_components_manage_Sidebar_SidebarPortal__WEBPACK_IMPORTED_MODULE_83__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Toolbar_PersonalTools__WEBPACK_IMPORTED_MODULE_84__ = __webpack_require__(/*! @plone/volto/components/manage/Toolbar/PersonalTools */ "./node_modules/@plone/volto/src/components/manage/Toolbar/PersonalTools.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "PersonalTools", function() { return _plone_volto_components_manage_Toolbar_PersonalTools__WEBPACK_IMPORTED_MODULE_84__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Toolbar_More__WEBPACK_IMPORTED_MODULE_85__ = __webpack_require__(/*! @plone/volto/components/manage/Toolbar/More */ "./node_modules/@plone/volto/src/components/manage/Toolbar/More.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "More", function() { return _plone_volto_components_manage_Toolbar_More__WEBPACK_IMPORTED_MODULE_85__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Toolbar_Types__WEBPACK_IMPORTED_MODULE_86__ = __webpack_require__(/*! @plone/volto/components/manage/Toolbar/Types */ "./node_modules/@plone/volto/src/components/manage/Toolbar/Types.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Types", function() { return _plone_volto_components_manage_Toolbar_Types__WEBPACK_IMPORTED_MODULE_86__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Toast_Toast__WEBPACK_IMPORTED_MODULE_87__ = __webpack_require__(/*! @plone/volto/components/manage/Toast/Toast */ "./node_modules/@plone/volto/src/components/manage/Toast/Toast.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Toast", function() { return _plone_volto_components_manage_Toast_Toast__WEBPACK_IMPORTED_MODULE_87__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Multilingual_ManageTranslations__WEBPACK_IMPORTED_MODULE_88__ = __webpack_require__(/*! @plone/volto/components/manage/Multilingual/ManageTranslations */ "./node_modules/@plone/volto/src/components/manage/Multilingual/ManageTranslations.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ManageTranslations", function() { return _plone_volto_components_manage_Multilingual_ManageTranslations__WEBPACK_IMPORTED_MODULE_88__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Form_Form__WEBPACK_IMPORTED_MODULE_89__ = __webpack_require__(/*! @plone/volto/components/manage/Form/Form */ "./node_modules/@plone/volto/src/components/manage/Form/Form.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Form", function() { return _plone_volto_components_manage_Form_Form__WEBPACK_IMPORTED_MODULE_89__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Form_BlocksToolbar__WEBPACK_IMPORTED_MODULE_90__ = __webpack_require__(/*! @plone/volto/components/manage/Form/BlocksToolbar */ "./node_modules/@plone/volto/src/components/manage/Form/BlocksToolbar.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "BlocksToolbar", function() { return _plone_volto_components_manage_Form_BlocksToolbar__WEBPACK_IMPORTED_MODULE_90__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Form_UndoToolbar__WEBPACK_IMPORTED_MODULE_91__ = __webpack_require__(/*! @plone/volto/components/manage/Form/UndoToolbar */ "./node_modules/@plone/volto/src/components/manage/Form/UndoToolbar.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "UndoToolbar", function() { return _plone_volto_components_manage_Form_UndoToolbar__WEBPACK_IMPORTED_MODULE_91__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Form_Field__WEBPACK_IMPORTED_MODULE_92__ = __webpack_require__(/*! @plone/volto/components/manage/Form/Field */ "./node_modules/@plone/volto/src/components/manage/Form/Field.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Field", function() { return _plone_volto_components_manage_Form_Field__WEBPACK_IMPORTED_MODULE_92__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Search_SearchTags__WEBPACK_IMPORTED_MODULE_93__ = __webpack_require__(/*! @plone/volto/components/theme/Search/SearchTags */ "./node_modules/@plone/volto/src/components/theme/Search/SearchTags.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "SearchTags", function() { return _plone_volto_components_theme_Search_SearchTags__WEBPACK_IMPORTED_MODULE_93__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Comments_CommentEditModal__WEBPACK_IMPORTED_MODULE_94__ = __webpack_require__(/*! @plone/volto/components/theme/Comments/CommentEditModal */ "./node_modules/@plone/volto/src/components/theme/Comments/CommentEditModal.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "CommentEditModal", function() { return _plone_volto_components_theme_Comments_CommentEditModal__WEBPACK_IMPORTED_MODULE_94__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Contents_ContentsBreadcrumbs__WEBPACK_IMPORTED_MODULE_95__ = __webpack_require__(/*! @plone/volto/components/manage/Contents/ContentsBreadcrumbs */ "./node_modules/@plone/volto/src/components/manage/Contents/ContentsBreadcrumbs.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ContentsBreadcrumbs", function() { return _plone_volto_components_manage_Contents_ContentsBreadcrumbs__WEBPACK_IMPORTED_MODULE_95__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Contents_ContentsIndexHeader__WEBPACK_IMPORTED_MODULE_96__ = __webpack_require__(/*! @plone/volto/components/manage/Contents/ContentsIndexHeader */ "./node_modules/@plone/volto/src/components/manage/Contents/ContentsIndexHeader.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ContentsIndexHeader", function() { return _plone_volto_components_manage_Contents_ContentsIndexHeader__WEBPACK_IMPORTED_MODULE_96__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Contents_ContentsItem__WEBPACK_IMPORTED_MODULE_97__ = __webpack_require__(/*! @plone/volto/components/manage/Contents/ContentsItem */ "./node_modules/@plone/volto/src/components/manage/Contents/ContentsItem.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ContentsItem", function() { return _plone_volto_components_manage_Contents_ContentsItem__WEBPACK_IMPORTED_MODULE_97__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Contents_ContentsUploadModal__WEBPACK_IMPORTED_MODULE_98__ = __webpack_require__(/*! @plone/volto/components/manage/Contents/ContentsUploadModal */ "./node_modules/@plone/volto/src/components/manage/Contents/ContentsUploadModal.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ContentsUploadModal", function() { return _plone_volto_components_manage_Contents_ContentsUploadModal__WEBPACK_IMPORTED_MODULE_98__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Contents_ContentsPropertiesModal__WEBPACK_IMPORTED_MODULE_99__ = __webpack_require__(/*! @plone/volto/components/manage/Contents/ContentsPropertiesModal */ "./node_modules/@plone/volto/src/components/manage/Contents/ContentsPropertiesModal.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ContentsPropertiesModal", function() { return _plone_volto_components_manage_Contents_ContentsPropertiesModal__WEBPACK_IMPORTED_MODULE_99__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Contents_ContentsRenameModal__WEBPACK_IMPORTED_MODULE_100__ = __webpack_require__(/*! @plone/volto/components/manage/Contents/ContentsRenameModal */ "./node_modules/@plone/volto/src/components/manage/Contents/ContentsRenameModal.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ContentsRenameModal", function() { return _plone_volto_components_manage_Contents_ContentsRenameModal__WEBPACK_IMPORTED_MODULE_100__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Contents_ContentsWorkflowModal__WEBPACK_IMPORTED_MODULE_101__ = __webpack_require__(/*! @plone/volto/components/manage/Contents/ContentsWorkflowModal */ "./node_modules/@plone/volto/src/components/manage/Contents/ContentsWorkflowModal.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ContentsWorkflowModal", function() { return _plone_volto_components_manage_Contents_ContentsWorkflowModal__WEBPACK_IMPORTED_MODULE_101__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Contents_ContentsTagsModal__WEBPACK_IMPORTED_MODULE_102__ = __webpack_require__(/*! @plone/volto/components/manage/Contents/ContentsTagsModal */ "./node_modules/@plone/volto/src/components/manage/Contents/ContentsTagsModal.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ContentsTagsModal", function() { return _plone_volto_components_manage_Contents_ContentsTagsModal__WEBPACK_IMPORTED_MODULE_102__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Controlpanels_Users_RenderUsers__WEBPACK_IMPORTED_MODULE_103__ = __webpack_require__(/*! @plone/volto/components/manage/Controlpanels/Users/RenderUsers */ "./node_modules/@plone/volto/src/components/manage/Controlpanels/Users/RenderUsers.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "RenderUsers", function() { return _plone_volto_components_manage_Controlpanels_Users_RenderUsers__WEBPACK_IMPORTED_MODULE_103__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Controlpanels_Groups_RenderGroups__WEBPACK_IMPORTED_MODULE_104__ = __webpack_require__(/*! @plone/volto/components/manage/Controlpanels/Groups/RenderGroups */ "./node_modules/@plone/volto/src/components/manage/Controlpanels/Groups/RenderGroups.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "RenderGroups", function() { return _plone_volto_components_manage_Controlpanels_Groups_RenderGroups__WEBPACK_IMPORTED_MODULE_104__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Diff_DiffField__WEBPACK_IMPORTED_MODULE_105__ = __webpack_require__(/*! @plone/volto/components/manage/Diff/DiffField */ "./node_modules/@plone/volto/src/components/manage/Diff/DiffField.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "DiffField", function() { return _plone_volto_components_manage_Diff_DiffField__WEBPACK_IMPORTED_MODULE_105__["default"]; });

/* harmony import */ var _plone_volto_components_manage_DragDropList_DragDropList__WEBPACK_IMPORTED_MODULE_106__ = __webpack_require__(/*! @plone/volto/components/manage/DragDropList/DragDropList */ "./node_modules/@plone/volto/src/components/manage/DragDropList/DragDropList.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "DragDropList", function() { return _plone_volto_components_manage_DragDropList_DragDropList__WEBPACK_IMPORTED_MODULE_106__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Form_InlineForm__WEBPACK_IMPORTED_MODULE_107__ = __webpack_require__(/*! @plone/volto/components/manage/Form/InlineForm */ "./node_modules/@plone/volto/src/components/manage/Form/InlineForm.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "InlineForm", function() { return _plone_volto_components_manage_Form_InlineForm__WEBPACK_IMPORTED_MODULE_107__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Block_BlocksForm__WEBPACK_IMPORTED_MODULE_108__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Block/BlocksForm */ "./node_modules/@plone/volto/src/components/manage/Blocks/Block/BlocksForm.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "BlocksForm", function() { return _plone_volto_components_manage_Blocks_Block_BlocksForm__WEBPACK_IMPORTED_MODULE_108__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Form_BlockDataForm__WEBPACK_IMPORTED_MODULE_109__ = __webpack_require__(/*! @plone/volto/components/manage/Form/BlockDataForm */ "./node_modules/@plone/volto/src/components/manage/Form/BlockDataForm.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "BlockDataForm", function() { return _plone_volto_components_manage_Form_BlockDataForm__WEBPACK_IMPORTED_MODULE_109__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Widgets_FormFieldWrapper__WEBPACK_IMPORTED_MODULE_110__ = __webpack_require__(/*! @plone/volto/components/manage/Widgets/FormFieldWrapper */ "./node_modules/@plone/volto/src/components/manage/Widgets/FormFieldWrapper.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "FormFieldWrapper", function() { return _plone_volto_components_manage_Widgets_FormFieldWrapper__WEBPACK_IMPORTED_MODULE_110__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Widgets_ArrayWidget__WEBPACK_IMPORTED_MODULE_111__ = __webpack_require__(/*! @plone/volto/components/manage/Widgets/ArrayWidget */ "./node_modules/@plone/volto/src/components/manage/Widgets/ArrayWidget.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ArrayWidget", function() { return _plone_volto_components_manage_Widgets_ArrayWidget__WEBPACK_IMPORTED_MODULE_111__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Widgets_CheckboxWidget__WEBPACK_IMPORTED_MODULE_112__ = __webpack_require__(/*! @plone/volto/components/manage/Widgets/CheckboxWidget */ "./node_modules/@plone/volto/src/components/manage/Widgets/CheckboxWidget.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "CheckboxWidget", function() { return _plone_volto_components_manage_Widgets_CheckboxWidget__WEBPACK_IMPORTED_MODULE_112__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Widgets_FileWidget__WEBPACK_IMPORTED_MODULE_113__ = __webpack_require__(/*! @plone/volto/components/manage/Widgets/FileWidget */ "./node_modules/@plone/volto/src/components/manage/Widgets/FileWidget.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "FileWidget", function() { return _plone_volto_components_manage_Widgets_FileWidget__WEBPACK_IMPORTED_MODULE_113__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Widgets_IdWidget__WEBPACK_IMPORTED_MODULE_114__ = __webpack_require__(/*! @plone/volto/components/manage/Widgets/IdWidget */ "./node_modules/@plone/volto/src/components/manage/Widgets/IdWidget.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "IdWidget", function() { return _plone_volto_components_manage_Widgets_IdWidget__WEBPACK_IMPORTED_MODULE_114__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Widgets_PasswordWidget__WEBPACK_IMPORTED_MODULE_115__ = __webpack_require__(/*! @plone/volto/components/manage/Widgets/PasswordWidget */ "./node_modules/@plone/volto/src/components/manage/Widgets/PasswordWidget.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "PasswordWidget", function() { return _plone_volto_components_manage_Widgets_PasswordWidget__WEBPACK_IMPORTED_MODULE_115__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Widgets_ReferenceWidget__WEBPACK_IMPORTED_MODULE_116__ = __webpack_require__(/*! @plone/volto/components/manage/Widgets/ReferenceWidget */ "./node_modules/@plone/volto/src/components/manage/Widgets/ReferenceWidget.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ReferenceWidget", function() { return _plone_volto_components_manage_Widgets_ReferenceWidget__WEBPACK_IMPORTED_MODULE_116__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Widgets_SchemaWidget__WEBPACK_IMPORTED_MODULE_117__ = __webpack_require__(/*! @plone/volto/components/manage/Widgets/SchemaWidget */ "./node_modules/@plone/volto/src/components/manage/Widgets/SchemaWidget.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "SchemaWidget", function() { return _plone_volto_components_manage_Widgets_SchemaWidget__WEBPACK_IMPORTED_MODULE_117__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Widgets_SchemaWidgetFieldset__WEBPACK_IMPORTED_MODULE_118__ = __webpack_require__(/*! @plone/volto/components/manage/Widgets/SchemaWidgetFieldset */ "./node_modules/@plone/volto/src/components/manage/Widgets/SchemaWidgetFieldset.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "SchemaWidgetFieldset", function() { return _plone_volto_components_manage_Widgets_SchemaWidgetFieldset__WEBPACK_IMPORTED_MODULE_118__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Widgets_SelectWidget__WEBPACK_IMPORTED_MODULE_119__ = __webpack_require__(/*! @plone/volto/components/manage/Widgets/SelectWidget */ "./node_modules/@plone/volto/src/components/manage/Widgets/SelectWidget.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "SelectWidget", function() { return _plone_volto_components_manage_Widgets_SelectWidget__WEBPACK_IMPORTED_MODULE_119__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Widgets_TextareaWidget__WEBPACK_IMPORTED_MODULE_120__ = __webpack_require__(/*! @plone/volto/components/manage/Widgets/TextareaWidget */ "./node_modules/@plone/volto/src/components/manage/Widgets/TextareaWidget.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "TextareaWidget", function() { return _plone_volto_components_manage_Widgets_TextareaWidget__WEBPACK_IMPORTED_MODULE_120__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Widgets_TextWidget__WEBPACK_IMPORTED_MODULE_121__ = __webpack_require__(/*! @plone/volto/components/manage/Widgets/TextWidget */ "./node_modules/@plone/volto/src/components/manage/Widgets/TextWidget.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "TextWidget", function() { return _plone_volto_components_manage_Widgets_TextWidget__WEBPACK_IMPORTED_MODULE_121__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Widgets_WysiwygWidget__WEBPACK_IMPORTED_MODULE_122__ = __webpack_require__(/*! @plone/volto/components/manage/Widgets/WysiwygWidget */ "./node_modules/@plone/volto/src/components/manage/Widgets/WysiwygWidget.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "WysiwygWidget", function() { return _plone_volto_components_manage_Widgets_WysiwygWidget__WEBPACK_IMPORTED_MODULE_122__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Widgets_ObjectBrowserWidget__WEBPACK_IMPORTED_MODULE_123__ = __webpack_require__(/*! @plone/volto/components/manage/Widgets/ObjectBrowserWidget */ "./node_modules/@plone/volto/src/components/manage/Widgets/ObjectBrowserWidget.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ObjectBrowserWidget", function() { return _plone_volto_components_manage_Widgets_ObjectBrowserWidget__WEBPACK_IMPORTED_MODULE_123__["default"]; });

/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ObjectBrowserWidgetMode", function() { return _plone_volto_components_manage_Widgets_ObjectBrowserWidget__WEBPACK_IMPORTED_MODULE_123__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Widgets_ObjectWidget__WEBPACK_IMPORTED_MODULE_124__ = __webpack_require__(/*! @plone/volto/components/manage/Widgets/ObjectWidget */ "./node_modules/@plone/volto/src/components/manage/Widgets/ObjectWidget.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ObjectWidget", function() { return _plone_volto_components_manage_Widgets_ObjectWidget__WEBPACK_IMPORTED_MODULE_124__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Widgets_ObjectListWidget__WEBPACK_IMPORTED_MODULE_125__ = __webpack_require__(/*! @plone/volto/components/manage/Widgets/ObjectListWidget */ "./node_modules/@plone/volto/src/components/manage/Widgets/ObjectListWidget.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ObjectListWidget", function() { return _plone_volto_components_manage_Widgets_ObjectListWidget__WEBPACK_IMPORTED_MODULE_125__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Description_Edit__WEBPACK_IMPORTED_MODULE_126__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Description/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/Description/Edit.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "EditDescriptionBlock", function() { return _plone_volto_components_manage_Blocks_Description_Edit__WEBPACK_IMPORTED_MODULE_126__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Title_Edit__WEBPACK_IMPORTED_MODULE_127__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Title/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/Title/Edit.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "EditTitleBlock", function() { return _plone_volto_components_manage_Blocks_Title_Edit__WEBPACK_IMPORTED_MODULE_127__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_ToC_Edit__WEBPACK_IMPORTED_MODULE_128__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/ToC/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/ToC/Edit.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "EditToCBlock", function() { return _plone_volto_components_manage_Blocks_ToC_Edit__WEBPACK_IMPORTED_MODULE_128__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Text_Edit__WEBPACK_IMPORTED_MODULE_129__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Text/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/Text/Edit.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "EditTextBlock", function() { return _plone_volto_components_manage_Blocks_Text_Edit__WEBPACK_IMPORTED_MODULE_129__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Image_Edit__WEBPACK_IMPORTED_MODULE_130__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Image/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/Image/Edit.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "EditImageBlock", function() { return _plone_volto_components_manage_Blocks_Image_Edit__WEBPACK_IMPORTED_MODULE_130__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Listing_Edit__WEBPACK_IMPORTED_MODULE_131__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Listing/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/Listing/Edit.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "EditListingBlock", function() { return _plone_volto_components_manage_Blocks_Listing_Edit__WEBPACK_IMPORTED_MODULE_131__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Video_Edit__WEBPACK_IMPORTED_MODULE_132__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Video/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/Video/Edit.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "EditVideoBlock", function() { return _plone_volto_components_manage_Blocks_Video_Edit__WEBPACK_IMPORTED_MODULE_132__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Block_Edit__WEBPACK_IMPORTED_MODULE_133__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Block/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/Block/Edit.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "EditBlock", function() { return _plone_volto_components_manage_Blocks_Block_Edit__WEBPACK_IMPORTED_MODULE_133__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_HeroImageLeft_Edit__WEBPACK_IMPORTED_MODULE_134__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/HeroImageLeft/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/HeroImageLeft/Edit.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "EditHeroImageLeftBlock", function() { return _plone_volto_components_manage_Blocks_HeroImageLeft_Edit__WEBPACK_IMPORTED_MODULE_134__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_HeroImageLeft_View__WEBPACK_IMPORTED_MODULE_135__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/HeroImageLeft/View */ "./node_modules/@plone/volto/src/components/manage/Blocks/HeroImageLeft/View.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ViewHeroImageLeftBlock", function() { return _plone_volto_components_manage_Blocks_HeroImageLeft_View__WEBPACK_IMPORTED_MODULE_135__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Maps_Edit__WEBPACK_IMPORTED_MODULE_136__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Maps/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/Maps/Edit.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "EditMapBlock", function() { return _plone_volto_components_manage_Blocks_Maps_Edit__WEBPACK_IMPORTED_MODULE_136__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_HTML_Edit__WEBPACK_IMPORTED_MODULE_137__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/HTML/Edit */ "./node_modules/@plone/volto/src/components/manage/Blocks/HTML/Edit.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "EditHTMLBlock", function() { return _plone_volto_components_manage_Blocks_HTML_Edit__WEBPACK_IMPORTED_MODULE_137__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Description_View__WEBPACK_IMPORTED_MODULE_138__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Description/View */ "./node_modules/@plone/volto/src/components/manage/Blocks/Description/View.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ViewDescriptionBlock", function() { return _plone_volto_components_manage_Blocks_Description_View__WEBPACK_IMPORTED_MODULE_138__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Title_View__WEBPACK_IMPORTED_MODULE_139__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Title/View */ "./node_modules/@plone/volto/src/components/manage/Blocks/Title/View.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ViewTitleBlock", function() { return _plone_volto_components_manage_Blocks_Title_View__WEBPACK_IMPORTED_MODULE_139__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_ToC_View__WEBPACK_IMPORTED_MODULE_140__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/ToC/View */ "./node_modules/@plone/volto/src/components/manage/Blocks/ToC/View.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ViewToCBlock", function() { return _plone_volto_components_manage_Blocks_ToC_View__WEBPACK_IMPORTED_MODULE_140__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Text_View__WEBPACK_IMPORTED_MODULE_141__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Text/View */ "./node_modules/@plone/volto/src/components/manage/Blocks/Text/View.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ViewTextBlock", function() { return _plone_volto_components_manage_Blocks_Text_View__WEBPACK_IMPORTED_MODULE_141__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Image_View__WEBPACK_IMPORTED_MODULE_142__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Image/View */ "./node_modules/@plone/volto/src/components/manage/Blocks/Image/View.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ViewImageBlock", function() { return _plone_volto_components_manage_Blocks_Image_View__WEBPACK_IMPORTED_MODULE_142__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Listing_View__WEBPACK_IMPORTED_MODULE_143__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Listing/View */ "./node_modules/@plone/volto/src/components/manage/Blocks/Listing/View.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ViewListingBlock", function() { return _plone_volto_components_manage_Blocks_Listing_View__WEBPACK_IMPORTED_MODULE_143__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Video_View__WEBPACK_IMPORTED_MODULE_144__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Video/View */ "./node_modules/@plone/volto/src/components/manage/Blocks/Video/View.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ViewVideoBlock", function() { return _plone_volto_components_manage_Blocks_Video_View__WEBPACK_IMPORTED_MODULE_144__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Maps_View__WEBPACK_IMPORTED_MODULE_145__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Maps/View */ "./node_modules/@plone/volto/src/components/manage/Blocks/Maps/View.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ViewMapBlock", function() { return _plone_volto_components_manage_Blocks_Maps_View__WEBPACK_IMPORTED_MODULE_145__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_HTML_View__WEBPACK_IMPORTED_MODULE_146__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/HTML/View */ "./node_modules/@plone/volto/src/components/manage/Blocks/HTML/View.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ViewHTMLBlock", function() { return _plone_volto_components_manage_Blocks_HTML_View__WEBPACK_IMPORTED_MODULE_146__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Listing_ListingBody__WEBPACK_IMPORTED_MODULE_147__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Listing/ListingBody */ "./node_modules/@plone/volto/src/components/manage/Blocks/Listing/ListingBody.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ListingBlockBody", function() { return _plone_volto_components_manage_Blocks_Listing_ListingBody__WEBPACK_IMPORTED_MODULE_147__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Listing_ListingData__WEBPACK_IMPORTED_MODULE_148__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Listing/ListingData */ "./node_modules/@plone/volto/src/components/manage/Blocks/Listing/ListingData.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ListingBlockData", function() { return _plone_volto_components_manage_Blocks_Listing_ListingData__WEBPACK_IMPORTED_MODULE_148__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Image_ImageSidebar__WEBPACK_IMPORTED_MODULE_149__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Image/ImageSidebar */ "./node_modules/@plone/volto/src/components/manage/Blocks/Image/ImageSidebar.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ImageSidebar", function() { return _plone_volto_components_manage_Blocks_Image_ImageSidebar__WEBPACK_IMPORTED_MODULE_149__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Maps_MapsSidebar__WEBPACK_IMPORTED_MODULE_150__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Maps/MapsSidebar */ "./node_modules/@plone/volto/src/components/manage/Blocks/Maps/MapsSidebar.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "MapsSidebar", function() { return _plone_volto_components_manage_Blocks_Maps_MapsSidebar__WEBPACK_IMPORTED_MODULE_150__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Video_VideoSidebar__WEBPACK_IMPORTED_MODULE_151__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Video/VideoSidebar */ "./node_modules/@plone/volto/src/components/manage/Blocks/Video/VideoSidebar.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "VideoSidebar", function() { return _plone_volto_components_manage_Blocks_Video_VideoSidebar__WEBPACK_IMPORTED_MODULE_151__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_LeadImage_LeadImageSidebar__WEBPACK_IMPORTED_MODULE_152__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/LeadImage/LeadImageSidebar */ "./node_modules/@plone/volto/src/components/manage/Blocks/LeadImage/LeadImageSidebar.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "LeadImageSidebar", function() { return _plone_volto_components_manage_Blocks_LeadImage_LeadImageSidebar__WEBPACK_IMPORTED_MODULE_152__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Block_Style__WEBPACK_IMPORTED_MODULE_153__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Block/Style */ "./node_modules/@plone/volto/src/components/manage/Blocks/Block/Style.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Style", function() { return _plone_volto_components_manage_Blocks_Block_Style__WEBPACK_IMPORTED_MODULE_153__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Block_Settings__WEBPACK_IMPORTED_MODULE_154__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Block/Settings */ "./node_modules/@plone/volto/src/components/manage/Blocks/Block/Settings.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "BlockSettingsSidebar", function() { return _plone_volto_components_manage_Blocks_Block_Settings__WEBPACK_IMPORTED_MODULE_154__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Block_Schema__WEBPACK_IMPORTED_MODULE_155__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Block/Schema */ "./node_modules/@plone/volto/src/components/manage/Blocks/Block/Schema.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "BlockSettingsSchema", function() { return _plone_volto_components_manage_Blocks_Block_Schema__WEBPACK_IMPORTED_MODULE_155__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Text_Schema__WEBPACK_IMPORTED_MODULE_156__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Text/Schema */ "./node_modules/@plone/volto/src/components/manage/Blocks/Text/Schema.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "TextSettingsSchema", function() { return _plone_volto_components_manage_Blocks_Text_Schema__WEBPACK_IMPORTED_MODULE_156__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_Image_Schema__WEBPACK_IMPORTED_MODULE_157__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/Image/Schema */ "./node_modules/@plone/volto/src/components/manage/Blocks/Image/Schema.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ImageSettingsSchema", function() { return _plone_volto_components_manage_Blocks_Image_Schema__WEBPACK_IMPORTED_MODULE_157__["default"]; });

/* harmony import */ var _plone_volto_components_manage_Blocks_ToC_Schema__WEBPACK_IMPORTED_MODULE_158__ = __webpack_require__(/*! @plone/volto/components/manage/Blocks/ToC/Schema */ "./node_modules/@plone/volto/src/components/manage/Blocks/ToC/Schema.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ToCSettingsSchema", function() { return _plone_volto_components_manage_Blocks_ToC_Schema__WEBPACK_IMPORTED_MODULE_158__["default"]; });

/* harmony import */ var _plone_volto_components_manage_MaybeWrap_MaybeWrap__WEBPACK_IMPORTED_MODULE_159__ = __webpack_require__(/*! @plone/volto/components/manage/MaybeWrap/MaybeWrap */ "./node_modules/@plone/volto/src/components/manage/MaybeWrap/MaybeWrap.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "MaybeWrap", function() { return _plone_volto_components_manage_MaybeWrap_MaybeWrap__WEBPACK_IMPORTED_MODULE_159__["default"]; });

/* harmony import */ var _plone_volto_components_theme_ContentMetadataTags_ContentMetadataTags__WEBPACK_IMPORTED_MODULE_160__ = __webpack_require__(/*! @plone/volto/components/theme/ContentMetadataTags/ContentMetadataTags */ "./node_modules/@plone/volto/src/components/theme/ContentMetadataTags/ContentMetadataTags.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "ContentMetadataTags", function() { return _plone_volto_components_theme_ContentMetadataTags_ContentMetadataTags__WEBPACK_IMPORTED_MODULE_160__["default"]; });

/* harmony import */ var _plone_volto_components_theme_FormattedDate_FormattedDate__WEBPACK_IMPORTED_MODULE_161__ = __webpack_require__(/*! @plone/volto/components/theme/FormattedDate/FormattedDate */ "./node_modules/@plone/volto/src/components/theme/FormattedDate/FormattedDate.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "FormattedDate", function() { return _plone_volto_components_theme_FormattedDate_FormattedDate__WEBPACK_IMPORTED_MODULE_161__["default"]; });

/* harmony import */ var _plone_volto_components_theme_FormattedDate_FormattedRelativeDate__WEBPACK_IMPORTED_MODULE_162__ = __webpack_require__(/*! @plone/volto/components/theme/FormattedDate/FormattedRelativeDate */ "./node_modules/@plone/volto/src/components/theme/FormattedDate/FormattedRelativeDate.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "FormattedRelativeDate", function() { return _plone_volto_components_theme_FormattedDate_FormattedRelativeDate__WEBPACK_IMPORTED_MODULE_162__["default"]; });

/* harmony import */ var _plone_volto_components_theme_Component_Component__WEBPACK_IMPORTED_MODULE_163__ = __webpack_require__(/*! @plone/volto/components/theme/Component/Component */ "./node_modules/@plone/volto/src/components/theme/Component/Component.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "Component", function() { return _plone_volto_components_theme_Component_Component__WEBPACK_IMPORTED_MODULE_163__["default"]; });

/* harmony import */ var _plone_volto_components_theme_App_App__WEBPACK_IMPORTED_MODULE_164__ = __webpack_require__(/*! @plone/volto/components/theme/App/App */ "./node_modules/@plone/volto/src/components/theme/App/App.jsx");
/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, "App", function() { return _plone_volto_components_theme_App_App__WEBPACK_IMPORTED_MODULE_164__["default"]; });

/**
 * Point of contact for component modules. This file is quite sensitive regarding the
 * order in which it's loaded. e.g. if the component depends on others to work, it
 * should ideally be loaded after them. If you start seeing imported components as
 * undefined, check the order of imports in this file.
 * @module components
 */
 //  Do not lazy load them, since it has not much sense (they will live in the main chunk)
// The App and View component are deliberatelly left out of this index.js file!
// They should be used by Volto and only by Volto internally






















































 // Lazy load them, since we want them and its deps to be in its own chunk







































const EventView = _loadable_component__WEBPACK_IMPORTED_MODULE_0___default()({
  resolved: {},

  chunkName() {
    return "plone-volto-components-theme-View-EventView";
  },

  isReady(props) {
    const key = this.resolve(props);

    if (this.resolved[key] !== true) {
      return false;
    }

    if (true) {
      return !!__webpack_require__.m[key];
    }

    return false;
  },

  importAsync: () => __webpack_require__.e(/*! import() | plone-volto-components-theme-View-EventView */ "plone-volto-components-theme-View-EventView").then(__webpack_require__.bind(null, /*! @plone/volto/components/theme/View/EventView */ "./node_modules/@plone/volto/src/components/theme/View/EventView.jsx")),

  requireAsync(props) {
    const key = this.resolve(props);
    this.resolved[key] = false;
    return this.importAsync(props).then(resolved => {
      this.resolved[key] = true;
      return resolved;
    });
  },

  requireSync(props) {
    const id = this.resolve(props);

    if (true) {
      return __webpack_require__(id);
    }

    return eval('module.require')(id);
  },

  resolve() {
    if (true) {
      return /*require.resolve*/(/*! @plone/volto/components/theme/View/EventView */ "./node_modules/@plone/volto/src/components/theme/View/EventView.jsx");
    }

    return eval('require.resolve')("@plone/volto/components/theme/View/EventView");
  }

});



















































































 // Potentially could ve removed from index, since they are internal components and
// we don't want them to end up in the main chunk

















































const DatetimeWidget = _loadable_component__WEBPACK_IMPORTED_MODULE_0___default()({
  resolved: {},

  chunkName() {
    return "plone-volto-components-manage-Widgets-DatetimeWidget";
  },

  isReady(props) {
    const key = this.resolve(props);

    if (this.resolved[key] !== true) {
      return false;
    }

    if (true) {
      return !!__webpack_require__.m[key];
    }

    return false;
  },

  importAsync: () => __webpack_require__.e(/*! import() | plone-volto-components-manage-Widgets-DatetimeWidget */ "vendors~plone-volto-components-manage-Widgets-DatetimeWidget~plone-volto-components-manage-Widgets-R~a875f490").then(__webpack_require__.bind(null, /*! @plone/volto/components/manage/Widgets/DatetimeWidget */ "./node_modules/@plone/volto/src/components/manage/Widgets/DatetimeWidget.jsx")),

  requireAsync(props) {
    const key = this.resolve(props);
    this.resolved[key] = false;
    return this.importAsync(props).then(resolved => {
      this.resolved[key] = true;
      return resolved;
    });
  },

  requireSync(props) {
    const id = this.resolve(props);

    if (true) {
      return __webpack_require__(id);
    }

    return eval('module.require')(id);
  },

  resolve() {
    if (true) {
      return /*require.resolve*/(/*! @plone/volto/components/manage/Widgets/DatetimeWidget */ "./node_modules/@plone/volto/src/components/manage/Widgets/DatetimeWidget.jsx");
    }

    return eval('require.resolve')("@plone/volto/components/manage/Widgets/DatetimeWidget");
  }

});
const RecurrenceWidget = _loadable_component__WEBPACK_IMPORTED_MODULE_0___default()({
  resolved: {},

  chunkName() {
    return "plone-volto-components-manage-Widgets-RecurrenceWidget-RecurrenceWidget";
  },

  isReady(props) {
    const key = this.resolve(props);

    if (this.resolved[key] !== true) {
      return false;
    }

    if (true) {
      return !!__webpack_require__.m[key];
    }

    return false;
  },

  importAsync: () => Promise.all(/*! import() | plone-volto-components-manage-Widgets-RecurrenceWidget-RecurrenceWidget */[__webpack_require__.e("vendors~plone-volto-components-manage-Widgets-DatetimeWidget~plone-volto-components-manage-Widgets-R~a875f490"), __webpack_require__.e("vendors~plone-volto-components-manage-Widgets-RecurrenceWidget-RecurrenceWidget")]).then(__webpack_require__.bind(null, /*! @plone/volto/components/manage/Widgets/RecurrenceWidget/RecurrenceWidget */ "./node_modules/@plone/volto/src/components/manage/Widgets/RecurrenceWidget/RecurrenceWidget.jsx")),

  requireAsync(props) {
    const key = this.resolve(props);
    this.resolved[key] = false;
    return this.importAsync(props).then(resolved => {
      this.resolved[key] = true;
      return resolved;
    });
  },

  requireSync(props) {
    const id = this.resolve(props);

    if (true) {
      return __webpack_require__(id);
    }

    return eval('module.require')(id);
  },

  resolve() {
    if (true) {
      return /*require.resolve*/(/*! @plone/volto/components/manage/Widgets/RecurrenceWidget/RecurrenceWidget */ "./node_modules/@plone/volto/src/components/manage/Widgets/RecurrenceWidget/RecurrenceWidget.jsx");
    }

    return eval('require.resolve')("@plone/volto/components/manage/Widgets/RecurrenceWidget/RecurrenceWidget");
  }

});











































































































/***/ }),

/***/ "./node_modules/@plone/volto/src/components/manage/LockingToastsFactory/LockingToastsFactory.jsx":
/*!*******************************************************************************************************!*\
  !*** ./node_modules/@plone/volto/src/components/manage/LockingToastsFactory/LockingToastsFactory.jsx ***!
  \*******************************************************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_toastify__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react-toastify */ "react-toastify");
/* harmony import */ var react_toastify__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react_toastify__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react-redux */ "react-redux");
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(react_redux__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-router-dom */ "react-router-dom");
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react_router_dom__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react-intl */ "react-intl");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react_intl__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var date_fns__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! date-fns */ "date-fns");
/* harmony import */ var date_fns__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(date_fns__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var use_deep_compare_effect__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! use-deep-compare-effect */ "use-deep-compare-effect");
/* harmony import */ var use_deep_compare_effect__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(use_deep_compare_effect__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_8__);
var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/node_modules/@plone/volto/src/components/manage/LockingToastsFactory/LockingToastsFactory.jsx";
 // import { Link } from 'react-router-dom';





 // import { flattenToAppURL } from '@plone/volto/helpers';




const messages = Object(react_intl__WEBPACK_IMPORTED_MODULE_4__["defineMessages"])({
  thisItemIsLocked: {
    "id": "This item was locked by {creator} on {date}",
    "defaultMessage": "This item was locked by {creator} on {date}"
  },
  unlockItem: {
    "id": "If you are certain this user has abandoned the object, you may unlock the object. You will then be able to edit it.",
    "defaultMessage": "If you are certain this user has abandoned the object, you may unlock the object. You will then be able to edit it."
  }
});

const LockingToastsFactory = props => {
  const intl = Object(react_intl__WEBPACK_IMPORTED_MODULE_4__["useIntl"])();
  const pathname = Object(react_router_dom__WEBPACK_IMPORTED_MODULE_3__["useLocation"])().pathname;
  const lang = Object(react_redux__WEBPACK_IMPORTED_MODULE_2__["useSelector"])(state => state.intl.locale);
  const {
    content,
    user
  } = props;
  const lock = content === null || content === void 0 ? void 0 : content.lock;
  const creator = (lock === null || lock === void 0 ? void 0 : lock.creator_name) || (lock === null || lock === void 0 ? void 0 : lock.creator) || ''; // const creator_url = locking?.creator_url || '';

  const date = (lock === null || lock === void 0 ? void 0 : lock.created) || '';
  const dateOptions = {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: 'numeric',
    minute: 'numeric'
  };
  use_deep_compare_effect__WEBPACK_IMPORTED_MODULE_7___default()(() => {
    if (user && content) {
      if (lock !== null && lock !== void 0 && lock.locked && lock !== null && lock !== void 0 && lock.stealable && (lock === null || lock === void 0 ? void 0 : lock.creator) !== user) {
        if (react_toastify__WEBPACK_IMPORTED_MODULE_1__["toast"].isActive('lockinginfo')) {
          react_toastify__WEBPACK_IMPORTED_MODULE_1__["toast"].update('lockinginfo', {
            render: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_8__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_5__["Toast"], {
              info: true,
              title: intl.formatMessage(messages.thisItemIsLocked, {
                creator: creator,
                date: new Intl.DateTimeFormat(lang, dateOptions).format(Object(date_fns__WEBPACK_IMPORTED_MODULE_6__["parse"])(date))
              }),
              content: intl.formatMessage(messages.unlockItem, {})
            })
          });
        } else {
          react_toastify__WEBPACK_IMPORTED_MODULE_1__["toast"].info( /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_8__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_5__["Toast"], {
            info: true,
            title: intl.formatMessage(messages.thisItemIsLocked, {
              creator: creator,
              date: new Intl.DateTimeFormat(lang, dateOptions).format(Object(date_fns__WEBPACK_IMPORTED_MODULE_6__["parse"])(date))
            }),
            content: intl.formatMessage(messages.unlockItem, {})
          }), {
            toastId: 'lockinginfo',
            autoClose: false,
            closeButton: false,
            transition: null
          });
        }
      } else {
        if (react_toastify__WEBPACK_IMPORTED_MODULE_1__["toast"].isActive('lockinginfo')) {
          react_toastify__WEBPACK_IMPORTED_MODULE_1__["toast"].dismiss('lockinginfo');
        }
      }
    }
  }, [content, creator, date, dateOptions, intl, lang, lock, pathname, user]);
  return null;
};

/* harmony default export */ __webpack_exports__["default"] = (LockingToastsFactory);

/***/ }),

/***/ "./node_modules/@plone/volto/src/components/manage/WorkingCopyToastsFactory/WorkingCopyToastsFactory.jsx":
/*!***************************************************************************************************************!*\
  !*** ./node_modules/@plone/volto/src/components/manage/WorkingCopyToastsFactory/WorkingCopyToastsFactory.jsx ***!
  \***************************************************************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react-router-dom */ "react-router-dom");
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react_router_dom__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var react_toastify__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react-toastify */ "react-toastify");
/* harmony import */ var react_toastify__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(react_toastify__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-redux */ "react-redux");
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react_redux__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react-intl */ "react-intl");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react_intl__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var date_fns__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! date-fns */ "date-fns");
/* harmony import */ var date_fns__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(date_fns__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _plone_volto_registry__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @plone/volto/registry */ "./node_modules/@plone/volto/src/registry.js");
/* harmony import */ var use_deep_compare_effect__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! use-deep-compare-effect */ "use-deep-compare-effect");
/* harmony import */ var use_deep_compare_effect__WEBPACK_IMPORTED_MODULE_9___default = /*#__PURE__*/__webpack_require__.n(use_deep_compare_effect__WEBPACK_IMPORTED_MODULE_9__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__);
var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/node_modules/@plone/volto/src/components/manage/WorkingCopyToastsFactory/WorkingCopyToastsFactory.jsx";












const messages = Object(react_intl__WEBPACK_IMPORTED_MODULE_4__["defineMessages"])({
  thisIsAWorkingCopyOf: {
    "id": "This is a working copy of {title}",
    "defaultMessage": "This is a working copy of {title}"
  },
  workingCopyIs: {
    "id": "This has an ongoing working copy in {title}",
    "defaultMessage": "This has an ongoing working copy in {title}"
  },
  workingCopyCreatedBy: {
    "id": "Created by {creator} on {date}",
    "defaultMessage": "Created by {creator} on {date}"
  }
});

const WorkingCopyToastsFactory = props => {
  const intl = Object(react_intl__WEBPACK_IMPORTED_MODULE_4__["useIntl"])();
  const pathname = Object(react_router_dom__WEBPACK_IMPORTED_MODULE_1__["useLocation"])().pathname;
  const lang = Object(react_redux__WEBPACK_IMPORTED_MODULE_3__["useSelector"])(state => state.intl.locale);
  const {
    content
  } = props;
  const title = content === null || content === void 0 ? void 0 : content.title;
  const working_copy = content === null || content === void 0 ? void 0 : content.working_copy;
  const dateOptions = {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  };
  use_deep_compare_effect__WEBPACK_IMPORTED_MODULE_9___default()(() => {
    if (content && _plone_volto_registry__WEBPACK_IMPORTED_MODULE_8__["default"].settings.hasWorkingCopySupport) {
      if (working_copy) {
        let toastMessage, toastTitle;

        if (content.working_copy_of) {
          var _content$working_copy;

          // I'm a working copy
          toastMessage = messages.thisIsAWorkingCopyOf;
          toastTitle = /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])(react_router_dom__WEBPACK_IMPORTED_MODULE_1__["Link"], {
            to: Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["flattenToAppURL"])(content.working_copy_of['@id']),
            children: (_content$working_copy = content.working_copy_of) === null || _content$working_copy === void 0 ? void 0 : _content$working_copy.title
          });
        } else {
          // I'm a baseline
          toastMessage = messages.workingCopyIs;
          toastTitle = /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])(react_router_dom__WEBPACK_IMPORTED_MODULE_1__["Link"], {
            to: Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["flattenToAppURL"])(working_copy['@id']),
            children: working_copy === null || working_copy === void 0 ? void 0 : working_copy.title
          });
        }

        if (react_toastify__WEBPACK_IMPORTED_MODULE_2__["toast"].isActive('workingcopyinfo')) {
          react_toastify__WEBPACK_IMPORTED_MODULE_2__["toast"].update('workingcopyinfo', {
            render: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_5__["Toast"], {
              info: true,
              title: intl.formatMessage(toastMessage, {
                title: toastTitle
              }),
              content: intl.formatMessage(messages.workingCopyCreatedBy, {
                creator: working_copy === null || working_copy === void 0 ? void 0 : working_copy.creator_name,
                date: new Intl.DateTimeFormat(lang, dateOptions).format(Object(date_fns__WEBPACK_IMPORTED_MODULE_7__["parse"])(working_copy === null || working_copy === void 0 ? void 0 : working_copy.created))
              })
            })
          });
        } else {
          react_toastify__WEBPACK_IMPORTED_MODULE_2__["toast"].info( /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_10__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_5__["Toast"], {
            info: true,
            title: intl.formatMessage(toastMessage, {
              title: toastTitle
            }),
            content: intl.formatMessage(messages.workingCopyCreatedBy, {
              creator: working_copy === null || working_copy === void 0 ? void 0 : working_copy.creator_name,
              date: new Intl.DateTimeFormat(lang, dateOptions).format(Object(date_fns__WEBPACK_IMPORTED_MODULE_7__["parse"])(working_copy === null || working_copy === void 0 ? void 0 : working_copy.created))
            })
          }), {
            toastId: 'workingcopyinfo',
            autoClose: false,
            closeButton: false,
            transition: null
          });
        }
      }

      if (!working_copy) {
        if (react_toastify__WEBPACK_IMPORTED_MODULE_2__["toast"].isActive('workingcopyinfo')) {
          react_toastify__WEBPACK_IMPORTED_MODULE_2__["toast"].dismiss('workingcopyinfo');
        }
      }
    }
  }, [pathname, content, title, working_copy, intl, lang, dateOptions]);
  return null;
};

/* harmony default export */ __webpack_exports__["default"] = (WorkingCopyToastsFactory);

/***/ }),

/***/ "./node_modules/@plone/volto/src/components/theme/App/App.jsx":
/*!********************************************************************!*\
  !*** ./node_modules/@plone/volto/src/components/theme/App/App.jsx ***!
  \********************************************************************/
/*! exports provided: __test__, fetchContent, default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "__test__", function() { return __test__; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "fetchContent", function() { return fetchContent; });
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/defineProperty */ "@babel/runtime/helpers/defineProperty");
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var jwt_decode__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! jwt-decode */ "jwt-decode");
/* harmony import */ var jwt_decode__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(jwt_decode__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! prop-types */ "prop-types");
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(prop_types__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react-redux */ "react-redux");
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react_redux__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var redux__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! redux */ "redux");
/* harmony import */ var redux__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(redux__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! semantic-ui-react */ "semantic-ui-react");
/* harmony import */ var semantic_ui_react__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(semantic_ui_react__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var react_router_config__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! react-router-config */ "react-router-config");
/* harmony import */ var react_router_config__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(react_router_config__WEBPACK_IMPORTED_MODULE_8__);
/* harmony import */ var react_toastify__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! react-toastify */ "react-toastify");
/* harmony import */ var react_toastify__WEBPACK_IMPORTED_MODULE_9___default = /*#__PURE__*/__webpack_require__.n(react_toastify__WEBPACK_IMPORTED_MODULE_9__);
/* harmony import */ var lodash_split__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! lodash/split */ "lodash/split");
/* harmony import */ var lodash_split__WEBPACK_IMPORTED_MODULE_10___default = /*#__PURE__*/__webpack_require__.n(lodash_split__WEBPACK_IMPORTED_MODULE_10__);
/* harmony import */ var lodash_join__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! lodash/join */ "lodash/join");
/* harmony import */ var lodash_join__WEBPACK_IMPORTED_MODULE_11___default = /*#__PURE__*/__webpack_require__.n(lodash_join__WEBPACK_IMPORTED_MODULE_11__);
/* harmony import */ var lodash_trim__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! lodash/trim */ "lodash/trim");
/* harmony import */ var lodash_trim__WEBPACK_IMPORTED_MODULE_12___default = /*#__PURE__*/__webpack_require__.n(lodash_trim__WEBPACK_IMPORTED_MODULE_12__);
/* harmony import */ var classnames__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! classnames */ "classnames");
/* harmony import */ var classnames__WEBPACK_IMPORTED_MODULE_13___default = /*#__PURE__*/__webpack_require__.n(classnames__WEBPACK_IMPORTED_MODULE_13__);
/* harmony import */ var _plone_volto_registry__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! @plone/volto/registry */ "./node_modules/@plone/volto/src/registry.js");
/* harmony import */ var _plone_volto_components_manage_Pluggable__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! @plone/volto/components/manage/Pluggable */ "./node_modules/@plone/volto/src/components/manage/Pluggable/index.js");
/* harmony import */ var _plone_volto_helpers_Blocks_Blocks__WEBPACK_IMPORTED_MODULE_16__ = __webpack_require__(/*! @plone/volto/helpers/Blocks/Blocks */ "./node_modules/@plone/volto/src/helpers/Blocks/Blocks.js");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_17__ = __webpack_require__(/*! react-intl */ "react-intl");
/* harmony import */ var react_intl__WEBPACK_IMPORTED_MODULE_17___default = /*#__PURE__*/__webpack_require__.n(react_intl__WEBPACK_IMPORTED_MODULE_17__);
/* harmony import */ var _plone_volto_error__WEBPACK_IMPORTED_MODULE_18__ = __webpack_require__(/*! @plone/volto/error */ "./node_modules/@plone/volto/src/error.jsx");
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_19__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var _plone_volto_actions__WEBPACK_IMPORTED_MODULE_20__ = __webpack_require__(/*! @plone/volto/actions */ "./node_modules/@plone/volto/src/actions/index.js");
/* harmony import */ var _plone_volto_icons_clear_svg__WEBPACK_IMPORTED_MODULE_21__ = __webpack_require__(/*! @plone/volto/icons/clear.svg */ "./node_modules/@plone/volto/src/icons/clear.svg");
/* harmony import */ var _plone_volto_icons_clear_svg__WEBPACK_IMPORTED_MODULE_21___default = /*#__PURE__*/__webpack_require__.n(_plone_volto_icons_clear_svg__WEBPACK_IMPORTED_MODULE_21__);
/* harmony import */ var _plone_volto_components_theme_MultilingualRedirector_MultilingualRedirector__WEBPACK_IMPORTED_MODULE_22__ = __webpack_require__(/*! @plone/volto/components/theme/MultilingualRedirector/MultilingualRedirector */ "./node_modules/@plone/volto/src/components/theme/MultilingualRedirector/MultilingualRedirector.jsx");
/* harmony import */ var _plone_volto_components_manage_WorkingCopyToastsFactory_WorkingCopyToastsFactory__WEBPACK_IMPORTED_MODULE_23__ = __webpack_require__(/*! @plone/volto/components/manage/WorkingCopyToastsFactory/WorkingCopyToastsFactory */ "./node_modules/@plone/volto/src/components/manage/WorkingCopyToastsFactory/WorkingCopyToastsFactory.jsx");
/* harmony import */ var _plone_volto_components_manage_LockingToastsFactory_LockingToastsFactory__WEBPACK_IMPORTED_MODULE_24__ = __webpack_require__(/*! @plone/volto/components/manage/LockingToastsFactory/LockingToastsFactory */ "./node_modules/@plone/volto/src/components/manage/LockingToastsFactory/LockingToastsFactory.jsx");
/* harmony import */ var _sentry_browser__WEBPACK_IMPORTED_MODULE_25__ = __webpack_require__(/*! @sentry/browser */ "@sentry/browser");
/* harmony import */ var _sentry_browser__WEBPACK_IMPORTED_MODULE_25___default = /*#__PURE__*/__webpack_require__.n(_sentry_browser__WEBPACK_IMPORTED_MODULE_25__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__);

var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/node_modules/@plone/volto/src/components/theme/App/App.jsx";

function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); if (enumerableOnly) { symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; }); } keys.push.apply(keys, symbols); } return keys; }

function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i] != null ? arguments[i] : {}; if (i % 2) { ownKeys(Object(source), true).forEach(function (key) { _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(target, key, source[key]); }); } else if (Object.getOwnPropertyDescriptors) { Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)); } else { ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } } return target; }

/**
 * App container.
 * @module components/theme/App/App
 */


























/**
 * @export
 * @class App
 * @extends {Component}
 */




class App extends react__WEBPACK_IMPORTED_MODULE_1__["Component"] {
  constructor(...args) {
    super(...args);

    _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(this, "state", {
      hasError: false,
      error: null,
      errorInfo: null
    });
  }

  /**
   * @method componentWillReceiveProps
   * @param {Object} nextProps Next properties
   * @returns {undefined}
   */
  UNSAFE_componentWillReceiveProps(nextProps) {
    if (nextProps.pathname !== this.props.pathname) {
      if (this.state.hasError) {
        this.setState({
          hasError: false
        });
      }
    }
  }
  /**
   * ComponentDidCatch
   * @method ComponentDidCatch
   * @param {string} error  The error
   * @param {string} info The info
   * @returns {undefined}
   */


  componentDidCatch(error, info) {
    this.setState({
      hasError: true,
      error,
      errorInfo: info
    });

    if (false) { var _window, _window$env, _SENTRY__; }
  }
  /**
   * Render method.
   * @method render
   * @returns {string} Markup for the component.
   */


  render() {
    var _this$props$content$l, _this$props$content, _this$props$content$l2, _this$props$intl, _this$props$content2, _this$props$content2$;

    const {
      views
    } = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_14__["default"];
    const path = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["getBaseUrl"])(this.props.pathname);
    const action = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["getView"])(this.props.pathname);
    const isCmsUI = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["isCmsUi"])(this.props.pathname);
    const ConnectionRefusedView = views.errorViews.ECONNREFUSED;
    const language = (_this$props$content$l = (_this$props$content = this.props.content) === null || _this$props$content === void 0 ? void 0 : (_this$props$content$l2 = _this$props$content.language) === null || _this$props$content$l2 === void 0 ? void 0 : _this$props$content$l2.token) !== null && _this$props$content$l !== void 0 ? _this$props$content$l : (_this$props$intl = this.props.intl) === null || _this$props$intl === void 0 ? void 0 : _this$props$intl.locale;
    return /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsxs"])(_plone_volto_components_manage_Pluggable__WEBPACK_IMPORTED_MODULE_15__["PluggablesProvider"], {
      children: [language && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["Helmet"], {
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])("html", {
          lang: language
        })
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["BodyClass"], {
        className: `view-${action}view`
      }), this.props.content && this.props.content['@type'] && /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["BodyClass"], {
        className: `contenttype-${this.props.content['@type'].replace(' ', '-').toLowerCase()}`
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["BodyClass"], {
        className: classnames__WEBPACK_IMPORTED_MODULE_13___default()({
          [lodash_trim__WEBPACK_IMPORTED_MODULE_12___default()(lodash_join__WEBPACK_IMPORTED_MODULE_11___default()(lodash_split__WEBPACK_IMPORTED_MODULE_10___default()(this.props.pathname, '/'), ' section-'))]: this.props.pathname !== '/',
          siteroot: this.props.pathname === '/',
          'is-authenticated': !!this.props.token,
          'is-anonymous': !this.props.token,
          'cms-ui': isCmsUI,
          'public-ui': !isCmsUI
        })
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_19__["SkipLinks"], {}), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_19__["Header"], {
        pathname: path
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_19__["Breadcrumbs"], {
        pathname: path
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_components_theme_MultilingualRedirector_MultilingualRedirector__WEBPACK_IMPORTED_MODULE_22__["default"], {
        pathname: this.props.pathname,
        contentLanguage: (_this$props$content2 = this.props.content) === null || _this$props$content2 === void 0 ? void 0 : (_this$props$content2$ = _this$props$content2.language) === null || _this$props$content2$ === void 0 ? void 0 : _this$props$content2$.token,
        children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(semantic_ui_react__WEBPACK_IMPORTED_MODULE_7__["Segment"], {
          basic: true,
          className: "content-area",
          children: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsxs"])("main", {
            children: [/*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_19__["OutdatedBrowser"], {}), this.props.connectionRefused ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(ConnectionRefusedView, {}) : this.state.hasError ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_error__WEBPACK_IMPORTED_MODULE_18__["default"], {
              message: this.state.error.message,
              stackTrace: this.state.errorInfo.componentStack
            }) : Object(react_router_config__WEBPACK_IMPORTED_MODULE_8__["renderRoutes"])(this.props.route.routes, {
              staticContext: this.props.staticContext
            })]
          })
        })
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_19__["Footer"], {}), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_components_manage_LockingToastsFactory_LockingToastsFactory__WEBPACK_IMPORTED_MODULE_24__["default"], {
        content: this.props.content,
        user: this.props.userId
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_components_manage_WorkingCopyToastsFactory_WorkingCopyToastsFactory__WEBPACK_IMPORTED_MODULE_23__["default"], {
        content: this.props.content
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(react_toastify__WEBPACK_IMPORTED_MODULE_9__["ToastContainer"], {
        position: react_toastify__WEBPACK_IMPORTED_MODULE_9__["toast"].POSITION.BOTTOM_CENTER,
        hideProgressBar: true,
        transition: react_toastify__WEBPACK_IMPORTED_MODULE_9__["Slide"],
        autoClose: 5000,
        closeButton: /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_19__["Icon"], {
          className: "toast-dismiss-action",
          name: _plone_volto_icons_clear_svg__WEBPACK_IMPORTED_MODULE_21___default.a,
          size: "18px"
        })
      }), /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_26__["jsx"])(_plone_volto_components__WEBPACK_IMPORTED_MODULE_19__["AppExtras"], _objectSpread({}, this.props))]
    });
  }

}

_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(App, "propTypes", {
  pathname: prop_types__WEBPACK_IMPORTED_MODULE_3___default.a.string.isRequired
});

const __test__ = Object(react_redux__WEBPACK_IMPORTED_MODULE_4__["connect"])((state, props) => ({
  pathname: props.location.pathname,
  token: state.userSession.token,
  content: state.content.data,
  apiError: state.apierror.error,
  connectionRefused: state.apierror.connectionRefused
}), {})(App);
const fetchContent = async ({
  store,
  location
}) => {
  const content = await store.dispatch(Object(_plone_volto_actions__WEBPACK_IMPORTED_MODULE_20__["getContent"])(Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["getBaseUrl"])(location.pathname)));
  const promises = [];
  const {
    blocksConfig
  } = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_14__["default"].blocks;

  const visitor = ([id, data]) => {
    const blockType = data['@type'];
    const {
      getAsyncData
    } = blocksConfig[blockType];

    if (getAsyncData) {
      const p = getAsyncData({
        store,
        dispatch: store.dispatch,
        path: location.pathname,
        location,
        id,
        data
      });

      if (!(p !== null && p !== void 0 && p.length)) {
        throw new _plone_volto_error__WEBPACK_IMPORTED_MODULE_18__["default"]('You should return a list of promises from getAsyncData');
      }

      promises.push(...p);
    }
  };

  Object(_plone_volto_helpers_Blocks_Blocks__WEBPACK_IMPORTED_MODULE_16__["visitBlocks"])(content, visitor);
  await Promise.allSettled(promises);
  return content;
};
/* harmony default export */ __webpack_exports__["default"] = (Object(redux__WEBPACK_IMPORTED_MODULE_5__["compose"])(Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["asyncConnect"])([{
  key: 'breadcrumbs',
  promise: ({
    location,
    store: {
      dispatch
    }
  }) =>  true && dispatch(Object(_plone_volto_actions__WEBPACK_IMPORTED_MODULE_20__["getBreadcrumbs"])(Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["getBaseUrl"])(location.pathname)))
}, {
  key: 'content',
  promise: ({
    location,
    store
  }) =>  true && fetchContent({
    store,
    location
  })
}, {
  key: 'navigation',
  promise: ({
    location,
    store: {
      dispatch
    }
  }) =>  true && dispatch(Object(_plone_volto_actions__WEBPACK_IMPORTED_MODULE_20__["getNavigation"])(Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["getBaseUrl"])(location.pathname), _plone_volto_registry__WEBPACK_IMPORTED_MODULE_14__["default"].settings.navDepth))
}, {
  key: 'types',
  promise: ({
    location,
    store: {
      dispatch
    }
  }) =>  true && dispatch(Object(_plone_volto_actions__WEBPACK_IMPORTED_MODULE_20__["getTypes"])(Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["getBaseUrl"])(location.pathname)))
}, {
  key: 'workflow',
  promise: ({
    location,
    store: {
      dispatch
    }
  }) =>  true && dispatch(Object(_plone_volto_actions__WEBPACK_IMPORTED_MODULE_20__["getWorkflow"])(Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["getBaseUrl"])(location.pathname)))
}]), react_intl__WEBPACK_IMPORTED_MODULE_17__["injectIntl"], Object(react_redux__WEBPACK_IMPORTED_MODULE_4__["connect"])((state, props) => ({
  pathname: props.location.pathname,
  token: state.userSession.token,
  userId: state.userSession.token ? jwt_decode__WEBPACK_IMPORTED_MODULE_2___default()(state.userSession.token).sub : '',
  content: state.content.data,
  apiError: state.apierror.error,
  connectionRefused: state.apierror.connectionRefused
}), null))(App));

/***/ }),

/***/ "./node_modules/@plone/volto/src/components/theme/MultilingualRedirector/MultilingualRedirector.jsx":
/*!**********************************************************************************************************!*\
  !*** ./node_modules/@plone/volto/src/components/theme/MultilingualRedirector/MultilingualRedirector.jsx ***!
  \**********************************************************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react-router-dom */ "react-router-dom");
/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react_router_dom__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react-redux */ "react-redux");
/* harmony import */ var react_redux__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(react_redux__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react_cookie__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-cookie */ "react-cookie");
/* harmony import */ var react_cookie__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react_cookie__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _plone_volto_registry__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @plone/volto/registry */ "./node_modules/@plone/volto/src/registry.js");
/* harmony import */ var _plone_volto_actions__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @plone/volto/actions */ "./node_modules/@plone/volto/src/actions/index.js");
/* harmony import */ var _plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @plone/volto/helpers */ "./node_modules/@plone/volto/src/helpers/index.js");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! react/jsx-runtime */ "react/jsx-runtime");
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__);
var _jsxFileName = "/Users/cihanandac/Documents/Code files/zeeuwsmuseumproject/frontend/node_modules/@plone/volto/src/components/theme/MultilingualRedirector/MultilingualRedirector.jsx";










const MultilingualRedirector = props => {
  const {
    settings
  } = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_4__["default"];
  const {
    pathname,
    children
  } = props;
  const [cookies] = Object(react_cookie__WEBPACK_IMPORTED_MODULE_3__["useCookies"])();
  const currentLanguage = cookies['I18N_LANGUAGE'] || settings.defaultLanguage;
  const redirectToLanguage = settings.supportedLanguages.includes(currentLanguage) ? currentLanguage : settings.defaultLanguage;
  const dispatch = Object(react_redux__WEBPACK_IMPORTED_MODULE_2__["useDispatch"])();
  react__WEBPACK_IMPORTED_MODULE_0___default.a.useEffect(() => {
    // ToDo: Add means to support language negotiation (with config)
    // const detectedLang = (navigator.language || navigator.userLanguage).substring(0, 2);
    let mounted = true;

    if (settings.isMultilingual && pathname === '/') {
      const langFileName = Object(_plone_volto_helpers__WEBPACK_IMPORTED_MODULE_6__["normalizeLanguageName"])(redirectToLanguage);
      __webpack_require__("./locales lazy recursive ^\\.\\/.*\\.json$")("./" + langFileName + ".json").then(locale => {
        if (mounted) {
          dispatch(Object(_plone_volto_actions__WEBPACK_IMPORTED_MODULE_5__["changeLanguage"])(redirectToLanguage, locale.default));
        }
      });
    }

    return () => {
      mounted = false;
    };
  }, [pathname, dispatch, redirectToLanguage, settings.isMultilingual]);
  return pathname === '/' && settings.isMultilingual ? /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])(react_router_dom__WEBPACK_IMPORTED_MODULE_1__["Redirect"], {
    to: `/${redirectToLanguage}`
  }) : /*#__PURE__*/Object(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["jsx"])(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_7__["Fragment"], {
    children: children
  });
};

/* harmony default export */ __webpack_exports__["default"] = (MultilingualRedirector);

/***/ }),

/***/ "./node_modules/@plone/volto/src/routes.js":
/*!*************************************************!*\
  !*** ./node_modules/@plone/volto/src/routes.js ***!
  \*************************************************/
/*! exports provided: multilingualRoutes, defaultRoutes, default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "multilingualRoutes", function() { return multilingualRoutes; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "defaultRoutes", function() { return defaultRoutes; });
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/defineProperty */ "@babel/runtime/helpers/defineProperty");
/* harmony import */ var _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @plone/volto/components */ "./node_modules/@plone/volto/src/components/index.js");
/* harmony import */ var _plone_volto_components_theme_App_App__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @plone/volto/components/theme/App/App */ "./node_modules/@plone/volto/src/components/theme/App/App.jsx");
/* harmony import */ var _plone_volto_components_theme_View_View__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @plone/volto/components/theme/View/View */ "./node_modules/@plone/volto/src/components/theme/View/View.jsx");
/* harmony import */ var _plone_volto_registry__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @plone/volto/registry */ "./node_modules/@plone/volto/src/registry.js");


var _config$settings, _config$settings2, _config$settings3, _config$settings4, _config$settings5, _config$settings6, _config$settings7, _config$settings8, _config$settings9;

function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); if (enumerableOnly) { symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; }); } keys.push.apply(keys, symbols); } return keys; }

function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i] != null ? arguments[i] : {}; if (i % 2) { ownKeys(Object(source), true).forEach(function (key) { _babel_runtime_helpers_defineProperty__WEBPACK_IMPORTED_MODULE_0___default()(target, key, source[key]); }); } else if (Object.getOwnPropertyDescriptors) { Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)); } else { ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } } return target; }

/**
 * Routes.
 * @module routes
 */
 // Deliberatelly use of absolute path of these components, since we do not want them
// in the components/index.js file.




/**
 * Default routes array.
 * @array
 * @returns {array} Routes.
 */

const multilingualRoutes = [{
  path: `/(${(_config$settings = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_4__["default"].settings) === null || _config$settings === void 0 ? void 0 : _config$settings.supportedLanguages.join('|')})/sitemap`,
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["Sitemap"]
}, {
  path: `/(${(_config$settings2 = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_4__["default"].settings) === null || _config$settings2 === void 0 ? void 0 : _config$settings2.supportedLanguages.join('|')})/search`,
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["Search"]
}, {
  path: `/(${(_config$settings3 = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_4__["default"].settings) === null || _config$settings3 === void 0 ? void 0 : _config$settings3.supportedLanguages.join('|')})/contact-form`,
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["ContactForm"]
}, {
  path: `/(${(_config$settings4 = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_4__["default"].settings) === null || _config$settings4 === void 0 ? void 0 : _config$settings4.supportedLanguages.join('|')})/change-password`,
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["ChangePassword"]
}, {
  path: `/(${(_config$settings5 = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_4__["default"].settings) === null || _config$settings5 === void 0 ? void 0 : _config$settings5.supportedLanguages.join('|')})/register`,
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["Register"]
}, {
  path: `/(${(_config$settings6 = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_4__["default"].settings) === null || _config$settings6 === void 0 ? void 0 : _config$settings6.supportedLanguages.join('|')})/password-reset`,
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["RequestPasswordReset"],
  exact: true
}, {
  path: `/(${(_config$settings7 = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_4__["default"].settings) === null || _config$settings7 === void 0 ? void 0 : _config$settings7.supportedLanguages.join('|')})/password-reset/:token`,
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["PasswordReset"],
  exact: true
}];
const defaultRoutes = [{
  path: '/',
  component: _plone_volto_components_theme_View_View__WEBPACK_IMPORTED_MODULE_3__["default"],
  exact: true
}, {
  path: '/login',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["Login"]
}, {
  path: '/logout',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["Logout"]
}, {
  path: '/sitemap',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["Sitemap"]
}, {
  path: '/search',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["Search"]
}, {
  path: '/contact-form',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["ContactForm"]
}, {
  path: '/controlpanel',
  exact: true,
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["Controlpanels"]
}, {
  path: '/controlpanel/dexterity-types/:id/layout',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["ContentTypeLayout"]
}, {
  path: '/controlpanel/dexterity-types/:id/schema',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["ContentTypeSchema"]
}, {
  path: '/controlpanel/dexterity-types/:id',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["ContentType"]
}, {
  path: '/controlpanel/dexterity-types',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["ContentTypes"]
}, {
  path: '/controlpanel/addons',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["AddonsControlpanel"]
}, {
  path: '/controlpanel/database',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["DatabaseInformation"]
}, {
  path: '/controlpanel/moderate-comments',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["ModerateComments"]
}, {
  path: '/controlpanel/users',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["UsersControlpanel"]
}, {
  path: '/controlpanel/usergroupmembership',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["UserGroupMembershipControlPanel"]
}, {
  path: '/controlpanel/groups',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["GroupsControlpanel"]
}, {
  path: '/controlpanel/:id',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["Controlpanel"]
}, {
  path: '/change-password',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["ChangePassword"]
}, {
  path: '/add',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["Add"]
}, {
  path: '/edit',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["Edit"]
}, {
  path: '/contents',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["Contents"]
}, {
  path: '/sharing',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["Sharing"]
}, {
  path: '/**/add',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["Add"]
}, {
  path: '/**/create-translation',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["CreateTranslation"]
}, {
  path: '/**/contents',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["Contents"]
}, {
  path: '/**/sharing',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["Sharing"]
}, {
  path: '/**/delete',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["Delete"]
}, {
  path: '/**/diff',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["Diff"]
}, {
  path: '/**/edit',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["Edit"]
}, {
  path: '/**/history',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["History"]
}, {
  path: '/**/sharing',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["Sharing"]
}, {
  path: '/**/manage-translations',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["ManageTranslations"]
}, {
  path: '/**/login',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["Login"]
}, {
  path: '/register',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["Register"]
}, {
  path: '/password-reset',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["RequestPasswordReset"],
  exact: true
}, {
  path: '/password-reset/:token',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["PasswordReset"],
  exact: true
}, {
  path: '/**',
  component: _plone_volto_components_theme_View_View__WEBPACK_IMPORTED_MODULE_3__["default"]
}, {
  path: '*',
  component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["NotFound"]
}];
/**
 * Routes array.
 * @array
 * @returns {array} Routes.
 */

const routes = [{
  path: '/',
  component: _plone_volto_components_theme_App_App__WEBPACK_IMPORTED_MODULE_2__["default"],
  routes: [// redirect to external links if path is in blacklist
  ...(((_config$settings8 = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_4__["default"].settings) === null || _config$settings8 === void 0 ? void 0 : _config$settings8.externalRoutes) || []).map(route => _objectSpread(_objectSpread({}, route.match), {}, {
    component: _plone_volto_components__WEBPACK_IMPORTED_MODULE_1__["NotFound"]
  })), // addon routes have a higher priority then default routes
  ...(_plone_volto_registry__WEBPACK_IMPORTED_MODULE_4__["default"].addonRoutes || []), ...(((_config$settings9 = _plone_volto_registry__WEBPACK_IMPORTED_MODULE_4__["default"].settings) === null || _config$settings9 === void 0 ? void 0 : _config$settings9.isMultilingual) && multilingualRoutes || []), ...defaultRoutes]
}];
/* harmony default export */ __webpack_exports__["default"] = (routes);

/***/ }),

/***/ "@sentry/browser":
/*!**********************************!*\
  !*** external "@sentry/browser" ***!
  \**********************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = require("@sentry/browser");

/***/ }),

/***/ "lodash/trim":
/*!******************************!*\
  !*** external "lodash/trim" ***!
  \******************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = require("lodash/trim");

/***/ })

};
//# sourceMappingURL=server.f22f1e40395ee230aedf.hot-update.js.map