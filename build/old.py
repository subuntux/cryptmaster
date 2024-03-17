#!/usr/bin/env python

import sys

def encrypt_decrypt(input_text, key, mode):
    output_text = ""
    for i, char in enumerate(input_text):
        shift = int(key[i % len(key)])
        if mode == "--crypt":
            shifted_char = chr(ord(char) + shift)
        elif mode == "--decrypt":
            shifted_char = chr(ord(char) - shift)
        else:
            print("Unknown mode.")
            return None
        output_text += shifted_char
    return output_text

def main():
    if len(sys.argv) < 4 or sys.argv[1] == "--help":
        print("Usage:")
        print("./crypter --crypt <inputfile> <outputfile>")
        print("./crypter --decrypt <inputfile> <outputfile>")
        print("./crypter --help")
        return
    
    mode = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    with open(input_file, 'r') as f:
        input_text = f.read().replace('\n', '')

    key = input("Please enter a ten-digit number: ")
    if len(key) != 10 or not key.isdigit():
        print("Invalid input for the key.")
        return

    encrypted_decrypted_text = encrypt_decrypt(input_text, key, mode)

    if encrypted_decrypted_text is not None:
        with open(output_file, 'w') as f:
            f.write(encrypted_decrypted_text)

if __name__ == "__main__":
    main()
