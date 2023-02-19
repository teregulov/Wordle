from random import randint

from colorama import Fore, Back, Style


def get_alphabet(words: list = None, start: str = None, finish: str = None) -> list:
    """
    returns alphabet of symbols. User only words or start+finish symbols
    :param words: number of words to extract symbols
    :param start: start symbol for range
    :param finish: finish symbol for range
    :return: alphabet of symbols
    """

    if start is None and finish is None and words is None:
        __alphabet = {'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                      'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'ё'}
        return __alphabet
    if words is not None:
        __alphabet = []
        for __word in words:
            for letter in __word:
                if letter not in __alphabet:
                    __alphabet.append(letter)
        __alphabet.sort()
        return __alphabet
    elif start is not None and finish is not None:
        __alphabet = []
        for i in range(ord(start), ord(finish) + 1):
            __alphabet.append(chr(i))
        __alphabet.sort()
        return __alphabet


def check_word(word, supported_symbols) -> bool:
    """
    returns True is all symbols of word are from supported symbols
    :param word: word to check
    :param supported_symbols: alphabet
    :return: True if all symbols in word from alphabet
    """
    for letter in word:
        if letter not in supported_symbols:
            return False
    return True


def get_words(file, supported_symbols, length) -> list:
    """
    collects words from file and returns words if it's good for game
    :param file: name of the file
    :param supported_symbols: alphabet for checking words
    :param length: len of the words for game
    :return: list of fits the game
    """
    __words = []
    with open(file, 'r', encoding='utf-8') as __words_f:
        for __word in __words_f.read().split():
            if len(__word) == length and check_word(__word, supported_symbols):
                __words.append(__word.lower())
    return __words


def game_start(game_words):
    parameters = {'secret': game_words[randint(0, len(game_words)-1)],
                  'attempts': 6,
                  'letters_did': [],
                  'opened_letters': [0]*5


    }
    print("НОВАЯ ИГРА")
#    print(parameters['secret'])

    while True:
        ans = input("ВВЕДИТЕ СЛОВО: ")
        if ans.lower() == 'выход':
            break
        if len(ans) == 5:
            if ans.lower() == parameters['secret']:
                print("ВЫ ВЫИГРАЛИ")
                break
            print("-     УГУДАНО: ", end='')
            for i, letter in enumerate(ans.lower()):
                if letter == parameters['secret'][i]:
                    print(Back.WHITE, Fore.BLACK, letter, sep='', end='')
                    print(Style.RESET_ALL, end='')
                else:
                    print('-', end='')
            print()
        else:
            print("НЕВЕРНАЯ ДЛИНА")

    return parameters


if __name__ == "__main__":

    alphabet = get_alphabet(start='а', finish='я')
    my_words = get_words('words.txt', alphabet, 5)

    game = game_start(my_words)

    print(Style.RESET_ALL)
    print(Back.WHITE,Fore.BLACK +"КОНЕЦ", end=' ')