# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.0.0, ansible-base 2.11.1

Ensure `password.sh` is executable:

    chmod +x password.sh

Try encrypting the included vars file using the command:

    ansible-vault encrypt --vault-id dev@./password.sh a_vars_file.yaml

Now run the playbook:

    ansible-playbook -i mastery-hosts --vault-id dev@./password.sh showme.yaml

