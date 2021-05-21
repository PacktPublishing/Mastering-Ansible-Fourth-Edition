# Instructions
  
Tested on:
- Ubuntu Server 20.04 LTS
- microk8s v1.20.6

For easy copy and paste, here are the `curl` commands used in the book to work with the AWX API. Remember to substitute the FQDN and credentials of your AWX server when running the commands:

     curl -k -s --user admin:adminpassword -X GET https://awx.example.org/api/v2/inventories/ | python -m json.tool

     curl -k -s --user admin:adminpassword -X GET https://awx.example.org/api/v2/job_templates/ | python -m json.tool

     curl -k -s --user admin:adminpassword -X POST -H 'Content-Type:application/json' https://awx.example.org/api/v2/job_templates/12/launch/ --data '{"extra_vars": "{\"http_port\": 80}"}' | python -m json.tool

     curl -k -s --user admin:adminpassword -X GET https://awx.example.org/api/v2/jobs/11/ | python -m json.tool

     curl -k -s --user admin:adminpassword -X GET https://awx.example.org/api/v2/jobs/11/stdout/

