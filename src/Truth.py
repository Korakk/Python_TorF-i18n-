#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint
import gettext

''' Si m'ho guarda amb diccionaris, no podia traduir-ho o almenys no sabia com fer-ho,
per aixo he optat per la forma "guarra" de fer-ho.

questions= {
  1:"How many legs does a crab have?",
  2:"Is John/Jane Doe real?",
  3:"Tabs or spaces, how do you indent your code?",
  4:"How many pokémons appear on the classic 1st gen pokedex?",
  5:"Is chess a recognized sport?",
}
answers= {
  1: "8",
  2: "no",
  3: "spaces",
  4: "151",
  5: "yes",
}
'''

def questions(rnd_number):
  if rnd_number == 1 :
    print(_("How many legs does a crab have?"))
  elif rnd_number == 2 :
    print(_("Is John/Jane Doe real?"))
  elif rnd_number == 3 :
    print(_("Tabs or spaces, how do you indent your code?"))
  elif rnd_number == 4 :
    print(_("How many pokémons appear on the classic 1st gen pokedex?"))
  else:
    print(_("Is chess a recognized sport?"))

def answers(rnd_number):
  if rnd_number == 1 :
    return _("8")
  elif rnd_number == 2 :
    return _("no").lower()
  elif rnd_number == 3 :
    return _("spaces").lower
  elif rnd_number == 4 :
    return _("151")
  else:
    return _("yes")

def questionAsker():
  questionN = 1
 
  while questionN < 6:
    rnd = randint(1,5)

    print(_("Question number"),questionN, ":")
    questions(rnd)
    user_answer = input();
    correct_answers = answers(rnd)
    if correct_answers == user_answer.lower():
      print (_("Your answer is correct!") , questionN/5, "!!")
    else:
      print(_("You failed. Restart the game and try again! See you later."))
      exit(0)

    questionN+=1
  

def dataAsker():
    username = input(_("Hi, what's your username?"))
    print (_("Hello ") + username)
    start = input(_("Do you want to start playing the game? (y/n)"))
    if start.lower() == "n":
      exit(0)
    while start.lower() != "y" and start.lower() != "n":
        start = input(_("Please input y(yes) or n(no)! Come on is not that hard [y/n]"))
    print (start)
    print(_("Answer correctly 5/5 questions to WIN!"))
    print(_("Answer questions in one word, let's begin"))



if __name__ == '__main__':
  gettext.install(domain='truth', localedir='locale')
  print("------------------------------------------------------------------------------------------------\n")
  print('''
    __ __ __                                  _ _ _ _            _
   |__    __|                               /   ___   \         |_|  _ __ __
      |  | ______   _    _  _____  _   _   |   |   |   | _    _  _  | _ __  |
      |  || |__| | | |  | ||_   _|| |_| |  |   |   |   || |  | || |     /  /
      |  ||     |  | |__| |  | |  |  _  |  |   |___|   || |__| || |   /  /__
      |__||__|\__\ |__ _ _|  |_|  |_| |_|   \ _ _\ \_ / |__ _ _||_| /__ __ _|   
                                                  \_\              
               
          ''')
  print("------------------------------------------------------------------------------------------------\n")
  dataAsker();
  questionAsker();
  print(_("You WIN!"))
  exit(0);