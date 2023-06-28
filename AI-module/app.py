import os
from key_NOT_FOR_GITHUB import key
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = key


# Classifiers are the easiest models to get started with. 
# For classification problems we suggest using !____ada____!, which generally tends to perform only 
# very slightly worse than more capable models once fine-tuned, 
# whilst being significantly faster and cheaper.

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="davinci:ft-personal-2023-06-28-00-18-49",
            prompt=generate_prompt(),
            temperature=0.5,
            max_tokens=50,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    print(result)
    return render_template("index.html", result=result)


# def generate_prompt(animal):
#     return """Suggest three names for an animal that is a superhero.

# Animal: Cat
# Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
# Animal: Dog
# Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
# Animal: {}
# Names:""".format(
#         animal.capitalize()
#     )

# Animal: Cat
# Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
# Animal: Dog
# Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot, Muchos
# Animal: {}

def generate_prompt():
    return """Suggest one and only one color for an input:
Input: You are bad->
Color: Red###
Input: You are pretty->
Color: Pink###
Input: {}
"""

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)