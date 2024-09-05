import random

subjects = ["The dog", "The cat", "My friend"]
verbs = ["bites", "runs towards", "jumps over"]
objects = ["the burger", "the wall", "the bike"]

print("Here is your story:")
for _ in range(5):
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    obj = random.choice(objects)
    
    # Ensure the sentence has correct spacing and punctuation
    print(f"{subject} {verb} {obj}.")
