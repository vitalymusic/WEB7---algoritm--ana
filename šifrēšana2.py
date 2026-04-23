import hashlib

# 1. Dati, kurus vēlamies hešēt
password = "manaDrošaParole123"

# 2. Pārvēršam tekstu baitos un palaižam caur SHA-256 algoritmu
hash_object = hashlib.sha256(password.encode())

# 3. Iegūstam hešu heksadecimālā formātā (lasāmā virknē)
hex_dig = hash_object.hexdigest()

print(f"Oriģinālais teksts: {password}")
print(f"SHA-256 hešs: {hex_dig}")