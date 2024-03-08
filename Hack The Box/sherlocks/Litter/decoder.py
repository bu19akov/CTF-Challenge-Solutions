import os

def read_dns_queries_from_pcap(pcap_path):
    """Execute tshark command to extract DNS query names from a pcap file."""
    command = f"tshark -r {pcap_path} -T fields -e dns.qry.name"
    raw_output = os.popen(command).read()
    return raw_output.strip().split('\n')

def decode_hex_string(hex_string):
    """Decode hex-encoded strings, filtering out non-printable characters."""
    hex_string = hex_string[18:].replace('.microsofto365.com', '').replace('.', '')
    try:
        bytes_object = bytes.fromhex(hex_string)
        ascii_string = bytes_object.decode("ASCII", errors='replace')
        return ''.join(char for char in ascii_string if char.isprintable() or char == '\n')
    except ValueError as e:
        print(f"Skipping invalid hex data due to error: {e}")
        return None

def main(pcap_file):
    lines = read_dns_queries_from_pcap(pcap_file)
    output_file_path = "./file.txt"

    with open(output_file_path, 'w') as file:
        for line in lines:
            if len(line) <= 56:
                continue
            decoded_string = decode_hex_string(line)
            if decoded_string:
                file.write(decoded_string + '\n')

if __name__ == "__main__":
    pcap_file_path = "./to_decode.pcap"
    main(pcap_file_path)

