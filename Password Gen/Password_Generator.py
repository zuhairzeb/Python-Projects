import string
import random 
all_char = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
lenght = int(input("Enter your password lenght: "))
password = ''.join(random.choice(all_char) for i in range (lenght))
print("Generated password:", password)