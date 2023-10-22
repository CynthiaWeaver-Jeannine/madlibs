def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input

properNoun1 = get_input("proper noun (name)")
properNoun2 = get_input("proper noun (name)")
noun1 = get_input("noun")
noun2 = get_input("noun")
noun3 = get_input("noun")
verb1 = get_input("verb")
verb2 = get_input("verb")
verbPresent1 = get_input("verb (present tense)")
verbPresent2 = get_input("verb (present tense)")
adjective1 = get_input("adjective")
adjective2 = get_input("adjective")
adjective3 = get_input("adjective")
adverb1 = get_input("adverb")
adverb2 = get_input("adverb")

story = f"""
Once day {properNoun1} was walking down the street when {properNoun2} came up to them.
{properNoun1} saw that {properNoun2} was behaving {adverb1} and asked them what was wrong.
{properNoun2} said that they were {verbPresent1} {properNoun1} because they were a {adjective1} {noun2}.

{properNoun1}: "What are you doing now?"
{properNoun2}: "I'm {verbPresent1} you!"
{properNoun1}: "Why?"
{properNoun2}: "Because I'm a {adjective1} {noun2}!"
{properNoun1}: "Oh, okay."
{properNoun2}: "I'm {verbPresent2} you again!"
{properNoun1}: "Why?"
{properNoun2}: "Because I'm a {adjective2} {noun2}!"
{properNoun1}: "Would you stop that?"
{properNoun2}: "What else would I do?"
{properNoun1}: "I don't know, maybe {verb1}?"
{properNoun2}: "No, but I will {verb2} you!"
{properNoun1}: "Why?"
{properNoun2}: "Because I'm a {adjective2} {noun2}!"
{properNoun1}: "I'm going home."

As {properNoun1} walked away, {properNoun2} said to themself, "And that, my friend, is how to get rid of a {adjective3} {noun3}!"

"""
print(story)