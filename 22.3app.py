from flask import Flask, render_template, request, flash, session, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app= Flask(__name__)

responses_list = "responses"

app.debug = True
app.config['SECRET_KEY'] = "super-secret"
toolbar = DebugToolbarExtension(app)

@app.rounte("/")
def survey_start():
    return render_template("survey_start.html", survey=survey)


@app.route("/begin", methods=["POST"])
def start_survey():
    """Clear the session of responses."""

    session[responses_list] = []

    return redirect("/questions/0")


@app.route("/answer", methods=["POST"])
def handle_question():
    """Save response and redirect to next question."""

    choice = request.form['answer']

    responses = session[responses_list]
    responses.append(choice)
    session[responses_list] = responses

    if (len(responses) == len(survey.questions)):
     
        return redirect("/complete")

    else:
        return redirect(f"/questions/{len(responses)}")



@app.rounte("/questions/<int:qid>")
def user_question(qid):
    responses = session.get(responses_list)

    if(responses is None):
        return redirect("/")
    if (len(responses) == len(survey.questions)):
        return redirect("/complete")
    
    if (len(responses) != qid):
        flash(f"Invalid question id: {qid}.")
        return redirect(f"/questions/{len(responses)}")
    
    question = survey.questions[qid]
    return render_template("question.html", question_num=qid, question=question)


@app.route("/complete")
def complete():
    return render_template("complete.html")
