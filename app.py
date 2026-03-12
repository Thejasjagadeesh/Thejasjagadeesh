from flask import Flask, render_template, request

app = Flask(__name__)

movies = [
    {
        "name": "Avengers",
        "location": "Mangalore",
        "price": 250,
        "image": "https://m.media-amazon.com/images/I/81ExhpBEbHL.jpg"
    },
    {
        "name": "Batman",
        "location": "Bangalore",
        "price": 220,
        "image": "https://m.media-amazon.com/images/I/71niXI3lxlL.jpg"
    },
    {
        "name": "Interstellar",
        "location": "Mumbai",
        "price": 300,
        "image": "https://m.media-amazon.com/images/I/91kFYg4fX3L.jpg"
    }
]
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/register")
def register():
    return render_template("register.html")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/movies")
def movie_list():
    return render_template("movies.html", movies=movies)

@app.route("/book/<movie>")
def book(movie):
    return render_template("book.html", movie=movie)

@app.route("/confirm", methods=["POST"])
def confirm():
    movie = request.form["movie"]
    seat = request.form["seat"]
    return render_template("confirmation.html", movie=movie, seat=seat)

if __name__ == "__main__":
    app.run(debug=True)