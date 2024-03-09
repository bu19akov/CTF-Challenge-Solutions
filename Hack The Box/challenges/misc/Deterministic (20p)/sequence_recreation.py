def find_sequence(start_number, end_number, input_file, output_file):
    # Read the input file and store lines
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Dictionary to map first column numbers to their full lines, skipping non-digit lines
    num_to_line = {}
    for line in lines:
        if line.split():  # Check if the line is not empty
            try:
                # Attempt to convert the first token to int
                first_col_num = int(line.split()[0])
                num_to_line[first_col_num] = line
            except ValueError:
                # Skip the line if the first token cannot be converted to an integer
                continue

    current_number = start_number
    with open(output_file, 'w') as file:
        while current_number in num_to_line:
            # Write the matching line to the output file
            file.write(num_to_line[current_number])
            
            # Get the next number to search for from the third column
            next_number = int(num_to_line[current_number].split()[2])
            
            # Check if the next number is the end condition
            if next_number == end_number:
                break
            
            current_number = next_number

# Example usage
start_number = 69420
end_number = 999
input_file = 'deterministic.txt'
output_file = 'output.txt'
find_sequence(start_number, end_number, input_file, output_file)
