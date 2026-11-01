"""Suggest simple Indian dishes from ingredients you already have."""


recipes = [
    {
        "name": "Aloo Jeera",
        "region": "North India",
        "ingredients": {"potato", "cumin", "oil", "salt"},
        "steps": [
            "Boil and cube the potatoes.",
            "Heat oil and add cumin seeds.",
            "Add potatoes and salt, then cook until lightly crisp.",
        ],
    },
    {
        "name": "Poha",
        "region": "Madhya Pradesh and Maharashtra",
        "ingredients": {"poha", "onion", "peanuts", "turmeric", "oil", "salt"},
        "steps": [
            "Rinse the poha briefly and let it drain.",
            "Cook onion and peanuts in a little oil.",
            "Stir in turmeric, poha, and salt; cook for a few minutes.",
        ],
    },
    {
        "name": "Tomato Rice",
        "region": "South India",
        "ingredients": {"rice", "tomato", "onion", "oil", "salt"},
        "steps": [
            "Cook the rice and set it aside.",
            "Cook chopped onion and tomato in a little oil until soft.",
            "Mix in the rice and salt, then heat through.",
        ],
    },
    {
        "name": "Egg Bhurji",
        "region": "Popular across India",
        "ingredients": {"egg", "onion", "tomato", "oil", "salt"},
        "steps": [
            "Cook chopped onion and tomato in a little oil.",
            "Beat the eggs with salt and pour them into the pan.",
            "Stir until the eggs are fully cooked.",
        ],
    },
    {
        "name": "Dal Khichdi",
        "region": "Popular across India",
        "ingredients": {"rice", "moong dal", "turmeric", "salt"},
        "steps": [
            "Rinse the rice and moong dal.",
            "Cook them together with turmeric, salt, and water until soft.",
            "Add more hot water if you prefer a softer khichdi.",
        ],
    },
    {
        "name": "Chana Salad",
        "region": "Popular across India",
        "ingredients": {"chickpeas", "onion", "tomato", "lemon", "salt"},
        "steps": [
            "Use cooked chickpeas and let them cool.",
            "Mix with chopped onion and tomato.",
            "Add lemon juice and salt, then mix well.",
        ],
    },
]


def get_user_ingredients():
    """Read comma-separated ingredients and return a set of words."""
    answer = input("Enter ingredients you have, separated by commas: ")
    ingredients = set()

    for item in answer.split(","):
        cleaned_item = item.strip().lower()
        if cleaned_item:
            ingredients.add(cleaned_item)

    return ingredients


def show_suggestions(user_ingredients):
    """Print recipes ordered by how many ingredients are missing."""
    matches = []

    for recipe in recipes:
        shared_ingredients = user_ingredients & recipe["ingredients"]
        missing_ingredients = recipe["ingredients"] - user_ingredients

        # Only show dishes that use at least one ingredient the user has.
        if shared_ingredients:
            matches.append((recipe, shared_ingredients, missing_ingredients))

    # Fewer missing ingredients comes first; ties show more matching items first.
    matches.sort(key=lambda match: (len(match[2]), -len(match[1])))

    if not matches:
        print("\nI could not find a recipe using those ingredients yet.")
        print("Try common items like rice, onion, tomato, potato, or egg.")
        return

    print("\nHere are some ideas:")
    for recipe, shared, missing in matches:
        print(f"\n{recipe['name']} ({recipe['region']})")
        print(f"  You have: {', '.join(sorted(shared))}")

        if missing:
            print(f"  Still needed: {', '.join(sorted(missing))}")
        else:
            print("  You have everything in this starter recipe!")

        print("  Steps:")
        for number, step in enumerate(recipe["steps"], start=1):
            print(f"    {number}. {step}")


def main():
    print("Welcome to the What Can I Make? Pantry Helper!")
    print("This is a small starter collection of Indian meal ideas.")
    user_ingredients = get_user_ingredients()

    if not user_ingredients:
        print("Please enter at least one ingredient next time.")
        return

    show_suggestions(user_ingredients)


if __name__ == "__main__":
    main()
