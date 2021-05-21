# Instructions

Tested on:
- Windows Server 2019, Version 1809, Build 17763.1817

Run this command:

    Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux

If installing Linux without the aid of the Windows Store:

    Invoke-WebRequest -Uri https://aka.ms/wslubuntu2004 -OutFile Ubuntu.appx -UseBasicParsing

    Rename-Item Ubuntu.appx Ubuntu.zip
    Expand-Archive Ubuntu.zip C:\WSL\Ubuntu

    C:\WSL\Ubuntu\ubuntu.exe


