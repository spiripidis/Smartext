import tkinter as tk
import pickle
from tkinter import simpledialog
import nltk
from nltk.tokenize import word_tokenize
import re, string, random
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


def run_this():
    txt2analyze = ""

    sentimentWND = tk.Toplevel()
    f = open('classifier.pickle', 'rb')
    classifier = pickle.load(f)
    f.close()

    sentimentWND.title("Sentiment Analysis")

    main_canvas = tk.Canvas(sentimentWND, width=400, height=300, relief='raised')
    main_canvas.pack()

    label1 = tk.Label(main_canvas, text='Sentiment Analysis')
    label1.config(font=('helvetica', 14))
    label1.pack()
    main_canvas.create_window(200, 25, window=label1)

    def remove_noise(tweet_tokens, stop_words=()):
        cleaned_tokens = []
        for token, tag in pos_tag(tweet_tokens):
            token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|' \
                           '(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', token)
            token = re.sub("(@[A-Za-z0-9_]+)", "", token)
            if tag.startswith("NN"):
                pos = 'n'
            elif tag.startswith('VB'):
                pos = 'v'
            else:
                pos = 'a'
            lemmatizer = WordNetLemmatizer()
            token = lemmatizer.lemmatize(token, pos)
            if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
                cleaned_tokens.append(token.lower())
        return cleaned_tokens

    def update_text(some=txt2analyze):
        return some

    def getSentiment():

        custom_tweet = simpledialog.askstring("Text for Sentiment Analysis", "Enter Your Text: ", parent=sentimentWND)
        custom_tokens = remove_noise(word_tokenize(custom_tweet))
        label3 = tk.Label(sentimentWND)
        label3.config(font=('helvetica', 14))
        label3.pack()
        main_canvas.create_window(200, 160, window=label3)
        label3.configure(text="Result: " + classifier.classify(dict([token, True] for token in custom_tokens)))

    button1 = tk.Button(sentimentWND, text='Enter new text', command=getSentiment, bg='brown',
                        fg='white',
                        font=('helvetica', 9, 'bold'))
    button1.pack()
    main_canvas.create_window(200, 200, window=button1)

    # sentimentWND.mainloop()
