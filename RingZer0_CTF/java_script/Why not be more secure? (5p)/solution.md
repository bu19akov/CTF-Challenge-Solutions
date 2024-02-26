# Why not be more secure?

## Challenge Details 

- **CTF:** RingZer0
- **Category:** JavaScript
- **Points:** 5

## Provided Materials

- Login form

## Solution

With `Developer Tools` we can find the `script` code:

```js
<script>
	// Look's like weak JavaScript auth script :)
	$(".c_submit").click(function(event) {
	    event.preventDefault();
	    var u = $("#cpass").val();
	    var k = $("#cuser").val();
	    var func = "\x2B\x09\x4A\x03\x49\x0F\x0E\x14\x15\x1A\x00\x10\x3F\x1A\x71\x5C\x5B\x5B\x00\x1A\x16\x38\x06\x46\x66\x5A\x55\x30\x0A\x03\x1D\x08\x50\x5F\x51\x15\x6B\x4F\x19\x56\x00\x54\x1B\x50\x58\x21\x1A\x0F\x13\x07\x46\x1D\x58\x58\x21\x0E\x16\x1F\x06\x5C\x1D\x5C\x45\x27\x09\x4C\x1F\x07\x56\x56\x4C\x78\x24\x47\x40\x49\x19\x0F\x11\x1D\x17\x7F\x52\x42\x5B\x58\x1B\x13\x4F\x17\x26\x00\x01\x03\x04\x57\x5D\x40\x19\x2E\x00\x01\x17\x1D\x5B\x5C\x5A\x17\x7F\x4F\x06\x19\x0A\x47\x5E\x51\x59\x36\x41\x0E\x19\x0A\x53\x47\x5D\x58\x2C\x41\x0A\x04\x0C\x54\x13\x1F\x17\x60\x50\x12\x4B\x4B\x12\x18\x14\x42\x79\x4F\x1F\x56\x14\x12\x56\x58\x44\x27\x4F\x19\x56\x49\x16\x1B\x16\x14\x21\x1D\x07\x05\x19\x5D\x5D\x47\x52\x60\x46\x4C\x1E\x1D\x5F\x5F\x1C\x15\x7E\x0B\x0B\x00\x49\x51\x5F\x55\x44\x31\x52\x45\x13\x1B\x40\x5C\x46\x10\x7C\x38\x10\x19\x07\x55\x13\x44\x56\x31\x1C\x15\x19\x1B\x56\x13\x47\x58\x30\x1D\x1B\x58\x55\x1D\x57\x5D\x41\x7C\x4D\x4B\x4D\x49\x4F";
	    buf = "";
	    if (k.length == 9) {
	        for (i = 0, j = 0; i < func.length; i++) {
	            c = parseInt(func.charCodeAt(i));
	            c = c ^ k.charCodeAt(j);
	            if (++j == k.length) {
	                j = 0;
	            }
	            buf += eval('"' + a(x(c)) + '"');
	        }
	        eval(buf);
	    } else {
	        $("#cresponse").html("<div class='alert alert-danger'>Wrong password sorry.</div>");
	    }
	});
	
	function a(h) {
	    if (h.length != 2) {
	        h = "\x30" + h;
	    }
	    return "\x5c\x78" + h;
	}
	
	function x(d) {
	    if (d < 0) {
	        d = 0xFFFFFFFF + d + 1;
	    }
	    return d.toString(16).toUpperCase();
	}
</script>
```

We need to find `username` *(k)* and `password` *(u)*. We can see, that the username needs to be 9 character long. Upon closer examination of the code, we observe that the `func` is XORed using the username. This process generates a code that is then executed by the `eval` command.

We can suspect that the start of the `func` might begin with `if(`. To verify this, we can performed an XOR operation on the first 3 characters of the function using the characters `if(`:

```
0x2b XOR i (where i is ASCII 0x69) results in 0x42, which corresponds to the character B.
0x09 XOR f (where f is ASCII 0x66) results in 0x6f, which corresponds to the character o.
0x4a XOR ( (where ( is ASCII 0x28) results in 0x62, which corresponds to the character b.
```

