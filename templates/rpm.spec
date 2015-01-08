Name: package_name
Summary: Short, single line summary of the package
Version: 0.1.0
Release: 1
License: BSD
Group: System Environment
Source: %{name}.tar.gz
BuildArch: noarch
Packager: James Southard <jsouthard@example.com>
Prefix: /opt

# Requires: pkgname >= 1.7.0, pkgname < 1.8.0

# The following causes the package manager to either prevent the install
#   or remove the conflicting package - handy for package name changes
# Conflicts: old_package_name
# Obsoletes: old_package_name

%define app_path apps/path

%description
Wax eloquently about how useful and necessary this package is. A longer
descriptions represents greater value in the package ;)


# Disable both the repack-jars and python-bytecompile, repack has a
#   switch, bytecompile doesn't
# %define __os_install_post %{nil}
#
# If only disabling repack-jars:
# %define __jar_repack 0
#   JAR repacking is slow and destroys checksum verification against atuomated
#   build output artifacts


%prep
%setup -c
%build


##
#  Scriptlet parameters
#    (taken from http://fedoraproject.org/wiki/Packaging:ScriptletSnippets)
#    $1 == Number of packages left after this action
#
#  %pre, %post: install ($1 == 1), upgrade ($1 == 2)
#  %preun, %postun: upgrade ($1 == 1), uninstall ($1 == 0)
#
#  Important consequence: uninstall-based cleanup should test $1 == 0 before
#  cleaning up, otherwise it'll delete the files from the upgrade
#  (see Scriptlet Ordering to understand why)
##

%install
INST_TGT=$RPM_BUILD_ROOT/%{app_path}
mkdir -p $INST_TGT
# Perform steps to move files from the unpacked tarball or from the build
#   results to the target installation directory


%clean
rm -rf $RPM_BUILD_ROOT

# RPM Trigger for taking action on install of related components
#   triggerin - triggers on package install or present when this rpm installed
#   triggerun - analog to previous, but for uninstall
#triggerin -- trigger_pkg_name


# %preun

# %postun
#   Analog to mkdir -p to clean up unused directories
#   rmdir --ignore-fail-on-non-empty %{app_path}
#   exit 0

%files 
%defattr(-,root,root,0755)


%changelog
* Thu Jan 01 1970 James Southard <jsouthard@example.com> 0.1.0
    - Enjoy the dawn of time as computers know it

