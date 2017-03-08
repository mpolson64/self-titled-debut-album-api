import requests
import random
import sys
import os

API_KEY = os.environ['WORDNIK_API_KEY']

def getRandomWord(partOfSpeech, apiKey):
    r = requests.get('http://api.wordnik.com:80/v4/words.json/randomWord?hasDictionaryDef=true&minCorpusCount=0&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&includePartOfSpeech=' + partOfSpeech + '&api_key=' + apiKey)
    return r.json()['word'].capitalize();

def thePluralNoun(apiKey):   #The Beatles
    return 'The ' + getRandomWord('noun-plural', apiKey);

def theAdjectiveNouns(apiKey):  #The Flaming Lips
    return 'The ' + getRandomWord('adjective', apiKey) + ' ' + getRandomWord('noun-plural', apiKey)

def theAdjective(apiKey):   #The National
    return 'The ' + getRandomWord('adjective', apiKey)

def pluralNounOfNoun(apiKey):    #Mates of State
    return getRandomWord('noun-plural', apiKey) + ' of ' + getRandomWord('noun', apiKey)

def properNounTheProfession(apiKey):     #Chance the Rapper
    profession = ''
    verb = getRandomWord('verb-transitive', apiKey)
    if(verb[len(verb) - 2] == 'e' and verb[len(verb) - 1] == 'r'):
        profession = verb
    elif(verb[len(verb) - 1] == 'e'):
        profession = verb + 'r'
    else:
        profession = verb + 'er'

    return getRandomWord('noun', apiKey) + ' the ' + profession

def nounNumber(apiKey):     #Blink-182
    return getRandomWord('noun', apiKey) + '-' + str(random.randint(100, 999))

def verbNumber(apiKey):     #Blink-182
    return getRandomWord('verb', apiKey) + '-' + str(random.randint(100, 999))

def adjectiveNoun(apiKey):  #Tame Impala
    return getRandomWord('adjective', apiKey) + ' ' + getRandomWord('noun', apiKey)

def adjectivePluralNoun(apiKey):
    return getRandomWord('adjective', apiKey) + ' ' + getRandomWord('noun-plural', apiKey)

def properNounLetterLetterLetter(apiKey):   #Charlie XCX
    letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
    return getRandomWord('proper-noun', apiKey) + ' ' + random.choice(letters) + random.choice(letters) + random.choice(letters)

def verbTheNoun(apiKey):    #Run the Jewels
    return getRandomWord('verb', apiKey) + ' the ' + getRandomWord('noun', apiKey)

def pluralNounDoubleLetter(apiKey):     #Desiigner
    pluralNoun = getRandomWord('noun-plural', apiKey)
    position = random.randint(0, len(pluralNoun) - 1)
    return pluralNoun[:position] + pluralNoun[position] + pluralNoun[position:]

ARCHETYPES = (thePluralNoun, theAdjectiveNouns, theAdjective, pluralNounOfNoun, properNounTheProfession, nounNumber, verbNumber, adjectiveNoun, adjectivePluralNoun, properNounLetterLetterLetter, verbTheNoun, pluralNounDoubleLetter)

if __name__ == '__main__':
    print(random.choice(ARCHETYPES)(API_KEY))
    sys.stdout.flush()
