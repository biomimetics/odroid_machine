#!/usr/bin/local

import subprocess
import datetime

logfile = '/home/odroid/monitor_zumy.log'

def get_timestamp():
  return datetime.datetime.now().strftime('%Y_%m_%d-%H:%M-%S.%f: ')

def log_message(message, filename=logfile):
  f = open(filename,'a')
  if len(message) and message[-1] != '\n':
    message = message + '\n'
  f.write(get_timestamp() + message)
  f.close()

def log_command(command):
  try:
    result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    success = True
    success_str = ' => '
  except subprocess.CalledProcessError as e:
    result = e.output
    success = False
    success_str = ' =X '

  log_message('>' + command + success_str + result)

  return success, result

def synchronize_clock(time_server='time.nist.gov'):
  log_message('Synchronizing Clock')
  log_command('service ntp stop')
  log_command('sntp -s ' + time_server)
  log_command('service ntp start')

def check_mbed_binary(mbed_file, mbed_md5)

if __name__ == '__main__':
  # Check wlan, eth configuration, proceed when one of them is up
  # Synchronize NTP daemon
  # Check mbed
  # Set mbed status light
  # ping loop?
