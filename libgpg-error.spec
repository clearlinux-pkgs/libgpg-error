#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v12
# autospec commit: f9eab48
#
# Source0 file verified with key 0x528897B826403ADA
#
%define keepstatic 1
Name     : libgpg-error
Version  : 1.50
Release  : 73
URL      : https://gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-1.50.tar.gz
Source0  : https://gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-1.50.tar.gz
Source1  : https://gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-1.50.tar.gz.sig
Source2  : 528897B826403ADA.pkey
Summary  : libgpg-error
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0+ LGPL-2.1
Requires: libgpg-error-bin = %{version}-%{release}
Requires: libgpg-error-data = %{version}-%{release}
Requires: libgpg-error-info = %{version}-%{release}
Requires: libgpg-error-lib = %{version}-%{release}
Requires: libgpg-error-license = %{version}-%{release}
Requires: libgpg-error-locales = %{version}-%{release}
Requires: libgpg-error-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : file
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gnupg
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This is a library that defines common error values for all GnuPG
components.  Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt,
pinentry, SmartCard Daemon and possibly more in the future.

%package bin
Summary: bin components for the libgpg-error package.
Group: Binaries
Requires: libgpg-error-data = %{version}-%{release}
Requires: libgpg-error-license = %{version}-%{release}

%description bin
bin components for the libgpg-error package.


%package data
Summary: data components for the libgpg-error package.
Group: Data

%description data
data components for the libgpg-error package.


%package dev
Summary: dev components for the libgpg-error package.
Group: Development
Requires: libgpg-error-lib = %{version}-%{release}
Requires: libgpg-error-bin = %{version}-%{release}
Requires: libgpg-error-data = %{version}-%{release}
Provides: libgpg-error-devel = %{version}-%{release}
Requires: libgpg-error = %{version}-%{release}

%description dev
dev components for the libgpg-error package.


%package dev32
Summary: dev32 components for the libgpg-error package.
Group: Default
Requires: libgpg-error-lib32 = %{version}-%{release}
Requires: libgpg-error-bin = %{version}-%{release}
Requires: libgpg-error-data = %{version}-%{release}
Requires: libgpg-error-dev = %{version}-%{release}

%description dev32
dev32 components for the libgpg-error package.


%package extras
Summary: extras components for the libgpg-error package.
Group: Default

%description extras
extras components for the libgpg-error package.


%package info
Summary: info components for the libgpg-error package.
Group: Default

%description info
info components for the libgpg-error package.


%package lib
Summary: lib components for the libgpg-error package.
Group: Libraries
Requires: libgpg-error-data = %{version}-%{release}
Requires: libgpg-error-license = %{version}-%{release}

%description lib
lib components for the libgpg-error package.


%package lib32
Summary: lib32 components for the libgpg-error package.
Group: Default
Requires: libgpg-error-data = %{version}-%{release}
Requires: libgpg-error-license = %{version}-%{release}

%description lib32
lib32 components for the libgpg-error package.


%package license
Summary: license components for the libgpg-error package.
Group: Default

%description license
license components for the libgpg-error package.


%package locales
Summary: locales components for the libgpg-error package.
Group: Default

%description locales
locales components for the libgpg-error package.


%package man
Summary: man components for the libgpg-error package.
Group: Default

%description man
man components for the libgpg-error package.


%package staticdev
Summary: staticdev components for the libgpg-error package.
Group: Default
Requires: libgpg-error-dev = %{version}-%{release}

%description staticdev
staticdev components for the libgpg-error package.


%package staticdev32
Summary: staticdev32 components for the libgpg-error package.
Group: Default
Requires: libgpg-error-dev = %{version}-%{release}

%description staticdev32
staticdev32 components for the libgpg-error package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 528897B826403ADA' gpg.status
%setup -q -n libgpg-error-1.50
cd %{_builddir}/libgpg-error-1.50
pushd ..
cp -a libgpg-error-1.50 build32
popd
pushd ..
cp -a libgpg-error-1.50 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1718818239
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure  --enable-static \
--enable-install-gpg-error-config
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
%configure  --enable-static \
--enable-install-gpg-error-config   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure  --enable-static \
--enable-install-gpg-error-config
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1718818239
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libgpg-error
cp %{_builddir}/libgpg-error-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libgpg-error/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1 || :
cp %{_builddir}/libgpg-error-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/libgpg-error/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
export GOAMD64=v2
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
%find_lang libgpg-error
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/gpg-error
/V3/usr/bin/yat2m
/usr/bin/gpg-error
/usr/bin/gpg-error-config
/usr/bin/gpgrt-config
/usr/bin/yat2m

%files data
%defattr(-,root,root,-)
/usr/share/libgpg-error/errorref.txt

%files dev
%defattr(-,root,root,-)
/usr/include/gpg-error.h
/usr/include/gpgrt.h
/usr/lib64/libgpg-error.so
/usr/lib64/pkgconfig/gpg-error.pc
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libgpg-error.so
/usr/lib32/pkgconfig/32gpg-error.pc
/usr/lib32/pkgconfig/gpg-error.pc

%files extras
%defattr(-,root,root,-)
/usr/share/common-lisp/source/gpg-error/gpg-error-codes.lisp
/usr/share/common-lisp/source/gpg-error/gpg-error-package.lisp
/usr/share/common-lisp/source/gpg-error/gpg-error.asd
/usr/share/common-lisp/source/gpg-error/gpg-error.lisp

%files info
%defattr(0644,root,root,0755)
/usr/share/info/gpgrt.info

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libgpg-error.so.0.37.0
/usr/lib64/libgpg-error.so.0
/usr/lib64/libgpg-error.so.0.37.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libgpg-error.so.0
/usr/lib32/libgpg-error.so.0.37.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgpg-error/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
/usr/share/package-licenses/libgpg-error/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gpg-error-config.1
/usr/share/man/man1/gpgrt-config.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libgpg-error.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libgpg-error.a

%files locales -f libgpg-error.lang
%defattr(-,root,root,-)

