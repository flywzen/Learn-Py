def caesar_cipher(text, shift):
    result = []
    for char in text:
        # Cek jika karakter adalah huruf besar atau kecil
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            # Geser karakter
            shifted_char = chr(((ord(char) - shift_base + shift) % 26) + shift_base)
            result.append(shifted_char)
        else:
            result.append(char)  # Pertahankan spasi atau karakter non-huruf
    return ''.join(result)

# Teks asli
text = "Amor Fati"

# Enkripsi dengan pergeseran 3
encrypted_text = caesar_cipher(text, 3)
print("Enkripsi Caesar Cipher:", encrypted_text)
