# I Lost my password

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Cryptography
- **Points:** 3

## Provided Materials

- Archive with some directories and files

## Solution

We can unpack an archive and look for `password` inside it:

```sh
$ grep -R password
./{75DE8F0A-DEC0-441F-AE29-90DFAFCF632B}/User/Preferences/Groups/Groups.xml:<Groups clsid="{3125E937-EB16-4b4c-9934-544FC6D24D26}"><User clsid="{DF5F1855-51E5-4d24-8B1A-D9BDE98BA1D1}" name="Administrator (built-in)" image="1" changed="2014-02-06 19:33:28" uid="{C73C0939-38FB-4287-AC48-478F614F5EF7}" userContext="0" removePolicy="0"><Properties action="R" fullName="Administrator" description="Administrator" cpassword="PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw" changeLogon="0" noChange="0" neverExpires="1" acctDisabled="0" subAuthority="" userName="Administrator (built-in)"/></User>
```

We got `cpassword="PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw"`, so we can use [this](https://securixy.kz/hack-faq/gpp-password-decrypt-online.html/) online tool to decrypt it:

![Image](./pass.jpg)

*(You can read [Find and Decrypt GPP Password](https://systemweakness.com/find-and-decrypt-gpp-password-4edb9a1663c4) about how it works)*

## Final Flag

`LocalRoot!`

*Created by [bu19akov](https://github.com/bu19akov)*