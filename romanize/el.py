#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: el.py

import re
from collections import OrderedDict
from romanizer import Romanizer

data = OrderedDict()

"""

Data mapping between roman and greek letters and their linguistic components

Resources:

- http://en.wikipedia.org/wiki/Greek_alphabet
- http://www.chlt.org/FirstGreekBook/JWW_FGB1.html
- http://www.webtopos.gr/eng/languages/greek/alphabet/alpha.htm
- http://www.class.uh.edu/mcl/faculty/pozzi/grnl1/intr/0.2.1.pract.vow.htm
- http://en.wikipedia.org/wiki/Romanization_of_Greek
- http://en.citizendium.org/wiki/greek_alphabet

Segments:
- vowel
- consonant
- numeral (only)

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

Seven vowels: α ε η ι ο υ ω (a e ê i o u ô)

Numerals only: ϛ ϙ ϡ (6, 90, 900 or w, q, j)

"""

# letters from α to θ (1 to 9)
# alpha:http://en.wiktionary.org/wiki/ἄλφα
data['alpha'] = dict(letter=[u'α'], name=u'αλφα', segment='vowel', subsegment='short', roman=u'a', order=1)
# beta:http://en.wiktionary.org/wiki/βῆτα
data['beta'] = dict(letter=[u'β'], name=u'βητα', segment='consonant', subsegment='mute', roman=u'b', order=2)
# gamma:http://en.wiktionary.org/wiki/γάμμα
data['gamma'] = dict(letter=[u'γ'], name=u'γαμμα', segment='consonant', subsegment='mute', roman=u'g', order=3)
# delta:http://en.wiktionary.org/wiki/δέλτα
data['delta'] = dict(letter=[u'δ'], name=u'δελτα', segment='consonant', subsegment='mute', roman=u'd', order=4)
# epsilon:http://en.wiktionary.org/wiki/epsilon
data['epsilon'] = dict(letter=[u'ε'], name=u'ε ψιλον', segment='vowel', subsegment='short', roman=u'e', order=5)
# digamma/stigma/episemon/wau
# http://en.wikipedia.org/wiki/Digamma
data['digamma'] = dict(letter=[u'ϝ', u'ϛ'], name=u'διγαμμα', segment='numeral', subsegment='', roman=u'w', order=6)
#data['stigma'] = dict(letter=[u'ϛ'], name=u'στιγμα', segment='numeral', roman=u'w')
# zeta:http://en.wiktionary.org/wiki/ζῆτα
data['zeta'] = dict(letter=[u'ζ'], name=u'ζητα', segment='consonant', subsegment='double', roman=u'z', order=7)
# eta:http://en.wiktionary.org/wiki/ἦτα
data['eta'] = dict(letter=[u'η'], name=u'ητα', segment='vowel', subsegment='long', roman=u'ê', order=8)
# theta:http://en.wiktionary.org/wiki/θῆτα
data['theta'] = dict(letter=[u'θ'], name=u'θητα', segment='consonant', subsegment='mute', roman=u'h', order=9)

