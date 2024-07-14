class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()
                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        text = text.replace(punct, '')
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []
        return all_words

    def find(self, word):
        word = word.lower()
        dict_find = {}
        for name, words in self.get_all_words().items():
            if word in words:
                result = 1 + words.index(word)
                dict_find[name] = result
        return dict_find

    def count(self, word):
        word = word.lower()
        dict_count = {}
        for key, words in self.get_all_words().items():
            result = words.count(word)
            dict_count[key] = result
        return dict_count





finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('везде')) 
print(finder2.count('teXT'))