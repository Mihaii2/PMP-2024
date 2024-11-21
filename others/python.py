

with open('a.txt') as f:
    data = f.read()

separators = [' ',',', '.', '!', '?', '\n']
all_words = []
current_word = ""


for char in data:
    if char in separators:
        if current_word:
            all_words.append(current_word)
            current_word = ""
    else:
            current_word += char

print(all_words)

words_sorted = sorted(all_words, key=lambda x: len(set(x)), reverse=True)

with open('output.txt', 'w') as f:
    for word in words_sorted:
        f.write(f'{word} - {len(set(word))}\n')
        print(f'{word} - {len(set(word))}')
