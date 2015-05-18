Vagrant.configure("2") do |config|
	# Base Box 
	config.vm.box = "ubuntu/vivid64"
	config.vm.synced_folder ".", "/var/www"
	config.vm.provision :shell, path: "bootstrap.sh"
    # Allows you to go to localhost:5001 to view the app 
	config.vm.network :forwarded_port, guest: 5000, host: 5001
end 
