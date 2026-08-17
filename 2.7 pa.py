# Amarren Hopkins 8/17/26. This program gives a user a pre determined number that they will try to guess.
# It will tell the user if their guesses are to high or low and after they get it correct
# how many tries it took.
name = input("Enter your name: ")
student_id = input("Enter your Student ID: ")

# Greeting
print("Hello,", name + "!")
print("Welcome to the number guessing game.")

correct_number = 5 # The number needed to be guessed.
tries = 0 # To keep track of attempts

# Loop
while True:
    guess = int(input("Enter a number between 1 and 10: "))
    tries += 1

    if guess > correct_number:
        print("Your guess is too high.")
    elif guess < correct_number:
        print("Your guess is too low.")
    else:
        print("Congratulations! You guessed correctly.")
        print("It took you", tries, "tries.")
        break

# While loop that runs five times
print("\nOutput from the 'while' loop:")

counter = 0

while counter < 5:
    print(counter + 1, "incremented by 1 is", counter + 2)
    counter += 1

# For loop that accomplishes the same thing
print("\nOutput from the 'for' loop:")

for counter in range(5):
    print(counter + 1, "incremented by 1 is", counter + 2)
