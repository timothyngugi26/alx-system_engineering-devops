#!/usr/bin/env bash
#set up your client SSH configuration file so that you can connect to a server without typing a password i.e using puppet
first_line{'turn off passwd auth':
'etc/ssh/ssh_config':}
ensure => 'present',
path =>'/etc/ssh/ssh_config',
line =>'PasswordAuthentication no',

file_line { 'Declare identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
  }
