import base64
import argparse

def encode(input_string):
    # Convert the input string to bytes
    input_bytes = input_string.encode('utf-8')

    # Encode the bytes using base64
    encoded_bytes = base64.b64encode(input_bytes)

    # Convert the encoded bytes to a string
    encoded_string = encoded_bytes.decode('utf-8')

    return encoded_string

def decode(input_string):
    # Convert the input string to bytes
    input_bytes = input_string.encode('utf-8')

    # Decode the bytes using base64
    decoded_bytes = base64.b64decode(input_bytes)

    # Convert the decoded bytes to a string
    decoded_string = decoded_bytes.decode('utf-8')

    return decoded_string

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Base64 encode/decode a string')
    parser.add_argument('input_string', type=str, help='The input string to encode/decode')
    parser.add_argument('-e', '--encode', action='store_true', help='Encode the input string')
    parser.add_argument('-d', '--decode', action='store_true', help='Decode the input string')
    args = parser.parse_args()

    if args.encode and args.decode:
        print("Error: Cannot specify both --encode and --decode")
    elif not args.encode and not args.decode:
        print("Error: Must specify either --encode or --decode")
    elif args.encode:
        encoded_string = encode(args.input_string)
        print(f"Encoded string: {encoded_string}")
    elif args.decode:
        decoded_string = decode(args.input_string)
        print(f"Decoded string: {decoded_string}")
