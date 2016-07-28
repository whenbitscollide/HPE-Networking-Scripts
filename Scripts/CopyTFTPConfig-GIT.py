# Tell the script what modules to use
from netmiko import ConnectHandler
from datetime import datetime
import time

# Variables
ip_addr01 = '10.31.1.101'
ip_addr02 = '10.31.1.102'
ip_addr03 = '10.31.1.103'
ip_addr04 = '10.31.1.104'
ip_addr05 = '10.31.1.105'
ip_addr06 = '10.31.1.106'
ip_addr07 = '10.31.1.107'
ip_addr08 = '10.31.1.108'
ip_addr09 = '10.31.1.109'
ip_addr10 = '10.31.1.110'
ip_addr11 = '10.31.1.111'
ip_addr12 = '10.31.1.112'
ip_addr13 = '10.31.1.113'
ip_addr14 = '10.31.1.114'
ip_addr15 = '10.31.1.115'
ip_addr16 = '10.31.1.116'
ip_addr17 = '10.31.1.117'
ip_addr18 = '10.31.1.118'
ip_addr19 = '10.31.1.119'
ip_addr20 = '10.31.1.120'
ip_addr21 = '10.31.1.121'
ip_addr22 = '10.31.1.122'
ip_addr23 = '10.31.1.123'
ip_addr24 = '10.31.1.124'
ip_addr25 = '10.31.1.125'
ip_addr26 = '10.31.1.126'
ip_addr27 = '10.31.1.127'
ip_addr28 = '10.31.1.128'
ip_addr29 = '10.31.1.129'
ip_addr30 = '10.31.1.130'
ip_addr31 = '10.31.1.131'
ip_addr32 = '10.31.1.132'
ip_addr33 = '10.31.1.133'
ip_addr34 = '10.31.1.134'
ip_addr35 = '10.31.1.135'

# Create a dictionary for the devices
hp1 = {
'device_type': 'hp_procurve',
'ip': ip_addr01,
'username': "",
'password': "",
}

hp2 = {
'device_type': 'hp_procurve',
'ip': ip_addr02,
'username': "",
'password': "",
}

hp3 = {
'device_type': 'hp_procurve',
'ip': ip_addr03,
'username': "",
'password': "",
}

hp4 = {
'device_type': 'hp_procurve',
'ip': ip_addr04,
'username': "",
'password': "",
}

hp5 = {
'device_type': 'hp_procurve',
'ip': ip_addr05,
'username': "",
'password': "",
}

hp6 = {
'device_type': 'hp_procurve',
'ip': ip_addr06,
'username': "",
'password': "",
}

hp7 = {
'device_type': 'hp_procurve',
'ip': ip_addr07,
'username': "",
'password': "",
}

hp8 = {
'device_type': 'hp_procurve',
'ip': ip_addr08,
'username': "",
'password': "",
}

hp9 = {
'device_type': 'hp_procurve',
'ip': ip_addr09,
'username': "",
'password': "",
}

hp10 = {
'device_type': 'hp_procurve',
'ip': ip_addr10,
'username': "",
'password': "",
}

hp11 = {
'device_type': 'hp_procurve',
'ip': ip_addr11,
'username': "",
'password': "",
}

hp12 = {
'device_type': 'hp_procurve',
'ip': ip_addr12,
'username': "",
'password': "",
}

hp13 = {
'device_type': 'hp_procurve',
'ip': ip_addr13,
'username': "",
'password': "",
}

hp14 = {
'device_type': 'hp_procurve',
'ip': ip_addr14,
'username': "",
'password': "",
}

hp15 = {
'device_type': 'hp_procurve',
'ip': ip_addr15,
'username': "",
'password': "",
}

hp16 = {
'device_type': 'hp_procurve',
'ip': ip_addr16,
'username': "",
'password': "",
}

hp17 = {
'device_type': 'hp_procurve',
'ip': ip_addr17,
'username': "",
'password': "",
}

