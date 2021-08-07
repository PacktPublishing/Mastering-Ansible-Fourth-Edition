# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.3.0, ansible-core 2.11.3
- Docker version 20.10.8

You can check if any related Docker containers are already in existence using the following commands:

    docker ps -a --filter ancestor=fedora-moo
    docker images --filter reference='fedora*'

Next, ensure you have Docker support installed for your Python environment - on my demo system I used the following commands:

    sudo apt install python3-docker
    export ANSIBLE_PYTHON_INTERPRETER=$(which python3)

Then run the playbook as follows to build and run the container:

    ansible-playbook -i mastery-hosts docker-interact.yaml 

Now run the two Docker queries again to see the running container:

    docker ps -a --filter ancestor=fedora-moo
    docker images --filter reference='fedora*'

Also check the container is running with:

    curl http://localhost:8080

