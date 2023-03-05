# USB Rubber Ducky Syntax
> Blue Cosmo | 05/17/2021

## To be Noted
- BASIC based
- commands are in all caps
- attributes are lowercase
- Delays are measured in milliseconds, 1 second = 1000 milliseconds

## REM
- remark or comment, attributes are not processed
```
REM this will not be ran
STRING this will be typed
```

## DEFAULT_DELAY | DEFAULTDELAY
- creates a default delay between commands
```
REM there will be a one second delay between commands
DEFAULT_DELAY 1000
GUI r
STRING notepad
```

## DELAY
- creates a single delay
```
REM this will delay for one second
DELAY 1000
GUI r

REM this will delay for half a second
DELAY 500
STRING notepad
```

## STRING
- inputs text
```
REM this will type 'Hello, World!'
STRING Hello, World!
```

## GUI | WINDOWS
- acts as the special key [windows key]
```
REM this will lock your screen
GUI l
```

## MENU | APP
- right click
```
REM this will paste the users clipboard
MENU
STRING p
```

## SHIFT
- holds down 'shift' key along with any selected key
```
REM this will paste the users clipboard
SHIFT INSERT
```

## ALT
- holds down 'alt' key along with any selected key
```
REM this will close the open window
ALT F4
```

## CONTROL | CTRL
- holds down 'control' key along with any selected key
```
REM this will select all and add content to clipboard
CTRL a
CONTROL c
```

## ARROW KEYS
- each direction hits each respective arrow key
```
REM 'DOWNARROW' or 'DOWN' will hit the down arrow
REM 'UPARROW' or 'UP' will hit the up arrow
REM 'LEFTARROW' or 'LEFT' will hit the left arrow
REM 'RIGHTARROW' or 'RIGHT' will hit the right arrow
```

## OTHER COMMANDS
```
REM 'BREAK' or 'PAUSE' will hit pause
REM 'CAPSLOCK' will hit the 'caps lock' key
REM 'DELETE' will hit the 'delete' key
REM 'END' will hit the 'end' key
REM 'ESC' or 'ESCAPE' will hit the 'escape' key
REM 'HOME' will hit the 'home' key
REM 'INSERT' will hit the 'insert' key
REM 'NUMLOCK' will hit the 'num lock' key
REM 'PAGEUP' will hit the 'page up' key
REM 'PAGEDOWN' will hit the 'page down' key
REM 'PRINTSCREEN' will hit the 'print screen' key
REM 'SCROLLOCK' will hit the 'scroll lock' key
REM 'SPACE' will hit the 'space' bar
REM 'TAB' will hit the 'tab' key
```
