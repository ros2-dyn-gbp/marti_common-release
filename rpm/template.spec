%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-swri-cli-tools
Version:        3.6.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS swri_cli_tools package

License:        BSD 3 Clause
Source0:        %{name}-%{version}.tar.gz

Requires:       python3-natsort
Requires:       ros-iron-marti-introspection-msgs
Requires:       ros-iron-rcl-interfaces
Requires:       ros-iron-rclpy
Requires:       ros-iron-ros2cli
Requires:       ros-iron-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python3-natsort
BuildRequires:  ros-iron-marti-introspection-msgs
BuildRequires:  ros-iron-rcl-interfaces
BuildRequires:  ros-iron-rclpy
BuildRequires:  ros-iron-ros-workspace
BuildRequires:  ros-iron-ros2cli
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-iron-ament-copyright
BuildRequires:  ros-iron-ament-flake8
BuildRequires:  ros-iron-ament-pep257
BuildRequires:  ros-iron-ament-xmllint
%endif

%description
Command line tools for introspecting ROS systems

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/iron"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Mon Sep 11 2023 Southwest Research Institute <swri-robotics@swri.org> - 3.6.1-1
- Autogenerated by Bloom

* Mon Aug 14 2023 Southwest Research Institute <swri-robotics@swri.org> - 3.5.4-1
- Autogenerated by Bloom

* Wed Jun 07 2023 Southwest Research Institute <swri-robotics@swri.org> - 3.5.3-1
- Autogenerated by Bloom

* Mon Jun 05 2023 Southwest Research Institute <swri-robotics@swri.org> - 3.5.2-1
- Autogenerated by Bloom

