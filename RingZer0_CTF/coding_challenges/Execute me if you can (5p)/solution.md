# Execute me if you can

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Coding Challenges
- **Points:** 5

## Provided Materials

- Web page with [shellcode](https://en.wikipedia.org/wiki/Shellcode)


## Solution

Firstly, we need to undertsnad what shellcode is doing. For that we can use [Online Disassembler](https://defuse.ca/online-x86-assembler.htm#disassembly2):
 
*(Firstly read the text under the shellcode)*

```
0:  eb 4d                   jmp    0x4f
2:  5e                      pop    rsi
3:  66 83 ec 0c             sub    sp,0xc // adjusts the stack pointer `rsp` by subtracting `12 (0xc)`
 											 bytes. This operation sets up `rsp` to point to a specific 
 											 location on the stack relative to our string.
7:  48 89 e0                mov    rax,rsp // moves the stack pointer into `rax`. 
											 `rax` will be used to store the decoded string.
a:  48 31 c9                xor    rcx,rcx // clears the `rcx` register, setting it to zero. 
											  This will be used as a counter.
d:  68 30 c4 58 cb          push   0xffffffffcb58c430 // pushes some data onto the stack. This data 
														 doesn't seem to be directly relevant 
														 to the decoding.
12: 48 89 cf                mov    rdi,rcx
15: 80 c1 0c                add    cl,0xc // `mov rdi, rcx` and `add cl, 0xc` set up 
											 `rcx` with a value of 12, which will be used as a loop 
											 counter. The loop iterates 12 times, decoding one byte 
											 of the string per iteration.		 
18: 40 8a 3e                mov    dil,BYTE PTR [rsi] // moves a byte from the address pointed by 
														`rsi` (our string) into the lower part of `rdi`.
1b: 40 f6 d7                not    dil // performs a bitwise NOT operation on the byte in `dil`,
										  effectively flipping all its bits.
1e: 40 88 38                mov    BYTE PTR [rax],dil // moves the negated byte into the location pointed 
														 by `rax`, effectively storing the decoded byte
														 in our stack-based string buffer.
21: 48 ff c6                inc    rsi
24: 68 82 cd 24 4d          push   0x4d24cd82
29: 48 ff c0                inc    rax // `inc rsi` and `inc rax` increment the `rsi` and `rax` 
										   pointers for the next byte.
2c: e2 ea                   loop   0x18 // decrements `rcx` and loops back if `rcx` is not zero.
2e: 2c 0c                   sub    al,0xc // adjusts `rax` by subtracting 12, thus pointing it to the 
											 start of the decoded string.
30: 48 89 c6                mov    rsi,rax
33: 68 21 fb 67 1b          push   0x1b67fb21
38: 48 31 c0                xor    rax,rax
3b: 48 89 c7                mov    rdi,rax
3e: 04 01                   add    al,0x1
40: 48 89 c2                mov    rdx,rax
43: 80 c2 0b                add    dl,0xb // The system call is prepared with `xor rax,rax` 
											 (clearing `rax`), `mov rdi, rax` (moving `rax` to `rdi`, 
											 which ends up being zero), and setting up `rax` and `rdx` 
											 for the syscall.
46: 0f 05                   syscall // The `syscall` is `sys_write`, but with `rdi` as 0, 
									   it writes to `stdin` instead of `stdout`.
48: 48 31 c0                xor    rax,rax 
4b: 04 3c                   add    al,0x3c // clears `rax`, and `add al, 0x3c` sets rax to 60, 
											  which is the system call number for `exit`.
4d: 0f 05                   syscall // performs the `exit` system call.
4f: e8 ae ff ff ff          call   0x2
54: bd c6 b5 93 90          mov    ebp,0x9093b5c6
59: 90                      nop
5a: c8 85 ba cf             enter  0xba85,0xcf
5e: 8e a7 f2 75 e4 96       mov    fs,WORD PTR [rdi-0x691b8a0e]
64: 6f                      outs   dx,DWORD PTR ds:[rsi]
65: 8c 9d ac d3 cc 34       mov    WORD PTR [rbp+0x34ccd3ac],ds
6b: 00 b7 4a 68 50 86       add    BYTE PTR [rdi-0x79af97b6],dh
71: f1                      icebp
72: 5b                      pop    rbx
73: 5b                      pop    rbx
74: 52                      push   rdx
75: 41                      rex.B
76: 4e                      rex.WRX
77: 44 53                   rex.R push rbx
79: 54                      push   rsp
7a: 52                      push   rdx
7b: 32                      .byte 0x32
7c: 5d                      pop    rbp
```

The jmp instruction at `0` jumps forward by `0x4f` bytes. This brings the instruction pointer `rip` to the address `4f`. This is a straightforward jump, skipping over `0x4f` bytes of code or data.

At `4f`, there is a call instruction. The call instruction does two things:

- First, it pushes the address of the next instruction `54` onto the stack. This address is effectively the return address for when the call completes.
- Second, it jumps to the target address of the call, which in this case is calculated as `4f` + `0x02` + the displacement (`-0x52`), resulting in the address `02`.

The clever part of this technique is that when the `call` instruction pushes the return address `54` onto the stack, that address is not just a return pointer but also the address where a string or some data begins.
The `pop rsi` instruction at `02` will then pop this value from the stack into the `rsi` register. Hence, `rsi` now holds the address `54`, which is the address of the string or data we're interested in.

This method cleverly obfuscates the process of loading the address of the string into the `rsi` register. Instead of using a direct approach like `mov rsi, 0x54` or `lea rsi, [rip+0x54]`, it utilizes the mechanics of call and pop to achieve the same result.

So, `rsi` now points to the start of our string.

Now return to reading the shellcode from `3`.

Here is the `python` code:

```python
import requests
import re
from ctypes import *
from bs4 import BeautifulSoup

session = requests.Session()

# Function to get the changed bytes from shellcode
def run_shellcode(shellcode):
    sc = bytes.fromhex(shellcode.replace('\\x', ''))

    # Extract a portion of the shellcode and convert it to hexadecimal string
    hx = sc[0x54:0x54+0x0c].hex()

    # Perform bitwise XOR with 0xFF and convert back to string
    result = ''.join(chr(int(x, 16) ^ 0xFF) for x in re.findall('..', hx))
    print(result)
    return result

def extract_flag(page_content):
    """
    This function extracts the FLAG from the HTML content using BeautifulSoup.
    """
    soup = BeautifulSoup(page_content, 'html.parser')
    message_div = soup.find('div', class_='alert alert-info')
    if message_div:
        message = message_div.get_text(strip=True)
        return message
    return None

def main():
    url = "http://challenges.ringzer0team.com:10121"
    response = session.get(url)
    html = response.text  # No need to decode
    match = re.search(r'----- BEGIN SHELLCODE -----(.*)----- END SHELLCODE -----', html, re.DOTALL | re.S)
    if match:
        # Clean the matched hash value by removing <br> tags
        shellcode = re.sub(r'<br\s*/?>', '', match.group(1).strip()).strip()
    output = run_shellcode(shellcode)

    url = f"http://challenges.ringzer0team.com:10121/?r={output}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Print the response content (HTML)
    print(extract_flag(response.text))


if __name__ == '__main__':
    main()
```

## Final Flag

`FLAG-W2gudjVCAlhexK1c3IfPun0CGs`

*Created by [bu19akov](https://github.com/bu19akov)*