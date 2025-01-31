### Prerequisite

Python 3.11+


### Example
```
import json
from scpapi.virtual_server import VirtualServer


virtual_server = VirtualServer(
    project_id='PROJECT-XXXXXXXXXXXXXXXXXXXXXX',
    access_key='XXXXXXXXXXXXXXXXXXXX',
    secret_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
)

### List of Virtual Server ###
vm_list = json.loads(virtual_server.list().text)
print(vm_list['contents'])

### Create a Virtual Server ###
virtual_server_body = {
    'virtualServerName': 'slurm-head',
    'blockStorage': {
        'blockStorageName': 'root',
        'diskSize': 100,
        'encryptEnabled': False,
        'diskType': 'SSD'
    },
    'imageId': 'IMAGE-9DNNuuBDrMcKq8kfr29xjm',
    'nic': {
        'subnetId': 'SUBNET-lr6CTHHQs2mQNdIZ9VK2-m',
        'natEnabled': True,
        'publicIpId' : 'PUBLIC_IP-avsFAjQPrNmJ--JFfLW9ei'
    },
    'deletionProtectionEnabled': False,
    'securityGroupIds': ['FIREWALL_SECURITY_GROUP-rj5TNm2VsXcOYbM04lvWah'],
    'serverType': 's1v2m4',
    'serviceZoneId': 'ZONE-FClPklmysrhRpknZ6DaI2f',
    'serverGroupId': 'SERVICE-Aj3ONjl2qEkTs_7ccYAPjo',
    'tags': [
        {'tagKey': 'cluster-name', 'tagValue': 'slurm-cluster'},
    ],
    'keyPairId': 'KEY_PAIR-t4ZeTus1q2lHpYZ1yICLEa'
}

print(virtual_server.create(body=virtual_server_body).text)
```