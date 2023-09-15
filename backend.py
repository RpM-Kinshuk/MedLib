from flask import Flask, render_template, request, redirect, url_for
import pymongo
import pandas as pd
import numpy as np
from modules.mailing import *
from modules.summary import nltk_summarizer
import pandas as pd
import numpy as np

app = Flask(__name__)
client = pymongo.MongoClient("mongodb://localhost:27017/")

OTP = 0
db = client["MedLib"]
logged_in = False
collection = db["books"]
em_collect = db["pwds"]


@app.route("/")
def index():
    return render_template("layout.html")


def add_pwd(email, pwd):
    em = em_collect.find({"email": email})
    if em:
        em_collect.update_one({"email": email}, {"$set": {"pwd": pwd}})
    else:
        em_collect.insert_one({"email": email, "pwd": pwd})


def check_pwd(email,pwd):
    em = em_collect.find({"email": email})
    global logged_in
    if em:
        
            logged_in=True
            return render_template("form.html")
        else:
            logged_in=False
            return False
    else:
        logged_in=False
        return False

@app.route('/enter_otp', methods=['GET', 'POST'])
def send_mail(email):
    global OTP 
    OTP = np.random.randint(100000, 999999)
    add_pwd(email, OTP)
    rnf_mail_alt(email=email, OTP=OTP)
    return render_template('otp.html', email=email)

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/otp", methods=["GET", "POST"])
def otp():
    email = request.form.get("email")
    send_mail(email)
    if otp == OTP:
        return render_template("form.html")
    else:
        return render_template("OTP.html", email=email)


@app.route("/login")
def login():
    return render_template("login.html")


def search_book(book_name):
    book = collection.find_one({"book_name": book_name})
    return book


def insert_review(book_name, review, rating):
    book = search_book(book_name)
    if book:
        collection.update_one(
            {"book_name": book_name},
            {"$push": {"reviews": {"review": review, "rating": rating}}},
        )
    else:
        collection.insert_one(
            {"book_name": book_name, "reviews": [{"review": review, "rating": rating}]}
        )

def summerize_category(review, statements):
    summary_text = nltk_summarizer(review, statements)
    print(summary_text)
    return summary_text


@app.route("/form_submit", methods=["GET", "POST"])
def form_submit():
    book_name = request.form.get("book_name", 1)
    review = request.form.get("review", 0)
    rating = request.form.get("rating", 0)

    insert_review(book_name, review, rating)
    return render_template(
        "Check.html",
        book_name=book_name,
        review=review,
        rating=rating,
        summary = summerize_category(review, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)
