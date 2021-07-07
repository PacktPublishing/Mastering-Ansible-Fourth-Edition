# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.0.0, ansible-base 2.11.1

Run this playbook using the command:

    ansible-playbook -i mastery-hosts objmethod.yaml

In the interactive debug session, run the following commands (full explanation of these commands is in the accompanying book):

    p task
    p task.args
    task_vars['derp']['missing'] = "the end"
    r

