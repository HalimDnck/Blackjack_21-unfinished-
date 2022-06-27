import random
import sys

import numpy as np
import os
import bcrypt


def login_system():
    pass

def signup_system(username= None, password= None, confirm_password= None):
    username = input("Username: ")
    password = input("Password: ")
    confirm_password = input("Confirm Password: ")

    if len(username) > 5:
        if password == confirm_password:
            if len(password) > 5:
                db= open("database.txt", "r")
                d = []
                for i in db:
                    a,b,c = i.split(",")












def system_start():
    print("Welcome to Blackjack")
    system_answer = input("Login/Signup: ")

    login_answer = ["login", "Login"]
    signup_answer = ["Signup", "Sign up", "signup", "sign up"]

    if system_answer in login_answer:
        login_system()
    elif system_answer in signup_answer:
        login_system()
    else:
        print("Check your answer.")
        system_start()

system_start()


# Blackjack Game
def blackjack():
    cards = {"heart", "diamond", "club", "spade", "ace", "king", "queen", "jack"}

    random_card1 = np.random.choice(len(cards), p=[0.18, 0.18, 0.18, 0.18, 0.07, 0.07, 0.07, 0.07])

    finish = bool()
    hand = int()
    if random_card1 <= 3:
        card1 = random.randint(2,10)
        print(f"1. card {card1}")
    elif random_card1 == 4:
        if hand <= 10:
            card1 = 11
            print(f"1. card {card1}")
        else:
            card1 = 1
            print(f"1. card {card1}")
    else :
        card1 = 10
        print(f"1. card {card1}")


    random_card2 = np.random.choice(len(cards), p=[0.18, 0.18, 0.18, 0.18, 0.07, 0.07, 0.07, 0.07])


    if random_card2 <= 3:
        card2 = random.randint(2,10)
        print(f"2. card {card2}")
    elif random_card2 == 4:
        if hand <= 10:
            card2 = 11
            print(f"2. card {card2}")
        else:
            card2 = 1
            print(f"2. card {card2}")
    else :
        card2 = 10
        print(f"2. card {card2}")

    hand = card1+ card2
    print(f"hand: {hand}")


    hit = {"Hit", "hit", "HIT", "HİT"}
    stand = {"Stand", "stand", "STAND"}

    if hand == 21:
        print("Congrats its 21")
        finish is True
    else:
        answer1 = input("Stand or Hit: ")
        if answer1 in hit:
            random_card3 = np.random.choice(len(cards), p=[0.18, 0.18, 0.18, 0.18, 0.07, 0.07, 0.07, 0.07])


            if random_card3 <= 3:
                card3 = random.randint(2, 10)
                print(f"3. card {card3}")
            elif random_card3 == 4:
                if hand <= 10:
                    card3 = 11
                    print(f"3. card {card3}")
                else:
                    card3 = 1
                    print(f"3. card {card3}")
            else:
                card3 = 10
                print(f"3. card {card3}")

            hand = card1 + card2 + card3

            if hand == 21:
                print("Congrats its 21")
                finish is True
            elif hand > 21:
                print("You go over 21. Dealer Win.")
            else:
                print(f"Your hand is {hand}")
                answer2 = input("Hit or Stand: ")

                if answer2 in hit:
                    random_card4 = np.random.choice(len(cards), p=[0.18, 0.18, 0.18, 0.18, 0.07, 0.07, 0.07, 0.07])


                    if random_card4 <= 3:
                        card4 = random.randint(2, 10)
                        print(f"4. card {card4}")
                    elif random_card4 == 4:
                        if hand <= 10:
                            card4 = 11
                            print(f"4. card {card4}")
                        else:
                            card4 = 1
                            print(f"4. card {card4}")
                    else:
                        card4 = 10
                        print(f"4. card {card4}")
                    hand = card1 + card2 + card3 + card4

                    if hand == 21:
                        print("Congrats its 21")
                        finish is True
                    elif hand > 21:
                        print("You go over 21. Dealer Win.")
                    else:
                        print(f"Your hand is {hand}")
                        answer3 = input("Hit or Stand: ")
                        if answer3 in hit:
                            random_card5 = np.random.choice(len(cards), p=[0.18, 0.18, 0.18, 0.18, 0.07, 0.07, 0.07, 0.07])


                            if random_card5 <= 3:
                                card5 = random.randint(2, 10)
                                print(f"5. card {card5}")
                            elif random_card5 == 4:
                                if hand <= 10:
                                    card5 = 11
                                    print(f"5. card {card5}")
                                else:
                                    card5 = 1
                                    print(f"5. card {card5}")
                            else:
                                card5 = 10
                                print(f"5. card {card5}")

                            hand = card1 + card2 + card3 + card4 + card5

                            if hand == 21:
                                print("Congrats its 21")
                                finish is True
                            elif hand > 21:
                                print("You go over 21. Dealer Win.")
                            else:
                                print(f"Your hand is {hand}")

                        elif answer3 in stand:
                            print(f"Your hand is {hand}")
                            finish is True

                elif answer2 in stand:
                    print(f"Your hand is {hand}")
                    finish is True

        elif answer1 in stand:
            print(f"Your hand is {hand}")
            finish is True



    dealer_card1 = np.random.choice(len(cards), p=[0.18, 0.18, 0.18, 0.18, 0.07, 0.07, 0.07, 0.07])

    dealer = int()
    if dealer_card1 <= 3:
        dcard1 = random.randint(2,10)

    elif dealer_card1 == 4:
        if dealer <= 10:
            dcard1 = 11
        else:
            dcard1 = 1
    else :
        dcard1 = 10

    print(f"dealer card1 {dcard1}")




    dealer_card2 = np.random.choice(len(cards), p=[0.18, 0.18, 0.18, 0.18, 0.07, 0.07, 0.07, 0.07])
    if dealer_card2 <= 3:
        dcard2 = random.randint(2,10)

    elif dealer_card2 == 4:
        if dealer <= 10:
            dcard2 = 11

        else:
            dcard2 = 1

    else :
        dcard2 = 10

    print(f"dealer card2 {dcard2}")

    dealer = dcard1 + dcard2
    print(f"Dealers hand {dealer}")

    if dealer<=16:
        dealer_card3 = np.random.choice(len(cards), p=[0.18, 0.18, 0.18, 0.18, 0.07, 0.07, 0.07, 0.07])
        if dealer_card3 <= 3:
            dcard3 = random.randint(2, 10)

        elif dealer_card3 == 4:
            if dealer <= 10:
                dcard3 = 11

            else:
                dcard3 = 1

        else:
            dcard3 = 10

        print(f"dealer card3 {dcard3}")

        dealer = dcard1 + dcard2 +dcard3
        print(f"Dealers hand {dealer}")

        if dealer <= 16:
            dealer_card4 = np.random.choice(len(cards), p=[0.18, 0.18, 0.18, 0.18, 0.07, 0.07, 0.07, 0.07])
            if dealer_card4 <= 3:
                dcard4 = random.randint(2, 10)

            elif dealer_card4 == 4:
                if dealer <= 10:
                    dcard4 = 11

                else:
                    dcard4 = 1

            else:
                dcard4 = 10

            print(f"dealer card4 {dcard4}")

            dealer = dcard1 + dcard2 + dcard3 + dcard4
            print(f"Dealers hand {dealer}")


            if dealer <= 16:
                dealer_card5 = np.random.choice(len(cards), p=[0.18, 0.18, 0.18, 0.18, 0.07, 0.07, 0.07, 0.07])
                if dealer_card5 <= 3:
                    dcard5 = random.randint(2, 10)

                elif dealer_card5 == 4:
                    if dealer <= 10:
                        dcard5 = 11

                    else:
                        dcard5 = 1

                else:
                    dcard5 = 10

                print(f"dealer card5 {dcard5}")

                dealer = dcard1 + dcard2 + dcard3 + dcard5
                print(f"Dealers hand {dealer}")




    if dealer > hand:
        print("You lose")
        return blackjack()
    elif dealer== hand:
        print("Equal")
        return blackjack()
    else:
        print("You win")
        return blackjack()



def game_select():
    game_ = input("Select game: ")
    if game_ == "blackjack":
        blackjack()

game_select()

