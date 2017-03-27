from losantrest import Client
import yaml
import json

def yamltolosant(filename):
    op_data = {}
    client = Client()
    app_responce=client.auth.authenticate_user(credentials={'email':'abukmca@gmail.com','password':'MY1losant'})
    app_token = app_responce['token']
    app_client=Client(auth_token=app_token, url="https://api.losant.com")
    
    mydevice = { "name": "My New Device ","description": "Description of my new device",
                 "tags": [{"key": "TagKey","value": "TagValue"}],
                 "attributes": [ { "name": "asset","dataType": "string"},{"name":"logger","dataType":"string"},
                                 {"name":"channel","dataType":"string"},{"name":"cycle","dataType":"number"},
                                 {"name":"class","dataType":"string"},{"name":"device_config","dataType":"string"},
                                 {"name":"ipaddr","dataType":"string"},{"name":"unit","dataType":"number"},
                                 {"name":"registers","dataType":"string"},{"name":"registers_to_log","dataType":"string"},
                                 {"name":"publish","dataType":"boolean"}],
                 "deviceClass": "standalone"
             }


    with open (filename) as f:
        data = yaml.load(f)
        for d in data['devices']:
            mydevice["name"] = d["asset"]+"name"
            new_device = app_client.devices.post(applicationId='58d4af606ef59c000177475a',device=mydevice)
            device_id = new_device['deviceId']
            op_data[mydevice["name"]]=device_id
            creds = {
                'deviceId': device_id,
                'key': 'aa668b98-b15e-419f-b567-a9fc5c0323c9',
                'secret': '68eed06c85d53626f71664f14abefd7a1fe4d9ed484583185f8092b5a81777bb'
            }
            response = client.auth.authenticate_device(credentials=creds)
            client.auth_token = response['token']
            app_id = response['applicationId']
            d["registers_to_log"] = str(d['registers_to_log'])
            d["registers"] = str(d['registers'])        
            state = dict(data=d)
            response = client.device.send_state(deviceId=device_id,
                                                applicationId=app_id, deviceState=state)
            print(response)
    op_data = json.dumps(op_data)
    with open("new_device_info.json", "w") as f:
        f.write(op_data)
        print("New devices created the details are in new_device_info.json file")

