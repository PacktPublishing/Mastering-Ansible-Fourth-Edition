# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.0.0, ansible-base 2.11.1

This example requires you to edit a core Ansible file - it might be worth making a backup before proceeding. Also be sure to reverse any changes you made in the previous example before attempting this one.

    sudo vim /usr/local/lib/python3.8/dist-packages/ansible/executor/playbook_executor.py

Add the following line just above the call to `set_default_transport` as shown in the book:

    import pdb; pdb.set_trace()

Now run the playbook as we did before:

    ansible-playbook -i mastery-hosts objmethod.yaml

Test out the interactive debug session as described in the book. The commands given in the book are:

    step
    list
    step
    step
    step
    step
    step
    n
    n
    n
    n
    n
    l
    n
    n
    n
    n
    p err

Reverse all changes to the Ansible core files when complete.
