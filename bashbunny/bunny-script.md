# Bunny Script
> Blue Cosmo
---

## Extraneous:
- the bash bunny does use *DuckyScript* [a language originally designed for the USB Rubber Ducky] as well as a other language called *BunnyScript*
- communtiy payloads - 'https://github.com/hak5/bashbunny-payloads'
- coupled with BASH
- payloads are saved to a `payload.txt` file
---
payload header
```
# Title: 		XXX
# Description:	XXX
# Author:		XXX
# Category:		XXX
# Target:		XXX
# Attackmodes:	XXX
```

## ATTACKMODE
- select emulation type

### Modes:
SERIAL
- enables serial console

ECM_ETHERNET
- enables ethernet control model [ecm] for linux, mac and android

RNDIS_ETHERNET
- enables remote network driver interface specification [rndis] for windows

STORAGE
- enables mass storage

RO_STORAGE
- enables read only [om] storage 

HID
- enables keyboard mode for keystroke injection

OFF
- turns off emulation

### Arguments:
SN_XX
- set serial number to *XX*

MAN_XX
- set device manufacturer to *XX*

VID_XX
- spoof vendor ID as *XX*

PID_XX
- spoof product ID as *XX*

## LED
change LED color

### Colors:
```markdown
| COMMAND | DESCRIPTION |
|---------|-------------|
| R       | Red         |
| G       | Green       |
| B       | Blue        |
| Y       | Yellow      |
| C       | Cyan        |
| M       | Magenta     |
| W       | White       |
```

### Paterns:
```markdown
| PATTERN  | DESCRIPTION            |
|----------|------------------------|
| SOLID    | LED turns on           |
| SLOW     | 1000ms on/off          |
| FAST     | 100ms on/off           |
| VERYFAST | 10ms on/off            |
| SINGLE   | 1 100ms on, 1000ms off |
| DOUBLE   | 2 100ms on, 1000ms off |
| TRIPLE   | 3 100ms on, 1000ms off |
| QUAD     | 4 100ms on, 1000ms off |
| QUIN     | 5 100ms on, 1000ms off |
| SUCCESS  | 1000ms VERYFAST, SOLID |
```

### LED State:
```markdown
| STATE      | DESCRIPTION                             |
|------------|-----------------------------------------|
| SETUP      | Magenta [solid]                         |
| FAIL[1-5]  | Red [slow blink - very fast blink]      |
| ATTACK     | Yellow [single blink]                   |
| STAGE[1-5] | Yellow [single blink - quintuple blink] |
| CLEANUP    | White [fast blink]                      |
| FINISH     | Green [1000ms VERYFAST, SOLID]          |
```

## QUACK | Q
run duckysrcript file or command
```
QUACK GUI r
```

## DUCKY_LANG
set keyboard language
```
DUCKY_LANG us
```

## RUN
a cross platform keystroke injection shortcut
```
RUN WIN Notepad.exe
```

## GET
obtain system variables
```
GET SWITCH_POSITION
```
- this gets the current switch position of the onboard switch of the bash bunny

## REQUIRETOOL
terminates payload if tool is not found in `/tools`
```
REQUIRETOOL impacket
```

## WAIT_FOR_PRESENT [MkII]
pauses payload until a a bluetooth id is detected
```
WAIT_FOR_PRESENT XXX
```

## WAIT_FOR_NOT_PRESENT [MkII]
pauses payload until a a bluetooth id is NOT detected
```
WAIT_FOR_NOT_PRESENT XXX
```