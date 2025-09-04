import string
import random
import argparse
import sys


def validateLength(length):
  if type(length) is not int or length == "":
     sys.exit("Please provide a valid length")
             
  if length < 6:
     sys.exit("Length should be >= 6")
   
  

def getAmountForEachCharacters(length): 
  # Special Characters - 15%
  specialCharactersAmount = round(0.15 * length)
  # Numbers - 20%
  numbersAmount = round(0.2 * length)
  # Upper Alphabets - 25%
  upperAlphabetsAmount = round(0.25 * length)
  # Lower Alphabets - 40%
  lowerAlphabetsAmount = round((0.4 * length))
  # Adjust lowerAlphabetsAmount to ensure total length matches
  lowerAlphabetsAmount += length - (specialCharactersAmount + upperAlphabetsAmount +numbersAmount +lowerAlphabetsAmount)

  return [lowerAlphabetsAmount,upperAlphabetsAmount,numbersAmount,specialCharactersAmount]

def pickRandomCharacter(characters):
  return random.choice(characters)

def generatePassword(length):
   validateLength(length)
   
   lowerAlphabets = string.ascii_lowercase
   upperAlphabets = string.ascii_uppercase
   numbers = string.digits 
   specialCharacters = string.punctuation
   lowerAlphabetsAmount ,upperAlphabetsAmount,numbersAmount, specialCharactersAmount = getAmountForEachCharacters(length)
   
   lowerAlphabetsCount, upperAlphabetsCount , numbersCount , specialCharactersCount = 0,0,0,0
   charactersArr = ["lower","upper","number","special"]
   password =""
   for _ in range(length):
     charactersToPickFrom = random.choice(charactersArr)
    #  Lower
     if charactersToPickFrom == "lower":
       lowerAlphabetsCount+=1
       password +=pickRandomCharacter(lowerAlphabets)
       if lowerAlphabetsAmount == lowerAlphabetsCount:
         charactersArr.remove("lower")
    # Upper
     elif charactersToPickFrom == "upper":
       upperAlphabetsCount+=1
       password += pickRandomCharacter(upperAlphabets)
       if upperAlphabetsAmount == upperAlphabetsCount:
         charactersArr.remove("upper")
    # Number
     elif charactersToPickFrom == "number":
       numbersCount+=1
       password +=pickRandomCharacter(numbers)
       if numbersAmount == numbersCount:
        charactersArr.remove("number")
    # Special
     elif charactersToPickFrom == "special":
       specialCharactersCount+=1
       password +=pickRandomCharacter(specialCharacters)
       if specialCharactersAmount == specialCharactersCount:
         charactersArr.remove("special")
 
   return password

 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument("length", type=int, help="Password length (integer >= 6)")
    args = parser.parse_args()
    print(generatePassword(args.length))
