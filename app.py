from boggle import Boggle
from flask import Flask, session, render_template, flash, request, jsonify, redirect
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "supersecret"
debug = DebugToolbarExtension(app)

boggle_game = Boggle()


@app.route("/")
def homepage():

    board = boggle_game.make_board()
    session['board']= board
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)


    return render_template("board.html", board=board,
                           highscore=highscore,
                           nplays=nplays)

@app.route("/words_check")
def words_check():

    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})

@app.route("/score", methods=["POST"])
def score():
    score = request.json["score"]
    highscore = session.get("highscore",0)
    nplays = session.get("nplays", 0)

    session['nplays'] = nplays +1
    session['highscore'] = max(score, highscore)
    return jsonify(newhighscore=score > highscore)
