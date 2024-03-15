import json


with open('C:/Users/madina.myrzakhan/Desktop/pp2/tsis4/sample-data.json') as file:
    data = json.load(file)

total_count = data['totalCount']

interfaces = []
for item in data['imdata']:
    interface = item['l1PhysIf']['attributes']
    interfaces.append(interface)

print(f"Count: {total_count}\n")

for interface in interfaces:
    dn = interface['dn']
    admin_st = interface['adminSt']
    speed = interface['speed']
    mtu = interface['mtu']

    print("Interface:")
    print(f"DN: {dn}")
    print(f"Status {admin_st}")
    print(f"Speed: {speed}")
    print(f"MTU: {mtu}")
    print()