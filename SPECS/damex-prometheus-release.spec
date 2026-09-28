%define debug_package %{nil}
%define disttype %{expand:%%(/usr/lib/rpm/redhat/dist.sh --disttype)}
%define distnum %{expand:%%(/usr/lib/rpm/redhat/dist.sh --distnum)}
%undefine source_date_epoch_from_changelog

Name: damex-prometheus-release
Version: 0.3.0
Release: 1%{?dist}
Summary: damex prometheus repository configuration
License: MIT
URL: https://yum-repositories.damex.org

%description

%prep

%build

%install
%{__install} -d %{buildroot}%{_sysconfdir}/yum.repos.d
cat <<EOF > %{buildroot}%{_sysconfdir}/yum.repos.d/damex-prometheus.repo
[damex-prometheus]
name = damex-prometheus
baseurl = https://yum-repositories.damex.org/prometheus/%{disttype}/%{distnum}/%{_arch}
gpgcheck = 1
repo_gpgcheck = 1
gpgkey = https://yum-repositories.damex.org/prometheus/prometheus-2036-09-25.asc
EOF

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/yum.repos.d/damex-prometheus.repo
