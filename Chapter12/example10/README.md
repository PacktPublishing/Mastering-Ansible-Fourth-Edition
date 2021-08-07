# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.3.0, ansible-core 2.11.3
- Docker version 20.10.8

Locate the Docker dynamic inventory script on your filesystem (e.g. `locate docker.py`)

You can test it as shown in the book with these commands:

    python3 /usr/local/lib/python3.8/dist-packages/ansible_collections/community/general/scripts/inventory/docker.py --help
    python3 /usr/local/lib/python3.8/dist-packages/ansible_collections/community/general/scripts/inventory/docker.py --list --pretty | grep -C2 playbook-container


