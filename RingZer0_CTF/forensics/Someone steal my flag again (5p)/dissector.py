import re

def xor_hex(hex1, hex2):
    result = int(hex1, 16) ^ int(hex2, 16)
    return '{:x}'.format(result).zfill(len(hex2))

# Path to your input file
file_path = './diss.txt'

# Regular expressions to match the sequence number and data
seq_regex = re.compile(r'Sequence Number \(BE\): (\d+) \((0x[a-fA-F0-9]+)\)')
data_regex = re.compile(r'Data: ([a-fA-F0-9]+)')

# Lists to hold extracted sequence numbers and data
sequences = []
data_values = []

# Read the file and extract sequence numbers and data
with open(file_path, 'r') as file:
    for line in file:
        seq_match = seq_regex.search(line)
        if seq_match:
            # Ensure the sequence number is repeated to be 16 characters long
            sequence = seq_match.group(2)[2:]  # Remove '0x' prefix
            sequences.append(sequence * (16 // len(sequence)))
        data_match = data_regex.search(line)
        if data_match:
            data_values.append(data_match.group(1))

# Perform XOR on the sequence numbers and data
xor_results = [xor_hex(seq, data) for seq, data in zip(sequences, data_values)]

# Concatenate all XOR results into a single hex string
final_xor_result = ''.join(xor_results)

# Convert hex to bytes
bytes_from_hex = bytes.fromhex(final_xor_result)

# Convert bytes to string
ascii_string = bytes_from_hex.decode('ascii')

print(ascii_string)
