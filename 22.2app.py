from flask import Flask, render_template, request
from ProjPython.stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"


@app.route("/")
def question_prompt():
    prompts = story.prompts
    return render_template("prompt.html", prompts =prompts)

@app.route("/story")
def show_story():
    text = story.generate(request.args)
    return render_template("stories.html", text=text)
