import aiml
import os

kernel = aiml.Kernel()

def load_bot():
    if os.path.exists("bot_brain.brn"):
       kernel.bootstrap(learnFiles="aiml_files/std-startup.aiml", commands="LOAD AIML B")
       kernel.saveBrain("bot_brain.brn")  # Optional: re-save brain after learning

    else:
        kernel.bootstrap(learnFiles="chatbot/std-startup.aiml", commands="LOAD AIML B")
        kernel.saveBrain("bot_brain.brn")

def get_response(message):
    return kernel.respond(message.upper())
