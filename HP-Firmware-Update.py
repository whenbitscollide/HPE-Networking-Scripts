
# coding: utf-8

# In[ ]:

# Tell the script what to use
from netmiko import ConnectHandler
from datetime import datetime
import time


# In[ ]:

# Variables
ip_addr01 = '10.40.1.11'
ip_addr02 = '10.40.1.13'
ip_addr03 = '10.40.1.14'
#ip_addr04 = '10.0.0.13'
#ip_addr05 = '10.0.0.14'
#ip_addr06 = '10.0.0.15'
#ip_addr07 = '10.0.0.16'
#ip_addr08 = '10.0.0.17'
#ip_addr09 = '10.0.0.18'
#ip_addr10 = '10.0.0.19'
#ip_addr11 = '10.0.0.20'
#ip_addr12 = '10.0.0.21'
#ip_addr13 = '10.0.0.22'
#ip_addr14 = '10.0.0.23'
#ip_addr15 = '10.0.0.24'
#ip_addr16 = '10.0.0.25' 
    


# In[ ]:

# Define Devices (In the future, this'll be defined in a separate sheet)
# For factory default switches = username:'manager', password:'\n'
hp1 = {
'device_type': 'hp_procurve',
'ip': ip_addr01,
'username': 'manager',
'password': '\n',
}

hp2 = {
'device_type': 'hp_procurve',
'ip': ip_addr02,
'username': 'manager',
'password': '\n',
}

hp3 = {
'device_type': 'hp_procurve',
'ip': ip_addr03,
'username': 'manager',
'password': '\n',
}

#hp4 = {
#'device_type': 'hp_procurve',
#'ip': ip_addr04,
#'username': 'manager',
#'password': '\n',
#}
#
#hp5 = {
#'device_type': 'hp_procurve',
#'ip': ip_addr05,
#'username': 'manager',
#'password': '\n',
#}
#
#hp6 = {
#'device_type': 'hp_procurve',
#'ip': ip_addr06,
#'username': 'manager',
#'password': '\n',
#}
#
#hp7 = {
#'device_type': 'hp_procurve',
#'ip': ip_addr07,
#'username': 'manager',
#'password': '\n',
#}
#
#hp8 = {
#'device_type': 'hp_procurve',
#'ip': ip_addr08,
#'username': 'manager',
#'password': '\n',
#}
#
#hp9 = {
#'device_type': 'hp_procurve',
#'ip': ip_addr09,
#'username': 'manager',
#'password': '\n',
#}
#
#hp10 = {
#'device_type': 'hp_procurve',
#'ip': ip_addr10,
#'username': 'manager',
#'password': '\n',
#}
#
#hp11 = {
#'device_type': 'hp_procurve',
#'ip': ip_addr11,
#'username': 'manager',
#'password': '\n',
#}
#
#hp12 = {
#'device_type': 'hp_procurve',
#'ip': ip_addr12,
#'username': 'manager',
#'password': '\n',
#}
#
#hp13 = {
#'device_type': 'hp_procurve',
#'ip': ip_addr13,
#'username': 'manager',
#'password': '\n',
#}
#
#hp14 = {
#'device_type': 'hp_procurve',
#'ip': ip_addr14,
#'username': 'manager',
#'password': '\n',
#}
#
#hp15 = {
#'device_type': 'hp_procurve',
#'ip': ip_addr15,
#'username': 'manager',
#'password': '\n',
#}
#
#hp16 = {
#'device_type': 'hp_procurve',
#'ip': ip_addr16,
#'username': 'manager',
#'password': '\n',
#}


# In[ ]:

# Group devices into one variable
all_devices = [hp1, hp2] #hp3] #hp4, hp5, hp6, hp7, hp8, hp9, hp10, hp11, hp12, hp13, hp14, hp15, hp16]


# In[ ]:

# Gets current date and time and prints it at the top of the output file
start_time = datetime.now()
print ("Start Time = {}".format(start_time))


# In[ ]:

# SSH to each device listed in "all_devices"
# Once SSH is established, net_connect will send the specified command(s)
# The text from the sent command will be stored in the variable "output
# "Print" will paste all of the stored info from output
for a_device in all_devices:
    net_connect = ConnectHandler(**a_device)
    print('\n\n>>>Starting Firmware Update on {0}<<<'.format(a_device['ip']))
    output = net_connect.send_command("copy tftp flash 10.10.1.174 test.swi pri")
    time.sleep(3)
    output += net_connect.send_command("y")
    print('\n\n>>>Waiting 2 Minutes for Download on {0}<<<'.format(a_device['ip']))
    time.sleep(120)
    #while net_connect.find_prompt() != "'HP-2530-8-PoEP#'":
    #    print("The firmware download will be done momentarily")
    #    time.sleep(10)
    if net_connect.find_prompt() == "'HP-2530-8-PoEP#'":
        shflash = net_connect.send_command("show flash")
        print(shflash)
    else:
        print('\n\n>>>Waiting 1 Minute for Install Completion<<<')
        time.sleep(60)
    print('\n\n>>Firmware Update Complete - Reloading {0}<<<'.format(a_device["ip"]))
    reload = net_connect.send_command("reload")
    time.sleep(3)
    reload += net_connect.send_command('y')
    #print ("\n\n>>>>>>>>> Device {0} <<<<<<<<<".format(a_device['ip']))
    #print (output)
    #print (">>>>>>>>> End <<<<<<<<<")


# In[ ]:

# This'll print the total time it took for this script to complete
end_time = datetime.now()
total_time = end_time - start_time
print ("Total Time = {}".format(total_time))

