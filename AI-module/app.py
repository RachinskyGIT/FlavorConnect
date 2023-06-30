import os
from key_NOT_FOR_GITHUB import key
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = key


@app.route("/", methods=("GET", "POST"))
def index():

    dish_tags = "FlavorConnect\jsons\dish-tags-row-splitted.json"
    dish_tags_query = f"""{dish_tags}"""
    query = f"""Use the below tags on the food preferences to answer the subsequent question. If the answer cannot be found, write "I don't know."

    Tags:
    \"\"\"
    {dish_tags_query}
    \"\"\"

    Question: I want to eat hummus"""

    if request.method == "POST":
        response = openai.ChatCompletion.create(
            messages=[
            {'role': 'system', 'content': 'You answer questions about the food preferences.'},
            {'role': 'user', 'content': query},
            ],
            model="gpt-3.5-turbo",
            temperature=0.5,
            max_tokens=50,
        )
        print(response['choices'][0]['message']['content'])
        return redirect(url_for("index", result=response))

    result = request.args.get("result")
    print(result)

    return render_template("index.html", result=result)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

