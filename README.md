winexe
======

CentOS/RH/Amazon RPMs for winexe <http://sourceforge.net/projects/winexe/>

Tested on CentOS 6.7/7.1 x86_64 and Amazon Linux 2015.09

Winexe remotely executes commands on Windows NT/2000/XP/2003/Vista/7/2008/8/2012 systems from GNU/Linux (and possibly also from other Unices capable of building the Samba 4 software package).

Requirements
------------

To build: 

* git
* rpm-build
* gcc
* pkgconfig
* libtalloc-devel
* samba4-devel
* popt-devel
* mingw64-gcc
* mingw32-gcc

Building fresh RPM
-------------------

Clone the repo: 

    git clone https://github.com/juliogonzalez/winexe-rpm.git
    cd winexe-rpm

Build the RPM:

    ./winexe-rpm

And install:

    rpm -iUvh RPMS/$HOSTTYPE/winexe-1.1-1b787d2.*.$HOSTTYPE.rpm

