# Write a Python program that prints out the number of decimal digits of the result of 2 to thepower 9741.

twosbigpower = 2**9741
stringpower = str(twosbigpower)
print(len(stringpower))


# Write a Python program that asks the user to guess an integer between 1 and 15, giving hints your guess is too high or your guess is too low.  After the correct guess, the program prints Congratulations, you guessed my number in x trials! where x is actual number of trials. 

def guessing(num):
  print("I am thinking of a number between 1 and 15.")
  trialsum = 0
  while True:
    guess = int(input("Take a guess:  "))
    trialsum += 1
    if guess == num:
      print("Congratulations, you guessed my number in {} trials!".format(trialsum))
      break
    elif guess > num:
      print("Your guess is too high.")
    else:
      print("Your guess is too low.")

guessing(12)