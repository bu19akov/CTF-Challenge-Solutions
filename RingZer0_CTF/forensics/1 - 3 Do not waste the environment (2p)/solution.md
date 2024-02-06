# 1 / 3 Do not waste the environment

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Forensics
- **Points:** 2

## Provided Materials

- File 

## Solution

The challenge name gives us a hint, that we need to look for environment variables. Let's analyze the file:

```sh
$ strings 5bd2510a83e82d271b7bf7fa4e0970d1 | grep -i -- 'Linux\|Windows' | head
SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings
SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\WinHttp
SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\WinHttp\Tracing
                {*.104C.8031.0.0.0.00000000.00008000}, \   ;; bit 15 PCI_HACK_DEFAULT_CARDBUS_WINDOWS
; subtractive decode, so its windows were ignored.  This is no longer the case,
; and the BIOS configures the windows to claim enormous quantities of address
Microsoft.Windows.Diagnosis.Commands.GetDiagInput.Resources,1.0.0.0,en,31bf3856ad364e35,msil
Microsoft.Windows.Diagnosis.SDHost.Resources,1.0.0.0,en,31bf3856ad364e35,msil
Microsoft.Windows.Diagnosis.TroubleshootingPack.Resources,6.1.0.0,en,31bf3856ad364e35,msil
C:\Windows\system32\advapi32.dll[MofResourceName]
```

Now, when the OS (`Microsoft Windows`) was identified, we need to get more information about it. We will use [volatility](https://github.com/volatilityfoundation/volatility) *(memory extraction utility framework)* to extract environment variables:

```sh
vol -f 5bd2510a83e82d271b7bf7fa4e0970d1 windows.envars.Envars
Volatility 3 Framework 2.5.0
Progress:  100.00		PDB scanning finished                        
PID	Process	Block	Variable	Value

252	smss.exe	0x3208c0	Path	C:\Windows\System32
252	smss.exe	0x3208c0	SystemDrive	C:
252	smss.exe	0x3208c0	SystemRoot	C:\Windows
...
1972	taskhost.exe	0xd1030	F l a g -	66d7724d872da91af56907aea0f6bfb8
```

## Final Flag

`Flag-66d7724d872da91af56907aea0f6bfb8`

*Created by [bu19akov](https://github.com/bu19akov)*