Vagrant.configure("2") do |config|
  config.vm.box = "dummy"
  config.vm.provider :aws do |aws, override|
    aws.keypair_name = "Clave AWS"
    aws.security_groups = [ 'Web Service' ]
    aws.instance_type= 't2.micro'
    aws.ami = "ami-fcc4db98"
    aws.tags = {
      Name: 'Proyecto IV'
    }
    override.ssh.username = "ubuntu"
    override.ssh.private_key_path = "~/AWS/ClaveAWS.pem"
  end
    config.vm.provision :ansible do |ansible|
      ansible.force_remote_user= true
      ansible.host_key_checking=false
      ansible.playbook = "provision/playbook.yml"
  end
end
