# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.3.0, ansible-core 2.11.3
- Cumulus VX 4.4.0

Adjust the inventory file to suit your setup, and then test with:

    ansible -i switch-inventory -m ansible.builtin.ping mastery-switch1

We can then query the switch using this playbook:

    ansible-playbook -i switch-inventory switch-query.yaml

Ports can then be configured using this playbook as discussed in the book:

    ansible-playbook -i switch-inventory switch-l2-configure.yaml
