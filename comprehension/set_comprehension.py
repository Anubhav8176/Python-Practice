favourite_chais = [
    "Masala chai", "Green Tea", "Masala chai",
    "Lemon Tea", "Green Tea", "Elaichi chai"    
]

unique_chai = {chai for chai in favourite_chais}

# print(unique_chai)

recipes = {
    "Masala chai": ["ginger", "cardamom", "clove"],
    "Elaichi chai": ["cardamom", "milk"],
    "Spicy chai": ["ginger", "black pepper", "clove"]
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)