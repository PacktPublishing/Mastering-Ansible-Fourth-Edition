#!/usr/bin/python 
# 
import shutil 
def main(): 
    module = AnsibleModule( 
        argument_spec = dict( 
            source=dict(required=True, type='str'), 
            dest=dict(required=True, type='str') 
        ) 
    ) 
    shutil.copy(module.params['source'], 
                module.params['dest']) 
    module.exit_json(changed=True) 
from ansible.module_utils.basic import * 
if __name__ == '__main__': 
    main() 

