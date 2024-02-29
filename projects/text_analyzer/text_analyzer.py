text = input('Write a text: ')
letters = input('Write tree letters to analize: ')

text_list = text.split(' ')
letters_list = list(letters)

letter_counter = {}
letter_counter[letters_list[0].upper()] = text.upper().count(letters_list[0].upper())
letter_counter[letters_list[1].upper()] = text.upper().count(letters_list[1].upper())
letter_counter[letters_list[2].upper()] = text.upper().count(letters_list[2].upper())

result = {
    'letter_count': letter_counter,
    'total_words': len(text_list),
    'first_letter': text[0],
    'last_letter': text[-1],
    'python': text.count('python') >= 1
}

print(result)
print('\n')
text_list.reverse()
print(' '.join(text_list));