import jwt
import sys
import base64
import argparse 

# Get the JWT token from the command line arguments
jwt_token = sys.argv[1]

def add_padding(input_str):
    num_pad_chars = len(input_str) % 4
    if num_pad_chars == 0:
        return input_str
    num_missing_pad_chars = 4 - num_pad_chars
    return input_str + '='*num_missing_pad_chars

def base_64_decode(input):
    encoded = add_padding(input).encode('utf-8')
    print("# Original: ")
    print(encoded)
    print("# Decoded: ")
    print(base64.b64decode(encoded).decode('utf-8'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='JWT Token parser. Decodes base64 strings and displays Header and Payload ')
    parser.add_argument('jwt_token', type=str, help='The input string to parse')
    args = parser.parse_args()

    parts = jwt_token.split('.')
    print("\nHeader: ")
    base_64_decode(parts[0])

    print("\nPayload: ")
    base_64_decode(parts[1])

# print("\nSignature: ")
# base_64_decode(parts[2])

# Create a jwt token 
# payload_data = {
#     'sub': '4242',
#     'name': 'Jessica Temporal',
#     'nickname': 'Jess'
# }

# secret = 'my_super_secret'
# jwt_token = jwt.encode(payload=payload_data, key=secret, algorithm='HS256')
# print("Created token: "+ jwt_token)

# Decode the JWT token
# try:
#     header_data = jwt.get_unverified_header(jwt_token)
#     print(header_data)
#     decoded_token = jwt.decode(
#         jwt_token, 
#         algorithms = header_data['alg'],
#         verify=False
#         )
#     print(decoded_token)
# except jwt.exceptions.DecodeError:
#     print("Invalid JWT token")