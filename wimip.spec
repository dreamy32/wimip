Name:           wimip
Version:        1.0.0
Release:        1%{?dist}
Summary:        Display your public IP, local IP, and location

License:        MIT
URL:            https://github.com/YOUR_USERNAME/wimip
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       curl, hostname

%description
wimip is a simple command-line tool that displays your public IP address,
local IP address, and geographic location with color-coded output.

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
* Fri Oct 03 2025 YOUR_NAME <your.email@example.com> - 1.0.0-1
- Initial package release
- Display public IP address
- Display local IP address
- Display geographic location
