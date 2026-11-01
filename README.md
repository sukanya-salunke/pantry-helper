# What Can I Make? Pantry Helper

A small beginner Python project that suggests Indian dishes using ingredients you already have.

## What it does

- Accepts a comma-separated list of ingredients.
- Finds starter recipes that use at least one ingredient you entered.
- Sorts recipes with fewer missing ingredients first.
- Shows the matching ingredients, missing ingredients, and simple steps.

The recipe list is intentionally small and uses basic Python data structures. Recipe suggestions are ideas, not dietary or food-safety advice. Check that food is safe to eat and cook ingredients fully.

## Run it

You need Python 3 installed. Open a terminal in this folder and run:

```bash
python pantry_helper.py
```

On this Windows setup, the Python launcher aliases are unavailable, so run the installed interpreter directly in PowerShell:

```powershell
& "$env:LOCALAPPDATA\Python\pythoncore-3.14-64\python.exe" pantry_helper.py
```

Example input:

```text
rice, onion, tomato
```

## Ingredients to try

`rice`, `onion`, `tomato`, `potato`, `cumin`, `poha`, `peanuts`, `turmeric`, `egg`, `moong dal`, `chickpeas`, and `lemon`.

## Ideas for future improvements

- Add more dishes from different Indian regions.
- Let the user choose vegetarian or egg recipes.
- Save favorite recipes to a file.
- Add ingredient aliases, such as `chana` for `chickpeas`.
- Add a simple menu so the user can try again without restarting.

## What I learned

This project practices variables, strings, lists, dictionaries, sets, loops, functions, sorting, and user input.
