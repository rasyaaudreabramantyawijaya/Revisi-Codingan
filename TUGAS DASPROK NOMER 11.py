input_string = input().strip()

seen = set()

result = []

for str in input_string:
    
    if str not in seen:
        seen.add(str)
        result.append(str)

print(''.join(result))