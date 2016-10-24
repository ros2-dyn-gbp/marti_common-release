Name:           ros-jade-swri-yaml-util
Version:        0.1.6
Release:        0%{?dist}
Summary:        ROS swri_yaml_util package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/swri-robotics/marti_common
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       yaml-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  pkgconfig
BuildRequires:  ros-jade-catkin
BuildRequires:  yaml-cpp-devel

%description
Provides wrappers around the yaml-cpp library for various utility functions and
to abstract out the API changes made to yaml-cpp between ubuntu:precise and
ubuntu:trusty.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sun Oct 23 2016 Marc Alban <malban@swri.org> - 0.1.6-0
- Autogenerated by Bloom

* Fri May 13 2016 Marc Alban <malban@swri.org> - 0.1.5-0
- Autogenerated by Bloom

* Thu May 12 2016 Marc Alban <malban@swri.org> - 0.1.4-0
- Autogenerated by Bloom

