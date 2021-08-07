# Instructions

Tested on:
- Ubuntu Server 20.10
- Ansible 4.3, ansible-core 2.11.3
- podman 2.0.6
- buildah 1.15.2
- ansible-bender 0.9.0

Perform the following commands to prepare your system for ansible-bender:

    sudo apt update
    sudo apt install podman runc python3-pip ansible
    sudo pip3 install ansible-bender

Now build your podman container with the command:

    sudo ansible-bender build moo-bender.yaml

Run your container with:

    sudo podman run -d fedora-moo

Finally, verify the output with (be sure to replace the IP address and container ID with the ones from your system):

    sudo podman ps
    sudo podman inspect -f '{{ .NetworkSettings.IPAddress }}' f711
    curl http://172.16.16.9

