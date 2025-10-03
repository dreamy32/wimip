Name:           wimip
Version:        1.0.1
Release:        1%{?dist}
Summary:        Display your public IP, local IP, and location

License:        MIT
URL:            https://github.com/dreamy32/wimip
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       curl, hostname

%description
wimip is a simple command-line tool that displays your public IP address,
local IP address, and geographic location with color-coded output.

This is a pure bash script package (noarch) and is compatible with all
Fedora, RHEL, CentOS, and Rocky Linux versions despite version-specific
package naming.

%prep
%setup -q

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 wimip %{buildroot}%{_bindir}/wimip

%files
%license LICENSE
%doc README.md
%{_bindir}/wimip

%changelog
* Fri Oct 03 2025 David Berube <davidberube2003@outlook.com> - 1.0.1-1
- Add compatibility note in package description
- Clarify that package works on all RHEL-based distros

* Fri Oct 03 2025 David Berube <davidberube2003@outlook.com> - 1.0.0-1
- Initial package release
- Display public IP address
- Display local IP address
- Display geographic location
