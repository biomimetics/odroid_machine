#!/usr/bin/python

import sys

STATIC_HOSTS = {
  '192.168.1.4': ''
}

def set_hostname(zumy_number):
  pass

def set_network(zumy_number, router_number):
  pass

def set_static_hosts(host_table):
  pass

def set_git_parameters(email='test.name@domain.com', name='Test Name'):
  gitstr = '''[user]
  email = %s
  name = %s
[core]
  editor = vim
[http]
  sslVerify = false'''
  print gitstr % (email, name)

if __name__ == '__main__':
  # Set hostname and static hosts
  # Set network interfaces
    # Set desired router number
    # Set static mac address for wired
    # make sure WiFi adapter is in udev rules and points to wlan0
  # Make sure fstab entry auto-mounts mbed
  # Configure avahi (https://askubuntu.com/questions/66020/avahi-slow-to-start-can-ping-ip-but-hostname-comes-online-after-few-mintues)
    # disable ipv6 in /etc/avahi/avahi-daemon.conf ?
    # in /etc/nsswitch.conf have hosts: files dns
  # Point bashrc to startup script
  # Set monitor_zumy.py to run as background service
  # Set git parameters
  pass
