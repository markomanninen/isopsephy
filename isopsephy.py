# -*- coding: utf-8 -*-

import re
import pandas as pd

data = {}

"""

Data mapping between roman and greek letters, isopsephy values and linguistic components

Resources:

- http://en.wikipedia.org/wiki/Greek_alphabet
- http://www.chlt.org/FirstGreekBook/JWW_FGB1.html
- http://www.webtopos.gr/eng/languages/greek/alphabet/alpha.htm
- http://www.class.uh.edu/mcl/faculty/pozzi/grnl1/intr/0.2.1.pract.vow.htm

Segments:
- vowel
- consonant

Subsegments:
- semivowel (liquid, siblant and γ-nasal not specified on data table)
- double
- mute

Mutes (not specified on data table):

{class-order} {letter}

labial-smooth π
labial-middle β
labial-rought φ

palatal-smooth κ
palatal-middle γ
palatal-rought χ

lingual-smooth τ
lingual-middle δ
lingual-rought θ


Seven vowels: α ε η ι ο υ ω (a e h i o u w)

Numerals: ϛ ϙ ϡ (6, 90, 900)

If numerals are found on greek text, their values are used on isopsephy calculation
but there are no corresponding roman letters for them. This is mainly because roman alphabet
has only 26 letters, so I would need to use arbitrary 2 letters (j, v) and some other special
character for the last letter like _ or number or anything. But it doesn't really make sense.

My choice was just to use numerical value on transliterated text, so ϛ, ϙ and ϡ will be transliterated to 6, 90, 900. However, if you transform roman to greek, only literals are handled, no numbers at all.

"""

# letters from α to θ (1 to 9)
# alpha:http://en.wiktionary.org/wiki/ἄλφα
data[1] = {'greek': 'α', 
           'capital': 'Α',
           'name': 'αλφα',
           'segment': 'vowel',
           'subsegment': 'short',
           'roman': 'a',
           'value': 1}
# beta:http://en.wiktionary.org/wiki/βῆτα
data[2] = {'greek': 'β',
           'capital': 'Β',
           'name': 'βητα',
           'segment': 'consonant',
           'subsegment': 'mute',
           'roman': 'b',
           'value': 2}
# gamma:http://en.wiktionary.org/wiki/γάμμα
data[3] = {'greek': 'γ',
           'capital': 'Γ',
           'name': 'γαμμα',
           'segment': 'consonant',
           'subsegment': 'mute',
           'roman': 'g',
           'value': 3}
# delta:http://en.wiktionary.org/wiki/δέλτα
data[4] = {'greek': 'δ',
           'capital': 'Δ',
           'name': 'δελτα',
           'segment': 'consonant',
           'subsegment': 'mute',
           'roman': 'd',
           'value': 4}
# epsilon:http://en.wiktionary.org/wiki/epsilon
data[5] = {'greek': 'ε',
           'capital': 'Ε',
           'name': 'ε ψιλον',
           'segment': 'vowel',
           'subsegment': 'short',
           'roman': 'e',
           'value': 5}
# digamma/stigma/episemon/wau
# http://en.wikipedia.org/wiki/Digamma
data[6] = {'greek': 'ϛ', 'small2': 'ϝ',
           'capital': 'Ϛ', 'capital2': 'Ϝ',
           'name': 'διγαμμα', 'name2': 'στιγμα', 'name3': 'επισημον', 'name4': 'βαυ',
           'segment': 'numeral',
           #'subsegment': '',
           'roman': '6',
           'value': 6}
# zeta:http://en.wiktionary.org/wiki/ζῆτα
data[7] = {'greek': 'ζ',
           'capital': 'Ζ',
           'name': 'ζητα',
           'segment': 'consonant',
           'subsegment': 'double',
           'roman': 'z',
           'value': 7}
# eta:http://en.wiktionary.org/wiki/ἦτα
data[8] = {'greek': 'η',
           'capital': 'Η',
           'name': 'ητα',
           'segment': 'vowel',
           'subsegment': 'long',
           'roman': 'h',
           'value': 8}
# theta:http://en.wiktionary.org/wiki/θῆτα
data[9] = {'greek': 'θ',
           'capital': 'Θ',
           'name': 'θητα',
           'segment': 'consonant',
           'subsegment': 'mute',
           'roman': 'q',
           'value': 9}

# letters from ι to ϙ (10 to 90)
# iota:http://en.wiktionary.org/wiki/ἰῶτα
data[10] = {'greek': 'ι',
            'capital': 'Ι',
            'name': 'ιωτα',
            'segment': 'vowel',
            'subsegment': 'short',
            'roman': 'i',
            'value': 10}
