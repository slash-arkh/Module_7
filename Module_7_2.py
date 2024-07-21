

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding= 'utf8')
    num = 0
    for i in strings:
        num += 1
        tuple_ = num, file.tell()
        strings_positions = {}
        strings_positions_ = tuple_ , i
        strings_positions[tuple_]=  i
        file.write(i + '\n')
        print(strings_positions_)
    return strings_positions

    file.close()


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

custom_write('test.txt', info)
