from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
    
        #fetch the form data; put it into the template; send it back to the user
        properNoun1 = details["properNoun1"]
        properNoun2 = details["properNoun2"]
        noun1 = details["noun1"]
        noun2 = details["noun2"]
        noun3 = details["noun3"]
        verb1 = details["verb1"]
        verb2 = details["verb2"]
        verbPresent1 = details["verbPresent1"]
        verbPresent2 = details["verbPresent2"]
        adjective1 = details["adjective1"]
        adjective2 = details["adjective2"]
        adjective3 = details["adjective3"]
        adverb1 = details["adverb1"]
        adverb2 = details["adverb2"]

        intro= f"""
        Once day {properNoun1} was walking down the street when {properNoun2} came up to them.
        {properNoun1} saw that {properNoun2} was behaving {adverb1} and asked them what was going on.
        {properNoun2} said that they were {verbPresent1} {properNoun1} because they were a(n) {adjective1} {noun2}.
        """
        script_section = f"""
        {properNoun1}: "What are you doing now?"
        {properNoun2}: "I'm {verbPresent1} at you!"
        {properNoun1}: "Why?"
        {properNoun2}: "Because I'm a {adjective1} {noun2}!"
        {properNoun1}: "Oh, okay."
        {properNoun2}: "I'm {verbPresent2} at you again!"
        {properNoun1}: "Why?"
        {properNoun2}: "Because I'm a {adjective2} {noun2}!"
        {properNoun1}: "Would you stop that?"
        {properNoun2}: "What else would I do?"
        {properNoun1}: "I don't know, maybe {verb1}?"
        {properNoun2}: "No, but I will {verb2} at you!"
        {properNoun1}: "Why?"
        {properNoun2}: "Because I'm {adverb2} a(n) {adjective2} {noun1}!"
        {properNoun1}: "I'm going home."
        """
        outro = f"""
        As {properNoun1} walked away, {properNoun2} said to themself, "And that, my friend, is how you make a(n) {adjective3} {noun3} leave you alone!"
        """
        return render_template('story.html', intro=intro, script_section=script_section, outro=outro)
    return render_template('input.html')
if __name__ == "__main__":
    app.run(debug=True)

