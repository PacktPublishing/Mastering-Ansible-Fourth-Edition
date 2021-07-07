# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.0.0, ansible-base 2.11.1

Edit this core Ansible file (this time by copying to a local `library/` directory first):

    mkdir library
    cp /usr/local/lib/python3.8/dist-packages/ansible/modules/systemd.py library/

Insert the following line as shown in the accompanying book:

    import rpdb; rpdb.set_trace(addr="0.0.0.0")

Edit the accompanying inventory to match your test host, then run the playbook:

    ansible-playbook -i mastery-debug rpdb.yaml -vv

Once the playbook is running, it will appear to hang. At this point you can telnet into the remote host on port 4444 and use rpdb as described in the book.

