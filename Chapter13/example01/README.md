# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.3.0, ansible-core 2.11.3

Note this is a theoretical example - it will need parameters changing if you have an F5 BIG-IP device to test with:

    sudo pip install ipaddress
    ansible-playbook -i mastery-hosts reset-f5.yaml
