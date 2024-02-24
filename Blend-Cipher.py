import math

def transpose_cipher_v2(text, num_cols):
    cipher_text = [''] * num_cols
    for col in range(num_cols):
        pointer = col
        while pointer < len(text):
            cipher_text[col] += text[pointer]
            pointer += num_cols
    return ''.join(cipher_text)

def vigenere_cipher_encrypt_v2(text, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key.upper()]
    plaintext_int = [ord(i) for i in text.upper()]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        if chr(plaintext_int[i]) in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            value = (plaintext_int[i] + key_as_int[i % key_length] - 2 * 65) % 26 + 65
            ciphertext += chr(value)
        else:
            ciphertext += text[i]
    return ciphertext

def caesar_cipher_modified(text, shift):
    encrypted_text = ""
    for i, char in enumerate(text.upper()):
        if char.isalpha():
            shifted = ((ord(char) - 65 + (shift + i)) % 26) + 65
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def mathematical_transformation(text, key):
    transformed_text = ""
    for char in text:
        if char.isalpha():
            transformed_value = (255 - ord(char) + key) % 128
            transformed_text += chr(transformed_value)
        else:
            transformed_text += char
    return transformed_text

def generate_mask_sequence_v2(key, length):
    mask = ('01' * (length // 2))[:length]
    return mask

def apply_binary_mask_v2(text, mask_sequence):
    masked_text = ""
    for i, char in enumerate(text):
        if char.isalpha():
            char_bin = format(ord(char), '08b')
            mask_bin = format(int(mask_sequence[i % len(mask_sequence)]) * 255, '08b')
            xor_result = int(char_bin, 2) ^ int(mask_bin, 2)
            masked_text += chr(xor_result % 128)
        else:
            masked_text += char
    return masked_text

def cryptoblend_cipher_v3(message, trans_cols, vigenere_key, caesar_shift, math_key, mask_key):
    message = ''.join(filter(str.isalpha, message.upper()))
    transposed = transpose_cipher_v2(message, trans_cols)
    vigenere_encrypted = vigenere_cipher_encrypt_v2(transposed, vigenere_key)
    caesar_encrypted = caesar_cipher_modified(vigenere_encrypted, caesar_shift)
    math_transformed = mathematical_transformation(caesar_encrypted, math_key)
    mask_sequence = generate_mask_sequence_v2(mask_key, len(math_transformed))
    masked_encrypted = apply_binary_mask_v2(math_transformed, mask_sequence)
    return masked_encrypted

# Exemplo de uso
message_example = "Test"
trans_cols_example = 5
vigenere_key_example = "Joas"
caesar_shift_example = 3
math_key_example = 10
mask_key_example = "joas2"

encrypted_message_example = cryptoblend_cipher_v3(
    message_example, 
    trans_cols_example, 
    vigenere_key_example, 
    caesar_shift_example, 
    math_key_example, 
    mask_key_example
)

print(encrypted_message_example)
