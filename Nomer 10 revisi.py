T = int(input())  # jumlah test case

for _ in range(T):
    C, K = map(int, input().split())  # Baca nilai C dan K (shift)
    ciphertext = input().strip()  # pesan terenkripsi

    # Fungsi untuk mendekripsi pesan dengan shift tertentu
    def decrypt_message(shift, ciphertext):
        decrypted_message = ''.join(
            chr((ord(ch) - (97 if ch.islower() else 65) - shift) % 26 + (97 if ch.islower() else 65))
            if ch.isalpha() else ch
            for ch in ciphertext
        )
        return decrypted_message

    # Dekripsi pesan pertama dengan shift C
    decrypted_message_C = decrypt_message(C, ciphertext)

    # Dekripsi hasil dari shift C dengan shift K
    decrypted_message_K = decrypt_message(K, decrypted_message_C)

    # Output hasil akhir setelah kedua dekripsi
    print(decrypted_message_K)
