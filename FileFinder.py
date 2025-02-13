import glob


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def clenanup(text):
    queryLower = text.lower()
    
    query = word_tokenize(queryLower)
    english_stopwords = stopwords.words('english')
    tokens_wo_stopwords = [t for t in query if t not in english_stopwords]
    return tokens_wo_stopwords




def search(query, files):
    match = set()
    folder_path = 'data/*.txt'
    match = set()
    query_words = set(clenanup(query))
    files = glob.glob(folder_path)
    for file in files:
        with open(file, 'r') as f:
            content = f.read()            
            if any(word in content for word in query_words):
                match.add(file)
    matchs = list(set(match))
    return matchs if matchs else None
