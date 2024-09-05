import random

subject  = ["A dog", "A cat", "My friend"]  
verbs    = ["bites", "runs", "jumps over"]  
objects  = ["a burger", "the wall", "a bike"]  

print("Here is your story:")
for _ in range(5):
    print(random.choice(subject), random.choice(verbs), random.choice(objects) + ".")  
