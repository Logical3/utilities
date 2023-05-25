import argparse
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519, rsa

def generate_rsa_keypair():
    # Generate RSA key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096
    )
    return private_key

def generate_ed25519_keypair():
    # Generate Ed25519 key pair
    private_key = ed25519.Ed25519PrivateKey.generate()
    return private_key

def save_keypair(private_key, public_key, private_file, public_file):
    # Serialize private key to PEM format
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    # Serialize public key to OpenSSH format
    public_ssh = public_key.public_bytes(
        encoding=serialization.Encoding.OpenSSH,
        format=serialization.PublicFormat.OpenSSH
    ).decode('utf-8')

    # Save private key to a file
    with open(private_file, 'wb') as f:
        f.write(private_pem)

    # Save public key to a file
    with open(public_file, 'w') as f:
        f.write(public_ssh)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate SSH key pair')
    parser.add_argument('-t', '--type', choices=['rsa', 'ed25519'], default='rsa', help='SSH key type')
    parser.add_argument('-C', '--email', default='', help='Email address')

    args = parser.parse_args()

    private_key_file = 'private_key.pem'
    public_key_file = 'public_key'

    if args.type == 'rsa':
        private_key = generate_rsa_keypair()
    else:
        private_key = generate_ed25519_keypair()

    public_key = private_key.public_key()

    save_keypair(private_key, public_key, private_key_file, public_key_file)

    print(f'Successfully generated {args.type.upper()} key pair.')
    print(f'Private key saved to: {private_key_file}')
    print(f'Public key saved to: {public_key_file}')
