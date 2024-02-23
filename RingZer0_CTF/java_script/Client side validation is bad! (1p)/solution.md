# Client side validation is bad!

## Challenge Details 

- **CTF:** RingZer0
- **Category:** JavaScript
- **Points:** 1

## Provided Materials

- Login form

## Solution

We can find following script while analyzing the page with `Web-Inspector`:

```javascript
<script>
// Look's like weak JavaScript auth script :)
$(".c_submit").click(function(event) {
    event.preventDefault()
    var u = $("#cuser").val();
    var p = $("#cpass").val();
    if (u == "admin" && p == String.fromCharCode(74, 97, 118, 97, 83, 99, 114, 105, 112, 116, 73, 115, 83, 101, 99, 117, 114, 101)) {
        if (document.location.href.indexOf("?p=") == -1) {
            document.location = document.location.href + "?p=" + p;
        }
    } else {
        $("#cresponse").html("<div class='alert alert-danger'>Wrong password sorry.</div>");
    }
});
</script>
```

So the username is `admin` and password we can get using `python3`:

```sh
$ python3
>>> ''.join([chr(x) for x in [74, 97, 118, 97, 83, 99, 114, 105, 112, 116, 73, 115, 83, 101, 99, 117, 114, 101]])
'JavaScriptIsSecure'
```

## Final Flag

`FLAG-66Jq5u688he0y46564481WRh`

*Created by [bu19akov](https://github.com/bu19akov)*