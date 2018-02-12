Name:           ros-lunar-swri-roscpp
Version:        2.2.0
Release:        0%{?dist}
Summary:        ROS swri_roscpp package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-diagnostic-updater
Requires:       ros-lunar-nav-msgs
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-std-msgs
Requires:       ros-lunar-std-srvs
BuildRequires:  gtest-devel
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-diagnostic-updater
BuildRequires:  ros-lunar-nav-msgs
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-rostest
BuildRequires:  ros-lunar-std-msgs
BuildRequires:  ros-lunar-std-srvs

%description
swri_roscpp

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Mon Feb 12 2018 Elliot Johnson <elliot.johnson@swri.org> - 2.2.0-0
- Autogenerated by Bloom

* Fri Jan 26 2018 Elliot Johnson <elliot.johnson@swri.org> - 2.1.0-0
- Autogenerated by Bloom

* Mon Dec 18 2017 Elliot Johnson <elliot.johnson@swri.org> - 2.0.0-0
- Autogenerated by Bloom

* Fri Oct 13 2017 Elliot Johnson <elliot.johnson@swri.org> - 1.2.0-0
- Autogenerated by Bloom

* Thu Aug 31 2017 Elliot Johnson <elliot.johnson@swri.org> - 1.1.0-0
- Autogenerated by Bloom

* Tue Jun 20 2017 Elliot Johnson <elliot.johnson@swri.org> - 0.3.0-0
- Autogenerated by Bloom

