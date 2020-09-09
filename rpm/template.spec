%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-swri-transform-util
Version:        2.14.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS swri_transform_util package

License:        BSD
URL:            https://github.com/swri-robotics/marti_common
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python3-devel
Requires:       geos-devel
Requires:       proj-devel
Requires:       python3-numpy
Requires:       ros-noetic-cv-bridge
Requires:       ros-noetic-diagnostic-msgs
Requires:       ros-noetic-genpy >= 0.6.14
Requires:       ros-noetic-geographic-msgs
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-gps-common
Requires:       ros-noetic-marti-nav-msgs
Requires:       ros-noetic-nodelet
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-rospy
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-swri-math-util
Requires:       ros-noetic-swri-nodelet
Requires:       ros-noetic-swri-roscpp
Requires:       ros-noetic-swri-yaml-util
Requires:       ros-noetic-tf
Requires:       ros-noetic-topic-tools
Requires:       yaml-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  boost-python3-devel
BuildRequires:  geos-devel
BuildRequires:  pkgconfig
BuildRequires:  proj-devel
BuildRequires:  python3-setuptools
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-cv-bridge
BuildRequires:  ros-noetic-diagnostic-msgs
BuildRequires:  ros-noetic-genpy >= 0.6.14
BuildRequires:  ros-noetic-geographic-msgs
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-gps-common
BuildRequires:  ros-noetic-marti-nav-msgs
BuildRequires:  ros-noetic-nodelet
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-rospy
BuildRequires:  ros-noetic-rostest
BuildRequires:  ros-noetic-swri-math-util
BuildRequires:  ros-noetic-swri-nodelet
BuildRequires:  ros-noetic-swri-roscpp
BuildRequires:  ros-noetic-swri-yaml-util
BuildRequires:  ros-noetic-tf
BuildRequires:  ros-noetic-topic-tools
BuildRequires:  yaml-cpp-devel
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The swri_transform_util package contains utility functions and classes for
transforming between coordinate frames.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Wed Sep 09 2020 Marc Alban <malban@swri.org> - 2.14.2-1
- Autogenerated by Bloom

* Tue Aug 18 2020 Marc Alban <malban@swri.org> - 2.14.1-1
- Autogenerated by Bloom

* Wed Jul 15 2020 Marc Alban <malban@swri.org> - 2.14.0-1
- Autogenerated by Bloom

* Fri Jun 26 2020 Marc Alban <malban@swri.org> - 2.13.7-1
- Autogenerated by Bloom

* Wed Jun 17 2020 Marc Alban <malban@swri.org> - 2.13.6-1
- Autogenerated by Bloom

* Wed Jun 17 2020 Marc Alban <malban@swri.org> - 2.13.5-1
- Autogenerated by Bloom

* Tue Jun 16 2020 Marc Alban <malban@swri.org> - 2.13.4-1
- Autogenerated by Bloom

* Fri Jun 12 2020 Marc Alban <malban@swri.org> - 2.13.3-1
- Autogenerated by Bloom

* Wed Jun 10 2020 Marc Alban <malban@swri.org> - 2.13.2-1
- Autogenerated by Bloom

