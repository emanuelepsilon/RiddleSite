from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def riddle():
    message = None
    correct_name = "mohammad nakhjavani"
    if request.method == "POST":
        user_name = request.form.get("name", "").strip().lower()
        if user_name == correct_name:
            message = "🎉 Correct! You solved the riddle.<br>Go to <a href='https://emanuelsengineeringarchive.onrender.com/' target='_blank'>Emanuel's Engineering Archive</a><br>Wait a minute or two for the site to start up!"
        else:
            message = "❌ Oops! Try again or ask Emanuel for a hint! 🤓"
    return render_template("riddle.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
