# Instructions

Tested on:
- Windows Server 2019, Version 1809, Build 17763.1817
- Ubuntu Server 20.04
- Ansible 4.3.0, ansible-core 2.11.3

Check for available installation candidates for OpenSSH on Windows in PowerShell:
    Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'

Assuming a suitable candidate is shown, install and configure it with the following PowerShell commands:

    Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
    Start-Service sshd
    Set-Service -Name sshd -StartupType 'Automatic'
    Get-NetFirewallRule -Name *ssh*
    New-ItemProperty -Path 'HKLM:\SOFTWARE\OpenSSH' -Name 'DefaultShell' -Value 'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'

Now you can run an Ansible ansible.windows.win_ping adhoc command just as we have done before:

    ansible -i windows-host -m ansible.windows.win_ping all