# letters from ι to ϙ (10 to 90)
# iota:http://en.wiktionary.org/wiki/ἰῶτα
data['iota'] = dict(letter=[u'ι'], name=u'ιωτα', segment='vowel', subsegment='short', roman=u'i', order=10)
# kappa:http://en.wiktionary.org/wiki/κάππα
data['kappa'] = dict(letter=[u'κ'], name=u'καππα', segment='consonant', subsegment='mute', roman=u'k', order=11)
# lambda:http://en.wiktionary.org/wiki/λάμβδα
data['lambda'] = dict(letter=[u'λ'], name=u'λαμβδα', segment='consonant', subsegment='semivowel', roman=u'l', order=12)
# mu:http://en.wiktionary.org/wiki/mu
data['mu'] = dict(letter=[u'μ'], name=u'μυ', segment='consonant', subsegment='semivowel', roman=u'm', order=13)
# nu:http://en.wiktionary.org/wiki/νῦ
data['nu'] = dict(letter=[u'ν'], name=u'νυ', segment='consonant', subsegment='semivowel', roman=u'n', order=14)
# xi:http://en.wiktionary.org/wiki/ξεῖ
data['xi'] = dict(letter=[u'ξ'], name=u'ξει', segment='consonant', subsegment='double', roman=u'c', order=15)
# omicron:http://en.wiktionary.org/wiki/omicron
data['omicron'] = dict(letter=[u'ο'], name=u'ο μικρον', segment='vowel', subsegment='short', roman=u'o', order=16)
# pi:http://en.wiktionary.org/wiki/πεῖ
data['pi'] = dict(letter=[u'π'], name=u'πει', segment='consonant', subsegment='mute', roman=u'p', order=17)
# koppa:http://en.wikipedia.org/wiki/Koppa_(letter)
# http://www.webtopos.gr/eng/languages/greek/alphabet/earlyletters.htm
data['qoppa'] = dict(letter=[u'ϙ', u'ϟ'], name=u'κοππα', segment='numeral', subsegment='', roman=u'q', order=18)

# letters from ρ to ϡ (100 to 900)
# rho:http://en.wiktionary.org/wiki/ῥῶ
data['rho'] = dict(letter=[u'ρ'], name=u'ρω', segment='consonant', subsegment='semivowel', roman=u'r', order=19)
# sigma:http://en.wiktionary.org/wiki/σίγμα
data['sigma'] = dict(letter=[u'σ', u'ϲ', u'ς'], name=u'σιγμα', segment='consonant', subsegment='semivowel', roman=u's', order=20)
#data['san'] = dict(letter=[u'ϻ'], name=u'σαν', segment='consonant', subsegment='semivowel', roman=u's')
# tau:http://en.wiktionary.org/wiki/tau
data['tau'] = dict(letter=[u'τ'], name=u'ταυ', segment='consonant', subsegment='mute', roman=u't', order=21)
# upsilon:http://en.wiktionary.org/wiki/upsilon
data['upsilon'] = dict(letter=[u'υ', u'ϒ'], name=u'υ ψιλον', segment='vowel', subsegment='short', roman=u'u', order=22)
# phi:http://en.wiktionary.org/wiki/phi
data['phi'] = dict(letter=[u'φ'], name=u'φει', segment='consonant', subsegment='mute', roman=u'f', order=23)
# khi, chi:http://en.wiktionary.org/wiki/chi
data['chi'] = dict(letter=[u'χ'], name=u'χει', segment='consonant', subsegment='mute', roman=u'x', order=24)
# psi:http://en.wiktionary.org/wiki/psi
data['psi'] = dict(letter=[u'ψ'], name=u'ψει', segment='consonant', subsegment='double', roman=u'y', order=25)
# omega:http://en.wiktionary.org/wiki/omega
data['omega'] = dict(letter=[u'ω'], name=u'ω μεγα', segment='vowel', subsegment='long', roman=u'ô', order=26)
# sampi/disigma
# http://en.wikipedia.org/wiki/Sampi
# http://www.tlg.uci.edu/~opoudjis/unicode/other_nonattic.html#sampi
# http://www.parthia.com/fonts/sampi.htm
# http://www.jstor.org/stable/636031
data['sampi'] = dict(letter=[u'ϡ', u'ͳ'], name=u'σαμπι', segment='numeral', subsegment='', roman=u'j', order=27)
#data['disigma'] = dict(letter=[u'ϡ'], name=u'δισιγμα', segment='numeral', subsegment='', roman=u'j')

r = Romanizer(data)

# accents / diacritics for simplified greek letters

_accents_ = {}

_accents_[u'Α'] = u"Ἀ Ἄ Ἂ Ἆ ᾏ ᾈ ᾌ ᾊ ᾎ Ά Ἁ Ἅ Ἃ Ἇ Ὰ ᾼ ᾉ ᾍ ᾋ Ἀ"
_accents_[u'α'] = u"ἀ ά ἄ ᾶ ᾳ ὰ ά ἀ ἁ ἂ ἃ ἄ ἅ ἆ ἇ ᾀ ᾁ ᾂ ᾃ ᾄ ᾅ ᾆ ᾇ ᾲ ᾳ ᾴ ᾶ ᾷ"

