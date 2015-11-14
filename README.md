# dw-vagrant
This is a Vagrant file and associated provisioning stuff for building a Dreamwidth dev machine.

## Pre-requisites
* On the host machine, you need vagrant installed: https://www.vagrantup.com/downloads.html
* You'll need Python and pyYAML installed on the host for running the configure script. (Or alternatively you can use the manual config format specified below)
* Dnsmasq or a hosts file needs to be set up to point whatever domain you want to the IP address `10.111.111.111`. (Potentially this will be replaced with something like vagrant-dnsmasq in future).
* You need a Github account, and you need to have forked the dreamwidth/dw-free and dreamwidth/dw-nonfree repositoies to this account.

## Configuration
Run `./configure.py` from the root directory. This currently randomly generates passwords for the dw MySQL user and the system login user as well as asking you for your github username.

## Running
From the root directory run `vagrant up` and it should take of the rest.
The root directory is mounted under `/vagrant`, so you should be able to edit anything in `./dw` and it will show up immediately on the site.

### Why is Ansible in the VM?
This is designed to be as easy as possible to set up. Ansible does not currently run under Windows (except using cygwin), so I made the decision to put it inside the VM. Plus all of the upgrade stuff can be handled from inside the VM when written.

## Caveats 
So far, this has only been tested against Parallels, and as such may need override config for other providers, pull requests are of course welcome if anyone finds any problems!
