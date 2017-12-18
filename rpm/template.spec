Name:           ros-lunar-swri-rospy
Version:        2.0.0
Release:        0%{?dist}
Summary:        ROS swri_rospy package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-rospy
Requires:       ros-lunar-std-msgs
Requires:       ros-lunar-std-srvs
BuildRequires:  ros-lunar-catkin

%description
This package provides added functionaliy on top of rospy, including a single-
threaded callback queue.

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
* Mon Dec 18 2017 Ed Venator <evenator@swri.edu> - 2.0.0-0
- Autogenerated by Bloom

* Fri Oct 13 2017 Ed Venator <evenator@swri.edu> - 1.2.0-0
- Autogenerated by Bloom

* Thu Aug 31 2017 Ed Venator <evenator@swri.edu> - 1.1.0-0
- Autogenerated by Bloom

* Tue Jun 20 2017 Ed Venator <evenator@swri.edu> - 0.3.0-0
- Autogenerated by Bloom