_accents_[u'Ε'] = u"Έ Ἑ Ἕ Ἓ Ὲ Ἐ Ἔ Ἒ"
_accents_[u'ε'] = u"έ ἔ ἐ ὲ έ ἐ ἑ ἒ ἓ ἔ ἕ"

_accents_[u'Η'] = u" ᾚ ᾞ Ἠ Ἤ Ἢ Ἦ Ή Ἡ Ἥ Ἣ Ἧ Ὴ ῌ ᾙ ᾝ ᾛ ᾟ ᾘ ᾜ"
_accents_[u'η'] = u"ή ἡ ῆ ἤ ἦ ὴ ῃ ὴ ή ᾐ ᾑ ᾒ ᾓ ᾔ ᾕ ᾖ ᾗ ῂ ῃ ῄ ῆ ῇ ἠ ἡ ἢ ἣ ἤ ἥ ἦ ἧ"

_accents_[u'Ι'] = u"Ί Ἱ Ἵ Ἳ Ἷ Ὶ Ἰ Ἴ Ἲ Ἶ Ἱ"
_accents_[u'ι'] = u"ἱ ἰ ἴ ί ῖ ἷ î ì ἶ ὶ ί ῒ ΐ ῖ ῗ ἰ ἱ ἲ ἳ ἴ ἵ ἶ ἷ ϊ"

_accents_[u'Ο'] = u"Ό Ὁ Ὅ Ὃ Ὸ Ὀ Ὄ Ὂ"
_accents_[u'ο'] = u"ὁ ò ó ὄ ὅ ὸ ό ὀ ὁ ὂ ὃ ὄ ὅ" # ô is excluded from this list!

_accents_[u'Ρ'] = u"Ῥ"
_accents_[u'ρ'] = u"ῥ ῤ"

_accents_[u'ϒ'] = u"Ύ Ὑ Ὕ Ὓ Ὗ Ὺ Ῡ"
_accents_[u'υ'] = u"ῦ ύ ϋ ὐ ὕ ὖ ù ὑ ὺ ύ ὐ ὑ ὒ ὓ ὔ ὕ ὖ ὗ ῠ ῡ ῢ ΰ ῦ ῧ"

_accents_[u'Ω'] = u"ᾪ ᾮ Ὠ Ὤ Ὢ Ὦ Ώ Ὡ Ὥ Ὣ Ὧ Ὼ ῼ ᾩ ᾭ ᾫ ᾯ ᾨ ᾬ"
_accents_[u'ω'] = u"ὥ ῶ ὧ ώ ὠ ῳ ᾧ ὼ ώ ὠ ὡ ὢ ὣ ὤ ὥ ὦ ὧ ᾠ ᾡ ᾢ ᾣ ᾤ ᾥ ᾦ ᾧ ῲ ῳ ῴ ῶ ῷ"

accents = {}

for letter, values in _accents_.iteritems():
    for value in values.split():
        accents[value] = letter

regex1 = re.compile('|'.join(accents.keys()))
# collect greek and roman letters from data dictionary
letters = ''.join([''.join(d['letter'])+\
          ''.join(d['letter']).upper()+\
          d['roman']+\
          d['roman'].upper() for key, d in data.items()])
regex2 = re.compile('[^%s ]+' % letters)

def preprocess(string):
    """
    Preprocess string to transform all diacritics and remove other special characters than appropriate
    :param string:
    :return:
    """
    string = unicode(string, encoding="utf-8")
    # convert diacritics to simpler forms
    string = regex1.sub(lambda x: accents[x.group()], string)
    # remove all rest of the unwanted characters
    return regex2.sub('', string).encode('utf-8')

def convert(string, sanitize=False):
    """
    Swap characters from script to roman and vice versa. Optionally sanitize string by using preprocess function.

    :param sanitize:
    :param string:
    :return:
    """
    return r.convert(string, (preprocess if sanitize else False))
