%lib_package xvidcore 4

Summary: Free reimplementation of the OpenDivX video codec
Name: xvidcore
Version: 1.3.2
Release: 15%{?dist}
License: XviD
Group: System Environment/Libraries
Source0: http://downloads.xvid.org/downloads/%{name}-%{version}.tar.gz
URL: http://www.xvid.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: /sbin/ldconfig
%ifarch %ix86 ia64
BuildRequires: nasm
%endif
%lib_dependencies
Obsoletes: xvidcore-static <= %{eversion}

%description
Free reimplementation of the OpenDivX video codec. You can play OpenDivX
and DivX4 videos with it, as well as encode compatible files.

%prep
%setup -q -n %{name}

%build
cd build/generic
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
cd build/generic
make install DESTDIR=%{buildroot}
/sbin/ldconfig -n %{buildroot}%{_libdir}
cd %{buildroot}%{_libdir}
for x in `ls *.so.* | grep '\.so\.[^.]*$'`; do
  chmod 0755 $x
  ln -s $x `echo $x | sed -e's,\.so.*,.so,'`
done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE README* ChangeLog AUTHORS TODO
%doc CodingStyle doc examples

%changelog
* Wed Sep 11 2013 Paulo Roma <roma@lcg.ufrj.br> - 1.3.2-14
- Update to 1.3.2.

* Fri Oct 23 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.2.2-13
- Update to 1.2.2.

* Sun Jan 18 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.2.1-12
- Update to 1.2.1.

* Wed Jul  4 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.1.3-11
- Update to 1.1.3.

* Wed Nov  8 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.1.2
- Update to 1.1.2.

* Sun Jan 22 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.1.0.

* Wed Jan 19 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.3.

* Thu Oct 14 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.2.

* Tue Jun  8 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.1.

* Fri May 28 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Upgrade to 1.0.0 final.
- run ldconfig to ensure proper symlink creating at packaging time.

* Mon Apr 12 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Upgrade to 1.0.0-rc4.

* Thu Oct 23 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- rename static to devel package and put include files in there.

* Mon Sep 15 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Added a .so symlink to the lib for proper detection.

* Thu Aug  7 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.2.
- The .so file has now a version appended.

* Mon Apr  7 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.1.
- Build and install changes since there is now a nice configure script.

* Mon Mar 31 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 9.

* Wed Jan 29 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Fixed the location of the .h files... doh!

* Sun Jan 12 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Remove the decore.h and encore2.h inks as divx4linux 5.01 will provide them.
- Rename -devel to -static as it seems more logic.

* Fri Dec 27 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Initial RPM release.
