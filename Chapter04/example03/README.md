# Instructions

Tested on:
- Windows Server 2019, Version 1809, Build 17763.1817

Ensure the WinRM Python module is installed on your Ansible host:

    sudo apt install python3-winrm

or:

    sudo pip install "pywinrm>=0.3.0"

Edit the inventory to suit your environment (password, IP address of Windows host) and then run the following command to test connectivity:

    ansible -i windows-hosts -m ansible.windows.win_ping all

