# DecodeLabs AI Internship
# Project 3: AI Recommendation Logic
print("=" * 50)
print("🤖 Welcome to the AI Recommendation System")
print("=" * 50)

# Recommendation Database
recommendations = {
    "action": [
        "Avengers",
        "John Wick",
        "Mad Max: Fury Road",
        "Mission Impossible"
    ],
    "comedy": [
        "Mr. Bean",
        "Home Alone",
        "The Mask",
        "Jumanji"
    ],
    "horror": [
        "The Conjuring",
        "Insidious",
        "Annabelle",
        "The Nun"
    ],
    "sci-fi": [
        "Interstellar",
        "Inception",
        "The Matrix",
        "Avatar"
    ],
    "romance": [
        "Titanic",
        "The Notebook",
        "La La Land",
        "Me Before You"
    ]
}

print("\nAvailable Categories:")
for category in recommendations:
    print("-", category.title())

# Take User Input
user_interest = input("\nEnter your favorite category: ").lower().strip()

# Recommendation Logic
if user_interest in recommendations:

    print("\n Recommended Movies For You:\n")

    for movie in recommendations[user_interest]:
        print("-", movie)

else:
    print("\n Category not found.")
    print("Please choose from the available categories.")

print("\nThank you for using the AI Recommendation System!")