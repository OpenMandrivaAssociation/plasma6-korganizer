#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE calendar and scheduling component
Name:		korganizer
Version:	25.04.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/korganizer/-/archive/%{gitbranch}/korganizer-%{gitbranchd}.tar.bz2#/korganizer-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/korganizer-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6UiTools)
BuildRequires:	cmake(Qt6UiPlugin)
BuildRequires:	cmake(KPim6AkonadiSearch)
BuildRequires:	cmake(KPim6AkonadiContactCore)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6TextTemplate)
BuildRequires:	cmake(KPim6TextEdit)
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	cmake(KF6CalendarCore)
BuildRequires:	cmake(KPim6IdentityManagementCore)
BuildRequires:	cmake(KPim6MailTransport)
BuildRequires:	cmake(KPim6AkonadiMime)
BuildRequires:	cmake(KPim6CalendarUtils)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Holidays)
BuildRequires:	cmake(KPim6LdapCore)
BuildRequires:	cmake(KPim6LdapWidgets)
BuildRequires:	cmake(KPim6AkonadiCalendar)
BuildRequires:	cmake(Phonon4Qt6)
BuildRequires:	cmake(KPim6KontactInterface)
BuildRequires:	cmake(KPim6Mime)
BuildRequires:	cmake(KPim6AkonadiNotes)
BuildRequires:	cmake(KPim6PimCommonAkonadi)
BuildRequires:	cmake(KPim6IncidenceEditor)
BuildRequires:	cmake(KPim6CalendarSupport)
BuildRequires:	cmake(KPim6EventViews)
BuildRequires:	cmake(KF6UserFeedback)
BuildRequires:	%mklibname -d KF6UserFeedbackWidgets
BuildRequires:	cmake(KPim6Libkdepim)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
Requires:	plasma6-akonadi-calendar-tools
Requires:	plasma6-kdepim-runtime
Suggests:	plasma6-kdepim-addons

%description
KOrganizer provides management of events and tasks, alarm notification,
web export, network transparent handling of data, group scheduling,
import and export of calendar files and more. It is able to work together
with a wide variety of groupware servers, for example Kolab, Open-Xchange,
Citadel or OpenGroupware.org.

%files -f all.lang
%{_datadir}/applications/korganizer-import.desktop
%{_datadir}/applications/org.kde.korganizer.desktop
%{_bindir}/korganizer
%{_datadir}/config.kcfg/korganizer.kcfg
%dir %{_datadir}/korganizer/
%{_datadir}/korganizer/*
%{_docdir}/*/*/korganizer
%{_iconsdir}/hicolor/*/apps/korganizer.*
%{_iconsdir}/hicolor/*/apps/korg-journal.*
%{_iconsdir}/hicolor/*/apps/korg-todo.*
%{_iconsdir}/hicolor/*/apps/quickview.*
%{_datadir}/dbus-1/services/org.kde.korganizer.service
%{_datadir}/qlogging-categories6/korganizer.categories
%{_datadir}/qlogging-categories6/korganizer.renamecategories
%{_datadir}/knsrcfiles/korganizer.knsrc
%{_datadir}/metainfo/org.kde.korganizer.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.korganizer.Korganizer.xml
%{_datadir}/dbus-1/interfaces/org.kde.Korganizer.Calendar.xml
%{_qtdir}/plugins/pim6/kcms/korganizer/korganizer_configcolorsandfonts.so
%{_qtdir}/plugins/pim6/kcms/korganizer/korganizer_configfreebusy.so
%{_qtdir}/plugins/pim6/kcms/korganizer/korganizer_configgroupscheduling.so
%{_qtdir}/plugins/pim6/kcms/korganizer/korganizer_configmain.so
%{_qtdir}/plugins/pim6/kcms/korganizer/korganizer_configplugins.so
%{_qtdir}/plugins/pim6/kcms/korganizer/korganizer_configtime.so
%{_qtdir}/plugins/pim6/kcms/korganizer/korganizer_configviews.so
%{_qtdir}/plugins/pim6/kcms/korganizer/korganizer_userfeedback.so
%{_qtdir}/plugins/pim6/kcms/summary/kcmapptsummary.so
%{_qtdir}/plugins/pim6/kcms/summary/kcmsdsummary.so
%{_qtdir}/plugins/pim6/kcms/summary/kcmtodosummary.so
%{_qtdir}/plugins/pim6/kontact/kontact_journalplugin.so
%{_qtdir}/plugins/pim6/kontact/kontact_korganizerplugin.so
%{_qtdir}/plugins/pim6/kontact/kontact_specialdatesplugin.so
%{_qtdir}/plugins/pim6/kontact/kontact_todoplugin.so
%{_qtdir}/plugins/korganizerpart.so
%{_datadir}/applications/korganizer-view.desktop
%{_libdir}/libkorganizer_core.so*
%{_libdir}/libkorganizer_interfaces.so*
%{_libdir}/libkorganizerprivate.so*
%{_qtdir}/plugins/pim6/korganizer/datenums.so
%{_qtdir}/plugins/pim6/korganizer/lunarphases.so
%{_qtdir}/plugins/pim6/korganizer/picoftheday.so
%{_qtdir}/plugins/pim6/korganizer/thisdayinhistory.so
%{_datadir}/icons/hicolor/scalable/status/moon-phase-first-quarter.svg
%{_datadir}/icons/hicolor/scalable/status/moon-phase-full.svg
%{_datadir}/icons/hicolor/scalable/status/moon-phase-last-quarter.svg
%{_datadir}/icons/hicolor/scalable/status/moon-phase-new.svg

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n korganizer-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang all --all-name
