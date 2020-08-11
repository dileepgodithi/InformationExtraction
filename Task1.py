import sys
import os
import nltk
import spacy

nltk.download('punkt')
nltk.download('wordnet')
spaci = spacy.load('en')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

def tokenize_sentence(sentences):
    for i in sentences:
        tokens=[]
        tokens=word_tokenize(i)
        print(tokens)

def lemmatize_sentence_nltk(sentences):
    lemmatizer = WordNetLemmatizer()
    for i in sentences:
        for word in word_tokenize(i):
            print(word,"-->",lemmatizer.lemmatize(word))

def lemmatize_sentence_spacy(sentences):
    for i in sentences:
        sentence_=spaci(i)
        for word in sentence_:
            print(word,"-->",word.lemma_)

def parts_of_speech_tag_spacy(sentences):
    for i in sentences:
        sentence_=spaci(i)
        for word in sentence_:
            print(word,"-->",word.pos_)

def dependency_parsing_features_spacy(sentences):
    for i in sentences:
        sentence_=spaci(i)
        for token in sentence_.noun_chunks:
            print(f'{token.text:.<{45}},{token.root.text:{10}},{token.root.dep_:{10}},{token.root.head.text:{10}},{token.root.head.pos_}')

def print_synset_relations(word):
    synset= wordnet.synsets(word)
    if len(synset)!=0:
        hypernymy=synset[0].hypernyms()
        if(len(hypernymy)!=0):
            print("Hypernyms of ",word)
            print(hypernymy)
        hyponymy=synset[0].hyponyms()
        if(len(hyponymy)!=0):
            print("Hyponyms of ",word)
            print(hyponymy)
        holonymy=synset[0].member_holonyms()
        if(len(holonymy)!=0):
            print("Holonyms of ",word)
            print(holonymy)
        meronymy=synset[0].member_meronyms()
        if(len(meronymy)!=0):
            print("meronyms of ",word)
            print(meronymy)


def NLP_features(sentences):
    print("Sentences")
    for sentence in sentences:
        print(sentence)
    print("tokens")
    tokenize_sentence(sentences)
    print("lemmas")
    lemmatize_sentence_spacy(sentences)
    print("parts of speech")
    parts_of_speech_tag_spacy(sentences)
    print("dependency_parsing_features")
    dependency_parsing_features_spacy(sentences)
    print("Synset Relations")
    for i in sentences:
        for word in word_tokenize(i):
            print_synset_relations(word)

if __name__ == '__main__':

    arg_list = sys.argv
    path =str(arg_list[1])
    sentences=[]
    with open(path,'r',encoding='utf-8-sig') as file:
              data=file.read()
              sentences=sent_tokenize(data)
    NLP_features(sentences)

    
