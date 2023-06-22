import argparse
import hashlib
def encrypt_with_shifting_bits(text, shift_amount):
    text = ''.join([bin(ord(i))[2:].zfill(8) for i in text])
    shifted_text = text[-shift_amount:] + text[:-shift_amount]  # Shift right
    res = ""
    for i in range(0, len(shifted_text), 8):
        res += chr(int(shifted_text[i:i+8], 2))
    return res
def encrypt_with_sha256(data):
    hashed_data = hashlib.sha256(data.encode()).hexdigest()
    return hashed_data
def encrypt_with_sha512(data):
    hashed_data = hashlib.sha512(data.encode()).hexdigest()
    return hashed_data
def reverse_bytes(data):
    return data[::-1]
def reverse_bits(data):
    binary_data = ''.join(format(ord(c), '08b') for c in data)
    reversed_bits = binary_data[::-1]
    encrypted_data = ''
    for i in range(0, len(reversed_bits), 8):
        byte = reversed_bits[i:i + 8]
        encrypted_data += chr(int(byte, 2))
    return encrypted_data
def flip_bits(data):
    flipped_data = ''
    for c in data:
        binary_repr = bin(ord(c))[2:].zfill(8)
        flipped_binary = ''.join('1' if bit == '0' else '0' for bit in binary_repr)
        flipped_data += chr(int(flipped_binary, 2))
    return flipped_data
def nullify(data):
    return '\x00' * len(data)
def main():
    parser = argparse.ArgumentParser(description='Encrypt/decrypt data using various encryption methods')
    parser.add_argument('-shift', type=int, metavar='shift_num', help='Number of shifts for shifting encryption')
    parser.add_argument('-sha256', action='store_true', help='Perform SHA-256 encryption')
    parser.add_argument('-sha512', action='store_true', help='Perform SHA-512 encryption')
    parser.add_argument('-revbyte', action='store_true', help='Perform reverse byte encryption')
    parser.add_argument('-revbit', action='store_true', help='Perform reverse bit encryption')
    parser.add_argument('-flipbit', action='store_true', help='Perform flip bit encryption')
    parser.add_argument('-null', action='store_true', help='Perform nullify encryption')
    parser.add_argument('input', help='Input file path')
    parser.add_argument('output', nargs='?', help='Output file path')
    parser.add_argument('-verbose', action='store_true', help='Outputs the output')
    args = parser.parse_args()
    with open(args.input, 'r', encoding='utf-8') as input_file:
        data = input_file.read()
    encrypted_data = ''
    if args.shift is not None:
        encrypted_data = encrypt_with_shifting_bits(data, args.shift)
    elif args.sha256:
        encrypted_data = encrypt_with_sha256(data)
        print("SHA256 Checksum: " + encrypted_data)
    elif args.sha512:
        encrypted_data = encrypt_with_sha512(data)
        print("SHA512 Checksum: " + encrypted_data)
    elif args.revbyte:
        encrypted_data = reverse_bytes(data)
    elif args.revbit:
        encrypted_data = reverse_bits(data)
    elif args.flipbit:
        encrypted_data = flip_bits(data)
    elif args.null:
        encrypted_data = nullify(data)
    if args.verbose:
        if args.shift is not None:
            print("Shift Encryption / Decryption: " + encrypted_data)
        elif args.revbyte:
            print("Reverse Byte Encryption / Decryption: " + encrypted_data)
        elif args.revbit:
            print("Reverse Bit Encryption / Decryption: " + encrypted_data)
        elif args.flipbit:
            print("Flip Bit Encryption / Decryption: " + encrypted_data)
    if args.output: open(args.output, 'w', encoding="utf-8").write(encrypted_data)
    else: open(args.input, 'w', encoding="utf-8").write(encrypted_data)
if __name__ == '__main__':
    main()