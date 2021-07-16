#!/usr/bin/python 
# 
import shutil 

DOCUMENTATION = ''' 
--- 
module: remote_copy 
version_added: future 
short_description: Copy a file on the remote host 
description: 
  - The remote_copy module copies a file on the remote host from a given source to a provided destination. 
options: 
  source: 
    description: 
      - Path to a file on the source file on the remote host 
    required: True 
  dest: 
    description: 
      - Path to the destination on the remote host for the copy 
    required: True 
author: 
  - Jesse Keating 
''' 
EXAMPLES = ''' 
# Example from Ansible Playbooks 
- name: backup a config file 
  remote_copy: 
    source: /etc/herp/derp.conf 
    dest: /root/herp-derp.conf.bak 
''' 
RETURN = ''' 
source: 
  description: source file used for the copy 
  returned: success 
  type: string 
  sample: "/path/to/file.name" 
dest: 
  description: destination of the copy 
  returned: success 
  type: string 
  sample: "/path/to/destination.file" 
gid: 
  description: group ID of destination target 
  returned: success 
  type: int 
  sample: 502 
group: 
  description: group name of destination target 
  returned: success 
  type: string 
  sample: "users" 
uid: 
  description: owner ID of destination target 
  returned: success 
  type: int 
  sample: 502 
owner: 
  description: owner name of destination target 
  returned: success 
  type: string 
  sample: "fred"
mode: 
  description: permissions of the destination target 
  returned: success 
  type: int 
  sample: 0644 
size: 
  description: size of destination target 
  returned: success 
  type: int 
  sample: 20 
state: 
  description: state of destination target 
  returned: success 
  type: string 
  sample: "file" 
''' 
def main(): 
    module = AnsibleModule( 
        argument_spec = dict( 
            source=dict(required=True, type='str'), 
            dest=dict(required=True, type='str') 
        ) 
    ) 
    shutil.copy(module.params['source'], 
                module.params['dest']) 
    facts = {'rc_source': module.params['source'], 
             'rc_dest': module.params['dest']} 
 
    module.exit_json(changed=True, ansible_facts=facts) 
from ansible.module_utils.basic import * 
if __name__ == '__main__': 
    main() 

