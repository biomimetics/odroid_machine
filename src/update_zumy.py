#!/usr/bin/python

def check_clone_update_repo(repo_dir, repo_url, repo_branch):
  if not glob.glob(repo_dir):
    log_command('git clone %s -b %s %s', repo_url, repo_branch, repo_dir)
  os.chdir(repo_dir)
  log_command('git pull')

def check_md5sum(filepath, md5_sum):
  _, current_md5 = log_command('md5sum ' + filepath)
  return current_md5.split()[0] == md5_sum
 
def check_download_program_mbed(bin_dir, bin_md5, bin_url):
  if not check_md5sum(bin_dir, bin_md5):
    bin_name = bin_dir.split('/')[-1]
    log_command('wget "%s" -O %s' % (bin_url, bin_name))
    if not check_md5sum(bin_name, bin_md5):
      log_message('Error: downloaded mbed binary does not match md5sum')
    else:
      log_command('mv %s %s' % (bin_name, bin_dir))
      log_command('sync')

def install_update_packages(packages=None):
  log_command('apt-get update')
  if packages is not None:
    log_command('apt-get --yes install ' + ' '.join(packages))
  log_command('apg-get upgrade')

def check_build_workspace(ws_dir, pkg_dirs):
  src_dir = ws_dir + '/src'
  if not glob.glob(src_dir):
    log_command('mkdir -P ' + src_dir)
  os.chdir(src_dir)

  # Create symbolic link to each package in workspace
  for pkg_dir in pkg_dirs:
    pkg_name = pkg_dir.split('/')[-1]
    if not glob.glob(pkg_name):
      log_command('ln -s ' + pkg_dir)
  
  os.chdir(ws_dir)
  log_command('catkin build')

if __name__ == '__main__':
  # Update packages
  install_update_packages([
    'ros-indigo-ros-base',
    'python-catkin-tools'
  ])
  # Pull repositories (odroid_machine, ros_zumy)
  check_clone_update_repo(
    '/home/odroid/odroid_machine',
    'https://github.com/abuchan/odroid_machine.git',
    'master'
  )
  
  check_clone_update_repo(
    '/home/odroid/ros_zumy',
    'https://github.com/abuchan/ros_zumy.git',
    'packet'
  )

  # Check ros workspace and catkin build
  check_build_workspace(
    '/home/odroid/exp_ws'
  )

  check_download_program_mbed(
  # Update mbed binary
    '/media/mbed/mbed_zumy_maker_galvo.bin',
    'f11737d33e5a6daa25892a46cc71806c',
    'https://wiki.eecs.berkeley.edu/biomimetics/Main/ZumyMbedUpdate?action=download&upname=mbed_zumy_marker_galvo.bin'
  )
      
