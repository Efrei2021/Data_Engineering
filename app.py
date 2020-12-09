from flask import Flask, request, render_template

import ast
import pandas as pd
import re
import string

import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import numpy as np

import os
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from joblib import load

MODEL_DIR = os.environ["MODEL_DIR"]
MODEL_FILE = os.environ["MODEL_FILE"]
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILE)

app = Flask(__name__)
model = load(MODEL_PATH)


def tranform(sen):
	sen = sen.values
	finalString = ' '.join(map(str, sen))
	elt = ast.literal_eval(finalString)
	finalelt = ' '.join(map(str, elt))
	return finalelt
     
@app.route('/')
def home():   
    return render_template('index.html')
    
@app.route('/', methods=['POST'])
def predict():
	tweet = pd.read_csv("tagged_data.csv")
	
	words = []
	tags = []
	
	for elt in tweet['words']:
	    elt = ast.literal_eval(elt)
	    words.append(elt)
	    
	for elt in tweet['tags']:
	    elt = ast.literal_eval(elt)
	    tags.append(elt[0])
	    
	    
	tweet['words'] = words
	tweet['tags'] = tags
	
	output = []
	
	if request.method == 'POST':
	    enter = request.form['search']
	    test_doc = word_tokenize(enter.lower())
	    test_doc_vector = model.infer_vector(test_doc)
	    similar_doc=model.docvecs.most_similar(positive = [test_doc_vector], topn=20)
	    
	    for i in range(0,len(similar_doc)):
	        sen = tweet['words'][tweet['tags'] == similar_doc[i][0]]
	        finalString = tranform(sen)
	        output.append(finalString.capitalize())
    		
    	
	return render_template('result.html', tweets=output)
    
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
    
    

