# Instructions

Tested on:
- Ubuntu Server 20.04
- Ansible 4.3.0, ansible-core 2.11.3
- OpenStack devstack - git tag kilo-2-4718-ge937dcb7

Create an appropriate `clouds.yaml` file for your environment - for example:

```yaml
clouds:
  mastery_cloud:
    auth:
      auth_url: "http://10.0.50.32/identity/v3"
      username: "demo"
      password: "password"
      project_name: "demo"
      project_domain_name: "default"
      user_domain_name: "default"
```

Also create an `openstack.yaml` as follows:

```yaml
# file must be named openstack.yaml or openstack.yml
plugin: openstack.cloud.openstack
expand_hostvars: yes
fail_on_errors: yes
all_projects: yes
```

Test this dynamic inventory provider as described in the book:

    python3 /usr/local/lib/python3.8/dist-packages/ansible_collections/openstack/cloud/scripts/inventory/openstack_inventory.py --list

Then when you are happy it is working, run the playbook against this inventory:

    ansible-playbook -i openstack.yaml configure-server.yaml --private-key mastery-key

