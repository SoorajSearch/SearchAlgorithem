from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def clenanup(text):
    queryLower = text.lower()
    
    query = word_tokenize(queryLower)
    english_stopwords = stopwords.words('english')
    tokens_wo_stopwords = [t for t in query if t not in english_stopwords]
    return tokens_wo_stopwords

def searchAlgorithem(query, content):
    query_words = set(clenanup(query))
              
    if any(word in content for word in query_words):
        return True
    return False
