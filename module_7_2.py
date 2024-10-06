import io
from pprint import pprint


def custom_write(file_name, strings):
    string_positions = {}
    file = open(file_name, 'w', encoding='utf-8')

    for line_number, string in enumerate(strings, 1):
        byte_position = file.tell()
        file.write(string + '\n')
        string_positions[(line_number, byte_position)] = string
    file.close()

    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
