Name:           ros-indigo-pyros-test
Version:        0.0.4
Release:        0%{?dist}
Summary:        ROS pyros_test package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-message-runtime >= 0.4.12
Requires:       ros-indigo-rospy >= 1.11.19
Requires:       ros-indigo-std-msgs >= 0.5.10
BuildRequires:  ros-indigo-catkin >= 0.6.18
BuildRequires:  ros-indigo-message-generation >= 0.2.10
BuildRequires:  ros-indigo-roslint >= 0.10.0
BuildRequires:  ros-indigo-rospy >= 1.11.19
BuildRequires:  ros-indigo-rostest >= 1.11.19
BuildRequires:  ros-indigo-rostopic >= 1.11.19
BuildRequires:  ros-indigo-rosunit >= 1.11.12
BuildRequires:  ros-indigo-std-msgs >= 0.5.10

%description
Basic test nodes for Pyros dynamic ROS interface

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
* Thu Jun 02 2016 AlexV <asmodehn@gmail.com> - 0.0.4-0
- Autogenerated by Bloom

* Thu Feb 18 2016 AlexV <asmodehn@gmail.com> - 0.0.3-0
- Autogenerated by Bloom

* Sun Jan 10 2016 AlexV <asmodehn@gmail.com> - 0.0.2-0
- Autogenerated by Bloom

* Wed Jan 06 2016 AlexV <asmodehn@gmail.com> - 0.0.1-1
- Autogenerated by Bloom

