# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 3.0.0, ansible-base 2.10.6

Run this playbook using the command:

    ansible-playbook -i mastery-hosts template-demo-v2.yaml
    ansible-playbook -i mastery-hosts template-demo-v2.yaml -e '{api: {"v2": false}}'
