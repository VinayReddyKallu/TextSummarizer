import nltk
import string
import math
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from string import punctuation

def text_summarizer(raw_docx):
    sents=sent_tokenize(raw_docx)
    if(len(sents)==0):
        s=""
        return s
    raw_text = raw_docx
    docx = raw_text
    stopwords1 = list(stopwords.words('english'))
    sents=sent_tokenize(raw_text)                   #tokenizes sentences
    tokens=word_tokenize(raw_text)                  #tokenizes words 
    # Build Word Frequency
    word_frequencies = {}  
    for word in tokens:  
        if word not in stopwords1:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
    maximum_frequncy = max(word_frequencies.values())
    for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    # Sentence Tokens
    sentence_list = [ sentence for sentence in sents ]
    # Calculate Sentence Score and Ranking
    print(sentence_list)
    l=len(sentence_list)
    print(l)
    sentence_scores = {}  
    for sent in sentence_list:
        sen_tokens=word_tokenize(sent)
        for sen_word in sen_tokens:
            if sen_word in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[sen_word]
                else:
                    sentence_scores[sent] += word_frequencies[sen_word]
    summary_sentences = sorted(sents, key=sentence_scores.get,reverse=True)
    x=0
    l=len(summary_sentences)
    if(l<=10):
        x=math.ceil((l*5)/10)
    elif(l<=20):
        x=math.ceil((l*50)/100)
    elif(l<=30):
        x=math.ceil((l*50)/100)
    else:
        x=math.ceil((l*5)/10)
    summary_sen=summary_sentences[0:x]
    sents2=['-1ab-1' for i in range(len(sents))]
    for i in range(len(summary_sen)):
        for j in range(len(sents)):
            if(sents[j]==summary_sen[i]):
                sents2[j]=summary_sen[i]
    sents2=[x for x in sents2 if x!='-1ab-1']                        
    final_sentences = [ w for w in sents2 ]
    summary = ' '.join(final_sentences)
    return(summary)
