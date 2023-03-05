# Wifi Pineapple Book Notes
> Blue Cosmo | 08/26/21
---

## Resources:
notes drawn from:
```
Wifi Pineapple, 'A GUIDE TO THE TOP AUDITING TOOLKIT'
```
- note that notes are modified to the MkVII

## Module 1 - Pineapple What?
- wifi auditing tool
	- passively gather intel
	- rouge access points
	- man in the middle

## Module 2 - Wifi Audit Workflow
- Pre-Engagement Interactions
	- determine scope and rules
- Intelligence Gathering
	- reconaissance
- Vulnerability Analysis
	- find possible attack vectors
- Exploitation
	- exploit said vectors
- Post Exploitation
	- persistance, pivot attack
- Reporting
	- report on vulnerabilites and issue within the network to better client's security
---
- PineAP Workflow
	- Recon
		- gather intel on the 'wireless landscape'
	- Filter
		- limit collateral damage
	- Log
		- keep track of wireless actions
	- Analyze
		- determinie your targets
	- Capture
		- a pool of SSIDs
	- Prepare
		- setup how attacks will be conducted
	- Test
		- ensure attack sucess
	- Broadcast
		- advertise SSIDs to nearby devices
	- Associate
		- filter specific targets
	- Deauthenticate
		- encourage devices to join your network
	- Monitor/Manipulate
		- monitor traffic or manipulate connections
	- Report
		- summarize attack workflow

## Module 3 - Basics of Wifi Operation
- learn, know, and understand the basics of wifi and wifi hacking

## Module 4 - The PineAP Suite
the 'engine' for the Pineapples hacking abilities

## Module 5 - Hardware Overview
we will skip this one due to them being specific to the TETRA and NANO

## Module 6 - Wifi Pineapple Setup
1. connect to 2-Amp USB powersource
2. join the "Pineapple_XXXX" Wi-Fi network
3. browse to *http://172.16.42.1:1471* and follow the on-screen instructions

## Module 7 - Setup From Android
specific to TETRA and NANO
- however, because the MkVII works through the web, it is accessible on practically any device

## Module 8 - Connectiong to The Internet
we will skip this one due to them being specific to the TETRA and NANO

## Module 9 - The Web Interface
if your Pineapple is connected sucessfully than you can access the web interface [here](http://172.16.42.1:1471)

## Module 10 - Wifi Pineapple Modules
- the wifi pineapple is designed to be modular
- community members can contribute modules to this [repository](https://github.com/hak5/mk7-modules)

## Module 11 - Shell Access And Upgrades
- remote acces for the MkVII is carried through CloudC2 and the Web Interface
---
ssh
```
ssh root@172.16.42.1
```
serial
```
flowcontrol: none
baudrate: 115200
parity: none
databits: 8
stopbit: 1
```