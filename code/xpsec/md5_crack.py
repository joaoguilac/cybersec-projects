import hashlib
import sys

def get_md5_hash(input_string):
    md5_hasher = hashlib.md5()
    # hash function only accepts bytes, we need to encode
    md5_hasher.update(input_string.encode('utf-8'))
    # converts the encoded data to hexadecimal format
    hash_string = md5_hasher.hexdigest()
    return hash_string

if len(sys.argv) < 3:
    print('Uso: python md5.py <wordlist> <hash>')
    sys.exit(1)

wordlist_path = sys.argv[1]
target_hash = sys.argv[2]

# print(get_md5_hash('william'))

with open(wordlist_path, 'r') as wordlist_file:
    for password in wordlist_file:
        password = password.strip()
        hash_guess = get_md5_hash(password)

        if hash_guess == target_hash:
            print(f'Senha encontrada: {password}')
            break
    if hash_guess != target_hash:
        print('A senha não foi encontrada na wordlist.')