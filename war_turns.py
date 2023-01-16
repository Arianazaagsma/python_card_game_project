import random
# from war_game import player1, player2


def war(player1_card, player2_card):
    while True:
        player1_card1 = player1.draw.pop(0)
        player1_card2 = player1.draw.pop(0)
        player1_card3 = player1.draw.pop(0)
        player1_card4 = player1.draw.pop(0)
        player1_card5 = player1.draw.pop(0)
        player2_card1 = player2.draw.pop(0)
        player2_card2 = player2.draw.pop(0)
        player2_card3 = player2.draw.pop(0)
        player2_card4 = player2.draw.pop(0)
        player2_card5 = player2.draw.pop(0)
        if player1_card5.value == player2_card5.value:
            print("Your " + player1_card5.name + " ties with the " +
                  player2_card5.name + "! You and the computer enter into another War.")
            war_cards = []
            war_cards.append(player1_card, player1_card1, player1_card2, player1_card3, player1_card4, player1_card5,
                             player2_card, player2_card1, player2_card2, player2_card3, player2_card4, player2_card5)
        elif player1_card5.value > player2_card5.value:
            print("Your " + player1_card5.name +
                  " beats the " + player2_card5.name + "!")
            player1.discard.append(player1_card, player1_card1, player1_card2, player1_card3, player1_card4,
                                   player1_card5, player2_card, player2_card1, player2_card2, player2_card3, player2_card4, player2_card5)
            if war_cards is not None:
                for card in war_cards:
                    player1.discard.append(card)
            break
        elif player1_card.value < player2_card.value:
            print("Your " + player1_card5.name +
                  " loses to the " + player2_card5.name + ".")
            player2.discard.append(player1_card, player1_card1, player1_card2, player1_card3, player1_card4,
                                   player1_card5, player2_card, player2_card1, player2_card2, player2_card3, player2_card4, player2_card5)
            if len(war_cards) != 0:
                for card in war_cards:
                    player2.discard.append(card)
            break


def discard_to_draw(player):
    if player.discard is not None:
        player.draw.append(random.shuffle(player.discard))
    else:
        print(player + " has run out of cards!")
        return False


def war_one_player():
    while True:
        choice = input(
            player1.name + ", select P to play your card or Q to quit the game.")
        if choice.upper() == "P":
            if len(player1.draw) == 0:
                x = discard_to_draw(player1)
                if x == False:
                    print(player2.name + " wins the game!")
            if len(player2.draw) == 0:
                x = discard_to_draw(player2)
                if x == False:
                    print(player1.name + " wins the game!")
            else:
                player1_card = player1.draw.pop(0)
                print("You have played a " + player1_card.name + ".")
                player2_card = player2.draw.pop(0)
                print("The computer has played a " + player2_card.name + ".")
                if player1_card.value > player2_card.value:
                    print("Your " + player1_card.name +
                          " beats the " + player2_card.name + "!")
                    player1.discard.append(player1_card, player2_card)
                    return
                elif player1_card.value < player2_card.value:
                    print("Your " + player1_card.name +
                          " loses to the " + player2_card.name + ".")
                    player2.discard.append(player1_card, player2_card)
                    return
                elif player1_card.value == player2_card.value:
                    print("Your " + player1_card.name + " ties with the " +
                          player2_card.name + "! You and the computer enter into War.")
                    war(player1_card, player2_card)
                    return
        elif choice.upper() == "Q":
            print("Thank you for playing! Your final point total is:", len(
                player1.draw) + len(player1.discard), "- We hope you play again soon!")
            break


def war_two_players():
    while True:
        choice_player1 = input(
            player1.name + ", select P to play your card or Q to quit the game.")
        choice_player2 = input(
            player2.name + "select P to play your card or Q to quit the game.")
        if choice_player1.upper() == "P" and choice_player2.upper() == "P":
            if player1.draw == None:
                x = discard_to_draw(player1)
                if x == False:
                    print(player2.name + " wins the game!")
            if player2.draw == None:
                x = discard_to_draw(player2)
                if x == False:
                    print(player1.name + " wins the game!")
            else:
                player1_card = player1.draw.pop(0)
                print("You have played a " + player1_card.name + ".")
                player2_card = player2.draw.pop(0)
                print("The computer has played a " + player2_card.name + ".")
                if player1_card.value > player2_card.value:
                    print("Your " + player1_card.name +
                          " beats the " + player2_card.name + "!")
                    player1.discard.append(player1_card, player2_card)
                    return
                elif player1_card.value < player2_card.value:
                    print("Your " + player1_card.name +
                          " loses to the " + player2_card.name + ".")
                    player2.discard.append(player1_card, player2_card)
                    return
                elif player1_card.value == player2_card.value:
                    print("Your " + player1_card.name + " ties with the " +
                          player2_card.name + "! You and the computer enter into War.")
                    war(player1_card, player2_card)
                    return
        elif choice_player1.upper() == "Q" or choice_player2.upper() == "Q":
            print("Thank you for playing!\n" + player1.name + "'s final point total is:", len(player1.draw) + len(player1.discard),
                  "\n" + player2.name + "'s final point total is:", len(player2.draw) + len(player2.discard), "\nWe hope you play again soon!")
            break
