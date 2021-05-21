# Instructions

Tested on:
- Ubuntu Server 20.04 LTS
- microk8s v1.20.6

With AWX installed, locate the persistent volume claim directory on the local host using the commands:

    microk8s kubectl get pods -A | awk '/hostpath/ {print $2}'

Using the output from the above command, run the following command and replace the string 'hostpath-provisioner-5c65fbdb4ff' with the value from the previous command.

    microk8s kubectl describe -n kube-system pod/hostpath-provisioner-5c65fbdb4f-jcq8b | awk '/PV_DIR/ {print $2}'
    microk8s kubectl describe pvc/awx-pvc | awk '/Volume:/ {print $2}'

Copy the included `example.yaml` into this directory (note the actual directory will be different on your system - use the output from the above commands to get the exact one:

    sudo cp example.yaml /var/snap/microk8s/common/default-storage/default-awx-pvc-pvc-52ea2e69-f3c7-4dd0-abcb-2a1370ca3ac6/
