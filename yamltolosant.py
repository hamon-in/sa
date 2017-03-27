from losantrest import Client
import yaml

client = Client()
creds = {
    'deviceId': '58d4b19d3cc88e00018ee148',
    'key': 'aa668b98-b15e-419f-b567-a9fc5c0323c9',
    'secret': '68eed06c85d53626f71664f14abefd7a1fe4d9ed484583185f8092b5a81777bb'
}
response = client.auth.authenticate_device(credentials=creds)
client.auth_token = response['token']
app_id = response['applicationId']

with open("logger.yaml") as f:
    data = yaml.load(f)
    for d in data['devices']:
        d["registers_to_log"] = str(d['registers_to_log'])
        d["registers"] = str(d['registers'])        
        state = dict(data=d)
        response = client.device.send_state(deviceId='58d4b19d3cc88e00018ee148',
                                            applicationId=app_id, deviceState=state)
        print(response)
