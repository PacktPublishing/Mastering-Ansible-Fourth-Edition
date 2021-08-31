# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.3.0, ansible-core 2.11.3

To create the empty repository to be used for testing this playbook, you can run the following commands:

    sudo mkdir -p /srv/app
    sudo chown $USER /srv/app
    cd /srv/app
    git init
    git commit --allow-empty -m "initial commit"

Run this playbook using the command:

    ansible-playbook -i mastery-hosts error.yaml -v
