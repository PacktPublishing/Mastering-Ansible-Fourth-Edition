# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.0.0, ansible-base 2.11.1

Run this playbook using the command:

    time ansible-playbook -i mastery-inventory.py inventory_test.yaml --limit backend,frontend,errors
