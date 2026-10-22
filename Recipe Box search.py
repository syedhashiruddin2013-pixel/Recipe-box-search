import math

RECIPES = [
    ("Pancakes", "mix flour eggs and milk then fry the batter in a pan"),
    ("Tomato Soup", "cook tomatoes with onion and salt then blend the soup"),
    ("Fruit Salad", "chop apple banana and mango and mix the fruit in a bowl"),
    ("Omelette", "beat eggs with salt and cook the eggs in a pan"),
    ("Cookies", "mix flour butter and sugar then bake the cookies"),
]

TEST_SEARCHES = [
    ("fry the batter", "Pancakes"),
    ("blend the soup", "Tomato Soup"),
    ("mango and apple", "Fruit Salad"),
    ("eggs in a pan", "Omelette"),
    ("butter and sugar", "Cookies"),
    ("cookie", "Cookies"),
]
def build_index(recipes):
    index = {}
    for(number, (title, text)) in enumerate(recipes):
        for word in text.split():
            if word not in index:
                index[word] = {}
            if number not in index[word]:
                index[word][number] = 0
            index[word][number] += 1
    return index

INDEX = build_index(RECIPES)
print("PART 1: Index")
print(INDEX.get("eggs"), INDEX.get("pizza", "not found"))

def score(query):
    scores = {}
    for word in query.split():
        for number, count in INDEX.get(word, {}).items():
            recipe_text = RECIPES[number][1]
            num_words = len(recipe_text.split())
            if number not in scores:
                scores[number] = 0
            scores[number] += count / num_words
    return scores

print("\nPART 2: Score")
print(round(score("eggs in a pan").get(3, 0), 2))

def best_recipe(query):

    scores = score(query)
    if not scores:
        return "no match"
    best_number = max(scores, key=scores.get)
    return RECIPES[best_number][0]

print("\nPART 3: Best recipe")
print(best_recipe("fry the batter"), "|", best_recipe("pizza"))
print("\nPART 4: Test all searches")
mistakes = 0
for query, wanted in TEST_SEARCHES:
    answer = best_recipe(query)
    if answer != wanted:
        mistakes += 1
    print(f"Query: {query} | Answer: {answer} | Wanted: {wanted}")

print(f"\nMistakes: {mistakes} out of {len(TEST_SEARCHES)}")
