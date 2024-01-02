categories = {
    "question": ["how", "what", "who", "?", "when"],
    "emotion": ["mad", "furious", "happy", "sad", "frustrated", "devastated", "miserable", "anxious", "excited",
                "scared", "eh", "nervous", "like", "crush", "love", "cry"],
    "action": ["going", "take", "punch", "sleep", "run", "walk", "swim", "sport", "sports"]
}

def determineCategory(user_input):
    user_words = user_input.lower().split()
    category_scores = {category: 0 for category in categories}

    for word in user_words:
        for category, keywords in categories.items():
            if word in keywords:
                category_scores[category] += 1

    highest_scoring_category = max(category_scores, key=category_scores.get)
    return highest_scoring_category

