# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 3.0.0, ansible-base 2.10.6

Ensure `password.sh` is executable:

    chmod +x password.sh

Try encrypting the included vars file using the command:

    ansible-vault encrypt --vault-id ./password.sh a_vars_file.yaml

Check the contents:

    cat a_vars_file.yaml

