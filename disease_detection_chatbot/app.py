from flask import Flask, render_template, request
import aiml
import os

app = Flask(__name__)

kernel = aiml.Kernel()

# Load or train brain
if os.path.exists("bot_brain.brn"):
    kernel.bootstrap(learnFiles="aiml_files/std-startup.aiml", commands="LOAD AIML B")
    kernel.saveBrain("bot_brain.brn")  # Optional: re-save brain after learning

else:
    kernel.bootstrap(learnFiles="chatbot/std-startup.aiml", commands="LOAD AIML B")
    kernel.saveBrain("bot_brain.brn")

@app.route("/", methods=["GET", "POST"])
def home():
    user_input = ""
    bot_response = ""
    if request.method == "POST":
        user_input = request.form["messageText"]
        bot_response = kernel.respond(user_input.upper())
    return render_template("index.html", user_input=user_input, bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)
