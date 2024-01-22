import hashlib
import os

def main():
    # Define character sets
    charset_small = list(range(48, 58)) + list(range(97, 103))
    charset = list(range(48, 58)) + list(range(97, 123))    

    # Directory for storing hash files
    base_path = "hashes"

    # Create the directory if it doesn't exist
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    # Open hash files
    fs = {}
    for f1 in charset_small:
        for f2 in charset_small:
            for f3 in charset_small:
                for f4 in charset_small:
                    bucket = chr(f1) + chr(f2) + chr(f3) + chr(f4)
                    file_path = os.path.join(base_path, bucket)
                    fs[bucket] = open(file_path, 'w')            

    # Build the list of plaintext to bruteforce
    for a in charset:
        for b in charset:
            for c in charset:
                for d in charset:
                    for e in charset:
                        for f in charset:
                            p = chr(a) + chr(b) + chr(c) + chr(d) + chr(e) + chr(f)
                            h = hashlib.sha1(p.encode()).hexdigest()  # Corrected to encode the string before hashing                            
                            fs[h[:4]].write('%s,%s\n' % (p, h))

    # Close all opened files
    for f in fs.values():
        f.close()

    print('Done.')

if __name__ == '__main__':
    main()