# kappa:http://en.wiktionary.org/wiki/κάππα
data[20] = {'greek': 'κ',
            'capital': 'Κ',
            'name': 'καππα',
            'segment': 'consonant',
            'subsegment': 'mute',
            'roman': 'k',
            'value': 20}
# lambda:http://en.wiktionary.org/wiki/λάμβδα
data[30] = {'greek': 'λ',
            'capital': 'Λ',
            'name': 'λαμβδα',
            'segment': 'consonant',
            'subsegment': 'semivowel',
            'roman': 'l',
            'value': 30}
# mu:http://en.wiktionary.org/wiki/mu
data[40] = {'greek': 'μ',
            'capital': 'Μ',
            'name': 'μυ',
            'segment': 'consonant',
            'subsegment': 'semivowel',
            'roman': 'm',
            'value': 40}
# nu:http://en.wiktionary.org/wiki/νῦ
data[50] = {'greek': 'ν',
            'capital': 'Ν',
            'name': 'νυ',
            'segment': 'consonant',
            'subsegment': 'semivowel',
            'roman': 'n',
            'value': 50}
# xi:http://en.wiktionary.org/wiki/ξεῖ
data[60] = {'greek': 'ξ',
            'capital': 'Ξ',
            'name': 'ξει',
            'segment': 'consonant',
            'subsegment': 'double',
            'roman': 'c',
            'value': 60}
# omicron:http://en.wiktionary.org/wiki/omicron
data[70] = {'greek': 'ο',
            'capital': 'Ο',
            'name': 'ο μικρον',
            'segment': 'vowel',
            'subsegment': 'short',
            'roman': 'o',
            'value': 70}
# pi:http://en.wiktionary.org/wiki/πεῖ
data[80] = {'greek': 'π',
            'capital': 'Π',
            'name': 'πει',
            'segment': 'consonant',
            'subsegment': 'mute',
            'roman': 'p',
            'value': 80}
# koppa:http://en.wikipedia.org/wiki/Koppa_(letter)
# http://www.webtopos.gr/eng/languages/greek/alphabet/earlyletters.htm
data[90] = {'greek': 'ϙ', 'small2': 'ϟ',
            'capital': 'Ϙ', 'capital2': 'Ϟ',
            'name': 'κοππα',
            'segment': 'numeral',
            #'subsegment': '',
            'roman': '90',
            'value': 90}

# letters from ρ to ϡ (100 to 900)
# rho:http://en.wiktionary.org/wiki/ῥῶ
data[100] = {'greek': 'ρ',
             'capital': 'Ρ',
             'name': 'ρω',
             'segment': 'consonant',
             'subsegment': 'semivowel',
             'roman': 'r',
             'value': 100}
# sigma:http://en.wiktionary.org/wiki/σίγμα
data[200] = {'greek': 'σ', 'small2': 'ϲ', 'small3': 'ς',
             'capital': 'Σ', 'capital2': 'Ϲ', 'capital3': 'Σ',
             'name': 'σιγμα',
             'segment': 'consonant',
             'subsegment': 'semivowel',
             'roman': 's',
             'value': 200}
# tau:http://en.wiktionary.org/wiki/tau
data[300] = {'greek': 'τ',
             'capital': 'Τ',
             'name': 'ταυ',
             'segment': 'consonant',
             'subsegment': 'mute',
             'roman': 't',
             'value': 300}
# upsilon:http://en.wiktionary.org/wiki/upsilon
data[400] = {'greek': 'υ',
             'capital': 'ϒ', 'capital2': 'Y',
             'name': 'υ ψιλον',
             'segment': 'vowel',
             'subsegment': 'short',
             'roman': 'u',
             'value': 400}
# phi:http://en.wiktionary.org/wiki/phi
data[500] = {'greek': 'φ',
             'capital': 'Φ',
             'name': 'φει',
             'segment': 'consonant',
             'subsegment': 'mute',
             'roman': 'f',
             'value': 500}
# khi, chi:http://en.wiktionary.org/wiki/chi
data[600] = {'greek': 'χ',
             'capital': 'Χ',
             'name': 'χει',
             'segment': 'consonant',
             'subsegment': 'mute',
             'roman': 'x',
             'value': 600}
# psi:http://en.wiktionary.org/wiki/psi
data[700] = {'greek': 'ψ',
             'capital': 'Ψ',
             'name': 'ψει',
             'segment': 'consonant',
             'subsegment': 'double',
             'roman': 'y',
             'value': 700}
# omega:http://en.wiktionary.org/wiki/omega
data[800] = {'greek': 'ω',
             'capital': 'Ω',
             'name': 'ω μεγα',
             'segment': 'vowel',
             'subsegment': 'long',
             'roman': 'w',
             'value': 800}
