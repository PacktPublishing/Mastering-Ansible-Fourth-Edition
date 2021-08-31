# Instructions

Tested on:
- Windows Server 2019, Version 1809, Build 17763.1817
- Ubuntu Server 20.04
- Ansible 4.3.0, ansible-core 2.11.3

Installing Kerberos support on the Ansible host:

    sudo apt-get install python3-dev libkrb5-dev krb5-user

Edit `/etc/krb5.conf` as detailed in the book. Then test with (modify to suit your Active Directory domain):

    kinit Administrator@MASTERY.EXAMPLE.COM
    klist

Modify the enclosed inventory to suit your environment. Then test connectivity with:

    ansible -i windows-hosts -m ansible.windows.win_ping all

