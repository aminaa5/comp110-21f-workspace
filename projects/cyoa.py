"""Create your own adventure program!"""


__author__ = "730398576"


points: int = 0
player: str
q1: int
q2: int
q3: int
emoji: str = '\U0001F970'


def main() -> None:
    """MAIN!"""
    greet()
    question_1()
    question_2()
    question_3()
    score()


def greet() -> None:
    """Greet the player, be nice!!"""
    global player
    player = str(input("What is your name? "))
    print("Welcome to the quiz where you find out the zodiac sign of your soulmate!!")
    print(F"{player}, pick a number / answer choice for each question and you'll reveal the love of your life!")


def question_1() -> None:
    """The very first question of the quiz."""
    global player
    global points
    global q1
    print("(Q1) What do you like to do in your freetime? ")
    q1 = int(input("1. Jumping jacks, 2. Coding in python :), 3. Frolick in the quad, 4. Eat burritos ")) 
    if q1 == 1:
        points += 1 
    if q1 == 2:
        points += 2
    if q1 == 3:
        points += 3
    if q1 == 4:
        points += 4
    print(F"{player}, you're doing great!!'")
    
    
def question_2() -> None:   
    """Second question of the quiz!"""  
    global player
    global points
    global q2
    print("(Q2) What is your favorite color? ")
    q2 = int(input("1. Purple, 2. Blue, 3. Yellow, 4. Green "))
    if q2 == 1:
        points += 1
    if q2 == 2:
        points += 2
    if q2 == 3:
        points += 3
    if q2 == 4:
        points += 4
    print(F"{player}, look at you go!")
    
    
def question_3() -> None: 
    """Third and last question of the quiz!"""
    global player
    global points    
    global q3
    print("(Q3) Can you touch your tongue to your nose? ")
    q3 = int(input("1. Yes, 2. No, 3. Maybe, 4. Why would you ask me this...? "))
    if q3 == 1:
        points += 1
    if q3 == 2:
        points += 2
    if q3 == 3:
        points += 3
    if q3 == 4:
        points += 4
    print(F"{player}, are you ready for your results??!?!")


def score() -> None:
    """The score determines your soulmates zodiac sign!"""
    global points
    global emoji
    if points <= 4:
        print(F"{emoji} Hooray! Your soulmate is a fire sign: Aries, Leo, or Sagittarius!")
    if points >= 5 and points <= 7:
        print(F"{emoji} OMG!!! Your soulmate is an earth sign: Taurus, Capricorn, or Virgo!")
    if points >= 8 and points <= 10:
        print(F"{emoji} Geewhiz, your soulmate is a water sign: Cancer, Scorpio, or Pisces!!!")
    if points >= 11 and points <= 12:
        print(F"{emoji} Let's gooooooo! Your soulmate is an air sign: Libra, Aquarius, or Gemini!")


if __name__ == "__main__":
    main()