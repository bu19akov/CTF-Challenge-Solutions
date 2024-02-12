# 2 / 3 Did you see my desktop?

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Forensics
- **Points:** 3

## Provided Materials

- File

## Solution

*(First read [1 / 3 Do not waste the environment](https://github.com/bu19akov/CTF-Challenge-Solutions/blob/main/RingZer0_CTF/forensics/1%20-%203%20Do%20not%20waste%20the%20environment%20(2p)/solution.md))*.

So we need to analyze our file further and as the name suggest we need to find something on the Desktop. Let's firstly list command line arguments:

```sh
$ vol -f 5bd2510a83e82d271b7bf7fa4e0970d1 windows.cmdline.CmdLine
Volatility 3 Framework 2.5.0
Progress:  100.00		PDB scanning finished                        
PID	Process	Args
...
2528	notepad.exe	"C:\Windows\system32\NOTEPAD.EXE" C:\Users\flag\Desktop\F$L%A^G-5bd2510a83e82d271b7bf7fa4e0970d1.txt
...
```

## Final Flag

`FLAG-5bd2510a83e82d271b7bf7fa4e0970d1`

*Created by [bu19akov](https://github.com/bu19akov)*