from cryptography.fernet import Fernet

# 1. Ģenerējam slepeno atslēgu
# Reālā dzīvē šī atslēga būtu droši jāsaglabā (piemēram, .env failā)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# 2. Oriģinālā ziņa
original_text = "Mana slepenā parole123".encode() # Datiem jābūt baitu formātā

# 3. Šifrēšana
cipher_text = cipher_suite.encrypt(original_text)
print(f"Aizšifrēts: {cipher_text}")

# 4. Atšifrēšana
decrypted_text = cipher_suite.decrypt(cipher_text)
print(f"Atšifrēts: {decrypted_text.decode()}")
