import random

categories = {
    "question": ["how", "what", "who", "?", "when"],
    "emotion": ["mad", "furious", "happy", "sad", "frustrated", "devastated", "miserable", "anxious", "excited",
                "scared", "eh", "nervous", "like", "crush", "love", "cry"],
    "action": ["going", "take", "punch", "sleep", "run", "walk", "swim", "sport", "sports"]
}

simple_response = ["Yes", "Sorry to hear that", "Mhm", "That sounds interesting! Tell me more.", "Absolutely, I totally get that."]

def determineCategory(user_input):
    """
    Determines the category of a user's input based on predefined keywords.

    Parameters:
    user_input (str): The input provided by the user.

    Returns:
    str: The highest scoring category based on the user's input.
    """
    user_words = user_input.lower().split()
    category_scores = {category: 0 for category in categories}

    for word in user_words:
        for category, keywords in categories.items():
            if word in keywords:
                category_scores[category] += 1

    highest_scoring_category = max(category_scores, key=category_scores.get)
    return highest_scoring_category

def response(user_input):
    """
    Generates a response based on the user's input and the determined category.

    Parameters:
    user_input (str): The input provided by the user.
    """
    try:
        category = determineCategory(user_input)
        if category == "emotion":
            print("Why are you feeling that?")
        elif category == "action":
            print("What made you act that way?")
        elif category == "question":
            print("tell me more about it")
        else:
            print(random.choice(simple_response))
    except Exception as e:
        print(f"An error occurred: {e}")

