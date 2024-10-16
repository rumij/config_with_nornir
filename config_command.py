from netmiko import ConnectHandler
import pandas as pd

dev = pd.read_excel('inventory.xlsx')
device = dev.to_dict(orient='records')
devi = device[0]
print(devi)


with ConnectHandler(**devi) as de:
    cmd = ['interface gig1/0/1','descri config by netmikok']
    config_output = de.send_config_set(config_commands=cmd)
    print(config_output)
    save_output = de.save_config()
    print(save_output)
