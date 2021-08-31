# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.3.0, ansible-core 2.11.3

Run this playbook using the command:

    time ansible-playbook -i mastery-inventory.py inventory_test.yaml --limit backend,frontend,errors
