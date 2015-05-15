Vagrant.configure("2") do |config|
	# Base Box 
	config.vm.box = "ubuntu/vivid64"
	config.vm.provision :shell, path: "bootstrap.sh"
	config.vm.network :forwarded_port, host: 5000, guest: 5000
end 
