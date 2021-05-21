# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 3.0.0, ansible-base 2.10.6

Run this command:

    ansible-vault create --vault-id @prompt secrets.yaml

Then insert the following data into the Vault:

    ---
    my_secret: is_safe

You can try and read the resulting file with:

    cat secrets.yaml


