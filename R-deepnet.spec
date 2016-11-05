#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-deepnet
Version  : 0.2
Release  : 5
URL      : https://cran.r-project.org/src/contrib/deepnet_0.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/deepnet_0.2.tar.gz
Summary  : deep learning toolkit in R
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n deepnet

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library deepnet
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library deepnet


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/deepnet/DESCRIPTION
/usr/lib64/R/library/deepnet/INDEX
/usr/lib64/R/library/deepnet/Meta/Rd.rds
/usr/lib64/R/library/deepnet/Meta/hsearch.rds
/usr/lib64/R/library/deepnet/Meta/links.rds
/usr/lib64/R/library/deepnet/Meta/nsInfo.rds
/usr/lib64/R/library/deepnet/Meta/package.rds
/usr/lib64/R/library/deepnet/NAMESPACE
/usr/lib64/R/library/deepnet/R/deepnet
/usr/lib64/R/library/deepnet/R/deepnet.rdb
/usr/lib64/R/library/deepnet/R/deepnet.rdx
/usr/lib64/R/library/deepnet/help/AnIndex
/usr/lib64/R/library/deepnet/help/aliases.rds
/usr/lib64/R/library/deepnet/help/deepnet.rdb
/usr/lib64/R/library/deepnet/help/deepnet.rdx
/usr/lib64/R/library/deepnet/help/paths.rds
/usr/lib64/R/library/deepnet/html/00Index.html
/usr/lib64/R/library/deepnet/html/R.css
