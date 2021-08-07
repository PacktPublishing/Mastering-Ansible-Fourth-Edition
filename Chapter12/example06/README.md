# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.3.0, ansible-core 2.11.3
- Microsoft Azure

To run this example, you will need an Azure account, and your credentials for this. Put your credentials where indicated into the playbook, then run it with the command:

    ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i mastery-hosts boot-azure-server.yaml

Note the setup commands you may need from the book before this will run, including:

    locate requirements-azure.txt
    sudo pip3 install -r /usr/local/lib/python3.8/dist-packages/ansible_collections/azure/azcollection/requirements-azure.txt
    curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
    az login
    az vm image list --offer fedora --all --output table
    az vm image show --urn tunnelbiz:fedora:fedoraupdate:34.0.1
    az vm image terms accept --urn tunnelbiz:fedora:fedoraupdate:34.0.1

