import json

'''
CREATING A BASIC CORPUS OF ALL WORDS MENTIONED IN 
CHAPTER 1 AND 2, AND SAVING AS JSON FILE
'''

with open("data\hp.txt", "r") as f:
    hp = f.read()
    
#hp = hp.split("\n\n")[3:]
#print (str(hp))
#print (hp[0])

chapters = hp.split("CHAPTER")
print (len(chapters))


# PARSING THROUGH EACH CHAPTER OF BOOK 1
corpus = []
for chap in range(len(chapters)-1):
    chapter_with_title = hp.split("CHAPTER")[chap+1:chap+2]
    chapter = chapter_with_title[0].split("\n\n")[2:]

    # Adding each chapter's words
    i = 1
    # Spliting each chapter in paragraphs
    for para in chapter:
        # Spliting each paragraph into sentences
        sentences = para.split("\n")
        word_list = []
        for sentence in sentences:
            # Spliting each sentence in to words
            words = sentence.split(" ")
            for word in words:
                # Refining each word (by removing extra characters)
                word = word.replace("\n", "").replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "").replace("'", "").replace("\"", "").replace("-", "").replace("--", "")
                if word != "":
                    word_list.append(word)
        corpus.append(word_list)
        i += 1
    
#print (corpus)

with open("basic_corpus.json", "w") as f:
    json.dump(corpus, f)

    
'''
DELETING STOPWORDS FROM BASIC CORPUS
'''

with open("basic_corpus.json", "r", encoding='utf-8') as f:
    basic_corpus = json.load(f)
with open("data\stopwords.json", "r", encoding='utf-8') as f:
    stopwords = json.load(f)

print (stopwords)

final_refined_corpus = []
for i in range(len(basic_corpus)):
    refined_corpus = []
    for j in range(len(basic_corpus[i])):
        if basic_corpus[i][j] not in stopwords:
            refined_corpus.append(basic_corpus[i][j])
    
    final_refined_corpus.append(refined_corpus)

#print (final_refined_corpus)

with open("refined_corpus.json", "w") as f:
    json.dump(final_refined_corpus, f)
