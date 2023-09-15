from flask import Flask, render_template, request, redirect, url_for
import pymongo
import pandas as pd
import numpy as np

app = Flask(__name__)
client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["MedLib"]

collection = db["books"]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

def search_book(book_name):
    book = collection.find_one({"book_name": book_name})
    return book

def insert(book_name, review, rating):
    book = search_book(book_name)
    if book:
        collection.update_one({"book_name": book_name}, {"$push": {"reviews": {"review": review, "rating": rating}}})
    else:
        collection.insert_one({"book_name": book_name, "reviews": [{"review": review, "rating": rating}]})

@app.route('/prediction', methods=['GET', 'POST'])
def form_submit():
    book_name = request.form.get("book_name", 1)
    review = request.form.get("review", 0)
    rating = request.form.get("rating", 0)
    
    return render_template('prediction.html',
                           book_name=book_name,
                           review=review,
                           rating=rating,
                           )













if __name__ == '__main__':
    app.run(debug=True)
