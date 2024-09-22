N = int(input())  # Jumlah ruangan
color_ids = list(map(int, input().split()))  # Daftar warna dari setiap ruangan

# Menghitung frekuensi setiap warna secara manual
freq = {}
for color in color_ids:
    if color in freq:
        freq[color] += 1
    else:
        freq[color] = 1

# Mencari warna yang paling sering muncul
most_common_color = max(freq.values())

# Menghitung jumlah ruangan yang perlu diubah
rooms_to_change = N - most_common_color

# Output jumlah ruangan yang perlu diubah
print(rooms_to_change)