# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.3.0, ansible-core 2.11.3

This example requires you to edit a core Ansible file - it might be worth making a backup before proceeding. Also be sure to reverse any changes you made in the previous example before attempting this one.

The path below is an example only - the exact path with depend upon your system and how you installed Ansible - refer to Chapter 9 of the book for more details on how to locate this path.

    sudo vim /usr/local/lib/python3.8/dist-packages/ansible/playbook/__init__.py

Add the following line just below the for loop for `get_all_plugin_loaders` as shown in the book:

    import pdb; pdb.set_trace()

Now run the playbook as we did before:

    ansible-playbook -i mastery-hosts objmethod.yaml

Test out the interactive debug session as described in the book.

Reverse all changes to the Ansible core files when complete.
