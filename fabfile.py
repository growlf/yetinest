#from fabric.api import settings, run, env, hide, fastprint
from fabric.api import *
from fabric.contrib.files import exists
from nest import *


# There are two mane processes that we will need to perform.
#
# 1) create the cards for the SBC's with minimum pre-configuration
# 2) complete the insdtallation, swarm joining  and etc of the final cluster

swarm_basename = 'nest'
swarm_masterhost = 'master'
swarm_workernode = 'worker'
swarm_storage = 'datastore'
swarm_net = '10.7.7.0'
swarm_address_start = 11
swarm_count = 5

image_src_url = 'https://oph.mdrjr.net/meveric/images/Jessie/Debian-Jessie-1.1.4-20171121-XU3+XU4.img.xz'


################################################
#### CARD CREATION FOR THE CLUSTER NODES

# Create a fresh OS image on an SD card for use as a generic node in a cluster
@task
def mksd():
    get_image()
    write_image()
    return True


# Edit Network Interface files
@task
def edit_interfaces():
    result = local(echo'''source-directory /etc/network/interfaces.d\nauto eth0\nallow-hotplug eth0\niface eth0 inet static\n\taddress %s.%s\n\tnetmask 255.255.255.0\n\tgateway %s.%s\n\tdns-nameservers 8.8.8.8''' > env.targetdevice/etc/network/interfaces)
    return result

# /etc/network/interfaces
# --------
# #interfaces(5) file used by ifup(8) and ifdown(8)
# #Include files from /etc/network/interfaces.d:
#
#    source-directory /etc/network/interfaces.d
#
#    auto eth0
#    allow-hotplug eth0
#    iface eth0 inet static
#      address %s.%s
#      netmask 255.255.255.0
#      gateway 172.16.28.1
#      dns-nameservers 8.8.8.8
#
# /etc/resolv.conf
# --------
# domain lan
# search lan
# nameserver 8.8.8.8

################################################
#### CONFIGURE NODES

# ssh root@"xu4-ip-address"
# echo 'Acquire::http::Proxy "http://172.16.28.2:3142";' >> /etc/apt/apt.conf.d/00proxy
# apt update && apt-get upgrade && apt-get dist-upgrade
# dpkg-reconfigure tzdata
# curl -sSL https://get.docker.com | sh
# apt install axel build-essential git xz-utils whiptail unzip wget sudo ssh htop whowatch nano curl
# adduser odroid
# usermod -aG sudo odroid
# usermod -aG docker odroid
# reboot
#
# ssh odroid@"xu4-ip-address"
# sudo curl -L https://github.com/docker/compose/releases/download/1.16.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
# sudo chmod +x /usr/local/bin/docker-compose
# sudo curl -L https://raw.githubusercontent.com/docker/compose/1.16.1/contrib/completion/bash/docker-compose -o /etc/bash_completion.d/docker-compose
# sudo reboot

