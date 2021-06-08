# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.0.0, ansible-base 2.11.1

Run this playbook with the following commands:

    ansible-playbook -i mastery-hosts -c local mastery.yaml
    ansible-playbook -i mastery-hosts -c local --limit frontend mastery.yaml
