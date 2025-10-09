import hashlib

message = "Hello, Cryptography!".encode()

md5_hash = hashlib.md5(message).hexdigest()
print("MD5 Hash: ",md5_hash)

sha1_hash = hashlib.sha1(message).hexdigest()
print("SHA-1 Hash: ",sha1_hash)
