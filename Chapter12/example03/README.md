# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.3.0, ansible-core 2.11.3
- OpenStack devstack - git tag kilo-2-4718-ge937dcb7

Run this playbook using the command (assumes prior setup of OpenStack - adjust the playbook according to your environment):

    export ANSIBLE_PYTHON_INTERPRETER=$(which python3)
    ansible-playbook -i mastery-hosts boot-server.yaml --private-key mastery-key

Note that `mastery-key` should be the private SSH key created in and then downloaded from your OpenStack environment.

Log into your OpenStack VM using a command similar to that below (being sure to reference your own key, and the appropriate IP address), and query the RPM database using the command provided:

    ssh -i mastery-key fedora@172.24.4.81
    rpm -qa --last | head

