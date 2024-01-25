#!/usr/bin/env python3

def rc8(state, key, n):
    '''
    Top Secret RC8 Stream Cipher
    '''
    while (n > 0):
        yield state & 0xff
        for _ in range(8):
            c, s = key, state
            b = 0
            while c:
                b ^= c & 1 * s & 1
                c >>= 1 ; s >>= 1
            state = state >> 1 | b << 63
        n -= 1

def main():
    seed_str, key_str = "30EE66FD6A3DEAD3", "008000021DCDC007"
    seed = int(seed_str, 16)  # Convert hexadecimal string to integer
    key = int(key_str, 16)    # Convert hexadecimal string to integer

    with open("./transcript.wav.enc", 'rb') as fin:
        data = bytearray(fin.read())

    for i,x in enumerate(rc8(seed, key, len(data))):
        data[i] ^= x

    with open("./transcript.wav", 'wb') as fout:
        fout.write(data)

if __name__ == "__main__":
    main()