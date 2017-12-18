Name:           ros-indigo-swri-rospy
Version:        2.0.0
Release:        0%{?dist}
Summary:        ROS swri_rospy package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-rospy
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
BuildRequires:  ros-indigo-catkin

%description
This package provides added functionaliy on top of rospy, including a single-
threaded callback queue.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Dec 18 2017 Ed Venator <evenator@swri.edu> - 2.0.0-0
- Autogenerated by Bloom

* Fri Oct 13 2017 Ed Venator <evenator@swri.edu> - 1.2.0-0
- Autogenerated by Bloom

* Thu Aug 31 2017 Ed Venator <evenator@swri.edu> - 1.1.0-0
- Autogenerated by Bloom

* Wed Aug 02 2017 Ed Venator <evenator@swri.edu> - 1.0.0-0
- Autogenerated by Bloom

* Tue Jun 20 2017 Ed Venator <evenator@swri.edu> - 0.3.0-0
- Autogenerated by Bloom

* Tue Apr 11 2017 Ed Venator <evenator@swri.edu> - 0.0.14-0
- Autogenerated by Bloom

* Sat Mar 18 2017 Ed Venator <evenator@swri.edu> - 0.0.13-1
- Autogenerated by Bloom

* Sun Oct 23 2016 Ed Venator <evenator@swri.edu> - 0.0.13-0
- Autogenerated by Bloom

* Sun Aug 14 2016 Ed Venator <evenator@swri.edu> - 0.0.12-0
- Autogenerated by Bloom

* Fri May 13 2016 Ed Venator <evenator@swri.edu> - 0.0.11-0
- Autogenerated by Bloom

* Thu May 12 2016 Ed Venator <evenator@swri.edu> - 0.0.10-3
- Autogenerated by Bloom

* Thu May 12 2016 Ed Venator <evenator@swri.edu> - 0.0.10-2
- Autogenerated by Bloom

* Thu May 12 2016 Ed Venator <evenator@swri.edu> - 0.0.10-1
- Autogenerated by Bloom

* Thu May 12 2016 Ed Venator <evenator@swri.edu> - 0.0.10-0
- Autogenerated by Bloom

