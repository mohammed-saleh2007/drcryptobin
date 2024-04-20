import argparse

def en_de_crypt(input_file, output_file):
    with open(input_file, 'rb') as file:
        binary_data = file.read()

    inverted_data = bytearray()
    for byte in binary_data:
        inverted_byte = ~byte & 0xFF  
        inverted_data.append(inverted_byte)

    with open(output_file, 'wb') as file:
        file.write(inverted_data)

def main():
    parser = argparse.ArgumentParser(
        prog='\033[1;34mDR. Crypto\n\033[0m',
        description='encrypt or decrypt any file you want')
    parser.add_argument("-i", "--input", help="the file to encrypt/decrypt")
    parser.add_argument("-o", "--output", help="where is the output file")
    args = parser.parse_args()


    if args.input and args.output:
        en_de_crypt(args.input, args.output)
    else:
        print("Please specify the input and output file using -i and -o option. \nex: -i input.txt -o output.txt")   

main()
