'''
Info: The fisrt chapter is the introduction of analyzing the text.
Created by Lishucheng on 2018.3.21.

'''

# import the text
from nltk.book import *

# search words in the text
text1.concordance("monstrous")

text1.similar("monstrous")

# the analyze of frequence of words
def lexical_diversity(text):
    return len(text) / len(set(text))

def percentage(count, total):
    return 100 * count/total

lexical_diversity(text1)
percentage(text1.count('a'), len(text4))

fdist1 = FreqDist(text1)