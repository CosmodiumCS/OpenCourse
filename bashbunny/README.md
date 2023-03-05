# Bash Bunny Book Notes
> Blue Cosmo | 07/21/21
---

## Resources:
notes drawn from:
```
Bash Bunny, 'A GUIDE TO HOT PLUG ATTACKS'
By: Darren Kitchen, Hak5
```

## Module 1 - The Bash Bunny
- advanced USB attack platform
- emulates trusted devices
	- gigabit ethernet
	- serial
	- flash storage
	- keyboards
---
Switch Positions
```markdown
| Postition | Mode           | Location         |
|-----------|----------------|------------------|
| 1         | Custom Payload | Closest to LED   |
| 2         | Custom Payload | Center           | 
| 3         | Arming Mode    | Closest to USB-A |
```
Directories
 - /docs - documentation
 - /languages - HID keyboard layouts
 - /loot - where payload output is stored
 - /tools - install additional tools
 - /payloads - store payloads for the respective switches
	 - /switch1 - store custom payload for switch one
	 - /switch2 - store custom payload for switch two
	 - /library - payload library
		 - /extensions - bunny script extensions

Config.txt
- a file where you can enable certain configurations for the bash bunny

Defaults
- username - *root*
- password - *hak5bunny*
- ip address - *172.16.64.1*

LED Staus
```markdown
| Led                    | Status            |
|------------------------|-------------------|
| Green [blinking]       | Booting           |
| Red [solid]            | Error             |
| Blue [blinking]        | Arming Mode       |
| Red/Blue [alternating] | Flashing Firmware |
```

## Module 2 - Getting Connected:
- the bash bunny has a serial console to access a linux shell
- it also has ssh enabled for other remote connectivity
---
Serial Settings
- Baud Rate - 115200
- Data Bits - 8
- Parity Bit - No
- Stop Bit - 1
---
- Full connectivity instructions in book

## Module 3 - Bunny Script:
- full syntax list in *bunny-script.md*

## Module 4 - Updates & Recovery:
Updating and Recovery Methods:
- BashBunny Updater [Windows, MacOS, and Linux]
- BashBunny Firmware Recovery
- Manual Firmware Updates

## Module 5 - Sample Payload:
SMB Exfiltration - 'https://github.com/hak5/bashbunny-payloads/tree/master/payloads/library/exfiltration/smb_exfiltrator'

## Bash Bunny Mark II:
- although the BashBunny MkII has most of the same features as the MkI, there are a few key differences we should notate.

- payloads are ran from the bunny's internals storage [not the SD card]
- 