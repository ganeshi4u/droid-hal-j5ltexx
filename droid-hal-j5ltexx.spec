# These and other macros are documented in dhd/droid-hal-device.inc

%define device j5ltexx
%define vendor samsung

%define vendor_pretty Samsung
%define device_pretty Galaxy J5

%define installable_zip 1

%define straggler_files \
/selinux_version\
/service_contexts\
%{nil}

%include rpm/dhd/droid-hal-device.inc
