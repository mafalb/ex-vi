Name:           ex-vi          
Version:        0.0
Release:        1%{?dist}
Summary:        The Traditional Vi
License:        BSD with attribution
Source0:        http://prdownloads.sourceforge.net/ex-vi/ex-050325.tar.bz2
#Patch0:         ex-vi-Makefile.patch
Packager:       Markus Falb <rpm@mafalb.at>

Requires:       ncurses
BuildRequires:  ncurses-devel

%description
The Traditional Vi

%prep
%setup -q
#%patch0 -p1

%build
%__make

%install
%__rm -rf %{buildroot}
%make_install

%clean
%__rm -rf %{buildroot}

%files

%defattr (0644, root, root, 0755)

%{_mandir}/man1/edit.ex-vi.1.gz
%{_mandir}/man1/ex.ex-vi.1.gz
%{_mandir}/man1/vedit.ex-vi.1.gz
%{_mandir}/man1/vi.ex-vi.1.gz
%{_mandir}/man1/view.ex-vi.1.gz

%defattr (0755, root, root, 0755)

%{_bindir}/ex.ex-vi
%{_bindir}/edit.ex-vi
%{_bindir}/vedit.ex-vi
%{_bindir}/vi.ex-vi
%{_bindir}/view.ex-vi
%{_libexecdir}/exrecover
%{_libexecdir}/expreserve

%changelog
* Sat Mar 25 2017 Markus Falb <rpm@mafalb.at>
- initial rpm build