# sampi/disigma
# http://en.wikipedia.org/wiki/Sampi
# http://www.tlg.uci.edu/~opoudjis/unicode/other_nonattic.html#sampi
# http://www.parthia.com/fonts/sampi.htm
# http://www.jstor.org/stable/636031
data[900] = {'greek': 'ϡ', 'small2': 'ͳ',
             'capital': 'Ϡ', 'capital2': 'Ͳ',
             'name': 'σαμπι', 'name2': 'δισιγμα',
             'segment': 'numeral',
             #'subsegment': '',
             'roman': '900',
             'value': 900}

greek_roman_values = {}
greek_roman_letters = {}
roman_greek_letters = {}

keys = ['roman', 'greek', 'capital', 'capital2', 'small2', 'small3', 'small4']
for num, d in data.items():
    for k in keys:
        if d.has_key(k):
            greek_roman_values[d[k]] = num
            if k == 'roman':
                greek_roman_letters[d[k]] = d['greek']
                greek_roman_letters[d[k].upper()] = d['capital']
                greek_roman_values[d[k].upper()] = num
            else:
                if d.has_key('roman'):
                    if k == 'capital' or k == 'capital2':
                        roman_greek_letters[d[k]] = d['roman'].upper()
                    else:
                        roman_greek_letters[d[k]] = d['roman']

greek_letters = ''
keys = ['greek', 'capital', 'capital2', 'small2', 'small3', 'small4']
for num, d in data.items():
    for k in keys:
        if d.has_key(k):
            #αΑβΒγΓδΔεΕϛϚϜϝζΖηΗθΘιΙυΥκΚϡϠͲͳλΛωΩμΜτΤνΝξΞοΟσΣϹϲςπΠχΧϙϘϞϟρΡψΨφΦ
            greek_letters += d[k]

regex_greek_roman_values = re.compile('|'.join(greek_roman_values.keys()))
regex_greek_to_roman_letters = re.compile('|'.join(roman_greek_letters.keys()))
regex_roman_to_greek_letters = re.compile('|'.join(greek_roman_letters.keys()))

def isopsephy(str):
    """
    Str is a roman letter representation (transliteration) of the greek word or sentence 
    that will be converted to the numerical value letter by letter
    """
    result = 0
    num_str = regex_greek_roman_values.sub(lambda x: '%s ' % greek_roman_values[x.group()], str)
    try:
        result = sum([int(i) for i in num_str.split()])
    except Exception as e:
        print str
    return result

def to_roman(word):
    """
    Create a roman letter version of the greek word.
    This will change all greek (primary), capital, capital2, small2, small3, and small4
    letters to roman letter. Capital letters are honored.
    """
    return regex_greek_to_roman_letters.sub(lambda x: roman_greek_letters[x.group()], word)

def to_greek(word):
    """
    Create a greek version of the roman letter word.
    This will change a-zA-Z except j, J, v & V to the corresponding greek letters
    Capital letters are honored.
    """
    return regex_roman_to_greek_letters.sub(lambda x: greek_roman_letters[x.group()], word)

names = {'name': 'name_value', 'name2': 'name_value2', 'name3': 'name_value3', 'name4': 'name_value4'}
for num, d in data.items():
    for k, v in names.items():
        if d.has_key(k):
            d[v] = isopsephy(d[k])

# accents / diacritics for simplified greek letters

_accents_ = {}

_accents_['Α'] = "Ἀ Ἄ Ἂ Ἆ ᾏ ᾈ ᾌ ᾊ ᾎ Ά Ἁ Ἅ Ἃ Ἇ Ὰ ᾼ ᾉ ᾍ ᾋ Ἀ"
_accents_['α'] = "ἀ ά ἄ ᾶ ᾳ ὰ ά ἀ ἁ ἂ ἃ ἄ ἅ ἆ ἇ ᾀ ᾁ ᾂ ᾃ ᾄ ᾅ ᾆ ᾇ ᾲ ᾳ ᾴ ᾶ ᾷ"

_accents_['E'] = "Έ Ἑ Ἕ Ἓ Ὲ Ἐ Ἔ Ἒ"
_accents_['ε'] = "έ ἔ ἐ ὲ έ ἐ ἑ ἒ ἓ ἔ ἕ"

_accents_['Η'] = " ᾚ ᾞ Ἠ Ἤ Ἢ Ἦ Ή Ἡ Ἥ Ἣ Ἧ Ὴ ῌ ᾙ ᾝ ᾛ ᾟ ᾘ ᾜ"
_accents_['η'] = "ή ἡ ῆ ἤ ἦ ὴ ῃ ὴ ή ᾐ ᾑ ᾒ ᾓ ᾔ ᾕ ᾖ ᾗ ῂ ῃ ῄ ῆ ῇ ἠ ἡ ἢ ἣ ἤ ἥ ἦ ἧ"

