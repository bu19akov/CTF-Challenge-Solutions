# Then obfuscation is more secure

## Challenge Details 

- **CTF:** RingZer0
- **Category:** JavaScript
- **Points:** 1

## Provided Materials

- Password field

## Solution

We can find following script while analyzing the page with `Web-Inspector`:

```javascript
<script>
// Look's like weak JavaScript auth script :)
var _0xc360 = ["\x76\x61\x6C", "\x23\x63\x70\x61\x73\x73", "\x61\x6C\x6B\x33", "\x30\x32\x6C\x31", "\x3F\x70\x3D", "\x69\x6E\x64\x65\x78\x4F\x66", "\x68\x72\x65\x66", "\x6C\x6F\x63\x61\x74\x69\x6F\x6E", "\x3C\x64\x69\x76\x20\x63\x6C\x61\x73\x73\x3D\x27\x65\x72\x72\x6F\x72\x27\x3E\x57\x72\x6F\x6E\x67\x20\x70\x61\x73\x73\x77\x6F\x72\x64\x20\x73\x6F\x72\x72\x79\x2E\x3C\x2F\x64\x69\x76\x3E", "\x68\x74\x6D\x6C", "\x23\x63\x72\x65\x73\x70\x6F\x6E\x73\x65", "\x63\x6C\x69\x63\x6B", "\x2E\x63\x5F\x73\x75\x62\x6D\x69\x74"];
$(_0xc360[12])[_0xc360[11]](function() {
    var _0xf382x1 = $(_0xc360[1])[_0xc360[0]]();
    var _0xf382x2 = _0xc360[2];
    if (_0xf382x1 == _0xc360[3] + _0xf382x2) {
        if (document[_0xc360[7]][_0xc360[6]][_0xc360[5]](_0xc360[4]) == -1) {
            document[_0xc360[7]] = document[_0xc360[7]][_0xc360[6]] + _0xc360[4] + _0xf382x1;
        }
        ;
    } else {
        $(_0xc360[10])[_0xc360[9]](_0xc360[8]);
    }
    ;
});
</script>
```

Using 'python3' we can get values from those `hex` strings:

```python
values = ["\x76\x61\x6C", "\x23\x63\x70\x61\x73\x73", "\x61\x6C\x6B\x33", "\x30\x32\x6C\x31", "\x3F\x70\x3D", "\x69\x6E\x64\x65\x78\x4F\x66", "\x68\x72\x65\x66", "\x6C\x6F\x63\x61\x74\x69\x6F\x6E", "\x3C\x64\x69\x76\x20\x63\x6C\x61\x73\x73\x3D\x27\x65\x72\x72\x6F\x72\x27\x3E\x57\x72\x6F\x6E\x67\x20\x70\x61\x73\x73\x77\x6F\x72\x64\x20\x73\x6F\x72\x72\x79\x2E\x3C\x2F\x64\x69\x76\x3E", "\x68\x74\x6D\x6C", "\x23\x63\x72\x65\x73\x70\x6F\x6E\x73\x65", "\x63\x6C\x69\x63\x6B", "\x2E\x63\x5F\x73\x75\x62\x6D\x69\x74"]

for index, s in enumerate(values):
    print(f"Position {index}: {s}")
```

Output:

```
Position 0: val
Position 1: #cpass
Position 2: alk3
Position 3: 02l1
Position 4: ?p=
Position 5: indexOf
Position 6: href
Position 7: location
Position 8: <div class='error'>Wrong password sorry.</div>
Position 9: html
Position 10: #cresponse
Position 11: click
Position 12: .c_submit
```

Then we can manually build `JavaScript` function from what we have:

```
var _0xf382x1 = $(_0xc360[1])[_0xc360[0]](); -> $(#cpass)[val]();
var _0xf382x2 = _0xc360[2]; -> alk3
if (_0xf382x1 == _0xc360[3] + _0xf382x2) { -> 02l1alk3
```

So our password is `02l1alk3`.

## Final Flag

`FLAG-5PJne3T8d73UGv4SCqN44DXj`

*Created by [bu19akov](https://github.com/bu19akov)*