Vagrant.configure("2") do |config|
	# Base Box 
	config.vm.box = "deb/jessie-amd64"

	# Masterless Salt 
	config.vm.synced_folder "salt/roots/", "/srv/salt"

	# Use Defaults 
	config.vm.provision :salt do |salt|

		salt.minion_config = "salt/minion"
		salt.run_highstate = true 

	end 
end 
