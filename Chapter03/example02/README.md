# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.3.0, ansible-core 2.11.3

Create a password file for your new Vault using the command:

    echo "my long password" > password_file

Then run this command to create the vault:

    ansible-vault create --vault-id ./password_file more_secrets.yaml

Later try decrypting this with:

    ansible-vault decrypt --vault-id ./password_file more_secrets.yaml

Check the contents to ensure decryption was successful.
