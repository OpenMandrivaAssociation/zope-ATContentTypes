%define Product ATContentTypes
%define product atcontenttypes
%define name    zope-%{Product}
%define version 1.2.3
%define release %mkrel 1

%define zope_minver     2.7
%define zope_home       %{_prefix}/lib/zope
%define software_home   %{zope_home}/lib/python

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Reimplementation of CMF's default content types with Archetypes
License:    GPL
Group:      System/Servers
URL:        http://plone.org/products/%{product}
Source:     http://plone.org/products/%{product}/releases/%{version}/%{Product}-%{version}.tgz
Requires:   zope >= %{zope_minver}
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This is a very roughe and short list of differences between the old CMF types
and the new ATContentTypes types.

* Archetypes: All types are written with Archetypes and have all features
  default Archetypes based types have like:
    o autogenerated edit forms based on the schema
    o referenceable
    o Easily enhanceable by subclassing or adding fields to the schema
    o Transformations like restructured text, python source code highlighting,
      pdf to html, office to html and many more.
    o plugable validation of fields
* Clean and documented API.
* Translateable using LinguaPlone.
* TemplateMixin: All types are using the template feature of Archetypes that
  allows you to choose the view template per instance. Simply register your
  template, assign it to a type and choose it in the edit form of your object.
  This features is used to turn an ordinary folder into a photo ablum by simple
  switching to a different view.
* Permissions per type and feature: Every type has its own add permission and
  all features like template mixin have their own modify permission, too.
* Numerous small adjustments and enhancements to all types for example:
    o Images can be rotated through the web and have exif informations
    o News Items have an image plus caption
    o Events have a body text
    o Documents have a history tab to show the last changes as an unified diff
      view using the ZODB history

%prep
%setup -c -q

%build
# Not much, eh? :-)

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
