# Вариант 1 с оператором in и методом upper()
def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        if (root_word.upper() in str(other_words[i]).upper()) or (str(other_words[i]).upper() in root_word.upper()):
            same_words.append(other_words[i])
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)  # ['richiest', 'orichalcum', 'richies']
print(result2)  # ['Able', 'Disable']

# Вариант 2 с методами count() и lower()
def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        if root_word.lower().count(str(other_words[i]).lower()) or str(other_words[i]).lower().count(root_word.lower()):
            same_words.append(other_words[i])
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)  # ['richiest', 'orichalcum', 'richies']
print(result2)  # ['Able', 'Disable']
