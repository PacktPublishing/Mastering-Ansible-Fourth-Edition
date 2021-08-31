# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.3.0, ansible-core 2.11.3
- Cumulus VX 4.4.0

This example assumes you already have a jump host set up with hostname `bastion01` and key based SSH authentication set up between this host and the jump host. When this is in place:

    ansible -i switch-inventory -m ansible.builtin.ping mastery-switch1

We can then query the switch using this playbook:

    ansible-playbook -i switch-inventory switch-query.yaml

Ports can then be configured using this playbook as discussed in the book:

    ansible-playbook -i switch-inventory switch-l2-configure.yaml
