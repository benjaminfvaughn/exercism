'''Functions for creating, transforming, and adding prefixes to strings.'''


def add_prefix_un(word):
    '''Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    '''

    return f'un{word}'

def make_word_groups(vocab_words):
    '''Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    '''

    prefix = vocab_words.pop(0)
    word_groups = prefix

    for base_word in vocab_words:
        word_groups = word_groups + ' :: ' + prefix + base_word

    return word_groups

def remove_suffix_ness(word):
    '''Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: 'heaviness' becomes 'heavy', but 'sadness' becomes 'sad'.
    '''

    if word.endswith('ness'):
        base_word = word[:len(word)-4]

    if base_word.endswith('i'):
        base_word = base_word[:len(base_word)-1] + 'y'

    return base_word

def adjective_to_verb(sentence, index):
    '''Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ('It got dark as the sun set', 2) becomes 'darken'.
    '''

    import string

    sentence_list = sentence.translate(str.maketrans('', '', string.punctuation)).split()

    return sentence_list[index] + 'en'
