# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.3.0, ansible-core 2.11.3

Run this playbook with the following command:

    ansible-playbook -i mastery-hosts -c local --limit frontend mastery.yaml
