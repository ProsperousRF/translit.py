#! python3

"""
Заменяет буквы русского алфавита буквами английского алфавита по правилам, установленным приказом
Федеральной миграционной службы от 26 марта 2014 г. N 211 "Об утверждении Административного
регламента предоставления Федеральной миграционной службой государственной услуги по оформлению и
выдаче паспортов гражданина Российской Федерации, удостоверяющих личность гражданина Российской
Федерации за пределами территории Российской Федерации, содержащих электронный носитель информации".
(Приложение N 6)

Таблица транслитерации имени и фамилии для загранпаспорта
а - a
б - b
в - v
г - g
д - d
е - e
ё - e
ж - zh
з - z
и - i
й - i
к - k
л - l
м - m
н - n
о - o
п - p
р - r
с - s
т - t
у - u
ф - f
х - kh
ц - ts
ч - ch
ш - sh
щ - shch
ы - y
ъ - ie
э - e
ю - iu
я - ia

От себя: Добавлен мягкий знак, так как его изначально не было.
"""

import sys
import pyperclip


TRANSLIT_DICTONARY = {
    "а" : "a", "б" : "b", "в" : "v", "г" : "g", "д" : "d", "е" : "e", "ё" : "e",
    "ж" : "zh", "з" : "z", "и" : "i", "й" : "i", "к" : "k", "л" : "l", "м" : "m",
    "н" : "n", "о" : "o", "п" : "p", "р" : "r", "с" : "s", "т" : "t", "у" : "u",
    "ф" : "f", "х" : "kh", "ц" : "ts", "ч" : "ch", "ш" : "sh", "щ" : "shch",
    "ы" : "y", "ъ" : "ie", "э" : "e", "ю" : "iu", "я" : "ia", "ь" : "'"}

def translit(string):
    """Gets str translit it and returns str"""
    for key in TRANSLIT_DICTONARY:
        string = string.lower().replace(key, TRANSLIT_DICTONARY[key])
    return string

def get_titled(name):
    """ Set name titled """
    return ' '.join(w.capitalize() for w in name.split())

def get_shorts(name):
    """ Returns last two word cutted by dot"""
    name_set = name.split(" ")
    # Set name like Ivanov I.P.
    name = name_set[0] + " " + name_set[1][0] + "."+ name_set[2][0] + "."
    return name

# Gather our code in a main() function
def main():
    """ The MAIN function """
    # Get clipboard
    original_name = pyperclip.paste()
    # do the translation
    translit_name = translit(original_name)
    # Set name titled
    translit_name = get_titled(translit_name)

    # if no argument is given set short output
    if len(sys.argv) == 1:
        pyperclip.copy(get_shorts(translit_name))
    else:
        # set clipboard to translated name
        pyperclip.copy(translit_name)


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
