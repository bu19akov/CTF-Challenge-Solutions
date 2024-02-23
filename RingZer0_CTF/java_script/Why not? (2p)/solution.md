# Why not?

## Challenge Details 

- **CTF:** RingZer0
- **Category:** JavaScript
- **Points:** 2

## Provided Materials

- Login form

## Solution

We can find following script while analyzing the page with `Web-Inspector`:

```javascript
<script>
// Look's like weak JavaScript auth script :)
$(".c_submit").click(function(event) {
    event.preventDefault();
    var k = new Array(176, 214, 205, 246, 264, 255, 227, 237, 242, 244, 265, 270, 283);
    var u = $("#cuser").val();
    var p = $("#cpass").val();
    var t = true;

    if (u == "administrator") {
        for (i = 0; i < u.length; i++) {
            if ((u.charCodeAt(i) + p.charCodeAt(i) + i * 10) != k[i]) {
                $("#cresponse").html("<div class='alert alert-danger'>Wrong password sorry.</div>");
                t = false;
                break;
            }
        }
    } else {
        $("#cresponse").html("<div class='alert alert-danger'>Wrong password sorry.</div>");
        t = false;
    }
    if (t) {
        if (document.location.href.indexOf("?p=") == -1) {
            document.location = document.location.href + "?p=" + p;
        }
    }
});
</script>
```

If we have such a password, that when we iterate from `0` to `u.length (12)`, each corresponding character at position `i` from username *(`administrator`)* + character at position `i` from password + `i * 10` will be equal to character at position `i` in `k`, we will be granted the access. We can write small python script to get our password:

`username[i] + password[i] + i*10 = k[i] --> password[i] = k[i] - username[i] - i*10`

```python
k = [176, 214, 205, 246, 264, 255, 227, 237, 242, 244, 265, 270, 283]
u = "administrator"
password = ""
for i in range(0, len(u)):
    password += chr(k[i] - ord(u[i]) - i * 10)
```

Output:

```
OhLord4309111
```


## Final Flag

`FLAG-65t23674o6N2NehA44272G24`

*Created by [bu19akov](https://github.com/bu19akov)*