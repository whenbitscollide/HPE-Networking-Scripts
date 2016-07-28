# HPE/Aruba-Networking-Scripts
I'd like to give a big thanks to Kirk Byers for developing Netmiko - It's been essential in my day-to-day operations.
  - Kirk Byers' site: https://pynet.twb-tech.com
  - Kirk Byers' GitHub: https://github.com/ktbyers

This is a collection of Python scripts I use for automating tasks on HPE/Aruba switches. 

WARNING
-------
My Python skills are below par and as a result, these scripts are very unintelligent and barely work.
I'll update them as my knowledge of Python grows, but for now, they'll serve as a starting point and a reminder of where I began.



OVERVIEW
----------
AIO (All in One):
- Firmware Update
- Create Self-Signed Cert
- Copy Config from TFTP server and set it as Startup-Config


CopyTFTPConfig:
- Copy Config from TFTP server and set it as Startup-Config


Send-Cmds:
- Will send commands to all switches in the list
- Has an Except statement that'll skip over any switches that give an error

Template-Creator:
- Generate configs from a template
- The template will substitute any markings inside curly braces {{}} with values from a CSV
- Requires Jinja2