_accents_['Ι'] = "Ί Ἱ Ἵ Ἳ Ἷ Ὶ Ἰ Ἴ Ἲ Ἶ Ἱ"
_accents_['ι'] = "ἱ ἰ ἴ ί ῖ ἷ î ì ἶ ὶ ί ῒ ΐ ῖ ῗ ἰ ἱ ἲ ἳ ἴ ἵ ἶ ἷ ϊ"

_accents_['Ο'] = "Ό Ὁ Ὅ Ὃ Ὸ Ὀ Ὄ Ὂ"
_accents_['ο'] = "ὁ ò ó ô ὄ ὅ ὸ ό ὀ ὁ ὂ ὃ ὄ ὅ"

_accents_['Ρ'] = "Ῥ"
_accents_['ρ'] = "ῥ ῤ"

_accents_['ϒ'] = "Ύ Ὑ Ὕ Ὓ Ὗ Ὺ Ῡ"
_accents_['υ'] = "ῦ ύ ϋ ὐ ὕ ὖ ù ὑ ὺ ύ ὐ ὑ ὒ ὓ ὔ ὕ ὖ ὗ ῠ ῡ ῢ ΰ ῦ ῧ"

_accents_['Ω'] = "ᾪ ᾮ Ὠ Ὤ Ὢ Ὦ Ώ Ὡ Ὥ Ὣ Ὧ Ὼ ῼ ᾩ ᾭ ᾫ ᾯ ᾨ ᾬ"
_accents_['ω'] = "ὥ ῶ ὧ ώ ὠ ῳ ᾧ ὼ ώ ὠ ὡ ὢ ὣ ὤ ὥ ὦ ὧ ᾠ ᾡ ᾢ ᾣ ᾤ ᾥ ᾦ ᾧ ῲ ῳ ῴ ῶ ῷ"

accents = {}

for letter, values in _accents_.iteritems():
    for value in values.split():
        accents[value] = letter

regex_roman = re.compile(r'[^a-z069 ]+', re.IGNORECASE)
def preprocess_roman(str):
    # regex to remove all special characters leaving only a-z and empty scape
    # for example: a)a/atos tau1 -> aaatos tau
    return regex_roman.sub('', str)

regex_greek = re.compile('|'.join(accents.keys()))
def preprocess_greek(str):
    # handle diacritics
    return regex_greek.sub(lambda x: accents[x.group()], str)

# http://stackoverflow.com/questions/21380268/matching-the-sum-of-values-on-string
def list2string(alist):
    return " ".join(map(str, alist))

def string2list(s):
    return list(map(int, s.split()))

def find_number(a, total):
    u = 0
    y = 0 # the current sum of the interval (u .. v)
    res = []
    for v in range(0, len(a)):
        # at this point the interval sum y is smaller than the requested total,
        # so we move the right end of the interval forward
        y += a[v]
        while y >= total:
            if y == total:
                res.append(list2string(a[ u : v+1 ]))
            # if the current sum is too large, move the left end of the interval forward
            y -= a[u]
            u += 1
    return res

def search_by_num(text, num):
    return list2string(find_number(string2list(text), num))

def digital_root(num, modulo = 9):
    # similar to modulo, but 0 = 9 and 9 = 9
    val = num % modulo
    return val if val > 0 else modulo

def digital_sum(num):
    return sum(prepare_digital_operation(num))

def digital_product(num):
    return reduce(lambda x, y: x * y, prepare_digital_operation(num), 1)

def prepare_digital_operation(num):
    # strip off 0|,|. and return a list of single digit integers from original number
    return map(int, str(num).replace('0', '').replace('.', '').replace(',', ''))

def char_table(text, mod = 9, capitalize = None, html = False):
    data = dict([key, []] for key in ['letter', 'transliteration', 'isopsephy', 'digital_sum', 'word'])
    # split text to columns: #, letter, translit, num, mod, word
    if capitalize == True:
        text = to_roman(text).upper()
    elif capitalize == False:
        text = to_roman(text).lower()
    else:
        text = to_roman(text)
    for word in text.split(" "):
        for letter in word:
            data['letter'].append(to_greek(letter))
            data['transliteration'].append(letter)
            num = isopsephy(letter)
            data['isopsephy'].append(num)
            data['digital_sum'].append(digital_root(num))
            data['word'].append(word)
    if html:
        # create html table from result
        return ""
    else:
        return pd.DataFrame(data)

def digital_root_summary(df):
    df2 = df.groupby('word').sum()
    df2['digital_root'] = df2['digital_sum'].apply(digital_root)
    df2['digital_product'] = df2['isopsephy'].apply(digital_product)
    df2['digital_product_root'] = df2['digital_product'].apply(digital_root)
    return df2