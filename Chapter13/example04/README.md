# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.3.0, ansible-core 2.11.3
- Arista vEOS 4.26.2F
- Cumulus VX 4.4.0

Adjust the inventory file to suit your setup, and then run the playbook with:

    ansible-playbook -i switch-inventory switch-facts.yaml

