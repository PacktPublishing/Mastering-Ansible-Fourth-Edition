# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.0.0, ansible-base 2.11.1

Run this playbook using the commands:

    ansible-playbook -i mastery-hosts includer.yaml -v
    ansible-playbook -i mastery-hosts includer.yaml -v -e foo=false
