#from fabric.api import settings, run, env, hide, fastprint
from fabric.api import *
from fabric.contrib.files import exists


# There are two mane processes that we will need to perform.
#
# 1) create the cards for the SBC's with minimum pre-configuration
# 2) complete the insdtallation, swarm joining  and etc of the final cluster

swarm_basename = 'nest'
swarm_masterhost = 'master'
swarm_workernode = 'worker'
swarm_storage = 'datastore'
swarm_net = '10.7.7.0'
swarm_count = 5

image_src_url = 'https://oph.mdrjr.net/meveric/images/Jessie/Debian-Jessie-1.1.4-20171121-XU3+XU4.img.xz'


################################################
#### CARD CREATION FOR THE CLUSTER NODES

# Get the image from the internet, if we do not already have it on our system
# wwget image_src_url
@task
def get_image():
    result = sudo('wget https://oph.mdrjr.net/meveric/images/Jessie/Debian-Jessie-1.1.4-20171121-XU3+XU4.img.xz')
    return result


# Write the OS image to the card
# xzcat Debian-Jessie-1.1.4-20171121-XU3+XU4.img.xz | sudo dd of=/dev/sdb status='progress'

# Edit the following files:
#
# /etc/network/interfaces
# --------
# interfaces(5) file used by ifup(8) and ifdown(8)
# Include files from /etc/network/interfaces.d:
#
#    source-directory /etc/network/interfaces.d
#
#    auto eth0
#    allow-hotplug eth0
#    iface eth0 inet static
#      address 172.16.28.50
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


####DEBUG: Library TEST
#from .nest import set_targetdevice
#set_targetdevice()
