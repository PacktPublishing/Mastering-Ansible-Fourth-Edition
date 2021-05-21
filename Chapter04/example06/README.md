# Instructions

Tested on:
- Windows Server 2019, Version 1809, Build 17763.1817
- Ubuntu Server 20.04

Import your CA signed certificate into the Windows Certificate store:

    Import-Certificate -FilePath .\certnew.cer -CertStoreLocation Cert:\LocalMachine\My

Delete any previously created WinRM listeners:

    winrm delete winrm/config/Listener?Address=*+Transport=HTTPS

Create a new HTTPS listener referring to the new CA signed certificate:

    New-Item -Path WSMan:\Localhost\Listener -Transport HTTPS -Address * -CertificateThumbprint <thumbprint of certificate>

Place a copy of the Base64 encoded CA certificate for the above in `/usr/share/ca-certificates/` on the Ansible host, ensuring the filename has the extension `.crt`. Then run:

    sudo dpkg-reconfigure ca-certificates

Answer `Yes` when asked if you want to trust certificates from new certificate authorities, and ensure you select your newly added certificate from the list.

Finally, update the enclosed inventory with the correct details for your Windows host and run the following command to test Ansible connectivity:

    ansible -i windows-hosts -m ansible.windows.win_ping all