This indicates that `Bob` is the initial part of the username.

We can create a Python script to decrypt a portion of the cipher using `Bob??????` as a key:

```py
func = ('\x2B\x09\x4A\x03\x49\x0F\x0E\x14\x15\x1A\x00\x10\x3F\x1A\x71\x5C\x5B\x5B\x00\x1A\x16\x38\x06\x46\x66'
        '\x5A\x55\x30\x0A\x03\x1D\x08\x50\x5F\x51\x15\x6B\x4F\x19\x56\x00\x54\x1B\x50\x58\x21\x1A\x0F\x13\x07'
        '\x46\x1D\x58\x58\x21\x0E\x16\x1F\x06\x5C\x1D\x5C\x45\x27\x09\x4C\x1F\x07\x56\x56\x4C\x78\x24\x47\x40'
        '\x49\x19\x0F\x11\x1D\x17\x7F\x52\x42\x5B\x58\x1B\x13\x4F\x17\x26\x00\x01\x03\x04\x57\x5D\x40\x19\x2E'
        '\x00\x01\x17\x1D\x5B\x5C\x5A\x17\x7F\x4F\x06\x19\x0A\x47\x5E\x51\x59\x36\x41\x0E\x19\x0A\x53\x47\x5D'
        '\x58\x2C\x41\x0A\x04\x0C\x54\x13\x1F\x17\x60\x50\x12\x4B\x4B\x12\x18\x14\x42\x79\x4F\x1F\x56\x14\x12'
        '\x56\x58\x44\x27\x4F\x19\x56\x49\x16\x1B\x16\x14\x21\x1D\x07\x05\x19\x5D\x5D\x47\x52\x60\x46\x4C\x1E'
        '\x1D\x5F\x5F\x1C\x15\x7E\x0B\x0B\x00\x49\x51\x5F\x55\x44\x31\x52\x45\x13\x1B\x40\x5C\x46\x10\x7C\x38'
        '\x10\x19\x07\x55\x13\x44\x56\x31\x1C\x15\x19\x1B\x56\x13\x47\x58\x30\x1D\x1B\x58\x55\x1D\x57\x5D\x41'
        '\x7C\x4D\x4B\x4D\x49\x4F')
key = "Bob??????"
functext = ""

for i, char in enumerate(func):
    C = i % len(key)  
    if key[C] == '?':
        functext += ' '   
    else:
        functext += chr(ord(char) ^ ord(key[C]))

print(functext)
```

Output:

```
if(      Xor      But      rea      ) {      cum      cat      ef.      f("      ==       doc      loc      = d      t.l      n.h      "?p      ; }      e {      cre      ").      <di      s='      >Wr      ssw      rry      >")
```

We can assume, that 

```
  cum      cat      ef
```

is `document.location.href`, so let's decode our `username` further:

```
cument.lo
cum\x13\x07\x46\x1d\x58\x58
```

```
0x13 XOR e (ASCII 0x65) results in 0x76, which is v.
0x07 XOR n (ASCII 0x6e) results in 0x69, which is i.
0x46 XOR t (ASCII 0x74) results in 0x32, which is 2.
0x1d XOR . (ASCII 0x2e) results in 0x33, which is 3.
0x58 XOR l (ASCII 0x6c) results in 0x34, which is 4.
0x58 XOR o (ASCII 0x6f) results in 0x37, which is 7.
```

So the `username` is `Bobvi2347`. Let's run our python code again with `Bobvi2347` and see the full function:

```js
if(u == "XorIsCoolButNotUnbreakable") { 
	if(document.location.href.indexOf("?p=") == -1) { 
		document.location = document.location.href + "?p=" + u; 
	} 
} else {  
	$("#cresponse").html("<div class='error'>Wrong password sorry.</div>"); 
}
```

`Username` is `Bobvi2347`, `password` is `XorIsCoolButNotUnbreakable`

## Final Flag

`FLAG-rhwMJNczASAJ4WgwfIA7fcJD`

*Created by [bu19akov](https://github.com/bu19akov)*