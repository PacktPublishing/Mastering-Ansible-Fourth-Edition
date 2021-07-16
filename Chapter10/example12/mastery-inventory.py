#!/usr/bin/env python 
# 
import json 
import argparse 
inventory = {} 
inventory['web'] = {'hosts': ['mastery.example.name'], 
                    'vars': {'http_port': 80, 
                             'proxy_timeout': 5}} 
inventory['dns'] = {'hosts': ['backend.example.name']} 
inventory['database'] = {'hosts': ['backend.example.name'], 
                         'vars': {'ansible_ssh_user': 'database'}} 
inventory['frontend'] = {'children': ['web']} 
inventory['backend'] = {'children': ['dns', 'database'], 
                        'vars': {'ansible_ssh_user': 'blotto'}} 
inventory['errors'] = {'hosts': ['scsihost']} 
inventory['failtest'] = {'hosts': ["failer%02d" % n for n in 
                                   range(1,11)]} 
allgroupvars = {'ansible_ssh_user': 'otto'} 
hostvars = {} 
hostvars['mastery.example.name'] = {'ansible_ssh_host': '192.168.10.25'} 
hostvars['scsihost'] = {'ansible_ssh_user': 'jfreeman'} 

agghostvars = dict()
for outergroup in inventory:
    for grouphost in inventory[outergroup].get('hosts', {}):
        agghostvars[grouphost] = allgroupvars.copy()
        for group in inventory:
            if grouphost in inventory[group].get('hosts', {}):
                for childgroup in inventory:
                    if group in inventory[childgroup].get('children', {}):
                        agghostvars[grouphost].update(inventory[childgroup].get('vars', {}))
        for group in inventory:
            if grouphost in inventory[group].get('hosts', {}):
                agghostvars[grouphost].update(inventory[group].get('vars', {}))
        agghostvars[grouphost].update(hostvars.get(grouphost, {}))

inventory['_meta'] = {'hostvars': agghostvars}

parser = argparse.ArgumentParser(description='Simple Inventory') 
parser.add_argument('--list', action='store_true', help='List all hosts') 
parser.add_argument('--host', help='List details of a host') 
args = parser.parse_args() 
if args.list: 
    for group in inventory: 
        ag = allgroupvars.copy() 
        ag.update(inventory[group].get('vars', {})) 
        inventory[group]['vars'] = ag 
    print(json.dumps(inventory)) 
elif args.host:
    raise StandardError("You've been a bad person")
