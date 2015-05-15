Vagrant.configure("2") do |config|
	# Base Box 
	config.vm.box = "ubuntu/vivid64"
	config.vm.synced_folder ".", "/var/www"
	config.vm.provision :shell, path: "bootstrap.sh"
	config.vm.network :forwarded_port, guest: 5000, host: 8081
end 
