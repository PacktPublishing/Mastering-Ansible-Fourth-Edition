# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.3.0, ansible-core 2.11.3

Run this playbook with the following commands:

    ansible-playbook -i mastery-hosts -c local mastery.yaml
    ansible-playbook -i mastery-hosts -c local --limit frontend mastery.yaml
