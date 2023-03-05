# USB Rubber Ducky Book Notes
> Blue Cosmo | 05/17/2021

## Resources
notes drawn from:
```
USB Rubber Ducky, 'A GUIDE TO KEYSTROKE INJECTION ATTACKS'
By: Darren Kitchen, Hak5
```
## Module 1 - Keystroke Injection Attacks
- relies on inherent trust
- keyboards
- human operations
- rely on keyboard rather than GUI [Graphic User Interface]
```
xcopy documents\*.txt d:\
```
above will copy all ".txt" files in the documents directory, moves them to "d" drive
- rather than moving each file manually

## Module 2 - The USB Rubber Ducky
- keystroke injection tool, programmable keyboard
  - remote access
  - back doors
  - reconnaissance
  - exfiltration
- 1000 WPM [Words Per Minute]

## Module 3 - Anatomy of the Duck

Payloads
- tells the ducky what to do

Ducky Script
- scripting language for ducky

Ducky Encoder
- encodes payloads into injectable code for the ducky

Inject.bin
- the encoded version of a payload file

Firmware
- the code running on the ducky's CPU [Central Processing Unit]

### Hardware Overview
Micro SD card Reader
- supports up to 2GB [Gigabyte] SD cards

Micro Push Button
- used to replay payload [one press] or flash firmware [press and hold upon plugin]

Multi-color LED Indicator
- green - payload is running successfully
- red - error

Standard USB Type A Connector
- connects ducky to most computers [adapters can be used]

Generic Flash Drive Case
- houses ducky

## Module 4 - The Attack Workflow
Pre-engagement Interactions
- allows for a better understanding for your targets/clients environment
  - hardware
  - software
  - network

Reconnaissance
- get a better understanding of the systems and challenges you may face

Target
- know your objective

Research
- understand the most effective way to achieve that objective

Write
- create the payload in an effective manner

Encode
- allow for it to be ran by the ducky

Test
- see how well it works

Optimize
- make it more efficient based on testing results

Deploy
- once the payload is as effective as it can be, it is ready for use

## Module 5 - Ducky Script
- see 'ducky-syntax.md' for full syntax list

## Module 6 - Payload Principles
1. Speed
  - payloads need to be fast, every second counts
  - instead of using GUI, keyboard shortcuts and typing is faster and more affective

2. Stages
- ducky payloads can be 'inline' or 'staged'

Inline
- complete objective in one payload, no external resources necessary

Staged
- the payload works in stages, or steps

3. Resources
- requires external resources

## Module 7 - Writing Your First Payload
Objective
```
open notepad and enter 'Hello, World!'
```
Research
- how do we open notepad effeciently
  - start menu
  - runbox <--
- how many delays do we need

Write
```
REM opens notepad and enter 'Hello, World!'

DELAY 1000
GUI r
DELAY 100
STRING c:\windows\notepad.exe
DELAY 1000
STRING Hello, World!
```

Encode
- use ducky encoder to encode payload
  - java
  - python
  - online

  Java
  - using the java duck encoder
```
java -jar duckencoder.jar
java -jar duckencoder.jar -i payload.txt -o inject.bin
```

  Python
  - using python duck encoder
```
python3 duckencoder.py
python3 duckencoder.py -i payload.txt -o inject.bin
```

  Online
  - use 'https://ducktoolkit.com/encode' to encode payload

Test
- delays too long
- unnecessary string text

Optimize
```
REM opens notepad and enter 'Hello, World!'

DELAY 1000
GUI r
DELAY 100
STRING notepad
DELAY 400
STRING Hello, World!
```

## Module 8 - Obfuscation & Optimization
Obfuscation
- reducing the visibility of the payload

> Example - Hiding CMD [Command Prompt]
```
REM assuming we have a CMD open, we have to obfuscate it

REM this will make the CMD have yellow text, white background
STRING color FE
ENTER

REM this will reduce the CMD window size
STRING mode con:cols=18 lines=1
ENTER
```

Optimization
- making the payload faster and more effective

> Example - start a obfuscated CMD
```
REM assuming we have a runbox open, start an obfuscated CMD
STRING cmd /c color FE&mode con:cols=18 lines=1&ipconfig
ENTER
```

- what would be multiple lines and take long, now only takes ~3 seconds

> Example - start a minimized CMD, autoruns command
```
REM assuming we have a runbox open, start a minimized CMD
STRING cmd /c "start /min cmd /c ipconfig"
ENTER
```
