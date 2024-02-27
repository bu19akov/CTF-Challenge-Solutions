import re

# Define the path to your input file
file_path = './diss.txt'

# Initialize a dictionary to store the lowest number found for each position
# Initialize with high values assuming a realistic upper bound
lowest_numbers = {i: 999 for i in range(1, 38)}

# Compile the regex pattern to match the lines
pattern = re.compile(r'User id:1 AND ORD\(MID\(\(SELECT IFNULL\(CAST\(flag AS CHAR\),0x20\) FROM chart_db\.flag ORDER BY flag LIMIT 0,1\),(\d+),1\)\)>(\d+) was not found')

# Read the file and search for matching lines
with open(file_path, 'r', errors='ignore') as file:
    for line in file:
        match = pattern.search(line)
        if match:
            position = int(match.group(1))
            number = int(match.group(2))
            # Update the dictionary if a lower number is found for the position
            if number < lowest_numbers[position]:
                lowest_numbers[position] = number

# Print the lowest number found for each position
# for position in sorted(lowest_numbers.keys()):
#    print(f"Position {position}: {lowest_numbers[position]}")

ascii_string = ''.join(chr(lowest_numbers[pos]) for pos in sorted(lowest_numbers.keys()))

print(ascii_string)