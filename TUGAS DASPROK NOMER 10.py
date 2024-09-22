T = int(input())  # jumlah baca test case nya

for _ in range(T):
    C, K = map(int, input().split())  # Baca nilai C dan K nya (Shift)
    ciphertext = input().strip()  # untuk baca pesan terenkripsinya

    # Dekripsi pesan dengan shift C
    decrypted_message_C = ''.join(
        chr((ord(str) - (97 if str.islower() else 65) - C) % 26 + (97 if str.islower() else 65))
        if str.isalpha() else str
        for str in ciphertext
        
    )
    print(decrypted_message_C)

    # Dekripsi pesan dengan shift K
    decrypted_message_K = ''.join(
        chr((ord(str) - (97 if str.islower() else 65) - K) % 26 + (97 if str.islower() else 65))
        if str.isalpha() else str
        for str in ciphertext
    )
    print(decrypted_message_K)