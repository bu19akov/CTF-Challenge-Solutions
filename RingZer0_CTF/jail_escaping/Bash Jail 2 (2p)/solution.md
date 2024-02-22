# Bash Jail 2

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Jail Escaping
- **Points:** 2

## Provided Materials

- SSH credentials

## Solution

Challenge bash code:

```sh
function check_space {
	if [[ $1 == *[bdks';''&'' ']* ]]
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
		output="echo Your command is: $input"
		eval $output
	fi
done 
```

None of the symbols from `cat flag.txt` are in the restricted characters set, so we need to figure out how to execute it without the space character.

**Redirection**: The `<` symbol is used for input redirection. It tells the shell to read the input for the command from a file instead of from the standard input (keyboard). In this case, `cat<flag.txt` means that the `cat` command will read its input from `flag.txt`.

But we also need `command substitution`:

**Command Substitution**: The `$(...)` syntax is used for command substitution. It executes the command inside the parentheses and substitutes the command's output into the outer command. This means that the shell will take the output of the command inside `$(...)` and use it as part of the command line.

`$(cat<flag.txt)` will read the contents of flag.txt and then execute those contents as a command:

```sh
Your input:
$(cat<flag.txt)
Your command is: FLAG-a78i8TFD60z3825292rJ9JK12gIyVI5P
```

## Final Flag

`FLAG-a78i8TFD60z3825292rJ9JK12gIyVI5P`

*Created by [bu19akov](https://github.com/bu19akov)*