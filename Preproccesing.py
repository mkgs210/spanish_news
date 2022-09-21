import re
import string
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


def clean_text(text):
    """The function removes punctuation marks, stop words, links, words
     with numbers inside and converts the string to lowercase.
    Args:
        text: input string.
    Returns:
        string.
    """
    text = str(text).lower()
    text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('\w*\d\w*', '', text)

    emoji_pattern = re.compile(pattern="["
                                       u"\U0001F600-\U0001F64F"  # emoticons
                                       u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                       u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                       u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                       "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)

    stop_word = stopwords.words('spanish')

    wo_punc = [letter for letter in text if letter not in string.punctuation + str('“”—·…¡¡¡�¡⭕♦✔️◀🧵✍️«»')]
    wo_punc = ''.join(wo_punc)
    wo_stop_word = [word for word in wo_punc.split() if word not in stop_word]
    result = ' '.join(wo_stop_word)
    return result


def lemma_text(text):
    lemma = WordNetLemmatizer()
    lemma_text = [lemma.lemmatize(i) for i in word_tokenize(text)]
    result = ' '.join(lemma_text)
    return result