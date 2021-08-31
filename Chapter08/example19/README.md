# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.3.0, ansible-core 2.11.3

The examples in this part of the chapter use the following commands:

    mkdir roles/
    ansible-galaxy role install -p roles/ angstwad.docker_ubuntu
    ansible-galaxy role list -p roles/
    ansible-galaxy role info -p roles/ angstwad.docker_ubuntu
    cat roles/angstwad.docker_ubuntu/meta/main.yml
    ansible-galaxy role init --help
    ansible-galaxy role init --init-path roles/ autogen
    tree roles/autogen

The following commands are theoretical - modify the repository URL and parameters to test:

    ansible-galaxy role install -p /opt/ansible/roles git+git@git.internal.site:ansible-roles/foowhiz
    ansible-galaxy role install -p /opt/ansible/roles git+git@git.internal.site:ansible-roles/foowhiz,v1
    ansible-galaxy role install -p /opt/ansible/roles git+git@git.internal.site:ansible-roles/foowhiz,,foo-whiz-common
    ansible-galaxy role install -r foowhiz-reqs.yaml
    
