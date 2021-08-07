# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.3.0, ansible-core 2.11.3
- OpenStack devstack - git tag kilo-2-4718-ge937dcb7

Run this playbook using the command (assumes prior setup of OpenStack - adjust the playbook according to your environment):

    export ANSIBLE_PYTHON_INTERPRETER=$(which python3)
    ansible-playbook -i mastery-hosts boot-server.yaml -vv
