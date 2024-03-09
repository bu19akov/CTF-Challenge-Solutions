def extract_second_column(input_file, output_file):
    # Initialize an empty list to store second column values
    second_column_values = []
    
    # Read the input file
    with open(input_file, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 2:  # Ensure the line has at least two columns
                second_column_values.append(parts[1])
    
    # Convert the list of second column values to a single string with spaces
    single_line = ' '.join(second_column_values)
    
    # Write the single line string to the output file
    with open(output_file, 'w') as file:
        file.write(single_line)

# Example usage
input_file = 'output.txt'
new_output_file = 'second_column_values.txt'
extract_second_column(input_file, new_output_file)
