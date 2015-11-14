# -*- mode: ruby -*-
# vi: set ft=ruby :

HOST_NAME = "dreamwidth-dev"
Vagrant.configure(2) do |config|

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "ubuntu/trusty64"

  config.vm.hostname = HOST_NAME

  config.ssh.shell = "bash -c 'BASH_ENV=/etc/profile exec bash'"
  config.vm.define HOST_NAME do |host|
  end

  # Override if Parallels
  config.vm.provider "parallels" do |v, override|
    override.vm.box = "parallels/ubuntu-14.04"
    override.vm.box_url = "https://vagrantcloud.com/parallels/ubuntu-14.04"
  end

  # Parallels-specific configuration
  config.vm.provider :parallels do |vm|
    vm.name = HOST_NAME
    # Auto-update Parallels Tools on the VM (takes a few minutes)
    vm.update_guest_tools = true
    vm.memory = 1024
    vm.cpus = 2
  end

  config.vm.provision :shell,
    :keep_color => true,
    :inline => "export PYTHONUNBUFFERED=1 && export ANSIBLE_FORCE_COLOR=1 && cd /vagrant/provisioning && ./init.sh"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.network "private_network", ip: "10.111.111.111"
end