hp18 = {
'device_type': 'hp_procurve',
'ip': ip_addr18,
'username': "",
'password': "",
}

hp19 = {
'device_type': 'hp_procurve',
'ip': ip_addr19,
'username': "",
'password': "",
}

hp20 = {
'device_type': 'hp_procurve',
'ip': ip_addr20,
'username': "",
'password': "",
}

hp21 = {
'device_type': 'hp_procurve',
'ip': ip_addr21,
'username': "",
'password': "",
}

hp22 = {
'device_type': 'hp_procurve',
'ip': ip_addr22,
'username': "",
'password': "",
}

hp23 = {
'device_type': 'hp_procurve',
'ip': ip_addr23,
'username': "",
'password': "",
}

hp24 = {
'device_type': 'hp_procurve',
'ip': ip_addr24,
'username': "",
'password': "",
}

hp25 = {
'device_type': 'hp_procurve',
'ip': ip_addr25,
'username': '',
'password': '',
}

hp26 = {
'device_type': 'hp_procurve',
'ip': ip_addr26,
'username': "",
'password': "",
}

hp27 = {
'device_type': 'hp_procurve',
'ip': ip_addr27,
'username': "",
'password': "",
}

hp28 = {
'device_type': 'hp_procurve',
'ip': ip_addr28,
'username': "",
'password': "",
}

hp29 = {
'device_type': 'hp_procurve',
'ip': ip_addr29,
'username': "",
'password': "",
}

hp30 = {
'device_type': 'hp_procurve',
'ip': ip_addr30,
'username': "",
'password': "",
}

hp31 = {
'device_type': 'hp_procurve',
'ip': ip_addr31,
'username': "",
'password': "",
}

hp32 = {
'device_type': 'hp_procurve',
'ip': ip_addr32,
'username': "",
'password': "",
}

hp33 = {
'device_type': 'hp_procurve',
'ip': ip_addr33,
'username': "",
'password': "",
}

hp34 = {
'device_type': 'hp_procurve',
'ip': ip_addr34,
'username': "",
'password': "",
}

hp35 = {
'device_type': 'hp_procurve',
'ip': ip_addr35,
'username': "",
'password': "",
}

# Group dictionary of devices into a list
all_devices = [hp1, hp2, hp3, hp4, hp5, hp6, hp7, hp8, hp9, hp10, hp11, hp12, hp13, hp14, hp15, hp16, hp17,hp18, hp19, hp20, hp21, hp22, hp23, hp24, hp25, hp26, hp27, hp28, hp29, hp30, hp31, hp32, hp33, hp34,hp35]

# Grabs the current date and time and prints it at the start of the output
start_time = datetime.now()
print ("Start Time = {}".format(start_time))

# Takes the list of "all_devices" and assigns a name (a_device) to each dictionary item.
# This is so the For Loop can iterate over each device in the dictionary
# The For Loop will SSH to each device in the list and execute the commands below, in order.
for a_device in all_devices:
	net_connect = ConnectHandler(**a_device)
	print("----------------------------------------BEGIN----------------------------------------")
	print ("\n\n>>>>>>>>> Copying Config From TFTP Server <<<<<<<<<")
	print ("\n\n>>>>>>>>> Setting Config as Startup-Config on - {0} <<<<<<<<<".format(a_device['ip']))
	tftpcopy = net_connect.send_command("copy tftp startup-config IP FIRMWARE detail".format(a_device['ip']))
	time.sleep(1)
	tftpcopy += net_connect.send_command("y")
	time.sleep(1)
	print ("\n\n>>>>>>>>> Startup-Config Has Been Set {0} <<<<<<<<<".format(a_device['ip']))
	print (tftpcopy)
	print ("----------------------------------------END----------------------------------------")
    
# This'll print the total time it took for this script to complete
end_time = datetime.now()
total_time = end_time - start_time
print ("Total Time = {}".format(total_time))