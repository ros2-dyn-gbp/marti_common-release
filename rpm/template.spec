Name:           ros-lunar-swri-transform-util
Version:        2.1.0
Release:        0%{?dist}
Summary:        ROS swri_transform_util package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/swri-robotics/marti_common
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       geos-devel
Requires:       proj-devel
Requires:       ros-lunar-cv-bridge
Requires:       ros-lunar-diagnostic-msgs
Requires:       ros-lunar-dynamic-reconfigure
Requires:       ros-lunar-geographic-msgs
Requires:       ros-lunar-geometry-msgs
Requires:       ros-lunar-gps-common
Requires:       ros-lunar-nodelet
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-rospy
Requires:       ros-lunar-sensor-msgs
Requires:       ros-lunar-swri-math-util
Requires:       ros-lunar-swri-roscpp
Requires:       ros-lunar-swri-yaml-util
Requires:       ros-lunar-tf
Requires:       ros-lunar-topic-tools
Requires:       yaml-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  geos-devel
BuildRequires:  pkgconfig
BuildRequires:  proj-devel
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-cv-bridge
BuildRequires:  ros-lunar-diagnostic-msgs
BuildRequires:  ros-lunar-dynamic-reconfigure
BuildRequires:  ros-lunar-geographic-msgs
BuildRequires:  ros-lunar-geometry-msgs
BuildRequires:  ros-lunar-gps-common
BuildRequires:  ros-lunar-nodelet
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-rospy
BuildRequires:  ros-lunar-rostest
BuildRequires:  ros-lunar-swri-math-util
BuildRequires:  ros-lunar-swri-roscpp
BuildRequires:  ros-lunar-swri-yaml-util
BuildRequires:  ros-lunar-tf
BuildRequires:  ros-lunar-topic-tools
BuildRequires:  yaml-cpp-devel

%description
The swri_transform_util package contains utility functions and classes for
transforming between coordinate frames.

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
* Fri Jan 26 2018 Marc Alban <malban@swri.org> - 2.1.0-0
- Autogenerated by Bloom

* Mon Dec 18 2017 Marc Alban <malban@swri.org> - 2.0.0-0
- Autogenerated by Bloom

* Fri Oct 13 2017 Marc Alban <malban@swri.org> - 1.2.0-0
- Autogenerated by Bloom

* Thu Aug 31 2017 Marc Alban <malban@swri.org> - 1.1.0-0
- Autogenerated by Bloom

* Tue Jun 20 2017 Marc Alban <malban@swri.org> - 0.3.0-0
- Autogenerated by Bloom

