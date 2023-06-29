import argparse
import sys
import random

def print_welcome():
  print(
    """
***********************************************************************************************************    
  
               _                                         _______                          _______ _______ 
              | |                            _          (_______)                        (_______|_______)
   _ _ _ _____| | ____ ___  ____  _____    _| |_ ___     _   ___ _   _ _____  ___  ___    _  _  _ _____   
  | | | | ___ | |/ ___) _ \|    \| ___ |  (_   _) _ \   | | (_  | | | | ___ |/___)/___)  | ||_|| |  ___)  
  | | | | ____| ( (__| |_| | | | | ____|    | || |_| |  | |___) | |_| | ____|___ |___ |  | |   | | |_____ 
   \___/|_____)\_)____)___/|_|_|_|_____)     \__)___/    \_____/|____/|_____|___/(___/   |_|   |_|_______)
                                                                                                          
***********************************************************************************************************
    """
  )



def build_num(n_digits):
  list_digits = ["0","1","2","3","4","5","6","7","8","9"]
  random.shuffle(list_digits)
  return list_digits[:n_digits]

def give_clue(chance_num, num):
  correct_nums = len(set(chance_num).intersection(set(num)))
  correct_pos = sum([1 for i in range(len(chance_num))
                     if chance_num[i] == num[i]])
  print("~~~Clue~~~")
  print("Correct digits: {}".format(correct_nums))
  print("Correct Positions: {}".format(correct_pos))
  print("".join(["*"]*50))


def main(digits, chances):
  while True:
    print_welcome()
    number = build_num(digits)
    print("You have {} chances to guess the {} digit number".format(
      chances, digits))
    print("Hint: The digits are unique in the number")
    chance = 0
    won = False
    print("".join(["*"] * 50))
    while chance < chances:
      chance += 1
      last_chance = "[Last Chance]" if chance == chances else ""
      print("Enter your {} digit guess [Chance: {}]{}".format(
        digits, chance, last_chance))
      chance_num = input(">>> ")
      chance_num = [i for i in chance_num]
      if not set(chance_num).issubset(
          {'0','1','2','3','4','5','6','7','8','9'}):
        print("Please enter only numbers", file=sys.stderr)
        print("".join(["*"] * 50))
        continue
      if len(chance_num) != digits:
        print("Please enter {} digit number".format(digits), file=sys.stderr)
        print("".join(["*"] * 50))
        continue
      if chance_num == number:
        won = True
        print("You won .. You won !!!")
        print("".join(["*"] * 50))
        break
      give_clue(chance_num, number)

    if not won:
      print("You are out of chances !! Better Luck Next Time")
      print("The correct answer is {}".format("".join(number)))

    while True:
      exit_check = input("Do you want to continue? Yes or No ?\n>>> ")
      if exit_check.lower() == "no":
        print("Good Bye!!!")
        sys.exit()
      if exit_check.lower() == "yes":
        print("\n\n\n")
        break





if __name__ == "__main__":
  arg_parser = argparse.ArgumentParser(description="Guess Me game")
  arg_parser.add_argument("--game_digits", type=int, default=4,
                        help="Number of digits to be guessed(Max 10)")
  arg_parser.add_argument("--game_chances", type=int, default=10,
                        help="Number of changes for the user")
  args = arg_parser.parse_args()
  game_digits, game_chances = min(10, args.game_digits), args.game_chances
  main(game_digits, game_chances)