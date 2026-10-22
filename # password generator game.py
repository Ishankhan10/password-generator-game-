# password generator game 
import random
print("Welcome to the Password Generator Game !")
print("1. Letters only")
print("2. Letters and numbers")
print("3. Letters, numbers and symbols")
length = int(input("enter length of password:"))
password = ""
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

choice = input("Choose password type (1/2/3): ")
if choice == "1":
    characters = letters
    print("password is weak")
    strength = "Weak"
elif choice == "2":
    characters = letters + numbers
    print("password is medium")
    strength = "Medium"
elif choice == "3":
    characters = letters + numbers + symbols
    print("password is strong")
    strength = "Strong"
else:
    print("Invalid choice. Please select 1, 2, or 3.")
for i in range(length):
  password = password + random.choice(characters)
print("Your password is:", password)
print("Password strength:", strength)

 