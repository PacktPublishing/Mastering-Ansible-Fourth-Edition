# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.3.0, ansible-core 2.11.3
- Amazon EC2

To get this example running on Ubuntu Server 20.04, you may need to install the boto3 module for Python3, and then ensure that Ansible uses your Python 3 environment using the following commands:

    sudo apt install python3-boto3
    export ANSIBLE_PYTHON_INTERPRETER=$(which python3)

To run this example, you will need an AWS account, and your credentials for this. Put your credentials where indicated into the playbook, then run it with the command:

    ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i mastery-hosts boot-ec2-server.yaml --private-key mastery-key.pem

Where mastery-key.pem is your private SSH key downloaded from the keypair you created in EC2.

