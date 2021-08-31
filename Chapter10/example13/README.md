# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.3.0, ansible-core 2.11.3

Run these commands to prepare for the code tests:

    sudo apt install python3-pytest python3-tz python3-pytest-mock python3-pycodestyle

Run these commands to perform the code tests described in the book:

    mkdir ~/devel
    cd ~/devel
    git clone https://github.com/ansible/ansible.git
    cd ansible
    source ./hacking/env-setup
    pytest-3 test/units/parsing
    ansible-test integration --python 3.8 ping
    ansible-test integration shippable/ --docker fedora32
    ansible-test sanity --test pep8

Mix tabs and spaces on a line of your choosing in a file such as: `lib/ansible/modules/file.py`

    ansible-test sanity --test pep8

