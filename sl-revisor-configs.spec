Name:       sl-revisor-configs
Version:    1
Release:    6.0.2
License:    GPLv2+
Summary:    Kickstart and config files for creating your own SL Spins
Group:      Applications/System
URL:        http://www.scientificlinux.org
Source0:    http://ftp.scientificlinux.org/scientific/linux/6/SRPMS/%{name}/%{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:  noarch

%description
Kickstarts and config files used to create customized  spins
and the official SL 6 Spins.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
# create /etc
# copy SL6 revisor kickstart files into  /etc/revisor/SL6/ks
mkdir -p $RPM_BUILD_ROOT/etc/revisor/SL6/ks
for file in SL6/ks/*.ks; do
    install -m 644 $file $RPM_BUILD_ROOT/etc/revisor/SL6/ks
done

# copy SL6 revisor doc files into  /etc/revisor/SL6/docs
mkdir -p $RPM_BUILD_ROOT/etc/revisor/SL6/docs
for file in SL6/docs/*; do
    install -m 644 $file $RPM_BUILD_ROOT/etc/revisor/SL6/docs
done

# copy SL6 revisor config files into  /etc/revisor/conf.d
mkdir -p $RPM_BUILD_ROOT/etc/revisor/conf.d
for file in conf.d/*.conf ; do
    install -m 644 $file $RPM_BUILD_ROOT/etc/revisor/conf.d
done

# copy SL6 revisor config files into  /etc/revisor
for file in *.conf ; do
    install -m 644 $file $RPM_BUILD_ROOT/etc/revisor
done

# copy SL6 revisor image files into  /etc/revisor/SL6/images
mkdir -p $RPM_BUILD_ROOT/etc/revisor/SL6/images
for file in SL6/images/*.img ; do
    install -m 644 $file $RPM_BUILD_ROOT/etc/revisor/SL6/images
done

# copy SL6 revisor scripts into  /etc/revisor/SL6/build/scripts
mkdir -p $RPM_BUILD_ROOT/etc/revisor/SL6/build/scripts
for file in SL6/build/scripts/*.sh ; do
    install -m 664 $file $RPM_BUILD_ROOT/etc/revisor/SL6/build/scripts
done
install -m 644 SL6/build/scripts/locations.include $RPM_BUILD_ROOT/etc/revisor/SL6/build/scripts

# copy SL6 revisor product/ and anacondaupdates/ into  /etc/revisor/SL6/build/scripts/
mkdir -p $RPM_BUILD_ROOT/etc/revisor/SL6/build/scripts/product
mkdir -p $RPM_BUILD_ROOT/etc/revisor/SL6/build/scripts/product/installclasses
for file in SL6/build/scripts/product/installclasses/* ; do
    install -m 644 $file $RPM_BUILD_ROOT/etc/revisor/SL6/build/scripts/product/installclasses
done
mkdir -p $RPM_BUILD_ROOT/etc/revisor/SL6/build/scripts/anacondaupdates
for file in SL6/build/scripts/anacondaupdates/* ; do
    install -m 644 $file $RPM_BUILD_ROOT/etc/revisor/SL6/build/scripts/anacondaupdates
done


%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root,-)
%dir %{_sysconfdir}/revisor/SL6/ks/
%dir %{_sysconfdir}/revisor/SL6/docs/
%dir %{_sysconfdir}/revisor/SL6/images/
%dir %{_sysconfdir}/revisor/SL6/build/scripts/product/installclasses
%dir %{_sysconfdir}/revisor/SL6/build/scripts/anacondaupdates
%doc %{_sysconfdir}/revisor/SL6/docs/*
%config(noreplace) %{_sysconfdir}/revisor/*.conf
%config(noreplace) %{_sysconfdir}/revisor/conf.d/*
%config(noreplace) %{_sysconfdir}/revisor/SL6/ks/*.ks
%config(noreplace) %{_sysconfdir}/revisor/SL6/images/*.img
%config(noreplace) %{_sysconfdir}/revisor/SL6/build/scripts/locations.include
%{_sysconfdir}/revisor/SL6/build/scripts/*.sh
%{_sysconfdir}/revisor/SL6/build/scripts/product/installclasses/*
%{_sysconfdir}/revisor/SL6/build/scripts/anacondaupdates/*

%changelog
* Mon Feb 28 2011 Connie Sieh <csieh@fnal.gov> 1-6.0.1
- Added an updates (or respin) configuration

* Thu Feb 24 2011 Connie Sieh <csieh@fnal.gov> 1-6.0
- Changed numbering to show it is for SL 6.0

* Wed Feb 23 2011 Connie Sieh <csieh@fnal.gov> 1.0.sl.3 
- Added revisor/SL6/build/scripts/ which contains
-   scripts for creation of products.img and updates.img
-   products/installclasses/scientific.py

* Thu Dec 09 2010 Connie Sieh <csieh@fnal.gov> 1.0.sl 
- SL 6 first release 

