# Kickstart file for composing the "SL 6" spin of RHEL 6
# Use a part of 'iso' to define how large you want your isos.
# Only used when composing to more than one iso.
# Default is 695 (megs), CD size. unless "revisor -cli --install-dvd" is used
# where the default size is a DVD 
# Listed below is the size of a DVD if you wanted to split higher.

#part iso --size=4998

# Package manifest for the compose. 
# Need to use "kickstart_manifest = 1" in your /etc/revisor/revisor.conf file
# to enable this file to be used as the definition of what is included
# in the compose , otherwise the "comps" file defines the compose
##########################
%packages 
@base
@core
@debugging
@directory-client
@java-platform
@network-file-system-client
@server-platform
@basic-desktop
@desktop-debugging
@desktop-platform
@general-desktop
@graphical-admin-tools
@input-methods
@legacy-x
@x11
@internet-browser
@internet-applications
@office-suite
@remote-desktop-clients
#basic server
@console-internet
@hardware-monitoring
@large-systems
@perl-runtime
@desktop-platform-devel
@print-client
@development
@eclipse
@emacs
@fonts
@graphics
@performance
#
#virtualization
@virtualization
@virtualization-client
@virtualization-platform
@php
@postgresql
@postgresql-client
@mysql
@mysql-client
@system-admin-tools
@technical-writing
@tex
@turbogears
@web-server
@web-servlet
@ice-desktop
@additional-devel
@server-platform-devel
#
# Need these to build the iso image
anaconda
#everything else
*
%end
