# P2000T

I got a Philips P2000T, and started to investigate it a bit.
This document describes my findings.


## BASIC

I started with the cartridge "Basic Interpreter 16K" or "P2305" (for slot "1").
Trying a 10-print program works as expected. Still I had some issues.

- The cartridge has two character _modes_, lets call them mix and allcaps.
  This mode is not to be confused with the capslock state. 
  
  In the _mix_ mode, this is the behavior of shift and capslock.
  
  | key  | no shift, no capslock | shift, no capslock | no shift, capslock | shift, capslock |
  |:----:|:---------------------:|:------------------:|:------------------:|:---------------:|
  | [A]  |          a            |         A          |         A          |         A       |
  | [1!] |          1            |         !          |         !          |         !       |

  In the _allcaps_ mode, this is the behavior of shift and capslock.
  
  | key  | no shift, no capslock | shift, no capslock | no shift, capslock | shift, capslock |
  |:----:|:---------------------:|:------------------:|:------------------:|:---------------:|
  | [A]  |          A            |         A          |         A          |         A       |
  | [1!] |          1            |         !          |         !          |         !       |
  
  To engage capslock press the Capslock key, to disengage capslock press the Shift key.
  To _toggle_ the character mode press Shift and Tab.
  
  ![Keys](images/capslock.jpg)
  
  BASIC itself is not case sensitive, so `print` and `PRINT` are the same, and so
  are `a$` and `A$`. What is more, BASIC converts these to uppercase when you type 
  the lowercase.
  
  However, as I discovered, some programs ask `Are you sure [y/n]?` and 
  they do not accept (uppercase) `Y`.
  
  BASIC 1.1 NL starts in mix mode, but the BASIC 1.0 UK starts in allcaps mode.

- To edit a basic program, say line 30, you can not just type `LIST`, cursor to 
  line 30 and start correcting. You have to give the command `EDIT 30`, and then 
  you are in a sort of [VI editor](https://en.wikipedia.org/wiki/Vi_(text_editor)) 
  (that only helps if you did a bit of Linux).
  This editor has three states: command, insert, overwrite.
  
  By default, you are in the command state where pressing a key gives a command.
  - `C` ("change") switches to overwrite state; each character typed next 
    overwrites the old text. `CODE` switches back to command state.
  - `I` ("insert") switches to insert state; each character typed next is inserted before 
    the old text. `CODE` switches back to command state.
  - `X` ("append") moves to end of line and switches to insert.
  - `H` deletes to end of line and switches to insert.
  - `S` ("search") moves the cursor to the next character typed. Use Shift `Cursor right` for find next.
  - `K` ("kill search") deletes to the next character typed.
  - `ENTER` commits changes.
  - `STOP` (Shift `,` on numeric keypad) aborts all changes.
  - `Backspace` backspaces one character and Shift `Backspace` deletes one character.
  - Tip: also the _line number_ can be edited (then, the old line stays as is).
  
  In all modes, the cursor keys are operational.
  
  This overview is for BASIC 1.1; BASIC 1.0 UK is severely limited: e.g. 
  the cursor keys don't work and and `C` is for one character only.

- The tape recorder works as a disk drive. You can get a directory with Zoek
  (Shift `1` on numeric keyboard), and load and save is with commands `CLOAD` 
  and `CSAVE`.
  
  ![dir](images/dir.jpg)

  The directory listing only shows the first character of every file in 
  BASIC 1.0 UK, the screenshot is for BASIC 1.1 NL.

- The P2000T has a printer port at the back. 

  ![printerport](images/printerport.jpg)
  
  The great thing is that this is actually a _serial_ port.
  To connect it to a PC, you need an old style D25 connector/converter, and 
  a cable to convert from Serial to USB. I used a 
  [US232R-500-BULK](https://nl.mouser.com/ProductDetail/FTDI/US232R-500-BULK).
  
  In the PC start a terminal, e.g. [ninjaterm](https://ninjaterm-app.mbedded.ninja/), 
  connect to the correct COM port with settings 1200,8,N,1, and 
  try `LPRINT` to print a line, `LLIST` to list the program on the printer,
  or use print-screen (Shift `00` on numeric keyboard) to copy the current 
  screen to the printer.
  
  Here an example on an empty screen.
  I first did a `list`, then a `run` (which prints due to the
  `LPRINT` statements), then a `llist` (which prints the listing), and finally 
  I pressed print screen.
  
  ![Terminal](images/terminal.png)
  
  The print screen button does not seem to work in BASIC 1.0 UK.
  
  > The `LLIST` and print screen are low threshold features to get 
  > data from P2000T to PC.
  
- What really confused me in the beginning was that my P2000T did not do what the 
  manual [Gebruiksaanwijzing](docs/Gebruiksaanwijzing-P2000T-met-P2305-BASIC-NL.pdf) specified.
  Later I found out the manual is for version NL 1.1, and my cartridge is UK 1.0.
  
  Differences I found
  - Version 1.1 adds many control chars. For example see that control 
    character 18 is not working in 1.0.
  
    ![control chars](images/controlchars.jpg)
    
  - Several keyboard keys are not working: cursor (!), print screen (numeric Shift 5), 
    clear screen (numeric Shift upper right), Def for edit last (numeric  Shift 0).
    
    I did have a "Tekstbewerking" or "P2301" (for slot "1") cartridge, and there 
    the cursor keys did work, so I did know it was not a hardware fault.
    
  - Tape directory (Zoek numeric Shift 1) only shows first char of file name, 
    instead of full name, file type and file size.
    
  - Statement `inp("")` to get a single keyboard key does not work in 1.0.
  
  - Default character  mode is allcaps in 1.0. I did not know I could switch 
    to mixed (see above), but my program required that.


## Links

- [Preservation project](https://github.com/p2000t), especially [Nieuwsbrief Natlab](https://github.com/p2000t/documentation/tree/main/NatLab)
- [Retroforum](https://www.retroforum.nl/topic/3914-philips-p2000t)

(end)
