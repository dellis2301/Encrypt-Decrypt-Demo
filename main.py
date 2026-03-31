from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# =====================
# SYMMETRIC ENCRYPTION
# =====================
print("=== SYMMETRIC (AES) ===")

# Key
sym_key = Fernet.generate_key()
cipher = Fernet(sym_key)

# Input
message = b"Hello, this is a secret message!"

# Encrypt / Decrypt
sym_encrypted = cipher.encrypt(message)
sym_decrypted = cipher.decrypt(sym_encrypted)

print("KEY:")
print(sym_key)

print("\nINPUT:")
print(message)

print("\nENCRYPTED:")
print(sym_encrypted)

print("\nDECRYPTED:")
print(sym_decrypted)


# =====================
# ASYMMETRIC ENCRYPTION
# =====================
print("\n=== ASYMMETRIC (RSA) ===")

# Keys
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Convert keys to readable format
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Encrypt / Decrypt
asym_encrypted = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

asym_decrypted = private_key.decrypt(
    asym_encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("PUBLIC KEY:")
print(public_pem.decode())

print("PRIVATE KEY:")
print(private_pem.decode())

print("INPUT:")
print(message)

print("\nENCRYPTED:")
print(asym_encrypted)

print("\nDECRYPTED:")
print(asym_decrypted)
