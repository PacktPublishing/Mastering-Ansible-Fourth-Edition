# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.3.0, ansible-core 2.11.3

Run these commands:

    ansible-galaxy collection install amazon.aws
    sudo apt install python3-boto3 python3-botocore

Now optionally install the ```awscli``` so that you can configure your credentials for the dynamic inventory plugin.

    sudo apt install awscli
    aws configure

Once you have set your default AWS credentials as described in the book run:

    ansible-inventory -i mastery_aws_ec2.yml --graph


If you have any virtual instances defined in EC2, you will see them listed in the output.


