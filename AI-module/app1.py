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

dish_tags = "FlavorConnect\jsons\dish-tags-row-splitted.json"

dish_tags_query = f"""{dish_tags}"""

query = f"""Use the below tags on the food preferences to answer the subsequent question. If the answer cannot be found, write "I don't know."

Tags:
\"\"\"
{dish_tags_query}
\"\"\"

Question: I want to eat hummus"""

response = openai.ChatCompletion.create(
    messages=[
        {'role': 'system', 'content': 'You answer questions about the food preferences.'},
        {'role': 'user', 'content': query},
    ],
    model="ada:ft-personal-2023-06-28-23-38-01",
    temperature=0,
)

print(response['choices'][0]['message']['content'])