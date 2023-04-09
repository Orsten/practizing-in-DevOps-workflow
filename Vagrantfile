# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # Set up the external SSD disk as a shared folder
 # config.vm.synced_folder "/Volumes/SSD", "/vagrant"

  # Define the first virtual machine
  config.vm.define "vm1" do |vm1|
    vm1.vm.box = "ubuntu/focal64"
    vm1.vm.hostname = "vm1"
    vm1.vm.network "private_network", ip: "192.168.1.101"
    vm1.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
      vb.cpus = "1"
    end

    # Install Git
    vm1.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update
      sudo apt-get install -y git
    SHELL
  end

  # Define the second virtual machine
  config.vm.define "vm2" do |vm2|
    vm2.vm.box = "ubuntu/focal64"
    vm2.vm.hostname = "vm2"
    vm2.vm.network "private_network", ip: "192.168.1.102"
    vm2.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
      vb.cpus = "1"
    end
  end

  # Define the third virtual machine
  config.vm.define "vm3" do |vm3|
    vm3.vm.box = "ubuntu/focal64"
    vm3.vm.hostname = "vm3"
    vm3.vm.network "private_network", ip: "192.168.1.103"
    vm3.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
      vb.cpus = "1"
    end
  end

  # Configure Nginx to serve the virtual machines
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y nginx
    sudo rm /etc/nginx/sites-enabled/default
    sudo tee /etc/nginx/sites-available/vms.conf <<EOF
    server {
        listen 80;
        server_name _;
        location /vm1 {
            proxy_pass http://192.168.1.101;
        }
        location /vm2 {
            proxy_pass http://192.168.1.102;
        }
        location /vm3 {
            proxy_pass http://192.168.1.103;
        }
    }
    EOF
    sudo ln -s /etc/nginx/sites-available/vms.conf /etc/nginx/sites-enabled/vms.conf
    sudo service nginx restart
  SHELL
end