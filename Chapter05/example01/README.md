# Instructions

Tested on:
- Ubuntu Server 20.04 LTS
- microk8s v1.20.6

Below are the commands referenced in the book to install AWX:

    sudo snap install microk8s --classic
    sudo gpasswd -a $USER microk8s
    
Log out and back in

    for i in storage dns ingress; do microk8s enable $i; done
    microk8s kubectl apply -f https://raw.githubusercontent.com/ansible/awx-operator/devel/deploy/awx-operator.yaml
    microk8s kubectl get pods
    openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout awx.key -out awx.crt -subj "/CN=awx.example.org/O=mastery" -addext "subjectAltName = DNS:awx.example.org"
    microk8s kubectl create secret tls awx-secret-ssl --namespace default --key awx.key --cert awx.crt
    microk8s kubectl create -f my-awx-storage.yml
    microk8s kubectl apply -f my-awx.yml
    microk8s kubectl get pods
    microk8s kubectl apply -f my-awx-ingress.yml
    microk8s kubectl describe ingress

If needed delete and reapply the ingress configuration to ensure the CREATE event is present:

    microk8s kubectl delete -f my-awx-ingress.yml
    microk8s kubectl apply -f my-awx-ingress.yml
    microk8s kubectl describe ingress

    microk8s kubectl get secret awx-admin-password -o jsonpath='{.data.password}' | base64 --decode

