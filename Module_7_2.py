from pprint import pprint

def custom_write(file_name, *strings):
    file = open(file_name, 'w', encoding= 'utf8')
    num = 0
    for i in strings:
        num += 1
        tuple_ = num, file.tell()
        dict_ = tuple_, i
        print(dict_)
        file.write(i + '\n')
    file.close()

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

custom_write('test.txt', *info)