Name:       sl-revisor-configs
Version:    1
Release:    6.3.4
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
* Thu Jul 26 2012 Connie Sieh <csieh@fnal.gov> 1-6.3.4
- Changed /etc/revisor/SL6/ks/sl6.install.dvd.x86_64.ks and sl6.install.dvd.i386.ks to include a few more packages

* Mon Jul 23 2012 Connie Sieh <csieh@fnal.gov> 1-6.3.3
- Changed revisor.conf to include new anaconda "final" option to disable beta message
- Renamed /etc/revisor/SL6/ks/sl6.match.tuv.install.dvd.x86_64.ks and sl6.match.tuv.install.dvd.i386.ks to sl6.install.dvd.x86_64.ks and sl6.install.dvd.i386.ks
- Modifed /etc/revisor/SL6/build/scripts/build.revisor.install-dvd.sh to handle the above name changes
- Updated /etc/revisor/SL6/build/scripts/locations.include to determine $ARCH automatically
- Added /etc/revisor/SL6/build/scripts/build.revisor.install-all-updates-included-dvd.sh which will create a DVD with all security errata incorporated 
- Updated /etc/revisor/SL6/build/scripts/anacondaupdates/yuminstall.py to match
  anaconda from 6_3

* Mon Jul 11 2011 Troy Dawson <dawson@fnal.gov> 1-6.1.0
- Added iso_label and iso_basename to revisor.conf entries
- Changed all configurations in conf.d to be 6x instead of 6.0
- Copied ks/sl6.match.tuv.install.dvd.*.ks to ks/sl6.match.tuv.install.dvd.*.60.ks
- Updated ks/sl6.match.tuv.install.dvd.*.ks to match 6.1
- Copied ks/sl6.all.groups.ks to ks/sl6.all.groups.60.ks
- Updated ks/sl6.all.groups.ks to match SL 6.1 groups

* Mon Feb 28 2011 Connie Sieh <csieh@fnal.gov> 1-6.0.3
- Fixed various script and config bugs.

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

