# ###
# #
# Bash script for creating SD cards for odroid cluster
# ask questions
#     what is naming scheme
#     what is IP scheme
#     how many cards(Master, NFS, workers)
# wget the file from the server
# dd the img to the sd card
#
# Edit the following files:
#
# /etc/network/interfaces
# ***********************
# # interfaces(5) file used by ifup(8) and ifdown(8)
# # Include files from /etc/network/interfaces.d:
# source-directory /etc/network/interfaces.d
#
# auto eth0
# allow-hotplug eth0
# iface eth0 inet static
#   address 172.16.28.50
#   netmask 255.255.255.0
#   gateway 172.16.28.1
#   dns-nameservers 8.8.8.8
#
# /etc/resolv.conf
# **********************
# domain lan
# search lan
# nameserver 8.8.8.8
#
#
#
# # ===================================
# ###
# #
# Bash script for creating SD cards for odroid cluster
# ask questions
#     what is naming scheme
#     what is IP scheme
#     how many cards(Master, NFS, workers)
# wget the file from the server
# dd the img to the sd card
#
# Edit the following files:
#
# /etc/network/interfaces
# ***********************
# # interfaces(5) file used by ifup(8) and ifdown(8)
# # Include files from /etc/network/interfaces.d:
# source-directory /etc/network/interfaces.d
#
# auto eth0
# allow-hotplug eth0
# iface eth0 inet static
#   address 172.16.28.50
#   netmask 255.255.255.0
#   gateway 172.16.28.1
#   dns-nameservers 8.8.8.8
#
# /etc/resolv.conf
# **********************
# domain lan
# search lan
# nameserver 8.8.8.8
